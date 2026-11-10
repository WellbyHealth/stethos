from parts import *
from segments import scene, seg_grid, seg_tabs, logo

# ---------- use cases (same tabbed layout as Inroad's specialties page) ----------
UC = [
    ("medtech", "sp-blue", "g-cl-stk-search-160.webp", "uc-medtech", "Medtech sales",
     "Give your sales agents the surgeons, groups and facilities that fit your product, and tell them the week a target moves, opens a site or starts a new service line.",
     ["Specialty, procedure focus and practice setting", "Group and hospital affiliations", "Licenses by state", "Practice contact details", "Industry payments from Open Payments"],
     ["A target surgeon changes groups", "A new ambulatory surgery center opens", "A health system names a new service line leader"]),
    ("pharma", "sp-lime", "g-cl-stk-enrich-160.webp", "s-medicare", "Pharma and life sciences",
     "Map the prescribers, key opinion leaders and institutions that matter for a launch, and keep commercial and medical teams current as people move.",
     ["Prescribing volume by drug class from Medicare Part D", "Publications, clinical trials and NIH grants", "Hospital and group affiliations", "Industry payments from Open Payments"],
     ["A high-volume prescriber changes practice", "A key opinion leader joins a new institution", "A new practice opens in a launch territory"]),
    ("health-it-sales", "sp-lime", "g-cl-ic-code-cut.webp", "compare", "Health IT and services sales",
     "Build target lists of health systems and practices by EHR, size and service lines, and reach the buyer the week a new leader starts or a system changes vendors.",
     ["Health systems, groups and clinics, with locations and size", "Certified health IT and EHR in use, where published", "Executives and service line leaders", "Parent and affiliate links across a system"],
     ["A health system names a new CIO, CMO or CFO", "A practice joins a larger group", "A system opens new sites in your territory"]),
    ("healthcare-marketing", "sp-pink", "g-cl-ic-pin-cut.webp", "cta", "Healthcare marketing",
     "Build audiences of clinicians and organizations for campaigns, events and account-based marketing, and keep lists clean as people change jobs.",
     ["Clinician audiences by specialty, setting and state", "Account lists of systems and groups, with who works where", "Practice contact details, with sources", "Conference and market-level counts"],
     ["A contact on a list changes employer", "A new practice opens in a target market", "An account adds clinicians in your specialty"]),
    ("investors", "sp-pink", "g-cl-stk-orgs-160.webp", "uc-investors", "Healthcare investors",
     "Track practice roll-ups, clinician headcount at portfolio and target companies, and new entrants in a market as it happens, not a quarter later.",
     ["Organizations with ownership, private equity owners and parent–child links", "Rostered clinicians per organization over time", "Locations by market"],
     ["A group adds or loses clinicians", "A new location opens in a target market", "An executive hire at a target"]),
    ("digital-health", "sp-blue", "g-cl-stk-agents-160.webp", "uc-digital", "Healthcare startups",
     "Find your first customers and design partners, size your market, and power provider search in your product, all from one API and MCP server.",
     ["Provider search by specialty, location and network", "Organization and location records", "NPI-keyed records that join to your data"],
     ["A provider in your app changes location", "A practice joins a network your users have", "A record your app shows is re-verified"]),
    ("post-acute", "sp-lime", "g-cl-ic-pin-cut.webp", "notfound", "Post-acute care and agencies",
     "There are always more referrers than your marketers can cover. Stethos ranks the ones worth working, reminds each marketer which referrers have gone quiet, and maps your network against the whole market.",
     ["Your referral list, matched to current records", "Physicians, practices and hospitals by market, with size and affiliations", "Large medical campuses broken down by department and who works where", "Physicians who order home health and hospice, from Medicare data", "Care Compare ratings for you and your competitors"],
     ["A referrer you haven't reached in a while", "A referring physician changes practice or hospital", "A new practice or clinic opens in your territory"]),
    ("clinical-staffing", "sp-butter", "g-cl-ic-license-cut.webp", "uc-staffing", "Clinical staffing and recruiting",
     "Source licensed clinicians by state and specialty for your recruiters and agents, and find the health systems hiring hardest right now.",
     ["Clinicians by specialty and license state", "Current employer and affiliation history", "Organizations with open clinical roles"],
     ["A new state license is issued", "An organization's clinical job posts spike", "A clinician leaves a large employer"]),
    ("provider-directories", "sp-lime", "g-cl-ic-payer-cut.webp", "uc-payer", "Provider directories and networks",
     "Check every listing in your directory against current sources, and flag stale addresses, lapsed licenses and network mismatches before members run into them.",
     ["Practice locations and phone numbers, with sources", "Licenses and their status", "Payer network listings across directories", "Accepting-new-patients signals where published"],
     ["A clinician leaves a listed location", "A license lapses or is restricted", "A practice drops out of a network"]),
    ("health-systems", "sp-pink", "g-cl-stk-orgs-160.webp", "s-healthsys", "Health systems",
     "Map the community physicians around your hospitals, see who is affiliated with you or a competitor, and tell your physician liaisons when a doctor moves or opens a practice.",
     ["Community physicians by specialty and location", "Hospital and group affiliations, including competitors", "ACO participation", "Medicare volume by clinician"],
     ["A physician joins a competing group", "A new practice opens in your service area", "A group joins another health system"]),
]


