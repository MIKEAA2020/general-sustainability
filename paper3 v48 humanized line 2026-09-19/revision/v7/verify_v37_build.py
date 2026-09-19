#!/usr/bin/env python3
"""Final gate for v37 (rerunnable).

(1) the logged edits reverse v37 -> v36 byte-exactly, modulo whitespace and the display-underscore
    convention; (2) the drafted typing block shipped verbatim into the md and into the tex after the dialect
    conversion; (3) statement labels unique and identical across formats, maxima as expected; (4) numbering
    note consistent; (5) tex pure ASCII, no `$`, no doubled backslashes, no duplicate \\label;
(6) the new claims present in both formats and in the compiled PDF, and v36's shipped content intact;
(7) the superseded standards wording gone, and the refuted acronym still absent.
"""
import json, re, sys

R = '/home/user/revision/v7/'
V = lambda f: open(R + f, encoding='utf-8').read()
WS = lambda s: re.sub(r'\s+', ' ', s).strip()
und = lambda x: re.sub(r'(?<!\\)\\_', '_', x)
ok = True

log = json.load(open(R + 'revisions_v37_kernel_log.json'))
print(f'v37 edits in log: {len(log)} (each must reverse)')
for fmt in ('md', 'tex'):
    t = V(f'paper3_material_ledgers_v37.{fmt}')
    un = []
    for e in reversed(log):
        new, old = (e['new'], e['old']) if fmt == 'md' else (e['new_tex'], e['old_tex'])
        if t.count(new) == 1:
            t = t.replace(new, old)
        elif new == old:
            pass
        else:
            un.append((e['name'], t.count(new)))
    same = und(WS(t)) == und(WS(V(f'paper3_material_ledgers_v36.{fmt}')))
    print(f'  {fmt}: reversal v37 -> v36 exact: {same} | unreversed: {un or "none"} | {len(WS(t))} chars')
    ok &= same and not un

md, tx = V('paper3_material_ledgers_v37.md'), V('paper3_material_ledgers_v37.tex')
sys.path.insert(0, R)
from build_v37_kernel import BLOCK, block_to_tex            # noqa: E402
inmd = BLOCK in md
intx = WS(block_to_tex(BLOCK)) in WS(tx)
print(f'  typing block verbatim into md: {inmd} | into tex after conversion: {intx}')
ok &= inmd and intx

lab = re.compile(r'\*\*(Definition|Proposition|Theorem|Corollary|Lemma|Remark)\s+(\d+)')
labs = [(m.group(1), int(m.group(2))) for m in lab.finditer(md)]
tll = [(m.group(1), int(m.group(2))) for m in
       re.compile(r'\\textbf\{(Definition|Proposition|Theorem|Corollary|Lemma|Remark)\s+(\d+)').finditer(tx)]
reps = sorted({l for l in labs if labs.count(l) > 1})
mx = {}
for k, n in labs:
    mx[k] = max(mx.get(k, 0), n)
want = {'Definition': 47, 'Proposition': 42, 'Theorem': 24, 'Remark': 36, 'Lemma': 4, 'Corollary': 19}
tl = re.findall(r'\\label\{([^}]*)\}', tx)
print(f'  labels: md {len(labs)} = tex {len(tll)}: {sorted(labs) == sorted(tll)} | repeats: {reps or "none"}')
print(f'  maxima: {mx} | as expected: {mx == want} | tex \\label dups: '
      f'{sorted({x for x in tl if tl.count(x) > 1}) or "none"}')
ok &= not reps and sorted(labs) == sorted(tll) and mx == want and not [x for x in tl if tl.count(x) > 1]

note = ('1\u201347 sequence counter' in md and '40\u201347, Lemma 4, Theorem 24, and Propositions 25\u201332 '
        'and 36\u201337 and 39\u201342, with Remarks 33\u201336,' in md
        and '1--47 sequence counter' in tx and '40--47, Lemma 4, Theorem 24, and Propositions 25--32 '
        'and 36--37 and 39--42, with Remarks 33--36,' in tx)
dbl = len(re.findall(r'\\\\[a-zA-Z;{]', md)), len(re.findall(r'\\\\[a-zA-Z;{]', tx))
print(f'  numbering note both formats: {note} | doubled backslashes (md, tex): {dbl} | '
      f'tex ascii: {not [c for c in tx if ord(c) > 127]} | tex $ count: {tx.count(chr(36))}')
ok &= note and dbl == (0, 0) and not tx.count(chr(36))

