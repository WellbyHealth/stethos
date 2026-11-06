from parts import *

# (slug, team, title, trigger, ask, steps, data, lands, art-icon)
EXAMPLES = [
    ("medtech-targeting", "Medtech sales", "Who should I call this week?",
     "Every Monday, or whenever a rep asks.",
     "Find independent spine surgeons in my territory doing 50+ fusions a year, and tell me who changed anything recently.",
     ["Searches surgeons by specialty, territory and Medicare procedure volume",
      "Ranks them by recent changes: a new group, a new surgery center, new hires",
      "Creates or updates the contacts in Salesforce with a one-line talking point"],
     ["Medicare procedure volumes", "Affiliations", "Change events", "Practice contacts"],
     "Salesforce or HubSpot, plus a weekly list in Claude", "g-cl-stk-search-160.webp", "#e4f0fd"),
    ("exec-trigger", "Health IT sales", "Reach the new buyer in their first 90 days",
     "A target health system names a new CIO, CMIO or CFO.",
     "Tell me when any health system in my territory hires a new CIO or CMIO, and draft a first note for each.",
     ["Watches every account in the territory for executive changes",
      "Adds the system's EHR, size and recent news to the alert",
      "Creates a task in the CRM with a short, specific first note for the rep to edit"],
     ["Organizations", "Executive changes", "Certified health IT data", "Change events"],
     "A task in Salesforce or HubSpot, and a Slack message to the rep", "g-cl-stk-watch-160.webp", "#e8f3d2"),
    ("ehr-campaign", "Health IT marketing", "Find every hospital on a given EHR",
     "You launch an integration for a specific EHR.",
     "List every hospital and large group running Oracle Health, with their IT leaders, and load them into HubSpot.",
     ["Finds organizations by the certified EHR they report using",
      "Adds the organization's leadership and locations",
      "Creates a HubSpot list for the campaign"],
     ["ONC certified health IT data", "EHR vendors' published customer lists", "Organizations", "Contacts"],
     "HubSpot or Salesforce", "g-cl-stk-agents-160.webp", "#f5efdf"),
    ("abm-list", "Marketing", "Build an ABM account list with the buying team",
     "Planning a quarter's account-based campaign.",
     "Give me the 200 health systems in the Southeast with 5+ hospitals and a cardiology service line, with the cardiology leaders at each.",
     ["Searches organizations by type, size, region and service lines",
      "Adds the clinicians and leaders in cardiology at each account",
      "Scores accounts by fit and loads them into your marketing tool as a list"],
     ["Organizations", "Service lines", "Affiliations", "Leaders"],
     "HubSpot, Salesforce or your ad platform's audience upload", "g-cl-stk-orgs-160.webp", "#ece6fb"),
    ("kol-mapping", "Pharma", "Map the key opinion leaders for a launch",
     "A new launch or an upcoming congress.",
     "Who are the most active clinicians in this drug class in the Northeast: publishing, running trials and prescribing?",
     ["Finds clinicians by prescribing volume in the class",
      "Adds their publications, trials and grants",
      "Flags industry relationships so medical affairs can review them first"],
     ["Part D prescribers", "Publications and trials", "NIH grants", "Open Payments"],
     "Your CRM or a medical affairs spreadsheet", "g-cl-stk-enrich-160.webp", "#e8f3d2"),
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
    ("staffing-sales", "Staffing sales", "Find the systems that need staff now",
     "Weekly, for the business development team.",
     "Which hospitals in Arizona are posting the most ICU nursing roles, and who runs nursing there?",
     ["Ranks nearby health systems by recent clinical job posts",
      "Adds the chief nursing officer and other leaders at each",
      "Creates the accounts and next steps in your CRM"],
     ["Health system job posts", "Organizations", "Leaders", "Change events"],
     "Your CRM, plus a weekly list in Claude", "g-cl-ic-license-96.webp", "#ece6fb"),
    ("physician-liaison", "Health system marketing", "Grow referrals where your network is thin",
     "A service line's referrals are down.",
     "Which independent primary care doctors near our hospitals aren't affiliated with us, and who recently joined a competing group?",
     ["Finds primary care clinicians near each hospital",
      "Separates those affiliated with you, with competitors, or independent",
      "Flags recent moves so physician liaisons can reach out first"],
     ["Affiliations", "ACO participation", "Change events"],
     "Your physician relations CRM", "g-cl-ic-gov-cut.webp", "#e8f3d2"),
]


def examples():
    items = [{"@type": "ListItem", "position": i + 1, "name": e[2], "url": f"{SITE}/examples#{e[0]}"} for i, e in enumerate(EXAMPLES)]
    h = head("Examples: Healthcare Sales and Marketing Workflows | Stethos",
             "Ten sales and marketing workflows: medtech targeting, new-executive triggers, EHR lists, ABM, KOL mapping, territories, event invites, CRM hygiene and more.",
             "/examples", crumbs=[("Examples", "/examples")],
             schema=[{"@type": "ItemList", "name": "Stethos example workflows", "itemListElement": items}])
    jump = "".join(f'<li><a href="#{e[0]}">{e[1]}</a></li>' for e in EXAMPLES)
    cards = ""
    for i, (slug, team, title, trigger, ask, steps, data, lands, ic, tint) in enumerate(EXAMPLES, 1):
        st = "".join(f"<li>{x}</li>" for x in steps)
        dt = "".join(f"<li>{x}</li>" for x in data)
        cards += f'''<article class="ex-card" id="{slug}" style="--t:{tint}">
      <div class="ex-head"><span class="ex-ic"><img src="/img/{ic}" width="64" height="64" alt="" loading="lazy" decoding="async"></span><div><p class="ex-team">{i:02d} · {team}</p><h2>{title}</h2></div></div>
      <p class="ex-trigger"><b>When</b> {trigger}</p>
      <p class="ex-ask"><span class="ex-ask-k">Ask</span>“{ask}”</p>
      <div class="ex-cols">
        <div><p class="ex-k">What the agent does</p><ol class="ex-steps">{st}</ol></div>
        <div><p class="ex-k">Stethos data it uses</p><ul class="ex-data">{dt}</ul><p class="ex-k">Where the result lands</p><p class="ex-lands">{lands}</p></div>
      </div>
    </article>
'''
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top ex" aria-labelledby="ex-title">
  <div class="wrap">
    <nav class="crumbs uc-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Examples</nav>
    <div class="head center">
      <p class="eyebrow"><span>Examples</span></p>
      <h1 id="ex-title">What sales and marketing agents <span class="pop">do with Stethos.</span></h1>
      <p class="kpi-lede">Ten sales and marketing workflows your team could run from the AI assistant and CRM it already uses. Each one shows the question, what the agent does, the data behind it and where the result lands. Names and numbers are examples.</p>
    </div>
    <ul class="ex-jump" aria-label="Jump to an example">{jump}</ul>
    <div class="ex-list">
    {cards}
    </div>
    <p class="cov-note ex-more">Have a workflow in mind? <a href="mailto:{EMAIL}?subject=Stethos%20workflow">Tell us about it</a>, or see the <a href="/use-cases">use cases</a> and <a href="/docs">docs</a>.</p>
  </div>
</section>
{cta_band("Self-serve", "Run your first workflow", "in five minutes.", "1,000 free credits, no card, no sales call. Pay only for the tool calls you make.", "examples")}
</main>
'''
    return h + body + tail()
