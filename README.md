# VRINDAVAN: store + Shopify theme

This repo holds two ways to run the same storefront design ("Mandir at Dusk"):

| Folder | What it is | Use it when |
|---|---|---|
| `vrindavan-store/` | Standalone Flask + SQLite web app: storefront, customer accounts, admin with roles, stock log, COD/PIN rules | You want to own the backend, or prototype quickly |
| `vrindavan-theme/` | Shopify Online Store 2.0 theme (Liquid) with the same look | You want to sell on Shopify and let it handle checkout, admin and accounts |
| `VRINDAVAN_*.md/.csv` | Business validation work (suppliers, GST, courier, payments, pilot SKUs). Parked; the launch gates are still open | Reference only |

Status: working build, not launch-ready. The Shopify theme passes `shopify theme check` but has not been tried on a live store.

## Quick start
Flask app: see [`vrindavan-store/README.md`](vrindavan-store/README.md).
Shopify theme: zip the *contents* of `vrindavan-theme/`, then Online Store > Themes > Add theme > Upload zip. Setup checklist in [`vrindavan-theme/README.md`](vrindavan-theme/README.md).

## Using this as a template for another app (for example "Sportify")
Assumption: Sportify is a sports-goods store (jerseys, shoes, equipment). If it is something else, tell whoever maintains this and adjust section 4.

### 1. Copy and rename
```bash
git clone <this repo> sportify
cd sportify
git rm -r --cached . >/dev/null   # optional: start fresh history instead
rm -rf .git && git init
```
Rename `vrindavan-store` and `vrindavan-theme` to `sportify-store` and `sportify-theme`. Delete the `VRINDAVAN_*` business documents, or keep them as a pattern for your own validation work.

### 2. Rebrand (find and replace)
Search for `VRINDAVAN`, `Vrindavan`, `vrindavan`, `VR_` (env prefix) across both folders. Hot spots:
- Flask: `app/__init__.py`, `app/auth.py`, `app/services.py`, `app/templates/` (header, footer, home), `app/static/brand/` (logo files), `tools/prepare_brand.py`.
- Theme: `config/settings_schema.json`, `config/settings_data.json`, `sections/header.liquid`, `sections/footer.liquid`, `assets/wordmark.webp`, `assets/emblem.webp`, `assets/favicon.png`.

### 3. Re-skin
All colour and type live in CSS variables at the top of `app/static/css/dusk.css` (Flask) and `assets/theme.css` (theme). Change the palette (night maroon `#1B0A10`, gold `#E9B449`, kumkum CTA) to your brand colours and swap the fonts. Decorative motifs (arch image frames, toran edge, marquee) are classes you can drop or restyle.

### 4. Re-model the catalogue
| Devotional store concept | Sports store equivalent |
|---|---|
| Collections by deity (Ganesha, Krishna...) | Collections by sport or category (Football, Cricket, Running...) |
| Product fields: material, finish, height/width/depth, base included, origin region, story, care | size, colour, brand, gender, fit, material, season, care |
| "Measured by us / Photographed by us / Protective packing" badges | "Authentic", "Size guide verified", "Easy exchange" (only show what is true) |
| Festival band | Season or tournament campaign band |
| Deity rail / tiles | Sport rail / tiles |

Flask: edit the schema in `app/db.py`, product forms in `app/templates/admin/`, the seed data in `app/cli.py`, and the placeholder art in `app/sampleart.py`. Add a variants table if you sell sizes (this app has one price/stock per product).
Shopify: use native variants for size/colour, and update the metafield list in `vrindavan-theme/README.md`. Edit `snippets/product-card.liquid` and `sections/main-product.liquid` to show the new fields.

### 5. Business rules to revisit
Free-shipping threshold, shipping fee, COD fee and cap, and PIN rules are Settings with pilot values, not decisions. Set your own. Add returns and exchange rules (sizes make returns far more common than for idols), and check GST rates for your goods with a CA.

### 6. Before real customers
Run `pytest -q` (Flask). Connect a payment gateway. Replace all sample art with real photos. Set `VR_SECRET_KEY` (rename the prefix if you changed it) and `VR_HTTPS=1` in production. Never commit `instance/`.
