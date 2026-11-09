from parts import *
import datetime as _dt
from zoneinfo import ZoneInfo as _Z
from posts_scheduled import SCHEDULED

POSTS = [
    dict(slug="what-the-npi-registry-can-and-cant-tell-you", tag="Public data", art="uc-payer", date="2026-11-05", nice="November 5, 2026", mins=5,
         title="What the NPI registry can and can't tell you", seo="What the NPI Registry Can and Can't Tell You", kw="NPI registry, NPPES, NPI lookup",
         desc="The NPPES NPI Registry is the backbone of US provider data. Here's what it reliably tells you, where it falls short, and what to pair it with.",
         alt="Illustration: a clay clipboard directory of doctors' offices with check marks, beside an insurance shield and a magnifying glass.",
         take=["The NPI is the one identifier almost every US provider record shares, so build on it.", "NPPES is self-reported and only as current as the provider's last update.", "Pair it with licensing, affiliation and network sources before an agent acts on it."],
         body='''<p>If you're building anything on US healthcare provider data, you'll meet the National Plan and Provider Enumeration System, or NPPES, on day one. It's the federal registry that issues National Provider Identifiers, and it's free to search and download. It's also easy to over-trust.</p>
<h2>What an NPI is</h2>
<p>An NPI is a 10-digit number that identifies a healthcare provider in standard transactions like claims. There are two kinds. Type 1 NPIs belong to individuals, such as physicians, nurse practitioners and therapists. Type 2 NPIs belong to organizations, such as hospitals, group practices, pharmacies and home health agencies. The number itself carries no meaning, and it's meant to stay with a provider for life.</p>
<p>That permanence is what makes it useful. Claims data, CRM records, credentialing files and payer directories can all be joined on the NPI, which is why it should be the key in your own data model too.</p>
<h2>What the registry tells you well</h2>
<ul>
<li><strong>Identity.</strong> Name, credential and whether the record is an individual or an organization.</li>
<li><strong>Taxonomy.</strong> The provider's self-selected specialty codes, including a primary one.</li>
<li><strong>Addresses.</strong> A mailing address and a primary practice location, with phone numbers.</li>
<li><strong>Status.</strong> When the NPI was issued, last updated, or deactivated.</li>
</ul>
<h2>Where it falls short</h2>
<p>The registry is self-reported. Providers are expected to update their information when it changes, but nothing forces the update to happen quickly, and many records lag behind reality. A physician who moved practices last year may still show the old address.</p>
<p>It also leaves out a lot of what commercial and clinical teams actually need:</p>
<ul>
<li>Which hospitals and groups a clinician is affiliated with today.</li>
<li>Which state licenses are active, expired or restricted.</li>
<li>Which payer networks a practice participates in.</li>
<li>Every location where a clinician actually sees patients, beyond the primary one.</li>
</ul>
<h2>What to pair it with</h2>
<p>Treat NPPES as the spine and attach other sources to it: state licensing boards for license status, CMS provider and facility data for affiliations and enrollment, payer directories for networks, and practice websites for where people work right now. Keep the source and date on every field you attach, so you can tell a fact checked yesterday from one that's three years old. That's the approach behind <a href="/docs#enrich">Stethos enrich</a>, which returns a source and verified date with every field.</p>
<p>That last part matters most if software is going to act on the data. An agent can't ask a colleague whether an address looks right. It needs the provenance in the record.</p>'''),
    dict(slug="why-provider-directories-go-stale", tag="Data quality", art="problem", date="2026-11-04", nice="November 4, 2026", mins=4,
         title="Why provider directories go stale, and what keeps them current", seo="Why Provider Directories Go Stale", kw="provider directory accuracy, provider data",
         desc="Provider directories drift out of date because clinicians move faster than the systems that track them. Here's where the errors come from and what helps.",
         alt="Illustration: a dusty clay filing cabinet, faded binders, a curling spreadsheet, returned envelopes and a map whose pins have fallen over.",
         take=["Directory errors come from many small, ordinary changes, not one big failure.", "Waiting for providers to report changes guarantees lag.", "Watching sources for changes beats re-verifying everything on a fixed schedule."],
         body='''<p>Anyone who has called a doctor's office from an insurance directory and reached the wrong practice knows the problem. Directories go stale, and they go stale for ordinary reasons.</p>
<h2>Where the errors come from</h2>
<ul>
<li><strong>Clinicians move.</strong> They join new groups, add a second location, cut back to part time or retire.</li>
<li><strong>Groups change.</strong> Practices merge, get acquired by health systems, rename themselves and consolidate phone lines.</li>
<li><strong>Networks change.</strong> Contracts start and end, and a practice can be in one plan's network and out of another's.</li>
<li><strong>Sources disagree.</strong> The registry, the practice website, the hospital's site and each payer's directory may all say something different.</li>
</ul>
<p>None of these is dramatic on its own. Together, across hundreds of thousands of clinicians, they add up to a directory that's never quite right.</p>
<h2>Why reporting alone doesn't fix it</h2>
<p>Most systems depend on providers telling them about changes. Busy practices don't always do that, and when they do, they tell one system, not every system. Federal rules now push health plans to verify directory information on a regular schedule, which helps, but a fixed schedule still leaves a gap between the change and the check.</p>
<h2>What keeps a directory current</h2>
<p>The teams that do this well flip the approach. Instead of re-checking everything on a calendar, they watch the sources that change first: practice websites, licensing boards, hospital rosters and job posts. When one of those sources moves, they re-verify that one record right away.</p>
<p>They also keep the evidence. A listing that says "verified at the practice website two days ago" is far more useful than one that just says "active." When sources conflict, they keep both and record which one won, so a reviewer, or an agent, can make the call. Read how Stethos is built for <a href="/use-cases/provider-directories">provider directory teams</a>, or start with <a href="/blog/what-the-npi-registry-can-and-cant-tell-you">what the NPI registry can and can't tell you</a>.</p>'''),
    dict(slug="giving-an-ai-agent-healthcare-data-checklist", tag="Agents", art="uc-digital", date="2026-11-03", nice="November 3, 2026", mins=4,
         title="Giving an AI agent healthcare data: a checklist", seo="Giving an AI Agent Healthcare Data: A Checklist", kw="AI agents, healthcare data, provider data API",
         desc="Before an AI agent acts on healthcare provider data, check freshness, provenance, identifiers, cost controls and patient privacy. A short checklist.",
         alt="Illustration: a clay smartphone showing a map of doctor pins, with a small clay robot leaning on it.",
         take=["Agents act on whatever data they're given, so stale data becomes wrong actions.", "Give agents provenance and dates so they can judge trust themselves.", "Keep patient data out of the loop unless you have the agreements to handle it."],
         body='''<p>An AI agent that books meetings, routes referrals or updates a directory will act on whatever provider data you hand it, confidently and at scale. That makes data quality a product decision, not a back-office one. Here's a short checklist to run before you connect the two.</p>
<h2>1. Is it fresh enough for the action?</h2>
<p>Looking someone up for a research summary can tolerate older data. Emailing a surgeon about a new device can't. Decide how recent each field needs to be for each action, and make sure the data carries a last-verified date the agent can read.</p>
<h2>2. Does every field say where it came from?</h2>
<p>An agent can't phone a colleague to ask whether an address looks right. Give it the source for each field and let it prefer stronger sources, or flag weak ones for a person to check.</p>
<h2>3. Is everything keyed on the NPI?</h2>
<p>Names collide and addresses change. The NPI is the one identifier shared across claims, CRMs and directories, so make it the key for every lookup and every write.</p>
<h2>4. Will it hear about changes?</h2>
<p>A list that was right when you pulled it starts going wrong the next day. Agents work best when they're told about changes, such as a move or a new license, instead of discovering them from a bounced email.</p>
<h2>5. Are costs bounded?</h2>
<p>Agents can make thousands of calls without anyone noticing. Use cheap searches to narrow the field before expensive enrichment, set budgets per task, and watch the credits each call reports.</p>
<h2>6. Is patient data out of the loop?</h2>
<p>Provider data, meaning who a clinician is and where they practice, is different from patient data. Keep the two separate unless you have the agreements and controls to handle protected health information, and make sure your agent's tools can't pull one into the other by accident.</p>
<p>Stethos is built around this checklist: NPI-keyed records with a source on every field, change events by webhook, per-call <a href="/pricing">credit pricing</a> and an <a href="/docs#mcp">MCP server</a> for agents, with no patient data.</p>'''),
]


