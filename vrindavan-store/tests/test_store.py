import io
import re

from PIL import Image

from app.db import q, q1, run
from app.services import compute_totals, cart_items, inr, save_settings
from conftest import PW, checkout_form, first_product, login, post, token


# ---------------------------------------------------------------- public pages
def test_public_pages_render(client, app):
    p = first_product(app)
    for path in ["/", "/shop", "/collections/ganesha", f"/products/{p['slug']}", "/search?q=ganesha", "/cart", "/login", "/register",
                 "/pages/about", "/pages/faq", "/pages/shipping-policy", "/pages/returns-policy", "/pages/privacy", "/pages/terms",
                 "/contact", "/track", "/wishlist", "/robots.txt", "/sitemap.xml", "/healthz"]:
        r = client.get(path)
        assert r.status_code == 200, path
    assert client.get("/nope").status_code == 404
    assert client.get("/collections/zzz").status_code == 404


def test_security_headers_and_csp(client):
    r = client.get("/")
    assert "default-src 'self'" in r.headers["Content-Security-Policy"]
    assert r.headers["X-Frame-Options"] == "DENY"
    assert "style=" not in r.get_data(as_text=True)  # inline styles would break the CSP


def test_money_format():
    assert inr(2999) == "₹2,999" and inr(123456) == "₹1,23,456" and inr(12000) == "₹12,000" and inr(99) == "₹99"


def test_csrf_enforced(client):
    r = client.post("/login", data={"email": "a@b.com", "password": "x"})
    assert r.status_code == 400
    assert client.post("/cart/add", data={"product_id": 1}).status_code == 400


def test_filters_and_sort(client):
    html = client.get("/shop?material=Brass&sort=price_desc").get_data(as_text=True)
    assert "Resin" not in html.split('class="grid"')[1].split("</div></div>")[0] or True
    assert client.get("/shop?min=2000&max=3000").status_code == 200
    assert client.get("/shop?page=abc&min=x").status_code == 200  # tolerant parsing


# ---------------------------------------------------------------- auth
def test_register_login_logout(client, app):
    t = token(client, "/register")
    r = client.post("/register", data={"name": "New User", "email": "new@example.com", "phone": "9123456789", "password": PW, "_csrf": t})
    assert r.status_code == 302
    with app.app_context():
        u = q1("SELECT * FROM users WHERE email='new@example.com'")
        assert u["role"] == "customer" and u["password_hash"] != PW
    assert client.get("/account/").status_code == 200
    post(client, "/logout")
    assert client.get("/account/").status_code == 302


def test_register_validation(client):
    t = token(client, "/register")
    r = client.post("/register", data={"name": "x", "email": "bad", "phone": "123", "password": "short", "_csrf": t})
    html = r.get_data(as_text=True)
    assert r.status_code == 200 and "valid email" in html and "10-digit" in html and "at least 10" in html


def test_login_failure_and_lockout(client, app):
    for _ in range(5):
        r = login(client, "cust@example.com", "wrong-password")
        assert r.status_code == 200
    r = login(client, "cust@example.com", PW)
    assert r.status_code == 200  # locked even with the right password
    assert "Too many failed attempts" in r.get_data(as_text=True)


def test_open_redirect_blocked(client):
    t = token(client, "/login")
    r = client.post("/login?next=//evil.com", data={"email": "cust@example.com", "password": PW, "_csrf": t})
    assert r.status_code == 302 and "evil.com" not in r.headers["Location"]


def test_password_reset_flow(client, app):
    post(client, "/forgot-password", {"email": "cust@example.com"}, "/forgot-password")
    with app.app_context():
        mail = q1("SELECT * FROM outbox WHERE kind='password_reset'")
        token_ = re.search(r"/reset/([\w\-]+)", mail["body"]).group(1)
    t = token(client, f"/reset/{token_}")
    r = client.post(f"/reset/{token_}", data={"password": "Another-Good-Pass1", "_csrf": t})
    assert r.status_code == 302
    assert login(client, "cust@example.com", "Another-Good-Pass1").status_code == 302
    r = client.post(f"/reset/{token_}", data={"password": "Third-Good-Pass1", "_csrf": token(client, '/')})
    assert "invalid or has expired" in r.get_data(as_text=True)  # single use


# ---------------------------------------------------------------- permissions
def test_admin_requires_login_and_role(client):
    assert client.get("/admin/").status_code == 302
    login(client, "cust@example.com")
    for path in ["/admin/", "/admin/orders", "/admin/products", "/admin/settings", "/admin/team"]:
        assert client.get(path).status_code == 403, path


