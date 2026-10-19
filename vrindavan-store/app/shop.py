import json
import math

from flask import (Blueprint, Response, abort, flash, g, jsonify, redirect, render_template, request, session, url_for)

from .db import q, q1, run
from .security import EMAIL_RE, PHONE_RE, PIN_RE, rate_limit
from .services import (cod_eligibility, get_settings, inr, pin_rules_for, rating_summary, sbool, sint, stock_label)

bp = Blueprint("shop", __name__)

PAGE_SIZE = 24
SORTS = {
    "featured": "p.is_featured DESC, p.created_at DESC",
    "newest": "p.created_at DESC",
    "price_asc": "p.price ASC",
    "price_desc": "p.price DESC",
}
PAGES = {
    "about": "About us",
    "faq": "Questions",
    "shipping-policy": "Shipping policy",
    "returns-policy": "Returns & refunds",
    "privacy": "Privacy policy",
    "terms": "Terms of use",
}

CARD_SQL = """
SELECT p.*,
  (SELECT base FROM product_images WHERE product_id=p.id ORDER BY sort_order, id LIMIT 1) AS img,
  (SELECT alt FROM product_images WHERE product_id=p.id ORDER BY sort_order, id LIMIT 1) AS img_alt,
  (SELECT COUNT(*) FROM reviews r WHERE r.product_id=p.id AND r.status='approved') AS rev_count,
  (SELECT AVG(rating) FROM reviews r WHERE r.product_id=p.id AND r.status='approved') AS rev_avg,
  (SELECT group_concat(c.name, ' · ') FROM collections c JOIN product_collections pc ON pc.collection_id=c.id
     WHERE pc.product_id=p.id AND c.kind='deity') AS deity_names
FROM products p
"""


def build_listing(collection=None, query=None):
    where, args = ["p.is_active=1"], []
    if collection:
        where.append("p.id IN (SELECT product_id FROM product_collections WHERE collection_id=?)")
        args.append(collection["id"])
    if query:
        like = f"%{query}%"
        where.append("""(p.title LIKE ? OR p.description LIKE ? OR p.material LIKE ? OR p.subtitle LIKE ? OR p.id IN
                        (SELECT pc.product_id FROM product_collections pc JOIN collections c ON c.id=pc.collection_id WHERE c.name LIKE ? OR c.name_native LIKE ?))""")
        args += [like] * 6
    materials = [m for m in request.args.getlist("material") if m]
    if materials:
        where.append("p.material IN (%s)" % ",".join("?" * len(materials)))
        args += materials
    deities = [d for d in request.args.getlist("deity") if d]
    if deities:
        where.append("""p.id IN (SELECT pc.product_id FROM product_collections pc JOIN collections c ON c.id=pc.collection_id
                        WHERE c.kind='deity' AND c.slug IN (%s))""" % ",".join("?" * len(deities)))
        args += deities
    try:
        pmin = int(request.args.get("min", ""))
        where.append("p.price >= ?")
        args.append(pmin)
    except ValueError:
        pmin = None
    try:
        pmax = int(request.args.get("max", ""))
        where.append("p.price <= ?")
        args.append(pmax)
    except ValueError:
        pmax = None
    if request.args.get("in_stock") == "1":
        where.append("(p.track_stock=0 OR p.allow_backorder=1 OR p.stock_qty>0)")
    sort = request.args.get("sort", "featured")
    order = SORTS.get(sort, SORTS["featured"])
    page = max(int(request.args.get("page", 1) or 1), 1) if (request.args.get("page", "1") or "1").isdigit() else 1
    total = q1(f"SELECT COUNT(*) c FROM products p WHERE {' AND '.join(where)}", args)["c"]
    rows = q(f"{CARD_SQL} WHERE {' AND '.join(where)} ORDER BY {order} LIMIT ? OFFSET ?", args + [PAGE_SIZE, (page - 1) * PAGE_SIZE])
    pages = max(math.ceil(total / PAGE_SIZE), 1)
    facets_m = q("SELECT material, COUNT(*) c FROM products WHERE is_active=1 AND material IS NOT NULL AND material<>'' GROUP BY material ORDER BY material")
    facets_d = q("""SELECT c.slug, c.name, c.name_native, COUNT(*) n FROM collections c JOIN product_collections pc ON pc.collection_id=c.id
                    JOIN products p ON p.id=pc.product_id AND p.is_active=1 WHERE c.kind='deity' AND c.is_active=1 GROUP BY c.id ORDER BY c.sort_order""")
    return dict(products=rows, total=total, page=min(page, pages), pages=pages, sort=sort, materials=materials, deities=deities,
                pmin=pmin, pmax=pmax, facets_m=facets_m, facets_d=facets_d, in_stock=request.args.get("in_stock") == "1")


