from parts import *

# ---------- use cases (same tabbed layout as Inroad's specialties page) ----------
UC = [
    ("medtech-pharma", "sp-blue", "g-cl-stk-search-160.webp", "uc-medtech", "Medtech and pharma sales",
     "Give your sales agents the surgeons, groups and facilities that fit your product, and tell them the week a target moves, opens a site or starts a new service line.",
     ["Specialty, procedure focus and practice setting", "Group and hospital affiliations", "Licenses by state", "Practice contact details", "Industry payments from Open Payments"],
     ["A target surgeon changes groups", "A new ambulatory surgery center opens", "A health system names a new service line leader"]),
    ("provider-directories", "sp-lime", "g-cl-ic-payer-cut.webp", "uc-payer", "Provider directories and networks",
     "Check every listing in your directory against current sources, and flag stale addresses, lapsed licenses and network mismatches before members run into them.",
     ["Practice locations and phone numbers, with sources", "Licenses and their status", "Payer network listings across directories", "Accepting-new-patients signals where published"],
     ["A clinician leaves a listed location", "A license lapses or is restricted", "A practice drops out of a network"]),
    ("clinical-staffing", "sp-butter", "g-cl-ic-license-cut.webp", "uc-staffing", "Clinical staffing and recruiting",
     "Source licensed clinicians by state and specialty for your recruiters and agents, and find the health systems hiring hardest right now.",
     ["Clinicians by specialty and license state", "Current employer and affiliation history", "Organizations with open clinical roles"],
     ["A new state license is issued", "An organization's clinical job posts spike", "A clinician leaves a large employer"]),
    ("investors", "sp-pink", "g-cl-stk-orgs-160.webp", "uc-investors", "Healthcare investors",
     "Track practice roll-ups, clinician headcount at portfolio and target companies, and new entrants in a market as it happens, not a quarter later.",
     ["Organizations with ownership and parent–child links", "Rostered clinicians per organization over time", "Locations by market"],
     ["A group adds or loses clinicians", "A new location opens in a target market", "An executive hire at a target"]),
    ("digital-health", "sp-blue", "g-cl-ic-code-cut.webp", "uc-digital", "Digital health and AI apps",
     "Power provider search, referrals and scheduling in your app with one API, and let your agents look up any clinician through MCP.",
     ["Provider search by specialty, location and network", "Organization and location records", "NPI-keyed records that join to your data"],
     ["A provider in your app changes location", "A practice joins a network your users have", "A record your app shows is re-verified"]),
]


