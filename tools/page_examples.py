from parts import *
from segments import scene, seg_grid, seg_tabs, logo, ih_art

# (slug, team, title, trigger, ask, steps, data, lands, art-icon)
EXAMPLES = [
    ("medtech-targeting", "Sales", "Who should I call this week?",
     "Every Monday, or whenever a rep asks.",
     "Find independent spine surgeons in my territory doing 50+ fusions a year, and tell me who changed anything recently.",
     ["Searches surgeons by specialty, territory and Medicare procedure volume",
      "Ranks them by recent changes: a new group, a new surgery center, new hires",
      "Creates or updates the contacts in Salesforce with a one-line talking point"],
     ["Medicare procedure volumes", "Affiliations", "Change events", "Practice contacts"],
     "Salesforce or HubSpot, plus a weekly list in Claude", "g-cl-stk-search-160.webp", "#e4f0fd"),
    ("exec-trigger", "Sales", "Reach the new buyer in their first 90 days",
     "A target health system names a new CIO, CMIO or CFO.",
     "Tell me when any health system in my territory hires a new CIO or CMIO, and draft a first note for each.",
     ["Watches every account in the territory for executive changes",
      "Adds the system's EHR, size and recent news to the alert",
      "Creates a task in the CRM with a short, specific first note for the rep to edit"],
     ["Organizations", "Executive changes", "Certified health IT data", "Change events"],
     "A task in Salesforce or HubSpot, and a Slack message to the rep", "g-cl-stk-watch-160.webp", "#e8f3d2"),
    ("ehr-campaign", "Marketing", "Find every hospital on a given EHR",
     "You launch an integration for a specific EHR.",
     "List every hospital and large group running Oracle Health, with their IT leaders, and load them into HubSpot.",
     ["Finds organizations by the certified EHR they report using",
      "Adds the organization's leadership and locations",
      "Creates a HubSpot list for the campaign"],
     ["ONC certified health IT data", "EHR vendors' published customer lists", "Organizations", "Contacts"],
     "HubSpot or Salesforce", "g-cl-stk-agents-160.webp", "#f5efdf"),
    ("abm-list", "Account-based marketing", "Build an ABM account list with the buying team",
     "Planning a quarter's account-based campaign.",
     "Give me the 200 health systems in the Southeast with 5+ hospitals and a cardiology service line, with the cardiology leaders at each.",
     ["Searches organizations by type, size, region and service lines",
      "Adds the clinicians and leaders in cardiology at each account",
      "Scores accounts by fit and loads them into your marketing tool as a list"],
     ["Organizations", "Service lines", "Affiliations", "Leaders"],
     "HubSpot, Salesforce or your ad platform's audience upload", "g-cl-stk-orgs-160.webp", "#ece6fb"),
    ("kol-mapping", "Medical affairs and marketing", "Map the key opinion leaders for a launch",
     "A new launch or an upcoming congress.",
     "Who are the most active clinicians in this drug class in the Northeast: publishing, running trials and prescribing?",
     ["Finds clinicians by prescribing volume in the class",
      "Adds their publications, trials and grants",
      "Flags industry relationships so medical affairs can review them first"],
     ["Part D prescribers", "Publications and trials", "NIH grants", "Open Payments"],
     "Your CRM or a medical affairs spreadsheet", "g-cl-stk-enrich-160.webp", "#e8f3d2"),
    ("deal-diligence", "Diligence", "Market diligence in an afternoon",
     "A deal comes in for a regional orthopedic or GI group.",
     "Map every orthopedic group in metro Phoenix: size, ownership, hospital ties, volume, quality and payer mix.",
     ["Maps every group, its clinicians and its parent organization",
      "Adds Medicare volume, quality scores and Medicare Advantage share by county",
      "Writes a short memo with a spreadsheet of the underlying records and sources"],
     ["Organizations", "Affiliations", "Medicare utilization", "Cost reports", "MA enrollment"],
     "A memo in Claude and a spreadsheet for the deal team", "g-cl-stk-orgs-160.webp", "#e4f0fd"),
    ("portfolio-watch", "Portfolio monitoring", "Know when a portfolio or target company changes",
     "Continuously, across the portfolio and the pipeline.",
     "Tell me whenever one of our portfolio companies or the 40 groups on our target list adds or loses clinicians, opens a site or hires an executive.",
     ["Watches each organization's clinicians, locations and leaders",
      "Rolls changes into a weekly digest, with the source for each",
      "Flags big moves, like a group losing several surgeons, the day they show up"],
     ["Organizations", "Affiliations", "Change events", "Locations"],
     "A weekly digest in Slack or email, plus your deal CRM", "g-cl-stk-watch-160.webp", "#ece6fb"),
    ("pe-rollup-sell", "Sales", "Sell to a PE-backed roll-up as one account",
     "A billing, staffing or software vendor wants multi-site groups.",
     "Which private equity firms own GI and orthopedic groups in the Southeast, how many sites does each platform have, and who runs the MSO?",
     ["Maps each firm's platforms and every site they own, by state",
      "Adds the MSO's executives and the firm's healthcare operating partners",
      "Creates one account per platform in your CRM, with its sites underneath"],
     ["Ownership", "Organizations", "Leadership", "Locations"],
     "Your CRM, one account per platform", "g-cl-stk-orgs-160.webp", "#fde8e4"),
    ("pe-map", "Market mapping", "See who has rolled up a market",
     "Before a new thesis or platform deal.",
     "Which private equity firms own dermatology practices in Florida, how many sites does each have, and which practices are still independent?",
     ["Groups every practice by its private equity owner and platform",
      "Counts sites per firm by metro, with the date each deal was seen",
      "Lists the independent practices left in each metro"],
     ["Ownership", "Organizations", "Locations", "Change events"],
     "A market map in Claude and a spreadsheet for the deal team", "g-cl-ic-pin-96.webp", "#ece6fb"),
    ("directory-audit", "Network operations", "Audit every listing before members find the errors",
     "Before each directory refresh, or monthly.",
     "Check our 12,000 cardiology and orthopedic listings and flag anyone who has moved, lost a license or left the network.",
     ["Matches each listing to a current record by NPI",
      "Flags moved clinicians, lapsed licenses and network changes, with sources",
      "Writes a fix list your team can review and push"],
     ["NPI records", "Licenses", "Network listings", "Practice locations"],
     "A review queue and a corrected file", "g-cl-ic-payer-96.webp", "#ece6fb"),
    ("audience-refresh", "Marketing operations", "Keep a campaign audience current",
     "Before every send.",
     "Refresh our 8,000-clinician audience: drop anyone who changed jobs or retired, and add new physicians who match.",
     ["Rechecks each contact's employer, location and license",
      "Removes people who left, before the emails bounce",
      "Adds new matches from the same specialties and markets"],
     ["Affiliations", "Licenses", "Practice contacts", "Change events"],
     "Your marketing platform or CRM", "g-cl-ic-pin-96.webp", "#fde8dc"),
    ("find-a-doctor", "Product", "Power provider search in your app",
     "Every time a user searches.",
     "Show in-network dermatologists within 10 miles who are accepting new patients.",
     ["Searches by specialty, location and network",
      "Returns current locations and contact details, with sources",
      "Sends a webhook when a listed provider changes"],
     ["Provider search", "Network listings", "Practice locations", "Watchers"],
     "Your app, through the REST API", "g-cl-stk-search-160.webp", "#e4f0fd"),
    ("license-sourcing", "Recruiting", "Source clinicians licensed where the job is",
     "When a hard-to-fill role opens.",
     "Find ICU nurses with an active Arizona license who practice within 50 miles of Phoenix and changed employers in the last two years.",
     ["Searches clinicians by license state, profession and specialty",
      "Adds current employer and employment history",
      "Ranks by fit and builds an outreach list"],
     ["Licenses", "Affiliations", "Practice locations"],
     "Your ATS or recruiting CRM", "g-cl-ic-license-96.webp", "#e3f4ec"),
    ("competitor-watch", "Physician relations", "Know when a physician joins a competitor",
     "Continuously, across your service area.",
     "Tell me when a physician in our service area joins a competing group or hospital, or opens a new practice.",
     ["Watches affiliations for community physicians",
      "Flags moves to competing systems and new practices",
      "Sends each liaison a weekly list with next steps"],
     ["Affiliations", "Change events", "Locations"],
     "Your physician relations CRM and a weekly email", "g-cl-stk-watch-160.webp", "#fbe4ea"),
    ("startup-first-customers", "First customers", "Find your first ten design partners",
     "A seed-stage team is ready to sell.",
     "Find independent cardiology groups with 10 to 40 clinicians in the Midwest that run athenahealth, with the practice administrator at each.",
     ["Searches groups by specialty, size, region and reported EHR",
      "Adds the practice's leaders and contact details, with sources",
      "Loads the list into your CRM and drafts a short first note for each"],
     ["Organizations", "Certified health IT data", "Leaders", "Practice contacts"],
     "HubSpot, Attio or a Google Sheet", "g-cl-stk-agents-160.webp", "#e8f3d2"),
    ("territory-planning", "Sales operations", "Draw territories on real accounts",
     "Annual planning, or a new rep starts.",
     "Split Texas into four territories with a similar number of high-volume orthopedic surgeons in each.",
     ["Counts target surgeons and facilities by county and metro",
      "Weights them by procedure volume and current affiliation",
      "Proposes balanced territories and lists the top accounts in each"],
     ["Medicare procedure volumes", "Practice locations", "Affiliations"],
     "A territory sheet for sales ops, and account owners in the CRM", "g-cl-ic-pin-96.webp", "#e4f0fd"),
    ("event-invites", "Field marketing", "Fill the room for a dinner or workshop",
     "A regional event or a booth at a congress.",
     "Find gastroenterologists within 30 miles of our Chicago dinner who perform colonoscopies and haven't met with us.",
     ["Finds clinicians by specialty, procedure and distance from the venue",
      "Removes anyone already in the CRM as a customer or recent contact",
      "Builds the invite list with practice contacts and sources"],
     ["Specialty and procedure data", "Practice locations", "Practice contacts", "Your CRM"],
     "A campaign list in your marketing tool", "g-cl-envelope-cut.webp", "#fbe3ee"),
    ("crm-hygiene", "Revenue operations", "Keep the CRM true without data entry",
     "Continuously, on every account and contact.",
     "Check every physician contact in Salesforce and fix anyone who moved, retired or changed groups.",
     ["Matches each contact to an NPI-keyed record",
      "Updates employer, location and specialty, with the source for each change",
      "Watches the list and sends a webhook whenever a contact changes again"],
     ["NPI Registry", "Affiliations", "Change events", "Licenses"],
     "Salesforce, HubSpot or your data warehouse", "g-cl-tr-shield-cut.webp", "#f5efdf"),
    ("staffing-sales", "Business development", "Find the systems that need staff now",
     "Weekly, for the business development team.",
     "Which hospitals in Arizona are posting the most ICU nursing roles, and who runs nursing there?",
     ["Ranks nearby health systems by recent clinical job posts",
      "Adds the chief nursing officer and other leaders at each",
      "Creates the accounts and next steps in your CRM"],
     ["Health system job posts", "Organizations", "Leaders", "Change events"],
     "Your CRM, plus a weekly list in Claude", "g-cl-ic-license-96.webp", "#ece6fb"),
    ("referrer-nudge", "Marketing", "Never let a referrer go quiet",
     "Every Monday, for each marketer on the team.",
     "Each week, tell every marketer which of their referrers they haven't reached in 60 days, and flag anyone who changed practices.",
     ["Matches your referral list, with the last time each one was contacted, to current records",
      "Finds referrers who've gone quiet, and anyone who moved to a new practice or hospital",
      "Sends each marketer a short list with the right address and a reason to reach out"],
     ["Your referral list", "Affiliations", "Practice contacts", "Change events"],
     "A weekly email or Slack message per marketer; no CRM needed", "g-cl-envelope-cut.webp", "#fbe3ee"),
    ("referral-map", "Market strategy", "Map your referral network against the market",
     "Entering a new city, or planning where to add a marketer.",
     "Compare our referral network with every physician practice and hospital in Dallas County, and show which offices and campuses we haven't reached.",
     ["Matches your referrers to their practices, hospitals and campuses",
      "Breaks large medical centers into departments and locations, with who works where",
      "Ranks the gaps by size and fit, so you know where the next marketer should start"],
     ["Your referral list", "Organizations", "Affiliations", "Medicare post-acute utilization"],
     "A territory map and ranked list in Claude, or a spreadsheet", "g-cl-ic-pin-96.webp", "#e4f0fd"),
    ("referral-partners", "Referral development", "Find the doctors who should be referring to you",
     "There are more referrers than your team can cover, or referrals dip.",
     "Which physicians in Maricopa County order the most home health for Medicare patients, and which of them don't refer to us yet?",
     ["Ranks physicians by home health and hospice orders from Medicare data",
      "Adds their practice, hospital ties and contact details",
      "Builds a call plan for each liaison and logs visits in the CRM"],
     ["Medicare post-acute utilization", "Affiliations", "Practice contacts", "Your CRM"],
     "Your referral CRM, plus a weekly list in Claude", "g-cl-ic-pin-96.webp", "#e8f3d2"),
    ("discharge-sources", "Hospital partnerships", "Get on the discharge planner's short list",
     "A skilled nursing facility or agency wants more hospital referrals.",
     "Which hospitals within 20 miles discharge the most patients to skilled nursing, who leads case management there, and how do we compare with nearby facilities?",
     ["Lists nearby hospitals by Medicare discharge volume to post-acute care",
      "Adds case management and population health leaders at each",
      "Compares your Care Compare ratings with nearby competitors for the pitch"],
     ["Hospitals", "Medicare post-acute files", "Care Compare ratings", "Leaders"],
     "A partnership plan in Claude and accounts in the CRM", "g-cl-ic-gov-cut.webp", "#f5efdf"),
    ("physician-liaison", "Physician relations", "Grow referrals where your network is thin",
     "A service line's referrals are down.",
     "Which independent primary care doctors near our hospitals aren't affiliated with us, and who recently joined a competing group?",
     ["Finds primary care clinicians near each hospital",
      "Separates those affiliated with you, with competitors, or independent",
      "Flags recent moves so physician liaisons can reach out first"],
     ["Affiliations", "ACO participation", "Change events"],
     "Your physician relations CRM", "g-cl-ic-gov-cut.webp", "#e8f3d2"),
]


