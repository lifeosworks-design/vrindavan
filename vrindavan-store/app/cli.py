"""CLI: flask --app run seed | create-admin | ..."""
import os
import secrets
import string

import click

from .db import get_db, q1, run
from .images import make_placeholder
from .security import EMAIL_RE, hash_password, password_problem
from .services import adjust_stock, save_settings, slugify, unique_slug

DEITIES = [("Ganesha", "गणेश", 1), ("Krishna", "कृष्ण", 2), ("Lakshmi", "लक्ष्मी", 3), ("Shiva", "शिव", 4), ("Hanuman", "हनुमान", 5), ("Durga", "दुर्गा", 6)]
PURPOSES = [("Home mandir", None, 1), ("Gifting", None, 2), ("Festivals", None, 3)]

# Placeholder catalogue taken from the pilot matrix. NOTHING here is a supplier quote, a measured value or a verified claim.
DEMO = [
    dict(title="Radha-Krishna idol, 9–10 in", deity="Krishna", purposes=["Home mandir", "Gifting"], material="Brass", price=2999, w=2000, h=24.0, featured=1),
    dict(title="Lakshmi–Ganesha pair, 6–7 in", deity="Lakshmi", also=["Ganesha"], purposes=["Home mandir", "Festivals", "Gifting"], material="Brass", price=1999, w=1200, h=16.0, featured=1),
    dict(title="Seated Ganesha idol, 5–6 in", deity="Ganesha", purposes=["Home mandir", "Gifting"], material="Brass", price=1499, w=800, h=14.0, featured=1),
    dict(title="Standing Hanuman idol, 12 in", deity="Hanuman", purposes=["Home mandir"], material="Brass", price=4999, w=4500, h=30.0, featured=1),
    dict(title="Seated Ganesha idol, 8 in", deity="Ganesha", purposes=["Home mandir", "Festivals"], material="Polyresin", price=1499, w=800, h=20.0, featured=0),
    dict(title="Krishna with flute, 10 in", deity="Krishna", purposes=["Home mandir", "Gifting"], material="Resin", price=1999, w=1200, h=25.0, featured=0, fragile=1),
    dict(title="Ganesha idol, 9–12 in", deity="Ganesha", purposes=["Home mandir", "Gifting"], material="Marble composite", price=4999, w=3500, h=28.0, featured=0, fragile=1),
    dict(title="Radha-Krishna idol, 12 in", deity="Krishna", purposes=["Home mandir", "Gifting"], material="Marble", price=12000, w=10000, h=30.0, featured=0, fragile=1, cod=0),
]


# (figure, body palette, ornament palette) for each sample product - illustrations, not photographs
ART = {
    "Radha-Krishna idol, 9–10 in": ("radha_krishna", "brass", "brass"),
    "Lakshmi–Ganesha pair, 6–7 in": ("lakshmi_ganesha", "brass", "brass"),
    "Seated Ganesha idol, 5–6 in": ("ganesha", "brass", "brass"),
    "Standing Hanuman idol, 12 in": ("hanuman", "brass", "brass"),
    "Seated Ganesha idol, 8 in": ("ganesha", "bronze", "brass"),
    "Krishna with flute, 10 in": ("krishna", "teal", "brass"),
    "Ganesha idol, 9–12 in": ("ganesha", "marble", "marble"),
    "Radha-Krishna idol, 12 in": ("radha_krishna", "marble", "marble"),
}


def add_sample_illustrations(product_id, title):
    """Replace a product's placeholder rows with 3 generated sample illustrations (front on stone, in a mandir niche, close-up)."""
    from flask import current_app
    from . import sampleart
    from .images import _write_sizes, delete_image_files
    from .db import q
    kind, pal, orn = ART.get(title, ("ganesha", "brass", "brass"))
    pals = {"brass": sampleart.BRASS, "bronze": sampleart.BRONZE, "teal": sampleart.TEAL, "marble": sampleart.MARBLE}
    for old in q("SELECT * FROM product_images WHERE product_id=? AND is_placeholder=1", (product_id,)):
        delete_image_files(current_app.config["MEDIA_ROOT"], old["base"])
    run("DELETE FROM product_images WHERE product_id=? AND is_placeholder=1", (product_id,))
    labels = ["front view", "in a mandir niche", "close-up"]
    for n, im in enumerate(sampleart.render(kind, pals[pal], pals[orn])):
        base = _write_sizes(im, current_app.config["MEDIA_ROOT"], product_id)
        run("INSERT INTO product_images(product_id,base,alt,sort_order,is_placeholder) VALUES (?,?,?,?,1)",
            (product_id, base, f"Sample illustration of {title} ({labels[n]})", n))