@bp.route("/")
def home():
    featured = q(f"{CARD_SQL} WHERE p.is_active=1 AND p.is_featured=1 ORDER BY p.created_at DESC LIMIT 8")
    if len(featured) < 4:
        featured = q(f"{CARD_SQL} WHERE p.is_active=1 ORDER BY p.is_featured DESC, p.created_at DESC LIMIT 8")
    hero = featured[0] if featured else None
    deity_tiles = q("""SELECT c.*, (SELECT pi.base FROM product_images pi JOIN product_collections pc ON pc.product_id=pi.product_id
                                    JOIN products p ON p.id=pi.product_id AND p.is_active=1
                                    WHERE pc.collection_id=c.id ORDER BY p.is_featured DESC, pi.sort_order, pi.id LIMIT 1) AS img
                       FROM collections c WHERE c.is_active=1 AND c.kind='deity' AND EXISTS
                       (SELECT 1 FROM product_collections pc JOIN products p ON p.id=pc.product_id WHERE pc.collection_id=c.id AND p.is_active=1)
                       ORDER BY c.sort_order, c.name""")
    home_reviews = q("""SELECT r.*, u.name uname, p.title ptitle FROM reviews r JOIN users u ON u.id=r.user_id JOIN products p ON p.id=r.product_id
                        WHERE r.status='approved' AND p.is_active=1 ORDER BY r.created_at DESC LIMIT 3""")
    return render_template("home.html", featured=featured, hero=hero, deity_tiles=deity_tiles, home_reviews=home_reviews)


@bp.route("/shop")
def shop_all():
    data = build_listing()
    return render_template("collection.html", collection=None, title="All murtis", **data)


@bp.route("/collections/<slug>")
def collection(slug):
    c = q1("SELECT * FROM collections WHERE slug=? AND is_active=1", (slug,))
    if not c:
        abort(404)
    data = build_listing(collection=c)
    return render_template("collection.html", collection=c, title=c["name"], **data)


@bp.route("/search")
@rate_limit("search", 60, 60)
def search():
    term = (request.args.get("q") or "").strip()[:80]
    data = build_listing(query=term) if term else dict(products=[], total=0, page=1, pages=1, sort="featured", materials=[], deities=[],
                                                      pmin=None, pmax=None, facets_m=[], facets_d=[], in_stock=False)
    return render_template("collection.html", collection=None, title=f"Search: {term}" if term else "Search", search_term=term, **data)


@bp.route("/api/suggest")
@rate_limit("suggest", 120, 60)
def suggest():
    term = (request.args.get("q") or "").strip()[:60]
    if len(term) < 2:
        return jsonify(results=[])
    like = f"%{term}%"
    rows = q("SELECT slug, title, price FROM products WHERE is_active=1 AND (title LIKE ? OR material LIKE ?) ORDER BY is_featured DESC LIMIT 6", (like, like))
    cols = q("SELECT slug, name, name_native FROM collections WHERE is_active=1 AND (name LIKE ? OR name_native LIKE ?) LIMIT 4", (like, like))
    return jsonify(results=[{"type": "product", "label": r["title"], "sub": inr(r["price"]), "url": url_for("shop.product", slug=r["slug"])} for r in rows]
                   + [{"type": "collection", "label": c["name"] + (f" · {c['name_native']}" if c["name_native"] else ""), "sub": "Collection", "url": url_for("shop.collection", slug=c["slug"])} for c in cols])


