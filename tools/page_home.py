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
    ("What is Stethos?", "An MCP server, and API, for US healthcare provider data. It's built to keep one clean, current record for every clinician, practice, hospital and health system, stitched together from public registries and licensed sources, and to tell your software the moment one of those records changes."),
    ("Who is it for?", "Teams building products on top of healthcare provider data: AI sales agents for medtech and pharma, provider directory and network teams at payers and digital front doors, clinical staffing and recruiting platforms, healthcare investors, and digital health apps that need to know who practices where."),
    ("Where does the data come from?", "Public sources like the NPPES NPI Registry, CMS provider and facility files, Open Payments and state licensing boards, plus payer directories, price transparency files, practice websites and health system job posts. Every field carries its source and the date it was last checked."),
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
    h = head("Stethos: Healthcare Provider Data MCP Server for AI Agents",
             "An MCP server for every US healthcare provider and organization. Add it to Claude or any MCP client in five minutes and pay per tool call. Free credits.",
             "/", css=("styles", "v2", "site", "home"), extra=pre,
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
    <h1 id="hero-title">Healthcare data for your&nbsp;AI&nbsp;agents</h1>
    <p class="cx-sub">An MCP server for every US clinician, practice and health system, kept current. Live in five minutes, priced per tool call, with a source on every answer.</p>
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

<section class="sec" aria-labelledby="familiar-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>The problem</span></p>
      <h2 id="familiar-title">Healthcare data goes stale <span class="pop">the day you buy it.</span></h2>
    </div>
    <figure class="art-wide">{art("problem", "Illustration: a dusty clay filing cabinet, faded binders, a curling spreadsheet, returned envelopes and a map whose pins have fallen over.", w=1600, h=893)}</figure>
    <ul class="pains">
      <li><img src="/img/g-cl-ic-binder-cut.webp" width="160" height="160" alt="" loading="lazy" decoding="async"><p>Provider databases refresh on a schedule. Clinicians change groups, locations and networks all year.</p></li>
      <li><img src="/img/g-cl-ic-gov-cut.webp" width="160" height="160" alt="" loading="lazy" decoding="async"><p>The best data is public, but it's scattered across NPPES, CMS files, state boards and payer directories, each with its own format.</p></li>
      <li><img src="/img/g-cl-ic-license-cut.webp" width="160" height="160" alt="" loading="lazy" decoding="async"><p>Licenses are issued and lapse state by state, on dozens of separate board websites.</p></li>
      <li><img src="/img/g-cl-ic-payer-cut.webp" width="160" height="160" alt="" loading="lazy" decoding="async"><p>Payer directories disagree with each other, and with where the doctor actually practices.</p></li>
      <li><img src="/img/g-cl-envelope-cut.webp" width="160" height="160" alt="" loading="lazy" decoding="async"><p>Your agent writes to a surgeon who left that group last spring, and nobody finds out until the email bounces.</p></li>
    </ul>
  </div>
</section>

<section class="sec stack" id="platform" aria-labelledby="platform-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>The platform</span></p>
      <h2 id="platform-title">One clean record for every provider, <span class="pop">and every change to it.</span></h2>
    </div>
    <ul class="stk-row">
{stk(0, "stk-market", "Search", "Built to search every clinician and organization in the US", "by specialty, place, license, affiliation or network.", "Wide, cheap queries so your agent can look at everyone before it picks anyone.", "stk-search")}
{stk(1, "stk-understand", "Enrich", "Built to turn an NPI into a full record", "with licenses, affiliations, networks and contacts.", "Additive pricing: the base record first, then only the extra fields you ask for.", "stk-enrich")}
{stk(2, "stk-plan", "Organizations", "Built to map health systems, groups and clinics", "and who works at each one.", "Locations, rostered clinicians, leadership, open roles and parent–child ownership.", "stk-orgs")}
{stk(3, "stk-reconnect", "Watch", "Built to tell your agent when a record changes,", "so it moves first.", "Affiliation changes, new licenses, network moves, executive hires and hiring spikes.", "stk-watch")}
{stk(4, "stk-grow", "MCP first", "Built to plug straight into your agents", "as an MCP server, in five minutes.", "REST and webhooks are there too, for the parts of your stack that aren't agents.", "stk-agents")}
</ul>
    <p class="sp-more">Explore: <a href="/healthcare-mcp-server">Healthcare MCP server</a> · <a href="/npi-lookup-api">NPI lookup API</a> · <a href="/physician-data-api">Physician data API</a> · <a href="/license-verification-api">License data API</a> · <a href="/health-system-data-api">Health system data API</a></p>
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
        <li><h3>Public registries first</h3><p>NPPES, CMS provider and facility files, Open Payments and state licensing boards are the backbone.</p></li>
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
    <ul class="kpis">
      <li style="--t:#e4f0fd"><b>Moves</b><h3>affiliation.changed</h3><p>A clinician joins or leaves a group, hospital or health system.</p></li>
      <li style="--t:#e8f3d2"><b>Licenses</b><h3>license.issued · license.lapsed</h3><p>A new state license, or one that expired or was restricted.</p></li>
      <li style="--t:#fbe3ee"><b>Networks</b><h3>network.joined · network.left</h3><p>A practice shows up in, or drops out of, a payer's directory.</p></li>
      <li style="--t:#fde7d6"><b>Locations</b><h3>location.opened</h3><p>A new clinic, practice site or service line comes online.</p></li>
      <li style="--t:#ece6fb"><b>Leaders</b><h3>org.exec_hire</h3><p>A health system names a new CMO, CNO, CFO or service line head.</p></li>
      <li style="--t:#e4f0fd"><b>Hiring</b><h3>org.hiring_spike</h3><p>An organization posts far more clinical roles than usual.</p></li>
    </ul>
  </div>
</section>

<section class="sec" id="teams" aria-labelledby="teams-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>Who it's for</span></p>
      <h2 id="teams-title">Built for teams <span class="pop">building on healthcare.</span></h2>
    </div>
    <ul class="roles">
      <li><figure class="role-art" style="--bg:#d3e6fb">{art("uc-medtech", "Illustration: a clay sales desk with a surgical instrument case, a knee model and a laptop showing a map with pins.")}</figure><h3><a class="role-link" href="/use-cases/medtech-pharma">AI sales agents for medtech and pharma</a></h3><p>Find the surgeons and groups that fit, and reach out the week a target changes affiliation or opens a new site.</p></li>
      <li><figure class="role-art" style="--bg:#e3f1e7">{art("uc-payer", "Illustration: a clay clipboard directory of doctors' offices with check marks, beside an insurance shield and a magnifying glass.")}</figure><h3><a class="role-link" href="/use-cases/provider-directories">Provider directory and network teams</a></h3><p>Flag stale locations, lapsed licenses and network mismatches before a member calls a number that doesn't work.</p></li>
      <li><figure class="role-art" style="--bg:#fde7d6">{art("uc-staffing", "Illustration: clay scrubs on a hanger rack, a stethoscope, a calendar and a small state map with glowing pins.")}</figure><h3><a class="role-link" href="/use-cases/clinical-staffing">Clinical staffing and recruiting</a></h3><p>Source licensed clinicians by state and specialty, and spot the health systems that are hiring hardest.</p></li>
    </ul>
    <p class="sp-more"><a href="/use-cases/medtech-pharma">Medtech and pharma</a> · <a href="/use-cases/provider-directories">Provider directories</a> · <a href="/use-cases/clinical-staffing">Clinical staffing</a> · <a href="/use-cases">All use cases <span aria-hidden="true">→</span></a></p>
  </div>
</section>

<section class="sec" aria-labelledby="yours-title">
  <div class="panel plain wrap-panel yours-grid">
    <figure class="art-wide yours-art">{art("compare", "Illustration: a dusty stack of sealed boxes and reports on one side, and the clay data machine sending out a stream of alerts on the other.", w=1600, h=893)}</figure>
    <div>
      <p class="eyebrow"><span>Why Stethos</span></p>
      <h2 id="yours-title">Others sell snapshots. <span class="pop">Stethos streams changes.</span></h2>
      <p class="yours-lede">Established healthcare data vendors are deep and trusted, and they're built for big commercial teams: annual contracts, seats, dashboards and periodic exports. Stethos is built for software that acts: an MCP server you can add to your agent today, priced per tool call, with change events your agents can subscribe to.</p>
      <p class="cmp-links"><a href="/compare/definitive-healthcare">Stethos vs Definitive Healthcare <span aria-hidden="true">→</span></a><a href="/compare/iqvia-onekey">Stethos vs IQVIA OneKey <span aria-hidden="true">→</span></a></p>
    </div>
    <div class="compare">
      <div class="col them">
        <h3>Traditional data platforms</h3>
        <ul><li>Annual contracts, sold by sales</li><li>Priced per seat or module</li><li>Dashboards first, API often extra</li><li>Periodic refreshes and exports</li><li>You find out what changed later</li><li>Built for analysts</li></ul>
      </div>
      <div class="col us">
        <h3>Stethos: built for agents</h3>
        <ul><li>Add to Claude in five minutes</li><li>Priced per tool call</li><li>MCP first, REST and webhooks too</li><li>Sources re-checked continuously</li><li>Change events, as they happen</li><li>Built for developers and agents</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="sec trust-sec" aria-labelledby="trust-title">
  <div class="wrap">
    <h2 class="sr" id="trust-title">Built for healthcare data</h2>
    <ul class="trust has-ic">
      <li><img class="tr-ic" src="/img/g-cl-tr-shield-cut.webp" width="160" height="160" alt="" loading="lazy" decoding="async"><b>Provider data, not patient data</b><span>No PHI in the API, so there's no business associate agreement to sign before you start.</span></li>
      <li><img class="tr-ic" src="/img/g-cl-tr-read-cut.webp" width="160" height="160" alt="" loading="lazy" decoding="async"><b>Source on every field</b><span>Every value carries where it came from and when it was last checked.</span></li>
      <li><img class="tr-ic" src="/img/g-cl-ic-gov-cut.webp" width="160" height="160" alt="" loading="lazy" decoding="async"><b>Public and licensed sources</b><span>Built on government registries first, with licensed and web sources layered on top.</span></li>
    </ul>
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
  <div class="panel navy wrap-panel join-grid">
    <div class="join-copy">
      <p class="eyebrow on-dark"><span>Self-serve</span></p>
      <h2 id="join-title">Give your agent <span class="pop">the healthcare map.</span></h2>
      <p>Paste one URL into Claude or your MCP client, sign in, and ask. Pay only for the tool calls you make.</p>
      <ul class="perks"><li>1,000 free credits, no card</li><li>Live in five minutes, no sales call</li><li>Provider data only, no PHI</li></ul>
      <div class="join-ctas"><a class="btn-cta" href="{TRIAL}">Start free trial</a><a class="join-signin" href="{TRIAL}#signin">Already have an account? Sign in</a></div>
      <p class="join-alt">Questions first? <a href="mailto:{EMAIL}?subject=Stethos">Email our team</a></p>
    </div>
    <figure class="join-art">{art("cta", "Illustration: a shelf of small clay healthcare buildings, each with a glowing teal map pin, and a clay robot holding a laptop.")}</figure>
  </div>
</section>
</main>
'''
    return h + body + tail(("nav", "teamday", "play", "copy"))