def use_cases():
    h = head("Use Cases: Healthcare Provider Data API | Stethos",
             "How sales agents, provider directories, staffing platforms, investors and digital health apps use real-time provider data from Stethos.",
             "/use-cases", image="/og/use-cases.jpg", crumbs=[("Use cases", "/use-cases")],
             schema=[{"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": u[4], "url": SITE + "/use-cases/" + u[0]} for i, u in enumerate(UC)]}])
    tabs = "".join(
        f'<a class="sp-tab" href="#{i}" id="tab-{i}" role="tab" aria-controls="{i}" aria-selected="{"true" if n == 0 else "false"}"><img src="/img/{ic}" width="160" height="160" alt="" decoding="async"><span>{t}</span></a>'
        for n, (i, c, ic, a, t, d, s, w) in enumerate(UC))
    panels = ""
    for n, (i, c, ic, a, t, d, src, watch) in enumerate(UC):
        prv, nxt = UC[n - 1], UC[(n + 1) % len(UC)]
        lazy = ' fetchpriority="high"' if n == 0 else ' loading="lazy"'
        panels += (f'<div class="sp-panel {c}" id="{i}" role="tabpanel" aria-labelledby="tab-{i}" tabindex="-1"><div class="sp-p-main">'
                   f'<figure class="sp-scene"><img{lazy} src="/img/g-art-{a}-900.webp" srcset="/img/g-art-{a}-900.webp 900w, /img/g-art-{a}-1600.webp 1600w" sizes="(max-width: 980px) 100vw, 560px" width="1600" height="1195" alt="Illustration for {t}" decoding="async"></figure>'
                   f'<h2>{t}</h2><p class="sp-k">Stethos is built to</p><p class="sp-do">{d}</p><p class="uc-read"><a href="/use-cases/{i}">Read more about {t[0].lower() + t[1:]} <span aria-hidden="true">→</span></a></p></div><div class="sp-p-side">'
                   f'<p class="sp-k">Data you\'d use</p><ul class="sp-src">{"".join(f"<li>{x}</li>" for x in src)}</ul>'
                   f'<p class="sp-k">Signals you\'d watch</p><ul class="sp-see">{"".join(f"<li>{x}</li>" for x in watch)}</ul>'
                   f'<div class="sp-pn"><a href="#{prv[0]}" data-go="{prv[0]}"><span aria-hidden="true">←</span> {prv[4]}</a><a href="#{nxt[0]}" data-go="{nxt[0]}">{nxt[4]} <span aria-hidden="true">→</span></a></div></div></div>')
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top ph-top" aria-labelledby="sp-title">
  <div class="wrap">
    <div class="head ph">
      <h1 id="sp-title">Built for every product that needs <span class="pop">to know who practices where.</span></h1>
      <p class="sp-lede">Pick a use case to see which data and which change events it runs on.</p>
    </div>
    <div class="sp-layout"><div class="sp-tabs" role="tablist" aria-orientation="vertical" aria-label="Use cases">{tabs}</div><div class="sp-panels">{panels}</div></div>
  </div>
