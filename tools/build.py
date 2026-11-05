# Builds every page in ../public from the templates in this folder.
# Run:  python3 tools/build.py
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from parts import SITE, BRAND, EMAIL, MCP_URL
import page_home, page_other, page_blog, page_uc, page_seo

OUT = os.path.join(os.path.dirname(__file__), "..", "public")


def w(path, text):
    p = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(text)


home = page_home.page().replace("{BLOG_CARDS}", "".join(page_blog.card(p) for p in page_blog.POSTS[:3]))
w("index.html", home)
w("use-cases.html", page_other.use_cases())
w("pricing.html", page_other.pricing())
w("docs.html", page_other.docs())
w("compare/definitive-healthcare.html", page_other.compare_definitive())
w("compare/iqvia-onekey.html", page_other.compare_onekey())
w("privacy.html", page_other.privacy())
w("404.html", page_other.notfound())
w("blog/index.html", page_blog.blog_index())
# blog: only posts whose date has arrived; remove any page for a post not (yet) published
import glob
live = {p["slug"] for p in page_blog.POSTS}
for f in glob.glob(os.path.join(OUT, "blog", "*.html")):
    n = os.path.basename(f)[:-5]
    if n != "index" and n not in live: os.remove(f)
for p in page_blog.POSTS:
    w(f"blog/{p['slug']}.html", page_blog.post(p))
from xml.sax.saxutils import escape as _x
import datetime as _dt
w("blog/rss.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
  f'<title>{BRAND} guides</title><link>{SITE}/blog</link><description>Guides to US healthcare provider data.</description>'
  + "".join(f'<item><title>{_x(p["title"])}</title><link>{SITE}/blog/{p["slug"]}</link><guid>{SITE}/blog/{p["slug"]}</guid><pubDate>{_dt.datetime.strptime(p["date"], "%Y-%m-%d").strftime("%a, %d %b %Y 08:00:00 -0800")}</pubDate><description>{_x(p["desc"])}</description></item>' for p in page_blog.POSTS)
  + '</channel></rss>\n')
for m in page_seo.SEO_PAGES:
    w(f"{m['slug']}.html", page_seo.seo_page(m))
for n, u in enumerate(page_other.UC):
    w(f"use-cases/{u[0]}.html", page_uc.uc_page(n))

# 1200x630 JPG share images (social sites handle JPG more reliably than WebP)
try:
    from PIL import Image
except ImportError:
    Image = None
os.makedirs(os.path.join(OUT, "og"), exist_ok=True)
def og(src, name):
    dst = os.path.join(OUT, "og", name + ".jpg")
    if Image is None or os.path.exists(dst): return
    im = Image.open(os.path.join(OUT, "img", src)).convert("RGB")
    tw = im.width; th = round(tw * 630 / 1200)
    if th > im.height: th = im.height; tw = round(th * 1200 / 630)
    x = (im.width - tw) // 2; y = (im.height - th) // 2
    im.crop((x, y, x + tw, y + th)).resize((1200, 630), Image.LANCZOS).save(os.path.join(OUT, "og", name + ".jpg"), quality=84)
og("g-art-pricing-1600.webp", "pricing"); og("g-art-compare-1600.webp", "compare"); og("g-art-uc-medtech-1600.webp", "use-cases")
for u in page_other.UC: og(f"g-art-{u[3]}-1600.webp", u[0])
for p in page_blog.ALL_POSTS: og(f"g-art-{p['art']}-1600.webp", p["slug"])
for m in page_seo.SEO_PAGES: og(f"g-art-{m['art']}-1600.webp", m["slug"])

urls = ["/"] + [f"/{m['slug']}" for m in page_seo.SEO_PAGES] + ["/use-cases"] + [f"/use-cases/{u[0]}" for u in page_other.UC] + ["/pricing", "/docs", "/compare/definitive-healthcare", "/compare/iqvia-onekey", "/blog", "/privacy"] + [f"/blog/{p['slug']}" for p in page_blog.POSTS]
LASTMOD = {f"/blog/{p['slug']}": p["date"] for p in page_blog.POSTS}
if page_blog.POSTS: LASTMOD["/blog"] = page_blog.POSTS[0]["date"]
w("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
  + "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{LASTMOD.get(u, '2026-11-05')}</lastmod></url>\n" for u in urls) + "</urlset>\n")
w("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
w("llms.txt", f"""# {BRAND}

> Self-serve MCP server (and REST API) for US healthcare provider and organization data, built for AI agents and priced per tool call. Tools: search_providers, enrich_provider, enrich_org, watch_providers, recent_changes. Provider data only, no patient data.\n\nMCP endpoint: """ + MCP_URL + """ (preview)

## Pages
- [Home]({SITE}/): what Stethos does and who it's for
- [Use cases]({SITE}/use-cases): medtech and pharma sales, provider directories, clinical staffing, investors, digital health
""" + "".join(f"- [{u[4]}]({SITE}/use-cases/{u[0]}): {page_uc.UC_PAGES[u[0]]['desc']}\n" for u in page_other.UC) + f"""- [Docs]({SITE}/docs): quickstart for search, enrich, organizations, watchers and MCP (preview)
""" + "".join(f"- [{m['name']}]({SITE}/{m['slug']}): {m['desc']}\n" for m in page_seo.SEO_PAGES) + f"""- [Pricing]({SITE}/pricing): credit-based pricing, Free, Build and Enterprise
- [Stethos vs Definitive Healthcare]({SITE}/compare/definitive-healthcare)
- [Stethos vs IQVIA OneKey]({SITE}/compare/iqvia-onekey)

## Guides
""" + "".join(f"- [{p['title']}]({SITE}/blog/{p['slug']}): {p['desc']}\n" for p in page_blog.POSTS) + f"\nContact: {EMAIL}\n")
print("built", len(urls) + 1, "pages")
