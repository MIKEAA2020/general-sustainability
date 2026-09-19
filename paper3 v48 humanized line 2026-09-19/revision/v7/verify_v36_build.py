#!/usr/bin/env python3
"""Final gate for v36 (rerunnable).

(1) the logged edits reverse v36 -> v35 byte-exactly, modulo whitespace and the display-underscore
    convention that v35 itself introduced; (2) the drafted block shipped verbatim into the md and into the
    tex after the md->tex dialect conversion; (3) statement labels unique and identical across formats;
(4) numbering note consistent; (5) tex pure ASCII, no doubled backslashes, balanced math delimiters;
(6) the substantive claims present in both formats and in the compiled PDF; (7) the refuted acronym and the
    stale bare pointer are absent everywhere.
"""
import json, re, sys

R = '/home/user/revision/v7/'
V = lambda f: open(R + f, encoding='utf-8').read()
WS = lambda s: re.sub(r'\s+', ' ', s).strip()
und = lambda x: re.sub(r'(?<!\\)\\_', '_', x)          # ignore display-underscore escaping
ok = True

log = json.load(open(R + 'revisions_v36_kernel_log.json'))
print(f'v36 edits in log: {len(log)} (each must reverse)')
for fmt in ('md', 'tex'):
    t = V(f'paper3_material_ledgers_v36.{fmt}')
    un = []
    for e in reversed(log):
        new, old = (e['new'], e['old']) if fmt == 'md' else (e['new_tex'], e['old_tex'])
        if t.count(new) == 1:
            t = t.replace(new, old)
        elif new == old:
            pass
        else:
            un.append((e['name'], t.count(new)))
    same = und(WS(t)) == und(WS(V(f'paper3_material_ledgers_v35.{fmt}')))
    print(f'  {fmt}: reversal v36 -> v35 exact: {same} | unreversed: {un or "none"} | {len(WS(t))} chars')
    ok &= same and not un

md, tx = V('paper3_material_ledgers_v36.md'), V('paper3_material_ledgers_v36.tex')
sys.path.insert(0, R)
from build_v36_kernel import BLOCK, m2t          # the exact strings the build consumed   # noqa: E402
inmd = BLOCK in md
intx = WS(m2t(BLOCK)) in WS(tx)
print(f'  block shipped verbatim into md: {inmd} | into tex (after bold/box conversion): {intx}')
ok &= inmd and intx

lab = re.compile(r'\*\*(Definition|Proposition|Theorem|Corollary|Lemma|Remark)\s+(\d+)')
labs = [(m.group(1), int(m.group(2))) for m in lab.finditer(md)]
tll = [(m.group(1), int(m.group(2))) for m in
        re.compile(r'\\textbf\{(Definition|Proposition|Theorem|Corollary|Lemma|Remark)\s+(\d+)').finditer(tx)]
reps = sorted({l for l in labs if labs.count(l) > 1})
mx = {}
for k, n in labs:
    mx[k] = max(mx.get(k, 0), n)
want = {'Definition': 46, 'Proposition': 41, 'Theorem': 24, 'Remark': 35, 'Lemma': 4, 'Corollary': 19}
print(f'  labels: md {len(labs)} = tex {len(tll)}: {sorted(labs) == sorted(tll)} | repeats: {reps or "none"}')
print(f'  maxima: {mx} | as expected: {mx == want}')
ok &= not reps and sorted(labs) == sorted(tll) and mx == want

note = ('1\u201346 sequence counter' in md and '40\u201346, Lemma 4, Theorem 24, and Propositions 25\u201332 '
        'and 36\u201337 and 39\u201341, with Remarks 33\u201335,' in md
        and '1--46 sequence counter' in tx and '40--46, Lemma 4, Theorem 24, and Propositions 25--32 '
        'and 36--37 and 39--41, with Remarks 33--35,' in tx)
dbl = len(re.findall(r'\\\\[a-zA-Z;{]', md)), len(re.findall(r'\\\\[a-zA-Z;{]', tx))
print(f'  numbering note both formats: {note} | doubled backslashes (md, tex): {dbl} | '
      f'tex ascii: {not [c for c in tx if ord(c) > 127]} | tex $ count: {tx.count(chr(36))}')
