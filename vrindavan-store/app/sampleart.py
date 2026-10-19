"""Generated SAMPLE illustrations of murtis (stylised, metallic/marble shading) used until real photographs exist.
They are original drawings made with Pillow - not photographs and not scraped images - and are labelled 'Sample illustration'."""
import math

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps

W, H, S = 1200, 1500, 2

BRASS = dict(dark=(86, 48, 6), mid=(190, 133, 42), hi=(255, 226, 144), edge=(62, 34, 4))
BRONZE = dict(dark=(48, 30, 16), mid=(118, 80, 38), hi=(212, 168, 96), edge=(34, 20, 8))
TEAL = dict(dark=(6, 36, 62), mid=(28, 122, 148), hi=(150, 226, 228), edge=(4, 26, 44))
MARBLE = dict(dark=(150, 144, 136), mid=(226, 221, 212), hi=(255, 254, 250), edge=(116, 108, 98))
GOLD = BRASS
SKIN_MARBLE = MARBLE


class Mask:
    """Draws one part in figure coordinates (600,1130 = centre of the base) mapped by (cx, by, scale)."""

    def __init__(self, cx, by, s):
        self.img = Image.new("L", (W * S, H * S), 0)
        self.d = ImageDraw.Draw(self.img)
        self.cx, self.by, self.s = cx, by, s

    def t(self, x, y):
        return ((self.cx + (x - 600) * self.s) * S, (self.by + (y - 1130) * self.s) * S)

    def ell(self, cx, cy, rx, ry, rot=0.0, fill=255):
        pts = []
        for i in range(90):
            a = 2 * math.pi * i / 90
            x, y = rx * math.cos(a), ry * math.sin(a)
            pts.append(self.t(cx + x * math.cos(rot) - y * math.sin(rot), cy + x * math.sin(rot) + y * math.cos(rot)))
        self.d.polygon(pts, fill=fill)

    def circ(self, cx, cy, r):
        self.ell(cx, cy, r, r)

    def poly(self, pts):
        self.d.polygon([self.t(*p) for p in pts], fill=255)

    def line(self, pts, w):
        tp = [self.t(*p) for p in pts]
        self.d.line(tp, fill=255, width=max(1, int(w * self.s * S)), joint="curve")
        r = w * self.s * S / 2
        for p in (tp[0], tp[-1]):
            self.d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=255)

    def taper(self, pts, w0, w1):
        n = len(pts)
        for i, (x, y) in enumerate(pts):
            self.circ(x, y, (w0 + (w1 - w0) * i / max(n - 1, 1)) / 2)

    def ring(self, cx, cy, r, w):
        self.ell(cx, cy, r, r, fill=255)
        self.ell(cx, cy, r - w, r - w, fill=0)


def bez(p0, p1, p2, p3, n=40):
    out = []
    for i in range(n + 1):
        t = i / n
        a, b, c, d = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t * t, t ** 3
        out.append((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]))
    return out


def shade(layer, mask, pal):
    """Cylindrical metallic/marble shading + dark edge + specular rim, composited onto the RGBA figure layer."""
    bb = mask.getbbox()
    if not bb:
        return
    pad = 10
    box = (max(bb[0] - pad, 0), max(bb[1] - pad, 0), min(bb[2] + pad, mask.width), min(bb[3] + pad, mask.height))
    mk = mask.crop(box)
    w, h = mk.size
    gh = Image.linear_gradient("L").rotate(90, expand=True).resize((w, h))      # left -> right
    tri = ImageChops.difference(gh, Image.new("L", (w, h), 110)).point(lambda v: min(255, v * 2))
    gv = Image.linear_gradient("L").resize((w, h))                              # top -> bottom
    light = ImageChops.add(ImageChops.multiply(ImageChops.invert(tri), Image.new("L", (w, h), 215)),
                           ImageChops.multiply(ImageChops.invert(gv), Image.new("L", (w, h), 40)))
    body = ImageOps.colorize(light.point(lambda v: min(255, int(v * 1.15))), black=pal["dark"], mid=pal["mid"], white=pal["hi"])
    layer.paste(body, box[:2], mk)
    er = mk.filter(ImageFilter.MinFilter(9))
    edge = ImageChops.subtract(mk, er)
    layer.paste(Image.new("RGB", (w, h), pal["edge"]), box[:2], edge.point(lambda v: int(v * 0.85)))
    hl = ImageChops.subtract(er, ImageChops.offset(er, 10, 12)).filter(ImageFilter.GaussianBlur(3))
    layer.paste(Image.new("RGB", (w, h), pal["hi"]), box[:2], hl.point(lambda v: int(v * 0.8)))


