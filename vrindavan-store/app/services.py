"""Business logic: settings, cart pricing, shipping/COD rules, coupons, orders, stock.
All money is whole rupees. Totals are always recomputed server-side."""
import re
import secrets
import string
from datetime import datetime, timezone

from flask import g

from .db import get_db, q, q1, run

# ---- Settings. Defaults are PILOT HYPOTHESES (see validation files) - all editable in /admin/settings ----
DEFAULT_SETTINGS = {
    "store_name": "VRINDAVAN",
    "legal_name": "",
    "gstin": "",
    "business_address": "",
    "support_email": "",
    "support_phone": "",
    "whatsapp": "",
    "announcement": "",
    "delivery_note": "Delivery time is confirmed for your PIN code after you place the order.",
    "returns_summary": "If a piece arrives damaged, tell us within 48 hours with photos. See the returns policy for details.",
    "free_ship_threshold": "1499",
    "ship_fee_below": "79",
    "heavy_threshold_g": "3000",
    "heavy_surcharge": "0",
    "cod_enabled": "1",
    "cod_fee": "49",
    "cod_max": "3999",
    "online_enabled": "0",
    "demo_banner": "1",
    "reviews_min_to_show_stars": "3",
    "policies_reviewed": "0",
}


def get_settings():
    if "settings" not in g:
        rows = q("SELECT key, value FROM settings")
        d = dict(DEFAULT_SETTINGS)
        d.update({r["key"]: r["value"] for r in rows})
        g.settings = d
    return g.settings


