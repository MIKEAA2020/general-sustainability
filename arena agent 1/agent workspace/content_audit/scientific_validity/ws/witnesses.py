#!/usr/bin/env python3
"""Independent exact-arithmetic WS validity checks, not a Lean or full-paper proof.

Run python3 witnesses.py. Does not import the deposited verification script.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

# prop:bench (source §continuous benchmark): its OWN Y>=2 and cap>=0
# hypotheses include the critical feasible point, so zero dual margin
# cannot be an obstruction at equality.
Y = Q(27,5)
c1 = Q(3,2) - (Y-2)/10
c2 = Q(59,50) - (Y-2)/10
assert (c1,c2)==(Q(29,25),Q(21,25)) and c1+c2==2
u=(c1,c2)
assert all(0<=v<=cap for v,cap in zip(u,(c1,c2))) and sum(u)>=2
assert (2-c1-c2)/2==0
print('benchmark: Y=27/5 meets every stated hypothesis, u=(29/25,21/25) feasible; dual margin=0, not obstruction')

# prop:helly: the claimed general tight example with sum<=1 fails
# to be infeasible when m=1. m-dependent sum<=m-1 fixes the example.
assert Q(1)>=1 and Q(1)<=1
for m in range(1,6):
    all_ones=(1,)*m
    assert sum(all_ones)>m-1
    for omitted in range(m):
        trial=[1]*m;trial[omitted]=0
        assert sum(trial)<=m-1
print('Helly: published example u>=1, u<=1 is FEASIBLE for m=1; corrected m-dimensional example has m+1 essential constraints')

# Figure timing caption: strict against continuous tau loses exactly 3
# boundary cells; strict against floored sigma loses 21 cells, not 6.
viable=real_strict_loss=floor_strict_loss=0
for i,T in product(range(10,41), (1,2,3)):
    z=Q(i,10);tau=z-1;sigma=tau.numerator//tau.denominator
    is_ok=(T<=tau);viable+=is_ok
    real_strict_loss+=is_ok and not T<tau
    floor_strict_loss+=is_ok and not T<sigma
assert (viable,real_strict_loss,floor_strict_loss)==(33,3,21)
print('timing: 93 cells, 33 viable; strict-real loses 3; strict-floored loses 21 (caption says 1 and 6)')

# 'Each aggregate fibre mixes safe and unsafe states' is not true
# on the manuscript's X={0,1,2,3}^2 and safe floor >=1.
fibres={s:[(a,b) for a,b in product(range(4),repeat=2) if a+b==s]
        for s in range(7)}
safe=lambda x: x[0]>=1 and x[1]>=1
assert all(safe(x) for x in fibres[4]+fibres[5]+fibres[6])
assert any(safe(x) for x in fibres[3]) and any(not safe(x) for x in fibres[3])
print('aggregation: sums 4,5,6 are wholly state-safe; sum 3 mixes state-safe and unsafe')

# Independently enumerate deterministic stationary policies for 12 steps,
# without importing the deposited verifier's backward recursion.
V=tuple(product((1,2,3), repeat=2))
pairs=tuple(product(V, repeat=2))
pairs=tuple((a,b) for a,b in pairs if a<b)
def step(x,u):
    a,b=x
    return (min(3,a+1),max(0,b-1)) if u==1 else (max(0,a-1),min(3,b+1))
def safe_pair(B,pi,info):
    for x in B:
        for _ in range(12):
            x=step(x,pi[info(x)])
            if not safe(x):return False
    return True
def stationary_union(info,keys):
    union=set()
    for choices in product((1,2),repeat=len(keys)):
        pi=dict(zip(keys,choices))
        union.update(B for B in pairs if safe_pair(B,pi,info))
    return union
aggregate=stationary_union(sum,range(2,7))
full=stationary_union(lambda x:x,V)
assert len(aggregate)==0 and len(full)==28
print('stationary: independent 32 aggregate policies union to 0 pairs; 512 full-info policies union to 28')

# Script coverage is a source-fidelity check when the downloaded verifier
# is present; all mathematical witnesses above are independent of it.
source=Path(__file__).with_name('source_ws_v17_verification.py')
if source.is_file():
    src=source.read_text()
    assert 'range(1, 6)' in src and 'len(K_agg) == 26' in src
    print('regime DP: deposited P21 checks 1..5; manuscript advertises through six')
