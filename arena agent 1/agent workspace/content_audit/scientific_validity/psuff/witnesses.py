#!/usr/bin/env python3
"""Exact hypothesis-checked witnesses for P3/psuff. Run: python3 witnesses.py.
No manuscript edits. All arithmetic is rational and states/actions are finite.
"""
from fractions import Fraction as Q

# prop:pathdeficit's SENSOR EXAMPLE claims optimized deficit eps for every
# prior and explicitly says no deterministic reading->action map does
# better. Let states x1,x2 have masses 99/100,1/100 and sensor error
# eps=1/20. Each action ai is safe only at xi. Constant map a(y)=a1
# is admissible for every reading and loses only the x2 branch: 1/100.
w=Q(99,100);eps=Q(1,20)
constant_deficit=1-w
assert constant_deficit==Q(1,100)<eps
# For eps<1/2 the optimal two-state Bayes loss equals
# min(eps,w,1-w), enumerated over all four deterministic maps.
def loss(a_left,a_right):
 return w*((1-eps)*int(a_left!=1)+eps*int(a_right!=1)) + (1-w)*(eps*int(a_left!=2)+(1-eps)*int(a_right!=2))
losses={(a,b):loss(a,b) for a in (1,2) for b in (1,2)}
assert min(losses.values())==constant_deficit and losses[(1,1)]==constant_deficit
assert losses[(1,2)]==eps
print('prop:pathdeficit sensor example: at b=(99/100,1/100), eps=1/20, constant admissible reading-map loses 1/100 < eps; optimized deficit is not eps for every prior')

# prop:dr(i) is correct: one-stage inf=(1-rho)E_p v+rho min v.
# But its (ii) does NOT distribute through repeated backups. Finite
# absorbing model Xperp={s,bot}, A={a}, T(s|s,a)=1/2,
# T(bot|s,a)=1/2, T(bot|bot,a)=1. Observation reveals the successor
# exactly: y_s from s and y_bot from bot. The belief starts at delta_s.
# For V0(s)=1,V0(bot)=0 the stated recursive operator gives at s
# V_{k+1}^rho=(1-rho)*(1/2)*V_k^rho(s) + rho*0.
p=Q(1,2);rho=Q(1,2)
def value(r,k):
 v=Q(1)
 for _ in range(k):v=(1-r)*p*v
 return v
assert value(rho,2)==Q(1,16)
assert (1-rho)*value(Q(0),2)+rho*value(Q(1),2)==Q(1,8)
print('prop:dr(ii): two-stage survival V_2^(1/2)=1/16, but interpolated endpoint values give 1/8; finite absorbing normalized rational model')
# prop:dr(iii) says concave in belief at EVERY rho, including rho=0.
# Source itself has the two-floor instance: two safe states, two
# deterministic actions each preserving only its own state, with
# absorbing bot for the other. One-step V1(b)=max(b(s1),b(s2)).
e1=Q(1);e2=Q(1);middle=max(Q(1,2),Q(1,2))
assert middle==Q(1,2)<(e1+e2)/2
print('prop:dr(iii): at rho=0, two-floor V1=max(b1,b2) is convex, not concave (midpoint 1/2 < endpoints 1)')
# prop:additivelaw: theta in {-1,+1}, scalar additive drift c(u)+h(u)*theta,
# actions fixed: hold c=-1/2,h=+1/2; probe c=-1/2,h=-1/2;
# post-learn c=+1,h=0 (common action, hence eligible for both theta).
# T=1, unit-duration hold and probe; floor=1. Worst hold and probe
# losses each equal1 but are attained at DIFFERENT theta values.
Th=(-1,1);drift=lambda c,h,theta:c+h*theta
hold={t:drift(-Q(1,2),Q(1,2),t) for t in Th}
probe={t:drift(-Q(1,2),-Q(1,2),t) for t in Th}
learn={t:drift(Q(1),Q(0),t) for t in Th}
d0=max(-v for v in hold.values());ep=max(-v for v in probe.values())
assert d0==ep==1 and min(learn.values())==1
z0=Q(2);paths={t:(z0,z0+hold[t],z0+hold[t]+probe[t]) for t in Th}
assert paths=={-1:(Q(2),Q(1),Q(1)),1:(Q(2),Q(2),Q(1))}
assert all(min(path)>=1 for path in paths.values())
assert z0<1+d0+ep
print('prop:additivelaw: both branches survive from z0=2, yet printed iff demands z0>=3 (hold/probe worst losses occur on opposite theta)')
# Actual threshold for this example is 2; at z0<2 a branch ends below
# the floor after its own -1 loss. In general with nonpositive hold/probe
# drift the maximum of the COMBINED branch loss is required, not the sum
# of independent maxima.
assert max(-(hold[t]+probe[t]) for t in Th)==1
