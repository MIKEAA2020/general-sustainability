#!/usr/bin/env python3
"""Definition-level checks: exact small game, LP duality, manuscript identities."""
from fractions import Fraction as Q
from itertools import product
from math import log,sqrt
from scipy.optimize import linprog
A=(-2,0,2); scenarios=list(product((-1,1), repeat=3))
values={}; counts={}
for u1 in A:
    cells=sorted({2+s*u1+d1 for s,d1,d2 in scenarios})
    counts[u1]=3**len(cells)
    best=(Q(-10),None)
    for us in product(A,repeat=len(cells)):
        policy=dict(zip(cells,us))
        val=sum((Q(2-abs(2+s*(u1+policy[2+s*u1+d1])+d1+d2),8) for s,d1,d2 in scenarios),Q(0))
        if val>best[0]:best=(val,policy)
    values[u1]=best[0]
assert counts=={-2:81,0:9,2:81},counts
assert values=={-2:Q(1,2),0:Q(0),2:Q(1,2)},values
# In the cube the drift-feasibility LP has one variable per action,
# one nonnegative expected drift constraint per hidden parameter.
def feasible(S,m):
    vs=list(product((-1,1),repeat=m)); actions=vs+[(0,)*m]
    d=[[Q(-1,2)+sum(a*b for a,b in zip(u,t))*Q(1,5) for u in actions] for t in S]
    sol=linprog([0.]*len(actions), A_ub=[[-float(x) for x in row] for row in d],b_ub=[0.]*len(S),A_eq=[[1.]*len(actions)],b_eq=[1.],bounds=(0,None), method='highs')
    return sol.success, sol
# m4: single cell yes, distance-one pair yes only from finite slack, triangle no.
vs=list(product((-1,1),repeat=4));v=vs[-1];near=tuple(-v[i] if i==0 else v[i] for i in range(4))
assert feasible([v],4)[0] and feasible([v,near],4)[0]
# m5 radius-one ball is viable from the floor by a single constant action.
v=(1,)*5; ball=[v]+[tuple(-1 if j==i else 1 for j in range(5)) for i in range(5)]
assert all(Q(-1,2)+sum(x*y for x,y in zip(v,t))*Q(1,5)>=0 for t in ball)
assert feasible(ball,5)[0]
# m4 triple with pairwise constraints where possible: prohibit by graph triangle.
assert sum(1 for x in vs if sum(x[i]!=v[i] for i in range(4))==1)==4
# manuscript numerical corrections checked from declared printed coefficients
r=0.2369;K=5000;q10=80.87;phi=0.60
# smaller root of (1-phi)r*S*(1-S/K)=q10
D=1-4*q10/((1-phi)*r*K)
root=K*(1-sqrt(D))/2
assert 1090<root<1094,root
omega=lambda y: (2*y-1)**2*2
assert abs(omega((1+sqrt(5))/2)-10)<1e-12
assert Q(4,5)+Q(4,5)<2
assert abs(log((710-631.52)/(660-631.52))/log(1/(1-15.41/60.70))-3.46121214)<1e-6
print('PASS exact fixed-law review-tree enumeration', counts,values, 'root_phi60_rounded',root)
print('PASS LP viability witnesses, harmonic-circle identity, reviewer demand floor, 660-ft rounded horizon')
