#!/usr/bin/env python3
"""Final gate for v39 (rerunnable).

v39 is a status reallocation, not a rewrite: two passages demoted to the supplementary, one
prose claim promoted to a labelled proposition, one pointer re-aimed. The gate therefore has to
prove four things: (i) nothing else moved -- reverting the five logged edits returns v38
byte-for-byte in both formats; (ii) the demoted text survives verbatim in supplementary v10;
(iii) the new label keeps the sequence and the numbering note honest; (iv) no reference dangles,
in the article or in the supplementary.
"""
import json, re, sys, unicodedata

R = '/home/user/revision/v7/'
V = lambda f: open(R + f, encoding='utf-8').read()
WS = lambda s: re.sub(r'\s+', ' ', s).strip()
und = lambda x: re.sub(r'(?<!\\)\\_', '_', x)
# a demoted passage may be reproduced in a different dialect: fold the punctuation tex writes as --/---
fold = lambda s: WS(unicodedata.normalize('NFKD', s.replace('\u2014', '---')
                .replace('\u2013', '--').replace('\u2019', "'").replace('\u201c', '"')
                .replace('\u201d', '"')).replace('\u2014', '---'))
ok = True

# ------------------------------------------------------------------ (i) reversibility
log = json.load(open(R + 'revisions_v39_kernel_log.json'))
print(f'v39 edits in log: {len(log)} (each must reverse)')
for fmt in ('md', 'tex'):
    t = V(f'paper3_material_ledgers_v39.{fmt}')
    un = []
    for e in reversed(log):
        for old, new in reversed(e[fmt]):
            if t.count(new) == 1:
                t = t.replace(new, old)
            elif new == old:
                pass
            else:
                un.append((e['name'], t.count(new)))
    same = und(WS(t)) == und(WS(V(f'paper3_material_ledgers_v38.{fmt}')))
    print(f'  {fmt}: reversal v39 -> v38 exact: {same} | unreversed: {un or "none"} | {len(WS(t))} chars')
    ok &= same and not un

# ------------------------------------------------------------------ (ii) label integrity
md, tx = V('paper3_material_ledgers_v39.md'), V('paper3_material_ledgers_v39.tex')
lab = re.compile(r'\*\*(Definition|Proposition|Theorem|Corollary|Lemma|Remark)\s+(\d+)')
labs = [(m.group(1), int(m.group(2))) for m in lab.finditer(md)]
tll = [(m.group(1), int(m.group(2))) for m in
       re.compile(r'\\textbf\{(Definition|Proposition|Theorem|Corollary|Lemma|Remark)\s+(\d+)').finditer(tx)]
reps = sorted({l for l in labs if labs.count(l) > 1})
mx = {}
for k, n in labs:
    mx[k] = max(mx.get(k, 0), n)
print(f'  labels: md {len(labs)} = tex {len(tll)}: {sorted(labs) == sorted(tll)} (62 expected) '
      f'| repeats: {reps or "none"}')
print(f'  maxima: {mx}')
ok &= not reps and sorted(labs) == sorted(tll) and len(labs) == 62 \
    and mx == {'Definition': 47, 'Proposition': 43, 'Theorem': 24, 'Remark': 36, 'Lemma': 4, 'Corollary': 19}

note = ('39\u201343' in md and '39--43' in tx and '39\u201342' not in md and '39--42' not in tx
        and '1\u201347 sequence counter' in md and '1--47 sequence counter' in tx)
dbl = len(re.findall(r'\\\\[a-zA-Z;{]', md)), len(re.findall(r'\\\\[a-zA-Z;{]', tx))
print(f'  numbering note extended to 39-43 and no stale 39-42: {note} | doubled backslashes: {dbl} '
      f'| tex ascii: {not [c for c in tx if ord(c) > 127]} | tex $ count: {tx.count(chr(36))}')
ok &= note and dbl == (0, 0) and not tx.count(chr(36))

# ------------------------------------------------------------------ (iii) the promoted claim
P43 = [
    ('Proposition 43 (The institutional-failure subsystem is exactly closed)', 'Prop 43 headline'),
    ('invariance is the projection', 'Prop 43 proof line'),
    ('so the projection is\none-way', 'one-way direction stated'),
    ('is made under the citation and is not re-proved here', 'semiconjugacy still deferred'),
    ('gated three-state core', 'paper4 pointer intact'),
]
for s_, name in P43:
    a = WS(s_)
    fa, fb = a in WS(md), (a in WS(tx) or a in WS(tx).replace('$', ''))
    print(f'   {name:34s} md {"ok" if fa else "MISSING"} | tex {"ok" if fb else "MISSING"}')
    ok &= fa and fb