class Figure:
    def __init__(self):
        self.rgb = Image.new("RGB", (W * S, H * S), (0, 0, 0))
        self.alpha = Image.new("L", (W * S, H * S), 0)

    def part(self, cx, by, s, pal, fn):
        m = Mask(cx, by, s)
        fn(m)
        shade(self.rgb, m.img, pal)
        self.alpha = ImageChops.lighter(self.alpha, m.img)


# ----------------------------------------------------------------- figure drawing
def pedestal(f, cx, by, s, pal, orn):
    f.part(cx, by, s, pal, lambda m: (m.poly([(300, 1128), (900, 1128), (930, 1196), (270, 1196)]), m.ell(600, 1128, 300, 30)))
    for i in range(-3, 4):
        f.part(cx, by, s, orn, lambda m, i=i: m.ell(600 + i * 92, 1170, 50, 34, rot=i * 0.12))
    f.part(cx, by, s, orn, lambda m: m.line([(300, 1136), (900, 1136)], 8))


def ganesha(f, cx, by, s, pal, orn):
    f.part(cx, by, s, orn, lambda m: m.ring(600, 585, 190, 11))
    f.part(cx, by, s, pal, lambda m: (m.ell(470, 600, 80, 118, rot=0.16), m.ell(730, 600, 80, 118, rot=-0.16)))
    f.part(cx, by, s, pal, lambda m: m.ell(600, 1050, 262, 80))
    f.part(cx, by, s, pal, lambda m: m.ell(600, 880, 178, 205))
    f.part(cx, by, s, orn, lambda m: m.line([(430, 905), (520, 960), (680, 960), (770, 905)], 16))
    f.part(cx, by, s, pal, lambda m: m.ell(600, 745, 142, 105))
    f.part(cx, by, s, pal, lambda m: (m.ell(452, 830, 50, 118, rot=0.38), m.ell(748, 830, 50, 118, rot=-0.38)))
    f.part(cx, by, s, orn, lambda m: (m.circ(740, 955, 28), m.circ(460, 955, 22)))
    f.part(cx, by, s, pal, lambda m: m.ell(600, 595, 104, 100))
    f.part(cx, by, s, pal, lambda m: m.taper(bez((600, 650), (610, 760), (535, 800), (560, 905)), 64, 26))
    f.part(cx, by, s, MARBLE, lambda m: (m.poly([(652, 668), (700, 690), (672, 742)]), m.poly([(548, 668), (500, 690), (528, 742)])))
    f.part(cx, by, s, orn, lambda m: (m.poly([(520, 520), (680, 520), (662, 450), (600, 395), (538, 450)]), m.circ(600, 384, 18)))
    f.part(cx, by, s, orn, lambda m: m.line([(470, 700), (530, 780), (600, 810), (670, 780), (730, 700)], 14))
    f.part(cx, by, s, TEAL if pal is not TEAL else BRASS, lambda m: (m.circ(556, 575, 11), m.circ(644, 575, 11)))


def krishna(f, cx, by, s, pal, orn):
    f.part(cx, by, s, orn, lambda m: m.ring(600, 440, 118, 9))
    f.part(cx, by, s, pal, lambda m: (m.ell(556, 1000, 54, 150, rot=0.10), m.ell(655, 1000, 54, 150, rot=-0.07)))
    f.part(cx, by, s, orn, lambda m: m.poly([(512, 760), (692, 760), (736, 1106), (498, 1106)]))
    f.part(cx, by, s, orn, lambda m: m.line([(505, 775), (700, 775)], 20))
    f.part(cx, by, s, pal, lambda m: m.ell(600, 650, 84, 128))
    f.part(cx, by, s, pal, lambda m: m.line([(668, 604), (698, 540), (650, 492)], 38))
    f.part(cx, by, s, pal, lambda m: m.line([(534, 612), (516, 706), (774, 626)], 38))
    f.part(cx, by, s, orn, lambda m: m.line([(618, 478), (800, 624)], 24))
    f.part(cx, by, s, orn, lambda m: [m.circ(535 + i * 16.5, 610 + 120 * math.sin(math.pi * i / 8), 10) for i in range(9)])
    f.part(cx, by, s, pal, lambda m: m.ell(600, 438, 64, 72))
    f.part(cx, by, s, orn, lambda m: (m.poly([(540, 400), (660, 400), (646, 352), (600, 322), (554, 352)])))
    f.part(cx, by, s, TEAL if pal is not TEAL else BRASS, lambda m: (m.ell(618, 296, 20, 52, rot=0.2), ))
    f.part(cx, by, s, orn, lambda m: m.circ(622, 290, 11))


