from parts import *
from segments import scene, seg_grid, seg_tabs, logo, ih_art
import json

# Landing pages aimed at specific searches. Each: slug, art, tint class, seo title, meta description,
# H1 (two parts), intro, two lists, example request, FAQs, related links.
SCENES = {'healthcare-mcp-server': 'w-s-mcp', 'npi-lookup-api': 'w-s-npi', 'physician-data-api': 'w-s-physician', 'license-verification-api': 'w-s-license', 'health-system-data-api': 'w-s-healthsys', 'medicare-utilization-data-api': 'w-s-medicare', 'home-health-hospice-data-api': 'w-s-homehealth', 'physician-referral-data': 'w-s-referral', 'private-equity-healthcare-ownership-data': 'w-s-pe'}
SCENE_ALTS = {'w-s-mcp': 'Illustration: a clay server box on a hill with cables running to little robots on clouds.', 'w-s-npi': 'Illustration: a meadow of clinician ID cards standing like signposts, and the robot with a big magnifying glass.', 'w-s-physician': "Illustration: a town of clinics with map pins, a doctor's coat on a signpost and the robot pointing the way.", 'w-s-license': 'Illustration: hills like a patchwork quilt of states with license scrolls planted on them.', 'w-s-healthsys': 'Illustration: a hospital campus on a hill with roads down to clinics, an urgent care and a surgery center.', 'w-s-medicare': 'Illustration: towers of stacked pill capsules beside a government building, with the robot measuring one.', 'w-s-homehealth': 'Illustration: a little car on a country road visiting houses with hearts on their roofs.', 'w-s-referral': 'Illustration: envelopes with hearts flying like birds between a hospital and clinics on the hills.', 'w-s-pe': 'Illustration: three hill regions whose clinics share flag colors, each linked to a matching briefcase-shaped building.'}