# ------------------------------------------------------------------ (iv) demotions: text moved, not cut
# the log holds the moved text in e['old']; each paragraph of it must survive verbatim in supp v10
# and must no longer stand in the v39 body.
supp = V('paper3_supplementary_v10.md')
v9 = open('/home/user/revision/v6/paper3_supplementary_v9.md', encoding='utf-8').read()
v38md = V('paper3_material_ledgers_v38.md')
for e in log:
    if not e['name'].startswith(('D1', 'D2')):
        continue
    pieces = [a for a, _b in e['md']]
    allsupp = all(fold(WS(q)) in fold(supp) for q in pieces)
    gone = all(fold(WS(q)) not in fold(md) for q in pieces)
    was = all(fold(WS(q)) in fold(v38md) for q in pieces)
    n = sum(len(q.split()) for q in pieces)
    print(f'   {e["name"]:34s} {n:4d} w | verbatim in v38: {was} | verbatim in supp v10: {allsupp} '
          f'| absent from v39 body: {gone}')
    ok &= allsupp and gone and was

v9intact = fold(WS(v9)) in fold(WS(supp))
parts = [h for h in ('# Part II', '# Part III') if h in supp]
print(f'  supp v10 = v9 verbatim + Part III: {v9intact} | parts present: {parts} '
      f'| words {len(supp.split())} (v9 {len(v9.split())})')
ok &= v9intact and len(parts) == 2

POINT = [("supplementary's S5.4", 'md', 'article pointer to S5.4 (dagger note + 6.5.2)'),
         ("supplementary's S14", 'md', 'article pointer to S14 (both template sections)'),
         ("## S5.4", 'supp', 'S5.4 exists in the supplementary'),
         ("## S14", 'supp', 'S14 exists in the supplementary'),
         ("## S10", 'supp', 'S10 identifiability table'),
         ("## S11", 'supp', 'S11 MDV table'),
         ("## S15", 'supp', 'S15 Typed proof-obligation row'),
         ("## S16", 'supp', 'S16 S7 pointer errata'),
         ("Lemma 3, with the typing of Definition 47", 'supp', 'S16 repoints Balanced'),
         ("Definitions 47, Proposition 42", 'supp', 'S15 cites Def 47 and Prop 42')]
for probe, side_, name in POINT:
    hold = fold(probe) in fold({'md': md, 'supp': supp}[side_])
    n_ = (md if side_ == 'md' else supp).count(probe)
    print(f'   {name:44s} {"ok" if hold else "FAIL"} ({side_}, {n_}x)')
    ok &= hold

DANGLE = ['the paragraph below', 'is the paragraph below', 'see below in this section']
for s_ in DANGLE:
    a = fold(s_) not in fold(md) and fold(s_) not in fold(tx)
    print(f'   dangling {"":12s}"{s_[:30]:30s}" absent from the article: {a}')
    ok &= a
supp_dangle = 'the paragraph below' not in supp
print(f'   supplementary preamble carries no "paragraph below" either: {supp_dangle}')
ok &= supp_dangle

ABSENT = ['is declared, not established. The reserve and\nproduction quantities used in Section 6.5.3 carry their source vintage',
          'aquitard depth and extent']
for s_ in ABSENT:
    a = fold(s_) not in fold(md)
    print(f'   demoted: {fold(s_)[:34]:36s} gone from v39 body: {a}')
    ok &= a

# ------------------------------------------------------------------ (v) internal pointers resolve
heads = set(re.findall(r'^#{2,4} (\d+(?:\.\d+){0,2})[.\s]', md, re.M))
dang = sorted({m.group(1) for m in re.finditer(r'(?:Section|\u00a7)\s*(\d+(?:\.\d+){1,2})', md)
               if m.group(1) not in heads
               and not re.search(r'\d{4},\s*$', md[max(0, m.start() - 40):m.start()])})
print(f'  internal section pointers: {len(set(re.findall(r"(?:Section|\u00a7)\s*(\d+(?:\.\d+){1,2})", md)))} distinct, '
      f'dangling (bibliographic ones excluded): {dang or "none"}')
ok &= not dang
dbl2 = 'Section 1.5' not in md and 'Section 1.2 draw their own' in md
print(f'  the standards self-pointer now names the section that holds the paragraph: {dbl2}')
ok &= dbl2

# ------------------------------------------------------------------ PDF
try:
    import pypdf
    rd = pypdf.PdfReader(R + 'paper3_material_ledgers_v39.pdf')
    raw = '\n'.join((p.extract_text() or '') for p in rd.pages)
    txt, pages = WS(raw), len(rd.pages)
    lit = len(re.findall(r'[A-Za-z}\)]_[A-Za-z0-9\\{]', raw))
    need = ['The institutional-failure subsystem is exactly closed', 'invariance is the projection',
            'full provenance is the supplementary', 'the supplementary', 'S14', 'S5.4',
            'Supplementary material', 'None declared', 'The classification status assigned below']
    miss = [x for x in need if x not in txt]
    print(f'  PDF: {pages} pages | missing probes: {miss or "none"} | underscores: {lit} (2 = e-mail) '
          f'| "??" in text: {txt.count("??")}')
    ok &= not miss and lit <= 2 and txt.count('??') == 0
except Exception as e:                                       # noqa: BLE001
    print('  PDF check unavailable:', e); ok = False

print('\nALL CHECKS PASS' if ok else '\nSOME CHECKS FAILED')
sys.exit(0 if ok else 1)
