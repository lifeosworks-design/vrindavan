import hashlib
import secrets
from datetime import datetime, timedelta, timezone

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from .db import q1, run
from .security import (EMAIL_RE, PHONE_RE, hash_password, login_user, logout_user, password_problem,
                       rate_limit, verify_password, log_audit)
from .services import apply_wishlist_merge

bp = Blueprint("auth", __name__)
_DUMMY_HASH = hash_password("not-a-real-password-just-for-timing")

MAX_FAILS = 5
LOCK_MINUTES = 15


def _safe_next(nxt):
    if nxt and nxt.startswith("/") and not nxt.startswith("//") and "\\" not in nxt:
        return nxt.rstrip("?")
    return None


@bp.route("/register", methods=["GET", "POST"])
@rate_limit("register", 10, 3600)
def register():
    if g.user:
        return redirect(url_for("account.dashboard"))
    errors, form = {}, {}
    if request.method == "POST":
        form = {k: (request.form.get(k) or "").strip() for k in ("name", "email", "phone")}
        pw = request.form.get("password") or ""
        if len(form["name"]) < 2:
            errors["name"] = "Please enter your name."
        if not EMAIL_RE.match(form["email"]):
            errors["email"] = "Enter a valid email address."
        if form["phone"] and not PHONE_RE.match(form["phone"]):
            errors["phone"] = "Enter a 10-digit Indian mobile number."
        prob = password_problem(pw)
        if prob:
            errors["password"] = prob
        if not errors and q1("SELECT 1 FROM users WHERE email=?", (form["email"],)):
            errors["email"] = "An account with this email already exists. Try signing in."
        if not errors:
            cur = run("INSERT INTO users(email,phone,name,password_hash,role,marketing_opt_in) VALUES (?,?,?,?, 'customer', ?)",
                      (form["email"].lower(), form["phone"] or None, form["name"], hash_password(pw), 1 if request.form.get("marketing") else 0))
            user = q1("SELECT * FROM users WHERE id=?", (cur.lastrowid,))
            wl = list(session.get("wl", []))
            login_user(user)
            apply_wishlist_merge(user["id"], wl)
            session.pop("wl", None)
            flash("Welcome to VRINDAVAN. Your account is ready.", "success")
            return redirect(_safe_next(request.args.get("next")) or url_for("account.dashboard"))
    return render_template("auth/register.html", errors=errors, form=form)


@bp.route("/login", methods=["GET", "POST"])
@rate_limit("login", 30, 900)
def login():
    if g.user:
        return redirect(url_for("account.dashboard"))
    error = None
    email = ""
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        pw = request.form.get("password") or ""
        user = q1("SELECT * FROM users WHERE email=?", (email,))
        now = datetime.now(timezone.utc)
        locked = False
        if user and user["locked_until"]:
            try:
                locked = datetime.strptime(user["locked_until"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc) > now
            except ValueError:
                locked = False
        if locked:
            error = "Too many failed attempts. Please try again in a few minutes."
        elif user and user["is_active"] and verify_password(pw, user["password_hash"]):
            wl = list(session.get("wl", []))
            login_user(user)
            apply_wishlist_merge(user["id"], wl)
            session.pop("wl", None)
            if user["role"] != "customer":
                log_audit("login", "user", user["id"])
            nxt = _safe_next(request.args.get("next"))
            if user["role"] in ("admin", "staff") and not nxt:
                return redirect(url_for("admin.dashboard"))
            return redirect(nxt or url_for("account.dashboard"))
        else:
            if user:
                fails = user["failed_logins"] + 1
                lock = (now + timedelta(minutes=LOCK_MINUTES)).strftime("%Y-%m-%d %H:%M:%S") if fails >= MAX_FAILS else None
                run("UPDATE users SET failed_logins=?, locked_until=? WHERE id=?", (0 if lock else fails, lock, user["id"]))
            else:
                verify_password(pw, _DUMMY_HASH)  # keep timing similar when the account does not exist
            error = "Email or password is incorrect."
    return render_template("auth/login.html", error=error, email=email)


@bp.route("/logout", methods=["POST"])
def logout():
    logout_user()
    flash("You have been signed out.", "info")
    return redirect(url_for("shop.home"))


@bp.route("/forgot-password", methods=["GET", "POST"])
@rate_limit("forgot", 8, 3600)
def forgot():
    sent = False
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        user = q1("SELECT * FROM users WHERE email=? AND is_active=1", (email,))
        if user:
            token = secrets.token_urlsafe(32)
            run("INSERT INTO password_resets(token_hash,user_id,expires_at) VALUES (?,?,?)",
                (hashlib.sha256(token.encode()).hexdigest(), user["id"], (datetime.now(timezone.utc) + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")))
            link = url_for("auth.reset", token=token, _external=True)
            run("INSERT INTO outbox(to_email,subject,body,kind) VALUES (?,?,?,?)",
                (user["email"], "Reset your VRINDAVAN password", f"Use this link within 1 hour:\n{link}\nIf you did not ask for this, ignore this email.", "password_reset"))
        sent = True  # same response whether or not the account exists
    return render_template("auth/forgot.html", sent=sent)


@bp.route("/reset/<token>", methods=["GET", "POST"])
@rate_limit("reset", 20, 3600)
def reset(token):
    th = hashlib.sha256(token.encode()).hexdigest()
    row = q1("SELECT * FROM password_resets WHERE token_hash=? AND used=0", (th,))
    valid = bool(row and row["expires_at"] >= datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
    error = None
    if request.method == "POST" and valid:
        pw = request.form.get("password") or ""
        error = password_problem(pw)
        if not error:
            run("UPDATE users SET password_hash=?, failed_logins=0, locked_until=NULL WHERE id=?", (hash_password(pw), row["user_id"]))
            run("UPDATE password_resets SET used=1 WHERE token_hash=?", (th,))
            flash("Password updated. Please sign in.", "success")
            return redirect(url_for("auth.login"))
    return render_template("auth/reset.html", valid=valid, error=error)