def use_cases():
    h = head("Use Cases: Healthcare Sales and Marketing Data | Stethos",
             "How medtech, pharma, health IT, post-acute, startup and investment teams use Stethos to find, size and track healthcare markets, accounts and clinicians.",
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
{cta_band("Self-serve", "Building something else?", "Tell us what you need to know.", "Add Stethos to your agent, try every tool on your own use case, and pay only for what you use.", "Stethos%20use%20case")}
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
    ("<code>search_providers</code>", "Name, NPI, specialty, city and primary organization, per result", "0.05"),
    ("<code>enrich_provider</code>", "The base provider record", "1"),
    ("&nbsp;&nbsp;+ licenses", "Every state license with status", "+1"),
    ("&nbsp;&nbsp;+ practice_contact", "Phone, fax and practice address with sources", "+1"),
    ("&nbsp;&nbsp;+ networks", "Payer network listings across directories", "+2"),
    ("&nbsp;&nbsp;+ industry_payments", "Open Payments summary", "+1"),
    ("<code>enrich_org</code>", "Locations, children, leadership and open roles", "2"),
    ("<code>watch_providers</code>", "Each change event delivered to your agent or webhook", "0.5"),
    ("<code>recent_changes</code>", "Every past event for one record", "1"),
]

PR_FAQ = [
    ("What is a credit?", "The unit every tool call is priced in. Searches cost a fraction of a credit per result, a full provider record costs one, and optional fields add to it. Every tool result shows the credits that call used."),
    ("Do I need to talk to sales?", "No. Sign up, add the MCP server to your client and start calling tools. Plans and top-ups are self-serve. Enterprise is there if you later want flat files, volume pricing or an SLA."),
    ("When are credits used?", "Only when data comes back. A search with no matches, or an enrich on an NPI we don't have, costs nothing."),
    ("Do unused credits roll over?", "On Build, unused monthly credits roll over for one month. Top-up credits last 12 months."),
    ("What happens if I run out?", "Calls return a clear error, never a surprise bill. You can top up any time, or turn on auto top-up with a monthly cap."),
    ("Is there a free plan?", "Every account starts with 1,000 free credits, no card needed, so you can try every tool on your own use case."),
    ("Do you offer flat files?", "Yes, on Enterprise. We deliver the full dataset, or the slice you need, to your warehouse on a schedule."),
    ("Do I need a BAA?", "No. Stethos only holds data about healthcare professionals and organizations, not patients."),
]


