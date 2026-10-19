"""Auth, roles/permissions, CSRF, rate limiting, security headers."""
import hmac
import re
import secrets
import time
from collections import defaultdict, deque
from functools import wraps

from flask import abort, current_app, flash, g, jsonify, redirect, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from .db import audit, q1, run

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]{2,}$")
PHONE_RE = re.compile(r"^[6-9]\d{9}$")
PIN_RE = re.compile(r"^[1-9]\d{5}$")

# Permission model. Customers have no admin permissions. Staff are limited. Admin is everything.
ROLE_PERMS = {
    "admin": {"*"},
    "staff": {
        "admin.access", "products.view", "products.edit", "orders.view", "orders.manage",
        "inventory.manage", "reviews.moderate", "messages.view", "collections.view",
    },
    "customer": set(),
}


def has_perm(user, perm):
    if not user:
        return False
    perms = ROLE_PERMS.get(user["role"], set())
    return "*" in perms or perm in perms


# ----------------------------- passwords -----------------------------
def hash_password(pw):
    return generate_password_hash(pw, method="scrypt")


def verify_password(pw, pw_hash):
    return check_password_hash(pw_hash, pw)


def password_problem(pw):
    if len(pw) < 10:
        return "Password must be at least 10 characters."
    if len(pw) > 128:
        return "Password is too long."
    if pw.lower() in {"password123", "1234567890", "qwertyuiop"}:
        return "That password is too common."
    classes = sum(bool(re.search(p, pw)) for p in (r"[a-z]", r"[A-Z]", r"\d", r"[^A-Za-z0-9]"))
    if classes < 2:
        return "Use a mix of letters and numbers or symbols."
    return None


# ----------------------------- sessions -----------------------------
def load_user():
    uid = session.get("uid")
    g.user = None
    if uid:
        u = q1("SELECT * FROM users WHERE id=? AND is_active=1", (uid,))
        if u is None:
            session.pop("uid", None)
        else:
            g.user = u


def login_user(user):
    keep = {"wl": session.get("wl"), "cart": session.get("cart")}
    session.clear()  # prevent session fixation
    session["uid"] = user["id"]
    session["csrf"] = secrets.token_urlsafe(32)
    session.permanent = True
    for k, v in keep.items():
        if v:
            session[k] = v
    run("UPDATE users SET last_login_at=datetime('now'), failed_logins=0, locked_until=NULL WHERE id=?", (user["id"],))


def logout_user():
    session.clear()


def login_required(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        if not g.get("user"):
            flash("Please sign in to continue.", "info")
            return redirect(url_for("auth.login", next=request.full_path if request.method == "GET" else url_for("account.dashboard")))
        return fn(*a, **kw)
    return wrapper


def perm_required(perm):
    def deco(fn):
        @wraps(fn)
        def wrapper(*a, **kw):
            user = g.get("user")
            if not user:
                return redirect(url_for("auth.login", next=request.full_path))
            if not has_perm(user, perm):
                abort(403)
            return fn(*a, **kw)
        return wrapper
    return deco


# ----------------------------- CSRF -----------------------------
def csrf_token():
    if "csrf" not in session:
        session["csrf"] = secrets.token_urlsafe(32)
    return session["csrf"]


def csrf_protect():
    if request.method in ("POST", "PUT", "PATCH", "DELETE"):
        sent = request.form.get("_csrf") or request.headers.get("X-CSRF-Token") or ""
        expected = session.get("csrf", "")
        if not expected or not hmac.compare_digest(sent, expected):
            abort(400, description="Security check failed. Please reload the page and try again.")


# ----------------------------- rate limiting (in-process; use Redis if you run several workers) -----------------------------
_hits = defaultdict(deque)


def rate_limited(key, limit, window):
    now = time.time()
    dq = _hits[key]
    while dq and now - dq[0] > window:
        dq.popleft()
    if len(dq) >= limit:
        return True
    dq.append(now)
    return False


def client_ip():
    return request.remote_addr or "?"


def rate_limit(name, limit, window):
    def deco(fn):
        @wraps(fn)
        def wrapper(*a, **kw):
            if current_app.config.get("TESTING") and not current_app.config.get("RATE_LIMIT_IN_TESTS"):
                return fn(*a, **kw)
            if rate_limited(f"{name}:{client_ip()}", limit, window):
                if request.accept_mimetypes.best == "application/json" or request.is_json:
                    return jsonify(error="Too many requests. Please wait and try again."), 429
                abort(429)
            return fn(*a, **kw)
        return wrapper
    return deco


# ----------------------------- headers -----------------------------
def add_security_headers(resp):
    resp.headers.setdefault("X-Content-Type-Options", "nosniff")
    resp.headers.setdefault("X-Frame-Options", "DENY")
    resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    resp.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=(), payment=()")
    resp.headers.setdefault(
        "Content-Security-Policy",
        "default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; "
        "font-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'",
    )
    if current_app.config.get("SESSION_COOKIE_SECURE"):
        resp.headers.setdefault("Strict-Transport-Security", "max-age=31536000; includeSubDomains")
    if request.endpoint and (request.endpoint.startswith("admin.") or request.endpoint.startswith("account.") or request.endpoint.startswith("auth.")):
        resp.headers["Cache-Control"] = "no-store"
    return resp


def log_audit(action, entity=None, entity_id=None, detail=None):
    u = g.get("user")
    audit(u["id"] if u else None, action, entity, entity_id, detail, client_ip())
