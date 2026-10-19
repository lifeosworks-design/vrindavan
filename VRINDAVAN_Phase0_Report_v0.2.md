# VRINDAVAN — Phase 0 Report v0.2 (visual research, logo, suppliers, economics, decision framework)
Date: 2026-10-08 · Status: DISCOVERY ONLY — nothing built, bought, installed or connected. Supersedes the open items in v0.1.

## 0. Evidence rules and honest limits
- **VERIFIED** = I saw it myself (browser screenshot, fetched page, or pixel measurement of your logo files).
- **REPORTED ⚠** = from a secondary source (blog, law-firm note, vendor). Needs confirmation before any decision.
- **ASSUMPTION** = my placeholder number. Never treat as a supplier quote.
- **What I did visually:** a real browser at 390px and 1440px wide. The browser pane is small, so screenshots are low-resolution. I judged layout, hierarchy, density, sticky elements, loading behaviour and contrast; I could **not** judge subtle typography, animation smoothness or image quality at pixel level.
- **Not inspected:** cart drawers and checkouts (I did not start any purchase), filter interactions, desktop views of Vedansh / Mejuri / Satvik, and Awwwards / SiteInspire / Godly / Mobbin / Behance / Dribbble (blocked or not opened; "Commerce Cream" returned nothing). The out-of-category set below was chosen by me from known premium brands and then actually opened.
- **Correction to v0.1:** v0.1 assumed 18% GST. Newer reports say brass handicraft statues are at **5%** after the 22 Sep 2025 rate changes, and marble/wooden deities used as objects of worship are **exempt** ⚠. Economics below use 5% with an 18% sensitivity. A CA must confirm.

---
## 1. Logo analysis (3 files received — all transparent-background WebP/PNG)
| File | What it is | Size | Ink coverage* |
|---|---|---|---|
| 1 | Gold emblem: lotus-petal/ogee arch outline, three-dome temple with dhwaja flag, peacock feather (only colour accent is the teal/navy eye), bansuri with tassel, scrollwork, lotus | 1254² | 8% |
| 2 | Circular full-colour emblem: gold ring, temple, **blue** feather, flute with blue bands, lotus | 1254² | 11% |
| 3 | Wordmark "VRINDAVAN": bevelled/embossed gold serif, swash V and R, lotus divider with arrow-tipped rules | 2000×667 | 14% |
*share of pixels that are opaque (measured). All three are airy: lots of empty space around thin lines.

- **Dominant colours (measured, quantised):** Emblem 1 — champagne/light gold `#D29646`, `#E6AA5A`, highlight `#FAD282`, shadow `#BE8232`. Emblems 2 & 3 — saturated antique gold `#D2961E`, `#BE820A`, deep `#AA6E0A`/`#965A0A`. Peacock eye (visual estimate, not sampled): teal-green ≈ `#1A8A8A` into navy ≈ `#0F2A6B`. Blue/teal covers ~5% of emblem 1, ~16% of emblem 2, 0% of the wordmark.
- **Contrast (computed from the hex values):** `#D2961E` on white ≈ 2.6:1, `#BE820A` ≈ 3.3:1, `#965A0A` ≈ 5.6:1. → The logo gold is **decorative only**. Never use it for body text, links or small UI text; use the deep brass `#965A0A` or ink for anything readable.
- **Visual weight:** light and decorative; the wordmark is the heaviest element. The gradient/bevel rendering feels "premium jewellery" but, at small sizes and next to flat modern UI, can look dated/skeuomorphic.
- **Symbolism & cultural cues:** peacock feather (mor pankh) and flute (bansuri) = Krishna; cusped/ogee arch = Rajput-Mughal-Indic architecture; domes with flag = a Vrindavan-style temple; lotus = purity/Lakshmi. **The mark is explicitly Krishna/Vaishnava.** Good for a name like "Vrindavan"; it may under-signal for Shiva/Hanuman/Durga/Buddha buyers (risk R-B1). Not a reason to change the logo; a reason to lean on neutral category naming in the UI.
- **Complexity & scalability:** emblems are detailed (feather barbs, thin arch lines, tassel). They hold up at ≥ 96px; below ~64px thin strokes and the feather barbs disappear. Wordmark is legible down to roughly 110px wide; below that the swashes and thin serifs fail.
- **Mobile header:** wordmark at ~110–130px wide (≈ 36–44px tall) fits a 56px header. The emblem does **not** belong in the mobile header.
- **Favicon:** none of the files is a favicon as-is. The peacock **eye** on a gold/ivory disc is the strongest 16–32px candidate. That is a *new derivative asset* (not modifying the logo) — needs owner/designer approval.
- **Footer:** emblem 1 at 96–128px, centred, mono gold on ivory or ink — a quiet brand "stamp".
- **Answer to A/B/C/D:** **C + D.** The wordmark carries the name in the header (both breakpoints); the emblem is used as a *brand mark at brand moments* (hero accent, footer, packaging insert, 404, loading, social avatar). Header is simplified on mobile (wordmark only, no tagline), slightly larger on desktop (wordmark ≈ 160–180px wide, centred or left).
- **Two emblem versions:** pick one canonical. Recommendation: **emblem 1** (mono gold + single teal eye) is the most elegant and flexible → primary mark; **emblem 2** (circle, full colour) → social avatar / WhatsApp business profile / app-icon style uses where a container shape helps.
- **Assets to request (owner/designer, not me modifying anything):** vector (SVG) or ≥ 3000px masters; a **flat single-colour** wordmark (ink and deep-brass versions) for small sizes, dark mode and print; a favicon/app-icon derivative; clear-space and minimum-size rules.
- **How the surrounding UI should behave so the logo doesn't compete:** flat ivory/neutral surfaces; no ornamental borders, mandalas, gold gradients or gold buttons; one accent colour (deep brass) for micro-details; all decoration reserved for the logo itself; generous space around the header logo; product photography is the only rich colour on the page; the lotus-arch shape may be reused **once per page** (e.g., as an image crop on the hero), not as a repeated pattern.