SEGMENTS = [
    ("Medtech", "medtech", ["medtech-targeting", "territory-planning", "abm-list"]),
    ("Pharma", "pharma", ["kol-mapping", "event-invites"]),
    ("Health IT and services", "health-it-sales", ["exec-trigger", "pe-rollup-sell", "ehr-campaign", "crm-hygiene"]),
    ("Healthcare marketing", "healthcare-marketing", ["audience-refresh"]),
    ("Investors", "investors", ["deal-diligence", "pe-map", "portfolio-watch"]),
    ("Startups", "digital-health", ["startup-first-customers", "find-a-doctor"]),
    ("Clinical staffing", "clinical-staffing", ["staffing-sales", "license-sourcing"]),
    ("Post-acute care", "post-acute", ["referrer-nudge", "referral-map", "referral-partners", "discharge-sources"]),
    ("Payers and directories", "provider-directories", ["directory-audit"]),
    ("Health systems", "health-systems", ["physician-liaison", "competitor-watch"]),
]
# Use cases grouped by the job they do (the use-case library is organized this way)
JOBS = [
    ("prospecting", "Prospecting and targeting", "Find the right accounts and people, and decide who to call first.",
     ["medtech-targeting", "abm-list", "ehr-campaign", "staffing-sales", "license-sourcing", "startup-first-customers", "event-invites"]),
    ("triggers", "Timing and triggers", "Reach out the week something changes, not a quarter later.",
     ["exec-trigger", "portfolio-watch", "competitor-watch", "referrer-nudge"]),
    ("referrals", "Referrals and networks", "See who works with whom, and grow the relationships that send you business.",
     ["referral-map", "referral-partners", "discharge-sources", "physician-liaison", "kol-mapping"]),
    ("markets", "Markets and ownership", "Map a market, its owners and its roll-ups before you plan or invest.",
     ["deal-diligence", "pe-map", "pe-rollup-sell", "territory-planning"]),
    ("data-quality", "Data quality", "Keep your CRM, directory, audience or app current without manual checks.",
     ["crm-hygiene", "directory-audit", "audience-refresh", "find-a-doctor"]),
]
# Borrowed workflows shown on a team page in addition to its own
EXTRA_WF = {"healthcare-marketing": ["abm-list", "event-invites"], "provider-directories": ["crm-hygiene"]}
_by = {e[0]: e for e in EXAMPLES}
SEG_OF = {slug: (name, page) for name, page, slugs in SEGMENTS for slug in slugs}
EXAMPLES = [_by[slug] for _, _, slugs in SEGMENTS for slug in slugs]