@bp.route("/products/<slug>")
def product(slug):
    p = q1(f"{CARD_SQL} WHERE p.slug=?", (slug,))
    if not p or (not p["is_active"] and not (g.user and g.user["role"] in ("admin", "staff"))):
        abort(404)
    images = q("SELECT * FROM product_images WHERE product_id=? ORDER BY sort_order, id", (p["id"],))
    cols = q("SELECT c.* FROM collections c JOIN product_collections pc ON pc.collection_id=c.id WHERE pc.product_id=? ORDER BY c.kind, c.sort_order", (p["id"],))
    reviews = q("""SELECT r.*, u.name uname FROM reviews r JOIN users u ON u.id=r.user_id
                   WHERE r.product_id=? AND r.status='approved' ORDER BY r.created_at DESC LIMIT 20""", (p["id"],))
    can_review = False
    my_review = None
    if g.user:
        my_review = q1("SELECT * FROM reviews WHERE product_id=? AND user_id=?", (p["id"], g.user["id"]))
        bought = q1("""SELECT o.id FROM orders o JOIN order_items i ON i.order_id=o.id
                       WHERE o.user_id=? AND i.product_id=? AND o.status='delivered' LIMIT 1""", (g.user["id"], p["id"]))
        can_review = bool(bought) and not my_review
    related = []
    if cols:
        related = q(f"""{CARD_SQL} WHERE p.is_active=1 AND p.id<>? AND p.id IN
                        (SELECT product_id FROM product_collections WHERE collection_id IN (%s)) ORDER BY p.is_featured DESC LIMIT 4""" % ",".join("?" * len(cols)),
                    [p["id"]] + [c["id"] for c in cols])
    rv = [i for i in session.get("rv", []) if i != p["id"]]
    recent = [r for r in (q1(f"{CARD_SQL} WHERE p.id=? AND p.is_active=1", (i,)) for i in rv[:4]) if r]
    session["rv"] = ([p["id"]] + rv)[:8]
    count, avg = rating_summary(p["id"])
    return render_template("product.html", p=p, images=images, cols=cols, reviews=reviews, can_review=can_review, my_review=my_review,
                           related=related, recent=recent, rev_count=count, rev_avg=avg, label=stock_label(p))


@bp.route("/products/<slug>/review", methods=["POST"])
@rate_limit("review", 10, 3600)
def submit_review(slug):
    if not g.user:
        flash("Please sign in to review.", "info")
        return redirect(url_for("auth.login", next=url_for("shop.product", slug=slug)))
    p = q1("SELECT * FROM products WHERE slug=?", (slug,))
    if not p:
        abort(404)
    bought = q1("""SELECT o.id FROM orders o JOIN order_items i ON i.order_id=o.id
                   WHERE o.user_id=? AND i.product_id=? AND o.status='delivered' LIMIT 1""", (g.user["id"], p["id"]))
    if not bought:
        flash("Only customers who received this item can review it.", "error")
        return redirect(url_for("shop.product", slug=slug))
    try:
        rating = int(request.form.get("rating", 0))
    except ValueError:
        rating = 0
    body = (request.form.get("body") or "").strip()[:1500]
    title = (request.form.get("title") or "").strip()[:120]
    if rating < 1 or rating > 5:
        flash("Choose a rating from 1 to 5.", "error")
        return redirect(url_for("shop.product", slug=slug) + "#reviews")
    run("INSERT OR IGNORE INTO reviews(product_id,user_id,order_id,rating,title,body,status) VALUES (?,?,?,?,?,?, 'pending')",
        (p["id"], g.user["id"], bought["id"], rating, title or None, body or None))
    flash("Thank you. Your review will appear after moderation.", "success")
    return redirect(url_for("shop.product", slug=slug) + "#reviews")


@bp.route("/api/pincode")
@rate_limit("pincode", 60, 60)
def pincode_check():
    pin = (request.args.get("pin") or "").strip()
    if not PIN_RE.match(pin):
        return jsonify(ok=False, message="Enter a valid 6-digit PIN code.")
    block_all, block_cod, surcharge, notes = pin_rules_for(pin)
    if block_all:
        return jsonify(ok=False, message="We are not able to deliver to this PIN code yet.")
    msg = ["We deliver to this PIN code. " + get_settings()["delivery_note"]]
    price = 0
    pid = request.args.get("product", type=int)
    allow = True
    if pid:
        p = q1("SELECT price, allow_cod FROM products WHERE id=?", (pid,))
        if p:
            price, allow = p["price"], bool(p["allow_cod"])
    if sbool("cod_enabled"):
        if block_cod or not allow:
            msg.append("Cash on delivery is not available here — pay online.")
        elif sint("cod_max") and price > sint("cod_max"):
            msg.append(f"Cash on delivery is available up to {inr(sint('cod_max'))}.")
        else:
            fee = sint("cod_fee")
            msg.append("Cash on delivery available" + (f" (handling fee {inr(fee)})." if fee else "."))
    if surcharge:
        msg.append(f"Extra delivery charge for this area: {inr(surcharge)}.")
    return jsonify(ok=True, message=" ".join(msg))


