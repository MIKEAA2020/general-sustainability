#!/usr/bin/env python3
"""Exact pair duals and symbolic all-facet witness bounds at T=6/5."""
from fractions import Fraction as Q
from math import sqrt
N=[(Q(1),Q(0)),(Q(-3,5),Q(4,5)),(Q(-3,5),Q(-4,5))]
U=N+[(-x,-y) for x,y in N]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
for pair,wt,t,rtest in [((0,1),(Q(3,8),Q(5,8)),Q(2,5),Q(1,4)),((0,2),(Q(3,8),Q(5,8)),Q(2,5),Q(1,4)),((1,2),(Q(1,2),Q(1,2)),Q(3,5),Q(2,5))]:
 v=tuple(sum(wt[j]*N[pair[j]][i] for j in range(2)) for i in range(2))
 h=max(dot(v,u) for u in U);assert h==t,(pair,v,h)
 # numerator for critical position minus 2 and its dual
 def margin(tau):return Q(-7,50)+(1-t)*tau-t*(1-t)*tau*tau/2
 ts=Q(1)+(1-t)*rtest
 assert ts<=Q(6,5) and margin(rtest)>0
 print('PAIR',pair,'weights',wt,'pooled',v,'support',h,'rational_tau',rtest,'t_star',ts,'dual_margin',margin(rtest))
# Exact irrational-root comparison by integer-squared rational brackets.
for t,lo,hi in [(Q(2,5),Q(2453,10000),Q(2454,10000)),(Q(3,5),Q(3973,10000),Q(3974,10000))]:
 m=lambda z:Q(-7,50)+(1-t)*z-t*(1-t)*z*z/2
 assert m(lo)<0<m(hi) and Q(1)+(1-t)*hi<Q(6,5)
 print('ROOT',t,'strict rational bracket',lo,hi,'dual signs',m(lo),m(hi))
# For any u in convex hull of unit vectors, n_i dot p_j(t) <=
# (34/25+t)n_i dot n_j+t^2/2 <=18/25 <2 when i != j, 0<=t<=6/5.
assert all(dot(N[i],N[j])<0 for i in range(3) for j in range(3) if i!=j)
assert Q(6,5)**2/2==Q(18,25)
# Critical coordinate increases through pre-control and post-control until rest;
# at root its maximum equals 2. Velocity components affine on each phase,
# so its maximum absolute component occurs at one of three junctions.
for pair,w,t,bound in [((0,1),(Q(-2,5),Q(-4,5)),Q(2,5),Q(2454,10000)),((0,2),(Q(-2,5),Q(4,5)),Q(2,5),Q(2454,10000)),((1,2),(Q(1),Q(0)),Q(3,5),Q(3974,10000))]:
 for j in pair:
  n=N[j];points=[n,tuple(n[i]+bound*w[i] for i in range(2)),tuple(bound*(w[i]+t*n[i]) for i in range(2))]
  vmax=max(abs(v) for p in points for v in p)
  assert vmax<Q(6,5),(pair,j,vmax)
  print('VELOCITY',pair,j,'upper_with_rational_tau_bound',vmax,'<6/5')
print('PASS pair dual, interval roots, all-time other-position and velocity bounds')
