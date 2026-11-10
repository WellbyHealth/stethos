from parts import *
from segments import BY as SEGBY, SCENE_ALT, scene, seg_tabs, logo
from page_other import UC
import page_examples as PX
import json

# Extra copy for one landing page per use case: (seo title, meta description, H1 a, H1 b, intro, example request, FAQs)
UC_PAGES = {
    "medtech": dict(
        title="Surgeon and Physician Data for Medtech Sales | Stethos",
        desc="Find surgeons by specialty, procedure focus, affiliation and license, and get alerts when targets move. Provider data for medtech sales teams and agents.",
        h1a="Surgeon and physician data", h1b="for medtech sales agents.",
        intro="Reach the right surgeon at the right moment: when they join a new group, start at a new facility or take over a service line. Stethos is built to keep a current record for every target and tell your agents the week it changes.",
        req={"specialty": "orthopedic surgery", "state": "AZ", "affiliation_type": "independent_group", "fields": ["affiliations", "practice_contact", "industry_payments"]},
        faq=[("Can I filter physicians by procedure focus?", "Search filters include specialty and sub-specialty, practice setting, affiliation and license state. Procedure-focus signals come from sources such as CMS data and practice websites, and each one shows its source."),
             ("Does it include Open Payments data?", "Yes. Enrich can add an Open Payments summary for a physician as an optional field, so your team can see existing industry relationships before reaching out."),
             ("Can it update our CRM automatically?", "Watchers send a webhook when a target's affiliation, location or license changes, so your CRM or agent can update the record and queue outreach without anyone re-checking lists.")]),
    "pharma": dict(
        title="Prescriber and KOL Data for Pharma Teams | Stethos",
        desc="Find prescribers by drug class and volume, map key opinion leaders, and get alerts when they move. Provider data for pharma commercial and medical teams.",
        h1a="Prescriber and KOL data", h1b="for pharma and life sciences.",
        intro="Launches depend on reaching the right prescribers and experts. Stethos is built to rank prescribers by Medicare Part D volume, map key opinion leaders and their work, and tell your teams when someone moves.",
        req={"specialty": "endocrinology", "state": "OH", "fields": ["part_d_volume", "affiliations", "publications", "industry_payments"], "limit": 25},
        faq=[("Where does prescribing data come from?", "From CMS's Medicare Part D Prescribers files, which report prescriptions by clinician and drug each year. Stethos matches each row to the right NPI and shows the release year on every number."),
             ("Can it map key opinion leaders?", "Stethos is built to add publications, clinical trials and NIH grants to a physician's record, next to affiliations and Open Payments, so medical affairs can see who leads in a therapeutic area."),
             ("Is there patient data?", "No. Part D data is aggregated to the prescriber, and CMS suppresses small counts. Stethos holds no patient records.")]),
    "health-it-sales": dict(
        title="Health System Data for Health IT and Services Sales | Stethos",
        desc="Target health systems and practices by EHR, size and service line, find the right buyer, and get alerts on new leaders and new sites, for AI sales agents.",
        h1a="Health system data for", h1b="health IT and services sales.",
        intro="Know which systems run which EHR, who owns the budget and when a leader changes. Stethos is built to give your reps, agents and CRM a current record for every health system and group, and flag the week something moves.",
        req={"org_type": "health_system", "state": "OH", "fields": ["locations", "health_it", "executives", "affiliates"]},
        faq=[("Can I filter health systems by EHR?", "Where it's published, yes. Certified health IT use comes from ONC and CMS sources, and each value shows its source and date. Where no source exists, the field is left empty rather than guessed."),
             ("Does it include executive contacts?", "Stethos returns named executives and service line leaders from sources such as organization websites and press releases, with the source for each. It doesn't sell personal emails or phone numbers."),
             ("Will it work in Salesforce or HubSpot?", "Yes. Your agent calls Stethos tools and writes the results into your CRM, and watchers can send a webhook when an account changes so the record and next step update on their own.")]),
    "healthcare-marketing": dict(
        title="Clinician and Account Data for Healthcare Marketing | Stethos",
        desc="Build clinician audiences and account lists for campaigns, events and ABM, and keep them clean as people change jobs. Current, sourced healthcare data.",
        h1a="Audience and account data for", h1b="healthcare marketing.",
        intro="Campaigns fail when the list is stale: the surgeon moved, the clinic closed, the group was bought. Stethos is built to give you current, sourced audiences of clinicians and organizations, and tell you when someone on a list changes jobs.",
        req={"specialty": "cardiology", "state": ["NY", "NJ"], "practice_setting": "hospital_employed", "fields": ["affiliations", "practice_contact"]},
        faq=[("Can I build an ABM account list?", "Yes. Search organizations by type, size, location and service lines, then pull the clinicians and leaders at each account, with who works where."),
             ("How do I keep lists up to date?", "Set a watcher on a list. When a contact changes employer or a practice closes or moves, Stethos sends a webhook so your CRM or marketing tool can update the record."),
             ("Is this patient data?", "No. Stethos only covers clinicians and organizations in their professional capacity, never patients.")]),
    "post-acute": dict(
        title="Referral Data for Home Care, Hospice and Post-Acute | Stethos",
        desc="More referrers than your marketers can cover? Rank the ones worth working, get nudged when one goes quiet, and map your network against the market.",
        h1a="More referrers than", h1b="your marketers can cover.",
        intro="New clients come from referrers, and there are more in your market than your team can work. Stethos is built to rank the referrers worth working, remind each marketer who has gone quiet and show which offices you're missing. A spreadsheet is enough; no CRM needed.",
        req={"match": "referrers.csv", "county": ["Dallas, TX", "Collin, TX"], "fields": ["affiliations", "practice_contact", "org_size", "post_acute_referrals"]},
        faq=[("We don't have a CRM. Does it still work?", "Yes. Upload a spreadsheet of your referrers, or export the list from your EHR or agency software, and Stethos matches each one to a current record. Results come back as a list, a weekly email or a spreadsheet; a CRM is optional."),
             ("We're private pay. Is the referral data still useful?", "The Medicare data shows which physicians order home health and hospice, which is a strong sign they refer patients who need care at home, whoever pays. The rest, such as practices, hospitals, affiliations and contact details, applies to any agency."),
             ("Can it help with big medical centers?", "Yes. Large academic and hospital campuses are broken down by department, practice and location, with who works where, so a marketer can see which parts of a campus they already know and which they haven't reached."),
             ("Where does referral data come from?", "From CMS data, such as Medicare home health, hospice and skilled nursing data, and physician utilization files, plus practice and organization records. Each value shows its source and date. No patient-level data is included.")]),
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
             ("Does it show ownership?", "Yes. Parent and child organizations are linked where sources show the relationship, and private equity owners are linked to the practices, clinics and facilities they own, with the source on each link. See <a href=\"/private-equity-healthcare-ownership-data\">private equity ownership data</a>."),
             ("Can I get the data as a file?", "Yes. Enterprise includes flat files delivered to your warehouse on a schedule, alongside the API.")]),
    "digital-health": dict(
        title="Healthcare Data for Startups and Digital Health | Stethos",
        desc="Find first customers and design partners, size your market and power provider search in your product, with one NPI-keyed API and MCP server.",
        h1a="Healthcare data for", h1b="startups and digital health.",
        intro="Find-a-doctor, referral and care navigation features all need the same thing underneath: a current, searchable record of who practices where and which networks they're in. Stethos is built to be that layer, through a REST API for your app and an MCP server for your agents.",
        req={"specialty": "dermatology", "city": "Austin", "state": "TX", "network": "[Payer A]", "limit": 10},
        faq=[("Can my AI agent use Stethos directly?", "Yes. The MCP server exposes search, enrich, organization and recent-changes tools to Claude and other MCP clients."),
             ("Is it HIPAA-covered data?", "No. Stethos holds provider and organization data only, with no patient information, so you can use it without a business associate agreement."),
             ("How do I keep my app's listings fresh?", "Create a watcher for the providers your app shows. When one changes location, network or license, you get a webhook and can update the listing.")]),
    "health-systems": dict(
        title="Physician Relations Data for Health Systems | Stethos",
        desc="Map community physicians, their affiliations and Medicare volume around your hospitals, and alert physician liaisons when a doctor moves or joins a competitor.",
        h1a="Physician relations data", h1b="for health systems.",
        intro="Physician liaisons grow referrals one office at a time. Stethos is built to map the community physicians around your hospitals, show who is affiliated with you or a competitor, and flag the doctors worth a visit this week.",
        req={"specialty": "cardiology", "city": "Nashville", "state": "TN", "fields": ["affiliations", "aco", "medicare_volume"], "limit": 25},
        faq=[("Can I see which physicians refer to us?", "Not from claims yet. Claims-level referral flows need CMS's research data environment, which Stethos plans to apply for. Today Stethos uses group, hospital and ACO ties, which explain much of who refers to whom, plus Medicare volume."),
             ("Does it work with our physician relations CRM?", "Yes. Enrich and watch through the API or MCP server, and send changes to your CRM with webhooks."),
             ("Is there patient data?", "No. Stethos holds data about clinicians and organizations only.")])
}


