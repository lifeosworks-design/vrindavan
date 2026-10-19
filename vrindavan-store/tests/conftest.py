import re
import shutil

import pytest

from app import create_app
from app.cli import seed_catalog
from app.db import q1, run
from app.security import hash_password

PW = "Str0ng-Test-Pass!"


@pytest.fixture(scope="session")
def template_dir(tmp_path_factory):
    """Seed once (slow: images + password hashing), copy per test."""
    d = tmp_path_factory.mktemp("template")
    app = create_app({"TESTING": True, "DATABASE": str(d / "t.db"), "MEDIA_ROOT": str(d / "media"), "SECRET_KEY": "test-secret"})
    with app.app_context():
        seed_catalog()
        pwh = hash_password(PW)
        for email, name, role in (("admin@example.com", "Admin One", "admin"), ("staff@example.com", "Staff One", "staff"),
                                  ("cust@example.com", "Cust One", "customer"), ("cust2@example.com", "Cust Two", "customer")):
            run("INSERT INTO users(email,name,password_hash,role,phone) VALUES (?,?,?,?,?)", (email, name, pwh, role, "9876543210"))
    return d


@pytest.fixture()
def app(tmp_path, template_dir):
    shutil.copy(template_dir / "t.db", tmp_path / "t.db")
    shutil.copytree(template_dir / "media", tmp_path / "media")
    return create_app({"TESTING": True, "DATABASE": str(tmp_path / "t.db"), "MEDIA_ROOT": str(tmp_path / "media"), "SECRET_KEY": "test-secret"})


@pytest.fixture()
def client(app):
    return app.test_client()


def token(client, path="/"):
    html = client.get(path).get_data(as_text=True)
    m = re.search(r'<meta name="csrf" content="([^"]+)"', html)
    assert m, "no csrf meta on " + path
    return m.group(1)


def login(client, email, pw=PW):
    t = token(client, "/login")
    return client.post("/login", data={"email": email, "password": pw, "_csrf": t}, follow_redirects=False)


def post(client, path, data=None, page="/"):
    d = dict(data or {})
    d["_csrf"] = token(client, page)
    return client.post(path, data=d, follow_redirects=False)


def first_product(app, material=None):
    with app.app_context():
        row = q1("SELECT * FROM products WHERE is_active=1 AND price < 3000 ORDER BY id LIMIT 1")
        return dict(row)


def checkout_form(**over):
    d = {"name": "Test Buyer", "email": "buyer@example.com", "phone": "9876543210", "line1": "12 Temple Street", "line2": "",
         "landmark": "", "city": "Jaipur", "state": "Rajasthan", "pincode": "302001", "payment_method": "cod", "customer_note": ""}
    d.update(over)
    return d