@bp.route("/api/wishlist/toggle", methods=["POST"])
@rate_limit("wishlist", 120, 60)
def wishlist_toggle():
    data = request.get_json(silent=True) or {}
    try:
        pid = int(data.get("product_id"))
    except (TypeError, ValueError):
        return jsonify(error="bad request"), 400
    if not q1("SELECT 1 FROM products WHERE id=? AND is_active=1", (pid,)):
        return jsonify(error="not found"), 404
    if g.user:
        row = q1("SELECT 1 FROM wishlist WHERE user_id=? AND product_id=?", (g.user["id"], pid))
        if row:
            run("DELETE FROM wishlist WHERE user_id=? AND product_id=?", (g.user["id"], pid))
            on = False
        else:
            run("INSERT INTO wishlist(user_id,product_id) VALUES (?,?)", (g.user["id"], pid))
            on = True
        count = q1("SELECT COUNT(*) c FROM wishlist WHERE user_id=?", (g.user["id"],))["c"]
    else:
        wl = list(session.get("wl", []))
        if pid in wl:
            wl.remove(pid)
            on = False
        else:
            wl.append(pid)
            on = True
        session["wl"] = wl[:100]
        count = len(session["wl"])
    return jsonify(on=on, count=count)


@bp.route("/wishlist")
def wishlist():
    if g.user:
        rows = q(f"{CARD_SQL} WHERE p.is_active=1 AND p.id IN (SELECT product_id FROM wishlist WHERE user_id=?)", (g.user["id"],))
    else:
        ids = [int(i) for i in session.get("wl", [])]
        rows = q(f"{CARD_SQL} WHERE p.is_active=1 AND p.id IN (%s)" % ",".join("?" * len(ids)), ids) if ids else []
    return render_template("wishlist.html", products=rows)


@bp.route("/pages/<slug>")
def page(slug):
    if slug not in PAGES:
        abort(404)
    return render_template(f"pages/{slug}.html", page_title=PAGES[slug])


@bp.route("/contact", methods=["GET", "POST"])
@rate_limit("contact", 5, 3600)
def contact():
    errors, form = {}, {}
    if request.method == "POST":
        form = {k: (request.form.get(k) or "").strip() for k in ("name", "email", "phone", "message")}
        if len(form["name"]) < 2:
            errors["name"] = "Please enter your name."
        if form["email"] and not EMAIL_RE.match(form["email"]):
            errors["email"] = "Enter a valid email."
        if form["phone"] and not PHONE_RE.match(form["phone"]):
            errors["phone"] = "Enter a 10-digit mobile number."
        if not form["email"] and not form["phone"]:
            errors["email"] = "Give us an email or phone so we can reply."
        if len(form["message"]) < 5 or len(form["message"]) > 2000:
            errors["message"] = "Please write a message (5–2000 characters)."
        if request.form.get("website"):  # honeypot
            return redirect(url_for("shop.contact"))
        if not errors:
            run("INSERT INTO contact_messages(name,email,phone,message) VALUES (?,?,?,?)", (form["name"], form["email"] or None, form["phone"] or None, form["message"]))
            flash("Thank you — we have received your message.", "success")
            return redirect(url_for("shop.contact"))
    return render_template("pages/contact.html", errors=errors, form=form)


@bp.route("/robots.txt")
def robots():
    body = "User-agent: *\nDisallow: /admin\nDisallow: /account\nDisallow: /cart\nDisallow: /checkout\nDisallow: /api/\n"
    base = request.url_root.rstrip("/")
    return Response(body + f"Sitemap: {base}/sitemap.xml\n", mimetype="text/plain")


@bp.route("/sitemap.xml")
def sitemap():
    base = request.url_root.rstrip("/")
    urls = [base + "/", base + "/shop"]
    urls += [base + url_for("shop.collection", slug=c["slug"]) for c in q("SELECT slug FROM collections WHERE is_active=1")]
    urls += [base + url_for("shop.product", slug=p["slug"]) for p in q("SELECT slug FROM products WHERE is_active=1")]
    urls += [base + url_for("shop.page", slug=s) for s in PAGES]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"<url><loc>{u}</loc></url>" for u in urls) + "\n</urlset>"
    return Response(xml, mimetype="application/xml")


@bp.route("/healthz")
def healthz():
    q1("SELECT 1")
    return jsonify(ok=True)
