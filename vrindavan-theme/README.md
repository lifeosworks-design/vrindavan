# VRINDAVAN Shopify theme ("Mandir at Dusk")

Online Store 2.0 theme ported from the Flask prototype. Shopify provides products, stock, orders, admin, staff permissions, customer accounts and checkout.

Status: passes `shopify theme check` (41 files, 0 offenses). It has NOT been previewed on a live store, so expect small visual tweaks on first load.

## Install
1. Zip the contents of this folder (files at the zip root, not inside a subfolder). `../vrindavan-theme.zip` is already built.
2. Shopify admin > Online Store > Themes > Add theme > Upload zip file.
3. Customize, then Publish.

## Setup checklist
**Collections** (handles matter for the deity tiles): ganesha, krishna, lakshmi, shiva, hanuman, durga, vishnu, plus any purpose collections (home-mandir, gifting, festival...).

**Menus** (Content > Menus): `main-menu` and `footer`.

**Pages** (Content > Pages): about, faq, shipping, returns, contact (template `page.contact`), wishlist (template `page.wishlist`).

**Metafield definitions** (Settings > Custom data > Products, namespace `custom`): material, finish, height_cm, width_cm, depth_cm (numbers), base_included (true/false), origin_region, story, care (text), measured_by_us, photographed_by_us, protective_packing (true/false). Collections: `custom.native_name` (text).
Only set the "measured/photographed by us" flags to true when it is actually true; the product page shows these as trust badges.

**Filters**: install Shopify Search & Discovery and enable filters (material, price, availability).

**Settings** (Customize > Theme settings): WhatsApp number, free-shipping threshold (1499), delivery/COD/returns notes, legal name, GSTIN, address, support contacts, social links.

**Store settings**: currency INR; shipping rate free above Rs 1,499 and Rs 79 below (pilot hypothesis); customer accounts = new customer accounts; policies filled in; taxes pending your CA's HSN/GST confirmation.

**Payments**: Shopify Payments is not available in India. Use Razorpay/PayU/Cashfree app + a manual "Cash on Delivery" method. Note PayU CommercePro COD requires login (no guest checkout) - verify before choosing.

**Reviews**: add any reviews app that supports app blocks and drop its block into the product page.

## What does not port from the Flask app
- PIN-prefix serviceability rules, COD fee/cap and COD limits -> use shipping zones/rates, a delivery-checker app, or a Shopify Function.
- Admin roles/permissions -> Shopify staff accounts and permissions.
- Stock movement log -> Shopify inventory history.
- Sample illustrations are placeholders; upload real product photos.