def for_page(page):
    return [e for e in EXAMPLES if SEG_OF[e[0]][1] == page]
assert len(EXAMPLES) == len(_by)


def card(e, tab=False, link=True):
    slug, team, title, trigger, ask, steps, data, lands, ic, tint = e
    seg, page = SEG_OF[slug]
    st = "".join(f"<li>{x}</li>" for x in steps)
    dt = "".join(f"<li>{x}</li>" for x in data)
    attrs = f' role="tabpanel" aria-labelledby="tab-{slug}" tabindex="-1"' if tab is not None else ""
    more = f'<p class="ex-foot"><a href="/solutions/{page}">More for {seg} <span aria-hidden="true">→</span></a></p>' if (link and page) else ""
    return f'''<article class="ex-card{" ex-on" if tab else ""}" id="{slug}"{attrs} style="--t:{tint}">
      <div class="ex-head"><span class="ex-ic"><img src="/img/{ic}" width="64" height="64" alt="" loading="lazy" decoding="async"></span><div><p class="ex-team">{seg} · {team}</p><h2>{title}</h2></div></div>
      <p class="ex-trigger"><b>When</b> {trigger}</p>
      <p class="ex-ask"><span class="ex-ask-k">Ask</span>“{ask}”</p>
      <div class="ex-cols">
        <div><p class="ex-k">What the agent does</p><ol class="ex-steps">{st}</ol></div>
        <div><p class="ex-k">Stethos data it uses</p><ul class="ex-data">{dt}</ul><p class="ex-k">Where the result lands</p><p class="ex-lands">{lands}</p></div>
      </div>{more}
    </article>
'''


