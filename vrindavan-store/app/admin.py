"""Admin panel. Permissions: staff = products/orders/inventory/reviews/messages; admin = everything."""
from flask import (Blueprint, abort, current_app, flash, g, jsonify, redirect, render_template, request, url_for)

from .db import get_db, q, q1, run
from .images import ImageError, delete_image_files, save_product_image
from .security import (EMAIL_RE, PHONE_RE, hash_password, log_audit, password_problem, perm_required)
from .services import (DEFAULT_SETTINGS, ORDER_FLOW, OrderError, adjust_stock, change_order_status, get_settings, inr, save_settings, slugify, unique_slug)

bp = Blueprint("admin", __name__)

ORDER_STATUSES = ["pending", "confirmed", "packed", "shipped", "delivered", "cancelled", "rto", "returned"]


def _int(v, default=None):
    try:
        return int(float(str(v).strip()))
    except (TypeError, ValueError):
        return default


def _float(v):
    try:
        s = str(v).strip()
        return float(s) if s else None
    except ValueError:
        return None


# ------------------------------------------------------------------ dashboard
@bp.route("/")
@perm_required("admin.access")
def dashboard():
    by_status = {r["status"]: r["c"] for r in q("SELECT status, COUNT(*) c FROM orders GROUP BY status")}
    revenue = q1("SELECT COALESCE(SUM(total),0) s, COUNT(*) c FROM orders WHERE status NOT IN ('cancelled','rto','returned')")
    last30 = q1("SELECT COALESCE(SUM(total),0) s, COUNT(*) c FROM orders WHERE status NOT IN ('cancelled','rto','returned') AND created_at >= datetime('now','-30 day')")
    cod_share = q1("SELECT SUM(CASE WHEN payment_method='cod' THEN 1 ELSE 0 END) cod, COUNT(*) n FROM orders")
    shipped = (by_status.get("delivered", 0) + by_status.get("rto", 0))
    rto_rate = round(100 * by_status.get("rto", 0) / shipped, 1) if shipped else None
    low = q("SELECT * FROM products WHERE track_stock=1 AND is_active=1 AND stock_qty <= low_stock_at ORDER BY stock_qty LIMIT 10")
    pending_reviews = q1("SELECT COUNT(*) c FROM reviews WHERE status='pending'")["c"]
    new_msgs = q1("SELECT COUNT(*) c FROM contact_messages WHERE handled=0")["c"]
    recent = q("SELECT * FROM orders ORDER BY created_at DESC LIMIT 8")
    top = q("""SELECT i.title, SUM(i.qty) units, SUM(i.line_total) rev FROM order_items i JOIN orders o ON o.id=i.order_id
               WHERE o.status NOT IN ('cancelled','rto','returned') GROUP BY i.title ORDER BY units DESC LIMIT 5""")
    margin = q1("""SELECT SUM(i.line_total) rev, SUM(i.cost_snapshot * i.qty) cost FROM order_items i JOIN orders o ON o.id=i.order_id
                   WHERE o.status NOT IN ('cancelled','rto','returned') AND i.cost_snapshot IS NOT NULL""")
    return render_template("admin/dashboard.html", by_status=by_status, revenue=revenue, last30=last30, cod_share=cod_share, rto_rate=rto_rate,
                           low=low, pending_reviews=pending_reviews, new_msgs=new_msgs, recent=recent, top=top, margin=margin)


# ------------------------------------------------------------------ products
@bp.route("/products")
@perm_required("products.view")
def products():
    term = (request.args.get("q") or "").strip()
    flt = request.args.get("filter", "")
    where, args = ["1=1"], []
    if term:
        where.append("(p.title LIKE ? OR p.slug LIKE ? OR p.supplier_name LIKE ?)")
        args += [f"%{term}%"] * 3
    if flt == "low":
        where.append("p.track_stock=1 AND p.stock_qty <= p.low_stock_at")
    elif flt == "inactive":
        where.append("p.is_active=0")
    elif flt == "demo":
        where.append("p.is_demo=1")
    rows = q(f"""SELECT p.*, (SELECT base FROM product_images WHERE product_id=p.id ORDER BY sort_order,id LIMIT 1) img
                 FROM products p WHERE {' AND '.join(where)} ORDER BY p.updated_at DESC""", args)
    return render_template("admin/products.html", products=rows, term=term, flt=flt)


