import secrets

from flask import Blueprint, abort, flash, g, jsonify, redirect, render_template, request, session, url_for

from .db import q, q1, run
from .security import EMAIL_RE, PHONE_RE, PIN_RE, client_ip, rate_limit
from .services import (OrderError, available_qty, cart_items, compute_totals, create_order, get_settings, inr, sbool)

bp = Blueprint("checkout", __name__)

STATES = ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh", "Chhattisgarh",
          "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
          "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
          "Mizoram", "Nagaland", "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
          "Uttar Pradesh", "Uttarakhand", "West Bengal"]


def _cart():
    return session.setdefault("cart", {})


@bp.route("/cart")
def cart():
    c = _cart()
    lines, problems = cart_items(c)
    session.modified = True
    for pr in problems:
        flash(pr, "info")
    code = session.get("coupon")
    t = compute_totals(lines, code, "online", None)  # preview only; COD fee and PIN charges apply at checkout
    if code and t["coupon_error"]:
        flash(t["coupon_error"], "error")
        session.pop("coupon", None)
        t = compute_totals(lines, None, "online", None)
    return render_template("cart.html", lines=lines, t=t, coupon=session.get("coupon"))


@bp.route("/cart/add", methods=["POST"])
@rate_limit("cart", 120, 60)
def cart_add():
    try:
        pid = int(request.form.get("product_id", ""))
        qty = max(1, min(int(request.form.get("qty", 1)), 10))
    except ValueError:
        abort(400)
    p = q1("SELECT * FROM products WHERE id=? AND is_active=1", (pid,))
    if not p:
        abort(404)
    c = _cart()
    new_qty = min(int(c.get(str(pid), 0)) + qty, 10)
    if new_qty > available_qty(p):
        flash(f"Only {available_qty(p)} available.", "error")
        return redirect(request.referrer or url_for("shop.product", slug=p["slug"]))
    c[str(pid)] = new_qty
    session.modified = True
    if request.form.get("buy_now") == "1":
        return redirect(url_for("checkout.checkout"))
    flash(f"Added “{p['title']}” to your cart.", "success")
    return redirect(url_for("checkout.cart"))


@bp.route("/cart/update", methods=["POST"])
def cart_update():
    c = _cart()
    pid = request.form.get("product_id", "")
    try:
        qty = int(request.form.get("qty", 1))
    except ValueError:
        abort(400)
    if pid in c:
        if qty <= 0:
            c.pop(pid)
        else:
            p = q1("SELECT * FROM products WHERE id=? AND is_active=1", (pid,))
            c[pid] = min(qty, 10, available_qty(p)) if p else 0
            if not p or c[pid] <= 0:
                c.pop(pid, None)
    session.modified = True
    return redirect(url_for("checkout.cart"))


@bp.route("/cart/remove", methods=["POST"])
def cart_remove():
    _cart().pop(request.form.get("product_id", ""), None)
    session.modified = True
    return redirect(url_for("checkout.cart"))


@bp.route("/cart/coupon", methods=["POST"])
@rate_limit("coupon", 20, 600)
def cart_coupon():
    if request.form.get("remove"):
        session.pop("coupon", None)
        return redirect(url_for("checkout.cart"))
    code = (request.form.get("code") or "").strip()[:40]
    lines, _ = cart_items(_cart())
    t = compute_totals(lines, code, "online", None)
    if t["coupon_error"]:
        flash(t["coupon_error"], "error")
    else:
        session["coupon"] = t["coupon"]["code"]
        flash(f"Coupon {t['coupon']['code']} applied.", "success")
    return redirect(url_for("checkout.cart"))


def _defaults():
    d = {"name": "", "email": "", "phone": "", "line1": "", "line2": "", "landmark": "", "city": "", "state": "", "pincode": "", "payment_method": "cod", "customer_note": ""}
    if g.user:
        d["name"], d["email"], d["phone"] = g.user["name"], g.user["email"], g.user["phone"] or ""
        a = q1("SELECT * FROM addresses WHERE user_id=? ORDER BY is_default DESC, id DESC LIMIT 1", (g.user["id"],))
        if a:
            d.update(name=a["name"], phone=a["phone"], line1=a["line1"], line2=a["line2"] or "", landmark=a["landmark"] or "", city=a["city"], state=a["state"], pincode=a["pincode"])
    return d


@bp.route("/api/quote")
@rate_limit("quote", 120, 60)
def quote():
    lines, _ = cart_items(_cart())
    pm = request.args.get("pm", "cod")
    pin = (request.args.get("pin") or "").strip()
    pin = pin if PIN_RE.match(pin) else None
    t = compute_totals(lines, session.get("coupon"), pm if pm in ("cod", "online") else "cod", pin)
    return jsonify(subtotal=t["subtotal"], discount=t["discount"], shipping=t["shipping"], cod_fee=t["cod_fee"], total=t["total"],
                   cod_ok=t["cod_ok"], cod_reason=t["cod_reason"], block_all=t["block_all"],
                   fmt={k: inr(t[k]) for k in ("subtotal", "discount", "shipping", "cod_fee", "total")})