---
## 2. Visual competitor research (390px mobile + 1440px desktop)
### What I actually looked at
| Site | Mobile 390 | Desktop 1440 |
|---|---|---|
| Statue Studio | home (top, mid-scroll) | home |
| Satvik Store | collection top, PDP + scroll | — |
| Jaypore | collection, PDP + scroll | PDP |
| Exotic India | home | home |
| Vedansh Craft | home (first paint) | — |
| Luxe Artisanship | home | home |
| The Stone Studio | home | home |
| The Citizenry | home, PDP + scroll | home |
| Mejuri | home | — |

### Observations and the *why*
- **Statue Studio** — Always-visible search bar under the header eats ~60px of the first screen on a 844px phone; rotating social-proof toasts ("X ordered…") sit bottom-left permanently and cover product cards. Dark brass photos behind white hero text reduce legibility. On desktop the hero image was still a blank grey block after 3s → slow first paint on the most important element. Cards carry a red "Save Rs." line and a Sale badge on nearly all items, so the badge carries no information. *Works:* round collection thumbnails (fast to scan), horizontal rails.
- **Satvik Store** — Two stacked black bars plus a ticker before content; hero is a flattened promo graphic with red "#1 ARTISANAL" text baked into the image (not responsive, not accessible, shouts "marketplace"). On the PDP three sticky layers fight for the bottom of the screen at once: text nav bar (Home / About / Login / TrackOrder / Whatsapp / International…), a sticky product mini-bar and a floating chat bubble. The Add-to-cart button is a thin outline (weak affordance) and the page continues into banner-style ads ("Lacquer Protected", "Free Jap Mala"). *Works:* clear size/price/strike price hierarchy; four-photo gallery with thumbnails on plain backgrounds; the "Tax included" line.
- **Jaypore** — The best *mobile commerce mechanics* of the set: breadcrumb + result count ("301 products"), two-column grid, a floating **Sort / Filter pill** fixed at the bottom thumb zone, PDP with swipe gallery (arrows + dots), a full-width **sticky red Add to Cart**, inline **PIN-code delivery check**, "Inclusive of GST", material tag and size chip. *Fails:* images loaded as grey skeletons for 5+ seconds on the collection page (perceived slowness); shows **"No Returns*"** next to Free Shipping on the PDP (it states a trust-negative at the buy box); "1 Left" scarcity cue; discounts of 47–65% off. Desktop PDP is a standard marketplace layout (thumbnails left, image, buy box right) — competent, not distinctive.
- **Exotic India** — The most contemporary Indian idol site: warm cream background, rounded hero card with a serif headline and one highlighted word, pill CTAs, search field with a real example placeholder, announcement marquee, and a 2×2 trust grid (hand-cast / sacred forms / certified / insured). Strong because it has a *system* (radius, type pairing, one orange accent). Weak: white headline over a busy brass image (contrast drops at the right edge), orange is very saturated, and the deity/size/occasion routes duplicate each other (observed in v0.1).
- **Vedansh Craft** — At first paint the top of the page was an empty white area (~600px) before the hero image, i.e. layout waiting on JS; a green WhatsApp button floats over the product image; once loaded, the Krishna photo against a red curtain is warm and appealing. Lesson: don't hide the header/hero behind JS; reserve space and render the logo immediately.
- **Luxe Artisanship** — Tall full-bleed AI-style "gifting" hero with tiny baked-in text (illegible at 390px); an evil-eye ornament overlays the header corner; a "70% Stock Clearance Sale" sticker floats over the press-logo bar; ticker + floating round widget. Looks busy and discount-led despite a warm beige palette that could be premium.
- **The Stone Studio** — Calm cream hero, large bold sans headline, one gold button, angled collage of real placement photos. It is the *calmest* mobile hero among idol sites, but the type is generic (Roboto-class) and the collage shows watermarked, mixed-quality customer photos. Desktop mirrors it as a split hero.
- **The Citizenry** (benchmark) — Letter-spaced centred wordmark; full-bleed lifestyle imagery; on the PDP: **gallery with the next image peeking** (affordance for swipe), **provenance line next to the star rating** ("Crafted in Portugal"), colour swatches, size buttons, full-width Add to bag, instalment line, **"In stock, ready to ship · Free shipping"** pill, then **three accordions (Story / Product Details / Shipping & Returns)**. A cookie sheet covers ~30% of the first screen (a cost of consent UX; ours must be compact).
- **Mejuri** (benchmark) — Black announcement bar with arrows, a stat-driven story module over a leaf photo, a giant vertical wordmark beside the product, a **pause control** on the auto-advancing hero, and underlined text CTAs. Strong story-to-product link; the neon-lime accent is Mejuri's own and not transferable.