TODAY = _dt.datetime.now(_Z("America/Los_Angeles")).date().isoformat()
import os as _os
TODAY = _os.environ.get("STETHOS_TODAY", TODAY)   # override to preview a later date
ALL_POSTS = POSTS + SCHEDULED
POSTS = sorted([p for p in ALL_POSTS if p["date"] <= TODAY], key=lambda p: p["date"], reverse=True)


def card(p, h="h3"):
    return (f'<li class="post-card"><a href="/blog/{p["slug"]}"><img src="/img/g-art-{p["art"]}-900.webp" srcset="/img/g-art-{p["art"]}-900.webp 900w, /img/g-art-{p["art"]}-1600.webp 1600w" sizes="(max-width: 700px) 100vw, 400px" width="1600" height="1195" alt="" loading="lazy" decoding="async">'
            f'<span class="pc-b"><span class="pc-tag">{p["tag"]}</span><{h}>{p["title"]}</{h}><span class="pc-p">{p["desc"]}</span><span class="pc-meta">{p["nice"]} · {p["mins"]} min read</span></span></a></li>')


def blog_index():
    h = head("Blog: Guides to Healthcare Provider Data | Stethos", "Plain-English guides to US healthcare provider data: the NPI registry, why provider directories go stale, and how to give AI agents healthcare data safely.", "/blog", crumbs=[("Blog", "/blog")])
    body = f'''{HEADER}
<main id="main">
  <div class="wrap blog-head ph-top"><div class="head ph"><h1>Guides for teams <span class="pop">selling into healthcare.</span></h1><p class="sp-lede">Plain-English guides on US healthcare provider data, where it comes from, how it goes wrong and how to put it to work.</p></div></div>
  <div class="wrap"><ul class="blog-grid">{"".join(card(p, "h2") for p in POSTS)}</ul></div>
</main>
'''
    return h + body + tail()


