#!/usr/bin/env python3
"""Exact finite-belief recursion for the v65 two-patch example, not a proof of other claims."""
from itertools import combinations
S=[(a,b) for a in range(1,4) for b in range(1,4)]
A=(1,2)
def step(x,u):
 a,b=x
 return (min(3,a+1-2*(u!=1)),min(3,b+1-2*(u!=2)))
def successors(B,u):
 nx={step(x,u) for x in B}
 if not nx <= set(S):return None
 return {frozenset(x for x in nx if sum(x)==y) for y in {sum(x) for x in nx}}
allbeliefs={frozenset(B) for n in range(1,len(S)+1) for B in combinations(S,n)}
W=set(allbeliefs);rounds=0
while True:
 rounds+=1
 nextW={B for B in W if any((succ:=successors(B,u)) is not None and succ <= W for u in A)}
 if nextW==W:break
 W=nextW
print('safe_physical_states',len(S),'possible_nonempty_safe_beliefs',len(allbeliefs),'fixed_point_rounds',rounds,'viable_beliefs',len(W))
for y in range(2,7):
 B=frozenset(x for x in S if sum(x)==y)
 if B:print('fibre',y,sorted(B),'viable',B in W,'one_step_safe_actions',[u for u in A if successors(B,u) is not None])
for row in [[(2,2)],[(1,2),(2,2)],[(2,1),(2,2)],[(1,2),(2,1)],[(1,2),(2,1),(2,2)],[(1,1)]]:
 B=frozenset(row)
 print('table_row',sorted(B),'one_reading',len({sum(x) for x in B})==1,'viable_if_given_as_one_initial_belief',B in W)
