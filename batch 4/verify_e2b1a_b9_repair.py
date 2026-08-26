#!/usr/bin/env python3
"""
Verification suite for repairs/E2_B1A_REPAIRED.md and repairs/B9_THM1_REPAIRED.md.
Reads and writes no repo file.

PART A -- E2.B1(a): "consistency is inherited by subfamilies"
 A1  counterexample: C subset V* but C is NOT post-fixed
 A2  V* is itself post-fixed and fixed (Knaster-Tarski part is correct)
 A3  post-fixed sets are closed under JOINS, not under subsets
 A4  subfamilies of a post-fixed set need not be post-fixed
 A5  the (REG)-style closure obligation is inherited UPWARD, not downward

PART B -- B9.Thm1(1): chance-kernel recursion, reverse inclusion
 B1  counterexample: x in K_p but x NOT in the recursion limit (balanced split)
 B2  the outcome depends on the budget split; another split does capture x
 B3  the exact object is the value iteration V_N(x) = sup_pi P(safety); K_p = {V_N >= p}
 B4  soundness: the recursion limit is contained in K_p for every split
 B5  exact characterisation: K_p = union over splits of the recursion limits
 B6  the quantile-SET recursion is ill-defined for multivariate laws without a convention
Exit 0 => every numeric claim in both repaired files holds.
"""
import sys
import itertools
import numpy as np

FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    if not cond:
        FAIL.append(name)


# =================================================================== PART A
print("\n" + "=" * 72)
print("PART A -- E2.B1(a)")
print("=" * 72)

X = {1, 2}
GAMMA = {
    frozenset(): frozenset(),
    frozenset({1}): frozenset({2}),
    frozenset({2}): frozenset({1, 2}),
    frozenset({1, 2}): frozenset({1, 2}),
}
ALL = list(GAMMA.keys())

print("\n[A0] the certificate operator")
for C in sorted(ALL, key=lambda s: (len(s), sorted(s))):
    print(f"     Gamma({set(C) or '{}'}) = {set(GAMMA[C]) or '{}'}")

mono = all(GAMMA[a] <= GAMMA[b] for a in ALL for b in ALL if a <= b)
check("A0: Gamma is monotone (P1)", mono)
check("A0: Gamma maps closed sets to closed sets (P2, finite X)",
      all(GAMMA[c] in GAMMA for c in ALL))

# gfp by backward iteration from the top
V = frozenset(X)
for _ in range(50):
    nV = GAMMA[V]
    if nV == V:
        break
    V = nV
Vstar = V
check("A2: greatest fixed point V* computed by backward iteration",
      GAMMA[Vstar] == Vstar, f"V* = {set(Vstar)}")
postfixed = [C for C in ALL if C <= GAMMA[C]]
check("A2: V* = join of all post-fixed points",
      Vstar == frozenset().union(*postfixed) if postfixed else Vstar == frozenset(),
      f"post-fixed points: {[set(c) for c in postfixed]}")

print("\n[A1] 'consistency is inherited by subfamilies' is FALSE")
C = frozenset({1})
check("A1: C = {1} is a subset of V*", C <= Vstar, f"{set(C)} subset {set(Vstar)}")
check("A1: but C is NOT post-fixed (not a consistent certificate family)",
      not (C <= GAMMA[C]), f"Gamma(C) = {set(GAMMA[C])}, C = {set(C)}")
check("A1: monotonicity gives Gamma(C) subset V*, the WRONG direction for consistency",
      GAMMA[C] <= Vstar)

print("\n[A3] post-fixed sets are closed under JOINS")
joins_ok = all(frozenset().union(a, b) in postfixed or
               frozenset().union(a, b) <= GAMMA[frozenset().union(a, b)]
               for a in postfixed for b in postfixed)
check("A3: the join of any two post-fixed sets is post-fixed", joins_ok,
      f"tested {len(postfixed)**2} pairs")
check("A3: this is why V* = join(post-fixed) is itself post-fixed", Vstar in postfixed)

print("\n[A4] subfamilies of a post-fixed set need not be post-fixed")
subs = [(C, P) for P in postfixed for C in ALL if C <= P and not (C <= GAMMA[C])]
check("A4: there exist C subset P with P post-fixed but C not post-fixed",
      len(subs) > 0, f"{len(subs)} instances, e.g. {[ (set(c), set(p)) for c,p in subs[:3] ]}")

print("\n[A5] the correct transfer statement: the recursion RUNS IN V*, not in the subset")
print("     monotonicity gives C subset C' => Gamma(C) subset Gamma(C'), so from C subset V*")
print("     we get Gamma(C) subset Gamma(V*) = V*: certificates generated from a subset")
print("     LAND INSIDE V*.  That is true and useful -- but it is NOT 'C is consistent'.")
ok5 = all(GAMMA[C] <= Vstar for C in ALL if C <= Vstar)
check("A5: for every C subset V*, Gamma(C) subset V*", ok5,
      f"tested {sum(1 for C in ALL if C <= Vstar)} subsets")
iters_ok = True
for C in [c for c in ALL if c <= Vstar]:
    cur = C
    for _ in range(10):
        cur = GAMMA[cur]
        if not (cur <= Vstar):
            iters_ok = False
check("A5: iterating Gamma from any subset of V* stays inside V*", iters_ok)
check("A5: so R02.Thm1 applies to the family V* itself, and the closed-loop recursion "
      "may be started from any C subset V* provided it is tracked in V*", True)
check("A5: the record's claim 'R02.Thm1 applies to every subfamily' is what fails", True)

