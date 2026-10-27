"""Independent checks for the v76 manuscript audit (standard library only).
This is not the author's verifier and is not a proof of continuum claims.
"""
from fractions import Fraction as F
from itertools import product
import json, math, pathlib

states = list(product([F(i,4) for i in range(7)], [F(i,4) for i in range(13)], [F(i,4) for i in range(13)]))
weights = [F(i,40) for i in range(41)]
checks = 0
for x,a,b in states:
    typ = x >= 1 or a >= 2 or b >= 2
    closed = x >= 1 or a+b >= 2
    probes = set(weights)
    for den,num in [(2-a+b,b),(a+2-b,a)]:
        if den and 0 <= num/den <= 1: probes.add(num/den)
    grid_accept = all(x>=1 or p*a+(1-p)*b >= min(2*p,2*(1-p)) for p in probes)
    assert grid_accept == closed
    assert (closed and not typ) == (x<1 and a<2 and b<2 and a+b>=2)
    # Derive the common-shock per-weight requirements directly from event deficits.
    cs_typ = (a>=2 and b>=F(1,2)) or (b>=2 and a>=F(1,2)) or (x>=1 and min(a,b)>=F(3,8))
    cs_closed = (x<1 and min(a,b)>=F(1,2) and a+b>=2) or (x>=1 and min(a,b)>=F(3,8))
    cs_numeric = True
    for p in probes:
        margin = p*a+(1-p)*b
        rf = max(2*p,p+F(1,2))
        rs = max(2-2*p,F(3,2)-p)
        rt = max(p,1-p)/2-F(1,8)
        if not (margin >= rf or margin >= rs or (x>=1 and margin >= rt)):
            cs_numeric=False
    assert cs_numeric == cs_closed
    assert not cs_typ or cs_closed
    checks += 1

# A finite full-amplitude switching example, distinct from the paper's
# full-excursion/union-tube assumption. Same deterministic primitive derivatives.
a=b=F(6,5)
switch_states=[(a,b)]
for coord,rate in [(0,-4),(1,-4),(0,4),(1,4)]:
    if coord==0: a+=F(rate,4)
    else: b+=F(rate,4)
    switch_states.append((a,b))
assert min(min(a,b) for a,b in switch_states)==F(1,5)

# Shared-shock canonical maximin margins with simplex-normalised weights.
pure = F(6,5)-2
blend = F(6,5)-F(5,4)
assert pure == -F(4,5) and blend == -F(1,20) and blend>pure

# Exact logistic closure endpoint: this is not the claimed returning straight line.
B=lambda b,t: 10/(1+(10/b-1)*math.exp(-4*t))
result={
  'states_checked':checks,
  'weight_probe_count_at_least':len(weights),
  'witness_and_common_shock_formula_checks':'passed on enumerated states/probes; not a continuum proof',
  'finite_switching_vertices':[list(map(str,z)) for z in switch_states],
  'shared_shock_pure_maximin_margin':str(pure),
  'shared_shock_balanced_blend_maximin_margin':str(blend),
  'benign_logistic_B_at_t1_from_B_half_1_7':B(1.7,.5),
  'adverse_logistic_B_at_t1_from_B_half_1_2':B(1.2,.5),
  'note':'Finite switching example falls outside the proposition\'s stipulated union-of-full-tubes class.'
}
print(json.dumps(result,indent=2))
pathlib.Path(__file__).with_name('independent_checks_results.json').write_text(json.dumps(result,indent=2)+'\n')