def _product_form_values():
    f = request.form
    v = {
        "title": (f.get("title") or "").strip(),
        "subtitle": (f.get("subtitle") or "").strip() or None,
        "description": (f.get("description") or "").strip() or None,
        "story": (f.get("story") or "").strip() or None,
        "care": (f.get("care") or "").strip() or None,
        "material": (f.get("material") or "").strip() or None,
        "finish": (f.get("finish") or "").strip() or None,
        "height_cm": _float(f.get("height_cm")), "width_cm": _float(f.get("width_cm")), "depth_cm": _float(f.get("depth_cm")),
        "weight_g": _int(f.get("weight_g")), "packed_weight_g": _int(f.get("packed_weight_g")),
        "base_included": (f.get("base_included") or "").strip() or None,
        "origin_region": (f.get("origin_region") or "").strip() or None,
        "hsn_code": (f.get("hsn_code") or "").strip() or None,
        "gst_rate": _float(f.get("gst_rate")),
        "price": _int(f.get("price")), "compare_at_price": _int(f.get("compare_at_price")), "cost_price": _int(f.get("cost_price")),
        "supplier_name": (f.get("supplier_name") or "").strip() or None, "supplier_sku": (f.get("supplier_sku") or "").strip() or None,
        "low_stock_at": _int(f.get("low_stock_at"), 2),
        "track_stock": 1 if f.get("track_stock") else 0, "allow_backorder": 1 if f.get("allow_backorder") else 0,
        "allow_cod": 1 if f.get("allow_cod") else 0, "fragile": 1 if f.get("fragile") else 0,
        "is_active": 1 if f.get("is_active") else 0, "is_featured": 1 if f.get("is_featured") else 0,
        "measured_by_us": 1 if f.get("measured_by_us") else 0, "photographed_by_us": 1 if f.get("photographed_by_us") else 0,
        "protective_packing": 1 if f.get("protective_packing") else 0,
        "seo_title": (f.get("seo_title") or "").strip() or None, "seo_description": (f.get("seo_description") or "").strip() or None,
    }
    return v


def _validate_product(v, current_id=None):
    errors = {}
    if len(v["title"]) < 3:
        errors["title"] = "Title is required (min 3 characters)."
    if v["price"] is None or v["price"] < 0:
        errors["price"] = "Enter a price in whole rupees."
    if v["compare_at_price"] is not None and v["price"] is not None and v["compare_at_price"] <= v["price"]:
        errors["compare_at_price"] = "Compare-at price must be higher than the price (leave blank unless it is a TRUE previous selling price)."
    if v["gst_rate"] is not None and not (0 <= v["gst_rate"] <= 40):
        errors["gst_rate"] = "GST rate must be between 0 and 40."
    return errors