def radha(f, cx, by, s, pal, orn):
    f.part(cx, by, s, orn, lambda m: m.ring(600, 470, 104, 8))
    f.part(cx, by, s, orn, lambda m: m.poly([(540, 722), (662, 722), (748, 1112), (452, 1112)]))
    f.part(cx, by, s, pal, lambda m: m.ell(600, 650, 66, 106))
    f.part(cx, by, s, pal, lambda m: (m.line([(546, 640), (498, 740), (548, 800)], 30), m.line([(654, 640), (702, 740), (652, 800)], 30)))
    f.part(cx, by, s, orn, lambda m: m.poly([(540, 600), (660, 600), (700, 800), (500, 800)]))
    f.part(cx, by, s, pal, lambda m: m.ell(600, 470, 58, 66))
    f.part(cx, by, s, orn, lambda m: (m.poly([(548, 430), (652, 430), (640, 392), (600, 372), (560, 392)]), m.circ(600, 360, 22)))


def lakshmi(f, cx, by, s, pal, orn):
    f.part(cx, by, s, orn, lambda m: m.ring(600, 520, 150, 9))
    f.part(cx, by, s, orn, lambda m: [m.ell(600 + i * 88, 1085, 62, 70, rot=i * 0.18) for i in range(-3, 4)])
    f.part(cx, by, s, pal, lambda m: m.ell(600, 1030, 232, 74))
    f.part(cx, by, s, orn, lambda m: m.poly([(508, 702), (692, 702), (742, 1040), (458, 1040)]))
    f.part(cx, by, s, pal, lambda m: m.ell(600, 690, 78, 98))
    f.part(cx, by, s, pal, lambda m: (m.line([(534, 730), (452, 832), (432, 908)], 28), m.line([(666, 730), (748, 832), (768, 908)], 28),
                                      m.line([(540, 690), (456, 640), (432, 566)], 28), m.line([(660, 690), (744, 640), (768, 566)], 28)))
    f.part(cx, by, s, orn, lambda m: (m.ell(428, 548, 38, 26), m.ell(772, 548, 38, 26), [m.circ(430 - (i % 2) * 8, 930 + i * 24, 10) for i in range(6)],
                                      [m.circ(770 + (i % 2) * 8, 930 + i * 24, 10) for i in range(6)]))
    f.part(cx, by, s, pal, lambda m: m.ell(600, 520, 62, 70))
    f.part(cx, by, s, orn, lambda m: m.poly([(542, 476), (658, 476), (644, 392), (600, 336), (556, 392)]))


FIGURES = {
    "ganesha": lambda f, pal, orn: (pedestal(f, 600, 1130, 1.0, pal, orn), ganesha(f, 600, 1130, 1.0, pal, orn)),
    "krishna": lambda f, pal, orn: (pedestal(f, 600, 1130, 1.0, pal, orn), krishna(f, 600, 1130, 1.0, pal, orn)),
    "lakshmi": lambda f, pal, orn: (pedestal(f, 600, 1130, 1.0, pal, orn), lakshmi(f, 600, 1130, 1.0, pal, orn)),
    "radha_krishna": lambda f, pal, orn: (pedestal(f, 600, 1130, 1.0, pal, orn), radha(f, 415, 1112, 0.74, pal, orn), krishna(f, 790, 1112, 0.76, pal, orn)),
    "lakshmi_ganesha": lambda f, pal, orn: (pedestal(f, 600, 1130, 1.0, pal, orn), lakshmi(f, 405, 1112, 0.74, pal, orn), ganesha(f, 800, 1118, 0.72, pal, orn)),
    "hanuman": lambda f, pal, orn: (pedestal(f, 600, 1130, 1.0, pal, orn), hanuman(f, pal, orn)),
}


def hanuman(f, pal, orn):
    f.part(600, 1130, 1.0, orn, lambda m: (m.taper(bez((540, 1030), (300, 930), (300, 520), (470, 340)), 46, 18), m.circ(470, 330, 28)))
    f.part(600, 1130, 1.0, pal, lambda m: (m.ell(540, 1010, 58, 152, rot=0.16), m.ell(668, 1010, 58, 152, rot=-0.16)))
    f.part(600, 1130, 1.0, orn, lambda m: m.poly([(500, 780), (700, 780), (726, 900), (474, 900)]))
    f.part(600, 1130, 1.0, pal, lambda m: m.ell(600, 700, 120, 142))
    f.part(600, 1130, 1.0, orn, lambda m: [m.circ(500 + i * 25, 600 + 90 * math.sin(math.pi * i / 8), 10) for i in range(9)])
    f.part(600, 1130, 1.0, orn, lambda m: (m.line([(788, 440), (798, 900)], 40), m.circ(788, 420, 58)))
    f.part(600, 1130, 1.0, pal, lambda m: (m.line([(712, 640), (780, 566), (788, 480)], 44), m.line([(490, 650), (466, 744), (562, 750)], 44)))
    f.part(600, 1130, 1.0, pal, lambda m: m.ell(600, 520, 76, 84))
    f.part(600, 1130, 1.0, orn, lambda m: m.poly([(534, 474), (666, 474), (646, 396), (600, 360), (554, 396)]))
    f.part(600, 1130, 1.0, MARBLE if pal is not MARBLE else BRONZE, lambda m: m.ell(600, 552, 46, 34))


