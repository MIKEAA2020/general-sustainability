#!/usr/bin/env python3
"""
Recover unit 1's supplementary material from the v51 lineage.

paper01_obstruction_calculus_v63.tex carries 17 pointers to its own supplement
(S1, S2, S3, Figure~S1, Figure~S2) and no supplement was produced after v51.
The v51 supplement still fits: v51 main and v63 main contain identical sets of
21 claims by (environment type, statement name).

Changes applied here, and only these:
  1. Retitle to match v63 (v63's \title, not the v51-era title).
  2. Drop the author line (v63 carries no \author).
  3. Number the "Additional figures" section S1/S2/S3 so the main text's
     Figure~S1 (ladder) and Figure~S2 (obstruction tree) resolve. The fibre
     figure earlier in the document keeps ordinary numbering and therefore
     does not consume an S-slot.
Nothing else is touched: no prose, no mathematics, no labels.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'v51supp.tex')
DST = os.path.join(os.path.dirname(HERE),
                   'paper01_obstruction_calculus_v63_supplementary.tex')

src = io.open(SRC, encoding='utf-8', errors='replace').read()
orig = src
log = []


def sub1(pattern, repl, label, count=1):
    """Apply a replacement that must match, and record it."""
    global src
    n = src.count(pattern)
    if n != count:
        sys.exit('FAIL: %s expected %d match(es), found %d' % (label, count, n))
    src = src.replace(pattern, repl)
    log.append(label)


# 1. Title: match v63 ("Obstruction certificates under incomplete observation").
sub1(r'\title{Supplementary Material: An Obstruction Calculus for Viability '
     r'under Incomplete Observation}',
     r'\title{Supplementary Material: Obstruction certificates under '
     r'incomplete observation}',
     'title -> v63 wording')

# 2. Author: v63 has no \author.
sub1('\\author{Amin Abaee}\n', '', 'author line removed')

# 3. Figure numbering for the "Additional figures" section.
s4 = r'\section*{S4. Additional figures}'
sub1(s4,
     '%% The main text cites these figures as Figure~S1 (obstruction ladder) and\n'
     '%% Figure~S2 (obstruction tree), so number them in the S-series. The fibre\n'
     '%% figure earlier in this document keeps ordinary figure numbering and does\n'
     '%% not consume an S-slot.\n'
     '\\renewcommand{\\thefigure}{S\\arabic{figure}}%\n'
     '\\setcounter{figure}{0}%\n\n' + s4,
     'S-series figure numbering inserted before S4')

io.open(DST, 'w', encoding='utf-8').write(src)

# ---- verification -------------------------------------------------------
print('source : %s (%d B)' % (os.path.basename(SRC), len(orig)))
print('written: %s (%d B)' % (os.path.basename(DST), len(src)))
print('changes:')
for l in log:
    print('   - %s' % l)
print()

ok = True


def check(label, cond, detail=''):
    global ok
    print('  %-42s %s %s' % (label, 'OK  ' if cond else 'FAIL', detail))
    if not cond:
        ok = False


strip = re.sub(r'(?<!\\)%.*$', '', src, flags=re.M)

check('braces balanced',
      src.count('{') == src.count('}'),
      '{ %d } %d' % (src.count('{'), src.count('}')))

import collections
b = collections.Counter(re.findall(r'\\begin\{([a-zA-Z*]+)\}', strip))
e = collections.Counter(re.findall(r'\\end\{([a-zA-Z*]+)\}', strip))
unb = [k for k in set(b) | set(e) if b[k] != e[k]]
check('environments balanced', not unb, str(unb) if unb else '')

labs = set(re.findall(r'\\label\{([^}]*)\}', strip))
refs = set(re.findall(r'\\ref\{([^}]*)\}', strip))
dang = sorted(refs - labs)
check('no dangling \\ref', not dang, str(dang) if dang else '%d labels, %d refs'
      % (len(labs), len(refs)))

check('S1 complete proofs present',
      r'\section*{S1. Complete proofs}' in src)
check('selector principle proof present',
      'Complete proof of the selector principle' in src)
check('Figure~S1 source (ladder) present', 'fig_p2_ladder.png' in src)
check('Figure~S2 source (tree) present', 'fig_p2_obstruction_tree.png' in src)
check('thefigure reset present', src.count('renewcommand{\\thefigure}') == 1)
check('no author command left', '\\author' not in src)
check('title matches v63',
      'Obstruction certificates under incomplete observation' in src)

# every section the main text cites must exist
main = io.open(os.path.join(os.path.dirname(HERE),
                            'paper01_obstruction_calculus_v63.tex'),
               encoding='utf-8', errors='replace').read()
main = re.sub(r'(?<!\\)%.*$', '', main, flags=re.M)
cited = sorted(set(re.findall(
    r"[Ss]upplementary(?:'s)?\s+(?:[Mm]aterial\s*)?\(?\s*S(\d+(?:\.\d+)?)", main)),
    key=lambda x: [int(i) for i in x.split('.')])
have = set(re.findall(r'\\section\*\{S(\d+)\.', src))
missing = [c for c in cited if c not in have]
check('all cited S-sections present', not missing,
      'cited %s ; have S%s' % (','.join('S' + c for c in cited),
                               ','.join(sorted(have))))

figcited = len(re.findall(r'Figure~\s*S\d+', main))
check('cited Figure~S all numbered in S-series', figcited <= 3,
      '%d cited, 3 available (S1 ladder, S2 tree, S3 ce-trap)' % figcited)

print()
print('RESULT: %s' % ('PASS' if ok else 'FAIL'))
sys.exit(0 if ok else 1)