@bp.route("/products/new", methods=["GET", "POST"])
@bp.route("/products/<int:pid>/edit", methods=["GET", "POST"])
@perm_required("products.edit")
def product_edit(pid=None):
    p = q1("SELECT * FROM products WHERE id=?", (pid,)) if pid else None
    if pid and not p:
        abort(404)
    errors, values = {}, (dict(p) if p else {"is_active": 1, "track_stock": 1, "allow_cod": 1, "low_stock_at": 2, "stock_qty": 0})
    all_cols = q("SELECT * FROM collections ORDER BY kind, sort_order, name")
    selected = {r["collection_id"] for r in q("SELECT collection_id FROM product_collections WHERE product_id=?", (pid,))} if pid else set()
    if request.method == "POST":
        v = _product_form_values()
        errors = _validate_product(v, pid)
        selected = {int(x) for x in request.form.getlist("collections") if x.isdigit()}
        values.update(v)
        if not errors:
            db = get_db()
            if p:
                sets = ", ".join(f"{k}=?" for k in v) + ", slug=?, updated_at=datetime('now')"
                slug = unique_slug("products", request.form.get("slug") or v["title"], exclude_id=pid)
                run(f"UPDATE products SET {sets} WHERE id=?", list(v.values()) + [slug, pid])
                log_audit("product.update", "product", pid, v["title"])
                new_id = pid
            else:
                v["stock_qty"] = 0
                cols = ", ".join(v.keys()) + ", slug"
                ph = ", ".join("?" * (len(v) + 1))
                slug = unique_slug("products", request.form.get("slug") or v["title"])
                cur = run(f"INSERT INTO products({cols}) VALUES ({ph})", list(v.values()) + [slug])
                new_id = cur.lastrowid
                init_stock = _int(request.form.get("initial_stock"), 0) or 0
                if init_stock > 0:
                    adjust_stock(new_id, init_stock, "initial stock", g.user["id"])
                log_audit("product.create", "product", new_id, v["title"])
            run("DELETE FROM product_collections WHERE product_id=?", (new_id,))
            for cid in selected:
                run("INSERT OR IGNORE INTO product_collections(product_id,collection_id) VALUES (?,?)", (new_id, cid))
            files = [f for f in request.files.getlist("images") if f and f.filename]
            for i, f in enumerate(files):
                try:
                    base = save_product_image(f, current_app.config["MEDIA_ROOT"], new_id)
                    n = q1("SELECT COALESCE(MAX(sort_order),-1)+1 n FROM product_images WHERE product_id=?", (new_id,))["n"]
                    run("INSERT INTO product_images(product_id,base,alt,sort_order) VALUES (?,?,?,?)", (new_id, base, v["title"], n))
                except ImageError as e:
                    flash(f"Image '{f.filename}' skipped: {e}", "error")
            flash("Product saved.", "success")
            return redirect(url_for("admin.product_edit", pid=new_id))
        flash("Please fix the highlighted fields.", "error")
    images = q("SELECT * FROM product_images WHERE product_id=? ORDER BY sort_order,id", (pid,)) if pid else []
    movements = q("""SELECT m.*, u.name uname FROM stock_movements m LEFT JOIN users u ON u.id=m.user_id WHERE m.product_id=? ORDER BY m.id DESC LIMIT 15""", (pid,)) if pid else []
    return render_template("admin/product_form.html", p=p, v=values, errors=errors, collections=all_cols, selected=selected, images=images, movements=movements)


@bp.route("/products/<int:pid>/images/<int:iid>", methods=["POST"])
@perm_required("products.edit")
def product_image_action(pid, iid):
    img = q1("SELECT * FROM product_images WHERE id=? AND product_id=?", (iid, pid))
    if not img:
        abort(404)
    action = request.form.get("action")
    if action == "delete":
        run("DELETE FROM product_images WHERE id=?", (iid,))
        if not q1("SELECT 1 FROM product_images WHERE base=?", (img["base"],)):
            delete_image_files(current_app.config["MEDIA_ROOT"], img["base"])
    elif action in ("up", "down", "first"):
        imgs = q("SELECT id FROM product_images WHERE product_id=? ORDER BY sort_order,id", (pid,))
        ids = [r["id"] for r in imgs]
        i = ids.index(iid)
        if action == "first":
            ids.insert(0, ids.pop(i))
        elif action == "up" and i > 0:
            ids[i - 1], ids[i] = ids[i], ids[i - 1]
        elif action == "down" and i < len(ids) - 1:
            ids[i + 1], ids[i] = ids[i], ids[i + 1]
        for n, _id in enumerate(ids):
            run("UPDATE product_images SET sort_order=? WHERE id=?", (n, _id))
    elif action == "alt":
        run("UPDATE product_images SET alt=? WHERE id=?", ((request.form.get("alt") or "").strip()[:200], iid))
    return redirect(url_for("admin.product_edit", pid=pid) + "#images")