EX_ART = {"clinical-staffing": ("r-staffing", "Illustration: the little clay robot with a clipboard outside a hospital, beside a calendar and a stack of clinician badges."),
          "digital-health": ("r-digital", "Illustration: the little clay robot next to a big phone showing a heart and map pins, with a small rocket lifting off."),
          "health-systems": ("s-referral", "Illustration: envelopes with hearts flying from a clay hospital to a home-care house along a dotted arc."),
          "medtech": ("s-physician", "Illustration: a clay doctor's coat and stethoscope on a coat stand, beside index cards and a map pin."),
          "investors": ("s-pe", "Illustration: the little clay robot with a magnifying glass over a regional map where clinics in each cluster share a flag color, linked to matching briefcases."),
          "health-it-sales": ("s-healthsys", "Illustration: a clay hospital on a hill linked by roads to smaller clinics around it.")}


def ex_art(slug):
    a = EX_ART.get(slug)
    if not a:
        return ""
    return (f'<figure class="ex-art"><img src="/img/g-art-{a[0]}-900.webp" srcset="/img/g-art-{a[0]}-900.webp 900w, /img/g-art-{a[0]}-1600.webp 1600w" '
            f'sizes="(max-width: 820px) 100vw, 540px" width="1600" height="1195" alt="{a[1]}" loading="lazy" decoding="async"></figure>')


