# VRINDAVAN store

A mobile-first e-commerce site for devotional murtis: storefront, customer accounts, and an admin panel with roles. Python 3 · Flask · SQLite · server-rendered (no JavaScript framework; ~10 KB of JS).

> **Status: working build, NOT launch-ready.** The business validation gates (supplier, samples, tax, courier, payment, trademark) are still open and parked. Everything that depends on them is configurable or left off. See "Before you go live".

## Run it
```bash
python -m venv .venv
.venv\Scripts\activate            # Windows   (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
flask --app run seed              # collections + clearly-labelled SAMPLE products with placeholder images
flask --app run create-admin --email you@example.com      # random password -> instance/admin_credentials.txt
python run.py                     # http://127.0.0.1:5000   (admin: /admin)
```
Production-style serving: `waitress-serve --listen=0.0.0.0:8000 run:app` behind HTTPS, with `VR_HTTPS=1` set (secure cookies + HSTS).
Tests: `pytest -q`.

## Accounts and permissions
| Role | Can do |
|---|---|
| **Customer** | Browse, wishlist, checkout as guest or signed-in, order history, track/cancel (pending/confirmed), saved addresses, reviews after delivery (moderated) |
| **Staff** | Admin panel: orders (status, courier/AWB, COD confirmation), products (add/edit, no delete), inventory, review moderation, messages |
| **Admin** | Everything: settings, collections, customers, coupons, PIN rules, team/roles, outbox, audit log, product delete |

Security built in: scrypt password hashing, 10-char minimum, lockout after 5 failures (15 min), session reset on login, CSRF on every POST, strict CSP (no inline scripts/styles), `HttpOnly`/`SameSite` cookies, rate limits on login/search/checkout-adjacent endpoints, safe-redirect handling, upload validation (real image decoded and re-encoded to WebP, EXIF stripped, 8 MB cap), IDOR checks on orders/addresses, audit log for admin actions, no secrets in code (`instance/secret_key` generated on first run; override with `VR_SECRET_KEY`).

## What is configurable (Admin → Settings)
Free-shipping threshold (default ₹1,499), fee below it (₹79), heavy-item surcharge, COD on/off, **COD fee (₹49)**, **COD cap (₹3,999)**, announcement bar, delivery note, returns summary, store/legal details, GSTIN. PIN rules (Admin → PIN rules) can block COD, block delivery, or add a surcharge by PIN prefix. **These defaults are pilot hypotheses, not decisions.**

## Behaviour worth knowing
- Prices are whole rupees. Totals are recomputed on the server at checkout; the browser never supplies a price.
- Stock is decremented inside a write lock (`BEGIN IMMEDIATE`); two buyers cannot take the last unit. Cancelling returns stock; every change is logged (Inventory → movements).
- Online payment is **disabled** until a gateway is connected (setting `online_enabled`). COD works; orders start as `pending` and the team confirms them.
- Notifications are written to the **Outbox** (Admin → Outbox) — nothing is emailed or WhatsApped yet.
- Receipts say "not a GST tax invoice" until a GSTIN is entered in Settings.
- Products carry private fields (supplier, supplier SKU, cost, HSN, GST rate) that are never shown to customers; cost feeds the dashboard margin figure.
- "Evidence badges" (Measured by us / Photographed by us / Protective packing) only appear when ticked on the product.
- Sample products are flagged `is_demo`, show a "Sample" tag and placeholder images, and can be removed in one click (Admin → Products → Delete all sample products).
- Delivery estimates are **not invented**: the PIN checker confirms serviceability rules and COD eligibility and shows the configurable delivery note.

## Before you go live (open items)
1. Supplier route, samples, courier rates, GST/HSN (CA), trademark — see the Phase 0.5/0.6 validation files.
2. Connect a payment gateway (PayU is the conditional primary; see `VRINDAVAN_Payment_Gateway_Validation.md`): implement the gateway adapter in `app/checkout.py` (create payment → redirect → verified webhook marks `payment_status`), then set `online_enabled=1`.
3. Connect email/WhatsApp sending to the Outbox table (the hook points are the `outbox` inserts in `services.py` and `auth.py`).
4. Replace sample products and placeholder images with real, permitted photography; review every product description against the claim register.
5. Have a lawyer finalise the policy pages (then set “policy pages reviewed” in Settings to hide the draft notice).
6. Fonts: system stacks are used until the type specimen tests on real Android devices are done.
7. Logo: files in `design/brand-originals` are resized into `app/static/brand` (the favicon is a dev-only downscale pending an approved favicon). Confirm logo ownership before launch.
8. Production hardening: HTTPS, `VR_HTTPS=1`, regular SQLite backups (`instance/store.db` + `instance/media`), move rate limiting to Redis if you run several workers, consider Postgres if order volume grows.

## Layout
```
app/            Flask app (shop, checkout, account, admin, auth, services, security, images, cli)
app/templates/  Jinja templates (storefront, account, admin, pages)
app/static/     css/app.css (design tokens), js/app.js, brand/
instance/       SQLite DB, uploaded media, secret key (git-ignored)
tests/          pytest suite
design/         original logo files (untouched)
```
