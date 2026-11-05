# Shared pieces for every Stethos page: head, header, footer, CTA band.
# Same structure as the Wellby Inroads site; edit here, then run tools/build.py.

OG_ALT = "Illustration: a clay data machine with a glass dome over a map of pins, taking in records from hospitals, doctors' offices, government and insurance buildings and sending alerts to small clay robots at laptops."
import os as _os
# Production URL: Vercel sets VERCEL_PROJECT_PRODUCTION_URL at build time (custom domain once one is added).
SITE = "https://" + _os.environ.get("VERCEL_PROJECT_PRODUCTION_URL", "stethos-one.vercel.app")
APP = "https://app.stethos.health"       # placeholder app URL
EMAIL = "team@stethos.health"            # placeholder contact
BRAND = "Stethos"

ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h9.5M8.5 3.5 13 8l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHECK = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 8.4l2.6 2.6L12 5.4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def head(title, desc, path, css=("styles", "v2", "site"), extra="", ld="", og_type="website",
         image=None, image_alt=None, crumbs=None, schema=None):
    """crumbs: [(name, path), ...] after Home. schema: list of extra JSON-LD objects."""
    import json as _j
    img = SITE + (image or "/og.jpg")
    img_alt = image_alt or OG_ALT
    graph = list(schema or [])
    if crumbs:
        items = [("Home", "/")] + list(crumbs)
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(items)]})
    if graph:
        ld += '<script type="application/ld+json">' + _j.dumps({"@context": "https://schema.org", "@graph": graph}) + '</script>\n'

    links = "\n".join(f'<link rel="stylesheet" href="/{c}.css">' for c in css)
    url = SITE + path
    return f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#D0D2F9">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta property="og:image:alt" content="{img_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img}">
<meta name="twitter:image:alt" content="{img_alt}">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/fonts/figtree-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
{extra}{links}
<link rel="stylesheet" href="/stethos.css">
{ld}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def dd_goal(href, img, tint, title, sub):
    return (f'<li><a href="{href}"><i class="dd-ic" style="--t:{tint}"><img src="/img/{img}" width="96" height="96" alt="" loading="lazy" decoding="async"></i>'
            f'<span class="dd-t"><b>{title}</b><span>{sub}</span></span></a></li>')


def dd_spec(href, img, label):
    return f'<li><a href="{href}"><img src="/img/{img}" width="96" height="96" alt="" loading="lazy" decoding="async">{label}</a></li>'


HEADER = f'''
<header class="hdr">
  <div class="bar">
    <a class="logo" href="/" aria-label="{BRAND} home">
      <img class="mark" src="/img/g-cl-logo-96.webp" width="30" height="30" alt="">
      <span>{BRAND}</span>
    </a>
    <nav aria-label="Primary">
      <div class="dd">
        <button class="dd-btn" type="button" aria-expanded="false" aria-controls="dd-solutions">Product<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5 6 7.5 9 4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
        <div class="dd-panel" id="dd-solutions">
          <div class="dd-col"><p class="dd-h">The API</p><ul class="dd-goals">{
    dd_goal("/physician-data-api", "g-cl-stk-search-160.webp", "#ddf2ee", "Provider search", "Every clinician and organization in the US, filtered your way.")
  }{dd_goal("/npi-lookup-api", "g-cl-stk-enrich-160.webp", "#e4f0fd", "NPI lookup and enrich", "Licenses, affiliations, networks and contact info from an NPI.")
  }{dd_goal("/health-system-data-api", "g-cl-stk-orgs-160.webp", "#fdf5d2", "Health system data", "Health systems, groups and clinics, with who works where.")
  }{dd_goal("/license-verification-api", "g-cl-stk-watch-160.webp", "#fcecf6", "License data and alerts", "License status across states, with a webhook when one changes.")
  }{dd_goal("/docs#mcp", "g-cl-stk-agents-160.webp", "#eff5d6", "MCP server", "Let your agents call Stethos directly.")}</ul></div>
          <div class="dd-col dd-side"><p class="dd-h">By use case</p><ul class="dd-spec">{
    dd_spec("/use-cases/medtech-pharma", "g-cl-stk-search-160.webp", "Medtech and pharma sales")
  }{dd_spec("/use-cases/provider-directories", "g-cl-ic-payer-96.webp", "Provider directories")
  }{dd_spec("/use-cases/clinical-staffing", "g-cl-ic-license-96.webp", "Clinical staffing")
  }{dd_spec("/use-cases/investors", "g-cl-stk-orgs-160.webp", "Healthcare investors")
  }{dd_spec("/use-cases/digital-health", "g-cl-ic-code-96.webp", "Digital health and AI apps")}</ul><a class="dd-all" href="/use-cases">All use cases <span aria-hidden="true">→</span></a><img class="dd-art" src="/img/g-cl-stk-search-cut.webp" width="480" height="480" alt="" loading="lazy" decoding="async"></div>
        </div>
      </div>
      <a href="/use-cases">Use cases</a>
      <a href="/docs">Docs</a>
      <a href="/pricing">Pricing</a><a href="/blog">Blog</a>
    </nav>
    <div class="hdr-act"><a class="btn-2" href="{APP}/login">Sign in</a><a class="btn-1" href="{APP}/signup">Get an API key</a><button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav" aria-label="Open menu"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 6h14M3 10h14M3 14h14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button></div><div class="mnav" id="mnav" hidden><a href="/#platform">Product</a><a href="/#playground">Try the API</a><a href="/use-cases">Use cases</a><a href="/docs">Docs</a><a href="/pricing">Pricing</a><a href="/blog">Blog</a><a href="/compare/definitive-healthcare">Stethos vs Definitive</a><a href="{APP}/login">Sign in</a></div>
  </div>
</header>
'''

