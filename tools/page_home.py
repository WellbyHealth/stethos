from parts import *
import os as _os
def _clients():
    d = _os.path.join(_os.path.dirname(__file__), "..", "public", "img", "clients")
    out = []
    for key, name in [("claude", "Claude"), ("cursor", "Cursor"), ("chatgpt", "ChatGPT")]:
        f = next((f"{key}.{e}" for e in ("svg", "png", "webp") if _os.path.isfile(_os.path.join(d, f"{key}.{e}"))), None)
        out.append(f'<li class="has-ic" title="{name}"><img src="/img/clients/{f}" width="20" height="20" alt="{name}"></li>' if f else f"<li>{name}</li>")
    return '<ul class="cx-clients" aria-label="Works with">' + "".join(out) + '<li class="cx-any">Any MCP client</li></ul>'
import json
CLIENTS = _clients()

FAQ = [
    ("What is Stethos?", "Current, sourced healthcare data for AI agents, delivered as an MCP server and API. Stethos resolves government, payer and web sources into one record for every US clinician, practice, health system and payer network, puts a source and a checked date on every field, keeps records current with verification agents, and tells your agent when something changes"),
    ("How does it help sales, marketing and investing?", "Your reps and agents can build target lists by specialty, setting, EHR or territory, enrich accounts and contacts with sourced fields, and get an alert the week a target changes jobs, a practice joins a system or a health system names a new leader. Those changes become your outreach triggers, and the records in your CRM stay current without anyone re-checking lists. Investment teams use the same tools to map a market, size a platform and track portfolio companies."),
    ("Can't my agent just ask a general AI assistant?", "General AI assistants can find some provider data, but they answer from whatever web page or registry copy they come across, often months or years old, with no source and no date. Provider data changes constantly: clinicians move groups, licenses lapse, networks change. Stethos re-checks its sources, shows where every field came from and when it was last checked, and tells your agent when a record changes."),
    ("Does it work with our CRM and AI tools?", "Yes, that's the point. Stethos runs as an MCP server inside Claude, ChatGPT, Microsoft Copilot Studio, Cursor or your own agent, and its REST API and webhooks keep records current in Salesforce, HubSpot, Attio or any CRM or data warehouse. There's no separate dashboard to adopt."),
    ("Who is it for?", "Anyone who sells into, markets to or invests in healthcare: medtech and pharma commercial teams, health IT, software and services sellers, healthcare marketers, investors and deal teams, startups finding their first customers, and clinical staffing firms. Stethos gives their people, agents and CRM a current view of who practices where, who buys, and what just changed. Provider directory teams use the same data."),
    ("Where does the data come from?", "Government files first: the NPPES NPI Registry, CMS's Medicare utilization files for clinicians, prescribers, hospitals, home health, hospice and nursing facilities, Care Compare ratings and affiliations, ACO participation, cost reports and Open Payments, plus state licensing boards. Payer directories, price transparency files, practice websites and health system job posts are layered on top. Every field carries its source and the date it was last checked. See the full list in the docs."),
    ("Does Stethos handle patient data?", "No. Stethos indexes healthcare professionals and organizations, not patients. There is no PHI in the API, so you don't need a business associate agreement to use it."),
    ("How fresh is it?", "Sources are re-checked on a rolling schedule, and every change is recorded as an event you can query or subscribe to with a webhook. Each record shows when it was last verified, so your agent can decide how much to trust it."),
    ("How is this different from Definitive Healthcare or IQVIA OneKey?", "Both are established, deep datasets, sold mostly through annual contracts to large commercial teams. Stethos is built API-first for developers and agents: pay per call, start free, and get change events instead of quarterly refreshes. See Stethos vs Definitive and Stethos vs IQVIA OneKey."),
    ("How do I connect it?", "Copy the Stethos MCP server URL and add it to your client: as a custom connector in Claude, or in the MCP config of Cursor or your own agent. Sign in, and the tools appear. It takes about five minutes and there's no sales call."),
    ("Is there a REST API too?", "Yes. The same data is available over REST, with webhooks for change events, for the parts of your stack that aren't agents."),
    ("How does pricing work?", "Per tool call, in credits. A search costs a fraction of a credit per result, enriching a provider costs more, and you only pay for the fields you ask for. Every account starts with 1,000 free credits, Build is a monthly plan, and Enterprise adds bulk files and volume pricing."),
    ("Can we get the whole dataset as a file?", "Yes, on Enterprise. We deliver flat files to your warehouse on a schedule, alongside API access for real-time lookups."),
    ("Is it live?", "Stethos is in development. The tools on this site are a preview of what we're building, and the results shown are sample data. Join the early access list and we'll send you access as soon as it's ready."),
]


