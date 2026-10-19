from flask import Blueprint, abort, flash, g, redirect, render_template, request, url_for

from .checkout import STATES
from .db import q, q1, run
from .security import (EMAIL_RE, PHONE_RE, PIN_RE, hash_password, login_required, password_problem, verify_password, rate_limit)

bp = Blueprint("account", __name__, url_prefix="/account")


@bp.route("/")
@login_required
def dashboard():
    orders = q("SELECT * FROM orders WHERE user_id=? ORDER BY created_at DESC LIMIT 5", (g.user["id"],))
    wl = q1("SELECT COUNT(*) c FROM wishlist WHERE user_id=?", (g.user["id"],))["c"]
    return render_template("account/dashboard.html", orders=orders, wl=wl)


@bp.route("/orders")
@login_required
def orders():
    rows = q("SELECT * FROM orders WHERE user_id=? ORDER BY created_at DESC", (g.user["id"],))
    return render_template("account/orders.html", orders=rows)


def _own_order(order_no):
    o = q1("SELECT * FROM orders WHERE order_no=? AND user_id=?", (order_no, g.user["id"]))
    if not o:
        abort(404)
    return o


@bp.route("/orders/<order_no>")
@login_required
def order_detail(order_no):
    o = _own_order(order_no)
    items = q("SELECT * FROM order_items WHERE order_id=?", (o["id"],))
    events = q("SELECT * FROM order_events WHERE order_id=? ORDER BY id", (o["id"],))
    return render_template("account/order_detail.html", o=o, items=items, events=events)


@bp.route("/orders/<order_no>/receipt")
@login_required
def receipt(order_no):
    o = _own_order(order_no)
    items = q("SELECT * FROM order_items WHERE order_id=?", (o["id"],))
    return render_template("receipt.html", o=o, items=items)


@bp.route("/orders/<order_no>/cancel", methods=["POST"])
@login_required
def cancel_order(order_no):
    from .services import OrderError, change_order_status
    o = _own_order(order_no)
    if o["status"] not in ("pending", "confirmed"):
        flash("This order can no longer be cancelled online. Please contact us.", "error")
    else:
        try:
            change_order_status(o, "cancelled", g.user["id"], "Cancelled by customer")
            flash("Your order has been cancelled.", "success")
        except OrderError as e:
            flash(str(e), "error")
    return redirect(url_for("account.order_detail", order_no=order_no))


@bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    errors = {}
    if request.method == "POST":
        action = request.form.get("action")
        if action == "details":
            name = (request.form.get("name") or "").strip()
            phone = (request.form.get("phone") or "").strip()
            if len(name) < 2:
                errors["name"] = "Please enter your name."
            if phone and not PHONE_RE.match(phone):
                errors["phone"] = "Enter a 10-digit mobile number."
            if not errors:
                run("UPDATE users SET name=?, phone=?, marketing_opt_in=? WHERE id=?", (name, phone or None, 1 if request.form.get("marketing") else 0, g.user["id"]))
                flash("Profile updated.", "success")
                return redirect(url_for("account.profile"))
        elif action == "password":
            cur, new = request.form.get("current") or "", request.form.get("password") or ""
            if not verify_password(cur, g.user["password_hash"]):
                errors["current"] = "Current password is incorrect."
            else:
                prob = password_problem(new)
                if prob:
                    errors["password"] = prob
            if not errors:
                run("UPDATE users SET password_hash=? WHERE id=?", (hash_password(new), g.user["id"]))
                flash("Password changed.", "success")
                return redirect(url_for("account.profile"))
    return render_template("account/profile.html", errors=errors)


@bp.route("/addresses", methods=["GET", "POST"])
@login_required
def addresses():
    errors, form = {}, {}
    if request.method == "POST":
        action = request.form.get("action")
        if action == "delete":
            run("DELETE FROM addresses WHERE id=? AND user_id=?", (request.form.get("id", type=int), g.user["id"]))
            flash("Address removed.", "info")
            return redirect(url_for("account.addresses"))
        if action == "default":
            aid = request.form.get("id", type=int)
            if q1("SELECT 1 FROM addresses WHERE id=? AND user_id=?", (aid, g.user["id"])):
                run("UPDATE addresses SET is_default=0 WHERE user_id=?", (g.user["id"],))
                run("UPDATE addresses SET is_default=1 WHERE id=?", (aid,))
            return redirect(url_for("account.addresses"))
        form = {k: (request.form.get(k) or "").strip() for k in ("label", "name", "phone", "line1", "line2", "landmark", "city", "state", "pincode")}
        if len(form["name"]) < 2:
            errors["name"] = "Enter a name."
        if not PHONE_RE.match(form["phone"]):
            errors["phone"] = "Enter a 10-digit mobile number."
        if len(form["line1"]) < 5:
            errors["line1"] = "Enter the house/flat and street."
        if len(form["city"]) < 2:
            errors["city"] = "Enter the city."
        if form["state"] not in STATES:
            errors["state"] = "Select a state."
        if not PIN_RE.match(form["pincode"]):
            errors["pincode"] = "Enter a valid 6-digit PIN."
        if not errors:
            count = q1("SELECT COUNT(*) c FROM addresses WHERE user_id=?", (g.user["id"],))["c"]
            if count >= 10:
                flash("You can save up to 10 addresses.", "error")
            else:
                run("""INSERT INTO addresses(user_id,label,name,phone,line1,line2,landmark,city,state,pincode,is_default) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                    (g.user["id"], form["label"] or None, form["name"], form["phone"], form["line1"], form["line2"] or None,
                     form["landmark"] or None, form["city"], form["state"], form["pincode"], 1 if count == 0 else 0))
                flash("Address saved.", "success")
                return redirect(url_for("account.addresses"))
    rows = q("SELECT * FROM addresses WHERE user_id=? ORDER BY is_default DESC, id DESC", (g.user["id"],))
    return render_template("account/addresses.html", addresses=rows, errors=errors, form=form, states=STATES)