MATH = [
    (r'S_{\mathcal{T}} \;=\; \bigoplus_{\gamma} S_{\gamma}', 'Prop 42 block-diagonal form'),
    (r'\ker S_{\mathcal{T}}^{\top} \;=', 'Prop 42 kernel splitting'),
    (r'(\alpha, \beta, c)', 'conversion coefficient triple'),
    (r'(\mathrm{ty}_i, \mathrm{un}_i)', 'type-and-unit pair'),
    (r'no column is both', 'transfer-or-conversion, never both'),
    (r'm_{\mathrm{needed}} \;=\; d_0\tau + \frac{d_0^{2}}{2\rho}', 'v36 Prop 41 intact'),
    (r'T = m_0/(\underline\delta g_m)', 'v36 Def 46 corner intact'),
]
for s_, name in MATH:
    fa = WS(s_) in WS(md)
    fb = WS(s_) in WS(tx) or WS(s_.replace('_', '\\_')) in WS(tx)
    print(f'   {name:34s} md {"ok" if fa else "MISSING"} | tex {"ok" if fb else "MISSING"}')
    ok &= fa and fb
PROSE = [
    ('Definition 47 (Type structure)', 'Def 47 present'),
    ('Proposition 42 (No conservation law crosses a type class)', 'Prop 42 present'),
    ('Remark 36 (What the type structure buys', 'Remark 36 present'),
    ('the declaration is Definition 47', 'Sec 2.1 forward pointer'),
    ('Proposition 42 states exactly in what sense it cannot', 'Sec 2.1 mass pointer'),
    ('typing (Definition 47) are the three predicates', 'Def 42 predicate pointer'),
    ('incommensurable objects under the type structure of Definition 47', 'Sec 6.5 names the object'),
    ('is a change of ledger and not a change of notation', 'Def 47 change-of-ledger clause'),
    ('cannot change', 'Redraw invariance with its hypothesis'),
    ('not a thesis about worth', 'Valuation half declined'),
    ('Endorsed by the United Nations Statistical Commission at its fifty-sixth session, March 2025',
     'SNA entry endorsed + dated'),
    ('an other change in the volume of assets', 'SNA 2008 contrast stated'),
    ('extraction in excess of the resource', 'rate-comparison definition'),
    ('a net aggregate moved because a classification moved', 'standards make the article point'),
    ('April 2002 to December 2020', 'G3P anomaly reference named'),
    ('June 2005', 'G3P documented defect carried'),
    ('Definition 45 (Latest safe intervention time)', 'v36 Def 45 intact'),
    ('Remark 35 (What a non-displacement gate can say', 'v36 Rem 35 intact'),
]
for s_, name in PROSE:
    fa, fb = WS(s_) in WS(md), WS(s_) in WS(tx)
    print(f'   {name:34s} md {"ok" if fa else "MISSING"} | tex {"ok" if fb else "MISSING"}')
    ok &= fa and fb
ABSENT = ['LSIT', 'leaves the classification of depletion settled', 'Adopted by the United Nations',
          'incommensurable objects under the typing of Section 2.1', 'Conservation, capacity and typing are the']
for s_ in ABSENT:
    a = md.count(s_) == 0 and tx.count(s_) == 0
    print(f'   {"absent: " + s_[:30]:34s} {a}')
    ok &= a
try:
    import pypdf
    raw = '\n'.join((p.extract_text() or '') for p in pypdf.PdfReader(R + 'paper3_material_ledgers_v37.pdf').pages)
    txt, pages = WS(raw), len(pypdf.PdfReader(R + 'paper3_material_ledgers_v37.pdf').pages)
    lit = len(re.findall(r'[A-Za-z}\)]_[A-Za-z0-9\\{]', raw))
    need = ['The type structure the operator', 'No conservation law crosses a type class',
            'What the type structure buys', 'extraction in excess of the resource', 'June 2005',
            'Latest safe intervention time', 'Supportable-output envelope']
    miss = [x for x in need if x not in txt]
    print(f'  PDF: {pages} pages | missing text probes: {miss or "none"} | '
          f'literal underscores in math: {lit} (2 = the e-mail address)')
    ok &= not miss and lit <= 2
except Exception as e:                                       # noqa: BLE001
    print('  PDF check unavailable:', e)
    ok = False

print('\nALL CHECKS PASS' if ok else '\nSOME CHECKS FAILED')
sys.exit(0 if ok else 1)
