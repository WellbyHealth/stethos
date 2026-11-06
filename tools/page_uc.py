from parts import *
from page_other import UC
import json

# Extra copy for one landing page per use case: (seo title, meta description, H1 a, H1 b, intro, example request, FAQs)
UC_PAGES = {
    "medtech-pharma": dict(
        title="Physician Data API for Medtech and Pharma Sales | Stethos",
        desc="Find surgeons and physicians by specialty, procedure focus, affiliation and license, and get alerts when targets move. A provider data API for sales agents.",
        h1a="Physician data for", h1b="medtech and pharma sales agents.",
        intro="Medtech and pharma reps win by reaching the right surgeon at the right moment: when they join a new group, start operating at a new facility or take over a service line. Stethos is built to give your sales agents and CRM a current record for every target, and to tell them the week something changes.",
        req={"specialty": "orthopedic surgery", "state": "AZ", "affiliation_type": "independent_group", "fields": ["affiliations", "practice_contact", "industry_payments"]},
        faq=[("Can I filter physicians by procedure focus?", "Search filters include specialty and sub-specialty, practice setting, affiliation and license state. Procedure-focus signals come from public sources such as CMS data and practice websites, and each one shows its source."),
             ("Does it include Open Payments data?", "Yes. Enrich can add an Open Payments summary for a physician as an optional field, so your team can see existing industry relationships before reaching out."),
             ("Can it update our CRM automatically?", "Watchers send a webhook when a target's affiliation, location or license changes, so your CRM or agent can update the record and queue outreach without anyone re-checking lists.")]),
    "health-it-sales": dict(
        title="Health System Data for Health IT and Services Sales | Stethos",
        desc="Target health systems and practices by EHR, size and service line, find the right buyer, and get alerts on new leaders and new sites, for AI sales agents.",
        h1a="Health system data for", h1b="health IT and services sales.",
        intro="Selling software or services into healthcare means knowing which systems run which EHR, who owns the budget and when something changes. Stethos is built to give your reps, SDR agents and CRM a current record for every health system and group, from ONC certified health IT data, CMS files and organization websites, and to flag the week a new executive starts or a practice joins a larger system.",
        req={"org_type": "health_system", "state": "OH", "fields": ["locations", "health_it", "executives", "affiliates"]},
        faq=[("Can I filter health systems by EHR?", "Where it's published, yes. Certified health IT use comes from ONC and CMS sources, and each value shows its source and date. Where no public source exists, the field is left empty rather than guessed."),
             ("Does it include executive contacts?", "Stethos returns named executives and service line leaders from public sources such as organization websites and press releases, with the source for each. It doesn't sell personal emails or phone numbers."),
             ("Will it work in Salesforce or HubSpot?", "Yes. Your agent calls Stethos tools and writes the results into your CRM, and watchers can send a webhook when an account changes so the record and next step update on their own.")]),
    "healthcare-marketing": dict(
        title="Clinician and Account Data for Healthcare Marketing | Stethos",
        desc="Build clinician audiences and account lists for campaigns, events and ABM, and keep them clean as people change jobs. Current, sourced healthcare data.",
        h1a="Audience and account data for", h1b="healthcare marketing.",
        intro="Healthcare campaigns go wrong when the list is stale: the surgeon moved, the clinic closed, the group was bought. Stethos is built to give your marketing team and its agents current audiences of clinicians and organizations by specialty, setting and market, each with sources, and to tell you when someone on a list changes employer.",
        req={"specialty": "cardiology", "state": ["NY", "NJ"], "practice_setting": "hospital_employed", "fields": ["affiliations", "practice_contact"]},
        faq=[("Can I build an ABM account list?", "Yes. Search organizations by type, size, location and service lines, then pull the clinicians and leaders at each account, with who works where."),
             ("How do I keep lists up to date?", "Set a watcher on a list. When a contact changes employer or a practice closes or moves, Stethos sends a webhook so your CRM or marketing tool can update the record."),
             ("Is this patient data?", "No. Stethos only covers clinicians and organizations in their professional capacity, never patients.")]),
    "provider-directories": dict(
        title="Provider Directory Data API for Payers | Stethos",
        desc="Check provider directory listings against current sources. Flag stale locations, lapsed licenses and network mismatches with a real-time provider data API.",
        h1a="Keep provider directories", h1b="accurate, every week.",
        intro="Directory listings drift out of date because clinicians move, groups merge and networks change faster than anyone reports it. Stethos is built to check each listing against current sources, show where they disagree, and alert your team when a listed clinician changes location, license or network.",
        req={"npi": "1234567890", "fields": ["practice_contact", "licenses", "networks"]},
        faq=[("How does Stethos help with directory accuracy?", "Each listing can be compared with current sources: practice websites, state boards, CMS data and other payer directories. Every field shows its source and last-verified date, and conflicts are returned rather than hidden."),
             ("Can it replace calling practices?", "It's built to cut down how many you need to call. Change events and source conflicts point your team at the listings most likely to be wrong, instead of re-verifying everyone on a fixed schedule."),
             ("Does it include patient data?", "No. Stethos only holds information about clinicians and organizations in their professional capacity.")]),
    "clinical-staffing": dict(
        title="Clinician and License Data API for Staffing | Stethos",
        desc="Source licensed clinicians by state and specialty, and spot health systems that are hiring. A real-time clinician data API for staffing platforms.",
        h1a="Clinician and license data for", h1b="staffing and recruiting.",
        intro="Recruiters need two things fast: clinicians who are licensed where the job is, and employers who are hiring now. Stethos is built to give your recruiting platform and agents both, from state boards, employer rosters and health system job posts.",
        req={"specialty": "registered nurse", "license_state": "TX", "fields": ["licenses", "affiliations"]},
        faq=[("Which licenses are covered?", "State licenses for physicians, nurses and other clinicians, with status and source, gathered from state licensing boards. Coverage will be published by state and profession at launch."),
             ("Can I see which organizations are hiring?", "Organization records include open clinical roles, and the org.hiring_spike event fires when an organization's postings rise well above its normal level."),
             ("Can I find clinicians who just got a new license?", "Yes. The license.issued event fires when a new state license appears for a clinician you watch, or you can query recent license events by state.")]),
    "investors": dict(
        title="Healthcare Practice Data for Investors | Stethos",
        desc="Track practice roll-ups, clinician headcount and new locations as they happen. Real-time healthcare organization data for investors and corporate development.",
        h1a="Healthcare market signals for", h1b="investors, as they happen.",
        intro="In healthcare services, the leading indicators are clinicians and locations: who is joining a platform, where new sites are opening and which groups are losing people. Stethos is built to turn those changes into events you can track across a portfolio or a target list.",
        req={"name": "Example Ortho Partners", "state": "AZ", "fields": ["children", "rostered_clinicians", "locations"]},
        faq=[("Can I track clinician headcount over time?", "Organization records include rostered clinicians, and change history shows who joined and left and when, so you can chart headcount for a group or platform."),
             ("Does it show ownership?", "Parent and child organizations are linked where public sources show the relationship, with the source on each link."),
             ("Can I get the data as a file?", "Yes. Enterprise includes flat files delivered to your warehouse on a schedule, alongside the API.")]),
    "digital-health": dict(
        title="Provider Search API for Digital Health Apps | Stethos",
        desc="Power provider search, referrals and scheduling in your app with one NPI-keyed API, and let AI agents look up any clinician over MCP.",
        h1a="Provider search for", h1b="digital health and AI apps.",
        intro="Find-a-doctor, referral and care navigation features all need the same thing underneath: a current, searchable record of who practices where and which networks they're in. Stethos is built to be that layer, through a REST API for your app and an MCP server for your agents.",
        req={"specialty": "dermatology", "city": "Austin", "state": "TX", "network": "[Payer A]", "limit": 10},
        faq=[("Can my AI agent use Stethos directly?", "Yes. The MCP server exposes search, enrich, organization and recent-changes tools to Claude and other MCP clients."),
             ("Is it HIPAA-covered data?", "No. Stethos holds provider and organization data only, with no patient information, so you can use it without a business associate agreement."),
             ("How do I keep my app's listings fresh?", "Create a watcher for the providers your app shows. When one changes location, network or license, you get a webhook and can update the listing.")]),
}


