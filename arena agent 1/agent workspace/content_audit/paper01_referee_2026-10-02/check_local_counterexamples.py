#!/usr/bin/env python3
"""Exact checks of limited v65 arithmetic and elementary counterexamples.
This does not prove global control/ODE assertions or validate the manuscript.
"""
from fractions import Fraction as F
# §3.4 Farkas witness: u<=2/5 and -u<=-3/5 cannot both hold.
A=(F(1),F(-1)); b=(F(2,5),F(-3,5));mu=(F(1,2),F(1,2))
assert sum(x*y for x,y in zip(mu,A))==0
assert sum(x*y for x,y in zip(mu,b))==F(-1,10)
print('PASS Farkas lambda=(1/2,1/2), normalized margin=1/10')
# §3.8 aggregate cap calculation: it is the SAME LP at each point of the fibre.
def caps(Y):return F(3,2)-(Y-2)/10,F(59,50)-(Y-2)/10
assert sum(caps(F(27,5)))==2
assert sum(caps(F(5)))==F(52,25)
assert sum(caps(F(6)))==F(47,25)
assert F(6,5)<=caps(F(5))[0] and F(4,5)<=caps(F(5))[1]
assert (2-sum(caps(F(6))))/2==F(3,50)
print('PASS aggregate LP Y*=27/5; sums 52/25 and 47/25; Y=6 margin=3/50')
# Prop 5: over S in [1,2], U(S)={0,S}, so common intersection is {0}.
assert {0,F(1)} & {0,F(3,2)} & {0,F(2)}=={0}
assert all(0<=1-s for s in [F(1),F(3,2),F(2)]) is False
assert all(1-s<=0 for s in [F(1),F(3,2),F(2)])
print('PASS Prop5 nonconvex common set={0}; constant u=1 viable only after controller-set convexification')
# Literal Theorem 3 example: q-minimum already zero, so drift only while q>0 is vacuous.
B=[F(0),F(1)];eps=F(1);T=F(1);xstar=min(B);f=F(0)
assert T>min(B)/eps
assert all(not (xstar>0) for _ in range(4))
assert all(F(0)<=x<=F(1) for x in B)  # stationary dynamics keep all safe
print('COUNTEREXAMPLE theorem3: B0=V=X=[0,1], O constant, f=0, q=x, x*=0, eps=T=1')
# Theorem 7: xdot=x-1, x(0)=1 is stationary; global boundary at 0 has drift -1.
assert F(1)-1==0 and F(0)-1<0
print('COUNTEREXAMPLE theorem7 global-boundary necessity: stationary x=1 viable in V=[0,2]')