FOOTER = f'''
<footer class="foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <a class="logo" href="/"><img class="mark" src="/img/g-cl-logo-96.webp" width="30" height="30" alt=""><span>{BRAND}</span></a>
      <p>Real-time healthcare provider data for AI agents. Product views and API responses on this site use illustrative sample data.</p>
    </div>
    <nav class="foot-links" aria-label="Footer">
      <a href="/#platform">Product</a>
      <a href="/use-cases">Use cases</a>
      <a href="/docs">Docs</a>
      <a href="/pricing">Pricing</a><a href="/blog">Blog</a>
      <a href="/npi-lookup-api">NPI lookup API</a>
      <a href="/physician-data-api">Physician data API</a>
      <a href="/license-verification-api">License data API</a>
      <a href="/health-system-data-api">Health system data API</a>
      <a href="/use-cases/medtech-pharma">Medtech and pharma</a>
      <a href="/use-cases/provider-directories">Provider directories</a>
      <a href="/use-cases/clinical-staffing">Clinical staffing</a>
      <a href="/compare/definitive-healthcare">vs Definitive</a>
      <a href="/compare/iqvia-onekey">vs IQVIA OneKey</a>
      <a href="/#faq">FAQ</a>
      <a href="/privacy">Privacy</a>
      <a href="mailto:{EMAIL}?subject={BRAND}">Contact</a>
    </nav>
    <p class="foot-copy">© 2026 {BRAND}</p>
  </div>
</footer>
'''


def cta_band(eyebrow, h2a, h2b, lede, subject):
    return f'''<section class="sec">
  <div class="panel navy wrap-panel sp-cta">
    <img class="cta-art l" src="/img/g-cl-stk-agents-cut.webp" width="320" height="320" alt="" loading="lazy" decoding="async"><img class="cta-art r" src="/img/g-cl-ic-pin-cut.webp" width="360" height="360" alt="" loading="lazy" decoding="async">
    <p class="eyebrow on-dark"><span>{eyebrow}</span></p>
    <h2>{h2a} <span class="pop">{h2b}</span></h2>
    <p>{lede}</p>
    <div class="sp-cta-row"><a class="btn-cta" href="{APP}/signup">Get an API key</a><a class="sp-cta-alt" href="mailto:{EMAIL}?subject={subject}">Questions? Email our team</a></div>
  </div>
</section>
'''


def tail(scripts=("nav",)):
    s = "\n".join(f'<script src="/{x}.js" defer></script>' for x in scripts)
    return FOOTER + s + "\n</body>\n</html>\n"


def art(name, alt, sizes="(max-width: 820px) 100vw, 1100px", w=1600, h=1195, lazy=True, cls=""):
    lz = ' loading="lazy"' if lazy else ''
    return (f'<img class="{cls}" src="/img/g-art-{name}-900.webp" srcset="/img/g-art-{name}-900.webp 900w, /img/g-art-{name}-1600.webp 1600w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{alt}"{lz} decoding="async">')