SEO_PAGES = [
    dict(slug="healthcare-mcp-server", art="s-mcp", color="sp-blue", name="Healthcare MCP server",
         title="Healthcare MCP Server for Provider Data | Stethos",
         desc="A self-serve MCP server for US healthcare provider data. Add it to Claude or Cursor in five minutes: search, enrich, organizations and change alerts.",
         h1a="A healthcare MCP server", h1b="your agents can use today.",
         intro="A remote MCP server for US healthcare provider data. Your agent can search clinicians and organizations, enrich any NPI, map health systems and watch for changes. Paste one URL, sign in and pay per tool call.",
         k1="Works with", l1=["Claude, as a custom connector", "Cursor and Claude Code", "Your own agent, via any MCP SDK", "REST and webhooks for everything else"],
         k2="Tools", l2=["search_providers", "enrich_provider", "enrich_org", "watch_providers", "recent_changes"],
         ep="providers/search", req={"specialty": "dermatology", "city": "Austin", "state": "TX", "limit": 10},
         faq=[("Why not just ask a general AI assistant?", "General assistants answer from whatever page they find, often out of date, with no source or date. Stethos returns current records with the source and last-checked date on every field, and alerts your agent when something changes."), ("How is this different from free NPI MCP servers?", "Free servers wrap the NPI registry. Stethos starts from the same NPI and adds state licenses, current affiliations, payer networks and organization data, with a source on every field and alerts when a record changes."),
              ("Do I need to talk to sales?", "No. It's self-serve: 1,000 free credits, no card, and plans and top-ups you can manage yourself."),
              ("Does it handle patient data?", "No. Stethos only holds data about clinicians and organizations, so there's no PHI and no business associate agreement needed."),
              ("What does it cost?", "Each tool call costs credits: a search result is 0.05, a provider record is 1 plus optional fields. Build is $149 a month for 20,000 credits.")],
         related=[("Docs: connect in five minutes", "/docs#connect"), ("NPI lookup API", "/npi-lookup-api"), ("Pricing", "/pricing")]),
    dict(slug="npi-lookup-api", art="s-npi", color="sp-lime", name="NPI lookup API",
         title="NPI Lookup API: Search and Enrich Any NPI | Stethos",
         desc="Look up any NPI and get more than the registry: licenses, affiliations, payer networks and practice contacts, each with a source and verified date.",
         h1a="An NPI lookup API that tells you", h1b="more than the registry.",
         intro="The NPI Registry tells you who an NPI belongs to. Stethos is built to return the rest from that same NPI: where the clinician practices now, active licenses, group and hospital affiliations, and payer networks.",
         k1="Look up by", l1=["NPI, Type 1 (individual) or Type 2 (organization)", "Name plus city and state", "Organization name or ID", "Batches of NPIs in one call"],
         k2="What comes back", l2=["Registry identity, taxonomy and addresses", "State licenses with status", "Current group and hospital affiliations", "Payer network listings and practice contacts", "A source and verified date on every field"],
         ep="providers/enrich", req={"npi": "1234567890", "fields": ["licenses", "affiliations", "networks"]},
         faq=[("Isn't there a free NPI registry API?", "Yes. CMS runs an NPI Registry API for NPPES data, and it's a good fit when you only need what providers reported to the registry. Stethos starts from the same NPI and adds licenses, affiliations, networks and change events from other sources."),
              ("Can I look up an NPI by name?", "Yes. Search by name with a city and state, or by specialty and location, then enrich the NPI you pick."),
              ("How current is the data?", "Every field carries its source and the date it was last verified, and watchers send a webhook when a record changes."),
              ("Does it cover organizations?", "Yes. Type 2 NPIs for hospitals, groups, pharmacies and agencies are supported, along with organization records that link locations and rostered clinicians.")],
         related=[("Docs: enrich a provider", "/docs#enrich"), ("What the NPI registry can and can't tell you", "/blog/what-the-npi-registry-can-and-cant-tell-you"), ("Physician data API", "/physician-data-api")]),
    dict(slug="physician-data-api", art="s-physician", color="sp-blue", name="Physician data API",
         title="Physician Data API for Sales and Product Teams | Stethos",
         desc="A physician data API with specialties, affiliations, state licenses and practice contacts for every US physician, plus webhooks when physicians move.",
         h1a="A physician data API that", h1b="keeps up with physicians.",
         intro="Physicians change groups, add locations, pick up licenses and join networks all year. Stethos is built to keep one current record per physician, keyed on the NPI, and to tell your product or sales agent when that record changes.",
         k1="Filter physicians by", l1=["Specialty and sub-specialty", "State, city or radius", "Hospital or group affiliation", "License state", "Payer network"],
         k2="Record includes", l2=["Practice locations and contact details", "Affiliations with start dates", "State licenses and status", "Open Payments summary", "Change history"],
         ep="providers/search", req={"specialty": "cardiology", "state": "TX", "affiliation_type": "independent_group", "limit": 25},
         faq=[("How many physicians does it cover?", "Stethos is built to cover every US physician with an NPI, from the NPPES registry, with other sources layered on top. Coverage of each field will be published at launch."),
              ("Can I get contact details?", "Practice contact details, such as phone, fax and practice address, are an optional field with their sources. Stethos does not sell personal home addresses or personal phone numbers."),
              ("Can I sync it to a CRM?", "Yes. Enrich records on demand and subscribe to watchers so your CRM is updated when a physician moves, instead of re-importing lists.")],
         related=[("Medtech sales", "/use-cases/medtech"), ("NPI lookup API", "/npi-lookup-api"), ("Pricing", "/pricing")]),
    dict(slug="license-verification-api", art="s-license", color="sp-butter", name="License data API",
         title="Medical License Lookup API by State | Stethos",
         desc="Check physician and nurse license status across states in one API call, and get a webhook when a license is issued, expires or is restricted.",
         h1a="Medical license lookups", h1b="across every state, in one call.",
         intro="Every state runs its own licensing boards, each with its own website and format. Stethos is built to gather license records from state boards into one NPI-keyed record, show each license's status and source, and alert you when one changes.",
         k1="Look up", l1=["All licenses for an NPI", "Clinicians licensed in a given state", "Recent license events by state and profession"],
         k2="For each license", l2=["State, profession and license number", "Status: active, expired, restricted", "Issue and expiration dates where published", "Source board and verified date"],
         ep="providers/enrich", req={"npi": "1234567890", "fields": ["licenses"]},
         faq=[("Is this primary source verification?", "No. Stethos is not a credentials verification organization. It's built for sourcing, prospecting, directory checks and monitoring. For credentialing, verify with the state board or your verification vendor."),
              ("Which professions are covered?", "Physicians first, then nurses and other licensed clinicians. Coverage will be published by state and profession at launch."),
              ("Can I be told when a license lapses?", "Yes. Watchers fire license.lapsed and license.issued events for the clinicians you follow.")],
         related=[("Clinical staffing and recruiting", "/use-cases/clinical-staffing"), ("Docs: watchers", "/docs#watch"), ("Physician data API", "/physician-data-api")]),
    dict(slug="health-system-data-api", art="s-healthsys", color="sp-pink", name="Health system data API",
         title="Health System and Hospital Data API | Stethos",
         desc="Health systems, hospitals, groups and clinics in one API: locations, rostered clinicians, leadership, open roles and ownership, with change alerts.",
         h1a="Health system and hospital data,", h1b="with the people inside.",
         intro="Know how a health system is built: the hospitals and groups it owns, who leads them, who practices there and where it's hiring. Stethos is built to keep that map current and alert you when it changes.",
         k1="Organization types", l1=["Health systems and hospitals", "Physician groups and clinics", "Ambulatory surgery centers", "Home health and post-acute providers"],
         k2="Record includes", l2=["Locations and child organizations", "Rostered clinicians", "Leadership with start dates", "Open clinical roles", "Executive hire and hiring spike events"],
         ep="orgs/enrich", req={"name": "Example Health System", "state": "AZ", "fields": ["children", "leadership", "open_roles"]},
         faq=[("Where does organization data come from?", "CMS provider and facility data, organization NPIs, health system websites and job posts, and press releases for leadership changes. Every field shows its source."),
              ("Can I see who works at a hospital?", "Organization records include rostered clinicians drawn from affiliation data, and the list updates as clinicians join or leave."),
              ("Can I track leadership changes?", "Yes. The org.exec_hire event fires when an organization names a new executive or service line leader.")],
         related=[("Healthcare investors", "/use-cases/investors"), ("Docs: organizations", "/docs#orgs"), ("Pricing", "/pricing")]),
]