@bp.route("/checkout", methods=["GET", "POST"])
def checkout():
    c = _cart()
    lines, problems = cart_items(c)
    session.modified = True
    if not lines:
        flash("Your cart is empty.", "info")
        return redirect(url_for("checkout.cart"))
    errors, form = {}, _defaults()
    if request.method == "GET":
        session.setdefault("co_token", secrets.token_urlsafe(16))  # reused until an order is placed, so a second tab/reload does not break the form
        for pr in problems:
            flash(pr, "info")
    else:
        for k in form:
            form[k] = (request.form.get(k) or "").strip()
        if form["email"]:
            form["email"] = form["email"].lower()
        if not secrets.compare_digest(request.form.get("co_token", "x"), session.get("co_token", "y")):
            flash("This checkout page expired (maybe you already placed the order). Please review your cart.", "error")
            return redirect(url_for("checkout.cart"))
        if len(form["name"]) < 2:
            errors["name"] = "Please enter your full name."
        if not EMAIL_RE.match(form["email"]):
            errors["email"] = "Enter a valid email address."
        if not PHONE_RE.match(form["phone"]):
            errors["phone"] = "Enter a 10-digit mobile number."
        if len(form["line1"]) < 5:
            errors["line1"] = "Please enter your house/flat and street."
        if len(form["city"]) < 2:
            errors["city"] = "Enter your city."
        if form["state"] not in STATES:
            errors["state"] = "Select your state."
        if not PIN_RE.match(form["pincode"]):
            errors["pincode"] = "Enter a valid 6-digit PIN code."
        if form["payment_method"] not in ("cod", "online"):
            errors["payment_method"] = "Choose a payment method."
        for k, mx in (("name", 80), ("line1", 160), ("line2", 160), ("landmark", 120), ("city", 60), ("customer_note", 400)):
            if len(form[k]) > mx:
                errors[k] = f"Too long (max {mx} characters)."
        if not errors:
            form["coupon_code"] = session.get("coupon")
            try:
                order = create_order(g.user, form, c, client_ip())
            except OrderError as e:
                flash(str(e), "error")
            else:
                if g.user and request.form.get("save_address"):
                    if not q1("SELECT 1 FROM addresses WHERE user_id=? AND line1=? AND pincode=?", (g.user["id"], form["line1"], form["pincode"])):
                        run("INSERT INTO addresses(user_id,label,name,phone,line1,line2,landmark,city,state,pincode,is_default) VALUES (?,?,?,?,?,?,?,?,?,?,0)",
                            (g.user["id"], "Saved at checkout", form["name"], form["phone"], form["line1"], form["line2"] or None, form["landmark"] or None, form["city"], form["state"], form["pincode"]))
                session["cart"] = {}
                session.pop("coupon", None)
                session.pop("co_token", None)
                mine = session.get("my_orders", [])
                session["my_orders"] = ([order["order_no"]] + mine)[:10]
                return redirect(url_for("checkout.confirmation", order_no=order["order_no"]))
    pm = form["payment_method"] if form["payment_method"] in ("cod", "online") else "cod"
    pin = form["pincode"] if PIN_RE.match(form["pincode"]) else None
    t = compute_totals(lines, session.get("coupon"), pm, pin)
    return render_template("checkout.html", lines=lines, t=t, form=form, errors=errors, states=STATES, co_token=session.get("co_token"))


@bp.route("/order/<order_no>")
def confirmation(order_no):
    o = q1("SELECT * FROM orders WHERE order_no=?", (order_no,))
    if not o:
        abort(404)
    owner = g.user and o["user_id"] == g.user["id"]
    if not owner and order_no not in session.get("my_orders", []):
        abort(404)
    items = q("SELECT * FROM order_items WHERE order_id=?", (o["id"],))
    return render_template("order_confirmation.html", o=o, items=items)


@bp.route("/track", methods=["GET", "POST"])
@rate_limit("track", 15, 600)
def track():
    o = items = events = None
    err = None
    if request.method == "POST":
        no = (request.form.get("order_no") or "").strip().upper()
        ident = (request.form.get("ident") or "").strip().lower()
        o = q1("SELECT * FROM orders WHERE order_no=?", (no,))
        # require the order number AND the phone or email used at checkout; same message either way
        if not o or ident not in (o["email"].lower(), o["phone"], o["ship_phone"]):
            o, err = None, "We couldn't find an order with those details."
        else:
            items = q("SELECT * FROM order_items WHERE order_id=?", (o["id"],))
            events = q("SELECT * FROM order_events WHERE order_id=? ORDER BY id", (o["id"],))
    return render_template("track.html", o=o, items=items, events=events, err=err)