@bp.route("/products/<int:pid>/stock", methods=["POST"])
@perm_required("inventory.manage")
def product_stock(pid):
    if not q1("SELECT 1 FROM products WHERE id=?", (pid,)):
        abort(404)
    delta = _int(request.form.get("delta"))
    reason = (request.form.get("reason") or "manual adjustment").strip()[:120]
    if not delta:
        flash("Enter a non-zero quantity to add (positive) or remove (negative).", "error")
    else:
        try:
            adjust_stock(pid, delta, reason, g.user["id"])
            log_audit("stock.adjust", "product", pid, f"{delta:+d} {reason}")
            flash("Stock updated.", "success")
        except OrderError as e:
            flash(str(e), "error")
    return redirect(request.form.get("next") or url_for("admin.product_edit", pid=pid))


@bp.route("/products/<int:pid>/archive", methods=["POST"])
@perm_required("products.edit")
def product_archive(pid):
    p = q1("SELECT * FROM products WHERE id=?", (pid,))
    if not p:
        abort(404)
    run("UPDATE products SET is_active=?, updated_at=datetime('now') WHERE id=?", (0 if p["is_active"] else 1, pid))
    log_audit("product.toggle_active", "product", pid)
    flash("Product hidden from the store." if p["is_active"] else "Product is live again.", "success")
    return redirect(request.referrer or url_for("admin.products"))


@bp.route("/products/<int:pid>/delete", methods=["POST"])
@perm_required("products.delete")
def product_delete(pid):
    p = q1("SELECT * FROM products WHERE id=?", (pid,))
    if not p:
        abort(404)
    for img in q("SELECT base FROM product_images WHERE product_id=?", (pid,)):
        delete_image_files(current_app.config["MEDIA_ROOT"], img["base"])
    run("DELETE FROM products WHERE id=?", (pid,))
    log_audit("product.delete", "product", pid, p["title"])
    flash("Product deleted. Past orders keep their item details.", "success")
    return redirect(url_for("admin.products"))


@bp.route("/products/delete-demo", methods=["POST"])
@perm_required("products.delete")
def delete_demo():
    n = 0
    for p in q("SELECT id FROM products WHERE is_demo=1"):
        for img in q("SELECT base FROM product_images WHERE product_id=?", (p["id"],)):
            delete_image_files(current_app.config["MEDIA_ROOT"], img["base"])
        run("DELETE FROM products WHERE id=?", (p["id"],))
        n += 1
    log_audit("product.delete_demo", detail=str(n))
    flash(f"Removed {n} sample products.", "success")
    return redirect(url_for("admin.products"))


# ------------------------------------------------------------------ inventory
@bp.route("/inventory")
@perm_required("inventory.manage")
def inventory():
    rows = q("""SELECT p.*, (SELECT base FROM product_images WHERE product_id=p.id ORDER BY sort_order,id LIMIT 1) img
                FROM products p ORDER BY (p.track_stock=1 AND p.stock_qty<=p.low_stock_at) DESC, p.stock_qty ASC, p.title""")
    moves = q("""SELECT m.*, p.title, u.name uname FROM stock_movements m JOIN products p ON p.id=m.product_id
                 LEFT JOIN users u ON u.id=m.user_id ORDER BY m.id DESC LIMIT 30""")
    return render_template("admin/inventory.html", products=rows, moves=moves)


# ------------------------------------------------------------------ collections
@bp.route("/collections", methods=["GET", "POST"])
@perm_required("collections.manage")
def collections():
    if request.method == "POST":
        action = request.form.get("action")
        cid = _int(request.form.get("id"))
        if action == "delete" and cid:
            run("DELETE FROM collections WHERE id=?", (cid,))
            flash("Collection deleted.", "success")
        else:
            name = (request.form.get("name") or "").strip()
            kind = request.form.get("kind") if request.form.get("kind") in ("deity", "purpose") else "deity"
            if len(name) < 2:
                flash("Name is required.", "error")
            else:
                vals = (name, (request.form.get("name_native") or "").strip() or None, kind, (request.form.get("description") or "").strip() or None,
                        _int(request.form.get("sort_order"), 0), 1 if request.form.get("is_active") else 0)
                if cid:
                    run("UPDATE collections SET name=?, name_native=?, kind=?, description=?, sort_order=?, is_active=? WHERE id=?", vals + (cid,))
                else:
                    run("INSERT INTO collections(name,name_native,kind,description,sort_order,is_active,slug) VALUES (?,?,?,?,?,?,?)", vals + (unique_slug("collections", name),))
                flash("Collection saved.", "success")
        return redirect(url_for("admin.collections"))
    rows = q("""SELECT c.*, (SELECT COUNT(*) FROM product_collections WHERE collection_id=c.id) n FROM collections c ORDER BY kind, sort_order, name""")
    return render_template("admin/collections.html", collections=rows)