def post(p):
    import json
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["desc"], "datePublished": p["date"], "dateModified": p["date"], "keywords": p.get("kw", ""),
          "author": {"@type": "Organization", "name": BRAND}, "publisher": {"@type": "Organization", "name": BRAND, "logo": {"@type": "ImageObject", "url": SITE + "/icon-512.png"}},
          "image": f'{SITE}/og/{p["slug"]}.jpg', "mainEntityOfPage": f'{SITE}/blog/{p["slug"]}'}
    h = head(p.get("seo", p["title"]) + " | Stethos", p["desc"], f'/blog/{p["slug"]}', og_type="article", image=f'/og/{p["slug"]}.jpg', image_alt=p["alt"],
             crumbs=[("Blog", "/blog"), (p["title"], f'/blog/{p["slug"]}')],
             extra=f'<meta property="article:published_time" content="{p["date"]}">\n<meta property="article:section" content="{p["tag"]}">\n', ld=f'<script type="application/ld+json">{json.dumps(ld)}</script>\n')
    tk = "".join(f"<li>{t}</li>" for t in p["take"])
    others = "".join(card(o) for o in [x for x in POSTS if x is not p][:3])
    body = f'''{HEADER}
<main id="main" class="wrap doc">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/blog">Blog</a></nav>
  <p class="art-tag">{p["tag"]}</p>
  <h1>{p["title"]}</h1>
  <p class="doc-meta">By the Stethos team · <time datetime="{p["date"]}">{p["nice"]}</time> · {p["mins"]} min read</p>
  <figure class="art-cover"><img src="/img/g-art-{p["art"]}-1600.webp" srcset="/img/g-art-{p["art"]}-900.webp 900w, /img/g-art-{p["art"]}-1600.webp 1600w" sizes="(max-width: 800px) 100vw, 760px" width="1600" height="1195" alt="{p["alt"]}" fetchpriority="high"></figure>
  <aside class="takeaways" aria-label="Key takeaways"><h2>Key takeaways</h2><ul>{tk}</ul></aside>
  <article>
{p["body"]}
  </article>
  <section class="more-posts" aria-labelledby="more-title"><h2 id="more-title">More guides</h2><ul class="blog-grid">{others}</ul></section>
</main>
'''
    return h + body + tail()
