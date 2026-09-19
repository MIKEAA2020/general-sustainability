#!/usr/bin/env python3
r"""Notation identity: which reused sentences would ship a symbol the deposited article uses for something else.

The audit read words and cleared 296 of the 306. The notation drill (`v48_notation_drift_v1.py`) then went through
the same sentences' inline `$...$` and found 31 spans with no counterpart in the deposited article in any spelling.
Read one by one, most were the draft re-typesetting the same object - a hat widened, a QED glyph swapped, a label
moved from below a symbol to above it. A minority were not. They are the rows below, and each one was checked
against the deposited article's own use of the glyph, quoted as evidence:

  S^{\top}              the draft calls the typed stoichiometric operator `S^{\top}` (30 times) where the
                        deposited article defines and uses `S_{\mathcal{T}}` (46 times) and says why:
                        "the $S_{\mathcal{T}}$ carries the subscript for that reason". Plain `S` in the
                        deposited article is the moiety readout ($S_m = c_m^{\top}x$), so the rename is not cosmetic.
  \mathsf{S},\mathsf{K}  the draft sans-seriffs the §2.4 state; the deposited article reserves sans-serif for the
                        hybrid incidence matrix (`\dot\chi = \mathsf{S}\eta + b`, `\mathsf{L}^{\top}\mathsf{S}=0`)
                        and for the certification predicates.
  S\eta                 the reverse direction, in the same conditional theorem: the draft dropped the sans-serif
                        from the hypothesis, so the two matrices become one letter.
  \mathcal{A}           the deposited article's `A^{\mathrm{win}}_{\min}` barrier becomes `\mathcal A^{\mathrm{win}}_{\min}`
                        in the draft - and `\mathcal A` is the adequacy functional of §8 ("let $\mathcal A:\mathbb
                        R^{n}\to\mathbb R$ be monotone").
  \mathcal{B}           the draft's biomass barrier `\mathcal B_{\mathrm{lim}}` renders identically to the deposited
                        article's attainable-balance domain `\mathcal{B}(x,t)`.
  \mathcal{H}           the draft decorates the horizon quantities (`\mathcal H^{\mathrm{loc}}_A`); the deposited
                        article writes `H_A^{\mathrm{loc}}` and never uses `\mathcal H` at all.

Nothing here edits a document. It writes `v48_reuse_findings.{md,csv,json}` and
`v48_overrules_notation_candidate.csv`, which the author accepts, edits or deletes.
"""
import csv
import json
import re

V48 = '/home/user/revision/v48'
DEPOSIT = '/home/user/revision/v7/paper3_material_ledgers_v42.md'
DRAFT = '/home/user/humanized/v1/paper3_humanized_v1_full.md'
V47 = '/home/user/revision/v7/paper3_material_ledgers_v47.md'
AUDIT = f'{V48}/v48_reuse_audit.json'

RULES = [
    ('reserved-operator', r'S\^\{?\\top',
     'the deposited article calls it $S_{\\mathcal{T}}$ and reserves plain $S$ for the moiety readout $S_m',
     'normalize the span to $S_{\\mathcal{T}}$, or regenerate the row'),
    ('reserved-font', r'\\mathsf\{?(?:S|K|N|P)\}?(?![a-zA-Z])',
     '$\\mathsf{S}$ is the hybrid incidence matrix of Conditional Theorem 15 and $\\mathsf{L}$ its left null basis; '
     'the §2.4 state is written undecorated',
     'regenerate the row, or drop the decoration'),
    ('dropped-font', r'\\dot\s*\\chi\s*=\s*S\s*\\eta',
     'the hypothesis in the deposited article reads $\\dot\\chi = \\mathsf{S}\\eta + b$',
     'restore $\\mathsf{S}$, or regenerate the row'),
    ('colliding-decoration-A', r'\\mathcal\s*\{?A\}?\s*(?:\^\{?\\mathrm\{?win|\^\{?\\sharp|_\{?\\min)',
     'the article writes the barrier $A_{\\min}^{\\mathrm{win}}$; $\\mathcal{A}$ is its adequacy functional',
     'strip the $\\mathcal$, or regenerate the row'),
    ('colliding-decoration-B', r'\\mathcal\s*\{?B\}?\s*_(?:\{)?(?:\\mathrm\{)?(?:lim|min)',
     'the article writes $B_{\\lim}$, and keeps $\\mathcal{B}(x,t)$ for the attainable-balance domain',
     'strip the $\\mathcal$, or regenerate the row'),
    ('renamed-object-H', r'\\mathcal\s*\{?H\}?',
     'the article defines $H_A^{\\mathrm{loc}}$ and $H_A^{\\mathrm{gross}}$ and never uses $\\mathcal{H}$',
     'strip the $\\mathcal$, or regenerate the row'),
]
COSMETIC = [
    (r'\\hat(?![a-zA-Z])', 'the deposited article writes \\widehat'),
    (r'\\dfrac', 'the deposited article writes \\frac'),
    (r'\\blacksquare', 'the deposited article ends a proof with □'),
    (r'\{,\}', 'the deposited article writes thousands inside maths differently'),
]
DEP_EVIDENCE = {
    'reserved-operator': r'where \$S_\{\\mathcal\{T\}\}\$ is the typed stoichiometric',
    'reserved-font': r'\\mathsf\{?L\}?\^?\\top\s*\\mathsf\{?S\}?\s*=\s*0',
    'dropped-font': r'\\dot\s*\\chi\s*=\s*\\mathsf\{?S\}?\s*\\eta',
    'colliding-decoration-A': r'\\mathcal\s*\{?A\}?\s*:\s*\\mathbb\s*\{?R',
    'colliding-decoration-B': r'\\mathcal\{?B\}?\(x,t\)',
    'renamed-object-H': r'H_A\^\{?\\mathrm\{?loc',
}


