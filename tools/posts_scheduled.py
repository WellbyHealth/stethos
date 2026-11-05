# Scheduled guides. The build publishes a post only once its date (US Pacific) has arrived.
SCHEDULED = [
    dict(slug="how-to-look-up-an-npi-number", tag="Public data", art="uc-digital", date="2026-11-10", nice="November 10, 2026", mins=4,
         title="How to look up an NPI number, and what to do with it", seo="How to Look Up an NPI Number", kw="NPI lookup, NPI number, NPPES",
         desc="Three ways to look up an NPI number, what each result tells you, and how to check that the record is still current before you act on it.",
         alt="Illustration: a clay smartphone showing a map of doctor pins, with a small clay robot leaning on it.",
         take=["The NPPES NPI Registry is free to search by name, NPI or location.", "A registry match confirms identity, not where someone practices today.", "Check the last-updated date and confirm with a second source before acting."],
         body='''<p>Every US healthcare provider who bills electronically has a National Provider Identifier, a 10-digit number issued through CMS. Looking one up is easy. Knowing whether what you found is still true takes a little more.</p>
<h2>Three ways to look up an NPI</h2>
<ul>
<li><strong>The NPI Registry website.</strong> CMS runs a free public search of NPPES. You can search by NPI, by name, or by location and taxonomy.</li>
<li><strong>The NPI Registry API.</strong> The same data is available through a free public API, which is handy for one-off lookups from code.</li>
<li><strong>The full NPPES download.</strong> CMS publishes the whole registry as a downloadable file, updated regularly, if you want every record in your own database.</li>
</ul>
<h2>What a result tells you</h2>
<p>A registry record gives you the provider's name and credential, whether the NPI belongs to an individual or an organization, their taxonomy codes, a mailing address, a primary practice location and phone number, and the dates the record was created and last updated.</p>
<h2>What to check before you act on it</h2>
<p>Registry data is self-reported, so look at the last-updated date first. A record untouched for years may still show an old practice. If you're about to call, mail or route a patient, confirm the location against a second source: the practice's own website, a hospital directory, or the state licensing board.</p>
<h2>Doing this at scale</h2>
<p>Checking one NPI by hand is fine. Checking thousands every week isn't. That's the job an <a href="/npi-lookup-api">NPI lookup API</a> like Stethos is built for: it starts from the NPI and returns licenses, affiliations and networks, each with a source and verified date. For background on the registry itself, see <a href="/blog/what-the-npi-registry-can-and-cant-tell-you">what the NPI registry can and can't tell you</a>.</p>'''),
    dict(slug="type-1-vs-type-2-npi", tag="Public data", art="uc-investors", date="2026-11-17", nice="November 17, 2026", mins=4,
         title="Type 1 vs Type 2 NPI: what's the difference?", seo="Type 1 vs Type 2 NPI: What's the Difference?", kw="Type 1 NPI, Type 2 NPI, organization NPI",
         desc="Type 1 NPIs identify individual clinicians and Type 2 NPIs identify organizations. Here's how they differ and why it matters when you join provider data.",
         alt="Illustration: a clay piggy bank beside a rising bar chart with tiny clinics on top of each bar.",
         take=["Type 1 is a person. Type 2 is an organization.", "An individual has one NPI for life; an organization can have several.", "Linking Type 1 to Type 2 records is what tells you who works where."],
         body='''<p>NPIs come in two kinds, and mixing them up is one of the most common mistakes in provider data.</p>
<h2>Type 1: individuals</h2>
<p>A Type 1 NPI belongs to a single person: a physician, nurse practitioner, therapist, dentist or other clinician. Each person can have only one, and it stays with them when they change jobs, move states or change their name.</p>
<h2>Type 2: organizations</h2>
<p>A Type 2 NPI belongs to an organization, such as a hospital, group practice, home health agency, pharmacy or lab. Organizations can obtain separate NPIs for subparts, so one health system may hold many Type 2 numbers for different facilities or service lines.</p>
<h2>Why the difference matters</h2>
<ul>
<li><strong>Counting.</strong> Counting NPIs at a health system mixes people and buildings unless you separate the two types.</li>
<li><strong>Contacting.</strong> A Type 2 record's phone number reaches an organization, not a specific clinician.</li>
<li><strong>Linking.</strong> The registry doesn't link Type 1 and Type 2 records to each other. Knowing which clinicians work at which organization takes other sources, such as CMS enrollment data, hospital rosters and practice websites.</li>
</ul>
<h2>Putting them together</h2>
<p>The useful picture is the link between the two: this physician, at these organizations, since these dates. That's what a <a href="/health-system-data-api">health system data API</a> is built to maintain, and what lets you answer questions like "who are the cardiologists at this hospital this month?"</p>'''),
    dict(slug="medical-license-verification-across-states", tag="Licensing", art="uc-staffing", date="2026-11-24", nice="November 24, 2026", mins=5,
         title="How medical license lookups work across 50 states", seo="How Medical License Lookups Work Across States", kw="medical license lookup, license verification, state medical board",
         desc="Every state licenses clinicians separately. Where license records live, why they are hard to track across states, and when you need primary source verification.",
         alt="Illustration: clay scrubs on a hanger rack, a stethoscope, a calendar and a small state map with glowing pins.",
         take=["Licenses are issued state by state, by separate boards.", "Many clinicians hold licenses in several states, and each can change independently.", "For credentialing, verify at the primary source. For monitoring, watch for changes."],
         body='''<p>There is no single national medical license in the US. Each state licenses the clinicians who practice there, through its own boards, and keeps its own records.</p>
<h2>Where license records live</h2>
<p>Physicians are licensed by state medical boards, and some states have separate boards for osteopathic physicians. Nurses are licensed by state boards of nursing. Most boards offer a public lookup on their website, though the fields, formats and update schedules vary from state to state.</p>
<p>A few national services pull records together for specific professions, such as the Federation of State Medical Boards for physicians and Nursys for nurses, and many organizations use them during credentialing.</p>
<h2>Why it's hard to track</h2>
<ul>
<li>Many clinicians hold licenses in several states, especially in telehealth and locum work.</li>
<li>Each license renews, expires or picks up restrictions on its own schedule.</li>
<li>Interstate compacts make it easier to get licensed in more states, which means more licenses to keep track of.</li>
</ul>
<h2>Verification vs monitoring</h2>
<p>When you credential a clinician, you verify each license at the primary source, or through a credentials verification organization. That's a formal process with its own rules.</p>
<p>Day-to-day work is different. A staffing platform wants to know who is licensed in Texas right now. A directory team wants to know when a listed clinician's license lapses. That's monitoring, and it's what a <a href="/license-verification-api">license data API</a> with change events is built for. See how it fits <a href="/use-cases/clinical-staffing">clinical staffing and recruiting</a>.</p>'''),
    dict(slug="why-physician-affiliations-are-hard-to-track", tag="Data quality", art="uc-medtech", date="2026-12-01", nice="December 1, 2026", mins=4,
         title="Why physician affiliations are so hard to track", seo="Why Physician Affiliations Are Hard to Track", kw="physician affiliations, physician data, hospital affiliations",
         desc="Knowing which hospitals and groups a physician works with is the most useful fact in provider data, and the hardest to keep current. Here's why.",
         alt="Illustration: a clay sales desk with a surgical instrument case, a knee model and a laptop showing a map with pins.",
         take=["Affiliations change more often than identity, licenses or specialty.", "No single source has the full list of where a physician works.", "Combine sources and keep dates, so you know when each link was last seen."],
         body='''<p>Ask a medtech rep, a recruiter or a directory team what they most need to know about a physician, and the answer is usually the same: where do they work now?</p>
<h2>Why it changes so often</h2>
<ul>
<li>Physicians join and leave groups, often when groups are acquired or merge.</li>
<li>Many hold privileges at several hospitals and operate at outpatient centers too.</li>
<li>Part-time, locum and telehealth work adds affiliations that come and go.</li>
</ul>
<h2>Why no single source has it</h2>
<p>The NPI registry lists one primary practice location, and it's self-reported. CMS enrollment data connects clinicians to the organizations they bill through. Hospitals and groups publish their own directories. Each source sees part of the picture, on its own schedule.</p>
<h2>What a good affiliation record looks like</h2>
<p>A useful affiliation isn't just "Dr. Example works at Sample Medical Center." It says where that fact came from, when it was first seen and when it was last confirmed. With those dates, you can tell a current relationship from one that ended a year ago.</p>
<p>That's how the <a href="/physician-data-api">Stethos physician data API</a> is designed, with an <code>affiliation.changed</code> event when a link appears or disappears. Read how sales teams use it in <a href="/use-cases/medtech-pharma">medtech and pharma sales</a>.</p>'''),
    dict(slug="healthcare-provider-taxonomy-codes-explained", tag="Public data", art="problem", date="2026-12-08", nice="December 8, 2026", mins=4,
         title="Healthcare provider taxonomy codes, explained", seo="Healthcare Provider Taxonomy Codes Explained", kw="provider taxonomy codes, NUCC taxonomy, specialty codes",
         desc="Taxonomy codes describe a provider's type and specialty. Here's how the code set works, how it shows up in NPI records, and where it falls short.",
         alt="Illustration: a dusty clay filing cabinet, faded binders, a curling spreadsheet, returned envelopes and a map whose pins have fallen over.",
         take=["Taxonomy codes describe provider type, classification and specialization.", "Providers pick their own codes in NPPES and can list several.", "Codes are a starting point for specialty, not proof of what someone does day to day."],
         body='''<p>If you've filtered the NPI registry by specialty, you've used taxonomy codes, whether you knew it or not.</p>
<h2>What the code set is</h2>
<p>The Health Care Provider Taxonomy code set is maintained by the National Uniform Claim Committee and updated periodically. Each code is 10 characters long and describes a provider in up to three levels: a grouping such as allopathic and osteopathic physicians, a classification such as internal medicine, and an optional area of specialization such as cardiovascular disease.</p>
<h2>How it shows up in NPI records</h2>
<p>When providers apply for or update an NPI, they choose one or more taxonomy codes and mark one as primary. Organizations do the same for the services they offer.</p>
<h2>Where it falls short</h2>
<ul>
<li><strong>Self-selected.</strong> Providers pick their own codes, and some pick broad ones.</li>
<li><strong>Rarely updated.</strong> A physician who has narrowed their practice may never change their codes.</li>
<li><strong>Not procedures.</strong> A code says "orthopedic surgery", not "mostly spine" or "mostly sports medicine".</li>
</ul>
<h2>Using codes well</h2>
<p>Treat taxonomy as the first filter, then refine with other signals, such as group affiliation, practice website descriptions and public billing data. For more on the registry these codes live in, read <a href="/blog/how-to-look-up-an-npi-number">how to look up an NPI number</a>.</p>'''),
    dict(slug="webhooks-vs-polling-for-provider-data", tag="Engineering", art="compare", date="2026-12-15", nice="December 15, 2026", mins=4,
         title="Webhooks vs polling for provider data changes", seo="Webhooks vs Polling for Provider Data Changes", kw="webhooks, provider data changes, API polling",
         desc="Should your app poll for provider data changes or subscribe to webhooks? The trade-offs in freshness, cost and complexity, and when each makes sense.",
         alt="Illustration: a dusty stack of sealed boxes and reports on one side, and a clay data machine sending out a stream of alerts on the other.",
         take=["Polling is simple but slow and wasteful at scale.", "Webhooks tell you only what changed, as soon as it's seen.", "Most teams use both: webhooks for changes, a periodic check as a safety net."],
         body='''<p>Once you've loaded provider records into your product, the hard part starts: keeping them current. There are two basic ways to do it.</p>
<h2>Polling</h2>
<p>Polling means re-fetching records on a schedule and comparing them with what you have. It's easy to build and easy to reason about. The cost shows up at scale: if you track 50,000 clinicians and re-check each one weekly, you make 50,000 calls a week to find the few hundred that changed, and a change can sit unnoticed for days.</p>
<h2>Webhooks</h2>
<p>With webhooks, you register the records you care about and the data provider calls your endpoint when one changes. You only process real changes, and you hear about them as soon as they're seen. The trade-off is a little more engineering: a public endpoint, signature checks, and retries when your service is down.</p>
<h2>What most teams do</h2>
<ul>
<li>Subscribe to webhooks for the changes that drive action, such as a moved physician or a lapsed license.</li>
<li>Run a light periodic check, monthly for example, as a safety net for anything missed.</li>
<li>Store the change history, so you can answer "what changed this quarter?" later.</li>
</ul>
<h2>With Stethos</h2>
<p>Stethos watchers are built for this pattern: signed webhooks, retries for 24 hours, and a change history endpoint for backfills. See <a href="/docs#watch">watchers in the docs</a> and the <a href="/pricing">credit cost per event</a>.</p>'''),
]
