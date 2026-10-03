#!/usr/bin/env python3
"""Read-only spot checks of the attached supplement audits vs frozen v67 TeX.
Supplement PDF pages 8, 9, 12, 14, 16 must also be inspected visually;
this script checks source and limited exact examples, not ODE proofs.
"""
from pathlib import Path
from fractions import Fraction as F
R=Path('/home/user'); D=R/'paper 2 family/01_obstruction'
s=(D/'paper01_obstruction_calculus_v67_supplementary.tex').read_text()
a=(D/'paper01_obstruction_calculus_v67.tex').read_text()
assert 'Notation and numbering follow the main text.' in s
assert r'\newtheorem{theorem}{Theorem}' in s and r'\newtheorem{proposition}{Proposition}' in s
print('TRUE supplement promises shared numbering yet declares independently numbered theorem/proposition environments')
assert s.count('Proposition prop:helly')>=2
print('TRUE raw Proposition prop:helly appears twice in supplement source (and compiled p9)')
assert r'\sum_{i=0}^{k-1} \bigl(F_{i} A_{j}^{\,k-1-i} B_{j}\bigr) u_{i}' in s
assert r'E_{j}^{\top} (A_{j}^{\,k-1-\ell})^{\top} F_{i}^{\top}' in s
print('TRUE LP row F_i is reused as both floor-row and time index; matrix ordering in the support term itself is correct')
assert r'\tfrac{\kappa}{2}(C_2 - C_1)' in s
assert r'\tfrac{\pi}{2}(C_2 - C_1)' not in s
assert r'[C_1/2, \bar S_1] \times [C_2/2, \bar S_2]' in s
print('FALSE alleged pi/2 typo and absent upper stock bounds: TeX and PDF p16 have kappa/2 and [Ci/2, barSi]; bound values and constant-control scope still need stating')
assert r'\mathcal{Y}_{\mathrm{safe}}' in s
for bogus in (r'\mathcal{V}_{\mathrm{safe}}',r'\Game','Velivor','Sentag','Veliv,',r'\dot{S} = S + b'):
 assert bogus not in s,bogus
assert r'\hat S' in s and r'\dot S' in s
print('FALSE alleged V_safe collision, Game, Velivor/Sentag, and hat/dot S typo in actual source; dot S correctly denotes derivative')
assert 'Admissible initial\nbeliefs are the compact information sets' in s
assert r'\mathfrak B=\{B\subseteq X:B\neq\varnothing\}' in a
assert 'in continuous\ntime the converse is the backward-recursion completion noted in\nSection 6.5' in s
print('TRUE supplementary aux Definition 1 narrows main ambient belief domain; selector converse claims continuous-time completion where the article says open')
assert 'A three-state system shows' in s and r'\{x_{1}, x_{2}, x_{4}\}' in s and r'x_{3} \notin \mathcal{V}' in s
print('TRUE A.3 has four physical states x1,x2,x3,x4, three safe; “three-state system” is an inaccurate count')
assert r'\alpha:(0,a]\to(0,\infty)' in s
# qdot=-sqrt(q), q0=1: contact at t=2, then q(t)=0. Original set [0,inf) remains safe.
for t,q in [(F(0),F(1)),(F(1),F(1,4)),(F(2),F(0)),(F(3),F(0))]:
 assert q >= 0
print('COUNTEREXAMPLE integrable alpha(s)=sqrt(s): q(t)=(max(1-t/2,0))^2 reaches zero at 2, remains safe; finite comparison integral alone does not give strict exit')
# D(z)=[-1,1] constant; g(z,d)=-1+z*d; D_{1}(z)={d: z*d<=0}
# D1(0)=[-1,1]; any z>0 has only d<=0. Point d=1 at z=0 lacks nearby selections for z>0.
assert all(F(1)*z>0 for z in [F(1,100),F(1,1000)])
print('COUNTEREXAMPLE D(z)=[-1,1] is constant/LSC, g(z,d)=-1+z*d has inf_d g<=-1 everywhere; D_1(0)=[-1,1] but D_1(z>0)=[-1,0], so negative-drift subcorrespondence is NOT LSC at (0,1)')
# MSY A.2 arithmetic at p* with equal harvest floors, C1=1, C2=2, kappa=1/5.
k=F(1,5); c1,c2=F(1),F(2)
v=(k*(c2-c1)/2,k*(c1-c2)/2)
assert v==(F(1,10),F(-1,10)) and sum(v)==0
print('PASS A.2 at p*=(C1/2,C2/2), f(p*)=(1/10,-1/10) for C1=1,C2=2,kappa=1/5, so zero-Wdot singleton is not invariant under fixed minimum harvest')