def uc_page(n):
    slug, color, icon, art_key, name, does, src, watch = UC[n]
    m = UC_PAGES[slug]
    path = f"/use-cases/{slug}"
    faqld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in m["faq"]]}
    h = head(m["title"], m["desc"], path, image=f"/og/{slug}.jpg", image_alt=f"Illustration for {name}",
             crumbs=[("Use cases", "/use-cases"), (name, path)], schema=[faqld])
    req = json.dumps(m["req"], indent=2)
    ep = "orgs/enrich" if slug == "investors" else ("providers/enrich" if "npi" in m["req"] else "providers/search")
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in m["faq"])
    others = "".join(f'<li><a href="/use-cases/{o[0]}"><img src="/img/{o[2]}" width="160" height="160" alt="" loading="lazy" decoding="async"><span>{o[4]}</span></a></li>' for o in UC if o[0] != slug)
    alt = {"uc-medtech": "Illustration: a clay sales desk with a surgical instrument case, a knee model and a laptop showing a map with pins.",
           "uc-payer": "Illustration: a clay clipboard directory of doctors' offices with check marks, beside an insurance shield and a magnifying glass.",
           "uc-staffing": "Illustration: clay scrubs on a hanger rack, a stethoscope, a calendar and a small state map with glowing pins.",
           "uc-investors": "Illustration: a clay piggy bank beside a rising bar chart with tiny clinics on top of each bar.",
           "uc-digital": "Illustration: a clay smartphone showing a map of doctor pins, with a small clay robot leaning on it.",
           "cta": "Illustration: a clay shelf of hospitals, clinics and houses with glowing map pins above them, and a small clay robot."}[art_key]
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top ph-top" aria-labelledby="uc-title">
  <div class="wrap">
    <nav class="crumbs uc-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/use-cases">Use cases</a> / {name}</nav>
    <div class="head ph">
      <h1 id="uc-title">{m["h1a"]} <span class="pop">{m["h1b"]}</span></h1>
      <p class="sp-lede">{m["intro"]}</p>
    </div>
    <div class="sp-panels uc-one"><div class="sp-panel {color}"><div class="sp-p-main">
      <figure class="sp-scene"><img fetchpriority="high" src="/img/g-art-{art_key}-900.webp" srcset="/img/g-art-{art_key}-900.webp 900w, /img/g-art-{art_key}-1600.webp 1600w" sizes="(max-width: 980px) 100vw, 560px" width="1600" height="1195" alt="{alt}" decoding="async"></figure>
      <h2>{name}</h2><p class="sp-k">Stethos is built to</p><p class="sp-do">{does}</p></div>
      <div class="sp-p-side"><p class="sp-k">Data you'd use</p><ul class="sp-src">{"".join(f"<li>{x}</li>" for x in src)}</ul>
      <p class="sp-k">Signals you'd watch</p><ul class="sp-see">{"".join(f"<li>{x}</li>" for x in watch)}</ul></div></div></div>
  </div>
