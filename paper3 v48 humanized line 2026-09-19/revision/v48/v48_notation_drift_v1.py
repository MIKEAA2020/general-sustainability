#!/usr/bin/env python3
"""Put the maths in the 306 reused sentences back beside the maths of the deposited article.

The audit read words. The reused sentences also carry inline `$...$`, and the humanizer edited *that* too: the
deposit writes `\\mathbf{1}^{\\top}` and the draft writes `\\mathbb 1^{\\top}`, the deposit writes
`A^{\\mathrm{act,*}}` and the draft writes `A_{\\mathrm{act},*}`. A value gate cannot see this - the number is the
number - and a word-level ledger cannot either, because the ledger strips `$...$` before it reads. Reuse imports
the draft's spelling into a document whose displayed equations come from the deposit, so the same object can end up
written two ways, and where the decorated form is used for something else, ambiguously.

Each `$...$` span in a reused sentence is normalised and tested against the deposited article's own maths, in three
relaxations:

  exact      the span, spaces and braces aside, occurs in the deposited article as written
  deco       it occurs once `\\mathbf|\\mathbb|\\mathcal|\\mathsf|\\boldsymbol|\\mathrm|\\text` wrappers are removed
             from one side or the other - a font choice, not a different object
  script     it occurs once sub- and superscript positions are identified (`_` and `^` both read as one marker) -
             the draft moved a label between the two
  absent     it occurs in no form, which is where a claim would actually be different

`deco` and `script` hits are not errors of fact; they are notation drift, and the author decides whether the
shipped document is normalised to the deposited article's spelling. `absent` spans are the ones to read.

Writes `v48_notation_drift.{md,csv,json}`. Nothing here edits a document.
"""
import csv
import difflib
import json
import re
from collections import Counter

V48 = '/home/user/revision/v48'
DEPOSIT = '/home/user/revision/v7/paper3_material_ledgers_v42.md'
AUDIT = f'{V48}/v48_reuse_audit.json'

WRAP = re.compile(r'\\(?:mathbf|mathbb|mathcal|mathsf|boldsymbol|mathrm|mathit|text|operatorname)\s*')


def base(s):
    """the span as written, with whitespace, thin spaces and size macros gone"""
    s = re.sub(r'\s+', '', s)
    for junk in ('\\,', '\\;', '\\:', '\\!', '\\thinspace', '~'):
        s = s.replace(junk, '')
    s = re.sub(r'\\(?:left|right|Bigl|Bigr|Bigg|bigg|big)', '', s)
    s = s.replace('\\tfrac', '\\frac').replace('\\dfrac', '\\frac').replace('{,}', ',')
    return s


def unwrap(s):
    """LaTeX grouping that carries no meaning: ^{x} reads as ^x, \\mathbb{R} as \\mathbb R, and the
    end-of-proof mark is the end-of-proof mark whichever glyph the source used"""
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\{([^{}]+)\}', r'\1', s)
    for qed in ('\\blacksquare', '\\square', '□', '\\qedsymbol', '\\Box'):
        s = s.replace(qed, 'QED')
    return s


def undecorate(s):
    """font wrappers gone, so \\mathbf{1}, \\mathbb 1 and 1 read alike"""
    s = unwrap(s)
    prev = None
    while prev != s:
        prev = s
        s = WRAP.sub('', s)
    return s.replace('{', '').replace('}', '')


def unscript(s):
    """identify sub- and superscript positions: A_{x} and A^{x} read the same"""
    return re.sub(r'[_^]', '@', undecorate(s))



def spans(sent):
    out = []
    for m in re.finditer(r'\$\$?(.+?)\$\$?', sent, flags=re.S):
        x = m.group(1).strip()
        if len(x) > 1:
            out.append(x)
    return out


def dep_span_inventory():
    """every inline `$...$` in the deposited article, and its level-3 normalised key"""
    txt = open(DEPOSIT).read()
    raw, keys = [], []
    for m in re.finditer(r'\$\$?(.+?)\$\$?', txt, flags=re.S):
        s = m.group(1).strip()
        if len(base(s)) >= 4:
            raw.append(s)
            keys.append(unscript(s))
    return raw, keys


DEP_SPANS, d_span_keys = dep_span_inventory()


