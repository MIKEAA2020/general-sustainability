#!/usr/bin/env python3
"""Final gate for v38 (rerunnable)."""
import json, re, sys

R = '/home/user/revision/v7/'
V = lambda f: open(R + f, encoding='utf-8').read()
WS = lambda s: re.sub(r'\s+', ' ', s).strip()
und = lambda x: re.sub(r'(?<!\\)\\_', '_', x)
ok = True

log = json.load(open(R + 'revisions_v38_kernel_log.json'))
print(f'v38 edits in log: {len(log)} (each must reverse)')
for fmt in ('md', 'tex'):
    t = V(f'paper3_material_ledgers_v38.{fmt}')
    un = []
    for e in reversed(log):
        new, old = (e['new'], e['old']) if fmt == 'md' else (e['new_tex'], e['old_tex'])
        if t.count(new) == 1:
            t = t.replace(new, old)
        elif new == old:
            pass
        else:
            un.append((e['name'], t.count(new)))
    same = und(WS(t)) == und(WS(V(f'paper3_material_ledgers_v37.{fmt}')))
    print(f'  {fmt}: reversal v38 -> v37 exact: {same} | unreversed: {un or "none"} | {len(WS(t))} chars')
    ok &= same and not un

md, tx = V('paper3_material_ledgers_v38.md'), V('paper3_material_ledgers_v38.tex')
lab = re.compile(r'\*\*(Definition|Proposition|Theorem|Corollary|Lemma|Remark)\s+(\d+)')
labs = [(m.group(1), int(m.group(2))) for m in lab.finditer(md)]
tll = [(m.group(1), int(m.group(2))) for m in
       re.compile(r'\\textbf\{(Definition|Proposition|Theorem|Corollary|Lemma|Remark)\s+(\d+)').finditer(tx)]
reps = sorted({l for l in labs if labs.count(l) > 1})
mx = {}
for k, n in labs:
    mx[k] = max(mx.get(k, 0), n)
want = {'Definition': 47, 'Proposition': 42, 'Theorem': 24, 'Remark': 36, 'Lemma': 4, 'Corollary': 19}
print(f'  labels: md {len(labs)} = tex {len(tll)}: {sorted(labs) == sorted(tll)} | repeats: {reps or "none"}')
print(f'  maxima: {mx} | unchanged from v37: {mx == want}')
ok &= not reps and sorted(labs) == sorted(tll) and mx == want

note = ('1\u201347 sequence counter' in md and '1--47 sequence counter' in tx
        and 'Remarks 33\u201336,' in md and 'Remarks 33--36,' in tx)
dbl = len(re.findall(r'\\\\[a-zA-Z;{]', md)), len(re.findall(r'\\\\[a-zA-Z;{]', tx))
print(f'  numbering note unchanged in both formats: {note} | doubled backslashes: {dbl} | '
      f'tex ascii: {not [c for c in tx if ord(c) > 127]} | tex $ count: {tx.count(chr(36))}')
ok &= note and dbl == (0, 0) and not tx.count(chr(36))

MATH = [
    (r'R_{Ca} = 1', 'quotient class-incidence matrix'),
    (r'E_\varphi = -e_a + e_b', 'exchange column'),
    (r'x_C = R x_0', 'quotient state map'),
    (r'r \le a_j^{\top} x + b_j', 'upper-endpoint LP'),
    (r'0 \le -1', 'infeasibility witness row'),
    (r'\pi_\varphi = +1', 'certificate-relativity instance'),
    (r'in units of one cycle', 'multiplier set at the kink'),
    (r'\mathsf{Cv}', 'Def 47 object still referenced'),
]
for s_, name in MATH:
    fa = WS(s_) in WS(md)
    fb = WS(s_) in WS(tx) or WS(s_.replace('_', '\\_')) in WS(tx)
    print(f'   {name:34s} md {"ok" if fa else "MISSING"} | tex {"ok" if fb else "MISSING"}')
    ok &= fa and fb
PROSE = [
    ('None declared.', 'Funding body'),
    ('concave function attains its minimum at an extreme point', 'polyhedral endpoint statement'),
    ('it is attained at the balanced start, in the interior of the fibre', 'interior-maximum note'),
    ('The two ways of reading the display above are different constructions', 'rows-vs-quotient remark'),
    ('types and units agree \\emph{throughout} each class', 'class-wide agreement check'),
    ('The verdict has three branches', 'Def 40 three-way verdict'),
    ('a statement about the declaration and not about the ledger', 'not-established branch'),
    ('it establishes no dynamic safety', 'Def 40 scope limit'),
    ('which is why the charge enters Definition 34\'s budgets and never its admissibility conditions',
     'charge does not prohibit'),
    ('Physical admissibility cannot turn on which certificate was', 'certificate-relativity claim'),
    ('named as a supergradient of the value', 'multiplier naming'),
    ('release v4.66 (Zenodo 14043031,', 'RAM vintage pinned'),
    ('values reproducing that release exactly', 'vintage verified from content'),
    ('The direction of the\ncomparison is one-way', 'Sec 1.5 non-inferential clause'),
    ('eligibility statement of exactly the kind Remark 36 treats as reclassification',
     'Sec 1.5 <-> Remark 36 link restored'),
]
for s_, name in PROSE:
    a = s_.replace('\n', ' ')
    fa, fb = WS(a) in WS(md), WS(a.replace('$', '')) in WS(tx) or WS(a) in WS(tx)
    print(f'   {name:34s} md {"ok" if fa else "MISSING"} | tex {"ok" if fb else "MISSING"}')
    ok &= fa and fb
fh = ('## Funding' in md and md.index('## Funding') < md.index('## Declaration of competing interest')
      and r'\subsection*{Funding}' in tx
      and tx.index(r'\subsection*{Funding}') < tx.index(r'\subsection*{Declaration of competing interest}'))
print(f'  Funding heading present in both formats, ahead of the competing-interest statement: {fh}')
ok &= fh
ABSENT = ['extrema of a continuous function over a polytope are attained at vertices',
          'are the values of two linear programmes over the polytope',
          'the pull date is archived in the analysis repository',
          'cohort pull date is archived', 'LSIT']
for s_ in ABSENT:
    a = WS(s_) not in WS(md) and WS(s_) not in WS(tx)
    print(f'   {"absent: " + s_[:28]:34s} {a}')
    ok &= a
try:
    import pypdf
    rd = pypdf.PdfReader(R + 'paper3_material_ledgers_v38.pdf')
    raw = '\n'.join((p.extract_text() or '') for p in rd.pages)
    txt, pages = WS(raw), len(rd.pages)
    lit = len(re.findall(r'[A-Za-z}\)]_[A-Za-z0-9\\{]', raw))
    need = ['Funding', 'None declared', 'No conservation law crosses a type class',
            'no cohort statistic is quoted from any other release', 'attains its minimum at an extreme point',
            'The verdict has three branches']
    miss = [x for x in need if x not in txt]
    print(f'  PDF: {pages} pages | missing text probes: {miss or "none"} | underscores: {lit} (2 = e-mail)')
    ok &= not miss and lit <= 2
except Exception as e:                                       # noqa: BLE001
    print('  PDF check unavailable:', e); ok = False

print('\nALL CHECKS PASS' if ok else '\nSOME CHECKS FAILED')
sys.exit(0 if ok else 1)