def lib_card(e):
    slug, team, title, trigger, ask, steps, data, lands, ic, tint = e
    seg, page = SEG_OF[slug]
    return (f'<article class="lib-card" id="{slug}" data-team="{page}" style="--t:{tint}">'
            f'<div class="ex-head"><span class="ex-ic"><img src="/img/{ic}" width="64" height="64" alt="" loading="lazy" decoding="async"></span>'
            f'<div><p class="ex-team"><a href="/solutions/{page}">{seg}</a> · {team}</p><h3>{title}</h3></div></div>'
            f'<p class="ex-trigger"><b>When</b> {trigger}</p>'
            f'<p class="lib-ask">“{ask}”</p>'
            f'<ul class="ex-data">{"".join(f"<li>{x}</li>" for x in data)}</ul>'
            f'<details class="lib-more"><summary>How it works</summary><ol class="ex-steps">{"".join(f"<li>{x}</li>" for x in steps)}</ol>'
            f'<p class="lib-lands"><b>Where the result lands:</b> {lands}</p></details></article>')


def examples():
    """The use-case library: every workflow, grouped by the job it does, filterable by team."""
    from segments import SEG
    items = [{"@type": "ListItem", "position": i + 1, "name": e[2], "url": f"{SITE}/use-cases#{e[0]}"} for i, e in enumerate(EXAMPLES)]
    h = head("Use Cases: Healthcare Sales and Market Workflows | Stethos",
             "Workflows your AI agent can run with Stethos: prospecting, buying triggers, referral networks, market and ownership mapping, and data quality.",
             "/use-cases", image="/og/use-cases.jpg", image_alt="Clay illustration, above the line: What teams do with Stethos.", crumbs=[("Use cases", "/use-cases")],
             schema=[{"@type": "ItemList", "name": "Stethos use cases", "itemListElement": items}])
    chips = '<button type="button" class="lib-chip" data-job="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" class="lib-chip" data-job="{k}" aria-pressed="false">{name}</button>' for k, name, _, _ in JOBS)
    teams = '<option value="all">All teams</option>' + "".join(f'<option value="{s[0]}">{s[1]}</option>' for s in SEG)
    groups = "".join(
        f'<section class="lib-group" id="{k}" data-job="{k}" aria-labelledby="h-{k}"><div class="lib-gh"><h2 id="h-{k}">{name}</h2><p>{blurb}</p></div>'
        f'<div class="lib-grid">{"".join(lib_card(_by[x]) for x in slugs)}</div></section>'
        for k, name, blurb, slugs in JOBS)
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top ih" aria-labelledby="lib-title">
  <div class="wrap">
    <nav class="crumbs uc-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Use cases</nav>
    <div class="ih-grid">
      <div class="ih-copy">
        <p class="eyebrow"><span>Use cases</span></p>
        <h1 id="lib-title">Workflows your agent can run, <span class="pop">by job and by team.</span></h1>
        <p class="ih-lede">{len(EXAMPLES)} workflows, from finding accounts to mapping referrals. Each one shows what to ask, what the agent does and where the result lands.</p>
        <div class="kw-ctas"><a class="btn-1" href="{TRIAL}">Start free trial</a><a class="btn-2" href="/solutions">Find your team</a></div>
      </div>
      {ih_art("home-map", "Illustration: a quilted clay map draped over the hills with pins on hospitals, clinics and homes, and the little robot planting a flag.")}
    </div>
  </div>