def main():
    dep = open(DEPOSIT).read()
    d_base = base(dep)
    d_cos, d_dec, d_scr = unwrap(d_base), undecorate(d_base), unscript(d_base)
    rows = json.load(open(AUDIT))
    recs = []
    tally = Counter()
    for r in rows:
        hits = []
        for sp in spans(r['draft']):
            b = base(sp)
            if len(b) < 4:                      # a bare symbol: nothing to compare
                continue
            if b in d_base:
                tally['exact'] += 1
                continue
            c = unwrap(b)
            if c in d_cos:
                tally['cosmetic'] += 1
                continue
            u = undecorate(b)
            if u in d_dec and u != c:
                tally['deco'] += 1
                hits.append(('deco', sp, closest(u, 1)))
                continue
            s2 = unscript(u)
            if s2 in d_scr and s2 != u:
                tally['script'] += 1
                hits.append(('script', sp, closest(s2, 2)))
                continue
            near = difflib.get_close_matches(unscript(sp), d_span_keys, n=1, cutoff=0.55)
            tally['absent'] += 1
            hits.append(('absent', sp, DEP_SPANS[d_span_keys.index(near[0])] if near else ''))
        if hits:
            recs.append(dict(id=r['id'], ratio=r['ratio'], sec=r['sec'], flags=[f'{k}: {s}' for k, s, _ in hits],
                             pairs=[dict(kind=k, draft=s, dep=c) for k, s, c in hits], sent=r['draft']))
    tot = tally['exact'] + tally['cosmetic'] + tally['deco'] + tally['script'] + tally['absent']
    lines = ['# The maths in the 306 reused sentences, held against the deposit\n',
             f'''Every inline `$...$` span of any length in a sentence marked for reuse ({tot} spans over {len(rows)}
sentences) was normalised and looked for in the deposited article, at four levels of generosity. {tally["exact"]}
occur as written, {tally["cosmetic"]} once meaningless grouping braces and the end-of-proof glyph are identified,
{tally["deco"]} once the font wrappers are taken off, {tally["script"]} once sub- and superscript positions are
identified - the humanizer re-typeset the notation without changing the claim, and a document cannot carry two
spellings of one object. {tally["absent"]} occur in no form, and those are listed below one at a time for reading.\n''',
             '\n| span status | count |', '|---|---|',
             f'| written as the deposited article writes it | {tally["exact"]} |',
             f'| differs only in grouping braces or the QED glyph | {tally["cosmetic"]} |',
             f'| font wrapper differs (`\\mathbf` to `\\mathbb`, `\\mathsf` added) | {tally["deco"]} |',
             f'| label moved between sub- and superscript | {tally["script"]} |',
             f'| no matching span in the deposited article | {tally["absent"]} |\n',
             '## Where the notation differs\n']
    for kind, lab in (('deco', 'font wrapper'), ('script', 'script position')):
        sub = [(r, p) for r in recs for p in r['pairs'] if p['kind'] == kind]
        lines.append(f'### {lab} - {len(sub)} spans over {len(set(id(r) for r, _ in sub))} sentences\n')
        seen = Counter()
        for r, p in sub:
            seen[(base(p['draft']), base(p['dep']))] += 1
        lines.append('| the draft writes | the deposit writes | in how many reused sentences |')
        lines.append('|---|---|---|')
        for (a, b), c in seen.most_common(18):
            lines.append(f'| `{a[:56]}` | `{b[:56]}` | {c} |')
        lines.append('')
    lines.append('## Spans with no counterpart in the deposited article\n')
    ab = [(r, p) for r in recs for p in r['pairs'] if p['kind'] == 'absent']
    if not ab:
        lines.append('None: every inline expression in the reuse set is the deposited article\'s, up to font and '
                     'script spelling.\n')
    for r, p in ab:
        lines.append(f"### {r['id']} · ratio {r['ratio']} · draft §{r['sec'] or 'front'}\n")
        lines.append(f"```\n{p['draft']}\n```\n")
        lines.append(f"> {r['sent'][:400]}\n")
    lines.append(f'''
## What this means for the build

The reuse ruling was written as though a reused sentence carried the document\'s maths with it. It carries the
*draft\'s* maths, and the draft re-typeset the symbols: `{tally["deco"] + tally["script"]}` of the spans differ from
the deposited article in spelling alone. Two ways out, and the choice is the author\'s, not the pipeline\'s:

1. **Normalize the reused sentences\' inline maths to the deposited article\'s spelling** - mechanical, reversible,
   and it changes no word; it is applied only where the two forms differ by wrapper or script position, never where
   a number sits differently.
2. **Send those sentences to the regenerate pile** - the prose comes from the deposit\'s own wording, so the
   notation arrives correct and the sentence loses whatever the draft\'s phrasing was chosen for.

Option 1 is what the draft\'s register argues for; option 2 is what the deposit-as-truth-source argues for. Neither
is applied by this file.
''')
    open(f'{V48}/v48_notation_drift.md', 'w').write('\n'.join(lines) + '\n')
    json.dump(recs, open(f'{V48}/v48_notation_drift.json', 'w'), indent=1)
    with open(f'{V48}/v48_notation_drift.csv', 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['id', 'ratio', 'kind', 'draft_span', 'deposit_span'])
        for r in recs:
            for p in r['pairs']:
                w.writerow([r['id'], r['ratio'], p['kind'], p['draft'][:200], p['dep'][:200]])
    print('spans:', dict(tally), '· sentences touched:', len(recs), '· absent listed:', len(ab))


_DEP_SPANS = None


def closest(u, level):
    """the deposit's own span that this one sits inside, so the diff can be read without hunting"""
    global _DEP_SPANS
    if _DEP_SPANS is None:
        _DEP_SPANS = [m.group(1).strip() for m in re.finditer(r'\$\$?(.+?)\$\$?', open(DEPOSIT).read(), flags=re.S)]
    for order in (0, 1, 2):
        for s in _DEP_SPANS:
            x = base(s)
            if order >= 1:
                x = undecorate(x)
            if order >= 2:
                x = unscript(x)
            if u in x:
                return re.sub(r'\s+', ' ', s)[:160]
    return 


if __name__ == '__main__':
    main()