</section>
{cta_band("Free credits", "Building something else?", "Tell us what you need to know.", "Get a key, try every endpoint on your own use case, and pay only for the data you use.", "Stethos%20use%20case")}
</main>
'''
    return h + body + tail(("nav", "sp"))


# ---------- pricing ----------
def pp_card(pid, title, art, tint, who, amt_m, amt_y, per, bill_m, bill_y, trial, cta, href, feats, support, pop=False):
    li = lambda xs: "".join(f'<li>{CHECK}<span>{x}</span></li>' for x in xs)
    badge = '<span class="pp-badge">Most popular</span>' if pop else ''
    amt = f'<span class="pp-amt" data-m="{amt_m}" data-y="{amt_y}">{amt_m}</span>' if amt_y else f'<span class="pp-amt">{amt_m}</span>'
    bill = f'<p class="pp-bill" data-m="{bill_m}" data-y="{bill_y}">{bill_m}</p>' if bill_y else f'<p class="pp-bill">{bill_m}</p>'
    return (f'<article class="pp-card{" pop" if pop else ""}" aria-labelledby="pp-{pid}">{badge}<div class="pp-top"><img class="pp-art" src="/img/{art}" width="320" height="320" alt="" decoding="async" style="--t:{tint}"><h2 id="pp-{pid}">{title}</h2></div>'
            f'<p class="pp-who">{who}</p><p class="pp-price">{amt}<span class="pp-per">{per}</span></p>{bill}<p class="pp-trial">{trial}</p>'
            f'<a class="pp-cta" href="{href}" data-base="{href}">{cta} {ARROW}</a><div class="pp-feat"><p class="pp-gh">Includes</p><ul class="pp-list">{li(feats)}</ul><p class="pp-gh">Support</p><ul class="pp-list">{li(support)}</ul></div></article>')


COSTS = [
    ("Search result", "Name, NPI, specialty, city and primary organization", "0.05"),
    ("Provider record", "The base enriched record", "1"),
    ("+ Licenses", "Every state license with status", "+1"),
    ("+ Practice contact", "Phone, fax and practice address with sources", "+1"),
    ("+ Networks", "Payer network listings across directories", "+2"),
    ("+ Industry payments", "Open Payments summary", "+1"),
    ("Organization record", "Locations, children, leadership and open roles", "2"),
    ("Watcher event", "Each change event delivered to your webhook", "0.5"),
    ("Change history", "Every past event for one record", "1"),
]

PR_FAQ = [
    ("What is a credit?", "The unit every call is priced in. Searches cost a fraction of a credit per result, a full provider record costs one, and optional fields add to it. Every response includes a header showing the credits that call used."),
    ("When are credits used?", "Only when data comes back. A search with no matches, or an enrich on an NPI we don't have, costs nothing."),
    ("Do unused credits roll over?", "On Build, unused monthly credits roll over for one month. Top-up credits last 12 months."),
    ("What happens if I run out?", "Calls return a clear error, never a surprise bill. You can top up any time, or turn on auto top-up with a monthly cap."),
    ("Is there a free plan?", "Every account starts with 1,000 free credits, no card needed, so you can try every endpoint on your own use case."),
    ("Do you offer flat files?", "Yes, on Enterprise. We deliver the full dataset, or the slice you need, to your warehouse on a schedule."),
    ("Do I need a BAA?", "No. Stethos only holds data about healthcare professionals and organizations, not patients."),
]


def pricing():
    import json as _j
    faqld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in PR_FAQ]}
    prod = {"@type": "SoftwareApplication", "name": BRAND, "applicationCategory": "DeveloperApplication", "operatingSystem": "Web", "url": SITE + "/",
            "offers": [{"@type": "Offer", "name": "Free", "price": "0", "priceCurrency": "USD", "description": "1,000 credits, once"},
                       {"@type": "Offer", "name": "Build", "price": "149", "priceCurrency": "USD", "description": "20,000 credits a month"}]}
    h = head("Pricing: Healthcare Provider Data API | Stethos",
             "Start with 1,000 free credits. Build is $149 a month for 20,000 credits, webhooks and MCP. Enterprise adds flat files and volume pricing.",
             "/pricing", css=("styles", "v2", "site", "pricing"), image="/og/pricing.jpg", crumbs=[("Pricing", "/pricing")], schema=[faqld, prod])
    cards = (pp_card("free", "Free", "g-cl-ic-pin-cut.webp", "#e4f0fd", "To try every endpoint on your own use case.",
                     "$0", None, "1,000 credits, once", "No card needed", None, "No sales call", "Get an API key", f"{APP}/signup?plan=free",
                     ["Every endpoint: search, enrich, organizations", "Source and verified date on every field", "Up to 2 watchers", "API keys for 1 project"],
                     ["Docs and community support"])
             + pp_card("build", "Build", "g-cl-stk-agents-cut.webp", "#eff5d6", "For teams shipping a product or an agent.",
                       "$149", "$124", "per month · 20,000 credits", "Billed monthly", "Billed $1,490 yearly", "Starts with 1,000 free credits", "Start building", f"{APP}/signup?plan=build",
                       ["20,000 credits a month, unused credits roll over a month", "Unlimited watchers and webhooks", "MCP server for your agents", "Top-ups at $8 per 1,000 credits", "Up to 10 API keys and projects"],
                       ["Email support, next business day"], pop=True)
             + pp_card("enterprise", "Enterprise", "g-cl-stk-orgs-cut.webp", "#fdf5d2", "For data and product teams at scale.",
                       "Custom", None, "volume pricing", "Annual agreement", None, "Starts with a short call", "Talk to us", f"mailto:{EMAIL}?subject=Stethos%20Enterprise",
                       ["Everything in Build", "Flat files delivered to your warehouse", "Volume credit pricing", "Uptime and freshness SLAs", "Custom fields and sources", "Data agreement and security review"],
                       ["Shared Slack channel", "Named contact"]))
    rows = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td class="n">{c}</td></tr>' for a, b, c in COSTS)
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in PR_FAQ)
    body = f'''{HEADER}