# ------------------------------------------------------------------ orders
@bp.route("/orders")
@perm_required("orders.view")
def orders():
    status = request.args.get("status", "")
    term = (request.args.get("q") or "").strip()
    where, args = ["1=1"], []
    if status in ORDER_STATUSES:
        where.append("status=?")
        args.append(status)
    if request.args.get("pay") in ("cod", "online"):
        where.append("payment_method=?")
        args.append(request.args["pay"])
    if term:
        where.append("(order_no LIKE ? OR email LIKE ? OR phone LIKE ? OR customer_name LIKE ? OR awb LIKE ?)")
        args += [f"%{term}%"] * 5
    rows = q(f"SELECT * FROM orders WHERE {' AND '.join(where)} ORDER BY created_at DESC LIMIT 200", args)
    counts = {r["status"]: r["c"] for r in q("SELECT status, COUNT(*) c FROM orders GROUP BY status")}
    return render_template("admin/orders.html", orders=rows, status=status, term=term, counts=counts, statuses=ORDER_STATUSES)


@bp.route("/orders/<order_no>", methods=["GET", "POST"])
@perm_required("orders.view")
def order_detail(order_no):
    o = q1("SELECT * FROM orders WHERE order_no=?", (order_no,))
    if not o:
        abort(404)
    if request.method == "POST":
        if not g.user or not (g.user["role"] in ("admin", "staff")):
            abort(403)
        action = request.form.get("action")
        if action == "status":
            new = request.form.get("status")
            if new == "shipped" and not ((request.form.get("courier") or o["courier"]) and (request.form.get("awb") or o["awb"])):
                flash("Add the courier and AWB/tracking number before marking as shipped.", "error")
            else:
                if new == "shipped":
                    run("UPDATE orders SET courier=?, awb=?, tracking_url=? WHERE id=?",
                        ((request.form.get("courier") or o["courier"]).strip()[:60], (request.form.get("awb") or o["awb"]).strip()[:60],
                         (request.form.get("tracking_url") or o["tracking_url"] or "").strip()[:300] or None, o["id"]))
                    o = q1("SELECT * FROM orders WHERE id=?", (o["id"],))
                try:
                    change_order_status(o, new, g.user["id"], (request.form.get("note") or "").strip()[:300] or None)
                    log_audit("order.status", "order", o["order_no"], new)
                    flash(f"Order marked {new}.", "success")
                except OrderError as e:
                    flash(str(e), "error")
        elif action == "shipping":
            run("UPDATE orders SET courier=?, awb=?, tracking_url=?, updated_at=datetime('now') WHERE id=?",
                ((request.form.get("courier") or "").strip()[:60] or None, (request.form.get("awb") or "").strip()[:60] or None,
                 (request.form.get("tracking_url") or "").strip()[:300] or None, o["id"]))
            flash("Shipping details saved.", "success")
        elif action == "payment":
            ps = request.form.get("payment_status")
            if ps in ("pending", "paid", "failed", "refunded"):
                run("UPDATE orders SET payment_status=?, updated_at=datetime('now') WHERE id=?", (ps, o["id"]))
                log_audit("order.payment", "order", o["order_no"], ps)
                flash("Payment status updated.", "success")
        elif action == "cod_confirm":
            run("UPDATE orders SET cod_confirmed=? WHERE id=?", (1 if request.form.get("value") == "1" else 0, o["id"]))
            flash("COD confirmation updated.", "success")
        elif action == "note":
            run("UPDATE orders SET internal_note=? WHERE id=?", ((request.form.get("internal_note") or "").strip()[:1000] or None, o["id"]))
            flash("Note saved.", "success")
        return redirect(url_for("admin.order_detail", order_no=order_no))
    items = q("SELECT * FROM order_items WHERE order_id=?", (o["id"],))
    events = q("SELECT e.*, u.name uname FROM order_events e LEFT JOIN users u ON u.id=e.actor_user_id WHERE e.order_id=? ORDER BY e.id", (o["id"],))
    nexts = ORDER_FLOW.get(o["status"], [])
    return render_template("admin/order_detail.html", o=o, items=items, events=events, nexts=nexts)