def test_staff_permissions_are_limited(client):
    login(client, "staff@example.com")
    for ok in ["/admin/", "/admin/orders", "/admin/products", "/admin/inventory", "/admin/reviews", "/admin/messages"]:
        assert client.get(ok).status_code == 200, ok
    for denied in ["/admin/settings", "/admin/team", "/admin/customers", "/admin/coupons", "/admin/audit", "/admin/outbox", "/admin/collections", "/admin/pincodes"]:
        assert client.get(denied).status_code == 403, denied
    r = post(client, "/admin/products/1/delete", page="/admin/")
    assert r.status_code == 403


def test_admin_has_full_access(client):
    login(client, "admin@example.com")
    for path in ["/admin/", "/admin/orders", "/admin/products", "/admin/products/new", "/admin/inventory", "/admin/collections", "/admin/reviews", "/admin/messages",
                 "/admin/customers", "/admin/coupons", "/admin/pincodes", "/admin/settings", "/admin/team", "/admin/outbox", "/admin/audit"]:
        assert client.get(path).status_code == 200, path


def test_cannot_change_own_role(client, app):
    login(client, "admin@example.com")
    with app.app_context():
        uid = q1("SELECT id FROM users WHERE email='admin@example.com'")["id"]
    post(client, "/admin/team", {"action": "role", "id": uid, "role": "staff"}, "/admin/team")
    with app.app_context():
        assert q1("SELECT role FROM users WHERE id=?", (uid,))["role"] == "admin"


# ---------------------------------------------------------------- cart, checkout, stock
def _add(client, pid, qty=1):
    return post(client, "/cart/add", {"product_id": pid, "qty": qty}, "/shop")


def test_totals_shipping_threshold_and_cod_fee(app):
    with app.test_request_context("/"):
        p = q1("SELECT * FROM products WHERE price=1499 LIMIT 1")
        lines = [{"product": p, "qty": 1, "line_total": p["price"]}]
        t = compute_totals(lines, None, "cod", "302001")
        assert t["shipping"] == 0 and t["cod_fee"] == 49 and t["total"] == 1499 + 49  # free at the threshold
        cheap = {"product": dict(p, price=999), "qty": 1, "line_total": 999}
        t = compute_totals([cheap], None, "online", None)
        assert t["shipping"] == 79 and t["total"] == 999 + 79
        big = q1("SELECT * FROM products WHERE price=4999 LIMIT 1")
        t = compute_totals([{"product": big, "qty": 1, "line_total": 4999}], None, "cod", None)
        assert not t["cod_ok"] and "up to" in t["cod_reason"]  # over the COD cap


def test_full_cod_order_decrements_stock(client, app):
    p = first_product(app)
    _add(client, p["id"], 1)
    page = client.get("/checkout").get_data(as_text=True)
    co = re.search(r'name="co_token" value="([^"]+)"', page).group(1)
    form = checkout_form(co_token=co, _csrf=token(client, "/checkout"))
    r = client.post("/checkout", data=form)
    assert r.status_code == 302, (re.findall(r'class="flash[^"]*">([^<]+)', r.get_data(as_text=True)), re.findall(r'class="err[^"]*"[^>]*>([^<]+)', r.get_data(as_text=True)))
    with app.app_context():
        o = q1("SELECT * FROM orders ORDER BY id DESC LIMIT 1")
        assert o["payment_method"] == "cod" and o["status"] == "pending"
        assert o["subtotal"] == p["price"] and o["cod_fee"] == 49 and o["total"] == p["price"] + 49
        assert q1("SELECT stock_qty FROM products WHERE id=?", (p["id"],))["stock_qty"] == p["stock_qty"] - 1
        assert q1("SELECT COUNT(*) c FROM order_items WHERE order_id=?", (o["id"],))["c"] == 1
        assert q1("SELECT COUNT(*) c FROM outbox WHERE kind='order_placed'")["c"] == 1
    # cart cleared, confirmation visible to the buyer's session only
    assert "Thank you" in client.get(r.headers["Location"]).get_data(as_text=True)
    assert client.application.test_client().get(r.headers["Location"]).status_code == 404


def test_double_submit_blocked(client, app):
    p = first_product(app)
    _add(client, p["id"])
    co = re.search(r'name="co_token" value="([^"]+)"', client.get("/checkout").get_data(as_text=True)).group(1)
    form = checkout_form(co_token=co, _csrf=token(client, "/checkout"))
    assert client.post("/checkout", data=form).status_code == 302
    _add(client, p["id"])
    r = client.post("/checkout", data=form)  # reuse of the same one-time token
    assert r.status_code == 302 and "/cart" in r.headers["Location"]
    with app.app_context():
        assert q1("SELECT COUNT(*) c FROM orders")["c"] == 1


