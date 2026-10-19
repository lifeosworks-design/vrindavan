"""Resize the supplied logo files (originals untouched in design/brand-originals) into web-sized assets.
Resizing only - the artwork is not modified. The favicon is a DEV-ONLY downscale of emblem 2, pending an approved favicon derivative."""
import os
from PIL import Image

root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
src = os.path.join(root, "design", "brand-originals")
dst = os.path.join(root, "app", "static", "brand")
os.makedirs(dst, exist_ok=True)


def save(name, size_w, out, fmt="WEBP"):
    im = Image.open(os.path.join(src, name)).convert("RGBA")
    h = round(im.height * size_w / im.width)
    im = im.resize((size_w, h), Image.LANCZOS)
    path = os.path.join(dst, out)
    if fmt == "WEBP":
        im.save(path, "WEBP", quality=90, method=6)
    else:
        im.save(path, fmt)
    print(out, im.size, os.path.getsize(path), "bytes")


save("3.webp", 420, "wordmark.webp")        # header (2x for ~210px) and footer
save("3.webp", 840, "wordmark-large.webp")  # hero/about
save("1.webp", 480, "emblem.webp")          # footer/brand moments
save("2.webp", 320, "emblem-circle.webp")   # social avatar style
save("2.webp", 64, "favicon-64.png", "PNG")
save("2.webp", 180, "apple-touch-icon.png", "PNG")
