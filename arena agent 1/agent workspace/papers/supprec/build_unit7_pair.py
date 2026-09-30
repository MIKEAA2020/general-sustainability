#!/usr/bin/env python3
"""Unit 7 is a merge (PAPER_MERGE_08_07): paper08 delay + paper07 sampled
governance. Each lineage has its own supplement, and unit 7 cites sections
from both. Emit one clearly-named file per lineage."""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
MAIN = os.path.join(OUT, 'paper08_governance_delay_v46.tex')

def title_of(p):
    s = io.open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'\\title\{(.*?)\}', s, re.S)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''

mt = title_of(MAIN)

JOBS = [
    # source, dest, old accompany title, what it carries
    ('p5supp_v19.md',
     'paper08_governance_delay_v46_supplementary_governance.md',
     'The decision clock: review intervals as a design lever for stable '
     'resource governance.',
     'sampled-governance lineage (old paper5): S1-S13.3, incl. S13.1-S13.3'),
    ('p4supp_v8.md',
     'paper08_governance_delay_v46_supplementary_delay.md',
     'Governance delay and the stability of harvested stocks: mobilising and '
     'protective feedback rules, and the review interval as a design parameter.',
     'delay-dynamics lineage (old paper4): S1-S12, incl. S9.5 (G5)'),
]

ok = True
for srcname, dstname, oldtitle, note in JOBS:
    src = io.open(os.path.join(HERE, srcname), encoding='utf-8',
                  errors='replace').read()
    pat = re.compile(r'(\*?Accompanies:?\s*)(?:"|“)([^"”]+)(?:"|”)')
    m = pat.search(src)
    if m:
        src = src[:m.start(2)] + mt + '.' + src[m.end(2):]
    # make the merge provenance explicit at the top
    banner = ('<!-- Unit 7 is a merge (paper08 delay + paper07 sampled '
              'governance). This is the %s.\n     Both files are required: '
              'the main text cites sections from each. -->\n\n' % note)
    src = banner + src
    dst = os.path.join(OUT, dstname)
    io.open(dst, 'w', encoding='utf-8').write(src)
    bal = src.count('{') == src.count('}')
    ok &= bal
    print('%s' % dstname)
    print('   %-56s %d B  braces %s' % (note, len(src),
                                        'OK' if bal else 'UNBALANCED'))
print('\nRESULT: %s' % ('PASS' if ok else 'FAIL'))