def page():
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "name": BRAND, "url": SITE + "/", "logo": SITE + "/icon-512.png", "email": EMAIL, "@id": SITE + "/#org"},
        {"@type": "WebSite", "@id": SITE + "/#site", "name": BRAND, "url": SITE + "/", "publisher": {"@id": SITE + "/#org"}},
        {"@type": "SoftwareApplication", "name": BRAND, "applicationCategory": "DeveloperApplication", "operatingSystem": "Web", "url": SITE + "/",
         "description": "An MCP server and API for US healthcare provider and organization data, built for AI agents and priced per tool call.", "publisher": {"@id": SITE + "/#org"},
         "offers": [{"@type": "Offer", "name": "Free", "price": "0", "priceCurrency": "USD"}, {"@type": "Offer", "name": "Build", "price": "149", "priceCurrency": "USD", "url": SITE + "/pricing"}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]}
    pre = ('<link rel="preload" as="image" href="/img/g-hero-1600.webp" imagesrcset="/img/g-hero-1600.webp 1600w, /img/g-hero-2400.webp 2400w, /img/g-hero-3200.webp 3200w" imagesizes="100vw" media="(min-width: 761px)" fetchpriority="high">\n'
           '<link rel="preload" as="image" href="/img/g-hero-m-800.webp" imagesrcset="/img/g-hero-m-800.webp 800w, /img/g-hero-m-1200.webp 1200w" imagesizes="100vw" media="(max-width: 760px)" fetchpriority="high">\n')
    h = head("Stethos: Healthcare Sales and Marketing Data for AI Agents",
             "Current, sourced data on every US clinician, practice and health system, for healthcare sales, marketing and investment teams and their AI agents.",
             "/", css=("styles", "v2", "site", "home"), extra=pre,
             share_title="Stethos | Healthcare sales and marketing data for your AI agents",
             share_desc="Find, enrich and track every US clinician, practice and health system you sell to, from Claude, ChatGPT, your CRM or any MCP client. Start free with 1,000 credits.",
             ld=f'<script type="application/ld+json">{json.dumps(ld)}</script>\n')

    def stk(i, cls, pill, title, pop, note, img):
        return (f'<li class="stk-item" style="--i:{i}"><article class="stk {cls}" aria-labelledby="stk-h{i}"><p class="stk-pill">{pill}</p>'
                f'<h3 class="stk-h" id="stk-h{i}">{title}<span class="pop"> {pop}</span></h3><p class="stk-note">{note}</p>'
                f'<div class="stk-art" aria-hidden="true"><img src="/img/g-cl-{img}-cut.webp" srcset="/img/g-cl-{img}-cut.webp 480w, /img/g-cl-{img}-960.webp 960w" sizes="(max-width: 900px) 90vw, 560px" width="480" height="480" alt="" loading="lazy" decoding="async"><i></i><i></i><i></i></div></article></li>')

    faq = "\n".join(f'      <details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    faq = faq.replace("See Stethos vs Definitive and Stethos vs IQVIA OneKey.", 'See <a href="/compare/definitive-healthcare">Stethos vs Definitive</a> and <a href="/compare/iqvia-onekey">Stethos vs IQVIA OneKey</a>.')
    faq = faq.replace("Join the early access list", f'<a href="{TRIAL}">Join the early access list</a>')

    body = f'''{HEADER}
<main id="main">
<section class="hero cx" aria-labelledby="hero-title">
  <div class="wrap cx-copy">
    <h1 id="hero-title">Turn your agent into a world&#8209;class <span class="rot" data-rot data-words="pharma rep|SDR|deal team|marketing team|founder"><span class="rot-w on">medtech rep</span></span></h1>
    <p class="cx-sub">Current, sourced data on every US clinician, practice and health system, inside the CRM and AI tools your team already uses.</p>
    <div class="cx-ctas"><a class="cx-btn dark" href="{TRIAL}">Start free trial<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a><a class="cx-btn light" href="/docs">Read the docs<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>
    <div class="cx-paste">
      <span class="cx-paste-k">Paste in your coding agent</span>
      <code class="cx-paste-v">Add the Stethos MCP server: {MCP_URL}</code>
      <button class="cx-copybtn copy-mcp" type="button" data-copy="Add the Stethos MCP server: {MCP_URL}">Copy</button>
    </div>
    <div class="cx-meta"><span class="cx-or">or install directly with</span>{CLIENTS}<span class="cx-fine">1,000 free credits · no card · no sales call</span></div>
  </div>
  <picture class="cx-art">
    <source media="(max-width: 760px)" srcset="/img/g-hero-m-800.webp 800w, /img/g-hero-m-1200.webp 1200w" sizes="100vw">
    <img src="/img/g-hero-1600.webp" srcset="/img/g-hero-1600.webp 1600w, /img/g-hero-2400.webp 2400w, /img/g-hero-3200.webp 3200w" sizes="100vw" width="3200" height="1358" alt="Illustration: a friendly clay data machine with a glass dome over a map of pins. Records flow into it from a hospital, a doctor's office, government buildings and an insurance office floating on clouds, and alerts flow out to three small clay robots working at laptops, set in green hills under a lavender sky." fetchpriority="high">
  </picture>
</section>

<section class="srcs" aria-labelledby="srcs-title">
  <p class="srcs-k" id="srcs-title">Resolved from the sources healthcare runs on</p>
  <div class="mq"><ul class="mq-row"><li>NPPES NPI Registry</li><li>CMS National Provider Directory</li><li>Medicare utilization by clinician</li><li>Medicare Part D prescribers</li><li>Medicare hospital inpatient and outpatient</li><li>Home health, hospice and SNF files</li><li>Care Compare ratings and affiliations</li><li>Provider of Services file</li><li>ACO participation</li><li>Hospital and SNF cost reports</li><li>Medicare Advantage enrollment</li><li>Open Payments</li><li>ONC certified health IT data</li><li>State licensing boards</li><li>Payer directories</li><li>Price transparency files</li><li>Practice websites</li><li>Health system job posts</li></ul><ul class="mq-row" aria-hidden="true"><li>NPPES NPI Registry</li><li>CMS National Provider Directory</li><li>Medicare utilization by clinician</li><li>Medicare Part D prescribers</li><li>Medicare hospital inpatient and outpatient</li><li>Home health, hospice and SNF files</li><li>Care Compare ratings and affiliations</li><li>Provider of Services file</li><li>ACO participation</li><li>Hospital and SNF cost reports</li><li>Medicare Advantage enrollment</li><li>Open Payments</li><li>ONC certified health IT data</li><li>State licensing boards</li><li>Payer directories</li><li>Price transparency files</li><li>Practice websites</li><li>Health system job posts</li></ul></div>
</section>

<section class="h2-panel" id="team-day" aria-labelledby="day-title">
  <span id="how" class="anchor" aria-hidden="true"></span>
  <div class="h2-panel-in">
    <div class="h2-day">
      <p class="eyebrow"><span>How it works</span></p>
      <h2 id="day-title">Connect once. Ask in plain words. <span class="pop">Hear when it changes.</span></h2>
      <p class="td-lede">Your agent gets Stethos as a set of tools. It decides when to search, enrich or watch, and every answer comes back with its sources.</p>
      <ol class="td-steps" role="tablist" aria-label="Search, enrich, watch">
        <li role="presentation"><button type="button" role="tab" id="td-s1" aria-controls="td-r1" aria-selected="true" data-i="0"><span class="td-n">1</span><span class="td-t"><b>Connect: paste one URL</b><span>Add the Stethos MCP server to Claude, Cursor or your own agent. Sign in, and the tools show up.</span></span></button></li>
        <li role="presentation"><button type="button" role="tab" id="td-s2" aria-controls="td-r2" aria-selected="false" data-i="1"><span class="td-n">2</span><span class="td-t"><b>Ask: the agent picks the tool</b><span>"Find independent orthopedic surgeons in Arizona" becomes a search_providers call, then enrich_provider on the ones that fit.</span></span></button></li>
        <li role="presentation"><button type="button" role="tab" id="td-s3" aria-controls="td-r3" aria-selected="false" data-i="2"><span class="td-n">3</span><span class="td-t"><b>Watch: changes come to you</b><span>watch_providers follows the people you care about and tells your agent when someone moves, gets licensed or joins a network.</span></span></button></li>
      </ol>
      <p class="td-cta"><a class="h2-btn w" href="#connect">Connect in 5 minutes {ARROW}</a><span>1,000 free credits · no sales call</span></p>
    </div>
    <div class="hq td-card" id="td-card" aria-label="Example of three Stethos tool calls">
      <div class="hq-top"><span class="hq-t">Stethos in Claude <span class="td-time">Mon 7:30 AM</span></span><span class="hq-live"><i></i>Sample data</span></div>
      <div class="hq-row td-row on" id="td-r1" role="tabpanel" aria-labelledby="td-s1" data-r="1"><span class="td-num" aria-hidden="true">1</span><img class="hq-ic" src="/img/g-cl-stk-search-160.webp" width="160" height="160" alt=""><div class="hq-txt"><span class="hq-k">Search · Ortho surgeons, AZ</span><b><span class="td-count" data-from="0" data-to="412">412</span> independent matches</b><span class="hq-d">0.05 credits per result · sources on every match</span></div><span class="hq-chip td-chip1">search_providers</span></div>
      <div class="td-link" aria-hidden="true"><i></i></div>
      <div class="hq-row td-row" id="td-r2" role="tabpanel" aria-labelledby="td-s2" data-r="2"><span class="td-num" aria-hidden="true">2</span><img class="hq-ic" src="/img/g-cl-stk-enrich-160.webp" width="160" height="160" alt=""><div class="hq-txt"><span class="hq-k">Enrich · Dr. Jane Example</span><b>Licensed in AZ and NV, 2 affiliations</b><span class="hq-d">Practice phone added · verified today</span></div><span class="hq-chip btn td-send" data-done="Enriched ✓" data-idle="enrich_provider">enrich_provider</span></div>
      <div class="td-link" aria-hidden="true"><i></i></div>
      <div class="hq-row td-row" id="td-r3" role="tabpanel" aria-labelledby="td-s3" data-r="3"><span class="td-num" aria-hidden="true">3</span><img class="hq-ic" src="/img/g-cl-stk-watch-160.webp" width="160" height="160" alt=""><div class="hq-txt"><span class="hq-k">Watch · Affiliation changed</span><b>Joined Northfield Spine Partners</b><span class="hq-d">Your agent was told <span class="td-count" data-from="0" data-to="4">4</span> min after the change was seen</span></div><span class="hq-chip up">Agent alerted</span></div>
    </div>
    <p class="td-cta td-cta-m"><a class="h2-btn w" href="#connect">Connect in 5 minutes {ARROW}</a><span>1,000 free credits · no sales call</span></p>
  </div>
</section>

<section class="sec df" id="difference" aria-labelledby="familiar-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>Data is the difference</span></p>
      <h2 id="familiar-title">Your agent is only as good <span class="pop">as the record it reads.</span></h2>
      <p class="kpi-lede">Agents now do the prospecting, sourcing and diligence. The same provider, two ways: what a registry lookup hands your agent, and what Stethos does.</p>
    </div>
    <div class="df-tabs" role="tablist" aria-label="Sample providers"><button type="button" role="tab" id="df-t-maya" aria-controls="df-p-maya" aria-selected="true" tabindex="0"><b>Dr. Maya Example</b><span>Orthopedic surgeon · Phoenix, AZ</span></button><button type="button" role="tab" id="df-t-jordan" aria-controls="df-p-jordan" aria-selected="false" tabindex="-1"><b>Jordan Example, NP</b><span>Family nurse practitioner · Denver, CO</span></button><button type="button" role="tab" id="df-t-org" aria-controls="df-p-org" aria-selected="false" tabindex="-1"><b>Northfield Spine Partners</b><span>Orthopedic and spine group · Arizona</span></button></div>
    <div class="df-panels">
      <div class="df-panel" id="df-p-maya" role="tabpanel" aria-labelledby="df-t-maya">
        <div class="df-card df-without"><p class="df-h">Without Stethos <span>NPI Registry lookup</span></p><p class="df-name">Dr. Maya Example</p><ul class="df-raw"><li><span>NPI</span><b>1234567890</b></li><li><span>Taxonomy</span><b>Orthopaedic Surgery</b></li><li><span>Practice address</span><b>4410 N 7th St, Phoenix (on file since 2019)</b></li><li><span>Phone</span><b>(602) 555-0100</b></li></ul><p class="df-end">That's the whole record. No sign of what changed.</p></div>
        <div class="df-card df-with"><p class="df-h">With Stethos <span class="tag">Sample data</span></p><p class="df-name">Dr. Maya Example</p><ul class="df-rich"><li class="df-sig new" style="--i:0"><span class="df-k">Current group</span><b>Northfield Spine Partners</b><span class="df-meta"><em>moved 3 weeks ago</em><span>Source: Practice website</span></span></li><li class="df-sig " style="--i:1"><span class="df-k">Licenses</span><b>AZ active to 2027 · NV active to 2026</b><span class="df-meta"><em>2 states</em><span>Source: State boards</span></span></li><li class="df-sig " style="--i:2"><span class="df-k">Hospital affiliations</span><b>Example Regional Medical Center, Desert Valley Surgical</b><span class="df-meta"><em>2 hospitals</em><span>Source: CMS files</span></span></li><li class="df-sig " style="--i:3"><span class="df-k">Payer networks</span><b>In 7 of 9 major plans in AZ</b><span class="df-meta"><em>checked this week</em><span>Source: Payer directories</span></span></li><li class="df-sig " style="--i:4"><span class="df-k">Contact</span><b>Practice line verified 2 days ago</b><span class="df-meta"><em>direct</em><span>Source: Practice website</span></span></li><li class="df-sig sig" style="--i:5"><span class="df-k">Signal</span><b>Group posted 3 new surgical roles</b><span class="df-meta"><em>hiring</em><span>Source: Job posts</span></span></li></ul></div>
      </div><div class="df-panel" id="df-p-jordan" role="tabpanel" aria-labelledby="df-t-jordan" hidden>
        <div class="df-card df-without"><p class="df-h">Without Stethos <span>NPI Registry lookup</span></p><p class="df-name">Jordan Example, NP</p><ul class="df-raw"><li><span>NPI</span><b>1234567891</b></li><li><span>Taxonomy</span><b>Nurse Practitioner, Family</b></li><li><span>Practice address</span><b>Mailing address only</b></li><li><span>Phone</span><b>Not listed</b></li></ul><p class="df-end">That's the whole record. No sign of what changed.</p></div>
        <div class="df-card df-with"><p class="df-h">With Stethos <span class="tag">Sample data</span></p><p class="df-name">Jordan Example, NP</p><ul class="df-rich"><li class="df-sig new" style="--i:0"><span class="df-k">Current location</span><b>Example Primary Care, Lakewood clinic</b><span class="df-meta"><em>since August</em><span>Source: Practice website</span></span></li><li class="df-sig " style="--i:1"><span class="df-k">Licenses</span><b>CO active · compact privilege in 3 states</b><span class="df-meta"><em>multistate</em><span>Source: State boards</span></span></li><li class="df-sig " style="--i:2"><span class="df-k">Organization</span><b>Example Primary Care, 14 sites, 120 clinicians</b><span class="df-meta"><em>parent: Example Health</em><span>Source: CMS files</span></span></li><li class="df-sig " style="--i:3"><span class="df-k">Payer networks</span><b>Medicare, Medicaid and 5 commercial plans</b><span class="df-meta"><em>checked this week</em><span>Source: Payer directories</span></span></li><li class="df-sig " style="--i:4"><span class="df-k">Accepting patients</span><b>Yes, new patients this month</b><span class="df-meta"><em>current</em><span>Source: Practice website</span></span></li><li class="df-sig sig" style="--i:5"><span class="df-k">Signal</span><b>License issued in Utah last week</b><span class="df-meta"><em>license.issued</em><span>Source: State boards</span></span></li></ul></div>
      </div><div class="df-panel" id="df-p-org" role="tabpanel" aria-labelledby="df-t-org" hidden>
        <div class="df-card df-without"><p class="df-h">Without Stethos <span>NPI Registry lookup</span></p><p class="df-name">Northfield Spine Partners</p><ul class="df-raw"><li><span>NPI</span><b>1234567892 (organization)</b></li><li><span>Taxonomy</span><b>Multi-Specialty Group</b></li><li><span>Practice address</span><b>One location listed</b></li><li><span>Authorized official</span><b>Listed by name only</b></li></ul><p class="df-end">That's the whole record. No sign of what changed.</p></div>
        <div class="df-card df-with"><p class="df-h">With Stethos <span class="tag">Sample data</span></p><p class="df-name">Northfield Spine Partners</p><ul class="df-rich"><li class="df-sig new" style="--i:0"><span class="df-k">Locations</span><b>4 clinics and 1 surgery center</b><span class="df-meta"><em>1 opened in October</em><span>Source: Practice website</span></span></li><li class="df-sig " style="--i:1"><span class="df-k">Rostered clinicians</span><b>23 surgeons, 11 advanced practitioners</b><span class="df-meta"><em>+2 this quarter</em><span>Source: CMS files</span></span></li><li class="df-sig " style="--i:2"><span class="df-k">Leadership</span><b>CEO, CMO and practice administrator</b><span class="df-meta"><em>named</em><span>Source: Practice website</span></span></li><li class="df-sig " style="--i:3"><span class="df-k">Ownership</span><b>Independent, no parent health system</b><span class="df-meta"><em>verified</em><span>Source: CMS files</span></span></li><li class="df-sig " style="--i:4"><span class="df-k">Industry payments</span><b>Received from 6 device makers last year</b><span class="df-meta"><em>Open Payments</em><span>Source: Open Payments</span></span></li><li class="df-sig sig" style="--i:5"><span class="df-k">Signal</span><b>Hiring spike: 8 clinical roles posted</b><span class="df-meta"><em>org.hiring_spike</em><span>Source: Job posts</span></span></li></ul></div>
      </div>
    </div>
  </div>
</section>

<section class="sec stack" id="platform" aria-labelledby="platform-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>The platform</span></p>
      <h2 id="platform-title">One clean record for every provider, <span class="pop">and every change to it.</span></h2>
    </div>
    <ul class="stats">
      <li><b><span class="cnt" data-to="51">51</span></b><span>licensing boards in scope: every state plus DC</span></li>
      <li><b><span class="cnt" data-to="18">18</span></b><span>government, payer and web sources, 12 of them from CMS, resolved into one record</span></li>
      <li><b><span class="cnt" data-to="5">5</span></b><span>tools your agent gets: search, enrich, orgs, watch, changes</span></li>
      <li><b><span class="cnt" data-to="100">100</span>%</b><span>of fields carry a source and the date it was checked</span></li>
    </ul>
    <ul class="stk-row">
{stk(0, "stk-market", "Search", "Built to search every clinician and organization in the US", "by specialty, place, license, affiliation or network.", "Wide, cheap queries so your agent can look at everyone before it picks anyone.", "stk-search")}
{stk(1, "stk-understand", "Enrich", "Built to turn an NPI into a full record", "with licenses, affiliations, networks and contacts.", "Additive pricing: the base record first, then only the extra fields you ask for.", "stk-enrich")}
{stk(2, "stk-plan", "Organizations", "Built to map health systems, groups and clinics", "and who works at each one.", "Locations, rostered clinicians, leadership, open roles and parent–child ownership.", "stk-orgs")}
{stk(3, "stk-reconnect", "Watch", "Built to tell your agent when a record changes,", "so it moves first.", "Affiliation changes, new licenses, network moves, executive hires and hiring spikes.", "stk-watch")}
{stk(4, "stk-grow", "MCP first", "Built to plug straight into your agents", "as an MCP server, in five minutes.", "REST and webhooks are there too, for the parts of your stack that aren't agents.", "stk-agents")}
</ul>
    <p class="sp-more">Explore: <a href="/healthcare-mcp-server">Healthcare MCP server</a> · <a href="/npi-lookup-api">NPI lookup API</a> · <a href="/physician-data-api">Physician data API</a> · <a href="/license-verification-api">License data API</a> · <a href="/health-system-data-api">Health system data API</a> · <a href="/medicare-utilization-data-api">Medicare utilization data</a> · <a href="/home-health-hospice-data-api">Home health and hospice data</a> · <a href="/physician-referral-data">Physician referral data</a></p>
  </div>
</section>

<section class="sec plugs" id="integrations" aria-labelledby="plug-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>Works where you work</span></p>
      <h2 id="plug-title">No new dashboard. <span class="pop">It plugs into what you use today.</span></h2>
      <p class="kpi-lede">Stethos isn't another tool to log into. Your team asks for healthcare data in the AI assistant they already use, and the answers land in the CRM they already live in, with sources attached.</p>
    </div>
    <div class="plug-grid">
      <div class="plug-card">
        <p class="plug-k">AI assistants and agents</p>
        <h3>Ask in plain words</h3>
        <ul class="plug-chips"><li>Claude</li><li>ChatGPT</li><li>Microsoft Copilot Studio</li><li>Cursor</li><li>Your own agent</li></ul>
        <p>Add Stethos as an MCP server and its tools show up in the assistant. Search, enrich, map organizations and watch for changes without leaving the chat.</p>
      </div>
      <div class="plug-flow" aria-hidden="true"><span></span><i>→</i><span></span></div>
      <div class="plug-card">
        <p class="plug-k">CRMs and systems of record</p>
        <h3>Records stay current</h3>
        <ul class="plug-chips"><li>Salesforce</li><li>HubSpot</li><li>Attio</li><li>Lightfield</li><li>Your data warehouse</li></ul>
        <p>Enrich accounts and contacts through the API, and let webhooks update the record and alert its owner when a provider moves, a license lapses or a network changes.</p>
      </div>
    </div>
    <p class="plug-ex"><b>Example:</b> a rep asks Claude for independent spine surgeons in Arizona. Stethos returns them with sources, the agent creates the contacts in Salesforce, and when one changes groups next month the record updates and the rep gets a task. <a href="/examples">See nine more examples</a>.</p>
  </div>
</section>

<section class="sec" id="connect" aria-labelledby="connect-title">
  <div class="wrap connect-grid">
    <div>
      <p class="eyebrow"><span>Live in five minutes</span></p>
      <h2 id="connect-title">Add Stethos to your agent. <span class="pop">No sales call.</span></h2>
      <ol class="connect-steps">
        <li><b>Copy the server URL</b><span>One endpoint for every tool: <code>{MCP_URL}</code></span></li>
        <li><b>Add it to your client</b><span>In Claude, add it as a custom connector. In Cursor or your own agent, add it to your MCP config.</span></li>
        <li><b>Sign in and ask</b><span>Your account starts with 1,000 free credits. Every tool result shows the credits it used.</span></li>
      </ol>
      <p class="connect-more"><a href="/docs#connect">Step-by-step setup for each client <span aria-hidden="true">→</span></a></p>
    </div>
    <div class="card connect-card">
      <div class="card-top"><span>MCP config</span><button class="copy-mcp connect-copy" type="button" data-copy='{{"mcpServers": {{"stethos": {{"url": "{MCP_URL}"}}}}}}'>Copy</button></div>
<pre class="code" tabindex="0" aria-label="MCP client config">{{
  "mcpServers": {{
    "stethos": {{
      "url": "{MCP_URL}"
    }}
  }}
}}</pre>
      <p class="play-note">Tools: <code>search_providers</code> · <code>enrich_provider</code> · <code>enrich_org</code> · <code>watch_providers</code> · <code>recent_changes</code></p>
    </div>
  </div>
</section>

<section class="sec" id="playground" aria-labelledby="play-title">
  <div class="panel navy wrap-panel">
    <div class="head product-head">
      <div>
        <p class="eyebrow on-dark"><span>Try a tool call</span></p>
        <h2 id="play-title">Your agent asks, <span class="pop">Stethos answers with sources.</span></h2>
      </div>
      <div class="product-side"><div class="seg" role="group" aria-label="Pick a tool"><button type="button" data-ep="search" aria-pressed="true">search_providers</button><button type="button" data-ep="enrich" aria-pressed="false">enrich_provider</button><button type="button" data-ep="org" aria-pressed="false">enrich_org</button><button type="button" data-ep="watch" aria-pressed="false">watch_providers</button></div><p class="product-hint">Pick a tool to see what your agent sends and what comes back. <span class="tag">Sample data</span></p></div>
    </div>
    <div class="play-grid">
      <div class="card play-card">
        <div class="card-top"><span id="pl-label">Agent tool call</span><span id="pl-cost">0.05 credits per result</span></div>
        <p class="play-ask" id="pl-ask"></p>
        <pre class="code" id="pl-req" tabindex="0" aria-label="Tool call"></pre>
        <p class="play-note" id="pl-note"></p>
      </div>
      <div class="card play-card">
        <div class="card-top"><span>Tool result</span><span class="play-ok" id="pl-status">ok</span></div>
        <pre class="code" id="pl-res" tabindex="0" aria-label="Tool result" aria-live="polite"></pre>
      </div>
    </div>
  </div>
</section>

<section class="sec acct" id="sources" aria-labelledby="acct-title">
  <div class="wrap acct-grid">
    <div class="acct-copy">
      <p class="eyebrow"><span>Provenance</span></p>
      <h2 id="acct-title">Every field shows <span class="pop">where it came from.</span></h2>
      <p class="acct-lede">An agent that acts on healthcare data needs to know how far to trust it. Stethos is built to keep the source and the last-verified date on every single field, not just on the record.</p>
      <ul class="acct-pts">
        <li><h3>Public registries first</h3><p>NPPES, CMS utilization, post-acute and Care Compare files, Open Payments and state licensing boards are the backbone.</p></li>
        <li><h3>Licensed and web sources on top</h3><p>Payer directories, price transparency files, practice websites and health system job posts fill the gaps.</p></li>
        <li><h3>Conflicts kept, not hidden</h3><p>When two sources disagree, you see both and which one we picked, so your agent can decide.</p></li>
        <li><h3>NPI as the key</h3><p>Join cleanly to the claims, CRM and EHR data you already have.</p></li>
      </ul>
    </div>
    <figure class="acct-card" aria-label="Sample provider record with sources">
      <div class="acct-top"><span>Provider record</span><span class="tag">Sample data</span></div>
      <p class="acct-name">Dr. Jane Example, MD</p>
      <p class="acct-meta">NPI 1234567890 · Interventional cardiology</p>
      <dl class="src-list">
        <div><dt>Practice location</dt><dd>Example Heart Group, Phoenix AZ</dd><dd class="src">Practice website · verified today</dd></div>
        <div><dt>Licenses</dt><dd>AZ active · NV active</dd><dd class="src">State boards · verified 3 days ago</dd></div>
        <div><dt>Affiliations</dt><dd>Sample Regional Medical Center</dd><dd class="src">CMS provider data · verified 6 days ago</dd></div>
        <div><dt>Networks</dt><dd>[Payer A] · [Payer B]</dd><dd class="src">Payer directories · verified 2 days ago</dd></div>
        <div class="src-conflict"><dt>Phone</dt><dd>(555) 010-0199</dd><dd class="src">2 sources disagree · picked the practice website</dd></div>
      </dl>
      <p class="acct-goal">Last change: <b>affiliation added</b>, seen 4 days ago.</p>
    </figure>
  </div>
</section>

<section class="sec" id="kpis" aria-labelledby="kpi-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>Signals</span></p>
      <h2 id="kpi-title">The changes <span class="pop">worth acting on.</span></h2>
      <p class="kpi-lede">Most databases tell you what's true today. Stethos is built to record every change as an event, so you can ask what changed this week, or get told as it happens.</p>
    </div>
    <div class="feed" aria-label="Sample change feed">
      <div class="feed-top"><span class="hq-t">Change feed</span><span class="hq-live"><i></i>Sample data</span></div>
      <ol class="feed-list" id="feed-list" aria-live="off"></ol>
    </div>
    <ul class="kpis">
      <li style="--t:#e4f0fd"><b>Moves</b><h3>affiliation.changed</h3><p>A clinician joins or leaves a group, hospital or health system.</p></li>
      <li style="--t:#e8f3d2"><b>Licenses</b><h3>license.issued · license.lapsed</h3><p>A new state license, or one that expired or was restricted.</p></li>
      <li style="--t:#fbe3ee"><b>Networks</b><h3>network.joined · network.left</h3><p>A practice shows up in, or drops out of, a payer's directory.</p></li>
      <li style="--t:#f5efdf"><b>Locations</b><h3>location.opened</h3><p>A new clinic, practice site or service line comes online.</p></li>
      <li style="--t:#ece6fb"><b>Leaders</b><h3>org.exec_hire</h3><p>A health system names a new CMO, CNO, CFO or service line head.</p></li>
      <li style="--t:#e4f0fd"><b>Hiring</b><h3>org.hiring_spike</h3><p>An organization posts far more clinical roles than usual.</p></li>
    </ul>
  </div>
</section>

<section class="sec" id="teams" aria-labelledby="teams-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>Who it's for</span></p>
      <h2 id="teams-title">Built for teams <span class="pop">selling into, and investing in, healthcare.</span></h2>
    </div>
    <ul class="roles">
      <li><figure class="role-art" style="--bg:#d3e6fb">{art("uc-medtech", "Illustration: a clay sales desk with a surgical instrument case, a knee model and a laptop showing a map with pins.")}</figure><h3><a class="role-link" href="/use-cases/medtech-pharma">Medtech and pharma</a></h3><p>Find the surgeons and groups that fit your product, and reach out the week a target changes affiliation or opens a new site.</p></li>
      <li><figure class="role-art" style="--bg:#f6efe2">{art("compare", "Illustration: clay stacks of boxes and binders on a table beside a small machine sending out envelopes and pins.")}</figure><h3><a class="role-link" href="/use-cases/health-it-sales">Health IT and services sales</a></h3><p>Target health systems by EHR, size and service line, and hear the week a new CIO or CMO starts.</p></li>
      <li><figure class="role-art" style="--bg:#0b1b33">{art("cta", "Illustration: a clay shelf of hospitals, clinics and houses with glowing map pins above them, and a small robot.")}</figure><h3><a class="role-link" href="/use-cases/healthcare-marketing">Healthcare marketing</a></h3><p>Build clinician audiences and ABM account lists, and keep them clean as people change jobs.</p></li>
      <li><figure class="role-art" style="--bg:#e3dcf7">{art("uc-investors", "Illustration: a clay piggy bank beside a rising bar chart topped with small clinic buildings.")}</figure><h3><a class="role-link" href="/use-cases/investors">Investors and deal teams</a></h3><p>Map a market in an afternoon: every group, its clinicians, owners and volume, and who just added sites.</p></li>
      <li><figure class="role-art" style="--bg:#f5e9b8">{art("uc-digital", "Illustration: a clay phone showing a map with pins, beside a small friendly robot.")}</figure><h3><a class="role-link" href="/use-cases/digital-health">Healthcare startups</a></h3><p>Find first customers and design partners, size your market, and power provider search in your product.</p></li>
      <li><figure class="role-art" style="--bg:#f5efdf">{art("uc-staffing", "Illustration: clay scrubs on a hanger rack, a stethoscope, a calendar and a small state map with glowing pins.")}</figure><h3><a class="role-link" href="/use-cases/clinical-staffing">Clinical staffing</a></h3><p>Find the systems hiring hardest and the licensed clinicians to place there.</p></li>
    </ul>
    <p class="sp-more"><a href="/use-cases">All use cases <span aria-hidden="true">→</span></a> · <a href="/examples">Example workflows <span aria-hidden="true">→</span></a></p>
  </div>
</section>

<section class="sec" aria-labelledby="yours-title">
  <div class="panel plain wrap-panel yours-grid">
    <figure class="art-wide yours-art">{art("compare", "Illustration: a dusty stack of sealed boxes and reports on one side, and the clay data machine sending out a stream of alerts on the other.", w=1600, h=893)}</figure>
    <div>
      <p class="eyebrow"><span>Why Stethos</span></p>
      <h2 id="yours-title">Snapshots, raw files or guesses. <span class="pop">Or a record you can trust.</span></h2>
      <p class="yours-lede">Agents now do the prospecting, sourcing and diligence, and they act on whatever data they are given. Today that means an annual-contract platform built for analysts, free government files that are raw and inconsistently dated, or a general AI assistant answering from old pages. Stethos is the layer in between: current, sourced records your agent can call, priced per call.</p>
      <p class="cmp-links"><a href="/compare/definitive-healthcare">Stethos vs Definitive Healthcare <span aria-hidden="true">→</span></a><a href="/compare/iqvia-onekey">Stethos vs IQVIA OneKey <span aria-hidden="true">→</span></a></p>
    </div>
    <div class="compare">
      <div class="col them">
        <h3>Traditional data platforms</h3><p class="col-k">Definitive, IQVIA</p>
        <ul><li>Annual contracts, sold by sales</li><li>Priced per seat or module</li><li>Dashboards first, API often extra</li><li>Periodic refreshes and exports</li><li>You find out what changed later</li><li>Built for analysts</li></ul>
      </div>
      <div class="col them">
        <h3>Free government files</h3>
        <ul><li>NPPES, CMS's provider directory, Medicare files</li><li>Free and comprehensive</li><li>Raw, in dozens of formats</li><li>No reliable per-record freshness date</li><li>Not matched across sources</li><li>You build and maintain the pipeline</li></ul>
      </div>
      <div class="col them ai">
        <h3>General AI assistants</h3>
        <ul><li>Answer from whatever page they find</li><li>Sources often months or years old</li><li>No source or date on the answer</li><li>Can't tell you when something changes</li><li>Answers vary from one ask to the next</li><li>Fine for a rough first look</li></ul>
      </div>
      <div class="col us">
        <h3>Stethos: built for agents</h3>
        <ul><li>One matched record per provider and organization</li><li>A source and checked date on every field</li><li>Verified by agents when sources disagree</li><li>Changes pushed to your agent</li><li>Plugs into your CRM and AI assistant</li><li>Live in five minutes, priced per call</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="sec why-now" aria-labelledby="now-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>Why now</span></p>
      <h2 id="now-title">Agents became the buyer. <span class="pop">The data didn't keep up.</span></h2>
    </div>
    <ol class="now-list">
      <li><b>Agents call tools now</b><p>MCP turned data into something an agent calls on its own. Incumbent platforms were built for analysts clicking through dashboards.</p></li>
      <li><b>Free data got bigger, not fresher</b><p>CMS's new provider directory, EHR data from ONC and Medicare Advantage plan directories are large and free, but they don't tell you how current each record is.</p></li>
      <li><b>Verification got cheap</b><p>Voice and web agents can do the research calls data vendors have staffed for years, at a fraction of the cost, whenever a record looks stale.</p></li>
    </ol>
  </div>
</section>

<section class="sec pillars-sec" aria-labelledby="pill-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>What you get</span></p>
      <h2 id="pill-title">Data your agent <span class="pop">can act on.</span></h2>
    </div>
    <ul class="pillars">
      <li style="--t:#e4f0fd"><img src="/img/g-cl-stk-watch-160.webp" width="160" height="160" alt="" loading="lazy" decoding="async"><h3>Fresh</h3><p>Sources are re-checked continuously, and Stethos agents call practices and check websites to confirm what files can't. Changes arrive as events, not quarterly exports.</p></li>
      <li style="--t:#e8f3d2"><img src="/img/g-cl-tr-read-cut.webp" width="160" height="160" alt="" loading="lazy" decoding="async"><h3>Trustworthy</h3><p>Every field shows where it came from and when it was last checked, matched to the right person or practice. Consistent answers, not a confident guess.</p></li>
      <li style="--t:#f5efdf"><img src="/img/g-cl-stk-agents-160.webp" width="160" height="160" alt="" loading="lazy" decoding="async"><h3>Built for agents</h3><p>Plugs into the AI assistants and CRM you already use: MCP for agents, REST and webhooks for everything else. Self-serve and priced per call.</p></li>
    </ul>
    <ul class="trust-line"><li>No patient data: no PHI, no BAA</li><li>A source and a checked date on every field</li><li>Government registries first, licensed sources on top</li></ul>
  </div>
</section>

<section class="sec home-price" id="pricing" aria-labelledby="hp-title">
  <div class="wrap">
    <div class="head center"><p class="eyebrow"><span>Pricing</span></p><h2 id="hp-title">Pay per tool call. <span class="pop">No seats, no sales call.</span></h2><p class="hp-lede">Every account starts with 1,000 free credits. Credits are only used when a tool returns data.</p></div>
    <ul class="hp-grid">
      <li class="hp-card"><h3>Free</h3><p class="hp-amt">$0</p><p>1,000 credits to try every tool on your own use case. No card, no sales call.</p></li>
      <li class="hp-card pop"><span class="hp-badge">Most popular</span><h3>Build</h3><p class="hp-amt">$149<span>/mo</span></p><p>20,000 credits a month for your agents, plus watchers and webhooks. Top up any time.</p></li>
      <li class="hp-card"><h3>Enterprise</h3><p class="hp-amt">Custom</p><p>Volume pricing, flat files delivered to your warehouse, SLAs and a data agreement.</p></li>
    </ul>
    <div class="hp-ctas"><a class="h2-btn y" href="/pricing">See the cost of each tool {ARROW}</a><a class="h2-btn w hp-trial" href="{TRIAL}">Start free trial {ARROW}</a></div>
    <p class="hp-fine">Annual billing includes 2 months free. Unused monthly credits roll over for one month.</p>
  </div>
</section>

<section class="sec" id="faq" aria-labelledby="faq-title">
  <div class="wrap faq-grid">
    <div class="head">
      <p class="eyebrow"><span>FAQ</span></p>
      <h2 id="faq-title">Common questions</h2>
      <figure class="faq-art">{art("notfound", "Illustration: a teal clay map pin beside a magnifying glass at the end of a dotted path.", w=1600, h=1195)}</figure>
      <p class="faq-more">Still curious? <a href="mailto:{EMAIL}?subject=Stethos%20question">Ask our team</a> or read the <a href="/docs">docs</a>.</p>
    </div>
    <div class="qs">
{faq}
    </div>
  </div>
</section>

<section class="sec home-blog" id="home-blog" aria-labelledby="hb-title">
  <div class="wrap">
    <div class="head center"><p class="eyebrow"><span>From the blog</span></p><h2 id="hb-title">Guides for teams <span class="pop">building on provider data.</span></h2></div>
    <ul class="blog-grid">{{BLOG_CARDS}}</ul>
    <p class="sp-more"><a href="/blog">Read all guides <span aria-hidden="true">→</span></a></p>
  </div>
</section>

<section class="sec" id="waitlist" aria-labelledby="join-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>Get started</span></p>
      <h2 id="join-title">Give your agent <span class="pop">the healthcare map.</span></h2>
    </div>
    <div class="split">
      <div class="split-card biz">
        <p class="split-k">For business leaders</p>
        <h3>See it on your own accounts.</h3>
        <p>Send us the providers or health systems you care about, and we'll show you what Stethos returns for them, side by side with what you have today.</p>
        <ul class="perks dark"><li>Your own list, not a canned demo</li><li>Sources and checked dates on every field</li><li>Volume pricing and data agreements available</li></ul>
        <a class="split-btn light" href="mailto:{EMAIL}?subject=Stethos%20on%20our%20accounts">Talk to our team {ARROW}</a>
      </div>
      <div class="split-card dev">
        <p class="split-k">For developers</p>
        <h3>Ship an agent tonight.</h3>
        <p>Paste one URL into Claude, Cursor or your MCP client and start calling tools. Pay only for the calls you make.</p>
        <ul class="perks"><li>1,000 free credits, no card</li><li>MCP server, REST API and webhooks</li><li>Live in five minutes, no sales call</li></ul>
        <div class="split-ctas"><a class="split-btn" href="{TRIAL}">Start free trial {ARROW}</a><a class="split-alt" href="/docs">Read the docs</a></div>
      </div>
    </div>
  </div>
</section>
</main>
'''
    return h + body + tail(("nav", "teamday", "play", "copy", "motion"))