<main id="main">
<section class="sec pp-hero" aria-labelledby="pr-title">
  <div class="wrap">
    <div class="pp-head">
      <div class="pp-head-t">
        <h1 id="pr-title">Pay for data, <span class="pop">not seats.</span></h1>
        <p class="pp-lede">Every account starts with free credits. Credits are only used when data comes back.</p>
      </div>
      <div class="pp-toggle" role="group" aria-label="Billing period">
        <button type="button" data-int="m" aria-pressed="true">Monthly</button>
        <button type="button" data-int="y" aria-pressed="false">Annual <span class="pp-save">2 months free</span></button>
      </div>
    </div>
    <div class="pp-grid">
      {cards}
    </div>
    <div class="pp-strip">
      <p class="pp-zero"><b>Free:</b> 1,000 credits<span aria-hidden="true">·</span>No card<span aria-hidden="true">·</span>No sales call</p>
      <ul class="pp-marks" aria-label="Payment methods"><li>Visa</li><li>Mastercard</li><li>Amex</li><li>Invoicing on Enterprise</li></ul>
      <p class="pp-remind">You'll get an email at 80% of your monthly credits.</p>
    </div>
    <div class="cost-wrap">
      <h2 id="cost-title">What each call costs</h2>
      <div class="cmp-wrap" tabindex="0" role="region" aria-labelledby="cost-title"><table class="cmp-table cost-table">
        <thead><tr><th scope="col">Data returned</th><th scope="col">What you get</th><th scope="col" class="n">Credits</th></tr></thead>
        <tbody>{rows}</tbody>
      </table></div>
      <p class="pp-example">An agent that searches 2,000 surgeons, enriches 300 with licenses and contacts, and watches them all month uses about <b>1,000 credits</b>.</p>
    </div>
  </div>
</section>
<section class="sec" aria-labelledby="pr-faq-title">
  <div class="wrap faq-grid">
    <div class="head"><p class="eyebrow"><span>FAQ</span></p><h2 id="pr-faq-title">Pricing questions</h2><figure class="faq-art"><img src="/img/g-art-pricing-900.webp" srcset="/img/g-art-pricing-900.webp 900w, /img/g-art-pricing-1600.webp 1600w" sizes="(max-width: 820px) 100vw, 480px" width="1600" height="1195" alt="Illustration: a glass jar of clay credit tokens beside a small meter dial." loading="lazy" decoding="async"></figure><p class="faq-more">Something else? <a href="mailto:{EMAIL}?subject=Stethos%20pricing">Email our team</a>.</p></div>
    <div class="qs">{faq}</div>
  </div>
