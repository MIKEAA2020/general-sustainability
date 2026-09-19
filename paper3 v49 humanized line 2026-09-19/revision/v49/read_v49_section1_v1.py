#!/usr/bin/env python3
"""Read Section 1 line by line against every earlier surface, for lost or condensed material.

Section 1 and the front matter are the region this build took from the author's adaptation instead of
from v48, and a *rewrite* is where legitimate content goes missing quietly: nothing is deleted, a
sentence is tightened, and a qualifier or a number disappears with it. A provenance check cannot see
that (the line is "adapt-identical", which is true and unhelpful), so this reads §1 against v48's §1,
v42's §1 and the deposited article, sentence by sentence, and asks of every element:

  present in an earlier §1, absent from v49's §1, and supported by the deposit  ->  a loss to explain

Qualifiers matter as much as numbers: "is not a forecast", "only if", "under declared assumptions" are
the sentences that carry the paper's honesty, and a compression that drops one turns a claim into an
overclaim. Every finding names the earlier sentence, the element that went, and whether the removal is
already on record (the waiver, the disposition, the term-revert list, the errata) or not.
"""
import difflib
import json
import pathlib
import re

R = pathlib.Path('/home/user')
V7 = R / 'revision/v7'
D = R / 'revision/v49'
V48 = R / 'revision/v48'
DEP = R / 'work/paper3.txt'
ABBREV = r'U\.S\.|No\.|cf\.|e\.g\.|i\.e\.|Sec\.|Vol\.|et al\.'


def region(text, head, nxt):
    i = text.index(head)
    j = text.index(nxt, i)
    return text[i:j]


