"""Builds public/og/*.jpg share cards in the same layout as og-home.jpg:
clay illustration on top, grass band with the page's headline, the robot logo and "Stethos".
Run: python3 tools/make_og_pages.py [font prefix, default /tmp/fl/figtree]"""
from PIL import Image, ImageDraw, ImageFont
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import page_other, page_blog, page_seo

R = os.path.join(os.path.dirname(__file__), "..", "public")
W, H, BAND = 1200, 630, 170
FONT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/fl/figtree"
BG = (213, 225, 182)
INK = (17, 17, 17)
LOGO = Image.open(R + "/img/g-cl-logo-cut.webp").convert("RGBA").resize((64, 64), Image.LANCZOS)


def card(art, line, name):
    out = Image.new("RGB", (W, H), BG)
    im = Image.open(f"{R}/img/g-art-{art}-1600.webp").convert("RGB")
    top = H - BAND
    a = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    y = max(0, (a.height - top) // 2)
    out.paste(a.crop((0, y, W, y + top)), (0, 0))
    d = ImageDraw.Draw(out)
    brand = ImageFont.truetype(FONT + "500.ttf", 34)
    tw = d.textlength("Stethos", font=brand)
    bx = W - 48 - tw
    mid = top + BAND / 2
    d.text((bx, mid), "Stethos", font=brand, fill=INK, anchor="lm")
    out.paste(LOGO, (int(bx - 72), int(mid - 34)), LOGO)
    room = bx - 72 - 40 - 60
    for size in range(56, 39, -1):          # one line if it fits at 40px or more
        f = ImageFont.truetype(FONT + "500.ttf", size)
        if d.textlength(line, font=f) <= room:
            d.text((60, mid), line, font=f, fill=INK, anchor="lm")
            break
    else:                                    # otherwise two balanced lines
        words = line.split()
        best = min(range(1, len(words)), key=lambda k: abs(len(" ".join(words[:k])) - len(" ".join(words[k:]))))
        l1, l2 = " ".join(words[:best]), " ".join(words[best:])
        for size in range(44, 25, -1):
            f = ImageFont.truetype(FONT + "500.ttf", size)
            if max(d.textlength(l1, font=f), d.textlength(l2, font=f)) <= room: break
        d.text((60, mid - size * 0.62), l1, font=f, fill=INK, anchor="lm")
        d.text((60, mid + size * 0.62), l2, font=f, fill=INK, anchor="lm")
    out.save(f"{R}/og/{name}.jpg", quality=86, optimize=True, progressive=True)


jobs = [("pricing", "Pay per tool call. Start free.", "pricing"),
        ("compare", "Stethos vs the legacy data platforms", "compare"),
        ("uc-medtech", "What teams do with Stethos.", "use-cases"),
        ("uc-digital", "How Stethos works, under the hood", "how-it-works")]
jobs += [(u[3], u[4], u[0]) for u in page_other.UC]
jobs += [(m["art"], m["name"], m["slug"]) for m in page_seo.SEO_PAGES]
jobs += [(p["art"], p["title"], p["slug"]) for p in page_blog.ALL_POSTS]
os.makedirs(R + "/og", exist_ok=True)
for art, line, name in jobs:
    card(art, line, name)
print(len(jobs), "cards")