</section>
<section class="sec lib" aria-label="Use case library">
  <div class="wrap">
    <div class="lib-bar"><div class="lib-chips" role="group" aria-label="Filter by job">{chips}</div>
      <label class="lib-team">Team <select id="lib-team">{teams}</select></label></div>
    {groups}
    <p class="lib-empty" hidden>No workflows match yet for that team and job. <a href="mailto:{EMAIL}?subject=Stethos%20workflow">Tell us what you need</a>.</p>
  </div>
</section>
{cta_band("Self-serve", "Run your first workflow", "in five minutes.", "1,000 free credits, no card, no sales call. Pay only for the tool calls you make.", "use-cases")}
</main>
'''
    return h + body + tail(("nav", "library"))


def solutions():
    """Index of customer profiles: one card per team."""
    from segments import SEG, ROLES
    h = head("Solutions: Healthcare Market Data for Every Team | Stethos",
             "Healthcare market data for medtech, pharma, health IT, marketing, investors, startups, post-acute, staffing, payers and health systems.",
             "/solutions", image="/og/use-cases.jpg", image_alt="Clay illustration of a little town of healthcare buildings.", crumbs=[("Solutions", "/solutions")],
             schema=[{"@type": "ItemList", "name": "Stethos solutions", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": t[1], "url": f"{SITE}/solutions/{t[0]}"} for i, t in enumerate(SEG)]}])
    def team_card(t):
        wfs = [e for e in EXAMPLES if SEG_OF[e[0]][1] == t[0]][:2]
        links = "".join(f'<li><a href="/use-cases#{e[0]}">{e[2]}</a></li>' for e in wfs)
        return (f'<li class="sol-card" style="--t:{t[4]}"><a class="sol-main" href="/solutions/{t[0]}"><img src="/img/g-{t[3]}-320.webp" width="80" height="80" alt="" loading="lazy" decoding="async">'
                f'<span><b>{t[1]}</b>{t[2]}</span></a><p class="sol-k">Built for {ROLES[t[0]][0].lower()}, {ROLES[t[0]][1].lower()} and more</p>'
                f'<ul class="sol-wf">{links}</ul><a class="sol-go" href="/solutions/{t[0]}">See {t[1]} <span aria-hidden="true">→</span></a></li>')
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top ih" aria-labelledby="sol-title">
  <div class="wrap">
    <nav class="crumbs uc-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Solutions</nav>
    <div class="ih-grid">
      <div class="ih-copy">
        <p class="eyebrow"><span>Solutions</span></p>
        <h1 id="sol-title">Built for every team <span class="pop">that sells into healthcare.</span></h1>
        <p class="ih-lede">Pick your team to see the workflows, data and signals that matter to you.</p>
        <div class="kw-ctas"><a class="btn-1" href="{TRIAL}">Start free trial</a><a class="btn-2" href="/use-cases">Browse use cases</a></div>
      </div>
      {ih_art("usecases", "Illustration: a little clay town with a hospital, a pharma lab, an office tower, a bank and a home-care house, with the robot walking between them.")}
    </div>
  </div>
</section>
<section class="sec" aria-labelledby="sol-list-title">
  <div class="wrap">
    <div class="head"><p class="eyebrow"><span>By team</span></p><h2 id="sol-list-title">Find your team.</h2></div>
    <ul class="sol-grid">{"".join(team_card(t) for t in SEG)}</ul>
  </div>
</section>
{cta_band("Self-serve", "Try it on", "your own market.", "1,000 free credits, no card, no sales call. Pay only for the tool calls you make.", "solutions")}
</main>
'''
    return h + body + tail()


HOME_PICKS = ["medtech-targeting", "kol-mapping", "exec-trigger", "deal-diligence", "referrer-nudge"]


def home_split():
    picks = [_by[x] for x in HOME_PICKS]
    tabs = "".join(
        f'<li role="presentation"><a class="ex-tab" href="#{e[0]}" role="tab" id="tab-{e[0]}" aria-controls="{e[0]}" aria-selected="{"true" if n == 0 else "false"}" style="--t:{e[9]}">'
        f'<span class="ex-tab-ic"><img src="/img/{e[8]}" width="40" height="40" alt="" loading="lazy" decoding="async"></span>'
        f'<span class="ex-tab-t"><b>{SEG_OF[e[0]][0]}</b>{e[2]}</span></a></li>' for n, e in enumerate(picks))
    cards = "".join(card(e, tab=(n == 0)) for n, e in enumerate(picks))
    return f'''<div class="ex-split">
      <div class="ex-navwrap"><ul class="ex-nav" role="tablist" aria-label="Example use cases">{tabs}</ul></div>
      <div class="ex-stage">{cards}</div>
    </div>'''