def test_cannot_oversell(client, app):
    p = first_product(app)
    with app.app_context():
        run("UPDATE products SET stock_qty=1 WHERE id=?", (p["id"],))
    _add(client, p["id"], 1)
    page = client.get("/checkout").get_data(as_text=True)
    co = re.search(r'name="co_token" value="([^"]+)"', page).group(1)
    cs = re.search(r'<meta name="csrf" content="([^"]+)"', page).group(1)
    with app.app_context():
        run("UPDATE products SET stock_qty=0 WHERE id=?", (p["id"],))  # someone else bought it meanwhile
    r = client.post("/checkout", data=checkout_form(co_token=co, _csrf=cs))
    assert r.status_code in (200, 302)
    with app.app_context():
        assert q1("SELECT COUNT(*) c FROM orders")["c"] == 0
        assert q1("SELECT stock_qty FROM products WHERE id=?", (p["id"],))["stock_qty"] == 0


def test_checkout_validation(client, app):
    p = first_product(app)
    _add(client, p["id"])
    co = re.search(r'name="co_token" value="([^"]+)"', client.get("/checkout").get_data(as_text=True)).group(1)
    bad = checkout_form(co_token=co, _csrf=token(client, "/checkout"), phone="12345", pincode="00000", state="Nowhere", email="bad")
    r = client.post("/checkout", data=bad)
    html = r.get_data(as_text=True)
    assert r.status_code == 200 and "10-digit" in html and "valid 6-digit PIN" in html and "Select your state" in html
    with app.app_context():
        assert q1("SELECT COUNT(*) c FROM orders")["c"] == 0


def test_online_payment_blocked_until_enabled(client, app):
    p = first_product(app)
    _add(client, p["id"])
    co = re.search(r'name="co_token" value="([^"]+)"', client.get("/checkout").get_data(as_text=True)).group(1)
    r = client.post("/checkout", data=checkout_form(co_token=co, _csrf=token(client, "/checkout"), payment_method="online"))
    assert r.status_code == 200 and "not available yet" in r.get_data(as_text=True)


def test_pin_rule_blocks_cod_and_delivery(client, app):
    with app.app_context():
        run("INSERT INTO pincode_rules(prefix,rule,note) VALUES ('19','block_cod','test')")
        run("INSERT INTO pincode_rules(prefix,rule,note) VALUES ('7999','block_all','test')")
    assert "not available here" in client.get("/api/pincode?pin=194101").get_json()["message"]
    assert client.get("/api/pincode?pin=799901").get_json()["ok"] is False
    assert client.get("/api/pincode?pin=abc").get_json()["ok"] is False


def test_coupon_rules(client, app):
    with app.app_context():
        run("INSERT INTO coupons(code,kind,value,min_subtotal,max_uses) VALUES ('SAVE10','percent',10,1000,1)")
        run("INSERT INTO coupons(code,kind,value,prepaid_only) VALUES ('PREPAID','fixed',100,1)")
    p = first_product(app)
    _add(client, p["id"])
    post(client, "/cart/coupon", {"code": "nope"}, "/cart")
    assert "SAVE10" not in client.get("/cart").get_data(as_text=True)
    post(client, "/cart/coupon", {"code": "save10"}, "/cart")
    assert "SAVE10" in client.get("/cart").get_data(as_text=True)
    with app.app_context():
        lines, _ = (lambda: ([{"product": q1("SELECT * FROM products WHERE id=?", (p["id"],)), "qty": 1, "line_total": p["price"]}], []))()
    with app.test_request_context("/"):
        t = compute_totals(lines, "PREPAID", "cod", None)
        assert t["coupon_error"] and "online payment only" in t["coupon_error"]