SEO_PAGES += [
    dict(slug="medicare-utilization-data-api", art="s-medicare", color="sp-lime",
         name="Medicare utilization data API",
         title="Medicare Provider Utilization Data API | Stethos",
         desc="Procedure volumes, Medicare patients and Part D prescribing for every US clinician, from CMS data, resolved to one NPI record. MCP and REST.",
         h1a="Medicare utilization data,", h1b="joined to every provider record.",
         intro="Medicare billing data for every clinician and hospital, matched to the right NPI: services by procedure code, Medicare patients seen, Part D prescriptions and equipment ordered, with the release year on every number.",
         k1="CMS files included", l1=["Medicare Physician &amp; Other Practitioners, by provider and service", "Medicare Part D Prescribers, by provider and drug", "Medicare DMEPOS, by referring provider", "Medicare Inpatient and Outpatient Hospitals, by provider"],
         k2="What your agent can ask", l2=["Which orthopedic surgeons in Ohio do the most knee replacements", "Which cardiologists prescribe a given drug class most", "Which clinicians order the most CPAP equipment", "Which hospitals in a market do the most spine DRGs"],
         ep="providers/search", req={"specialty": "orthopedic surgery", "state": "OH", "procedure_codes": ["27447"], "sort": "-medicare_services", "limit": 25},
         faq=[("Where does this data come from?", "CMS's Medicare Provider Utilization and Payment data. They summarize 100% of Original Medicare fee-for-service claims at the provider level, and CMS suppresses small counts to protect patients."),
              ("How current is it?", "CMS releases these files once a year, covering a past year, so they describe volume and mix rather than this week's activity. Stethos shows the data year on every number and pairs it with fresher signals like affiliation and license changes."),
              ("Does it include Medicare Advantage or commercial claims?", "No. These files cover Original Medicare only. Claims-level data, including Medicare Advantage, requires CMS research access, which Stethos plans to pursue."),
              ("Is there patient data in it?", "No. Every number is aggregated to the provider, and CMS removes counts under 11. Stethos returns provider data only.")],
         related=[("Docs: data sources", "/docs#sources"), ("Physician data API", "/physician-data-api"), ("Medtech sales", "/use-cases/medtech")]),
    dict(slug="home-health-hospice-data-api", art="s-homehealth", color="sp-butter",
         name="Home health and hospice data API",
         title="Home Health, Hospice and SNF Data API | Stethos",
         desc="Volume, payments, patient mix, star ratings and ownership for every Medicare home health agency, hospice and nursing facility, via MCP or REST.",
         h1a="Post-acute provider data", h1b="for home health, hospice and SNFs.",
         intro="One record for every Medicare home health agency, hospice, nursing facility, rehab facility and long-term care hospital: volume, star ratings, quality, ownership and costs, keyed to its CCN and NPI.",
         k1="CMS files included", l1=["Medicare Post-Acute Care &amp; Hospice, by provider", "Care Compare star ratings and quality measures", "Provider of Services file: ownership, beds, certification", "Hospital and SNF cost reports (HCRIS)"],
         k2="What your agent can ask", l2=["Which hospices in a county serve the most dementia patients", "Which home health agencies gained star ratings this year", "Who owns every SNF in a metro, and how many beds each has", "Which agencies' Medicare volume is growing fastest"],
         ep="orgs/search", req={"type": "home_health_agency", "state": "GA", "fields": ["utilization", "star_rating", "ownership"], "limit": 25},
         faq=[("How is this different from Trella Health or similar platforms?", "Those platforms are built on claims-level Medicare data and sold as annual subscriptions with dashboards. Stethos starts from CMS data, priced per tool call and built for agents through MCP. Claims-level referral flows are planned, through CMS's research data program."),
              ("How current is it?", "Star ratings and quality measures refresh monthly to quarterly. The utilization files are released yearly. Every field shows its source and date."),
              ("Can I see referral sources and destinations?", "Not yet. Which hospitals and physicians send patients to which agencies requires claims-level data from CMS's Virtual Research Data Center, which Stethos plans to apply for. Today you get each provider's volume, mix, quality and ownership."),
              ("Does it include patient data?", "No. Everything is aggregated to the provider, and CMS suppresses small counts.")],
         related=[("Docs: data sources", "/docs#sources"), ("Health system data API", "/health-system-data-api"), ("Provider directories", "/use-cases/provider-directories")]),
    dict(slug="physician-referral-data", art="s-referral", color="sp-pink",
         name="Physician referral data",
         title="Physician Referral Data API for AI Agents | Stethos",
         desc="Map who works with whom: group rosters, hospital affiliations, ACO membership and shared practice sites for every US clinician. Referral flows planned.",
         h1a="Physician referral data,", h1b="built from what CMS publishes.",
         intro="Clinicians in the same group, hospital, ACO or building refer to each other most. Stethos maps those ties for every US clinician from CMS data, so your agent can see who is likely to refer to whom.",
         k1="Signals included", l1=["Group practice rosters from Care Compare", "Hospital affiliations", "ACO participation from the Shared Savings Program", "Shared practice addresses and organization NPIs"],
         k2="What your agent can ask", l2=["Which cardiologists share a group or hospital with these PCPs", "Which ACO a practice belongs to, and who else is in it", "Which surgeons operate at the hospitals a group is affiliated with", "Who joined or left a referral network this quarter"],
         ep="providers/enrich", req={"npi": "1234567890", "fields": ["affiliations", "group_roster", "aco", "colocated"]},
         faq=[("Does CMS publish referral data?", "CMS released Physician Shared Patient Patterns files in response to FOIA requests, but they cover claims only through 2015. For current relationships, Stethos uses group, hospital, ACO and location data that CMS updates regularly."),
              ("Will Stethos have claims-based referral flows?", "That's the plan. Current referral counts between clinicians require claims-level Medicare data from CMS's Virtual Research Data Center. Stethos plans to apply as an Innovator; only aggregate, privacy-protected counts can leave that environment."),
              ("Is this enough for sales targeting?", "Often, yes. Shared groups, hospitals and ACOs explain most referral patterns, and they change faster than annual claims files. Stethos also tells your agent when an affiliation changes."),
              ("Is there patient data?", "No. Stethos holds data about clinicians and organizations only.")],
         related=[("Docs: data sources", "/docs#sources"), ("Physician data API", "/physician-data-api"), ("Medtech sales", "/use-cases/medtech")]),
    dict(slug="private-equity-healthcare-ownership-data", art="s-pe", color="sp-blue",
         name="Private equity ownership data",
         title="Private Equity Healthcare Ownership Data API | Stethos",
         desc="Which private equity firms own which practices, clinics, MSOs and facilities, in which markets. Owner, platform and add-on links with sources, via MCP or REST.",
         h1a="See which private equity firms own",
         h1b="which clinics, and where.",
         intro="Private equity has rolled up practices, surgery centers and agencies across the US. Stethos is built to map each firm, its platforms and every site they own by market, plus the people who decide for all of them.",
         k1="What you get", l1=["Private equity owner for each practice, clinic, MSO and facility", "Platform and add-on links, with the date each deal was seen", "Every site in a roll-up, by state and metro", "Deal team and operating partners at the firm, plus MSO leadership"],
         k2="What your agent can ask", l2=["Which PE-backed orthopedic or GI groups operate in Texas", "Every site owned by this firm's dermatology platform", "Which home health agencies in Ohio have a private equity owner", "Which practices in my territory were acquired this quarter"],
         ep="orgs/search", req={"owner_type": "private_equity", "specialty": "gastroenterology", "state": "TN", "fields": ["owners", "platform", "sites", "leadership"], "limit": 25},
         faq=[("Where does ownership data come from?", "For hospitals, nursing homes, home health agencies, hospices, rural health clinics and FQHCs, CMS publishes ownership files that list each owner and flag owner types such as private equity. For physician practices, surgery centers and MSOs, which those files don't cover, Stethos is built to combine firm portfolio pages, acquisition announcements and state filings. Every link carries its source and the date it was seen."),
              ("Who is this for?", "Teams that sell to multi-site, PE-backed groups: revenue cycle, billing, staffing, software and services vendors. Selling to one MSO can open dozens of sites, and the decision usually sits with the MSO and the firm's operating partners rather than each clinic."),
              ("Can I see the people, not just the companies?", "Yes. Stethos is built to return MSO executives and the firm's healthcare deal and operating partners, with business contact details where they're published."),
              ("How current is it?", "CMS updates its ownership files regularly, and acquisitions are picked up when they're announced. Your agent can watch a firm or a platform and hear about new add-ons as they happen."),
              ("Does it include patient data?", "No. Stethos holds data about organizations, their owners and the people who run them only.")],
         related=[("Docs: data sources", "/docs#sources"), ("What CMS ownership files show", "/blog/cms-ownership-data-private-equity"), ("Healthcare investors", "/use-cases/investors")]),
]

