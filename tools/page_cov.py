from parts import *

COV_CATS = [
    ("identity", "Identity", "NPPES NPI Registry", "One NPI per clinician or organization, with taxonomy and practice address.", "Weekly", "Public"),
    ("licenses", "Licenses", "State licensing boards, 50 states + DC", "License status, expiry, discipline and nurse compact privileges.", "Varies by board", "Public"),
    ("affiliations", "Affiliations and organizations", "Care Compare, Provider of Services file, ACO participation, organization NPIs", "Who works where, group rosters, ownership and parent systems.", "Monthly to annual", "Public"),
    ("clinician-volume", "Clinician volume", "Medicare Physician &amp; Other Practitioners, Part D Prescribers, DMEPOS", "Procedures, Medicare patients, prescribing and equipment orders per clinician.", "Annual", "Public"),
    ("facility-volume", "Facility volume", "Medicare Inpatient &amp; Outpatient Hospitals, Post-Acute Care &amp; Hospice", "Discharges per hospital; volume and patient mix for home health, hospice, SNF, IRF and LTCH.", "Annual", "Public"),
    ("quality", "Quality and financials", "Care Compare star ratings and measures, hospital and SNF cost reports", "Ratings, quality scores, beds, staffing, revenue and costs.", "Monthly to quarterly", "Public"),
    ("payers", "Payers and networks", "Payer directories, price transparency files, Medicare Advantage enrollment", "Which plans each provider is in, negotiated rates and MA share by market.", "Monthly", "Public"),
    ("industry", "Industry relationships", "Open Payments", "Payments from drug and device makers to clinicians and teaching hospitals.", "Annual", "Public"),
    ("signals", "Live signals", "Practice websites, health system job posts", "New locations, moves, leadership changes and hiring spikes.", "Continuous", "Public"),
    ("verified", "Agent-verified", "Stethos voice and web agents", "Calls practices and checks websites to confirm address, phone, accepting patients and network participation when sources disagree or go stale.", "On change, and on a schedule", "Stethos agents"),
    ("claims", "Claims-level Medicare", "100% Medicare Part A, B and MA claims, via CMS VRDC", "Current referral flows, shared patients, discharge destinations and market share.", "Quarterly", "Planned"),
]

COV_UC = [
    ("Medtech and pharma sales", "/use-cases/medtech-pharma", "Which independent spine surgeons in Arizona do the most fusions, and who just changed groups?", ["H", "", "C", "C", "H", "", "H", "C", "C", "V", "C"]),
    ("Provider directories and payer networks", "/use-cases/provider-directories", "Which listings have a stale address, a lapsed license or a network mismatch?", ["C", "C", "C", "", "", "H", "C", "", "C", "C", ""]),
    ("Clinical staffing and recruiting", "/use-cases/clinical-staffing", "Which NPs hold licenses in these three states, and which systems are hiring hardest?", ["H", "C", "C", "", "", "", "", "", "C", "C", ""]),
    ("Healthcare investors and diligence", "/use-cases/investors", "Who owns every orthopedic group in this metro, how big is each, and what is its payer mix?", ["", "", "C", "H", "C", "C", "C", "H", "H", "V", "C"]),
    ("Post-acute business development", "/home-health-hospice-data-api", "Which hospices in this county are growing, and which hospitals discharge most to home health?", ["", "", "C", "H", "C", "C", "H", "", "H", "V", "C"]),
    ("Digital health and AI apps", "/use-cases/digital-health", "Is this doctor in-network for the patient's plan, licensed in their state and taking new patients?", ["C", "C", "C", "", "", "H", "C", "", "H", "C", ""]),
]

MARK = {
    "C": '<span class="cov-c" title="Core" aria-hidden="true">●</span><span class="sr">Core</span>',
    "H": '<span class="cov-h" title="Helpful" aria-hidden="true">○</span><span class="sr">Helpful</span>',
    "": '<span class="sr">Not needed</span>',
    "V": '<span class="cov-h" title="Helpful" aria-hidden="true">○</span><span class="sr">Helpful</span>',
}


def coverage():
    dataset = {"@type": "Dataset", "name": "Stethos healthcare provider data",
               "description": "US clinician and organization records resolved from NPPES, CMS Medicare files, state licensing boards, payer directories and web sources.",
               "creator": {"@type": "Organization", "name": BRAND}, "spatialCoverage": "United States",
               "variableMeasured": [c[1] for c in COV_CATS]}
    h = head("Healthcare Provider Data Coverage by Source | Stethos",
             "Eleven categories of US provider data, from NPPES and CMS Medicare files to licenses, payer networks and agent-verified fields, mapped to six use cases.",
             "/data-coverage", crumbs=[("Data coverage", "/data-coverage")], schema=[dataset])
    cards = ""
    for k, n, src, what, ref, st in COV_CATS:
        cls = "cov-card planned" if st == "Planned" else ("cov-card agent" if st == "Stethos agents" else "cov-card")
        cards += (f'<li class="{cls}" id="cat-{k}"><div class="cov-top"><h3>{n}</h3><span class="cov-st">{st}</span></div>'
                  f'<p>{what}</p><p class="cov-src"><b>Sources</b> {src}</p><p class="cov-ref"><b>Refresh</b> {ref}</p></li>')
    th = "".join(f'<th scope="col"><a href="#cat-{c[0]}">{c[1]}</a></th>' for c in COV_CATS)
    trs = ""
    for n, u, q, vals in COV_UC:
        trs += f'<tr><th scope="row"><a href="{u}">{n}</a><span class="cov-q">{q}</span></th>' + "".join(f"<td>{MARK[v]}</td>" for v in vals) + "</tr>"
    body = f'''{HEADER}
<main id="main">
<section class="sec sp-top cov" aria-labelledby="cov-title">
  <div class="wrap">
    <nav class="crumbs uc-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Data coverage</nav>
    <div class="head center">
      <p class="eyebrow"><span>Data coverage</span></p>
      <h1 id="cov-title">Eleven kinds of provider data, <span class="pop">one record per NPI.</span></h1>
      <p class="kpi-lede">Stethos is built on government files first: the NPI Registry, CMS Medicare files and state licensing boards. Payer, web and hiring signals are layered on top, and Stethos agents call practices and check websites to confirm what the files can't. Every field names its source and the date it was last checked.</p>
    </div>
    <h2 class="sr">Data categories</h2>
    <ul class="cov-grid">{cards}</ul>
    <p class="cov-note">Claims-level Medicare data needs CMS research access, which Stethos plans to apply for. Everything else comes from public files today. The full source list is in the <a href="/docs#sources">docs</a>.</p>
  </div>
</section>
<section class="sec" aria-labelledby="cov-uc-title">
  <div class="wrap">
    <div class="head center">
      <p class="eyebrow"><span>By use case</span></p>
      <h2 id="cov-uc-title">What each team <span class="pop">relies on most.</span></h2>
      <p class="kpi-lede cov-key"><span class="cov-c" aria-hidden="true">●</span> Core &nbsp;&nbsp; <span class="cov-h" aria-hidden="true">○</span> Helpful</p>
    </div>
    <div class="cov-wrap" tabindex="0" role="region" aria-label="Coverage by use case"><table class="cov-table"><thead><tr><th scope="col">Use case</th>{th}</tr></thead><tbody>{trs}</tbody></table></div>
  </div>
</section>
{cta_band("Self-serve", "Query all eleven categories", "from one MCP server.", "1,000 free credits, no card, no sales call. Pay only for the tool calls you make.", "data-coverage")}
</main>
'''
    return h + body + tail()
