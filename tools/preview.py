# Makes preview/: a copy of public/ with relative links (for hosts without clean URLs).
import re, os, glob, shutil
ROOT = os.path.join(os.path.dirname(__file__), "..")
R = os.path.join(ROOT, "preview")
shutil.rmtree(R, ignore_errors=True)
shutil.copytree(os.path.join(ROOT, "public"), R)
for x in ("vercel.json",):
    p = os.path.join(R, x)
    if os.path.exists(p): os.remove(p)
pages = {'/': 'index.html', '/use-cases': 'use-cases.html', '/pricing': 'pricing.html', '/docs': 'docs.html', '/privacy': 'privacy.html', '/blog': 'blog/index.html'}
def target(path):
    base, _, frag = path.partition('#')
    if base == '' : t = 'index.html'
    elif base in pages: t = pages[base]
    elif base.startswith(('/compare/', '/blog/', '/solutions/')) and not os.path.splitext(base)[1]: t = base[1:] + '.html'
    else: t = base[1:]
    return t + ('#' + frag if frag else '')
for f in glob.glob(R + '/**/*.html', recursive=True):
    pre = '../' * os.path.relpath(f, R).count('/')
    s = open(f).read()
    s = re.sub(r'(href|src)=(["\'])(/[^"\']*)\2', lambda m: f'{m.group(1)}={m.group(2)}{pre}{target(m.group(3))}{m.group(2)}', s)
    s = re.sub(r'(srcset|imagesrcset)="([^"]*)"', lambda m: f'{m.group(1)}="' + re.sub(r'(^|, )/', lambda k: k.group(1) + pre, m.group(2)) + '"', s)
    open(f, 'w').write(s)
for f in glob.glob(R + '/*.css'):
    s = open(f).read().replace('url(/fonts/', 'url(fonts/').replace('url(/img/', 'url(img/'); open(f, 'w').write(s)
