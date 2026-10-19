import os
import secrets
from datetime import timedelta

from flask import Flask, g, jsonify, render_template, request, send_from_directory, session
from markupsafe import Markup, escape

from . import db as dbm
from .security import add_security_headers, csrf_protect, csrf_token, has_perm, load_user
from .services import get_settings, inr, rating_summary, sbool, stock_label


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, instance_path=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "instance")))
    os.makedirs(app.instance_path, exist_ok=True)

    secret_file = os.path.join(app.instance_path, "secret_key")
    secret = os.environ.get("VR_SECRET_KEY")
    if not secret:
        if not os.path.exists(secret_file):
            with open(secret_file, "w") as f:
                f.write(secrets.token_hex(32))
            try:
                os.chmod(secret_file, 0o600)
            except OSError:
                pass
        secret = open(secret_file).read().strip()

    app.config.update(
        SECRET_KEY=secret,
        DATABASE=os.path.join(app.instance_path, "store.db"),
        MEDIA_ROOT=os.path.join(app.instance_path, "media"),
        MAX_CONTENT_LENGTH=12 * 1024 * 1024,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=os.environ.get("VR_HTTPS", "0") == "1",
        PERMANENT_SESSION_LIFETIME=timedelta(days=14),
        JSON_SORT_KEYS=False,
        SITE_URL=os.environ.get("VR_SITE_URL", ""),
    )
    if test_config:
        app.config.update(test_config)
    os.makedirs(app.config["MEDIA_ROOT"], exist_ok=True)

    app.teardown_appcontext(dbm.close_db)
    with app.app_context():
        dbm.init_db()

    # ---- request hooks ----
    @app.before_request
    def _before():
        if request.endpoint in ("static", "media"):
            return None
        load_user()
        csrf_protect()

    app.after_request(add_security_headers)

    # ---- template helpers ----
    app.jinja_env.filters["inr"] = inr

    @app.template_filter("nl2br")
    def nl2br(s):
        return Markup("<br>".join(str(escape(s or "")).splitlines()))

    @app.template_filter("urlencode_args")
    def urlencode_args(d, **over):
        from urllib.parse import urlencode
        pairs = []
        for k, vals in d.items():
            if k in over:
                continue
            for v in (vals if isinstance(vals, list) else [vals]):
                pairs.append((k, v))
        pairs += list(over.items())
        return urlencode(pairs)

    @app.template_filter("dt")
    def fmt_dt(s):
        if not s:
            return ""
        try:
            from datetime import datetime
            d = datetime.strptime(s[:19], "%Y-%m-%d %H:%M:%S")
            return d.strftime("%d %b %Y, %H:%M")
        except ValueError:
            return s

    @app.context_processor
    def _ctx():
        s = get_settings()
        cart = session.get("cart", {})
        nav = []
        try:
            nav = dbm.q(
                """SELECT c.* FROM collections c WHERE c.is_active=1 AND c.kind='deity' AND EXISTS
                   (SELECT 1 FROM product_collections pc JOIN products p ON p.id=pc.product_id
                    WHERE pc.collection_id=c.id AND p.is_active=1) ORDER BY c.sort_order, c.name"""
            )
            purposes = dbm.q(
                """SELECT c.* FROM collections c WHERE c.is_active=1 AND c.kind='purpose' AND EXISTS
                   (SELECT 1 FROM product_collections pc JOIN products p ON p.id=pc.product_id
                    WHERE pc.collection_id=c.id AND p.is_active=1) ORDER BY c.sort_order, c.name"""
            )
        except Exception:
            purposes = []
        wl = set()
        if g.get("user"):
            wl = {r["product_id"] for r in dbm.q("SELECT product_id FROM wishlist WHERE user_id=?", (g.user["id"],))}
        else:
            wl = set(session.get("wl", []))
        demo = bool(dbm.q1("SELECT 1 FROM products WHERE is_demo=1 AND is_active=1 LIMIT 1")) and sbool("demo_banner")
        return dict(
            S=s, csrf_token=csrf_token, cart_count=sum(int(v) for v in cart.values()) if cart else 0,
            nav_deities=nav, nav_purposes=purposes, wl_ids=wl, can=lambda perm: has_perm(g.get("user"), perm),
            stock_label=stock_label, rating_summary=rating_summary, demo_site=demo,
        )

    # ---- blueprints ----
    from .auth import bp as auth_bp
    from .shop import bp as shop_bp
    from .checkout import bp as checkout_bp
    from .account import bp as account_bp
    from .admin import bp as admin_bp
    app.register_blueprint(shop_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")

    @app.route("/media/<path:filename>", endpoint="media")
    def media(filename):
        resp = send_from_directory(app.config["MEDIA_ROOT"], filename, max_age=60 * 60 * 24 * 30)
        return resp

    # ---- errors ----
    def _err(code, title, msg):
        if request.path.startswith("/api/") or request.accept_mimetypes.best == "application/json":
            return jsonify(error=msg), code
        return render_template("error.html", code=code, title=title, msg=msg), code

    @app.errorhandler(400)
    def e400(e):
        return _err(400, "Request problem", getattr(e, "description", "Bad request."))

    @app.errorhandler(403)
    def e403(e):
        return _err(403, "Not allowed", "You do not have permission to view this page.")

    @app.errorhandler(404)
    def e404(e):
        return _err(404, "Page not found", "We couldn't find the page you were looking for.")

    @app.errorhandler(413)
    def e413(e):
        return _err(413, "File too large", "That upload is too large.")

    @app.errorhandler(429)
    def e429(e):
        return _err(429, "Slow down", "Too many attempts. Please wait a few minutes and try again.")

    @app.errorhandler(500)
    def e500(e):
        return _err(500, "Something went wrong", "An unexpected error occurred. Please try again.")

    from . import cli
    cli.register(app)
    return app
