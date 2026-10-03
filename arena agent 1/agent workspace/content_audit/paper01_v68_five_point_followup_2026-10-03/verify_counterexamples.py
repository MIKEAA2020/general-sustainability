#!/usr/bin/env python3
"""Read-only exact checks for follow-up proposal. These are counterexamples, not theorem proofs."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
R=Path(__file__).resolve().parents[2]
D=R/'paper 2 family/01_obstruction'
for filename,digest in [
 ('paper01_obstruction_calculus_v67.tex','4f5cc909e9035319e7056d9d9b8d64f60285d9a68bcf801cf5b8154aff9fad39'),
 ('paper01_obstruction_calculus_v67_supplementary.tex','99819f72de9c85570ab2daa2f8610ca5c1e8fb703d0a5be8c593b08f2022ce62')]:
 assert sha256((D/filename).read_bytes()).hexdigest()==digest
 print('PINNED',filename,digest)
# D(x)={1/x} for x>0 and {0} otherwise has closed graph and nonempty
# convex compact singleton values, but is not locally bounded at zero.
# f(x,d)=-2+x*d is continuous, affine in d, and bounded by 2 on the
# admissible graph. q=x, epsilon=1, D_epsilon is nonempty throughout.
def d(x):return Q(1)/x if x>0 else Q(0)
def vel(x):return -Q(2)+x*d(x)
assert vel(Q(0))==-2
assert all(vel(Q(1,n))==-1 for n in (2,10,1000))
assert all(vel(-Q(1,n))==-2 for n in (2,10))
print('COUNTEREXAMPLE_J1_1 D(x)={1/x} for x>0,{0} otherwise: closed graph/compact convex values and graph-bounded affine f=-2+xd, but Psi(x)={-1} for x>0 and {-2} at x=0; Psi not usc. This refutes the cited proof, not existence in every such model.')
# Nonconvex, uniformly bounded disturbance d=+/-1. N triangular cycles
# over time 1: terminal x=0, integral x^2 dt=1/(12N^2)>0. Limit
# (x,z)=(0,0) unattainable, since z=0 would require x=0 a.e.
for N in (1,2,5,20,100):
 z=Q(1,12*N*N)
 assert z>0
print('COUNTEREXAMPLE_POST_CLOSURE xdot=d in {+/-1}, zdot=x^2, initial (0,0): time-1 points (0,1/(12N^2)) approach unattainable (0,0); compact action values do not ensure closed ordinary reach.')
# Tolerance sensor h=id in R^2, rho=1. If endpoints distance>2
# no closed unit ball can contain both; at distance2 the midpoint does.
p=(-Q(1),Q(0));q=(Q(1),Q(0))
for N in (2,5,20):
 qn=(Q(1)+Q(1,N),Q(0))
 assert qn[0]-p[0]>2
assert q[0]-p[0]==2
print('COUNTEREXAMPLE_R3 rho=1, h=id: B={(-1,0),(1,0)} has two-point midpoint cell; B_N={(-1,0),(1+1/N,0)} has only singleton cells, so the two-point posterior cannot be approximated.')
# Exact threshold with a multivalued tie is a distinct observation model.
print('SENSOR_SCOPE exact y=1[x>=0] has a half-open negative cell; allowing both readings at 0 is a different, multivalued tie convention.')
# Nature-after-policy versus clairvoyant policy: an interval U=D=[-1,1]
# and g(u,d)=ud-1/2 has sup_u inf_d=-1/2, but for every d=+/-1
# a policy seeing d can choose u=d and obtain g=+1/2. A common d*=0
# exists and defeats all u; this illustrates timing and Sion's pointwise
# swap, not a refutation of the stronger H5.1^u premise.
for d0 in (Q(-1),Q(1)):
 assert d0*d0-Q(1,2)==Q(1,2)
assert Q(0)*Q(1)-Q(1,2)==-Q(1,2)
print('CHECK_INFORMATION_ORDER g=ud-1/2: policy seeing d=+/-1 can choose u=d and avoid negative drift, although a uniform d*=0 defeats all u; pointwise quantifier order must be typed.')
