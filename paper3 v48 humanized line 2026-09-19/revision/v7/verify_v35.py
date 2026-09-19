#!/usr/bin/env python3
"""v35 checks: (1) log reversal v35 -> v34 byte-exact in both formats; (2) structure; (3) label
register; (4) the corrected claims present in both formats. All matching is plain substring, so that
backslash levels cannot distort a check: every pattern below is written in a raw string with the exact
number of backslashes the file contains."""
import json, re, sys

R = r'/home/user/revision/v7'
V = lambda f: open(f'{R}/paper3_material_ledgers_v{f}', encoding='utf-8').read()
A = {f: V(f) for f in ('34.md', '34.tex', '35.md', '35.tex')}
log = json.load(open(f'{R}/revisions_v35_kernel_log.json'))
ok = True

for fmt, key in (('md', '35.md'), ('tex', '35.tex')):
    t = A[key]
    for e in reversed(log):
        old = e['old'] if fmt == 'md' else e['old_tex']
        new = e['new'] if fmt == 'md' else e['new_tex']
        c = t.count(new)
        if c != 1:
            print(f'  !! {fmt}: {e["name"]}: new text occurs {c} times')
            ok = False
            continue
        t = t.replace(new, old)
    same = t == A['34.' + fmt]
    print(f'reversal {fmt} -> v34 byte-exact: {same}  ({len(t)} B rebuilt vs {len(A["34." + fmt])} B)')
    ok &= same

md, tx = A['35.md'], A['35.tex']
print('\n--- structure')
h_md = len(re.findall(r'^#{2,4} ', md, re.M))
h_tx = len(re.findall(r'\\(section|subsection|subsubsection|paragraph)\*?\{', tx))
print(f'headings md {h_md} vs tex {h_tx} -> ' + ('ok' if h_md == h_tx else 'MISMATCH'))
ok &= h_md == h_tx

pat = re.compile(r'\*\*(Definition|Proposition|Theorem|Corollary|Lemma|Remark|Example)\s+(\d+)')
labels = [(m.group(1), int(m.group(2))) for m in pat.finditer(md)]
reps = sorted({l for l in labels if labels.count(l) > 1})
maxima = {}
for k, n in labels:
    maxima[k] = max(maxima.get(k, 0), n)
print(f'statement labels {len(labels)} | repeats: {reps or "none"} | maxima: '
      + ', '.join(f'{k} {v}' for k, v in sorted(maxima.items())))
ok &= not reps
for k, want in (('Definition', 40), ('Remark', 34), ('Proposition', 39), ('Theorem', 24)):
    got = maxima.get(k)
    ok &= got == want
    print(f'  {k} max {got} (expect {want}) -> ' + ('ok' if got == want else 'CHECK'))
for k, n in (('Definition', 40), ('Remark', 34)):
    hit = rf'\textbf{{{k} {n} ' in tx
    ok &= hit
    print(f'  tex carries {k} {n}: {hit}')

print('\n--- corrected claims (md / tex), plain substring')
C = [
    ('orientation-free charge', r'$|\pi_\varphi|\,\bar v_\varphi T$', r'|\pi_\varphi|\,\bar v_\varphi T'),
    ('free iff pi >= 0', r'interface is free when $\pi_\varphi \ge 0$', r'interface is free when \(\pi_\varphi \ge 0\)'),
    ('ABSENT old pi^+ display', r'\pi_\varphi^{+}\, \bar v', r'\pi\_\varphi^{+}\, \bar v'),
    ('compatible conserved pairs', 'agree on every identified compartment', 'agree on every identified compartment'),
    ('merge destroys a moiety', 'the moiety of the first part is gone', 'the moiety of the first part is gone'),
    ('ker D^T rank condition', r'\ker D_J^{\top}', r'\ker D_J^{\top}'),
    ('sufficiency, no iff', 'certifies the composition whenever', 'certifies the composition whenever'),
    ('joint programme is the value fn', 'the value of the joint programme over the fibre product',
     'the value of the joint programme over the fibre product'),
    ('instance has pi = -1', r'$\pi = -1$', r'\pi = -1'),
    ('V dot sign fixed', r'G_2 b_2 - \sum_\varphi \pi_\varphi f_\varphi', r'G_2 b_2 - \sum_\varphi \pi_\varphi f_\varphi'),
    ('worst-case bound in proof', r'(-\pi_\varphi)^{+}\bar v_\varphi', r'(-\pi_\varphi)^{+}\bar v_\varphi'),
    ('Remark 34 box multipliers', r'$\lambda = 0$, $\rho = 1$', r'\lambda = 0\), \(\rho = 1'),
    ('Motzkin non-SOS', 'Motzkin', 'Motzkin'),
    ('interval from connectedness', 'interval image on a connected fibre', 'interval image on a connected fibre'),
    ('non-convex caveat', 'bound the value set from outside', 'bound the value set from outside'),
    ('noise typing', 'a diffusion that creates mass', 'a diffusion that creates mass'),
    ('drift bracket caveat', 'does not transfer to a bracket on its support', 'does not transfer to a bracket on its support'),
    ('Def 40 predicate', 'Compensation as a decidable predicate', 'Compensation as a decidable predicate'),
    ('price does not characterize', 'not by whether a capacity price is finite', 'not by whether a capacity price is finite'),
    ('premium 213 d', r'$\Pi_\tau = 213$', r'\Pi_\tau = 213'),
    ('premium 173 d', r'$173$ d', r'173'),
    ('convention declared', 'the convention is declared with the figure', 'the convention is declared with the figure'),
    ('C labelled correctly', 'moiety-composition matrix of Section 2.1', 'moiety-composition matrix of Section 2.1'),
    ('numbering to 40', '1\u201340 sequence counter', '1--40 sequence counter'),
    ('Remarks 33 and 34 in note', 'with Remarks 33 and 34,', 'with Remarks 33 and 34,'),
]
for name, a, b in C:
    if name.startswith('ABSENT'):
        fa, fb = a not in md, b not in tx
        print(f'  {name[8:]:32s} md {"ok (gone)" if fa else "STILL PRESENT"} | tex '
              + ('ok (gone)' if fb else 'STILL PRESENT'))
        ok &= fa and fb
        continue
    fa, fb = a in md, b in tx
    print(f'  {name:32s} md {"ok" if fa else "MISSING"} | tex {"ok" if fb else "MISSING"}')
    ok &= fa and fb

n_lstar = (md.count(r'\lambda^{*}'), tx.count(r'\lambda^{*}'))
print(f'  residual lambda-star               md {n_lstar[0]} | tex {n_lstar[1]} -> '
      + ('ok' if n_lstar == (0, 0) else 'CHECK'))
ok &= n_lstar == (0, 0)
print('\n--- display-math rendering fix')
for f in ('v34', 'v35'):
    s_ = V(f'paper3_material_ledgers_{f}.tex')
    segs = re.findall(r'\\\[[\s\S]*?\\\]', s_)
    print(f'  {f}: display regions {len(segs)} | escaped underscores inside them {sum(x.count(chr(92)+"_") for x in segs)}')

print('\nALL CHECKS PASS' if ok else '\nSOME CHECKS FAILED')
sys.exit(0 if ok else 1)