</section>
{cta_band("Free credits", "Make your first call", "in five minutes.", "Get a key, try every endpoint, and see exactly what each call costs in the response headers.", "Stethos%20pricing")}
</main>
'''
    return h + body + tail(("nav", "pricing"))


# ---------- compare ----------
def compare(slug, them, title_a, title_b, lede, them_list, rows, both_h, both_p, sources, note, other):
    h = head(f"Stethos vs {them} | Provider Data Compared",
             f"How Stethos compares with {them} for healthcare provider data: API access, pricing model, data freshness and who each is built for.",
             f"/compare/{slug}", image="/og/compare.jpg", crumbs=[(f"Stethos vs {them}", f"/compare/{slug}")])
    tr = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows)
    src = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{t}</a></li>' for t, u in sources)
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top ph-top cmp-top" aria-labelledby="cmp-title">
  <div class="wrap">
    <div class="head ph">
      <h1 id="cmp-title">{title_a} <span class="pop">{title_b}</span></h1>
      <p class="sp-lede">{lede}</p>
    </div>
    <div class="cmp-pick">
      <div class="cmp-card them"><p class="sp-k">With {them}, you typically</p><ul>{"".join(f"<li>{x}</li>" for x in them_list)}</ul></div>
      <div class="cmp-card us"><p class="sp-k">With Stethos, you're built to</p><ul><li>Start today on free credits, no sales call</li><li>Pay per call and per field, not per seat</li><li>Get change events by webhook as they happen</li><li>See the source and verified date on every field</li><li>Let agents call it directly over MCP</li></ul></div>
    </div>
    <figure class="art-wide cmp-art">{art("compare", "Illustration: a dusty stack of sealed boxes and reports on one side, and the clay data machine sending out a stream of alerts on the other.", w=1600, h=893, lazy=False)}</figure>
  </div>
</section>
<section class="sec cmp-sec" aria-labelledby="cmp-table-title">
  <div class="wrap">
    <h2 id="cmp-table-title" class="cmp-h">Stethos vs {them}, side by side</h2>
    <div class="cmp-wrap" tabindex="0" role="region" aria-label="Comparison table"><table class="cmp-table">
      <thead><tr><th scope="col"><span class="sr">Area</span></th><th scope="col">{them}<span class="cmp-sub">Based on public materials</span></th><th scope="col" class="us">Stethos<span class="cmp-sub">Built for agents</span></th></tr></thead>
      <tbody>{tr}</tbody>
    </table></div>
    <div class="cmp-both"><h3>{both_h}</h3><p>{both_p}</p></div>
    <div class="cmp-src">
      <p class="sp-k">Sources</p>
      <ul>{src}</ul>
      <p class="cmp-note">{note}</p>
      <p class="cmp-other">{other}</p>
    </div>
  </div>
</section>
{cta_band("Free credits", "Try it on your", "own use case.", "Get a key and compare the records side by side. Pay only for the data you use.", "Stethos%20vs%20" + them.replace(" ", "%20"))}
</main>
'''
    return h + body + tail()


def compare_definitive():
    return compare(
        "definitive-healthcare", "Definitive Healthcare", "Definitive is a platform for analysts.", "Stethos is an API for agents.",
        "Definitive Healthcare is one of the largest healthcare commercial intelligence platforms, with deep data on hospitals, physicians and claims, sold mostly to enterprise teams. Stethos is built for developers and the agents they ship.",
        ["Buy an annual platform subscription through sales", "Search and filter in the web platform", "Pay extra to pipe data into your CRM or warehouse", "Work from periodic refreshes and exports", "Get deep claims and market analytics"],
        [("Who it's for", "Health systems, life sciences, medtech and other enterprise commercial teams.", "Developers and data teams building agents, apps and directories."),
         ("How you access it", "A web platform, with API access and bulk export typically sold as add-ons.", "REST API, webhooks and an MCP server from day one. Flat files on Enterprise."),
         ("How you pay", "Annual contracts priced by modules and seats, quoted by sales.", "Free credits to start, then pay per call and per field."),
         ("Freshness", "Periodically refreshed datasets.", "Sources re-checked on a rolling basis, with every change recorded as an event."),
         ("Knowing what changed", "Compare exports or check the platform.", "Subscribe to change events and get a webhook."),
         ("Claims and market analytics", "A core strength.", "Not offered. Stethos focuses on who practices where, and what changed."),
         ("Patient data", "Claims-based analytics products.", "None. Provider and organization data only.")],
        "Already using Definitive?", "Keep it for claims and market analytics. Stethos is built for the real-time lookups and change alerts your product and agents need, priced so you can call it from code.",
        [("Definitive Healthcare: Home", "https://www.definitivehc.com"), ("Ampliz: Definitive Healthcare pricing and alternatives (2026, third-party)", "https://www.ampliz.com/resources/definitive-healthcare-pricing"),
         ("Sultan of SaaS: Definitive Healthcare review (2026, third-party)", "https://sultanofsaas-com.pages.dev/tools/definitive-healthcare/")],
        "Definitive Healthcare details are based on its public website and third-party reviews as of November 2026; pricing and packaging may differ by contract. Definitive Healthcare is a trademark of its owner; Stethos is not affiliated with it. Stethos is in development, and its column describes what it is built to do.",
        '<a href="/compare/iqvia-onekey">See Stethos vs IQVIA OneKey <span aria-hidden="true">→</span></a>')


