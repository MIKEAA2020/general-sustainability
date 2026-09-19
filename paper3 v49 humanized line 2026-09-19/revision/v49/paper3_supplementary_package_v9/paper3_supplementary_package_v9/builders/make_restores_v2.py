#!/usr/bin/env python3
"""Rebuild v49_required_restores.json from the raw markdown of the alignment ancestor.

Why this file exists: the six restores were previously taken from a flattened dump of the earlier
line, and that dump had already destroyed the article's maths (`$\ell=\mathbf{1}$` had come out as
`M`) and run past paragraph boundaries. Two consequences shipped into v49: one restored sentence
repeated a sentence v48 already carried, and one crossed a horizontal rule into the next
paragraph. A restored claim is only as good as the bytes it was copied from.

The rule stated plainly:
  * the raw surface for inserted *text* is v42's markdown, because that is where `$...$` survives;
  * the deposited article stays the correctness oracle - the phrase must exist in it;
  * a whole donor sentence is inserted only when the target line carries no sentence like it;
    where v48 kept the sentence and dropped only its tail, the tail clause is extended onto it,
    verbatim from the same donor line, so no claim is duplicated;
  * every inserted string must be a verbatim substring of the donor line, or this script stops.
"""
import json
import pathlib
import re

V7 = pathlib.Path('/home/user/revision/v7')
D = pathlib.Path('/home/user/revision/v49')
v42 = (V7 / 'paper3_material_ledgers_v42.md').read_text()
dep = pathlib.Path('/home/user/work/paper3.txt').read_text()

DECLARED = [
    {'row': 'D0238', 'phrase': 'monomaterial projection', 'sec': '2.2', 'mode': 'append-sentence',
     'target_probe': 'Uptake', 'anchor_section': '2.2'},
    {'row': 'D0286', 'phrase': 'never in the stock', 'sec': '2.5', 'mode': 'extend-final-sentence',
     'target_probe': 'prevented inflow', 'clause_from': ' — routing it into product'},
    {'row': 'D0385', 'phrase': 'differentiated only by', 'sec': '4.3', 'mode': 'append-sentence',
     'target_probe': 'conservation lemma', 'anchor_section': '4.3'},
    {'row': 'D0521', 'phrase': 'replenished by recharge', 'sec': '6.5.1', 'mode': 'extend-final-sentence',
     'target_probe': 'access structure', 'clause_from': ': it draws on stored water'},
    {'row': 'D0719', 'phrase': 'two readings of one ledger', 'sec': '11', 'mode': 'append-sentence',
     'target_probe': 'closing statement', 'anchor_section': '11'},
    {'row': 'D0631', 'phrase': 'not a primitive of the closed natural block', 'sec': '2.5',
     'mode': 'extend-final-sentence', 'target_probe': 'extractor-side remark only',
     'clause_from': '; it is not a primitive of the closed natural block'},
]

L42 = v42.split('\n')
out, problems = [], []
for rec in DECLARED:
    ph = rec['phrase']
    hits = [k for k, l in enumerate(L42) if ph in l and not l.lstrip().startswith(('#', '|'))]
    if not hits:
        problems.append(f"{rec['row']}: phrase {ph!r} not found in a v42 prose line")
        continue
    li = hits[0]
    donor_line = L42[li]
    # the donor sentence: split the raw line on sentence-final punctuation, maths protected
    masked = re.sub(r'\$\$.*?\$\$|\$[^$]*\$', lambda m: '\x00' * len(m.group(0)), donor_line, flags=re.S)
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z*(\u201c])', masked)
    sent = None
    off = 0
    for p in parts:
        idx = donor_line.find(p, off)
        if idx < 0:
            idx = off
        if ph in p:
            sent = donor_line[idx:idx + len(p)].strip().lstrip('. ').strip()
            break
        off = idx + len(p)
    if not sent:
        problems.append(f"{rec['row']}: could not isolate the donor sentence")
        continue
    # a restored claim has to come from somewhere that is not this build: the deposited article
    # first, and failing that the previous shipped line (v47), which is the case where v48's own
    # repair pass dropped a sentence the author had published. Either way the source is recorded
    # per row rather than asserted in prose, because one of these six is exactly of the second kind
    v47 = (V7 / 'paper3_material_ledgers_v47.md').read_text()
    if ph in dep:
        rec_oracle = 'deposit'
    elif ph in v47:
        rec_oracle = 'v47 (the previous shipped line); the deposited article does not state it'
    else:
        problems.append(f"{rec['row']}: {ph!r} is in neither the deposited article nor v47, "
                        'so restoring it would be inventing it')
        continue
    if re.search(r'#{2,4}\s|\s---\s|^\$\$|\$\$$', sent) and rec['mode'] == 'append-sentence':
        problems.append(f"{rec['row']}: donor sentence crosses a heading or rule boundary: {sent[:80]!r}")
        continue
    if sent.count('$') % 2:
        problems.append(f"{rec['row']}: donor sentence has unbalanced $ - the split is wrong")
        continue
    item = {'row': rec['row'], 'phrase': ph, 'sec': rec['sec'], 'mode': rec['mode'],
            'target_probe': rec['target_probe'], 'donor': 'paper3_material_ledgers_v42.md',
            'donor_line': li + 1, 'donor_sentence': sent, 'oracle': rec_oracle,
            'note': 'verbatim from the donor line, maths intact; the deposit carries the phrase too'}
    if rec['mode'] == 'extend-final-sentence':
        k = sent.find(rec['clause_from'])
        if k < 0:
            problems.append(f"{rec['row']}: declared clause {rec['clause_from'][:40]!r} is not a "
                            'substring of the donor sentence')
            continue
        clause = sent[k:].rstrip()
        if clause.endswith('.') and not clause.endswith('..'):
            clause = clause[:-1]
        item['clause'] = clause
        item['clause_verbatim_in_donor_line'] = clause in donor_line
        if clause not in donor_line:
            problems.append(f"{rec['row']}: clause is not verbatim in the v42 line")
            continue
        # the clause must be genuinely missing from v48, or the "restore" is a duplicate
        md48 = (V7 / 'paper3_material_ledgers_v48.md').read_text()
        core = ' '.join(re.sub(r'[._;:,]', ' ', clause).split())[:60]
        if core and core in ' '.join(md48.split()):
            problems.append(f"{rec['row']}: the clause is already in v48 - not a loss, skip it")
            continue
    out.append(item)

(D / 'v49_required_restores.json').write_text(json.dumps(out, indent=1) + '\n')
rep = {'records': len(out), 'modes': {m: sum(1 for x in out if x['mode'] == m)
                                      for m in ('append-sentence', 'extend-final-sentence')},
       'sentences': [{'row': x['row'], 'mode': x['mode'], 'chars': len(x.get('clause', x['donor_sentence']))}
                     for x in out],
       'problems': problems}
(D / 'v49_restores_v2.json').write_text(json.dumps(rep, indent=1) + '\n')
for x in out:
    print(f"  {x['row']:7} {x['mode']:22} {len(x.get('clause', x['donor_sentence'])):4} chars  "
          f"{(x.get('clause') or x['donor_sentence'])[:78]}")
print(json.dumps(rep['problems'], indent=1)[:800])
raise SystemExit(1 if problems or len(out) != 6 else 0)
