# Sportify theme

A sports-gear Shopify theme (Online Store 2.0, sections-everywhere + theme blocks). It is built on Shopify's open-source **Horizon** theme, in the same file layout as a Shopify theme export, then re-skinned: black / electric-volt palette, bold uppercase Archivo headings, square sporty buttons, and a "Gear up. Game on." home page.

## Upload
1. Zip the **contents** of this folder (files at the zip root). `sportify-theme.zip` is already built.
2. Shopify admin > Online Store > Themes > Add theme > Upload zip file.
3. Customize, then Publish.

## After upload
- **Logo**: Customize > Theme settings > Logo (none is set).
- **Hero image**: Home page > Hero > replace the empty background with a sports photo (the hero is dark with volt buttons until you do).
- **Collections**: create football, cricket, running, gym-training and cycling. The "Shop by sport" row on the home page uses these handles. Rename them in the home page section settings if yours differ.
- **Menus**: set header and footer menus under Content > Menus.
- **Colours**: Theme settings > Colors. Scheme 4 is the volt accent, schemes 5 and 6 are the dark ones.
- **Fonts**: Theme settings > Typography (heading: Archivo, body: Inter).

## Notes
- Not previewed on a live store by me. Shopify's older theme checker (CLI 3.70) flags 168 offenses, but the unmodified Horizon export gives the identical count, so they come from the checker not knowing newer Horizon syntax and not from the re-skin.
- Removed a leftover custom block from the source export's header that pointed at another store's images.
- Horizon is by Shopify; keep its license and attribution if you redistribute.