def seed_catalog():
    from flask import current_app
    db = get_db()
    for name, native, order in DEITIES:
        if not q1("SELECT 1 FROM collections WHERE name=?", (name,)):
            run("INSERT INTO collections(slug,name,name_native,kind,sort_order) VALUES (?,?,?,?,?)", (slugify(name), name, native, "deity", order))
    for name, native, order in PURPOSES:
        if not q1("SELECT 1 FROM collections WHERE name=?", (name,)):
            run("INSERT INTO collections(slug,name,name_native,kind,sort_order) VALUES (?,?,?,?,?)", (slugify(name), name, native, "purpose", order))
    if q1("SELECT 1 FROM products LIMIT 1"):
        return 0
    n = 0
    for d in DEMO:
        slug = unique_slug("products", d["title"] + " sample")
        cur = run(
            """INSERT INTO products(slug,title,subtitle,description,material,height_cm,weight_g,price,stock_qty,track_stock,allow_cod,fragile,is_active,is_featured,is_demo,low_stock_at)
               VALUES (?,?,?,?,?,?,?,?,0,1,?,?,1,?,1,2)""",
            (slug, d["title"], f"{d['material']} · sample listing", "Sample listing for layout testing. Product details, material, finish and dimensions are placeholders until the piece is sourced and inspected.",
             d["material"], d["h"], d["w"], d["price"], d.get("cod", 1), d.get("fragile", 0), d.get("featured", 0)),
        )
        pid = cur.lastrowid
        for cname in [d["deity"]] + d.get("also", []) + d["purposes"]:
            c = q1("SELECT id FROM collections WHERE name=?", (cname,))
            if c:
                run("INSERT OR IGNORE INTO product_collections(product_id,collection_id) VALUES (?,?)", (pid, c["id"]))
        add_sample_illustrations(pid, d["title"])
        adjust_stock(pid, 5, "sample stock", None)
        n += 1
    save_settings({"announcement": ""})
    return n


def make_password(n=16):
    alphabet = string.ascii_letters + string.digits + "!@#%^*-_"
    while True:
        pw = "".join(secrets.choice(alphabet) for _ in range(n))
        if password_problem(pw) is None:
            return pw


def register(app):
    @app.cli.command("seed")
    def seed_cmd():
        """Create deity/purpose collections and a clearly-labelled SAMPLE catalogue (only if no products exist)."""
        n = seed_catalog()
        click.echo(f"Seeded {n} sample products." if n else "Collections ensured; products already exist, nothing added.")

    @app.cli.command("sample-photos")
    def sample_photos():
        """(Re)generate sample illustrations for every sample product (is_demo=1)."""
        from .db import q
        n = 0
        for p in q("SELECT id, title FROM products WHERE is_demo=1"):
            add_sample_illustrations(p["id"], p["title"])
            n += 1
        click.echo(f"Generated sample illustrations for {n} products.")

    @app.cli.command("refresh-placeholders")
    def refresh_placeholders():
        """Regenerate the sample placeholder images (only rows flagged is_placeholder)."""
        from flask import current_app
        from .db import q
        from .images import delete_image_files
        n = 0
        for im in q("SELECT i.*, p.title FROM product_images i JOIN products p ON p.id=i.product_id WHERE i.is_placeholder=1"):
            base = make_placeholder(im["title"], current_app.config["MEDIA_ROOT"], im["product_id"])
            run("UPDATE product_images SET base=? WHERE id=?", (base, im["id"]))
            delete_image_files(current_app.config["MEDIA_ROOT"], im["base"])
            n += 1
        click.echo(f"Refreshed {n} placeholder images.")

    @app.cli.command("create-admin")
    @click.option("--email", required=True)
    @click.option("--name", default="Store Admin")
    @click.option("--role", type=click.Choice(["admin", "staff"]), default="admin")
    @click.option("--password", default=None, help="Omit to generate a random password written to instance/admin_credentials.txt")
    def create_admin(email, name, role, password):
        email = email.strip().lower()
        if not EMAIL_RE.match(email):
            raise click.ClickException("Invalid email")
        if q1("SELECT 1 FROM users WHERE email=?", (email,)):
            raise click.ClickException("That email already exists")
        generated = password is None
        pw = password or make_password()
        prob = password_problem(pw)
        if prob:
            raise click.ClickException(prob)
        run("INSERT INTO users(email,name,password_hash,role) VALUES (?,?,?,?)", (email, name, hash_password(pw), role))
        if generated:
            path = os.path.join(app.instance_path, "admin_credentials.txt")
            with open(path, "a", encoding="utf-8") as f:
                f.write(f"{role}: {email}  password: {pw}\n")
            try:
                os.chmod(path, 0o600)
            except OSError:
                pass
            click.echo(f"{role} created. Generated password saved in {path} (delete that file after you store the password safely).")
        else:
            click.echo(f"{role} created.")