@bp.route("/orders/<order_no>/receipt")
@perm_required("orders.view")
def order_receipt(order_no):
    o = q1("SELECT * FROM orders WHERE order_no=?", (order_no,))
    if not o:
        abort(404)
    items = q("SELECT * FROM order_items WHERE order_id=?", (o["id"],))
    return render_template("receipt.html", o=o, items=items, admin_view=True)


# ------------------------------------------------------------------ reviews / messages
@bp.route("/reviews", methods=["GET", "POST"])
@perm_required("reviews.moderate")
def reviews():
    if request.method == "POST":
        rid, action = _int(request.form.get("id")), request.form.get("action")
        if action in ("approved", "rejected", "pending") and rid:
            run("UPDATE reviews SET status=? WHERE id=?", (action, rid))
            log_audit("review." + action, "review", rid)
        elif action == "delete" and rid:
            run("DELETE FROM reviews WHERE id=?", (rid,))
        return redirect(url_for("admin.reviews", status=request.args.get("status", "")))
    status = request.args.get("status", "pending")
    rows = q("""SELECT r.*, p.title ptitle, u.name uname, u.email uemail FROM reviews r JOIN products p ON p.id=r.product_id JOIN users u ON u.id=r.user_id
                WHERE (?='' OR r.status=?) ORDER BY r.created_at DESC LIMIT 100""", (status, status))
    return render_template("admin/reviews.html", reviews=rows, status=status)


@bp.route("/messages", methods=["GET", "POST"])
@perm_required("messages.view")
def messages():
    if request.method == "POST":
        mid = _int(request.form.get("id"))
        if mid:
            run("UPDATE contact_messages SET handled=? WHERE id=?", (1 if request.form.get("handled") == "1" else 0, mid))
        return redirect(url_for("admin.messages"))
    rows = q("SELECT * FROM contact_messages ORDER BY handled, created_at DESC LIMIT 100")
    return render_template("admin/messages.html", messages=rows)


# ------------------------------------------------------------------ admin-only
@bp.route("/customers")
@perm_required("customers.view")
def customers():
    term = (request.args.get("q") or "").strip()
    rows = q("""SELECT u.*, (SELECT COUNT(*) FROM orders o WHERE o.user_id=u.id) orders_n,
                       (SELECT COALESCE(SUM(total),0) FROM orders o WHERE o.user_id=u.id AND o.status NOT IN ('cancelled','rto','returned')) spent
                FROM users u WHERE u.role='customer' AND (?='' OR u.email LIKE ? OR u.name LIKE ? OR u.phone LIKE ?) ORDER BY u.created_at DESC LIMIT 200""",
             (term, f"%{term}%", f"%{term}%", f"%{term}%"))
    return render_template("admin/customers.html", customers=rows, term=term)


@bp.route("/customers/<int:uid>/toggle", methods=["POST"])
@perm_required("customers.manage")
def customer_toggle(uid):
    u = q1("SELECT * FROM users WHERE id=? AND role='customer'", (uid,))
    if not u:
        abort(404)
    run("UPDATE users SET is_active=? WHERE id=?", (0 if u["is_active"] else 1, uid))
    log_audit("customer.toggle", "user", uid)
    flash("Account updated.", "success")
    return redirect(url_for("admin.customers"))


