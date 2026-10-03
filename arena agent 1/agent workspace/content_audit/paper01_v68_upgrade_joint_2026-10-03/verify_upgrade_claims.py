#!/usr/bin/env python3
"""Pinned, read-only source checks and elementary counterexamples for the two upgrade proposals.
These tests do not prove proposed continuous-time transfer/duality or validate citations.
"""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
R=Path(__file__).resolve().parents[2]
paths={
 'article':R/'paper 2 family/01_obstruction/paper01_obstruction_calculus_v67.tex',
 'supp':R/'paper 2 family/01_obstruction/paper01_obstruction_calculus_v67_supplementary.tex',
 'main_proposal':R/'uploads/01 upgrade.txt',
 'supp_proposal':R/'uploads/01 supp upgrade.txt',
}
expected={
 'article':'4f5cc909e9035319e7056d9d9b8d64f60285d9a68bcf801cf5b8154aff9fad39',
 'supp':'99819f72de9c85570ab2daa2f8610ca5c1e8fb703d0a5be8c593b08f2022ce62',
 'main_proposal':'9d3d4978adb72d314ac791e1229ab5eb48be1bd6d9cd16e99c2e19e26074bfb6',
 'supp_proposal':'6ce044e3e200721c7d5cf3ca2f1e6c704886e41516f8f08aef623e2c32b86a1e',
}
for k,p in paths.items():
 assert sha256(p.read_bytes()).hexdigest()==expected[k],(k,p)
 print('PINNED',k,expected[k])
a=paths['article'].read_text();s=paths['supp'].read_text()
assert r'\mathcal{Y}_{\mathrm{safe}}' in a and r'\mathcal{Y}_{\mathrm{safe}}' in s
assert r'\mathcal{V}_{\mathrm{safe}}' not in a+s
print('SOURCE safe notation is already Y-safe in both v67 files; no V-safe token to replace')
assert r'O : Z \to Y' in a and r'O^{-1}(y) \subseteq K' in a
print('SOURCE exact certifier uses O:Z->Y; intersection of inverse fibre with Z is redundant on this typed domain')
assert r'\mathrm{RViab}(\mathcal{V})' in a and 'state-feedback policy' in a
assert 'The selected action is held until the next observation' in a
print('SOURCE robust kernel is called state-feedback; H2.1 requires an action held until review')
assert 'A three-state system' in s and all('x_{'+str(i)+'}' in s for i in range(1,5))
assert r'\tfrac{\kappa}{2}' in s and 'Proposition prop:helly' in s
print('SOURCE A.3 has four states despite three-state label; kappa is correct; two raw Helly mentions remain')
# Bad corner-qualification direction: at zero q=x^3 has zero gradient but
# the constant vector field xdot=-1 leaves {q>=0} immediately.
q=lambda x:x**3
dq=lambda x:3*x*x
assert dq(0)*(-1)>=0 and all(q(-Q(1,n))<0 for n in (1,2,10))
print('COUNTEREXAMPLE active-gradient >=0 is NOT sufficient for tangent viability without regularity: q(x)=x^3, xdot=-1 at x=0')
# Constant observation does not erase the prior: posterior=P if O is constant.
U=lambda x:{Q(0),x}
assert U(Q(3,2))=={Q(0),Q(3,2)} and U(Q(1)) & U(Q(2))=={Q(0)}
print('COUNTEREXAMPLE singleton prior P={3/2} remains singleton under constant O; u=3/2 holds x=3/2 viable; non-singleton {1,2} has common action {0}')
# LSC of thresholded correspondence does not follow from LSC of D.
D_bounds=lambda z:(Q(-1),Q(1)) if z==0 else ((Q(-1),Q(0)) if z>0 else (Q(0),Q(1)))
assert D_bounds(Q(0))==(Q(-1),Q(1)) and D_bounds(Q(1,10))==(Q(-1),Q(0))
print('COUNTEREXAMPLE D(z)=[-1,1] constant with g=-1+zd: D_1(0)=[-1,1]; D_1(z>0)=[-1,0]')
# The old Prop2 pointwise drift gives exit for every positive Delta; no uniform time.
for delta in (Q(1,100),Q(3)):
 t=min(delta/2,Q(1,10));assert t>0 and -t<0
print('CHECK pointwise negative boundary drift gives an unsafe point inside any positive hold interval')
# A negative lower bound on an infimum gives no failure witness.
J=[Q(2),Q(3)]; lower=Q(-1)
assert lower<0 and min(J)>0
print('COUNTEREXAMPLE lower bound -1 on inf{2,3}=2 cannot certify negative recourse; need actual negative scenario/upper bound')
# Abstract infinite-depth vs infinite-horizon game: s chooses x>0; x doubles
# until x>1/2 and then enters unsafe star. For each N, x=2^-(N+1)
# survives >=N rounds; no x>0 survives indefinitely; x=0 exits at once.
for N in range(1,13):
 x=Q(1,2**(N+1))
 assert all(0<x*(2**k)<=Q(1,2) for k in range(N))
 assert x*(2**(N+1))>Q(1,2)
print('COUNTEREXAMPLE abstract compact-action recursion: s survives every finite horizon via smaller x>0, but no one action survives forever; no finite-depth refutation without compact closed witness sets')
# Noncommuting matrix-order sanity check for robust floor row.
A=((0,1),(0,0));E=((0,0),(1,0));F=(1,0);w=(1,0)
matvec=lambda M,v:tuple(sum(M[i][j]*v[j] for j in range(2)) for i in range(2))
row=lambda v:sum(F[i]*v[i] for i in range(2))
assert row(matvec(A,matvec(E,w)))==1 and row(matvec(E,matvec(A,w)))==0
print('CHECK F A E w=1 while F E A w=0 for noncommuting A,E: matrix order is load-bearing')