def seo_page(m):
    import page_examples as PX
    from segments import BY as SEGBY
    from seo_extra import EXTRA
    x = EXTRA[m["slug"]]
    path = "/" + m["slug"]
    faqld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in m["faq"]]}
    h = head(m["title"], m["desc"], path, image=f"/og/{m['slug']}.jpg", image_alt=f"Illustration for {m['name']}",
             crumbs=[(m["name"], path)], schema=[faqld])
    li = lambda xs: "".join(f"<li>{v}</li>" for v in xs)
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in m["faq"])
    rel = " · ".join(f'<a href="{u}">{t}</a>' for t, u in m["related"])
    sm = x["sample"]
    rows = "".join(f'<li><span class="rec-k">{k}</span><span class="rec-v">{v}</span><span class="rec-s">{n}</span></li>' for k, v, n in sm["rows"])
    asks_is_l2 = m["k2"].lower().startswith("what your agent")
    lists = f'<p class="sp-k">{m["k1"]}</p><ul class="kw-list">{li(m["l1"])}</ul>'
    if not asks_is_l2:
        lists += f'<p class="sp-k">{m["k2"]}</p><ul class="kw-list">{li(m["l2"])}</ul>'
    asks = "".join(f'<li><p class="ask-q">“{q}”</p><p class="ask-a">{a}</p></li>' for q, a in x["asks"])
    teams = "".join(f'<li><a href="/use-cases/{t}" style="--t:{SEGBY[t][4]}">{logo(t, 64)}<span><b>{SEGBY[t][1]}</b>{SEGBY[t][2]}</span></a></li>' for t in x["teams"])
    wf = PX.card(PX._by[x["workflow"]], tab=None, link=True)
    pages = {p2["slug"]: p2 for p2 in SEO_PAGES}
    related = "".join(
        f'<li><a href="/{r}"><img src="/img/g-art-{pages[r]["art"]}-900.webp" width="900" height="672" alt="" loading="lazy" decoding="async">'
        f'<span><b>{pages[r]["name"]}</b>{pages[r]["desc"].split(". ")[0].rstrip(".")}.</span></a></li>' for r in x["related"])
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top ih" aria-labelledby="kw-title">
  <div class="wrap">
    <nav class="crumbs uc-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / {m["name"]}</nav>
    <div class="ih-grid">
      <div class="ih-copy">
        <p class="eyebrow"><span>{m["name"]}</span></p>
        <h1 id="kw-title">{m["h1a"]} <span class="pop">{m["h1b"]}</span></h1>
        <p class="ih-lede">{m["intro"]}</p>
        <div class="kw-ctas"><a class="btn-1" href="{TRIAL}">Start free trial</a><a class="btn-2" href="/docs">Read the docs</a></div>
      </div>
      {ih_art(SCENES[m["slug"]][2:], SCENE_ALTS[SCENES[m["slug"]]])}
    </div>
  </div>
