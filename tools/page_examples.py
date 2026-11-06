from parts import *

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
    ("referral-partners", "Referral development", "Find the doctors who should be referring to you",
     "A home health or hospice agency enters a new county, or referrals dip.",
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
    ("Medtech", "medtech-pharma", ["medtech-targeting", "territory-planning", "abm-list"]),
    ("Pharma", "medtech-pharma", ["kol-mapping", "event-invites"]),
    ("Health IT and services", "health-it-sales", ["exec-trigger", "ehr-campaign", "crm-hygiene"]),
    ("Investors", "investors", ["deal-diligence", "portfolio-watch"]),
    ("Startups", "digital-health", ["startup-first-customers"]),
    ("Clinical staffing", "clinical-staffing", ["staffing-sales"]),
    ("Post-acute care and agencies", "post-acute", ["referral-partners", "discharge-sources"]),
    ("Health systems", None, ["physician-liaison"]),
]
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
    more = f'<p class="ex-foot"><a href="/use-cases/{page}">More for {seg} <span aria-hidden="true">→</span></a></p>' if (link and page) else ""
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


def examples():
    items = [{"@type": "ListItem", "position": i + 1, "name": e[2], "url": f"{SITE}/use-cases#{e[0]}"} for i, e in enumerate(EXAMPLES)]
    h = head("Use Cases: Healthcare Sales, Marketing and Deal Workflows",
             "Agent workflows by segment: medtech, pharma, health IT, investors, startups, staffing, post-acute and health systems. Targeting, referrals, ABM and more.",
             "/use-cases", image="/og/use-cases.jpg", crumbs=[("Use cases", "/use-cases")],
             schema=[{"@type": "ItemList", "name": "Stethos use cases", "itemListElement": items}])
    jump, n = "", 0
    for name, page, slugs in SEGMENTS:
        jump += f'<li class="ex-grp" role="presentation">{name}</li>'
        for slug in slugs:
            e = _by[slug]
            jump += (f'<li role="presentation"><a class="ex-tab" href="#{e[0]}" role="tab" id="tab-{e[0]}" aria-controls="{e[0]}" aria-selected="{"true" if n == 0 else "false"}" style="--t:{e[9]}">'
                     f'<span class="ex-tab-ic"><img src="/img/{e[8]}" width="40" height="40" alt="" loading="lazy" decoding="async"></span>'
                     f'<span class="ex-tab-t"><b>{e[1]}</b>{e[2]}</span></a></li>')
            n += 1
    cards = "".join(card(e, tab=(n == 0)) for n, e in enumerate(EXAMPLES))
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top ex" aria-labelledby="ex-title">
  <div class="wrap">
    <nav class="crumbs uc-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Use cases</nav>
    <div class="head center">
      <p class="eyebrow"><span>Use cases</span></p>
      <h1 id="ex-title">What teams <span class="pop">do with Stethos.</span></h1>
      <p class="kpi-lede">Real workflows by segment, run from the AI assistant and CRM you already use. Pick one to see how it works, or open a segment for the data behind it.</p>
    </div>
    <div class="ex-split">
      <div class="ex-navwrap">
        <ul class="ex-nav" role="tablist" aria-label="Example workflows">{jump}</ul>
        <button class="ex-morebtn" type="button" tabindex="-1" aria-hidden="true">More workflows <span aria-hidden="true">↓</span></button>
      </div>
      <div class="ex-stage">
      {cards}
      </div>
    </div>
    <p class="cov-note ex-more">Have a workflow in mind? <a href="mailto:{EMAIL}?subject=Stethos%20workflow">Tell us about it</a>, or see the <a href="/docs">docs</a>. Also: <a href="/use-cases/healthcare-marketing">healthcare marketing</a> and <a href="/use-cases/provider-directories">provider directories</a>.</p>
  </div>
</section>
{cta_band("Self-serve", "Run your first workflow", "in five minutes.", "1,000 free credits, no card, no sales call. Pay only for the tool calls you make.", "use-cases")}
</main>
'''
    return h + body + tail(("nav", "examples"))


HOME_PICKS = ["medtech-targeting", "kol-mapping", "exec-trigger", "deal-diligence", "referral-partners"]


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