### Comparison table
| Website | Mobile UX | Desktop UX | Photography | Typography | Brand feel | Conversion UX | What to borrow | What to avoid |
|---|---|---|---|---|---|---|---|---|
| Statue Studio | Rails + round collection thumbs; toasts and search bar crowd the screen | Classic centred-logo + nav; slow hero | Dark brass on black, mixed | Serif logo + sans body, uppercase nav | Mid-market catalogue | Free-shipping and tax line in cart; Sale badges on everything | Round deity thumbnails | Persistent toasts, blank slow hero, sale on all |
| Satvik | Cluttered: 2 bars, ticker, 3 sticky layers | — | Plain-background gallery OK; hero is a graphic ad | Generic sans | Marketplace/ad | Weak outline ATC, add-on banners | Size-first, "Tax included" | Text baked into images, stacked sticky UI |
| Jaypore | Best mechanics (sort/filter pill, sticky ATC, PIN check) but slow images | Standard marketplace PDP | Clean studio on warm backdrop | Refined serif logo + sans | Curated lifestyle retailer | Strongest buy-box (pincode, GST, sticky) | Sticky ATC, PIN-check, bottom filter pill, breadcrumb+count | "No Returns*" at buy box, deep discounts, skeleton delay |
| Exotic India | Coherent system; hero contrast issue | Mega-category bar + hero card + trust row | Warm lit brass | Serif headline + sans | Modern heritage | Trust grid, search-first | Cream bg, hero card, trust grid, pill CTA | Saturated orange, duplicate routes |
| Vedansh | Empty first screen, floating WhatsApp | — | Good warm photography once loaded | Sans | Generic one-stop | Offer stack unclear | Product photo with context | JS-gated header, discount stack |
| Luxe | Beige palette; tiny baked-in text, overlays | Banner + press strip | AI-like staged gifting | Serif accents | Gift/lifestyle but sale-led | Ticker incl. COD / same-day | Warm neutral palette | Sticker overlays, ornaments on header |
| Stone Studio | Calm hero, collage | Split hero | Real placement photos (watermarked) | Generic sans | Honest, founder-led | Single CTA | One-CTA hero, placement stories | Watermarks, generic type |
| The Citizenry | Excellent PDP structure; cookie sheet heavy | Full-bleed editorial hero | Editorial lifestyle | Letter-spaced sans + italic serif | Global artisan, premium | Ready-to-ship pill, accordions, instalments | Provenance next to rating, accordions, peek gallery | Promo-led hero (sitewide sale) |
| Mejuri | Story modules, pause control | — | Studio macro + abstract | Bold grotesk | Modern fine jewellery | Underlined CTAs; policies in footer | Story ↔ product link, pause control | Brand-specific neon |