</section>
<section class="sec" aria-labelledby="kw-data-title">
  <div class="wrap">
    <div class="head"><p class="eyebrow"><span>The data</span></p><h2 id="kw-data-title">What it looks like <span class="pop">for your agent.</span></h2></div>
    <div class="kw-data">
      <article class="rec" aria-label="Sample record"><div class="rec-top"><div><p class="rec-t">{sm["title"]}</p><p class="rec-sub">{sm["sub"]}</p></div><span class="hq-live"><i></i>Sample data</span></div><ul class="rec-rows">{rows}</ul></article>
      <div class="kw-side">{lists}</div>
    </div>
  </div>
</section>
<section class="sec kw-asks-sec" aria-labelledby="kw-ask-title">
  <div class="wrap">
    <div class="head"><p class="eyebrow"><span>Ask in plain words</span></p><h2 id="kw-ask-title">What your agent <span class="pop">can ask.</span></h2></div>
    <ul class="kw-asks">{asks}</ul>
  </div>
</section>
<section class="sec" aria-labelledby="kw-who-title">
  <div class="wrap">
    <div class="head"><p class="eyebrow"><span>Who uses it</span></p><h2 id="kw-who-title">Built for teams <span class="pop">like yours.</span></h2></div>
    <ul class="kw-teams">{teams}</ul>
    <div class="kw-wf">{wf}</div>
  </div>