@bp.route("/coupons", methods=["GET", "POST"])
@perm_required("coupons.manage")
def coupons():
    if request.method == "POST":
        action = request.form.get("action")
        cid = _int(request.form.get("id"))
        if action == "delete" and cid:
            run("DELETE FROM coupons WHERE id=?", (cid,))
            flash("Coupon deleted.", "success")
        elif action == "toggle" and cid:
            run("UPDATE coupons SET is_active = 1 - is_active WHERE id=?", (cid,))
        else:
            code = (request.form.get("code") or "").strip().upper()
            kind = request.form.get("kind")
            value = _int(request.form.get("value"), 0)
            if not (3 <= len(code) <= 30) or not code.replace("-", "").replace("_", "").isalnum():
                flash("Code must be 3–30 letters/numbers.", "error")
            elif kind not in ("percent", "fixed") or value <= 0 or (kind == "percent" and value > 90):
                flash("Enter a valid value (percent up to 90, or a fixed rupee amount).", "error")
            elif q1("SELECT 1 FROM coupons WHERE code=?", (code,)):
                flash("That code already exists.", "error")
            else:
                run("INSERT INTO coupons(code,kind,value,min_subtotal,max_uses,expires_at,prepaid_only) VALUES (?,?,?,?,?,?,?)",
                    (code, kind, value, _int(request.form.get("min_subtotal"), 0), _int(request.form.get("max_uses")),
                     ((request.form.get("expires_at") or "").strip() + " 23:59:59") if request.form.get("expires_at") else None,
                     1 if request.form.get("prepaid_only") else 0))
                log_audit("coupon.create", "coupon", code)
                flash("Coupon created.", "success")
        return redirect(url_for("admin.coupons"))
    return render_template("admin/coupons.html", coupons=q("SELECT * FROM coupons ORDER BY id DESC"))


@bp.route("/pincodes", methods=["GET", "POST"])
@perm_required("settings.manage")
def pincodes():
    if request.method == "POST":
        if request.form.get("action") == "delete":
            run("DELETE FROM pincode_rules WHERE id=?", (_int(request.form.get("id")),))
        else:
            prefix = (request.form.get("prefix") or "").strip()
            rule = request.form.get("rule")
            if not prefix.isdigit() or not (1 <= len(prefix) <= 6) or rule not in ("block_cod", "block_all", "surcharge"):
                flash("Enter 1–6 digits and choose a rule.", "error")
            else:
                run("INSERT INTO pincode_rules(prefix,rule,surcharge,note) VALUES (?,?,?,?)",
                    (prefix, rule, _int(request.form.get("surcharge"), 0) if rule == "surcharge" else 0, (request.form.get("note") or "").strip()[:200] or None))
                flash("Rule added.", "success")
        return redirect(url_for("admin.pincodes"))
    return render_template("admin/pincodes.html", rules=q("SELECT * FROM pincode_rules ORDER BY prefix"))


SETTING_GROUPS = [
    ("Store details", [("store_name", "Store name"), ("legal_name", "Legal / business name"), ("gstin", "GSTIN (leave blank until registered)"),
                       ("business_address", "Registered address"), ("support_email", "Support email"), ("support_phone", "Support phone"), ("whatsapp", "WhatsApp number (digits only)")]),
    ("Messages (claims need evidence — see the claim register)", [("announcement", "Announcement bar (leave blank for none)"), ("delivery_note", "Delivery note"),
                                                                    ("returns_summary", "Returns summary")]),
    ("Shipping rules (PILOT HYPOTHESES — not locked)", [("free_ship_threshold", "Free shipping at or above (₹)"), ("ship_fee_below", "Shipping fee below threshold (₹)"),
                                                          ("heavy_threshold_g", "Heavy item from (grams)"), ("heavy_surcharge", "Heavy item surcharge (₹)")]),
    ("COD rules (PILOT HYPOTHESES)", [("cod_enabled", "COD enabled (1/0)"), ("cod_fee", "COD handling fee (₹)"), ("cod_max", "COD maximum order value (₹)")]),
    ("Payments", [("online_enabled", "Online payment enabled (1/0) — keep 0 until a gateway is connected")]),
    ("Display", [("demo_banner", "Show 'sample listings' notices (1/0)"), ("reviews_min_to_show_stars", "Reviews needed before stars show on cards"), ("policies_reviewed", "Policy pages reviewed by a legal adviser (1/0) — hides the draft notice")]),
]