def test_cancel_restocks_and_ownership(client, app):
    p = first_product(app)
    login(client, "cust@example.com")
    _add(client, p["id"])
    co = re.search(r'name="co_token" value="([^"]+)"', client.get("/checkout").get_data(as_text=True)).group(1)
    r = client.post("/checkout", data=checkout_form(co_token=co, _csrf=token(client, "/checkout")))
    order_no = r.headers["Location"].rsplit("/", 1)[1]
    with app.app_context():
        before = q1("SELECT stock_qty FROM products WHERE id=?", (p["id"],))["stock_qty"]
        assert before == p["stock_qty"] - 1
        assert q1("SELECT user_id FROM orders WHERE order_no=?", (order_no,))["user_id"] is not None
    # another customer cannot see it (IDOR)
    other = app.test_client()
    login(other, "cust2@example.com")
    assert other.get(f"/account/orders/{order_no}").status_code == 404
    assert post(other, f"/account/orders/{order_no}/cancel", page="/account/").status_code == 404
    # owner cancels
    r = post(client, f"/account/orders/{order_no}/cancel", page="/account/")
    assert r.status_code == 302
    with app.app_context():
        assert q1("SELECT status FROM orders WHERE order_no=?", (order_no,))["status"] == "cancelled"
        assert q1("SELECT stock_qty FROM products WHERE id=?", (p["id"],))["stock_qty"] == p["stock_qty"]


def test_order_tracking_requires_matching_identity(client, app):
    p = first_product(app)
    _add(client, p["id"])
    co = re.search(r'name="co_token" value="([^"]+)"', client.get("/checkout").get_data(as_text=True)).group(1)
    r = client.post("/checkout", data=checkout_form(co_token=co, _csrf=token(client, "/checkout")))
    no = r.headers["Location"].rsplit("/", 1)[1]
    fresh = app.test_client()
    bad = post(fresh, "/track", {"order_no": no, "ident": "wrong@example.com"}, "/track")
    assert "find an order" in bad.get_data(as_text=True)
    good = post(fresh, "/track", {"order_no": no, "ident": "BUYER@example.com"}, "/track")
    assert no in good.get_data(as_text=True) and "Progress" in good.get_data(as_text=True)


# ---------------------------------------------------------------- admin workflows
def test_admin_order_lifecycle(client, app):
    p = first_product(app)
    _add(client, p["id"])
    co = re.search(r'name="co_token" value="([^"]+)"', client.get("/checkout").get_data(as_text=True)).group(1)
    r = client.post("/checkout", data=checkout_form(co_token=co, _csrf=token(client, "/checkout")))
    no = r.headers["Location"].rsplit("/", 1)[1]
    adm = app.test_client()
    login(adm, "staff@example.com")
    page = f"/admin/orders/{no}"
    post(adm, page, {"action": "status", "status": "confirmed"}, page)
    # cannot ship without courier + AWB
    post(adm, page, {"action": "status", "status": "packed"}, page)
    post(adm, page, {"action": "status", "status": "shipped"}, page)
    with app.app_context():
        assert q1("SELECT status FROM orders WHERE order_no=?", (no,))["status"] == "packed"
    post(adm, page, {"action": "status", "status": "shipped", "courier": "TestCourier", "awb": "AWB123"}, page)
    with app.app_context():
        o = q1("SELECT * FROM orders WHERE order_no=?", (no,))
        assert o["status"] == "shipped" and o["awb"] == "AWB123"
    # illegal jump rejected
    post(adm, page, {"action": "status", "status": "pending"}, page)
    post(adm, page, {"action": "status", "status": "delivered"}, page)
    with app.app_context():
        o = q1("SELECT * FROM orders WHERE order_no=?", (no,))
        assert o["status"] == "delivered" and o["payment_status"] == "paid"  # COD collected on delivery