# ----------------------------------------------------------------- backgrounds
def _font(size):
    for name in ("arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()


def background_niche():
    bg = Image.linear_gradient("L").resize((W, H))
    img = ImageOps.colorize(bg, black=(44, 15, 24), white=(16, 6, 10)).convert("RGB")
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([140, 330, 1060, 1250], fill=(150, 98, 24))
    glow = glow.filter(ImageFilter.GaussianBlur(160))
    img = ImageChops.add(img, glow.point(lambda v: int(v * 0.55)))
    d = ImageDraw.Draw(img)
    arch = [(180, 1250), (180, 560)] + [(600 + 420 * math.cos(math.pi + math.pi * i / 60), 560 - 420 * math.sin(math.pi * i / 60)) for i in range(61)] + [(1020, 560), (1020, 1250)]
    d.line(arch + [arch[0]], fill=(214, 160, 56), width=6)
    inner = [(206, 1250), (206, 565)] + [(600 + 394 * math.cos(math.pi + math.pi * i / 60), 565 - 394 * math.sin(math.pi * i / 60)) for i in range(61)] + [(994, 565), (994, 1250)]
    d.line(inner, fill=(120, 74, 20), width=3)
    d.rectangle([0, 1250, W, H], fill=(24, 9, 14))
    d.line([(0, 1250), (W, 1250)], fill=(120, 74, 20), width=3)
    for dx in (150, 1050):
        fl = Image.new("RGB", (W, H), (0, 0, 0))
        ImageDraw.Draw(fl).ellipse([dx - 46, 1146, dx + 46, 1226], fill=(255, 190, 70))
        img = ImageChops.add(img, fl.filter(ImageFilter.GaussianBlur(26)).point(lambda v: int(v * 0.8)))
        d = ImageDraw.Draw(img)
        d.pieslice([dx - 52, 1206, dx + 52, 1290], 0, 180, fill=(190, 133, 42))
        d.ellipse([dx - 10, 1160, dx + 10, 1210], fill=(255, 226, 150))
    return img


def background_stone():
    bg = Image.linear_gradient("L").resize((W, H))
    img = ImageOps.colorize(bg, black=(250, 244, 232), white=(228, 212, 184)).convert("RGB")
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    ImageDraw.Draw(glow).ellipse([200, 260, 1000, 1160], fill=(70, 50, 14))
    img = ImageChops.add(img, glow.filter(ImageFilter.GaussianBlur(180)).point(lambda v: int(v * 0.5)))
    return img


def caption(img, text, dark):
    d = ImageDraw.Draw(img)
    f = _font(30)
    tw = d.textlength(text, font=f)
    d.text(((W - tw) / 2, H - 62), text, fill=(214, 170, 90) if dark else (110, 92, 70), font=f)


def render(kind, pal, orn):
    """Returns [stone_front, niche, detail] RGB images (W x H)."""
    fig = Figure()
    FIGURES[kind](fig, pal, orn)
    rgb = fig.rgb.resize((W, H), Image.LANCZOS)
    alpha = fig.alpha.resize((W, H), Image.LANCZOS)

    niche = background_niche()
    shadow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(shadow).ellipse([260, 1160, 940, 1230], fill=150)
    niche.paste(Image.new("RGB", (W, H), (0, 0, 0)), (0, 0), shadow.filter(ImageFilter.GaussianBlur(18)))
    niche.paste(rgb, (0, 0), alpha)
    caption(niche, "SAMPLE ILLUSTRATION", True)

    stone = background_stone()
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).ellipse([240, 1150, 960, 1250], fill=120)
    stone.paste(Image.new("RGB", (W, H), (60, 40, 20)), (0, 0), sh.filter(ImageFilter.GaussianBlur(26)))
    stone.paste(rgb, (0, 0), alpha)
    caption(stone, "SAMPLE ILLUSTRATION", False)

    crop = niche.crop((260, 300, 940, 1150)).resize((W, round(850 * W / 680)), Image.LANCZOS)
    top = max(0, (crop.height - H) // 2)
    detail = crop.crop((0, top, W, top + H))
    caption(detail, "SAMPLE ILLUSTRATION", True)
    return [stone, niche, detail]