def quote(txt, pat, span=170):
    m = re.search(pat, txt)
    if not m:
        return '(no such line - check the rule)'
    a, z = max(0, m.start() - 55), min(len(txt), m.end() + 115)
    s = re.sub(r'\s+', ' ', txt[a:z]).strip()
    if a > 0 and s and s[0] == ' ':
        s = s.lstrip()
    if a > 0:
        s = re.sub(r'^[^ \n]{1,9} ', '', s)          # do not start mid-word
    return s[:span]


def main():
    dep = open(DEPOSIT).read()
    drf = open(DRAFT).read()
    v47 = open(V47).read()
    rows = json.load(open(AUDIT))
    out = []
    counts = {}
    for r in rows:
        t = r['draft']
        for name, pat, why, fix in RULES:
            found = re.findall(pat, t)
            if not found:
                continue
            counts[name] = counts.get(name, 0) + len(found)
            out.append(dict(id=r['id'], cls=name, n=len(found), sec=r.get('sec', ''), ratio=r['ratio'],
                            why=why, fix=fix, why_kind=r['why'], sent=t,
                            evidence=quote(dep, DEP_EVIDENCE[name]),
                            draft_doc_count=len(re.findall(pat, drf)),
                            deposit_doc_count=len(re.findall(pat, dep)),
                            v47_count=len(re.findall(pat, v47))))
    cos = {}
    for pat, note in COSMETIC:
        n = sum(len(re.findall(pat, r['draft'])) for r in rows)
        if n:
            cos[pat] = (n, note)

    ids = sorted(set(o['id'] for o in out))
    L = ['# Notation identity in the reuse set\n',
         f'''A line-level read of the {len(rows)} sentences the ledger cleared for verbatim reuse, following
`v48_reuse_audit_v1.py` (words) with `v48_notation_drift_v1.py` (the maths inside them). {len(ids)} of the
{len(rows)} reuse a symbol in a form the deposited article does not use for that object. This is not a spelling
quibble: in this paper the fonts are load-bearing, and in four of the six classes the form the draft chose is a
letter the deposited article has already given something else.\n''',
         '\n| class | occurrences in the 306 | in the whole draft | in the deposited article | already in the shipped v47 |',
         '|---|---|---|---|---|']
    for name, pat, why, fix in RULES:
        L.append(f'| `{name}` | {counts.get(name, 0)} | {len(re.findall(pat, drf))} | {len(re.findall(pat, dep))} '
                 f'| {len(re.findall(pat, v47))} |')
    L.append('\nThe columns are counts of the pattern, not of flaws: the deposited article\'s own `\\mathsf{S}` and '
             '`\\mathcal{B}(x,t)` are correct uses of the same glyphs, which is exactly the point - the document '
             'would print one glyph for two objects.\n')
    L.append('## The rows, with the line each rule is measured against\n')
    cur = None
    for o in sorted(out, key=lambda x: (x['cls'], x['id'])):
        if o['cls'] != cur:
            cur = o['cls']
            L.append(f'### `{cur}`\n')
        L.append(f"**{o['id']}** · draft §{o['sec'] or 'front'} · nearest deposit sentence at ratio {o['ratio']} "
                 f"· ledger verdict: {o['why_kind']}\n")
        L.append(f"- {o['why']}\n- disposition: {o['fix']}\n")
        L.append(f"- the deposited article writes: `{o['evidence']}`\n")
        L.append(f"> {o['sent'][:300]}\n")
    L.append('## The cosmetics, for completeness\n')
    for pat, (n, note) in cos.items():
        L.append(f'- `{pat}` - {n} occurrences in the reuse set; {note}. No object changes, so nothing needs a '
                 'decision; a build that wants one spelling can fold them in the same pass as the classes above.\n')
    L.append(f'''
## What this changes about the reuse ruling

The ruling was: reuse what the ledger found supported, and the ledger compared *stripped* prose, so it never saw the
maths a reused sentence carries. The 306 are clean on names, pointers, status labels, universals and hedges - the
audit\'s own planted-defect test (`v48_audit_selftest.md`) catches 6 of 6 on those checks - and they are not clean
on notation. Nothing here argues for trusting the deposit\'s *prose* over the draft\'s; the sentences below are not
a register problem either. They are the reuse decision importing a second name for a defined object.

`v48_overrules_notation_candidate.csv` holds these {len(ids)} rows marked `regenerate`: move the sentence to the
deposit\'s wording and the notation comes with it, with no hand-editing. Renaming that file to `v48_overrules.csv`
applies it, and `v48_reuse_split_v1.py` will re-partition and log every row it moves. Deleting it keeps the reuse,
and then the normalisation is a build-time decision the README has to state.
''')
    open(f'{V48}/v48_reuse_findings.md', 'w').write('\n'.join(L) + '\n')
    json.dump(out, open(f'{V48}/v48_reuse_findings.json', 'w'), indent=1)
    with open(f'{V48}/v48_reuse_findings.csv', 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['id', 'class', 'occurrences', 'deposit_evidence', 'why', 'disposition'])
        for o in out:
            w.writerow([o['id'], o['cls'], o['n'], o['evidence'], o['why'], o['fix']])
    with open(f'{V48}/v48_overrules_notation_candidate.csv', 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['id', 'decision'])
        for i in ids:
            w.writerow([i, 'regenerate'])
    print(f'{len(ids)} rows over {sum(counts.values())} occurrences · classes: ' +
          ', '.join(f'{k}={v}' for k, v in sorted(counts.items())))
    print('cosmetic:', {p[1:]: v[0] for p, v in cos.items()})


if __name__ == '__main__':
    main()
