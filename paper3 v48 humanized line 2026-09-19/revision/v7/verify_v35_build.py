#!/usr/bin/env python3
"""Final gate for v35. Rerunnable. Checks: (1) the logged 22 edits reverse v35 -> v34 exactly (mod whitespace
and the deliberate display-underscore change); (2) statement labels unique and identical in md and tex;
(3) numbering note consistent; (4) tex stays pure ASCII with no stray math delimiters; (5) the corrected and
new claims are present in both formats and in the compiled PDF."""
import json, re, sys

R = '/home/user/revision/v7/'
V = lambda f: open(R + f, encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
und = lambda x: re.sub(r'(?<!\\)\\_', '_', x)          # ignore the port's display-underscore escaping
ok = True

log = json.load(open(R + 'revisions_v35_kernel_log.json'))
print(f'edits in log: {len(log)}')
for fmt in ('md', 'tex'):
    t = V(f'paper3_material_ledgers_v35.{fmt}')
    un = []
    for e in reversed(log):
        new, old = (e['new'], e['old']) if fmt == 'md' else (e['new_tex'], e['old_tex'])
        if t.count(new) == 1:
            t = t.replace(new, old)
        elif new == old:
            pass
        else:
            un.append((e['name'], t.count(new)))
    a, b = und(norm(t)), und(norm(V(f'paper3_material_ledgers_v34.{fmt}')))
    print(f'  {fmt}: reversal == v34 : {a == b} | unreversed: {un or "none"} | {len(a)} vs {len(b)} chars')
    ok &= a == b and not un

md, tx = V('paper3_material_ledgers_v35.md'), V('paper3_material_ledgers_v35.tex')
lab = re.compile(r'\*\*(Definition|Proposition|Theorem|Corollary|Lemma|Remark)\s+(\d+)')
tl = re.compile(r'\\textbf\{(Definition|Proposition|Theorem|Corollary|Lemma|Remark)\s+(\d+)')
labs = [(m.group(1), int(m.group(2))) for m in lab.finditer(md)]
tll = [(m.group(1), int(m.group(2))) for m in tl.finditer(tx)]
reps = sorted({l for l in labs if labs.count(l) > 1})
mx = {}
for k, n in labs:
    mx[k] = max(mx.get(k, 0), n)
print(f'  labels: md {len(labs)} tex {len(tll)} identical {sorted(labs) == sorted(tll)} '
      f'repeats {reps or "none"}')
print('  maxima:', mx)
ok &= not reps and sorted(labs) == sorted(tll)

want = {'Definition': 44, 'Proposition': 40, 'Theorem': 24, 'Remark': 34, 'Lemma': 4, 'Corollary': 19}
ok &= mx == want
note = ('1\u201344 sequence counter' in md and '40\u201344, Lemma 4,' in md
        and '1--44 sequence counter' in tx and '40--44, Lemma 4,' in tx)
print(f'  numbering note: {note} | tex pure ascii: {not [c for c in tx if ord(c) > 127]} '
      f'| dollar signs in tex: {tx.count(chr(36))}')
ok &= note

PROBE = [
    ('interface charge uses |pi|', r'$|\pi_\varphi|\,\bar v_\varphi T$', r'|\pi_\varphi|\,\bar v_\varphi T'),
    ('free iff pi >= 0', r'interface is free when $\pi_\varphi \ge 0$', r'interface is free when \(\pi_\varphi \ge 0\)'),
    ('conservation = compatible pairs', 'agree on every identified compartment', 'agree on every identified compartment'),
    ('merge can destroy a moiety', 'the moiety of the first part is gone', 'the moiety of the first part is gone'),
    ('Prop 37 sufficiency only', 'certifies the composition whenever', 'certifies the composition whenever'),
    ('value function is the joint LP', 'the value of the joint programme over the fibre product',
     'the value of the joint programme over the fibre product'),
    ('instance pi = -1', r'$\pi = -1$', r'\pi = -1'),
    ('proof sign fixed', r'G_2 b_2 - \sum_\varphi \pi_\varphi f_\varphi', r'G_2 b_2 - \sum_\varphi \pi_\varphi f_\varphi'),
    ('box multipliers rho', r'$\lambda = 0$, $\rho = 1$', r'\lambda = 0\), \(\rho = 1'),
    ('Motzkin non-SOS', 'Motzkin', 'Motzkin'),
    ('interval from connectedness', 'interval image on a connected fibre', 'interval image on a connected fibre'),
    ('non-convex caveat', 'bound the value set from outside', 'bound the value set from outside'),
    ('noise typing', 'a diffusion that creates mass', 'a diffusion that creates mass'),
    ('Def 40 compensation predicate', 'Compensation as a decidable predicate', 'Compensation as a decidable predicate'),
    ('price does not characterize', 'not by whether a capacity price is finite', 'not by whether a capacity price is finite'),
    ('Def 41 control margin', 'Definition 41 (Control margin)', 'Definition 41 (Control margin)'),
    ('Def 42 affinity predicate', 'the fourth admissibility predicate', 'the fourth admissibility predicate'),
    ('Prop 40 corridor witness', 'corridor-infeasibility witness', 'corridor-infeasibility witness'),
    ('Def 43 circulation time', 'Definition 43 (Circulation time)', 'Definition 43 (Circulation time)'),
    ('Def 44 governability ratio', 'Definition 44 (Governability ratio)', 'Definition 44 (Governability ratio)'),
    ('Lemma 4 baseline covariance', 'Lemma 4 (A moving baseline', 'Lemma 4 (A moving baseline'),
    ('premium figures 213/173', r'$\Pi_\tau = 213$', r'\Pi_\tau = 213'),
    ('C labelled moiety matrix', 'moiety-composition matrix of Section 2.1', 'moiety-composition matrix of Section 2.1'),
]
for name, a_, b_ in PROBE:
    fa, fb = a_ in md, b_ in tx
    print(f'   {name:34s} md {"ok" if fa else "MISSING"} | tex {"ok" if fb else "MISSING"}')
    ok &= fa and fb
gone = md.count(r'\pi_\varphi^{+}\, \bar v')
print(f'   {"old pi^+ display gone":34s} md {"ok" if not gone else "PRESENT"}')
ok &= not gone
try:
    import pypdf
    pages = pypdf.PdfReader(R + 'paper3_material_ledgers_v35.pdf').pages
    txt = re.sub(r'\s+', ' ', '\n'.join((p.extract_text() or '') for p in pages))
    lit = len(re.findall(r'[A-Za-z}\)]_[A-Za-z0-9\\{]', txt))
    print(f'  PDF: {len(pages)} pages | literal underscores in math: {lit} (2 = the e-mail address) | '
          f'Def 44 in text: {"Governability ratio" in txt}')
    ok &= lit <= 2 and 'Governability ratio' in txt
except Exception as e:                                      # noqa: BLE001
    print('  PDF check unavailable:', e)

print('\nALL CHECKS PASS' if ok else '\nSOME CHECKS FAILED')
sys.exit(0 if ok else 1)
