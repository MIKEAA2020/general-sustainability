"""Independent audit of paper2_obstruction_calculus_v55 tab:patch (two-patch protection).
Model exactly as printed: z_i in {0,1,2,3}; u in {1,2};
  z_i^+ = min{3, z_i + 1 - 2*1[u != i]}
floor z_i >= 1 both; reading y = z1 + z2.
Beliefs are SETS of states (set-membership semantics), updated by the exact
belief-level recursion under blind (reading-dependent is disallowed: policies
are action sequences fixed in advance) control.
"""
from itertools import product
from fractions import Fraction

Z = range(0, 4)
STATES = [(a, b) for a in Z for b in Z]
def step(z, u):
    return tuple(min(3, z[i] + 1 - (0 if u == i + 1 else 2)) for i in (0, 1))
def safe(z):  return z[0] >= 1 and z[1] >= 1
V = frozenset(z for z in STATES if safe(z))
def rd(z):    return z[0] + z[1]

# --- full-information kernel: greatest fixpoint of z in V and exists u: step(z,u) in K
K = frozenset(V)
while True:
    nk = frozenset(z for z in K if any(step(z, u) in K for u in (1, 2)))
    if nk == K: break
    K = nk
claimed_kernel = V - frozenset({(1, 1)})
print("full-info kernel size", len(K), "| equals {z>=1}\\{(1,1)}:", K == claimed_kernel)
print("  (1,1) in kernel:", (1, 1) in K, "| (1,2),(2,1),(2,2) in kernel:",
      all(z in K for z in [(1,2),(2,1),(2,2)]))

# --- certainly-safe readings: y such that EVERY state with that y is safe
cert_safe = sorted({y for y in range(7) if all(safe(z) for z in STATES if rd(z) == y)})
print("certainly-safe readings:", cert_safe, "| claimed: exactly y >= 4 ->",
      cert_safe == [4, 5, 6])

# --- belief-level recursion under BLIND policies (action sequences, no feedback)
def viable_belief(B, H=40):
    """B: frozenset of states, all safe. Blind-viable: exists an action sequence
    of length H keeping every branch safe at every step (branching on nothing:
    the blind policy is one action per step applied to all branches)."""
    # belief update under blind policy: B_{t+1} = { step(z,u) : z in B }
    reach = {frozenset(B)}
    for _ in range(H):
        nxt = set()
        for C in reach:
            for u in (1, 2):
                D = frozenset(step(z, u) for z in C)
                if all(safe(z) for z in D):
                    nxt.add(D)
        if not nxt: return False
        reach = nxt
    return True

rows = [({(2,2)}, True, "u=(1,2) cycling"),
        ({(1,2),(2,2)}, True, "u=(1,2) cycling"),
        ({(2,1),(2,2)}, True, "u=(2,1) cycling"),
        ({(1,2),(2,1)}, False, "common-action"),
        ({(1,2),(2,1),(2,2)}, False, "common-action"),
        ({(1,1)}, False, "common-action")]
print("\nrow-by-row (blind viability, H=40):")
ok = True
for B, claimed, why in rows:
    got = viable_belief(frozenset(B))
    m = (got == claimed); ok &= m
    print(f"  {str(sorted(B)):38} claimed {'viable   ' if claimed else 'NONviable'} "
          f"got {'viable   ' if got else 'NONviable'} {'OK' if m else 'MISMATCH'}  ({why})")

# --- common-action certificate: safe-action sets of the belief's states have empty intersection
def safe_actions(z):  return frozenset(u for u in (1, 2) if safe(step(z, u)))
print("\ncommon-action certificate fires (empty intersection of safe-action sets):")
for B, claimed, _ in rows:
    if claimed: continue
    inter = frozenset({1, 2})
    for z in B: inter &= safe_actions(z)
    print(f"  {str(sorted(B)):38} intersection = {sorted(inter)}  "
          f"certificate fires: {len(inter) == 0}")

print("\nALL tab:patch ROWS CONFIRMED:", bool(ok) and K == claimed_kernel and cert_safe == [4,5,6])