ok &= note and dbl == (0, 0) and not tx.count(chr(36))

MATH = [
    (r'm_{\mathrm{needed}} \;=\; d_0\tau + \frac{d_0^{2}}{2\rho}', 'Prop 41 closed form'),
    (r't_{\mathrm{last}} \;=\; \frac{m_0}{d_0} - \tau - \frac{d_0}{2\rho}', 't_last closed form'),
    (r'the frozen-rate ratio of Proposition 26', 'horizon attributed to Prop 26'),
    (r'A \ge A_{\min}', 'barrier respected'),
    (r'\dot d \ge -\rho', 'ramp-rate constraint in the supremum'),
    (r'T = m_0/(\underline\delta g_m)', 'envelope corner = Def 22 horizon'),
    (r't_{\mathrm{last}} = -0.75', 'negative-deadline instance'),
    (r'T \ge H^{\mathrm{loc}}', 'Prop 26 direction clause'),
    (r'10 - 2 - 5 = 3', 'illustration arithmetic'),
]
for s_, name in MATH:
    fa = WS(s_) in WS(md)
    fb = WS(s_) in WS(tx) or WS(s_.replace('_', '\\_')) in WS(tx)
    print(f'   {name:34s} md {"ok" if fa else "MISSING"} | tex {"ok" if fb else "MISSING"}')
    ok &= fa and fb
PROSE = [
    ('Definition 45 (Latest safe intervention time)', 'Def 45 present'),
    ('Definition 46 (Supportable-output envelope)', 'Def 46 present'),
    ('Remark 35 (What a non-displacement gate can say', 'Remark 35 present'),
    ('declared as illustrative and not empirical', 'instance marked illustrative'),
    ('is not below the deficit of the host ledger alone', 'gate compares deficits'),
    ('vocabulary of the per-parameter field of the declaration protocol', 'per-parameter status field'),
    ('no biocapacity figure is computed for carbon uptake', 'carbon convention cited'),
    ('Global Footprint Network, 2021, Section 9.1.2', 'guidebook cited in text'),
    ('Working Guidebook to the National Footprint and Biocapacity Accounts, 2021 edition', 'guidebook in refs'),
    ('28 July, the 209th day', 'vintage reconciliation'),
    ('its eq. (1), where the memory--effort pair is defined', 'companion pointer (4.1) precise'),
    ('its eq. (1), the gated three-state core', 'companion pointer (2.4) precise'),
]
for s_, name in PROSE:
    fa, fb = WS(s_) in WS(md), WS(s_) in WS(tx)
    print(f'   {name:34s} md {"ok" if fa else "MISSING"} | tex {"ok" if fb else "MISSING"}')
    ok &= fa and fb
ABSENT = ['LSIT', 'eq. (1) and Section 2.4 of that analysis', 'so the convention is declared with the figure',
          'unit per year$^2$', r'\pi_\varphi^{+}\, \bar v']
for s_ in ABSENT:
    a = md.count(s_) == 0 and tx.count(s_) == 0
    print(f'   {"absent: " + s_[:30]:34s} {a}')
    ok &= a
try:
    import pypdf
    pages = pypdf.PdfReader(R + 'paper3_material_ledgers_v36.pdf').pages
    txt = WS('\n'.join((p.extract_text() or '') for p in pages))
    lit = len(re.findall(r'[A-Za-z}\)]_[A-Za-z0-9\\{]', '\n'.join((p.extract_text() or '') for p in pages)))
    need = ['Latest safe intervention time', 'Supportable-output envelope', 'non-displacement gate',
            'no biocapacity figure is computed for carbon uptake', 'Working Guidebook']
    miss = [x for x in need if x not in txt]
    print(f'  PDF: {len(pages)} pages | missing text probes: {miss or "none"} | '
          f'literal underscores in math: {lit} (2 = the e-mail address)')
    ok &= not miss and lit <= 2
except Exception as e:                                       # noqa: BLE001
    print('  PDF check unavailable:', e)
    ok = False

print('\nALL CHECKS PASS' if ok else '\nSOME CHECKS FAILED')
sys.exit(0 if ok else 1)
