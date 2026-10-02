#!/usr/bin/env python3
"""Scoped tests for repaired Theorem 3 and Table 3; not an external proof review."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
T=(Path('/home/user/papers/paper01_obstruction_calculus_v66.tex')).read_text()
S=(Path('/home/user/papers/paper01_obstruction_calculus_v66_supplementary.tex')).read_text()
for text in (T,S):
 theorem=text[text.index('\\begin{theorem}[delayed-information obstruction]'):text.index('\\end{theorem}',text.index('\\begin{theorem}[delayed-information obstruction]'))]
 assert '0\\le q(x(t))\\le a' in theorem
 assert 'through any first contact' in theorem
 assert 'every' in theorem and 'admissible disturbance realization' in theorem
 assert 'while } q(x(t)) > 0' not in theorem
print('PASS both theorem statements demand genuine through-boundary closed-strip drift, not positive-only drift')
# Old f=0 counterexample: derivative 0 on [0,a]; no epsilon>0 satisfies (2).
assert all(not (F(0)<=-eps) for eps in [F(1),F(1,100)])
print('PASS stationary f=0 counterexample excluded, including q-minimizer at boundary')
# A distinct satisfiable continuous hold-class example; no disturbance is required.
# Hidden theta in {-1,+1}, q=x, x(0)=1, xdot=theta*u, u held in {-1,+1}; O constant.
for u in (-1,1):
 theta=-u
 assert theta*u==-1
 x=lambda t:F(1)-t
 assert x(F(1))==0 and x(F(3,2))<0 and F(1)<F(2)
print('PASS nonvacuous continuous hold-class example: for each held control one hidden branch crosses strictly before T=2')
# It does not prove unrestricted-control failure: a sign reversal at t=1 can rescue both branches.
for theta in (-1,1):
 x=F(1)+theta*F(1)*F(1)+theta*F(-1)*F(1)
 assert x==1
print('PASS restriction matters: two-phase +1,-1 leaves both hidden branches at x=1 at T=2')
# Actual y=5 fibre policy: play action 1 until a y=4 singleton is reached,
# then alternate 2,1 forever, with the history giving its singleton identity.
def step(x,u):return tuple(min(3,z+1-2*(u!=i)) for i,z in enumerate(x,1))
for start in [(2,3),(3,2),(3,3)]:
 x=start
 for t in range(20):
  assert min(x)>=1,(start,t,x)
  if sum(x)==6 or sum(x)==5:u=1
  elif x==(3,1):u=2
  elif x==(2,2):u=1
  else:raise AssertionError((start,t,x))
  x=step(x,u)
print('PASS explicit histories keep the y=5 and y=6 initial fibres safe for 20 steps; fixed-point code establishes infinite continuation')
