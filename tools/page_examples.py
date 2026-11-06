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
    ("kol-mapping", "Pharma", "Map the key opinion leaders for a launch",
     "A new launch or an upcoming congress.",
     "Who are the most active clinicians in this drug class in the Northeast: publishing, running trials and prescribing?",
     ["Finds clinicians by prescribing volume in the class",
      "Adds their publications, trials and grants",
      "Flags industry relationships so medical affairs can review them first"],
     ["Part D prescribers", "Publications and trials", "NIH grants", "Open Payments"],
     "Your CRM or a medical affairs spreadsheet", "g-cl-stk-enrich-160.webp", "#e8f3d2"),
    ("directory-accuracy", "Health plans", "Keep the provider directory accurate",
     "Quarterly attestation, or a member complaint.",
     "Check our cardiology listings in Ohio and tell me which ones are wrong.",
     ["Compares each listing with current licenses, locations and affiliations",
      "Has Stethos agents call the practice to confirm the phone line and whether it's taking new patients",
      "Opens a ticket for every mismatch, with the evidence attached"],
     ["Payer directories", "NPI Registry and CMS directory", "Licenses", "Agent verification"],
     "Your ticketing system or data warehouse", "g-cl-ic-payer-96.webp", "#fbe3ee"),
    ("license-watch", "Telehealth", "Catch license problems before a shift",
     "A clinician joins, then continuous monitoring.",
     "Watch licenses for all 140 of our clinicians and warn me before anyone sees a patient in a state where they can't.",
     ["Confirms every state license and nurse compact privilege at onboarding",
      "Watches for lapses, discipline and exclusions",
      "Alerts operations by webhook before the next shift is booked"],
     ["State licensing boards", "Compact privileges", "Exclusion lists"],
     "Your scheduling system or Slack", "g-cl-ic-license-96.webp", "#f5efdf"),
    ("staffing-sourcing", "Clinical staffing", "Fill an urgent role with licensed candidates",
     "A hospital posts an urgent travel nurse or locum role.",
     "Find ICU nurses licensed in Arizona within 50 miles of Tucson, and which nearby systems are hiring hardest.",
     ["Lists clinicians with the right license, specialty and location",
      "Ranks nearby health systems by recent hiring",
      "Adds candidates and sales targets to your applicant system and CRM"],
     ["Licenses", "Affiliations", "Health system job posts", "Contacts"],
     "Your applicant system and CRM", "g-cl-stk-orgs-160.webp", "#ece6fb"),
    ("deal-diligence", "Investors", "Market diligence in an afternoon",
     "A deal comes in for a regional orthopedic or GI group.",
     "Map every orthopedic group in metro Phoenix: size, ownership, hospital ties, volume, quality and payer mix.",
     ["Maps every group, its clinicians and its parent organization",
      "Adds Medicare volume, quality scores and Medicare Advantage share by county",
      "Writes a short memo with a spreadsheet of the underlying records and sources"],
     ["Organizations", "Affiliations", "Medicare utilization", "Cost reports", "MA enrollment"],
     "A memo in Claude and a spreadsheet for the deal team", "g-cl-stk-orgs-160.webp", "#e4f0fd"),
    ("network-mapping", "Health systems", "See where your network is thin",
     "Strategy asks why a service line's volume is down.",
     "Which independent primary care doctors near our hospitals aren't affiliated with us, and who recently joined a competing group?",
     ["Finds primary care clinicians near each hospital",
      "Separates those affiliated with you, with competitors, or independent",
      "Flags recent moves so physician liaisons can reach out first"],
     ["Affiliations", "ACO participation", "Change events"],
     "Your physician relations CRM", "g-cl-ic-gov-cut.webp", "#e8f3d2"),
    ("in-network-lookup", "Digital health", "Find a doctor who can actually see the patient",
     "A patient asks your app's assistant for a dermatologist.",
     "Find dermatologists within 10 miles who take this patient's plan and are accepting new patients.",
     ["Searches by specialty, location and the patient's plan",
      "Checks licenses and uses agent-verified availability",
      "Returns the practice's EHR so your app knows how to book"],
     ["Payer directories", "Licenses", "Agent verification", "EHR in use (ONC data)"],
     "Your app, through the API", "g-cl-ic-code-96.webp", "#fbe3ee"),
    ("ehr-campaign", "Health IT vendors", "Find every hospital on a given EHR",
     "You launch an integration for a specific EHR.",
     "List every hospital and large group running Oracle Health, with their IT leaders, and load them into HubSpot.",
     ["Finds organizations by the certified EHR they report using",
      "Adds the organization's leadership and locations",
      "Creates a HubSpot list for the campaign"],
     ["ONC certified health IT data", "EHR vendors' published customer lists", "Organizations", "Contacts"],
     "HubSpot or Salesforce", "g-cl-stk-agents-160.webp", "#f5efdf"),
]


def examples():
    items = [{"@type": "ListItem", "position": i + 1, "name": e[2], "url": f"{SITE}/examples#{e[0]}"} for i, e in enumerate(EXAMPLES)]
    h = head("Examples: What AI Agents Do With Stethos | Stethos",
             "Nine example workflows: medtech targeting, KOL mapping, directory accuracy, license watch, staffing, diligence, network mapping, in-network lookup, EHR lists.",
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
      <h1 id="ex-title">What agents do <span class="pop">with Stethos.</span></h1>
      <p class="kpi-lede">Nine workflows your team could run from the AI assistant and CRM it already uses. Each one shows the question, what the agent does, the data behind it and where the result lands. Names and numbers are examples.</p>
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