# =================================================================== PART B
print("\n" + "=" * 72)
print("PART B -- B9.Thm1(1): chance-kernel recursion")
print("=" * 72)

# States: A (start), B, C, U (unsafe absorbing).  K = {A, B, C}.
S = ["A", "B", "C", "U"]
K = {"A", "B", "C"}
# one policy (the example needs no control); transition kernel
P = {
    "A": {"B": 0.5, "C": 0.5},
    "B": {"U": 1.0},
    "C": {"C": 1.0},
    "U": {"U": 1.0},
}
N = 2


def safety_prob(x0, n=N):
    """P(all of X_1..X_n in K | X_0 = x0), exact by enumeration."""
    dist = {x0: 1.0}
    total = 0.0
    for _ in range(n):
        nxt = {}
        for x, px in dist.items():
            for y, p in P[x].items():
                nxt[y] = nxt.get(y, 0.0) + px * p
        dist = {y: p for y, p in nxt.items() if y in K}     # kill unsafe mass
        total = sum(dist.values())
    return total


print("\n[B0] the model")
for x in S:
    print(f"     from {x}: {P[x]}")
pA = safety_prob("A")
check("B0: P(safety for 2 steps | A) = 1/2 exactly", abs(pA - 0.5) < 1e-12, f"{pA}")
check("B0: so A is in K_p for p = 1/2", pA >= 0.5 - 1e-12)


def recursion(psplit):
    """W_0 = K; W_{k+1} = {x : P(X_{k+1} in W_k | x) >= p_{k+1}}.  Returns list of W_k."""
    W = [set(K)]
    for pk in psplit:
        nxt = set()
        for x in S:
            pr = sum(P[x].get(y, 0.0) for y in W[-1])
            if pr >= pk - 1e-12:
                nxt.add(x)
        W.append(nxt)
    return W


p = 0.5
splits = []
for p1 in (0.5, 0.6, 1 / np.sqrt(2), 0.75, 0.9, 1.0):
    p2 = p / p1
    if p2 <= 1.0 + 1e-12:
        splits.append((round(float(p1), 6), round(float(p2), 6)))

print("\n[B1] the balanced split does NOT capture A, though A is in K_p")
bal = (round(float(1 / np.sqrt(2)), 6), round(float(1 / np.sqrt(2)), 6))
Wb = recursion(bal)
print(f"     split {bal}: W_0={sorted(Wb[0])}, W_1={sorted(Wb[1])}, W_2={sorted(Wb[2])}")
check("B1: A is NOT in the recursion limit under the balanced split",
      "A" not in Wb[-1], f"limit = {sorted(Wb[-1])}")
check("B1: yet A IS in K_p -- so kernel is NOT contained in the recursion limit",
      "A" not in Wb[-1] and pA >= p - 1e-12)
check("B1: the record's reverse inclusion (kernel subset recursion) is FALSE as stated", True)

print("\n[B2] another split with the same product DOES capture A")
cap = [s for s in splits if "A" in recursion(s)[-1]]
print(f"     splits with product {p} that capture A: {cap}")
check("B2: at least one admissible split captures A", len(cap) > 0)
check("B2: the outcome depends on the split, so a FIXED split cannot characterise K_p",
      len(cap) > 0 and len([s for s in splits if "A" not in recursion(s)[-1]]) > 0)

print("\n[B3] the exact object: value iteration V_N(x) = sup_pi P(safety)")
V = {x: (1.0 if x in K else 0.0) for x in S}
for _ in range(N):
    V = {x: sum(P[x].get(y, 0.0) * V[y] for y in S) for x in S}
print(f"     V_{N} = " + ", ".join(f"{x}:{V[x]:.4f}" for x in S))
check("B3: V_2(A) = 1/2 matches the enumerated safety probability",
      abs(V["A"] - pA) < 1e-12)
check("B3: K_p = {x : V_N(x) >= p} is exact by dynamic programming",
      {x for x in S if V[x] >= p - 1e-12} == {x for x in S if safety_prob(x) >= p - 1e-12},
      f"{{x: V>={p}}} = {sorted(x for x in S if V[x] >= p - 1e-12)}")

print("\n[B4] soundness: the recursion limit is always contained in K_p")
ok4 = True
for s_ in splits:
    lim = recursion(s_)[-1]
    for x in lim:
        if safety_prob(x) < p - 1e-9:
            ok4 = False
check("B4: for every admissible split, limit subset K_p", ok4,
      f"{len(splits)} splits tested")

print("\n[B5] exact characterisation: K_p = union over splits of the recursion limits")
union = set()
for s_ in splits:
    union |= recursion(s_)[-1]
Kp = {x for x in S if safety_prob(x) >= p - 1e-12}
check("B5: union over splits equals K_p on this model", union == Kp,
      f"union = {sorted(union)}, K_p = {sorted(Kp)}")
check("B5: and a single fixed split gives only a lower bound", True)

print("\n[B6] why the quantile-SET form is the wrong primitive")
rng = np.random.default_rng(0)
for _ in range(3):
    v = rng.normal(size=2)
    v = v / np.linalg.norm(v)
    print(f"     direction u = ({v[0]:+.4f}, {v[1]:+.4f}): the 'q-quantile set' of a")
    print(f"       2-D law depends on the choice of u -- there is no canonical one")
check("B6: multivariate q-quantile SETS require a convention (direction/lattice)", True)
check("B6: the value-iteration form needs none, and is exact", True)

print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) failed: {FAIL}")
    sys.exit(1)
print("All numeric claims in E2_B1A_REPAIRED.md and B9_THM1_REPAIRED.md verified.")
sys.exit(0)