</section>
<section class="sec" aria-labelledby="kw-call-title">
  <div class="wrap uc-call">
    <div><p class="eyebrow"><span>For developers</span></p><h2 id="kw-call-title">One request, <span class="pop">sourced answers.</span></h2>
    <p class="uc-call-p">Your agent can make the same call as an MCP tool. Every result carries the source and last-verified date on each field and the credits it used. See the <a href="/docs">quickstart</a> and <a href="/pricing">pricing</a>.</p></div>
<pre class="uc-code" tabindex="0" aria-label="Example request"><code>curl https://api.stethos.health/v1/{m["ep"]} \\
  -H "Authorization: Bearer $STETHOS_KEY" \\
  -d '{json.dumps(m["req"], indent=2)}'</code></pre>
  </div>
</section>
<section class="sec" aria-labelledby="kw-faq-title">
  <div class="wrap faq-grid">
    <div class="head"><p class="eyebrow"><span>FAQ</span></p><h2 id="kw-faq-title">Common questions</h2><p class="faq-more">Related: {rel}</p><figure class="faq-art"><img src="/img/g-art-r-faq-900.webp" width="900" height="672" alt="Illustration: the little clay robot sitting on a stack of books, thinking, next to a question mark and a lightbulb." loading="lazy" decoding="async"></figure></div>
    <div class="qs">{faq}</div>
  </div>
</section>
<section class="sec" aria-labelledby="kw-rel-title">
  <div class="wrap">
    <div class="head"><p class="eyebrow"><span>Related data</span></p><h2 id="kw-rel-title">Pairs well <span class="pop">with.</span></h2></div>
    <ul class="kw-rel">{related}</ul>
  </div>
</section>
{cta_band("Self-serve", "Make your first tool call", "in five minutes.", "1,000 free credits, no card, no sales call. Pay only for the tool calls you make.", "Stethos%20" + m["slug"])}
</main>
'''
    return h + body + tail()
