#!/usr/bin/env python3
"""Exact counterchecks to minimax dynamic extensions. Run: python3 witnesses.py.
Does not change source scripts/manuscripts and does not refute the static
minimax theorem or the valid general DP when histories/null cells are handled.
"""
from fractions import Fraction as F

# thm:general permits arbitrary product probability measures, no full-
# support hypothesis. K=2, D1={0,1}, D2={0}, prior Dirac on (0,0),
# P1=P2={{(0,0)}, {(1,0)}}. Both partitions refine to singletons.
# A1=A2={0}, rational bounded G=0. On null C={(1,0)}, the recursion
# requests w(C')=mu(C')/mu(C)=0/0 for its singleton child: undefined.
paths=((0,0),(1,0))
mu={paths[0]:F(1),paths[1]:F(0)}
null=(paths[1],)
assert len(paths)==2 and sum(mu.values())==1 and sum(mu[p] for p in null)==0
try:
    _=sum(mu[p] for p in null)/sum(mu[p] for p in null)
    raise AssertionError('a null-cell ratio unexpectedly exists')
except ZeroDivisionError:pass
print('general envelope: allowed rational product Dirac prior creates a null tree node where printed w(C\u2032)=0/0 (undefined)')

# Under the *definition* Q(t)=ess sup over full policies of E[F^pi|F_t],
# maximizing over different PREVIOUS actions separately on each newly
# observed path is not a continuation of any original policy. Let a0
# be selected blind from {0,1}, reveal s in {0,1} with uniform prior,
# terminal G(s,a0)=1[a0=s]. Subsequent action is a dummy singleton.
policies=(0,1);states=(0,1)
payoff=lambda s,a: F(int(s==a))
root=max(sum(F(1,2)*payoff(s,a) for s in states) for a in policies)
pointwise={s:max(payoff(s,a) for a in policies) for s in states}
assert root==F(1,2) and pointwise=={0:F(1),1:F(1)}
assert sum(F(1,2)*pointwise[s] for s in states)==1>root
print('dynamic definition: Q(0)=1/2 but esssup over FULL policies after reveal gives Q(1)=1 everywhere, an unattainable pasted pre-action')
# New live v16 prior-art prose equates local common-action feasibility with
# nonemptiness of a global discriminating/viability domain. A deterministic
# special case of the standing continuous hypotheses refutes that unqualified
# identification: V=[0,1], x'=1, U={0}, D singleton, B={0}. The sole
# active facet at x=0 has inward derivative +1, so the local common action
# is feasible, but every x in V exits by t<=1, so the infinite-horizon
# viability (no-adversary discriminating) kernel is empty.
x0=F(0); q_lower=lambda x:x; q_upper=lambda x:1-x
assert q_lower(x0)==0 and q_upper(x0)>0 and F(1)>0
assert all(x+F(2)>1 for x in (F(0),F(1,2),F(1)))
print('live prior-art scope: local feasible action at x=0, but global viability/discriminating kernel of [0,1] is empty for x\u2032=1')
# This example satisfies thm:envelope-finite's stated finite/rational data.
# If b is just a posterior partition cell, its continuation value at t=1
# is 1 per cell; a blind pre-action cannot attain their average. Including
# the committed action in the DP node/history fixes the issue, as the later
# thm:general explicitly does by indexing N_k by action prefix.