def pricing():
    import json as _j
    faqld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in PR_FAQ]}
    prod = {"@type": "SoftwareApplication", "name": BRAND, "applicationCategory": "DeveloperApplication", "operatingSystem": "Web", "url": SITE + "/",
            "offers": [{"@type": "Offer", "name": "Free", "price": "0", "priceCurrency": "USD", "description": "1,000 credits, once"},
                       {"@type": "Offer", "name": "Build", "price": "149", "priceCurrency": "USD", "description": "20,000 credits a month"}]}
    h = head("Pricing: Pay Per Tool Call | Stethos MCP Server",
             "Self-serve pricing per MCP tool call. Start with 1,000 free credits, no card. Build is $149 a month for 20,000 credits. Enterprise adds flat files.",
             "/pricing", css=("styles", "v2", "site", "pricing"), image="/og/pricing.jpg", crumbs=[("Pricing", "/pricing")], schema=[faqld, prod])
    cards = (pp_card("free", "Free", "g-cl-ic-pin-cut.webp", "#e4f0fd", "To try every endpoint on your own use case.",
                     "$0", None, "1,000 credits, once", "No card needed", None, "Live in five minutes", "Start free trial", TRIAL,
                     ["Every tool: search, enrich, organizations, watch", "Source and verified date on every field", "Up to 2 watchers", "Works in Claude, Cursor and any MCP client"],
                     ["Docs and community support"])
             + pp_card("build", "Build", "g-cl-stk-agents-cut.webp", "#eff5d6", "For teams shipping a product or an agent.",
                       "$149", "$124", "per month · 20,000 credits", "Billed monthly", "Billed $1,490 yearly", "Starts with 1,000 free credits", "Start self-serve", f"{TRIAL}?plan=build",
                       ["20,000 credits a month, unused credits roll over a month", "Unlimited watchers, plus webhooks for your backend", "REST API alongside the MCP server", "Top-ups at $8 per 1,000 credits", "Up to 10 projects and keys"],
                       ["Email support, next business day"], pop=True)
             + pp_card("enterprise", "Enterprise", "g-cl-stk-orgs-cut.webp", "#fdf5d2", "For data and product teams at scale.",
                       "Custom", None, "volume pricing", "Annual agreement", None, "Optional, once you scale", "Talk to us", f"mailto:{EMAIL}?subject=Stethos%20Enterprise",
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
        <h1 id="pr-title">Pay per tool call. <span class="pop">No sales call.</span></h1>
        <p class="pp-lede">Self-serve from the first call. Every account starts with 1,000 free credits, and credits are only used when a tool returns data.</p>
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
      <p class="pp-zero"><b>Self-serve:</b> 1,000 free credits<span aria-hidden="true">·</span>No card<span aria-hidden="true">·</span>No sales call<span aria-hidden="true">·</span>Live in five minutes</p>
      <ul class="pp-marks" aria-label="Payment methods"><li>Visa</li><li>Mastercard</li><li>Amex</li><li>Invoicing on Enterprise</li></ul>
      <p class="pp-remind">You'll get an email at 80% of your monthly credits.</p>
    </div>
    <div class="cost-wrap">
      <h2 id="cost-title">What each tool call costs</h2>
      <div class="cmp-wrap" tabindex="0" role="region" aria-labelledby="cost-title"><table class="cmp-table cost-table">
        <thead><tr><th scope="col">Tool</th><th scope="col">What you get</th><th scope="col" class="n">Credits</th></tr></thead>
        <tbody>{rows}</tbody>
      </table></div>
      <p class="pp-example">An agent that searches 2,000 surgeons, enriches 300 with licenses and contacts, and watches them all month uses about <b>1,000 credits</b>, which fits inside the free tier.</p>
    </div>
  </div>
</section>
{scene("w-pricing", "Illustration: a pastel vending machine on a hill dispensing tokens, with the little robot catching them in a basket.")}
<section class="sec" aria-labelledby="pr-faq-title">
  <div class="wrap faq-grid">
    <div class="head"><p class="eyebrow"><span>FAQ</span></p><h2 id="pr-faq-title">Pricing questions</h2><figure class="faq-art"><img src="/img/g-art-pricing-900.webp" srcset="/img/g-art-pricing-900.webp 900w, /img/g-art-pricing-1600.webp 1600w" sizes="(max-width: 820px) 100vw, 480px" width="1600" height="1195" alt="Illustration: a glass jar of clay credit tokens beside a small meter dial." loading="lazy" decoding="async"></figure><p class="faq-more">Something else? <a href="mailto:{EMAIL}?subject=Stethos%20pricing">Email our team</a>.</p></div>
    <div class="qs">{faq}</div>
  </div>
</section>
{cta_band("Self-serve", "Make your first tool call", "in five minutes.", "Add Stethos to Claude or any MCP client, sign in, and see exactly what each call costs in the result.", "Stethos%20pricing")}
</main>
'''
    return h + body + tail(("nav", "pricing"))


# ---------- compare ----------
CMP_ART = {"definitive-healthcare": ("cmp-dh", "Illustration: a balance scale with a heavy, padlocked stack of binders on one side and a single light data card with a bell on the other."),
           "iqvia-onekey": ("cmp-iqvia", "Illustration: a big padlocked chest with a long contract unrolling out of it, next to a small open box where a robot pulls out one data card.")}


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
      <div class="cmp-card us"><p class="sp-k">With Stethos, you're built to</p><ul><li>Add it to Claude in five minutes, no sales call</li><li>Pay per tool call and per field, not per seat</li><li>Get change events as they happen</li><li>See the source and verified date on every field</li><li>Use REST and webhooks for the rest of your stack</li></ul></div>
    </div>
    <figure class="art-wide cmp-art">{art(CMP_ART[slug][0], CMP_ART[slug][1], w=1600, h=900, lazy=False)}</figure>
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
{cta_band("Self-serve", "Try it on your", "own use case.", "Add Stethos to your agent and compare the records side by side. Pay only for the tool calls you make.", "Stethos%20vs%20" + them.replace(" ", "%20"))}
</main>
'''
    return h + body + tail()


def compare_definitive():
    return compare(
        "definitive-healthcare", "Definitive Healthcare", "Definitive is a platform for analysts.", "Stethos is an API for agents.",
        "Definitive Healthcare is one of the largest healthcare commercial intelligence platforms, with deep data on hospitals, physicians and claims, sold mostly to enterprise teams. Stethos is built for developers and the agents they ship.",
        ["Buy an annual platform subscription through sales", "Search and filter in the web platform", "Pay extra to pipe data into your CRM or warehouse", "Work from periodic refreshes and exports", "Get deep claims and market analytics"],
        [("Who it's for", "Health systems, life sciences, medtech and other enterprise commercial teams.", "Developers and data teams building agents, apps and directories."),
         ("How you access it", "A web platform, with API access and bulk export typically sold as add-ons.", "An MCP server your agents call directly, plus REST and webhooks. Flat files on Enterprise."),
         ("How you pay", "Annual contracts priced by modules and seats, quoted by sales.", "Self-serve: free credits to start, then pay per tool call and per field."),
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
         ("How you access it", "APIs, portals and integrated data services.", "An MCP server your agents call directly, plus REST and webhooks. Flat files on Enterprise."),
         ("How you pay", "Enterprise agreements; one third-party review puts IQVIA spend at $50k to $500k+ a year across modules.", "Self-serve: free credits to start, then pay per tool call and per field."),
         ("Getting started", "A sales process and implementation.", "Paste one URL into your MCP client. Live in five minutes, no sales call."),
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
    h = head("Docs: Connect the Stethos MCP Server | Stethos", "Add the Stethos healthcare MCP server to Claude, Cursor or any MCP client in five minutes. Tools, credits, REST API and webhooks.",
             "/docs", crumbs=[("Docs", "/docs")], schema=[tech])
    body = f'''{HEADER}
<main id="main" class="wrap doc">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Docs</nav>
  <h1>Quickstart: connect Stethos to your agent</h1>
  <p class="doc-meta">Preview · tools and prices may change before launch</p>
  <figure class="scene-inline"><img src="/img/g-w-docs-1600.webp" srcset="/img/g-w-docs-900.webp 900w, /img/g-w-docs-1600.webp 1600w" sizes="(max-width: 800px) 100vw, 760px" width="1600" height="686" alt="Illustration: the little robot at a workbench on a hill, plugging cables into the clay data machine." decoding="async"></figure>
  <ul class="doc-toc"><li><a href="#connect">Connect</a></li><li><a href="#tools">Tools</a></li><li><a href="#sources">Data sources</a></li><li><a href="#credits">Credits</a></li><li><a href="#rest">REST API</a></li><li><a href="#watch">Webhooks</a></li><li><a href="#errors">Errors</a></li></ul>
  <p class="note">Stethos is in development. This page shows the MCP server and API we're building so you can plan against it. <a href="{TRIAL}">Join early access</a> to get access when it opens.</p>

  <h2 id="connect" class="h-spot"><img src="/img/g-spot-connect-320.webp" width="160" height="160" alt="" loading="lazy" decoding="async">Connect in five minutes</h2>
  <p>Stethos is a remote MCP server. One URL gives your agent every tool:</p>
<pre><code>{MCP_URL}</code></pre>
  <h3>Claude</h3>
  <ol><li>Open Settings, then Connectors, and choose to add a custom connector.</li><li>Paste the server URL above and save.</li><li>Sign in to Stethos when prompted. The tools appear in your next chat.</li></ol>
  <h3>Cursor, Claude Code and other MCP clients</h3>
  <p>Add Stethos to your client's MCP config:</p>
<pre><code>{{
  "mcpServers": {{
    "stethos": {{ "url": "{MCP_URL}" }}
  }}
}}</code></pre>
  <p>For agents that can't sign in through a browser, create a key in the dashboard and send it as <code>Authorization: Bearer $STETHOS_KEY</code>.</p>

  <h2 id="tools" class="h-spot"><img src="/img/g-spot-tools-320.webp" width="160" height="160" alt="" loading="lazy" decoding="async">Tools</h2>
  <table><thead><tr><th>Tool</th><th>What it does</th><th>Credits</th></tr></thead><tbody>
    <tr><td><code>search_providers</code></td><td>Find clinicians and organizations by specialty, location, license state, affiliation or network</td><td>0.05 per result</td></tr>
    <tr><td><code>enrich_provider</code></td><td>Full record for an NPI, with optional licenses, practice contact, networks and payments</td><td>1 + fields</td></tr>
    <tr><td><code>enrich_org</code></td><td>Health system, hospital, group or clinic with locations, clinicians, leadership, open roles and owners, including private equity</td><td>2</td></tr>
    <tr><td><code>watch_providers</code></td><td>Follow NPIs or organizations and get told when they change</td><td>0.5 per event</td></tr>
    <tr><td><code>recent_changes</code></td><td>Change history for a record or a filter, such as new licenses in Texas this week</td><td>1</td></tr>
  </tbody></table>
  <p>Every result carries a <code>source</code> and <code>verified</code> date on each field. When sources disagree, the result includes <code>alternatives</code> so the agent can choose.</p>

  <h2 id="rest" class="h-spot"><img src="/img/g-spot-rest-320.webp" width="160" height="160" alt="" loading="lazy" decoding="async">REST API</h2>
  <p>The same data is available over REST for the parts of your stack that aren't agents. Authenticate with your key:</p>
<pre><code>export STETHOS_KEY="sk_live_..."
curl https://api.stethos.health/v1/account \\
  -H "Authorization: Bearer $STETHOS_KEY"</code></pre>

  <h3 id="search">Search providers</h3>
  <p>Search returns lightweight matches at 0.05 credits per result. Filter by <code>specialty</code>, <code>state</code>, <code>city</code>, <code>license_state</code>, <code>affiliation_type</code>, <code>org_id</code> or <code>network</code>.</p>
<pre><code>curl https://api.stethos.health/v1/providers/search \\
  -H "Authorization: Bearer $STETHOS_KEY" \\
  -d '{{"specialty": "orthopedic surgery", "state": "AZ", "limit": 50}}'</code></pre>

  <h3 id="enrich">Enrich a provider</h3>
  <p>Pass an <code>npi</code>, or a name plus city and state. The base record costs 1 credit; each extra field group adds to it, so ask only for what you need.</p>
<pre><code>curl https://api.stethos.health/v1/providers/enrich \\
  -H "Authorization: Bearer $STETHOS_KEY" \\
  -d '{{"npi": "1234567890", "fields": ["licenses", "practice_contact"]}}'</code></pre>
  <p>Every field comes back with a <code>source</code> and a <code>verified</code> date. When sources disagree, the response includes <code>alternatives</code> so you can choose.</p>

  <h3 id="orgs">Organizations</h3>
  <p>Look up health systems, hospitals, groups and clinics by name, <code>org_id</code> or NPI. Records include locations, child organizations, rostered clinicians, leadership and open clinical roles.</p>
<pre><code>curl https://api.stethos.health/v1/orgs/enrich \\
  -H "Authorization: Bearer $STETHOS_KEY" \\
  -d '{{"name": "Example Health System", "state": "AZ"}}'</code></pre>

  <h2 id="watch" class="h-spot"><img src="/img/g-spot-watch-320.webp" width="160" height="160" alt="" loading="lazy" decoding="async">Watchers and webhooks</h2>
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

  <h2 id="sources" class="h-spot"><img src="/img/g-spot-sources-320.webp" width="160" height="160" alt="" loading="lazy" decoding="async">Data sources</h2>
  <p>Every field Stethos returns names the source it came from and when it was last checked. Stethos is built on CMS and other government files first, resolved to one record per NPI, with licensed and web sources layered on top.</p>
  <table><thead><tr><th>Source</th><th>What it adds</th><th>Refresh</th><th>Access</th></tr></thead><tbody>
    <tr><td>CMS All Owners files</td><td>Owners of Medicare-enrolled hospitals, nursing homes, home health agencies, hospices, rural health clinics and FQHCs, with owner types such as private equity</td><td>Periodic</td><td>Public file</td></tr><tr><td>NPPES NPI Registry</td><td>Every clinician and organization NPI, taxonomy, practice address</td><td>Weekly</td><td>Public file</td></tr><tr><td>CMS National Provider Directory</td><td>Practitioners, organizations, locations and digital endpoints, in FHIR bulk files</td><td>Monthly</td><td>Public file</td></tr><tr><td>Medicare Physician &amp; Other Practitioners</td><td>Services and Medicare patients per clinician, by procedure code</td><td>Annual</td><td>Public file</td></tr><tr><td>Medicare Part D Prescribers</td><td>Prescribing volume per clinician, by drug</td><td>Annual</td><td>Public file</td></tr><tr><td>Medicare DMEPOS by Referring Provider</td><td>Durable equipment and supplies ordered per clinician</td><td>Annual</td><td>Public file</td></tr><tr><td>Medicare Inpatient &amp; Outpatient Hospitals</td><td>Discharges and services per hospital, by DRG and APC</td><td>Annual</td><td>Public file</td></tr><tr><td>Medicare Post-Acute Care &amp; Hospice</td><td>Volume, payments and patient mix per home health agency, hospice, SNF, IRF and LTCH</td><td>Annual</td><td>Public file</td></tr><tr><td>Care Compare and Provider Data Catalog</td><td>Star ratings, quality measures, clinician–group and hospital affiliations</td><td>Monthly to quarterly</td><td>Public file</td></tr><tr><td>Medicare Provider of Services file</td><td>Facility type, ownership, beds and certification</td><td>Quarterly</td><td>Public file</td></tr><tr><td>Medicare Shared Savings Program</td><td>Which practices and clinicians participate in each ACO</td><td>Annual</td><td>Public file</td></tr><tr><td>Hospital and SNF cost reports (HCRIS)</td><td>Beds, staffing, revenue and costs per facility</td><td>Quarterly</td><td>Public file</td></tr><tr><td>Medicare Advantage enrollment by county</td><td>MA penetration and plan mix in each market</td><td>Monthly</td><td>Public file</td></tr><tr><td>ONC certified health IT data</td><td>Which certified EHR each hospital and clinician reports using, and EHR vendors' published customer endpoint lists</td><td>Annual and ongoing</td><td>Public file</td></tr><tr><td>Open Payments</td><td>Industry payments to clinicians and teaching hospitals</td><td>Annual</td><td>Public file</td></tr><tr><td>Medicare Part A, B and MA claims, 100%</td><td>Current referral flows, shared patients, sources and destinations of post-acute patients, market share</td><td>Quarterly</td><td>Planned: CMS VRDC Innovator access</td></tr>
  </tbody></table>
  <p>CMS's public utilization files summarize 100% of Original Medicare claims but are released yearly, with a lag. Claims-level detail, such as which physicians actually refer to which home health agencies this quarter, requires CMS's Virtual Research Data Center. Stethos plans to apply as an Innovator, and only aggregate, privacy-protected outputs leave that environment. Provider data only: no patient data is ever returned.</p>

  <span id="mcp"></span>
  <h2 id="credits" class="h-spot"><img src="/img/g-spot-credits-320.webp" width="160" height="160" alt="" loading="lazy" decoding="async">Credits</h2>
  <p>Every tool result shows the credits it used (REST responses carry an <code>X-Credits-Used</code> header), and checking your balance is free. See <a href="/pricing">pricing</a> for the cost of each tool.</p>

  <h2 id="errors" class="h-spot"><img class="" src="/img/g-spot-r-errors-320.webp" width="160" height="160" alt="" loading="lazy" decoding="async">Errors and limits</h2>
  <table><thead><tr><th>Status</th><th>Meaning</th></tr></thead><tbody>
    <tr><td>401</td><td>Not signed in, or missing or invalid key</td></tr>
    <tr><td>402</td><td>Out of credits. Nothing was charged.</td></tr>
    <tr><td>404</td><td>No record found. Nothing was charged.</td></tr>
    <tr><td>429</td><td>Rate limit: 600 requests a minute on Build. Retry after the <code>Retry-After</code> header.</td></tr>
  </tbody></table>
  <p>Questions? Email <a href="mailto:{EMAIL}?subject=Stethos%20API">{EMAIL}</a>.</p>
</main>
'''
    return h + body + tail()


def privacy():
    h = head("Privacy Notice: Website and API Data | Stethos", "How Stethos handles information you share through this website, and what data the Stethos API does and does not hold.", "/privacy", crumbs=[("Privacy", "/privacy")])
    body = f'''{HEADER}
<main id="main" class="wrap doc">
  <img class="doc-spot" src="/img/g-spot-r-privacy-320.webp" width="160" height="160" alt="" loading="lazy" decoding="async">
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


def signup():
    h = head("Start your free trial | Stethos",
             "Get 1,000 free credits for the Stethos healthcare provider data MCP server. No card, no sales call. Works with Claude, Cursor and ChatGPT.",
             "/signup", crumbs=[("Free trial", "/signup")],
             share_title="Stethos | Start your free trial",
             share_desc="1,000 free credits for US healthcare provider data in Claude, Cursor or ChatGPT. No card, no sales call.")
    opts = lambda pairs: "".join(f'<option value="{v}">{t}</option>' for v, t in pairs)
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top su" aria-labelledby="su-title">
  <div class="wrap su-grid">
    <div class="su-copy">
      <p class="eyebrow"><span>Free trial</span></p>
      <h1 id="su-title">Start your <span class="pop">free trial.</span></h1>
      <p class="sp-lede">1,000 free credits for the Stethos MCP server and API. No card, no sales call.</p>
      <ul class="su-list">
        <li><b>Search and enrich</b> every US clinician, practice and health system</li>
        <li><b>A source and a checked date</b> on every field your agent gets back</li>
        <li><b>Watchers</b> that tell your agent when a provider moves or changes groups</li>
        <li><b>Works with</b> Claude, Cursor, ChatGPT or any MCP client, plus REST</li>
      </ul>
      <p class="su-note" id="signin">Stethos is in preview, and we're opening access in small batches. We'll email your key and setup link, usually within one business day. Already signed up? Your access link is in that email.</p>
    </div>
    <div class="su-card">
      <form id="su-form" novalidate>
        <label>Your name<input name="name" autocomplete="name" required></label>
        <label>Work email<input name="email" type="email" autocomplete="email" inputmode="email" required></label>
        <label>Company<input name="company" autocomplete="organization"></label>
        <label>What are you building?<select name="use_case">{opts([("medtech","Sales and targeting for medtech or pharma"),("health-it-sales","Sales for health IT or services"),("marketing","Healthcare marketing"),("provider-directory","A provider directory or network tool"),("post-acute","Post-acute care or an agency"),("staffing","Clinical staffing or recruiting"),("investing","Healthcare investing or diligence"),("digital-health","A healthcare startup or digital health product"),("other","Something else")])}</select></label>
        <label>Where will you use it?<select name="client">{opts([("claude","Claude"),("cursor","Cursor"),("chatgpt","ChatGPT"),("other-mcp","Another MCP client"),("rest-api","REST API from my own code")])}</select></label>
        <label><span>Anything we should know? <span class="opt">Optional</span></span><textarea name="note" rows="3"></textarea></label>
        <input type="hidden" name="source">
        <div class="su-hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
        <button class="su-btn" type="submit">Start free trial {ARROW}</button>
        <p class="su-err" role="alert" hidden></p>
        <p class="su-fine">By signing up you agree to our <a href="/privacy">privacy policy</a>. We'll only email you about your account.</p>
      </form>
      <div class="su-done" hidden tabindex="-1">
        <img src="/img/g-cl-logo-cut.webp" width="120" height="120" alt="">
        <h2>You're on the list.</h2>
        <p>We'll send your key and setup link to <b class="su-mail"></b>, usually within one business day.</p>
        <p>While you wait, see how to connect Stethos and what each tool returns.</p>
        <a class="su-btn" href="/docs#connect">Read the docs {ARROW}</a>
      </div>
    </div>
  </div>
</section>
{scene("w-signup", "Illustration: the little robot waving under a flower arch at the start of a path up the hills to the data machine.")}
</main>
'''
    return h + body + tail(("nav", "signup"))
