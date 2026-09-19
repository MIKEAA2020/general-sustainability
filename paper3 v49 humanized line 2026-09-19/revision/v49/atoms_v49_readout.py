#!/usr/bin/env python3
"""For each §1 candidate, show v49's nearest sentence so a human can judge proposition vs paraphrase."""
import json
import pathlib
import re

R = pathlib.Path('/home/user')
D = R / 'revision/v49'
V7 = R / 'revision/v7'
GENERIC = set('''because therefore however whether which those that these with without within from into
over under above below itself themselves something anything nothing someone anyone each every both
either neither other others same such only just even also than then there here when where while during
since until against toward towards regarding including included include includes point points issue
issues case cases sense senses thing things way ways fact facts form forms kind kinds make makes making
made take takes taken give gives given use uses used using base based paper papers section sections
article articles result results number numbers quantity quantities question questions claim claims'''.split())


def stem(w):
    for suf in ('ies', 'es', 's', 'ing', 'edly', 'ed', 'ly', 'ment', 'tion', 'ation', 'ity'):
        if len(w) - len(suf) >= 4 and w.endswith(suf):
            return w[:-len(suf)]
    return w


def words(s):
    return {stem(w.lower()) for w in re.findall(r"[A-Za-z][A-Za-z\-']{4,}", s) if w.lower() not in GENERIC}


def nums(s):
    return set('#' + n for n in re.findall(r'\d[\d,]*(?:\.\d+)?(?!\d)', s))


def atoms(s):
    return words(s) | nums(s)


def sents(s):
    s = ' '.join(s.split())
    for a in (r'U\.S\.', r'et al\.', r'e\.g\.', r'i\.e\.', r'Vol\.', r'No\.'):
        s = re.sub(a, a.replace('.', '\u0001'), s)
    return [x.strip().replace('\u0001', '.') for x in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9*_(\[])', s) if len(x) > 30]


md49 = (V7 / 'paper3_material_ledgers_v49.md').read_text()
s49 = md49[md49.index('## 1. '):md49.index('## 2. ')]
V49S = sents(s49)
data = json.loads((D / 'v49_section1_atoms.json').read_text())['candidates']
print(f'{len(data)} candidates\n')
rows = []
for c in data:
    a = atoms(c['sentence'])
    best, bs = None, 0.0
    for t in V49S:
        ta = atoms(t)
        j = len(a & ta) / max(1, len(a | ta))
        if j > bs:
            bs, best = j, t
    rows.append((c, bs, best))
rows.sort(key=lambda x: -x[1])
for c, bs, best in rows:
    print('=' * 100)
    print(f"[{c['from']}] atom jaccard with v49's nearest §1 sentence = {round(bs, 2)} "
          f"| §1 coverage {c['coverage_of_v49_section_1']}")
    print('  EARLIER:', c['sentence'][:200])
    print('  v49 NEAR:', (best or '(no sentence above zero overlap)')[:200])
    print('  missing :', ', '.join(c['atoms_absent_from_all_of_v49'][:10]))
    if c['of_which_in_the_deposit']:
        print('  deposit :', ', '.join(x for x in c['of_which_in_the_deposit'][:10]))
lo = [c for c, bs, b in rows if bs < 0.12]
print('=' * 100)
print(f'\n{len(lo)} of {len(rows)} have essentially no counterpart in v49 §1 (jaccard < .12)')
json.dump([{'from': c['from'], 'coverage': c['coverage_of_v49_section_1'], 'jaccard': round(bs, 3),
            'sentence': c['sentence'], 'nearest': (b or '')[:200],
            'missing': c['atoms_absent_from_all_of_v49'], 'deposit': c['of_which_in_the_deposit']}
           for c, bs, b in rows], (D / 'v49_section1_readout.json').open('w'), indent=1)