def sents(s):
    """sentences, keeping their inline citations and numbers intact"""
    s = re.sub(r'\s+', ' ', s)
    for a in ABBREV.split('|'):
        s = re.sub(a, a.replace('.', '\u0001'), s)
    out = [x.strip().replace('\u0001', '.') for x in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9*_(\[])', s)]
    return [x for x in out if len(x) > 28]


def norm(s):
    return ' '.join(re.sub(r"[^0-9A-Za-z\u2019'\- ]", ' ', s.lower()).split())


def nums(s):
    return set(re.findall(r'\d[\d,]*(?:\.\d+)?(?!\d)', s))


def cites(s):
    out = set()
    for m in re.finditer(r'\(([^)]{3,200})\)', s):
        for part in m.group(1).split(';'):
            mm = re.search(r'([A-Z][A-Za-z\-\u2019\'.]{2,}[^;()]*?)\b((?:1[89]|20)\d\d)[a-z]?', part)
            if mm:
                out.add(norm(mm.group(1)).split()[0] + ' ' + mm.group(2))
    for mm in re.finditer(r"([A-Z][A-Za-z\-\u2019'.]{2,}(?:[ ,]+(?:and|&)?\s*[A-Z][A-Za-z\-\u2019'.]{2,})*)\s*\(\s*((?:1[89]|20)\d\d)", s):
        out.add(norm(mm.group(1)).split()[0] + ' ' + mm.group(2))
    return out


QUAL = (r'\bnot\b|\bno\b|\bonly\b|\bcannot\b|\bnever\b|\bunless\b|\bif\b|\bmay\b|\bmight\b|\bcan\b'
        r'|\bapproximat|\broughly\b|\bnearly\b|\bare\b|\bis\b|\bunder\b|\bassuming\b|\bwithin\b'
        r'|\bexactly\b|\bstrictly\b|\bfail(s|ure)?\b|\bguarantee[sd]?\b|\bverifi(?:ed|cation)\b'
        r'|\bcertificat\w*\b|\bnot\s+identified\b|\bno\s+claim\b|\bnot\s+a\s+forecast\b')


def quals(s):
    return set(m.group(0).lower() for m in re.finditer(QUAL, s))


md49 = (V7 / 'paper3_material_ledgers_v49.md').read_text()
md48 = (V7 / 'paper3_material_ledgers_v48.md').read_text()
md42 = (V7 / 'paper3_material_ledgers_v42.md').read_text()
dep = DEP.read_text() if DEP.exists() else ''
s49 = region(md49, '## 1. ', '## 2. ')
n49 = norm(s49)
nums49, cites49, quals49 = nums(s49), cites(s49), quals(s49)
# a logged-edit surface: anything these files name is accounted for, not silent
_edits = (D / 'v49_front_matter_edits.json').read_text() + (D / 'v49_carry_over.json').read_text() \
    + (D / 'adaptation_term_revert_v1.csv').read_text() + (V48 / 'ERRATA_v48.md').read_text() \
    + (D / 'disposition_v49.json').read_text()
_abol = [l.split(',')[0].strip() for l in (D / 'adaptation_term_revert_v1.csv').read_text().split('\n')[1:] if l.strip()]

report, findings = {}, []
for tag, md in (('v48', md48), ('v42', md42)):
    try:
        src = region(md, '## 1. ', '## 2. ')
    except ValueError:
        continue
    present = reworded = absent = 0
    for s in sents(src):
        ns = norm(s)
        best, br = None, 0.0
        for t in sents(s49):
            nt = norm(t)
            r = difflib.SequenceMatcher(None, ns, nt).ratio()
            if r > br:
                br, best, nt = r, t, nt
        if br >= 0.985:
            present += 1
            continue
        if br >= 0.62:
            reworded += 1
            lost_n = nums(s) - nums49
            lost_c = cites(s) - cites49
            lost_q = {q for q in quals(s) - quals49 if len(q) > 2}
            logged = all(x in _edits for x in (lost_q or []))
            if lost_n or lost_c or lost_q:
                findings.append({'kind': f'a {tag} §1 sentence survived reworded with elements dropped',
                                 'source_sentence': s[:190], 'nearest_v49': (best or '')[:190],
                                 'similarity': round(br, 3),
                                 'numerals_dropped': sorted(lost_n), 'citations_dropped': sorted(lost_c),
                                 'qualifiers_dropped': sorted(lost_q),
                                 'supported_by_the_deposit': bool(nums(s) and ns[:70] in norm(dep)),
                                 'dropped_elements_appear_in_the_logs': logged,
                                 'v48_only': tag == 'v48' and ns[:60] not in norm(dep)})
            continue
        absent += 1
        findings.append({'kind': f'a {tag} §1 sentence has no counterpart in v49 §1',
                         'source_sentence': s[:200], 'numerals': sorted(nums(s)),
                         'citations': sorted(cites(s)), 'supported_by_the_deposit': ns[:70] in norm(dep),
                         'named_in_the_logs': any(w and w in _edits for w in
                                                  [norm(s).split()[0], *sorted(cites(s))][:3])})
    report[tag] = {'sentences_in_that_§1': len(sents(src)), 'verbatim_in_v49': present,
                   'reworded_in_v49': reworded, 'no_counterpart': absent}

# and the reverse: v49 §1 material that no earlier surface carries
invented = []
for s in sents(s49):
    ns = norm(s)
    best = 0.0
    for other in (md48, dep):
        for t in sents(other):
            best = max(best, difflib.SequenceMatcher(None, ns, norm(t)).ratio())
            if best > 0.8:
                break
        if best > 0.8:
            break
    if best < 0.62:
        invented.append({'sentence': s[:170], 'best_similarity_to_v48_or_deposit': round(best, 2)})
report['v49_section_1_sentences_with_no_visible_source'] = invented[:12]
report['count'] = len(invented)
report['findings_total'] = len(findings)
print(json.dumps(report, indent=1)[:2400])
print(f'\nfindings: {len(findings)}')
for f in findings[:22]:
    print(' -', json.dumps(f)[:300])
(D / 'v49_section1_read.json').write_text(json.dumps({'report': report, 'findings': findings}, indent=1))
