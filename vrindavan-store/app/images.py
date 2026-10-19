"""Image upload processing: validate, strip metadata, re-encode to WebP in three widths."""
import io
import os
import secrets

from PIL import Image, ImageOps

WIDTHS = (480, 800, 1200)
MAX_BYTES = 8 * 1024 * 1024
ALLOWED_FORMATS = {"JPEG", "PNG", "WEBP"}
MAX_PIXELS = 40_000_000


class ImageError(Exception):
    pass


def save_product_image(file_storage, media_root, product_id):
    data = file_storage.read(MAX_BYTES + 1)
    if not data:
        raise ImageError("Empty file.")
    if len(data) > MAX_BYTES:
        raise ImageError("Image is larger than 8 MB.")
    try:
        probe = Image.open(io.BytesIO(data))
        probe.verify()  # structural check
        img = Image.open(io.BytesIO(data))
    except Exception:
        raise ImageError("That file is not a valid image.")
    if img.format not in ALLOWED_FORMATS:
        raise ImageError("Only JPG, PNG or WebP images are allowed.")
    if img.width * img.height > MAX_PIXELS:
        raise ImageError("Image dimensions are too large.")
    img = ImageOps.exif_transpose(img)
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGB")
    if img.mode == "RGBA":
        bg = Image.new("RGB", img.size, (247, 241, 230))
        bg.paste(img, mask=img.split()[3])
        img = bg
    return _write_sizes(img, media_root, product_id)


def _write_sizes(img, media_root, product_id):
    token = secrets.token_hex(8)
    rel_dir = f"products/{int(product_id)}"
    out_dir = os.path.join(media_root, rel_dir)
    os.makedirs(out_dir, exist_ok=True)
    for w in WIDTHS:
        im = img if img.width <= w else img.resize((w, max(1, round(img.height * w / img.width))), Image.LANCZOS)
        im.save(os.path.join(out_dir, f"{token}_{w}.webp"), "WEBP", quality=82, method=2)
    return f"{rel_dir}/{token}"


def delete_image_files(media_root, base):
    for w in WIDTHS:
        path = os.path.join(media_root, f"{base}_{w}.webp")
        try:
            os.remove(path)
        except OSError:
            pass


def make_placeholder(title, media_root, product_id, hue_seed=0):
    """Honest placeholder: ivory stone gradient + arch outline + 'Sample listing' - never implies a real photo."""
    from PIL import ImageDraw, ImageFont
    w, h = 1200, 1500
    top, bottom = (247, 241, 230), (232, 218, 190)
    grad = Image.linear_gradient("L").resize((w, h))
    img = ImageOps.colorize(grad, black=top, white=bottom).convert("RGB")
    d = ImageDraw.Draw(img)
    cx, base_y = w // 2, int(h * 0.80)
    brass = (143, 90, 14)
    d.line([(cx - 90, base_y), (cx + 90, base_y)], fill=brass, width=4)
    # simple lamp-glow dot
    d.ellipse([cx - 16, base_y - 40, cx + 16, base_y - 8], fill=(210, 150, 30))
    try:
        font = ImageFont.truetype("arial.ttf", 44)
        small = ImageFont.truetype("arial.ttf", 34)
    except Exception:
        font = small = ImageFont.load_default()
    label = "SAMPLE LISTING"
    tw = d.textlength(label, font=font)
    d.text(((w - tw) / 2, base_y + 70), label, fill=(90, 77, 66), font=font)
    sub = "Photograph to be added"
    tw = d.textlength(sub, font=small)
    d.text(((w - tw) / 2, base_y + 130), sub, fill=(90, 77, 66), font=small)
    return _write_sizes(img, media_root, product_id)
