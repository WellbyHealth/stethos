# One entry per customer type: slug, name, one-liner, logo, tint, wide scene.
SEG = [
    ("medtech", "Medtech", "Reach surgeons the week they move.", "l-medtech", "#e4f0fd", "w-uc-medtech"),
    ("pharma", "Pharma and life sciences", "Map prescribers and KOLs for a launch.", "l-pharma", "#e3f4ec", "w-uc-pharma"),
    ("health-it-sales", "Health IT and services", "Sell to systems by EHR, size and leader.", "l-healthit", "#ece6fb", "w-uc-healthit"),
    ("healthcare-marketing", "Healthcare marketing", "Clinician audiences that stay current.", "l-marketing", "#fde8dc", "w-uc-marketing"),
    ("investors", "Investors and PE", "Roll-ups, headcount and new sites.", "l-investors", "#fbe4ea", "w-uc-investors"),
    ("digital-health", "Healthcare startups", "First customers and provider search.", "l-startups", "#e4f0fd", "w-uc-digital"),
    ("post-acute", "Post-acute care", "Rank referrers and see who's gone quiet.", "l-postacute", "#fdf5d2", "w-uc-postacute"),
    ("clinical-staffing", "Clinical staffing", "Licensed clinicians and who's hiring.", "l-staffing", "#e3f4ec", "w-uc-staffing"),
    ("provider-directories", "Payers and directories", "Keep every listing accurate.", "l-directories", "#ece6fb", "w-uc-directories"),
    ("health-systems", "Health systems", "Physician relations and network growth.", "l-healthsystems", "#fbe4ea", "w-uc-healthsystems"),
]
BY = {s[0]: s for s in SEG}

SCENE_ALT = {
    "w-uc-medtech": "Illustration: the little clay robot riding a delivery van with a device box from a surgery center toward a cluster of clinics.",
    "w-uc-pharma": "Illustration: a clay pharma lab with a flask on its roof, giant pill capsules on the meadow and paths to clinics, with the robot carrying a sample case.",
    "w-uc-healthit": "Illustration: small hospitals across clay hills connected by glowing cables to a server tower, with the robot adjusting a dial.",
    "w-uc-marketing": "Illustration: hot air balloons with envelope baskets over a town of clinics, with the robot dropping envelopes.",
    "w-uc-investors": "Illustration: tiny clinic buildings growing in rows like plants, with the robot watering them beside a piggy bank.",
    "w-uc-digital": "Illustration: a phone-shaped building with a heart on its screen and the robot riding a small rocket.",
    "w-uc-postacute": "Illustration: a hospital on a hill with dotted paths down to cozy homes with hearts on their roofs.",
    "w-uc-staffing": "Illustration: a hospital with hiring flags in its windows and a line of clinician badges on the path, with the robot holding a clipboard.",
    "w-uc-directories": "Illustration: a giant open directory book with pop-up clinics, and the robot moving a pin with a big pencil.",
    "w-uc-healthsystems": "Illustration: a hospital on a hill sending a little car to visit physician offices, with the robot holding a gift basket.",
}


def logo(slug, size=160, cls="seg-logo"):
    s = BY[slug]
    return f'<img class="{cls}" src="/img/g-{s[3]}-{"320" if size > 80 else "160"}.webp" width="{size}" height="{size}" alt="" loading="lazy" decoding="async">'


def scene(name, alt, eager=False):
    lz = '' if eager else ' loading="lazy"'
    return (f'<figure class="scene-band"><img src="/img/g-{name}-1600.webp" srcset="/img/g-{name}-900.webp 900w, /img/g-{name}-1600.webp 1600w" '
            f'sizes="100vw" width="1600" height="686" alt="{alt}"{lz} decoding="async"></figure>')


def seg_tabs(active=None):
    items = "".join(
        f'<li><a href="/use-cases/{s[0]}" style="--t:{s[4]}"{" aria-current=\"page\"" if s[0] == active else ""}>{logo(s[0], 40)}<span>{s[1]}</span></a></li>'
        for s in SEG)
    return f'<nav class="seg-tabs" aria-label="Solutions by team"><ul>{items}</ul></nav>'


def seg_grid():
    return '<ul class="seg-grid">' + "".join(
        f'<li><a href="/use-cases/{s[0]}" style="--t:{s[4]}">{logo(s[0], 72)}<span class="sg-t"><b>{s[1]}</b><span>{s[2]}</span></span></a></li>'
        for s in SEG) + '</ul>'


def ih_art(name, alt, src=None):
    """Contained 4:3 scene for the right side of an interior page hero."""
    if src is None:
        src = (f'/img/g-wc-{name}-1200.webp', f'/img/g-wc-{name}-700.webp 700w, /img/g-wc-{name}-1200.webp 1200w', 1200, 900)
    s, ss, w, h = src
    return (f'<figure class="ih-art"><img src="{s}" srcset="{ss}" sizes="(max-width: 900px) 100vw, 560px" width="{w}" height="{h}" '
            f'alt="{alt}" fetchpriority="high" decoding="async"></figure>')
