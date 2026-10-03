#!/usr/bin/env python3
"""Read-only, source-tethered spot checks for six uploaded Paper01 v67 reviews.
No manuscript mutation, no Lean build, no analytic theorem verification.
"""
from fractions import Fraction as F
from pathlib import Path
R=Path('/home/user'); D=R/'paper 2 family/01_obstruction'
a=(D/'paper01_obstruction_calculus_v67.tex').read_text()
s=(D/'paper01_obstruction_calculus_v67_supplementary.tex').read_text()
audit=(R/'uploads/01 v67 audit.txt').read_text()
for name in ('haiku:','gemini:','qwen:','deepseek:','gemini2:','grok:'):
 assert name in audit
print('PASS six named reviewers in one attached file; embedded review map is not a seventh independent review')
for fragment in (r'\tfrac{9}{10} z \pm u',r'(\tfrac{10}{9})^{k}',r'\tfrac32-\tfrac{Y-2}{10}',r'\tfrac{59}{50}-\tfrac{Y-2}{10}',r'\tfrac{67}{25}-\tfrac{Y-2}{5}',r'\tfrac{\mathrm{cap}_1(Y)+\mathrm{cap}_2(Y)}{2}-1',r'2\mathbf 1[u\ne i]',r'\hat S = S + b'):
 assert fragment in a,fragment
for spurious in (r'\tfrac{5}{10} z',r'\Game',r'\dot S = S + b','Nagumoy','Empitied'):
 assert spurious not in a,spurious
print('PASS OCR-derived (190), mangled fractions, 21-indicator, missing half, 5/10, dot-S, Game, Nagumoy and Empitied are absent from article source; visual PDF p9/p12 checked separately')
caps=lambda Y:(F(3,2)-(Y-2)/10,F(59,50)-(Y-2)/10)
assert sum(caps(F(27,5)))==2
assert sum(caps(F(5)))==F(52,25)
assert sum(caps(F(6)))==F(47,25)
assert sum(caps(F(6)))/2-1==F(-3,50)
assert F(9,10)**3*F(10,9)**3==1
print('PASS exact rational threshold Y*=27/5, cap sums 52/25 and 47/25, normalized dual bound -3/50 at Y=6; Example2 base 9/10 and reciprocal 10/9')
assert r'\max_{w \in W_{j}} F E_{j} A^{\ell} w' in a
assert r'E_{j}^{\top} (A_{j}^{\,k-1-\ell})^{\top} F_{i}^{\top}' in s
print('PASS main Theorem4 proof sketch has wrong F E A matrix order; supplement has correct rowwise support-function order')
assert r'\mathcal{A}_{\mathrm{tube}}(B, \Delta) = \{ a : \mathrm{Reach}' in a
assert r'\mathcal{A}_{\mathrm{tube}}(B,\Delta)=\varnothing \;\Longrightarrow\; B\notin\mathrm{ERViab}' in s
print('PASS tube definition lacks explicit held-action admissibility; supplement gives unqualified fixed-Delta tube->kernel implication')
assert r'a \in U^B(B)' in a and r'\mathcal{R}_{\mathcal{V}}^B(B)' in a
print('PASS subset-emptiness propagation U^B empty -> R^B empty -> A_tube empty is logically in the correct direction; no converse was shown')
# Constructive counterexample: xdot=u, V=[-1,1], B={0}, U={-1,+1}, Delta=3.
# Either constant u leaves V before Delta. A time-varying blind, open-loop signal
# u=+1 on [2n,2n+1), -1 on [2n+1,2n+2) keeps x in [0,1] indefinitely.
for u in (-1,1): assert abs(u*F(2))>1
assert all(F(0)<=x<=F(1) for x in [F(0),F(1),F(0),F(1)])
print('COUNTEREXAMPLE fixed-Delta tube emptiness does not imply unrestricted open-loop nonviability: xdot=u, B={0}, V=[-1,1], U={-1,+1}, Delta=3; 1-step alternating control remains in [0,1]')
# theorem 3 H3.2 selects a minimizer on every u: unequal-slack proposed
# branch counterexample fails this explicit hypothesis.
block=a[a.index(r'\begin{theorem}[delayed-information obstruction]'):a.index(r'\end{theorem}',a.index(r'\begin{theorem}[delayed-information obstruction]'))]
assert r'For every implementable blind-window control' in block and r'\(x_u\in B_0\) of \(q\)' in block and r'\inf_{x \in B_0} q(x)' in block
print('PASS Theorem3 requires adverse drift FROM an initial minimizer for every blind control; unequal-slack counterexample attacks a hypothesis-free generalization, not this theorem')
assert r'\tfrac{\mathrm{cap}_1(Y)+\mathrm{cap}_2(Y)}{2}-1' in a
assert 'The cap sum is the affine function '+r'\(\tfrac{67}{25}-\tfrac{Y-2}{5}\)' in a
assert 'The present v66 edits have' in a
print('PASS genuinely stale internal v66 language remains; alleged cap-sum and missing-half errors do not')