def compare_onekey():
    return compare(
        "iqvia-onekey", "IQVIA OneKey", "OneKey is reference data for life sciences.", "Stethos is built for agents.",
        "IQVIA OneKey is a long-established reference dataset of healthcare professionals and organizations, delivered through APIs, portals and data services and connected to IQVIA's other datasets. Stethos is built for developers who want to start small and pay per call.",
        ["Sign a multi-year agreement through sales", "Use OneKey as the master data behind your CRM", "Connect it to other IQVIA datasets", "Request data corrections through validation workflows", "Budget for an enterprise contract"],
        [("Who it's for", "Life sciences commercial, compliance and regulatory teams.", "Developers and data teams building agents, apps and directories."),
         ("How you access it", "APIs, portals and integrated data services.", "REST API, webhooks and an MCP server. Flat files on Enterprise."),
         ("How you pay", "Enterprise agreements; one third-party review puts IQVIA spend at $50k to $500k+ a year across modules.", "Free credits to start, then pay per call and per field."),
         ("Getting started", "A sales process and implementation.", "An API key in minutes, no sales call."),
         ("Knowing what changed", "Refreshed reference data and validation requests.", "Subscribe to change events and get a webhook."),
         ("Connected datasets", "A strength: unique IDs link to IQVIA's wider data.", "NPI-keyed, so it joins to your own claims, CRM and EHR data."),
         ("Patient data", "Separate IQVIA products.", "None. Provider and organization data only.")],
        "Already on OneKey?", "Keep it as your CRM's master data if it works for you. Stethos is built for the fast, cheap lookups and change alerts that agents and new products need.",
        [("IQVIA: Connect your organization to a single source provider for reference data", "https://www.iqvia.com/locations/united-states/library/fact-sheets/connect-your-organization-to-a-single-source-provider-for-reference-data"),
         ("IQVIA: OneKey reference data", "https://www.iqvia.com/locations/united-states/library/fact-sheets/onekey-reference-data"),
         ("Prospeo: Definitive Healthcare alternatives (2026, third-party, includes IQVIA pricing estimate)", "https://prospeo.io/s/definitive-healthcare-alternatives")],
        "IQVIA OneKey details are based on IQVIA's public fact sheets and third-party reviews as of November 2026; pricing varies by contract. IQVIA and OneKey are trademarks of their owner; Stethos is not affiliated with them. Stethos is in development, and its column describes what it is built to do.",
        '<a href="/compare/definitive-healthcare">See Stethos vs Definitive Healthcare <span aria-hidden="true">→</span></a>')


