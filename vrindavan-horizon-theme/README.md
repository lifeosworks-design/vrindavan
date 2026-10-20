# Vrindavan (Horizon format) Shopify theme

Same look as the Vrindavan site ("Mandir at Dusk": night maroon, gold, kumkum buttons, arch frames, scrolling deity strip), packaged in the same file layout as a full Shopify theme export (blocks, sections, snippets, locales, JSON templates). It is built on Shopify's open-source Horizon theme, so the cart drawer, product page, collection filters, search, accounts and blocks all come from Horizon. Vrindavan's own look is added on top.

## What is Vrindavan-specific
- **Home page** sections: `vr-hero` (arch picture), `vr-marquee` (scrolling deity names), `vr-deity-rail` (Shop by deity tiles), Horizon product list (featured murtis), `vr-festival-band`, `vr-promise`.
- **Colours and type**: all six colour schemes are re-set to the Dusk palette (Theme settings > Colors). Headings use Playfair Display, body uses Inter.
- `assets/vr-theme.css`: Vrindavan styling for the `vr-*` sections only. Every rule is scoped under `.vr`, so it cannot change the rest of the theme.
- Brand files: `assets/vr-wordmark.webp`, `assets/vr-emblem.webp`, `assets/vr-favicon.png`.

## Upload
Zip the contents of this folder (files at the zip root; `vrindavan-horizon-theme.zip` is already built), then Online Store > Themes > Add theme > Upload zip file.

## After upload
1. **Logo**: Theme settings > Logo and favicon > upload `assets/vr-wordmark.webp` (themes cannot pre-set an image file) and the favicon.
2. **Collections**: create ganesha, krishna, lakshmi and hanuman (the deity tiles use these handles; change them in the Shop by deity blocks if yours differ).
3. **Hero picture**: Home page > Hero > pick a product or image. An emblem shows until you do.
4. **Menus**, policies, payments and GST: as in the main repo README (`vrindavan-theme/README.md`). PIN-code rules, COD fee and cap are not part of Shopify; use shipping rates or an app.
5. Product details such as material, finish and dimensions: add metafields and show them with Horizon's text blocks in the product template.

## Differences from the earlier plain `vrindavan-theme`
The earlier theme is a hand-built theme matching the Flask site everywhere (header, drawers, wishlist, filters). This one keeps Horizon's tested commerce pages and applies Vrindavan's look to the home page and the colour/type system, so product, cart and collection pages look Dusk-coloured but are Horizon's layouts.

## Notes
- Not previewed on a live store. Shopify's older checker (CLI 3.70) reports 168 offenses, identical to the unmodified Horizon export, so none come from the Vrindavan additions.
- Horizon is by Shopify; keep its license and attribution if you redistribute.