@bp.route("/settings", methods=["GET", "POST"])
@perm_required("settings.manage")
def settings():
    if request.method == "POST":
        vals = {}
        for _g, fields in SETTING_GROUPS:
            for key, _label in fields:
                v = (request.form.get(key) or "").strip()
                if key in ("free_ship_threshold", "ship_fee_below", "heavy_threshold_g", "heavy_surcharge", "cod_fee", "cod_max", "reviews_min_to_show_stars"):
                    if not v.isdigit():
                        flash(f"“{key}” must be a whole number.", "error")
                        return redirect(url_for("admin.settings"))
                if key in ("cod_enabled", "online_enabled", "demo_banner", "policies_reviewed") and v not in ("0", "1"):
                    flash(f"“{key}” must be 1 or 0.", "error")
                    return redirect(url_for("admin.settings"))
                vals[key] = v[:500]
        save_settings(vals)
        log_audit("settings.update")
        flash("Settings saved.", "success")
        return redirect(url_for("admin.settings"))
    return render_template("admin/settings.html", groups=SETTING_GROUPS, S=get_settings())


@bp.route("/team", methods=["GET", "POST"])
@perm_required("team.manage")
def team():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "create":
            email = (request.form.get("email") or "").strip().lower()
            name = (request.form.get("name") or "").strip()
            role = request.form.get("role")
            pw = request.form.get("password") or ""
            prob = password_problem(pw)
            if not EMAIL_RE.match(email) or len(name) < 2 or role not in ("staff", "admin"):
                flash("Enter a name, valid email and role.", "error")
            elif prob:
                flash(prob, "error")
            elif q1("SELECT 1 FROM users WHERE email=?", (email,)):
                flash("That email already has an account.", "error")
            else:
                run("INSERT INTO users(email,name,password_hash,role) VALUES (?,?,?,?)", (email, name, hash_password(pw), role))
                log_audit("team.create", "user", email, role)
                flash(f"{role.title()} account created.", "success")
        elif action in ("role", "toggle", "reset"):
            uid = _int(request.form.get("id"))
            u = q1("SELECT * FROM users WHERE id=? AND role IN ('staff','admin')", (uid,))
            if not u:
                abort(404)
            if u["id"] == g.user["id"] and action in ("role", "toggle"):
                flash("You can't change your own role or deactivate yourself.", "error")
            elif action == "role" and request.form.get("role") in ("staff", "admin"):
                run("UPDATE users SET role=? WHERE id=?", (request.form["role"], uid))
                log_audit("team.role", "user", uid, request.form["role"])
                flash("Role updated.", "success")
            elif action == "toggle":
                run("UPDATE users SET is_active=? WHERE id=?", (0 if u["is_active"] else 1, uid))
                log_audit("team.toggle", "user", uid)
                flash("Account updated.", "success")
            elif action == "reset":
                pw = request.form.get("password") or ""
                prob = password_problem(pw)
                if prob:
                    flash(prob, "error")
                else:
                    run("UPDATE users SET password_hash=?, failed_logins=0, locked_until=NULL WHERE id=?", (hash_password(pw), uid))
                    log_audit("team.reset_password", "user", uid)
                    flash("Password reset.", "success")
        return redirect(url_for("admin.team"))
    return render_template("admin/team.html", team=q("SELECT * FROM users WHERE role IN ('staff','admin') ORDER BY role, name"))


@bp.route("/outbox")
@perm_required("settings.manage")
def outbox():
    return render_template("admin/outbox.html", mails=q("SELECT * FROM outbox ORDER BY id DESC LIMIT 100"))


@bp.route("/audit", endpoint="audit")
@perm_required("settings.manage")
def audit_view():
    return render_template("admin/audit.html", rows=q("""SELECT a.*, u.email FROM audit_log a LEFT JOIN users u ON u.id=a.user_id ORDER BY a.id DESC LIMIT 200"""))
