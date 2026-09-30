#!/usr/bin/env python3
"""
Attach the recovered supplements for units 6, 7 and 9.

These files already exist on the branch under the OLD paper numbering
(paper1 / paper3 / paper5). Nothing is rewritten except the "Accompanies"
line, where the main text has since been retitled. No prose, mathematics or
data is altered.

Unit 7 uses v19 (unblinded), not v20 (blinded review copy), because unit 7's
main text is the unblinded v46.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

JOBS = [
    # (source file here, destination name, current main .tex, old accompany title)
    ('p1supp_v12.md',
     'paper06_assessment_separation_v67_supplementary.md',
     'paper06_assessment_separation_v67.tex',
     'Aggregate Indices and Transition Safety: A Quantifier-Order Separation '
     'Between Scalarized and Coordinate-Wise Feasibility.'),
    ('p5supp_v19.md',
     'paper08_governance_delay_v46_supplementary.md',
     'paper08_governance_delay_v46.tex',
     'The decision clock: review intervals as a design lever for stable '
     'resource governance.'),
    ('p3supp_v18.tex',
     'paper10_depletion_ledgers_v53_supplementary.tex',
     'paper10_depletion_ledgers_v53.tex',
     'Typed Flux Ledgers and Depletion Arithmetic: Conservation, '
     'Componentwise Diagnostics, and the Semantics of Depletion Horizons.'),
]


def main_title(path):
    s = io.open(path, encoding='utf-8', errors='replace').read()
    m = re.search(r'\\title\{(.*?)\}', s, re.S)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else None


ok = True
for srcname, dstname, mainname, oldtitle in JOBS:
    print('=' * 74)
    src = io.open(os.path.join(HERE, srcname), encoding='utf-8',
                  errors='replace').read()
    mainpath = os.path.join(OUT, mainname)
    title = main_title(mainpath)
    print('%s' % dstname)
    print('  from        : %s (%d B)' % (srcname, len(src)))
    print('  main title  : %s' % title)

    # Update the "Accompanies" line if the main text has been retitled.
    norm_old = re.sub(r'\s+', ' ', oldtitle).strip().rstrip('.')
    norm_new = (title or '').rstrip('.')
    if norm_old.lower() == norm_new.lower():
        print('  accompany   : already current (title matches)')
    else:
        # Replace only inside the *Accompanies: "..."* line.
        pat = re.compile(r'(\*?Accompanies:?\s*)(?:"|“)([^"”]+)(?:"|”)')
        m = pat.search(src)
        if not m:
            print('  accompany   : WARNING - no "Accompanies" line found; '
                  'left untouched')
            ok = False
        else:
            print('  accompany   : "%s"' % m.group(2))
            print('             -> "%s"' % norm_new + '.')
            src = src[:m.start(2)] + norm_new + '.' + src[m.end(2):]

    # Refer to the new main filename so the pairing is unambiguous.
    src = re.sub(r'Accompanies blinded main v\d+\.', '', src)

    dst = os.path.join(OUT, dstname)
    io.open(dst, 'w', encoding='utf-8').write(src)
    print('  written     : %d B' % len(src))

    # sanity
    strip = re.sub(r'(?<!\\)%.*$', '', src, flags=re.M)
    labs = set(re.findall(r'\\label\{([^}]*)\}', strip))
    refs = set(re.findall(r'\\ref\{([^}]*)\}', strip))
    dang = sorted(refs - labs)
    print('  braces      : { %d } %d  %s' % (src.count('{'), src.count('}'),
                                             'balanced'
                                             if src.count('{') == src.count('}')
                                             else 'UNBALANCED'))
    if dang:
        print('  dangling    : %s' % dang[:5])
    else:
        print('  dangling    : none (%d labels, %d refs)' % (len(labs), len(refs)))
    if src.count('{') != src.count('}'):
        ok = False

print('=' * 74)
print('RESULT: %s' % ('PASS' if ok else 'FAIL'))
sys.exit(0 if ok else 1)
