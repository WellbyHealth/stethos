"""Builds public/og-home.jpg in the Aria share-card layout: clay scene on top, grass band with headline + logo."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
R = os.path.join(os.path.dirname(__file__), "..", "public")
W, H, BAND = 1200, 630, 170
FONT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/fl/figtree"
out = Image.new("RGB", (W, H), (213, 225, 182))
art = Image.open(R + "/img/g-hero-3200.webp").convert("RGB")
a = art.resize((W, round(art.height * W / art.width)), Image.LANCZOS)   # 1200 x 509
top_h = H - BAND                                                         # 460
y0 = 22
out.paste(a.crop((0, y0, W, y0 + top_h)), (0, 0))
d = ImageDraw.Draw(out)
band = (213, 225, 182)
d.rectangle([0, top_h, W, H], fill=band)
brand = ImageFont.truetype(FONT + "500.ttf", 34)
logo = Image.open(R + "/img/g-cl-logo-cut.webp").convert("RGBA").resize((64, 64), Image.LANCZOS)
tw = d.textlength("Stethos", font=brand)
bx = W - 48 - tw
d.text((bx, top_h + BAND / 2), "Stethos", font=brand, fill=(17, 17, 17), anchor="lm")
out.paste(logo, (int(bx - 72), int(top_h + BAND / 2 - 34)), logo)
line, size = "Healthcare data for your AI agents.", 60
while True:  # largest size that leaves a 40px gap before the logo
    h1 = ImageFont.truetype(FONT + "500.ttf", size)
    if 60 + d.textlength(line, font=h1) <= bx - 72 - 40: break
    size -= 1
d.text((60, top_h + BAND / 2), line, font=h1, fill=(17, 17, 17), anchor="lm")
print("headline size", size)
out.save(sys.argv[1], quality=88, optimize=True, progressive=True)
print(os.path.getsize(sys.argv[1]))