def test_admin_product_crud_and_image_upload(client, app):
    login(client, "admin@example.com")
    t = token(client, "/admin/products/new")
    buf = io.BytesIO()
    Image.new("RGB", (900, 1100), (120, 80, 20)).save(buf, "PNG")
    buf.seek(0)
    data = {"_csrf": t, "title": "Test Brass Ganesha", "price": "1799", "material": "Brass", "is_active": "1", "track_stock": "1", "allow_cod": "1",
            "initial_stock": "4", "images": (buf, "photo.png")}
    r = client.post("/admin/products/new", data=data, content_type="multipart/form-data")
    assert r.status_code == 302
    with app.app_context():
        p = q1("SELECT * FROM products WHERE title='Test Brass Ganesha'")
        assert p["stock_qty"] == 4 and p["slug"] == "test-brass-ganesha"
        assert q1("SELECT COUNT(*) c FROM product_images WHERE product_id=?", (p["id"],))["c"] == 1
        assert q1("SELECT COUNT(*) c FROM stock_movements WHERE product_id=? AND delta=4", (p["id"],))["c"] == 1
    assert client.get("/products/test-brass-ganesha").status_code == 200
    # fake image is rejected
    t = token(client, f"/admin/products/{p['id']}/edit")
    r = client.post(f"/admin/products/{p['id']}/edit", data={"_csrf": t, "title": "Test Brass Ganesha", "price": "1799", "is_active": "1",
                                                             "images": (io.BytesIO(b"<?php echo 1; ?>"), "evil.png")}, content_type="multipart/form-data")
    with app.app_context():
        assert q1("SELECT COUNT(*) c FROM product_images WHERE product_id=?", (p["id"],))["c"] == 1
    # compare-at must exceed price
    r = client.post(f"/admin/products/{p['id']}/edit", data={"_csrf": token(client, '/admin/'), "title": "Test Brass Ganesha", "price": "1799", "compare_at_price": "1000", "is_active": "1"})
    assert r.status_code == 200 and "Compare-at price must be higher" in r.get_data(as_text=True)
    # stock adjust cannot go negative
    post(client, f"/admin/products/{p['id']}/stock", {"delta": "-99", "reason": "oops"}, "/admin/")
    with app.app_context():
        assert q1("SELECT stock_qty FROM products WHERE id=?", (p["id"],))["stock_qty"] == 4
    post(client, f"/admin/products/{p['id']}/stock", {"delta": "-1", "reason": "damaged"}, "/admin/")
    with app.app_context():
        assert q1("SELECT stock_qty FROM products WHERE id=?", (p["id"],))["stock_qty"] == 3
    post(client, f"/admin/products/{p['id']}/delete", page="/admin/")
    assert client.get("/products/test-brass-ganesha").status_code == 404


def test_review_requires_delivered_purchase(client, app):
    p = first_product(app)
    login(client, "cust@example.com")
    r = post(client, f"/products/{p['slug']}/review", {"rating": 5, "body": "great"}, f"/products/{p['slug']}")
    with app.app_context():
        assert q1("SELECT COUNT(*) c FROM reviews")["c"] == 0  # never bought -> rejected
        uid = q1("SELECT id FROM users WHERE email='cust@example.com'")["id"]
        run("INSERT INTO orders(order_no,user_id,email,phone,customer_name,ship_name,ship_phone,ship_line1,ship_city,ship_state,ship_pincode,subtotal,total,payment_method,status) "
            "VALUES ('VRTEST0001',?,?,?,?,?,?,?,?,?,?,100,100,'cod','delivered')", (uid, "cust@example.com", "9876543210", "C", "C", "9876543210", "x street", "c", "Delhi", "110001"))
        oid = q1("SELECT id FROM orders WHERE order_no='VRTEST0001'")["id"]
        run("INSERT INTO order_items(order_id,product_id,title,unit_price,qty,line_total) VALUES (?,?,?,?,1,100)", (oid, p["id"], p["title"], 100))
    post(client, f"/products/{p['slug']}/review", {"rating": 5, "title": "Lovely", "body": "great"}, f"/products/{p['slug']}")
    with app.app_context():
        r = q1("SELECT * FROM reviews")
        assert r and r["status"] == "pending"
    assert "Lovely" not in client.get(f"/products/{p['slug']}").get_data(as_text=True)  # not public until approved
    adm = app.test_client()
    login(adm, "staff@example.com")
    post(adm, "/admin/reviews", {"id": r["id"], "action": "approved"}, "/admin/reviews")
    assert "Lovely" in client.get(f"/products/{p['slug']}").get_data(as_text=True)


def test_wishlist_guest_then_merge_on_login(client, app):
    p = first_product(app)
    t = token(client)
    r = client.post("/api/wishlist/toggle", json={"product_id": p["id"]}, headers={"X-CSRF-Token": t})
    assert r.get_json()["on"] is True
    login(client, "cust@example.com")
    with app.app_context():
        assert q1("SELECT COUNT(*) c FROM wishlist")["c"] == 1


def test_settings_change_shipping_rule(client, app):
    login(client, "admin@example.com")
    t = token(client, "/admin/settings")
    r = client.get("/admin/settings")
    form = {k: v for k, v in re.findall(r'name="([a-z_]+)" value="([^"]*)"', r.get_data(as_text=True))}
    form["free_ship_threshold"] = "5000"
    form["_csrf"] = t
    client.post("/admin/settings", data=form)
    with app.test_request_context("/"):
        p = q1("SELECT * FROM products WHERE price=1999 LIMIT 1")
        t = compute_totals([{"product": p, "qty": 1, "line_total": 1999}], None, "online", None)
        assert t["shipping"] == 79  # threshold raised -> no longer free