def save_settings(values):
    for k, v in values.items():
        if k in DEFAULT_SETTINGS:
            run("INSERT INTO settings(key,value) VALUES (?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (k, v))
    g.pop("settings", None)


def sint(key, default=0):
    try:
        return int(float(get_settings().get(key, default)))
    except (TypeError, ValueError):
        return default


def sbool(key):
    return get_settings().get(key, "0") in ("1", "true", "True", "on", "yes")


# ---- helpers ----
def inr(n):
    """Indian digit grouping: 1,23,456"""
    if n is None or isinstance(n, str):
        return ""
    try:
        n = int(round(n))
    except TypeError:  # jinja Undefined etc.
        return ""
    sign = "-" if n < 0 else ""
    s = str(abs(n))
    if len(s) <= 3:
        return f"{sign}₹{s}"
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return f"{sign}₹{','.join(parts)},{tail}"


def slugify(text):
    text = re.sub(r"[^a-zA-Z0-9]+", "-", (text or "").lower()).strip("-")
    return text or "item"


def unique_slug(table, base, exclude_id=None):
    slug = slugify(base)
    n = 1
    cand = slug
    while True:
        row = q1(f"SELECT id FROM {table} WHERE slug=?", (cand,))
        if not row or (exclude_id and row["id"] == exclude_id):
            return cand
        n += 1
        cand = f"{slug}-{n}"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


# ---- availability ----
def available_qty(p):
    if not p["track_stock"] or p["allow_backorder"]:
        return 10_000
    return max(p["stock_qty"], 0)


def stock_label(p):
    if not p["track_stock"] or p["allow_backorder"]:
        return "in_stock"
    if p["stock_qty"] <= 0:
        return "out"
    if p["stock_qty"] <= p["low_stock_at"]:
        return "low"
    return "in_stock"


# ---- PIN rules ----
def pin_rules_for(pin):
    """Return (block_all, block_cod, surcharge, notes) from admin-managed prefix rules."""
    block_all = block_cod = False
    surcharge = 0
    notes = []
    if not pin:
        return block_all, block_cod, surcharge, notes
    for r in q("SELECT * FROM pincode_rules"):
        if pin.startswith(r["prefix"]):
            if r["rule"] == "block_all":
                block_all = True
            elif r["rule"] == "block_cod":
                block_cod = True
            elif r["rule"] == "surcharge":
                surcharge = max(surcharge, r["surcharge"])
            if r["note"]:
                notes.append(r["note"])
    return block_all, block_cod, surcharge, notes


# ---- cart ----
def cart_items(cart):
    """cart: dict[str product_id] -> qty. Returns (lines, problems)."""
    lines, problems = [], []
    for pid, qty in list(cart.items()):
        try:
            pid_i, qty_i = int(pid), int(qty)
        except (TypeError, ValueError):
            continue
        p = q1("SELECT * FROM products WHERE id=? AND is_active=1", (pid_i,))
        if not p:
            problems.append("An item in your cart is no longer available and was removed.")
            cart.pop(pid, None)
            continue
        avail = available_qty(p)
        if avail <= 0:
            problems.append(f"“{p['title']}” is out of stock and was removed.")
            cart.pop(pid, None)
            continue
        if qty_i > avail:
            problems.append(f"Only {avail} of “{p['title']}” available — quantity adjusted.")
            qty_i = avail
            cart[pid] = avail
        qty_i = max(1, min(qty_i, 10))
        im = q1("SELECT base FROM product_images WHERE product_id=? ORDER BY sort_order, id LIMIT 1", (p["id"],))
        lines.append({"product": p, "qty": qty_i, "line_total": p["price"] * qty_i, "img": im["base"] if im else None})
    return lines, problems


def compute_totals(lines, coupon_code=None, payment_method="cod", pincode=None):
    s = get_settings()
    subtotal = sum(l["line_total"] for l in lines)
    discount, coupon_error, coupon = 0, None, None
    if coupon_code:
        discount, coupon_error, coupon = evaluate_coupon(coupon_code, subtotal, payment_method)
    after = max(subtotal - discount, 0)
    shipping = 0
    block_all, block_cod, pin_surcharge, notes = pin_rules_for(pincode)
    if after > 0 and after < sint("free_ship_threshold", 1499):
        shipping = sint("ship_fee_below", 79)
    heavy_g = sint("heavy_threshold_g", 3000)
    if any((l["product"]["weight_g"] or 0) >= heavy_g > 0 for l in lines):
        shipping += sint("heavy_surcharge", 0)
    shipping += pin_surcharge
    cod_ok, cod_reason = cod_eligibility(lines, after + shipping, pincode, block_cod)
    cod_fee = sint("cod_fee", 0) if payment_method == "cod" and cod_ok else 0
    total = after + shipping + cod_fee
    return {
        "subtotal": subtotal, "discount": discount, "shipping": shipping, "cod_fee": cod_fee, "total": total,
        "coupon": coupon, "coupon_error": coupon_error, "cod_ok": cod_ok, "cod_reason": cod_reason,
        "block_all": block_all, "pin_notes": notes,
        "free_ship_gap": max(sint("free_ship_threshold", 1499) - after, 0) if after > 0 else 0,
    }


def cod_eligibility(lines, payable_before_cod, pincode, pin_block_cod=False):
    if not sbool("cod_enabled"):
        return False, "Cash on delivery is not available right now."
    if any(not l["product"]["allow_cod"] for l in lines):
        return False, "Cash on delivery is not available for one or more items in your cart."
    if pin_block_cod:
        return False, "Cash on delivery is not available for this PIN code."
    cap = sint("cod_max", 0)
    if cap and payable_before_cod > cap:
        return False, f"Cash on delivery is available for orders up to {inr(cap)}. Please pay online for larger orders."
    return True, ""


# ---- coupons ----
def evaluate_coupon(code, subtotal, payment_method):
    c = q1("SELECT * FROM coupons WHERE code=? AND is_active=1", ((code or "").strip(),))
    if not c:
        return 0, "That coupon code is not valid.", None
    if c["expires_at"] and c["expires_at"] < now_iso():
        return 0, "That coupon has expired.", None
    if c["max_uses"] is not None and c["used_count"] >= c["max_uses"]:
        return 0, "That coupon has reached its usage limit.", None
    if subtotal < c["min_subtotal"]:
        return 0, f"This coupon needs a minimum order of {inr(c['min_subtotal'])}.", None
    if c["prepaid_only"] and payment_method != "online":
        return 0, "This coupon is valid for online payment only.", None
    disc = subtotal * c["value"] // 100 if c["kind"] == "percent" else c["value"]
    disc = min(disc, subtotal)
    return int(disc), None, c


# ---- orders ----
def new_order_no():
    alphabet = string.ascii_uppercase + string.digits
    for _ in range(20):
        no = "VR" + datetime.now().strftime("%y%m%d") + "".join(secrets.choice(alphabet) for _ in range(4))
        if not q1("SELECT 1 FROM orders WHERE order_no=?", (no,)):
            return no
    raise RuntimeError("could not allocate order number")


class OrderError(Exception):
    pass


def create_order(user, form, cart, ip):
    """Atomic: validates stock, recomputes totals, decrements stock, writes order. Returns order row."""
    db = get_db()
    payment_method = form["payment_method"]
    if payment_method == "online" and not sbool("online_enabled"):
        raise OrderError("Online payment is not available yet. Please choose cash on delivery.")
    db.execute("BEGIN IMMEDIATE")
    try:
        lines, problems = cart_items(dict(cart))
        if problems and not lines:
            raise OrderError("Your cart is empty or items are unavailable.")
        if not lines:
            raise OrderError("Your cart is empty.")
        # re-check stock inside the write lock
        for l in lines:
            p = q1("SELECT * FROM products WHERE id=? AND is_active=1", (l["product"]["id"],))
            if not p or l["qty"] > available_qty(p):
                raise OrderError(f"“{l['product']['title']}” is no longer available in the requested quantity.")
            l["product"] = p
        t = compute_totals(lines, form.get("coupon_code") or None, payment_method, form["pincode"])
        if t["block_all"]:
            raise OrderError("We are not able to deliver to this PIN code yet.")
        if payment_method == "cod" and not t["cod_ok"]:
            raise OrderError(t["cod_reason"] or "Cash on delivery is not available for this order.")
        if form.get("coupon_code") and t["coupon_error"]:
            raise OrderError(t["coupon_error"])
        order_no = new_order_no()
        cur = db.execute(
            """INSERT INTO orders(order_no,user_id,email,phone,customer_name,ship_name,ship_phone,ship_line1,ship_line2,ship_landmark,
               ship_city,ship_state,ship_pincode,subtotal,discount,shipping_fee,cod_fee,total,coupon_code,payment_method,payment_status,
               status,customer_note,ip) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (order_no, user["id"] if user else None, form["email"], form["phone"], form["name"], form["name"], form["phone"],
             form["line1"], form.get("line2") or None, form.get("landmark") or None, form["city"], form["state"], form["pincode"],
             t["subtotal"], t["discount"], t["shipping"], t["cod_fee"], t["total"],
             t["coupon"]["code"] if t["coupon"] else None, payment_method, "pending", "pending",
             (form.get("customer_note") or None), ip),
        )
        oid = cur.lastrowid
        for l in lines:
            p = l["product"]
            img = q1("SELECT base FROM product_images WHERE product_id=? ORDER BY sort_order, id LIMIT 1", (p["id"],))
            db.execute(
                """INSERT INTO order_items(order_id,product_id,title,slug,image_base,unit_price,qty,line_total,cost_snapshot,hsn_snapshot,gst_snapshot)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                (oid, p["id"], p["title"], p["slug"], img["base"] if img else None, p["price"], l["qty"], l["line_total"],
                 p["cost_price"], p["hsn_code"], p["gst_rate"]),
            )
            if p["track_stock"] and not p["allow_backorder"]:
                res = db.execute("UPDATE products SET stock_qty = stock_qty - ?, updated_at=datetime('now') WHERE id=? AND stock_qty >= ?",
                                 (l["qty"], p["id"], l["qty"]))
                if res.rowcount != 1:
                    raise OrderError(f"“{p['title']}” just sold out. Please review your cart.")
            elif p["track_stock"]:
                db.execute("UPDATE products SET stock_qty = stock_qty - ? WHERE id=?", (l["qty"], p["id"]))
            db.execute("INSERT INTO stock_movements(product_id,delta,reason,order_id,user_id) VALUES (?,?,?,?,?)",
                       (p["id"], -l["qty"], "order", oid, user["id"] if user else None))
        if t["coupon"]:
            res = db.execute("UPDATE coupons SET used_count=used_count+1 WHERE id=? AND (max_uses IS NULL OR used_count < max_uses)", (t["coupon"]["id"],))
            if res.rowcount != 1:
                raise OrderError("That coupon has just reached its usage limit.")
        db.execute("INSERT INTO order_events(order_id,status,note,actor_user_id) VALUES (?,?,?,?)",
                   (oid, "pending", "Order placed", user["id"] if user else None))
        body = (f"Thank you for your order {order_no}.\nTotal: {inr(t['total'])} ({'Cash on delivery' if payment_method == 'cod' else 'Online payment'}).\n"
                f"We will confirm your order shortly. {get_settings()['delivery_note']}")
        db.execute("INSERT INTO outbox(to_email,subject,body,kind) VALUES (?,?,?,?)",
                   (form["email"], f"Order {order_no} received", body, "order_placed"))
        db.execute("COMMIT")
    except Exception:
        db.execute("ROLLBACK")
        raise
    return q1("SELECT * FROM orders WHERE id=?", (oid,))


ORDER_FLOW = {
    "pending": ["confirmed", "cancelled"],
    "confirmed": ["packed", "cancelled"],
    "packed": ["shipped", "cancelled"],
    "shipped": ["delivered", "rto", "cancelled"],
    "delivered": ["returned"],
    "rto": ["returned"],
    "cancelled": [],
    "returned": [],
}


def change_order_status(order, new_status, actor_id, note=None, restock=False):
    allowed = ORDER_FLOW.get(order["status"], [])
    if new_status not in allowed:
        raise OrderError(f"Cannot move an order from {order['status']} to {new_status}.")
    db = get_db()
    db.execute("BEGIN IMMEDIATE")
    try:
        if new_status == "cancelled":
            restock = True  # cancelling always returns stock unless it already shipped (admin can adjust manually)
            if order["status"] == "shipped":
                restock = False
        if restock:
            for it in q("SELECT * FROM order_items WHERE order_id=?", (order["id"],)):
                if it["product_id"]:
                    p = q1("SELECT track_stock FROM products WHERE id=?", (it["product_id"],))
                    if p and p["track_stock"]:
                        db.execute("UPDATE products SET stock_qty = stock_qty + ? WHERE id=?", (it["qty"], it["product_id"]))
                        db.execute("INSERT INTO stock_movements(product_id,delta,reason,order_id,user_id) VALUES (?,?,?,?,?)",
                                   (it["product_id"], it["qty"], f"restock:{new_status}", order["id"], actor_id))
        pay_status = order["payment_status"]
        if new_status == "delivered" and order["payment_method"] == "cod":
            pay_status = "paid"
        if new_status == "cancelled" and order["payment_status"] == "paid":
            pay_status = "refunded"
        db.execute("UPDATE orders SET status=?, payment_status=?, updated_at=datetime('now') WHERE id=?", (new_status, pay_status, order["id"]))
        db.execute("INSERT INTO order_events(order_id,status,note,actor_user_id) VALUES (?,?,?,?)", (order["id"], new_status, note, actor_id))
        if new_status in ("confirmed", "shipped", "delivered", "cancelled"):
            db.execute("INSERT INTO outbox(to_email,subject,body,kind) VALUES (?,?,?,?)",
                       (order["email"], f"Order {order['order_no']} — {new_status}", f"Your order {order['order_no']} is now {new_status}." + (f"\nTracking: {order['courier'] or ''} {order['awb'] or ''}" if new_status == "shipped" else ""), "order_status"))
        db.execute("COMMIT")
    except Exception:
        db.execute("ROLLBACK")
        raise


def adjust_stock(product_id, delta, reason, user_id):
    db = get_db()
    db.execute("BEGIN IMMEDIATE")
    try:
        res = db.execute("UPDATE products SET stock_qty = stock_qty + ?, updated_at=datetime('now') WHERE id=? AND stock_qty + ? >= 0", (delta, product_id, delta))
        if res.rowcount != 1:
            raise OrderError("Stock cannot go below zero.")
        db.execute("INSERT INTO stock_movements(product_id,delta,reason,user_id) VALUES (?,?,?,?)", (product_id, delta, reason, user_id))
        db.execute("COMMIT")
    except Exception:
        db.execute("ROLLBACK")
        raise


# ---- ratings ----
def rating_summary(product_id):
    r = q1("SELECT COUNT(*) c, AVG(rating) a FROM reviews WHERE product_id=? AND status='approved'", (product_id,))
    return (r["c"], round(r["a"], 1) if r["c"] else None)


def apply_wishlist_merge(user_id, session_ids):
    for pid in session_ids or []:
        try:
            run("INSERT OR IGNORE INTO wishlist(user_id, product_id) VALUES (?,?)", (user_id, int(pid)))
        except Exception:
            pass