def uc_page(n):
    slug, color, icon, art_key, name, does, src, watch = UC[n]
    m = UC_PAGES[slug]
    path = f"/use-cases/{slug}"
    faqld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in m["faq"]]}
    h = head(m["title"], m["desc"], path, image=f"/og/{slug}.jpg", image_alt=f"Illustration for {name}",
             crumbs=[("Solutions", "/use-cases"), (name, path)], schema=[faqld])
    req = json.dumps(m["req"], indent=2)
    ep = "orgs/enrich" if slug == "investors" else ("providers/enrich" if "npi" in m["req"] else "providers/search")
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in m["faq"])
    others = "".join(f'<li><a href="/use-cases/{o[0]}">{logo(o[0], 64)}<span>{o[4]}</span></a></li>' for o in UC if o[0] != slug)
    alt = {"uc-medtech": "Illustration: a clay sales desk with a surgical instrument case, a knee model and a laptop showing a map with pins.",
           "uc-payer": "Illustration: a clay clipboard directory of doctors' offices with check marks, beside an insurance shield and a magnifying glass.",
           "uc-staffing": "Illustration: clay scrubs on a hanger rack, a stethoscope, a calendar and a small state map with glowing pins.",
           "uc-investors": "Illustration: a clay piggy bank beside a rising bar chart with tiny clinics on top of each bar.",
           "uc-digital": "Illustration: a clay smartphone showing a map of doctor pins, with a small clay robot leaning on it.",
           "compare": "Illustration: clay stacks of boxes and binders on a table beside a small machine sending out envelopes and pins.",
           "notfound": "Illustration: a clay folded map with a dotted path leading to a map pin, beside a magnifying glass.",
           "cta": "Illustration: a clay shelf of hospitals, clinics and houses with glowing map pins above them, and a small clay robot."}.get(art_key, f"Illustration for {name}")
    wfs = PX.for_page(slug) or [PX._by[x] for x in {"healthcare-marketing": ["abm-list", "ehr-campaign", "event-invites"]}.get(slug, [])]
    wf = (f'''<section class="sec" aria-labelledby="uc-wf-title">
  <div class="wrap">
    <div class="head"><p class="eyebrow"><span>Workflows</span></p><h2 id="uc-wf-title">What teams <span class="pop">do with it.</span></h2></div>
    <div class="ex-list">{"".join(PX.card(e, tab=None, link=False) for e in wfs)}{ex_art(slug) if len(wfs) % 2 else ""}</div>
    <p class="cov-note ex-more"><a href="/use-cases">See workflows for every segment <span aria-hidden="true">→</span></a></p>
  </div>
</section>
''' if wfs else "")
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top ph-top" aria-labelledby="uc-title">
  <div class="wrap">
    <nav class="crumbs uc-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/use-cases">Solutions</a> / {name}</nav>
    {seg_tabs(slug)}
    <div class="head ph seg-head">{logo(slug, 88, "seg-hero-logo")}
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
{scene(SEGBY[slug][5], SCENE_ALT[SEGBY[slug][5]])}
{wf}<section class="sec" aria-labelledby="uc-call-title">
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
    <div class="head"><p class="eyebrow"><span>FAQ</span></p><h2 id="uc-faq-title">{name}: common questions</h2><p class="faq-more">Something else? <a href="mailto:{EMAIL}?subject=Stethos%20{name.replace(" ", "%20")}">Email our team</a>.</p><figure class="faq-art"><img src="/img/g-art-r-faq-900.webp" width="900" height="672" alt="Illustration: the little clay robot sitting on a stack of books, thinking, next to a question mark and a lightbulb." loading="lazy" decoding="async"></figure></div>
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