# ---------- docs ----------
def docs():
    tech = {"@type": "TechArticle", "headline": "Stethos API quickstart", "about": "Healthcare provider data API", "dateModified": "2026-11-05",
            "author": {"@type": "Organization", "name": BRAND}, "mainEntityOfPage": SITE + "/docs"}
    h = head("Provider Data API Docs: NPI Search and Enrich | Stethos", "Quickstart for the Stethos API: authenticate, search providers, enrich a record from an NPI, watch for changes by webhook and connect the MCP server.",
             "/docs", crumbs=[("Docs", "/docs")], schema=[tech])
    body = f'''{HEADER}
<main id="main" class="wrap doc">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Docs</nav>
  <h1>Quickstart</h1>
  <p class="doc-meta">API preview · endpoints and prices may change before launch</p>
  <ul class="doc-toc"><li><a href="#auth">Authenticate</a></li><li><a href="#search">Search</a></li><li><a href="#enrich">Enrich</a></li><li><a href="#orgs">Organizations</a></li><li><a href="#watch">Watchers</a></li><li><a href="#mcp">MCP</a></li><li><a href="#credits">Credits</a></li><li><a href="#errors">Errors</a></li></ul>
  <p class="note">Stethos is in development. This page shows the API we're building so you can plan against it. <a href="{APP}/signup">Join early access</a> to get a key when it opens.</p>

  <h2 id="auth">Authenticate</h2>
  <p>Every request takes your API key as a bearer token. Keys are created per project in the dashboard.</p>
<pre><code>export STETHOS_KEY="sk_live_..."
curl https://api.stethos.health/v1/account \\
  -H "Authorization: Bearer $STETHOS_KEY"</code></pre>

  <h2 id="search">Search providers</h2>
  <p>Search returns lightweight matches at 0.05 credits per result. Filter by <code>specialty</code>, <code>state</code>, <code>city</code>, <code>license_state</code>, <code>affiliation_type</code>, <code>org_id</code> or <code>network</code>.</p>
<pre><code>curl https://api.stethos.health/v1/providers/search \\
  -H "Authorization: Bearer $STETHOS_KEY" \\
  -d '{{"specialty": "orthopedic surgery", "state": "AZ", "limit": 50}}'</code></pre>

  <h2 id="enrich">Enrich a provider</h2>
  <p>Pass an <code>npi</code>, or a name plus city and state. The base record costs 1 credit; each extra field group adds to it, so ask only for what you need.</p>
<pre><code>curl https://api.stethos.health/v1/providers/enrich \\
  -H "Authorization: Bearer $STETHOS_KEY" \\
  -d '{{"npi": "1234567890", "fields": ["licenses", "practice_contact"]}}'</code></pre>
  <p>Every field comes back with a <code>source</code> and a <code>verified</code> date. When sources disagree, the response includes <code>alternatives</code> so you can choose.</p>

  <h2 id="orgs">Organizations</h2>
  <p>Look up health systems, hospitals, groups and clinics by name, <code>org_id</code> or NPI. Records include locations, child organizations, rostered clinicians, leadership and open clinical roles.</p>
<pre><code>curl https://api.stethos.health/v1/orgs/enrich \\
  -H "Authorization: Bearer $STETHOS_KEY" \\
  -d '{{"name": "Example Health System", "state": "AZ"}}'</code></pre>

  <h2 id="watch">Watchers and webhooks</h2>
  <p>A watcher follows a set of NPIs or organizations and posts an event to your webhook when something changes. Each delivered event costs 0.5 credits.</p>
  <table><thead><tr><th>Event</th><th>Fires when</th></tr></thead><tbody>
    <tr><td><code>affiliation.changed</code></td><td>A clinician joins or leaves a group, hospital or system</td></tr>
    <tr><td><code>license.issued</code> · <code>license.lapsed</code></td><td>A state license is added, expires or is restricted</td></tr>
    <tr><td><code>network.joined</code> · <code>network.left</code></td><td>A listing appears in or drops from a payer directory</td></tr>
    <tr><td><code>location.opened</code></td><td>A new practice site or clinic is seen</td></tr>
    <tr><td><code>org.exec_hire</code></td><td>An organization names a new executive</td></tr>
    <tr><td><code>org.hiring_spike</code></td><td>Clinical job posts rise well above normal</td></tr>
  </tbody></table>
<pre><code>curl https://api.stethos.health/v1/watchers \\
  -H "Authorization: Bearer $STETHOS_KEY" \\
  -d '{{"npis": ["1234567890"], "events": ["affiliation.changed"],
       "webhook_url": "https://your-app.example/hooks/stethos"}}'</code></pre>
  <p>Webhooks are signed with your project secret in the <code>Stethos-Signature</code> header. Failed deliveries retry with backoff for 24 hours.</p>

  <h2 id="mcp">MCP server</h2>
  <p>Agents in Claude and other MCP clients can use Stethos as tools: <code>search_providers</code>, <code>enrich_provider</code>, <code>enrich_org</code> and <code>recent_changes</code>. Add the server URL and your key in your client's connector settings.</p>
<pre><code>https://mcp.stethos.health/v1   # Authorization: Bearer $STETHOS_KEY</code></pre>

  <h2 id="credits">Credits</h2>
  <p>Every response includes an <code>X-Credits-Used</code> header, and <code>GET /v1/account/credits</code> returns your balance for free. See <a href="/pricing">pricing</a> for the cost of each call.</p>

  <h2 id="errors">Errors and limits</h2>
  <table><thead><tr><th>Status</th><th>Meaning</th></tr></thead><tbody>
    <tr><td>401</td><td>Missing or invalid API key</td></tr>
    <tr><td>402</td><td>Out of credits. Nothing was charged.</td></tr>
    <tr><td>404</td><td>No record found. Nothing was charged.</td></tr>
    <tr><td>429</td><td>Rate limit: 600 requests a minute on Build. Retry after the <code>Retry-After</code> header.</td></tr>
  </tbody></table>
  <p>Questions? Email <a href="mailto:{EMAIL}?subject=Stethos%20API">{EMAIL}</a>.</p>
</main>
'''
    return h + body + tail()