---
## 3. Out-of-category creative research (8 sites opened; 390px)
| Site | Category | What I saw (mobile) | Pattern worth stealing |
|---|---|---|---|
| The Citizenry | Artisan home | Described above | Provenance beside rating; accordions; "ready to ship" pill |
| Mejuri | Jewellery | Stat-story hero, pause, text CTAs | Story-linked proof; accessible pause |
| Good Earth (India) | Luxury home | Hero is a **pattern collage of the products on white** with one burgundy medallion + "Discover gifting"; pause control; cookie sheet | Brand "print language" as hero; the product collage doubles as identity |
| Jonathan Adler | Design-led home | Full-bleed object photo, bold navy wordmark, single grey CTA, stacked offer bars | Objects as sculpture photographed big; bold simple CTA |
| Tanishq (India) | Jewellery | Search bar with **camera + mic** icons; celebrity hero; consent sheet with **Reject All** | Search prominence; fair consent buttons |
| Ferm Living | Danish furniture | Transparent header over a hero, tiny stacked wordmark, serif headline, outlined button; below-fold sections empty on first paint | Restrained header; editorial serif — but avoid blank lazy sections |
| Kama Ayurveda (India) | Luxury Ayurveda | Category ticker (Skincare • Gifting • Haircare…), festival hero, gift thresholds ("gifts worth ₹1,770 above ₹2,500"), blurred-colour category tiles | Festive gift-threshold mechanic; quick category chips |
| Our Place | Cookware | Hero video with pause, serif headline, terracotta CTA; **3 overlays at first paint** (announcement + region modal + cookie banner) | Warm terracotta CTA; AVOID stacked overlays |
(Not opened: Awwwards, SiteInspire, Godly, Mobbin, Behance, Dribbble, Shopify showcase. Awwwards' e-commerce honourees in 2026 per search listing: Bucks Sauce, Outfit, Pixel Vault, Drop Edition, Gielly Green, LAB46 — names only, not inspected.)

### Scored creative ideas (Brand / Conversion / Mobile usability: higher = better · Performance risk / Complexity: higher = worse)
| Idea | Brand | Conv | Mobile | Perf risk | Complexity | Verdict |
|---|---|---|---|---|---|---|
| Provenance line beside rating ("Hand-cast in Moradabad · Brass") | 8 | 7 | 9 | 1 | 1 | **Adopt** (only with real origin data) |
| Sticky Add-to-cart + inline PIN-code delivery check | 5 | 9 | 10 | 1 | 2 | **Adopt** |
| Bottom floating Sort/Filter pill → bottom-sheet filters | 4 | 8 | 10 | 1 | 3 | **Adopt** |
| Gallery with next image peeking + dot count | 6 | 6 | 10 | 2 | 2 | **Adopt** |
| PDP accordions: Story / Details / Shipping & Returns | 6 | 7 | 9 | 1 | 1 | **Adopt** |
| "Ready to ship" / delivery pill at buy box (only if true) | 5 | 8 | 9 | 1 | 1 | **Adopt (when proven)** |
| Hero = one sculpture, warm neutral set, single CTA | 9 | 6 | 8 | 2 | 2 | **Adopt** |
| Find by deity / by space (pooja room, desk, car) / by occasion tiles | 6 | 8 | 9 | 1 | 2 | **Adopt** |
| Lotus-arch image crop used once per page (from the logo) | 8 | 4 | 8 | 1 | 3 | **Adopt sparingly** |
| Story-linked proof ("12-step hand finishing, every piece inspected") | 7 | 7 | 8 | 1 | 1 | Adopt if operationally true |
| Short 5–8s product video on hero SKUs (poster + lazy) | 8 | 6 | 7 | 5 | 4 | Limited use |
| Dark "festival edit" band (Navratri/Diwali) | 8 | 6 | 7 | 2 | 2 | Adopt seasonally |
| Gift-threshold mechanic (Kama-style) | 5 | 7 | 8 | 1 | 3 | Test later |
| Instalment/EMI widget (PayU "Affordability widget" exists per PayU docs) | 5 | 7 | 8 | 3 | 4 | Phase 2 for ₹5k+ |
| Camera/voice search | 3 | 5 | 7 | 4 | 8 | **Reject for MVP** |
| 360° viewer | 4 | 3 | 5 | 8 | 7 | **Reject** |
| Scroll-jacking / WebGL / cursor effects | 5 | 1 | 2 | 9 | 9 | **Reject** |
| Social-proof toasts ("Bhushan ordered…") | 1 | 3 | 2 | 3 | 2 | **Reject** |
| Countdown timers / "1 left" scarcity | 1 | 2 | 5 | 1 | 1 | **Reject** |
| Stacked overlays at first paint (announcement + region + cookie + chat) | 1 | 1 | 1 | 4 | 2 | **Reject** |

---
## 4. Three visual directions
**A — "Quiet Mandir Gallery"** (modern temple + gallery)
- Palette: ivory `#FAF6EE`, stone surface `#F2EBDD`, ink `#1F1A16`, secondary text `#5B5249`, deep brass `#965A0A` (text-safe accent), logo gold `#D2961E` (decor only), peacock teal `#0E6E6E` (links/focus), navy `#12306B` (rare).
- Background: warm ivory; sections alternate ivory/stone; no patterns. Text ink. Accent: deep brass hairlines and small caps labels.
- Type: high-contrast editorial serif for headlines (Devanagari-capable family preferred), neutral humanist sans for UI; two families max, self-hosted, subset.
- Photography: warm stone sweep, soft side light, one scale shot per SKU, one in-situ pooja shelf.
- Borders: hairline 1px stone; no ornamental frames. Cards: borderless, image-led, 4:5 ratio, small radius (4–6px). Buttons: solid ink primary, outlined secondary; deep brass only for tiny accents; 48px height. Icons: 1.5px outline, rounded, custom lotus/diya sparingly.
- Animation: only feedback (≤200ms), image cross-fade; respects reduced-motion.
- Homepage mood: calm gallery; one sculpture hero; deity/space/occasion tiles. Product page: museum label feel (specs as a clean table). Mobile: single column, sticky ATC, bottom filter pill. Desktop: asymmetric 12-col editorial grid, sticky buy box, generous whitespace.

**B — "Peacock Night Sanctum"** (dark editorial)
- Palette: deep ink-teal `#0F1B1E`, surface `#162428`, ivory text `#F3EBDD`, gold `#E6AA5A`, teal `#2BA3A0`. Photography: brass lit like a diya in a dark room. Borders: hairline gold at 20% opacity. Cards: dark surface, image bleeds. Buttons: gold fill/ink text. Icons: thin gold line. Animation: slow fades and a soft glow on hover (desktop only). Homepage mood: nocturnal, cinematic. Product page: product as a lit object. Mobile: strong but needs high brightness; desktop: dramatic.
- Risks: supplier photos on white will look pasted; dark UIs are harder to read outdoors on budget panels; gold text contrast depends on exact tones; heavier imagery needed.

**C — "Marigold Atelier"** (contemporary Indian craft, colour-led)
- Palette: warm cream `#FFF8EC`, terracotta `#B4472B`, marigold `#F2A900`, indigo `#1F2A5A`, ink. Photography: bright, colourful props (flowers, textiles). Borders: soft rounded 12–16px. Cards: tinted backgrounds. Buttons: terracotta solid. Icons: filled, playful. Animation: gentle marquee-style rails. Homepage mood: festive, joyful. Product page: lifestyle-heavy. Mobile: rails and colour blocks; desktop: collage grids.
- Risks: feels closest to Kama/Good Earth and competes with the logo's gold/teal; festive colours date quickly; easiest to drift into "bazaar".

### Recommendation: **Direction A**, with a seasonal "festival edit" band borrowed from B
Why: (1) the logo is gold, thin-lined and detailed → needs a quiet ivory/ink surround, otherwise gold-on-gold clutter; (2) the market's problem is noise and distrust, so calm is the differentiator; (3) brass and stone photograph best on warm neutral and it tolerates mixed supplier photography better than a dark theme; (4) lowest performance cost; (5) contrast is controllable (gold stays decorative); (6) A scales to ₹1,000 gifts and ₹8,000 showpieces without changing character.

---
## 5. Supplier research (no suppliers invented; every entry is a lead until verified)
Method: web searches, B2B profile pages, official site pages I could fetch. **Nothing below has been contacted.** B2B listing pages are self-reported marketing.

### A. VERIFIED DROPSHIPPING (platform states it; fit for idols NOT verified)
| Name | What I verified | What I could NOT verify |
|---|---|---|
| **Baapstore** (baapstore.com) | Own site says it offers **white-label dropshipping access to 5,000+ products** on a subscription, orders dispatched **under your brand name**, "COD Available", it handles "shipping, tracking, and COD settlement"; provides product sheets for Shopify/Amazon/WooCommerce | Visible categories were apparel, kitchenware and storage — **no idols/pooja/décor seen** (page truncated); pricing, shipping charge, RTO/return terms, MOQ, plan cost, Shopify app status (search snippets conflict: "50,000+" vs "150,000+" products; one blog quotes ₹39 flat shipping — unverified) |

### B. POSSIBLE BUT UNVERIFIED
| Name | Why it's listed | Status |
|---|---|---|
| GlowRoad | Appears in guides/forum as an India resale/dropship platform with COD; Amazon announced acquisition in 2022 | Current status/terms conflict (one forum post says it stopped for Indian users; 2026 blogs list it as active). **Not confirmed active.** Idol availability unknown |
| Platforms listed in blogs (Roposo, Meesho-style resale apps) | Mentioned by roundups | Marketplace/reseller apps, not manufacturer fulfilment; quality/brand control weak |

### C. WHOLESALE / MANUFACTURER — REQUIRES DIRECT OUTREACH (not dropshipping until they say so in writing)
*Brass:* Kamal Metals (Moradabad, IndiaMART), Aakrati Brassware (Aligarh, TradeIndia), Indian Culture Handicraft (Jaipur, TradeIndia), Yaqub Handicrafts (Moradabad), Vedic Vaani (Mumbai; lists GST + IEC), Keshav Enterprises (Aligarh; MOQ 1 kg on listing), Shahab Metal Crafts (Moradabad; MOQ 70 pcs on a thali listing). *Miraya International (Moradabad)* shows **MOQ 500 pcs** on a Nataraja listing → unsuitable unless exception.
*Resin / polyresin / composite:* Arham Trades (Jaipur), Craftam (Jaipur; listing shows MOQ 1), Bemount Creations (Loni UP), Keshav Arts (Mathura), Satyam Gifts (Mumbai; MOQ 1, "dispatch within 3 days" claim on listing), Rati Greentech (Delhi), P&R Groups / Elysee Decor (Muzaffarnagar). *Note:* several "resin" listings are actually fibre or marble-powder composites.
*Marble:* Harihar Murti Bhandar, Icones Moorti Creation, Moorti India, Riddhi Siddhi Marble Moorti Art, Sai Sagar Arts, Jaipur Marble Emporium (all Jaipur; wholesale; heavy/fragile).
*Retailer-manufacturers with a trade route:* The Stone Studio (wholesale page: **terms negotiated case by case**, contact by phone/form; no dropship terms stated); Exotic India (official wholesale page returned 404; a Faire wholesale brand page and an 8% affiliate programme appear in search — affiliate is *not* supply; wholesale terms unverified).

### D. NOT SUITABLE
Meesho / IndiaMART / TradeIndia / ExportersIndia **as "dropshipping"** (directories/marketplaces); Qikink / Printrove (print-on-demand merchandise); CJ and other China-sourced platforms (import, wrong product origin for "handcrafted Indian art"); India-to-USA export dropship services (Seasonsway, ShoppRe, etc.); any supplier with a bulk MOQ ≥ 70 pcs for a pilot (e.g., Miraya 500).

### Shortlist by confidence
1. **Highest (actionable now):** Baapstore — ask for a catalogue extract and the pricing page; verify idol availability. 2–3 per-material manufacturers from C that show **MOQ 1 / sample-friendly** listings (Satyam Gifts, Craftam, Keshav Enterprises) — request samples.
2. **Medium:** Stone Studio (stone/Buddha, trade desk exists but terms unknown), Moradabad brass makers (Kamal, Yaqub, Aakrati) for per-order dispatch.
3. **Low/unknown:** GlowRoad, Exotic India wholesale, marble manufacturers (heavy freight).
**Conclusion:** **No supplier is a verified idol dropshipper.** The pilot (below) will create the evidence.

---
## 6. Supplier outreach templates (do not disclose volumes, margins, brand name or launch date)
**WhatsApp**
> Namaste. I'm setting up a small online décor/devotional store in India and am looking for a manufacturing partner for [brass / resin / marble] idols. Could you please share: (1) catalogue + wholesale rates, (2) whether you can ship single orders directly to my customers (dropshipping) with plain/unbranded packing, (3) MOQ, (4) GST invoice, (5) delivery time and courier used, (6) whether you accept COD and how RTO/returns are handled, (7) damage/replacement policy and packing method. I'd also like to order 2–3 samples. Thank you — [Name]

**Email** — Subject: *Partnership enquiry – single-order shipping & samples ([material] idols)*
> Dear [Supplier],
> I run a new India-based online store for devotional and décor pieces and am evaluating manufacturers for a pilot range. Could you please confirm the following in writing?
> 1. **Fulfilment:** Do you offer dropshipping (direct dispatch to my customers) with blind shipping — no supplier branding, invoice, or contact on the parcel?
> 2. **Branding:** White-label/private-label options (plain or custom box, insert card, custom tag) and their cost and MOQ.
> 3. **Pricing & MOQ:** Catalogue, wholesale rates by product, MOQ per SKU, price validity.
> 4. **Logistics:** Courier partners, shipping cost by weight/zone, dispatch time after order, delivery times, tracking number sharing, COD support and COD remittance cycle.
> 5. **Quality & loss:** Packing method for fragile items, damaged-in-transit and wrong-item replacement policy, RTO handling (who pays, restocking), return policy.
> 6. **Operations:** How orders are forwarded (WhatsApp/Excel/API/Shopify integration), inventory updates, stock-out handling.
> 7. **Compliance & content:** GST invoice, HSN code used, product images and permission to use them (and whether raw photos/video of the exact piece are available).
> 8. **Samples:** Sample order process, cost and lead time for [3] items.
> Please also share your GST number. Thank you — [Name, phone]

**IndiaMART short enquiry**
> Looking for [product/size] — need 2–3 sample pieces first. Please confirm: single-order dispatch to customers (dropship) with unbranded packing? MOQ, price/pc, GST invoice, dispatch time, courier, COD, damage replacement policy. Kindly send catalogue on WhatsApp [no.].

(Before paying anyone, verify GST/IEC numbers on the official portals; don't send advance payments beyond the sample cost.)

---
## 7. Sample-first pilot (neutral between pure dropship and hybrid)
**Pilot range: 8 SKUs × 2–3 units** (represents price, weight, material and size).
| # | SKU type | Material | Approx weight | Price tier |
|---|---|---|---|---|
| 1 | Small Ganesha 4–5" | Brass | 0.4–0.7 kg | ₹999–1,499 |
| 2 | Mid Lakshmi-Ganesha pair 6–8" | Brass | 1.5–2.5 kg | ₹2,999 |
| 3 | Radha-Krishna 9–12" | Brass | 3–5 kg | ₹4,999 |
| 4 | Large Krishna / Hanuman 15"+ | Brass | 6–9 kg | ₹7,999 |
| 5 | Ganesha 6–8" | Polyresin | 0.5–1 kg | ₹1,499–1,999 |
| 6 | Meditating Buddha 8–10" | Resin / composite | 1–2 kg | ₹1,999–2,999 |
| 7 | White deity 9–12" | Marble-composite (or marble if freight acceptable) | 3–8 kg | ₹2,999–4,999 |
| 8 | Painted/coloured brass 6" | Brass, painted | 1 kg | ₹1,999 |
Ship **10+ parcels** through the actual courier to: 2 metros, 3 tier-2/3 cities, 1 remote/hill pin code, 1 NE or J&K pin, 3 COD (to friends, with real COD collection). Statistics at this size are directional only.

**Scoring sheet per sample** — PRODUCT: finish defects, dimension/weight vs listing, colour vs photo, loose parts, smell/paint, base stability, packaging quality. SHIPPING: dispatch time, delivery days, damage, tracking quality, NDR behaviour, COD remittance time, RTO outcome. CUSTOMER: unboxing appearance, perceived value vs price, photo-vs-reality match (ask 3 testers). ECONOMICS: landed cost, price, payment fee, shipping, COD fee, packaging, expected RTO/replacement, contribution.

**PASS / FAIL criteria (proposed thresholds — tune after talking to supplier)**
- Critical defects (cracks, wrong deity, paint flaking, unstable): **0** → fail the SKU otherwise.
- Dimensions/weight within **±5%** of listing; colour judged "matches" by ≥ 2 of 3 testers.
- Parcels arriving damaged: **0 of 10** pilot parcels (any damage = fix packing and retest; two damages = fail supplier).
- Dispatch within **≤ 2 working days** of order for ≥ 90% of orders.
- Delivery **≤ 7 working days (metro), ≤ 10 (other)** for ≥ 80% of parcels; no unexplained NDRs.
- Tracking updated at least at pick-up, in-transit, out-for-delivery, delivered.
- COD remittance within the agreed cycle; RTO handling written and tested (restock without fee, or fee ≤ ₹X agreed).
- Contribution before ads ≥ **30% of ex-GST revenue (prepaid)** and ≥ **20% (COD blended)** at the target price, using real landed cost.
- Unboxing score ≥ 4/5 from testers; photo-reality match ≥ 4/5.

---
## 8. Unit economics (rebuilt; assumptions separated from facts)
### Verified / reported facts used
| Item | Value | Status |
|---|---|---|
| Shopify Payments not available in India; third-party gateway needed; Shopify adds 2% (Basic) / 1% (Grow) / ~0.6% (Advanced) on third-party gateways | secondary (PayGlocal, Razorpay blogs) | ⚠ REPORTED |
| Gateway fee ≈ 2% (Razorpay/PayU), Cashfree ~1.75–1.95% | vendor comparison | ⚠ REPORTED; confirm in writing |
| Delhivery 2–3 kg band ≈ ₹80–120; DTDC ₹100–150; Blue Dart ₹200–300 | third-party blog | ⚠ REPORTED; get real rate card |
| COD RTO 20–40% (home & kitchen 30–38% COD; 15–20% prepaid) | base.com vendor benchmark | ⚠ REPORTED, vendor-biased |
| GST on brass handicraft statues 5%; marble/wooden deities exempt (Sep 2025 onwards) | 2026 AAR commentary | ⚠ REPORTED; CA to confirm; older listings show 12% / 18% |
| PayU supports UPI in hosted app and COD via CommercePro COD | PayU docs | VERIFIED (docs); PayU fees **not** published |

### Assumptions used (ALL placeholders — not supplier pricing)
Supplier cost = **42% of GST-inclusive price** (target ceiling; sensitivity 50%) · GST 5% (sensitivity 18%) · shipping we pay by weight tier: ₹60 / 80 / 100 / 120 / 180 / 300 (for ₹999 … ₹7,999 SKUs) · packaging ₹25 / 30 / 35 / 45 / 70 / 110 · payment fee prepaid = gateway 2% + 18% GST on fee + Shopify 2% ≈ 4.4% of price · COD fee ₹40 courier cost (assumes no Shopify fee on manual payment methods ⚠) · COD RTO 30%, RTO costs forward + return shipping + packaging (goods resaleable, no supplier charge) · damage/replacement 5% of delivered orders, costing a full replacement (cost + shipping + packaging) with no supplier recovery · COD share 50%.

### Results per order placed, before advertising (₹, rounded)
| Price (incl. GST) | Supplier cost | Ship | Pack | Payment fee (prepaid) | COD fee | Expected RTO cost (COD) | Expected replace (prepaid) | **Contribution prepaid** | **Contribution COD** | **Blended (50/50)** = max viable CAC (break-even) |
|---|---|---|---|---|---|---|---|---|---|---|
| ₹999 | 420 | 60 | 25 | 44 | 40 | 44 | 25 | **378** | **224** | **301** |
| ₹1,499 | 630 | 80 | 30 | 65 | 40 | 57 | 37 | **586** | **371** | **478** |
| ₹1,999 | 840 | 100 | 35 | 87 | 40 | 70 | 49 | **793** | **518** | **656** |
| ₹2,999 | 1,260 | 120 | 45 | 131 | 40 | 86 | 71 | **1,230** | **839** | **1,034** |
| ₹4,999 | 2,100 | 180 | 70 | 218 | 40 | 129 | 117 | **2,076** | **1,449** | **1,762** |
| ₹7,999 | 3,360 | 300 | 110 | 349 | 40 | 213 | 188 | **3,311** | **2,321** | **2,816** |
- **Sensitivity (blended):** supplier cost 50% of price → ₹230 / 371 / 513 / 820 / 1,405 / 2,245. GST 18% → ₹212 / 345 / 477 / 767 / 1,316 / 2,103.
- **Recommended CAC ceiling = ~50% of blended** (leaves room for software, returns beyond model, fixed costs, and profit): ≈ ₹150 / 240 / 330 / 520 / 880 / 1,400. A ₹999 SKU with ₹150 CAC is nearly unachievable via paid ads → **sell it only as an add-on/gift, not an acquisition product**.
- **Software/app cost is not included per order** (Shopify Basic ≈ ₹1,499/mo yearly ⚠; apps) — at 100 orders/month, ~₹15–50/order.
- **Max discount:** at ₹2,999 a prepaid incentive of ₹100–150 stays inside the model; deeper blanket discounts do not.
- **COD risk:** COD is worth ₹150–600 less per order than prepaid in this model before conversion effects; the lever is verification and nudging. RTO 30% is a vendor benchmark; the pilot must measure ours.
- **Biggest unknown:** supplier cost ratio. If the real ratio is ≥ 55%, ₹999–1,999 SKUs go near zero.

---
## 9. Free shipping — options compared
| Option | Pros | Cons | Fit |
|---|---|---|---|
| A. Free on everything | Matches market (StatueStudio, Exotic India, Jaypore, Satvik all show free shipping); simplest | Loses money on ₹999 items and heavy (>3 kg) pieces; invites low-value COD | Only if every SKU ≥ ~₹1,999 |
| B. Free above ₹X | Protects small baskets; raises AOV | Customers compare against "free everywhere" sites | Good |
| C. Free on prepaid only | Pushes prepaid, cuts RTO | Penalises COD-heavy customers; may reduce conversion | Risky alone |
| D. Free above ₹X + small COD fee | Funds COD risk | Fee can hurt conversion (vendor warning ⚠) | Good with testing |
| E. Product-specific | Handles heavy/fragile realistically | Complex to message | Needed for heavy items |
**Recommendation: B + D + E.** (1) Free shipping on orders **≥ ₹1,499** (in price, not as a banner promise); (2) COD allowed with a **₹49 handling fee** (A/B test against a ₹100 prepaid discount in the soft launch); (3) items **> 3 kg** (large brass/marble) priced with freight embedded and labelled "Insured delivery included"; (4) don't sell standalone items below ~₹1,499 — bundle them or position as add-ons. Reason: shipping is ~4% of price at ₹2,999 but ~8% at ₹999, and COD RTO costs real money. No conversion data exists yet — it is a hypothesis for the pilot.

## 10. Delivery promise — evidence needed before "Delivery within 7 days"
Define and measure: **supplier SLA** (order forwarded → ready), **processing time** (confirmation + COD verification), **dispatch time** (pick-up scan), **courier SLA** (pick-up → delivered by zone), **remote-area exceptions** (pin-code serviceability), **COD delays** (OTP/confirmation delay). Required evidence: ≥ 30 completed orders across zones (pilot + soft launch); P80 (80th percentile) of order-to-delivery ≤ 6 working days and P95 ≤ 9 days for the claimed zone; written supplier dispatch SLA; courier rate card with zone TAT; PIN-code level estimate. **Rule: public promise = P90 of observed order-to-delivery + 1 working day buffer.**
**Safe wording until then:** *"Dispatched within 2–3 working days. Delivery time shown for your PIN code at checkout (most orders arrive in about 5–10 working days — estimate)."* → drop "most orders…" if the pilot doesn't support it; never say "7 days".

---
## 11. Decision framework — Pure dropship vs Stock-light hybrid
| Factor | Pure dropship | Stock-light hybrid |
|---|---|---|
| Capital requirement | Lowest (sample + ads) | Moderate (units of 8–10 SKUs, say ₹40–80k ⚠ ASSUMPTION) + storage |
| Inventory risk | None (supplier holds) | Dead stock, damage, festival timing |
| Margin | Lower wholesale discount, supplier takes margin | Better unit cost on repeated buys; extra handling cost |
| Delivery control | Low (depends on supplier dispatch) | High (you set dispatch) |
| Quality control | Low unless pre-dispatch photo/video check | High (inspect before packing) |
| Branding | Only if supplier supports blind/white-label packing | Full control: box, insert, invoice |
| Returns / damage | Slow, depends on supplier replacement | Fast replacement from stock |
| RTO | Product may not return to usable stock; supplier policy | You can restock |
| Scalability | Easy to add SKUs; breaks on ops complexity | Needs space/process; scales after demand proof |
| Customer experience | Variable | Consistent |
| Supplier dependency | High | Medium |
**Choose PURE DROPSHIP if the pilot shows ALL of:** ≥ 2 suppliers with written blind-shipping/white-label + replacement policies; 0 critical defects and 0 damaged parcels in pilot; dispatch ≤ 2 working days at ≥ 90%; delivery P90 inside the target; supplier handles RTO without fees or charges ≤ agreed cap; landed cost ≤ 42–45% ratio at target prices.
**Choose STOCK-LIGHT HYBRID if ANY of:** supplier won't do blind shipping/branding; any damaged parcel or inconsistent finish between units; dispatch SLA missed > 10%; RTO/replacement not recoverable; heavy items > 3 kg with high damage risk; best-sellers emerge (top 5 SKUs ≥ 60% of orders) — stock those, keep the long tail dropship.
**Also possible and common:** hybrid by SKU (stock best-sellers, dropship the rest). Decide **after** the pilot, not before.

---
## 12. Updated master roadmap
Legend: DONE · IN PROGRESS · BLOCKED · NEEDS DECISION · NEEDS EXTERNAL VERIFICATION · NOT STARTED
| Phase | Status | Note |
|---|---|---|
| 0 Discovery | **IN PROGRESS** (v0.2 done; awaiting your approval) | |
| 1 Brand + market research | **IN PROGRESS** | Logo analysed (done); customer interviews/keyword demand NOT STARTED |
| 2 Product/category strategy | **NEEDS DECISION** | 4 collections proposed; pilot SKUs need your picks |
| 3 Supplier research | **IN PROGRESS / NEEDS EXTERNAL VERIFICATION** | Leads only; outreach drafted, not sent |
| 4 Unit economics | **IN PROGRESS** | Model ready; needs real quotes |
| 5 Business/legal | **NEEDS DECISION + EXTERNAL VERIFICATION** | CA: GST registration/rate; trademark; entity |
| 6 Domain + email | **NEEDS DECISION** | availability not checked |
| 7 Shopify architecture | **IN PROGRESS** | native-first; blocked on plan/gateway choice |
| 8 Information architecture | **NOT STARTED** (draft in v0.1) | |
| 9 UX/wireframes | **BLOCKED** until direction A approved | |
| 10 Design system | **BLOCKED** until direction + logo assets | |
| 11 Mobile storefront | **BLOCKED** | |
| 12 Desktop adaptation | **BLOCKED** | |
| 13 Product data architecture | **NOT STARTED** | needs pilot specs |
| 14 Supplier workflow | **BLOCKED** (supplier choice) | |
| 15 Payments | **NEEDS EXTERNAL VERIFICATION** | PayU/Razorpay/Cashfree quotes |
| 16 COD | **NEEDS DECISION** | |
| 17 Shipping | **NEEDS EXTERNAL VERIFICATION** | real rate cards |
| 18 Returns/refunds | **NEEDS DECISION** | |
| 19–21 Accounts / Wishlist / Reviews | **NOT STARTED** | |
| 22–23 SEO / Analytics | **NOT STARTED** | |
| 24 Marketing | **NEEDS DECISION** | budget unknown |
| 25–27 Security / Accessibility / Performance | **NOT STARTED** (requirements drafted) | |
| 28 Testing | **NOT STARTED** | |
| 29 Soft launch / 30 Full launch / 31 Optimisation | **NOT STARTED** | |

## 13. Remaining blockers
1. Visual direction approval. 2. Logo masters (vector/flat/favicon derivative). 3. No verified idol dropship supplier — outreach + samples. 4. GST/legal confirmation and entity registration. 5. Gateway and courier quotes (PayU fees unpublished). 6. Product/SKU picks and photography plan. 7. Domain/trademark check. 8. Budget (marketing + pilot stock).

## 14. Exact next 5 actions
1. **You:** approve Direction A (or choose B/C) and send logo masters (SVG/flat/favicon request).
2. **You (with my drafts):** send the outreach to ~10–12 suppliers (4 brass, 3 resin, 2 marble, Baapstore, Stone Studio); I log replies against the scoring sheet.
3. **You:** request written rate cards — Shiprocket/Delhivery (by weight and zone, COD fee, RTO charge) and PayU, Razorpay, Cashfree (MDR, COD, settlement time).
4. **You + CA:** confirm GST registration need and rate for each material; check "Vrindavan" trademark/domain availability.
5. **Together:** pick the 8 pilot SKUs and order samples; I'll rerun §8 with real numbers, then we decide pure vs hybrid.

*Next decision: approve visual direction A and release the supplier outreach.*

---
### Sources (primary where available)
- PayU Shopify docs (primary): https://docs.payu.in/docs/shopify-faqs
- Baapstore (supplier's own site): https://www.baapstore.com/
- The Stone Studio wholesale page (supplier's own site): https://www.thestonestudio.in/wholesale/
- Competitor/benchmark sites opened: statuestudio.com, satvikstore.in, jaypore.com, exoticindiaart.in, vedanshcraft.com, luxeartisanship.com, thestonestudio.in, the-citizenry.com, mejuri.com, goodearth.in, jonathanadler.com, tanishq.co.in, fermliving.com, kamaayurveda.com, fromourplace.com
- GST reports (secondary): https://taxguru.in/?p=1072173 · https://www.msassociates.pro/gst/gst-handicraft.php · https://disytax.com/?p=19411 · https://www.patronaccounting.com/case-laws/aar/m-s-tushar-agarwal-advance-ruling-no-raj-aar-2026-27-10-dated-30-07-2026.pdf
- Courier ranges (secondary): https://www.shiprocket.in/blog/delhivery-courier-charges/ · https://wareiq.com/resources/blogs/courier-charges-in-india-per-kg/
- COD/RTO (vendor): https://base.com/en-IN/blog/cod-return-rates-by-product-category-in-india-2026-report/
- Shopify India fees (secondary): https://payglocal.in/blog/shopify-price-india-guide
- Supplier listings (B2B, self-reported): IndiaMART / TradeIndia / GlobalLinker profiles for the companies named in §5C
- Awwwards e-commerce list (not opened in detail): https://www.awwwards.com/websites/winner_category_ecommerce/
