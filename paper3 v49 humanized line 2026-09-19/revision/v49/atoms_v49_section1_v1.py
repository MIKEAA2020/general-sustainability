#!/usr/bin/env python3
"""Section 1 read, second instrument: coverage by content atoms, not by string similarity.

The sentence-similarity read reported 0 of v48's 134 §1 sentences as verbatim, which is true (the
adaptation rewrote §1) and useless: a paraphrase of the same proposition scores 0.45 and looks like a
loss. So compare what a sentence is *about*. Each sentence contributes atoms - its numbers, its
citations, and its rare content words - and coverage is the share of those atoms present in v49's §1.
A reworded sentence keeps its atoms; a condensed-away one loses a distinctive one. Atoms missing from
all of v49 are the real candidates, and whether the deposit carries them decides whether the material
is legitimate (the source's) or v48's own addition (the author's earlier line, free to drop).
"""
import json
import pathlib
import re

R = pathlib.Path('/home/user')
V7 = R / 'revision/v7'
D = R / 'revision/v49'
DEP = R / 'work/paper3.txt'
GENERIC = set('''because therefore however whether which those this that these with without within from
into over under above below itself themselves something anything nothing someone anyone each every
both either neither other others same such only just even also than then there here when where while
during since until against toward towards regarding including included include includes point points
issue issues case cases sense senses thing things way ways fact facts form forms kind kinds make makes
making made take takes taken give gives given use uses used using base based paper papers section
sections section's article articles result results number numbers quantity quantities question
questions claim claims claims'''.split())


def region(text, head, nxt):
    i = text.index(head)
    return text[i:text.index(nxt, i)]


def sents(s):
    s = ' '.join(s.split())
    for a in (r'U\.S\.', r'et al\.', r'e\.g\.', r'i\.e\.', r'Vol\.', r'No\.'):
        s = re.sub(a, a.replace('.', '\u0001'), s)
    out = [x.strip().replace('\u0001', '.') for x in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9*_(\[])', s)]
    return [x for x in out if len(x) > 30]


def stem(w):
    """a deliberately crude ending-strip, and it is here because the first run of this check called
    `passenger` a lost atom next to a v49 sentence reading `ten passengers`, and `rated` lost beside
    `engineered ... for` - morphology noise on the scale of the real findings is not acceptable"""
    for suf in ('ies', 'es', 's', 'ing', 'edly', 'ed', 'ly', 'ment', 'tion', 'ation', 'ity', 'ies'):
        if len(w) - len(suf) >= 4 and w.endswith(suf):
            return w[:-len(suf)]
    return w


def words(s):
    return {stem(w.lower()) for w in re.findall(r"[A-Za-z][A-Za-z\-']{4,}", s) if w.lower() not in GENERIC}


def nums(s):
    return set(re.findall(r'\d[\d,]*(?:\.\d+)?(?!\d)', s))


def cites(s):
    out = set()
    for m in re.finditer(r'\(([^)]{3,200})\)', s):
        for part in m.group(1).split(';'):
            mm = re.search(r"([A-Z][A-Za-z\-\u2019'.]{2,})[^;()]*?\b((?:1[89]|20)\d\d)", part)
            if mm:
                out.add(mm.group(2))
    return out


def atoms(s):
    return words(s) | {f'#{n}' for n in nums(s)} | {f'@{c}' for c in cites(s)}


md49 = (V7 / 'paper3_material_ledgers_v49.md').read_text()
md48 = (V7 / 'paper3_material_ledgers_v48.md').read_text()
md42 = (V7 / 'paper3_material_ledgers_v42.md').read_text()
dep = DEP.read_text() if DEP.exists() else ''
s49 = region(md49, '## 1. ', '## 2. ')
A49 = set().union(*[atoms(x) for x in sents(s49)]) if sents(s49) else set()
ALL49 = atoms(md49)
DEPA = atoms(dep)
out = {}
cands = []
for tag, src in (('v48', md48), ('v42', md42)):
    try:
        sec = region(src, '## 1. ', '## 2. ')
    except ValueError:
        continue
    ss = sents(sec)
    lo, hi = 0, 0
    for s in ss:
        a = atoms(s)
        if not a:
            continue
        cov = len(a & A49) / len(a)
        if cov >= 0.5:
            hi += 1
            continue
        lo += 1
        miss = sorted(a - ALL49)                     # atoms nowhere in v49, not just not in §1
        if not miss:
            continue
        cands.append({'from': tag, 'coverage_of_v49_section_1': round(cov, 2),
                      'atoms_absent_from_all_of_v49': miss[:12],
                      'of_which_in_the_deposit': sorted(x for x in miss
                                                        if (x.startswith('#') or x.startswith('@')
                                                            or x.strip('#@') in DEPA))[:12],
                      'sentence': s[:220]})
    out[tag] = {'sentences': len(ss), 'atoms_covered_at_or_above_half': hi, 'below_half': lo}
out['v49_section_1_atoms'] = len(A49)
out['candidates_with_atoms_nowhere_in_v49'] = len(cands)
print(json.dumps(out, indent=1))
print(f'\n{len(cands)} sentences lose distinctive atoms document-wide; '
      f'{sum(1 for c in cands if c["of_which_in_the_deposit"])} of them lose an atom the DEPOSIT carries')
for c in sorted(cands, key=lambda x: (-len(x['of_which_in_the_deposit']), x['coverage_of_v49_section_1']))[:16]:
    print(f'\n [{c["from"]}] coverage {c["coverage_of_v49_section_1"]}')
    print('   ', c['sentence'][:190])
    print('    atoms nowhere in v49:', ', '.join(c['atoms_absent_from_all_of_v49'][:12]))
    if c['of_which_in_the_deposit']:
        print('    DEPOSIT-carried   :', ', '.join(c['of_which_in_the_deposit'][:12]))
(D / 'v49_section1_atoms.json').write_text(json.dumps({'summary': out, 'candidates': cands}, indent=1))