def privacy():
    h = head("Privacy Notice | Stethos", "How Stethos handles information you share through this website, and what data the Stethos API does and does not hold.", "/privacy", crumbs=[("Privacy", "/privacy")])
    body = f'''{HEADER}
<main id="main" class="wrap doc">
  <h1>Privacy notice</h1>
  <p class="doc-meta">Last updated November 5, 2026 · Draft for review</p>
  <h2>What this covers</h2>
  <p>This notice covers the Stethos marketing website. Stethos is in development. Before the API opens, we will publish terms and a data policy that cover the product itself.</p>
  <h2>What we collect on this site</h2>
  <p>If you email us or join early access, we receive your name, work email, company and anything you choose to tell us. Our hosting provider records standard technical information, such as browser type and referring page, in normal server logs. This site does not use advertising or analytics cookies.</p>
  <h2>How we use it</h2>
  <p>Only to contact you about Stethos, including early access, research conversations and product updates. We do not sell your information or share it for others' marketing.</p>
  <h2>About the data in the API</h2>
  <p>The Stethos API is built to hold information about healthcare professionals and organizations in their professional capacity, drawn from public registries and licensed sources. It does not hold patient information. Clinicians who want to correct or ask about their record can email us.</p>
  <h2>Your choices</h2>
  <p>You can ask us to update or delete your information, or to stop contacting you, at any time by emailing <a href="mailto:{EMAIL}?subject=Stethos%20privacy%20request">{EMAIL}</a>.</p>
  <h2>Contact</h2>
  <p>Questions about this notice can go to <a href="mailto:{EMAIL}?subject=Stethos%20privacy">{EMAIL}</a>.</p>
</main>
'''
    return h + body + tail()


def notfound():
    h = head("Page not found | Stethos", "This page doesn't exist.", "/404")
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top nf" aria-labelledby="nf-title">
  <div class="wrap">
    <div class="head center">
      <img class="nf-art" src="/img/g-art-notfound-900.webp" width="900" height="672" alt="" decoding="async">
      <p class="eyebrow"><span>404</span></p>
      <h1 id="nf-title">This pin wandered <span class="pop">off the map.</span></h1>
      <p class="sp-lede">We couldn't find what you were looking for. Try one of these instead.</p>
      <div class="nf-links"><a class="btn-1" href="/">Home</a><a class="btn-2" href="/docs">Docs</a><a class="btn-2" href="/pricing">Pricing</a></div>
    </div>
  </div>
</section>
</main>
'''
    return h.replace('content="index,follow,max-image-preview:large"', 'content="noindex"') + body + tail()