</section>
<section class="sec" aria-labelledby="uc-call-title">
  <div class="wrap uc-call">
    <div><p class="eyebrow"><span>Example call</span></p><h2 id="uc-call-title">What it looks like <span class="pop">in code.</span></h2>
    <p class="uc-call-p">One request against the Stethos API. Responses carry the source and last-verified date on every field. See the <a href="/docs">quickstart</a> for authentication, watchers and the MCP server, and <a href="/pricing">pricing</a> for what each call costs.</p></div>
<pre class="uc-code" tabindex="0" aria-label="Example request"><code>curl https://api.stethos.health/v1/{ep} \\
  -H "Authorization: Bearer $STETHOS_KEY" \\
  -d '{req}'</code></pre>
  </div>
</section>
<section class="sec" aria-labelledby="uc-faq-title">
  <div class="wrap faq-grid">
    <div class="head"><p class="eyebrow"><span>FAQ</span></p><h2 id="uc-faq-title">{name}: common questions</h2><p class="faq-more">Something else? <a href="mailto:{EMAIL}?subject=Stethos%20{name.replace(" ", "%20")}">Email our team</a>.</p></div>
    <div class="qs">{faq}</div>
  </div>
</section>
<section class="sec" aria-labelledby="uc-more-title">
  <div class="wrap"><h2 id="uc-more-title" class="uc-more-h">More use cases</h2><ul class="uc-more">{others}</ul></div>
</section>
{cta_band("Free credits", "Try it on", "your own targets.", "Get a key, run your first search in minutes, and pay only for the data you use.", "Stethos%20" + slug)}
</main>
'''
    return h + body + tail()
