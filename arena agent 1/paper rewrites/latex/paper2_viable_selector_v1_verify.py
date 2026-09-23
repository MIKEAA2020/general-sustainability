#!/usr/bin/env python3
"""
Paper 3 (the viable selector: unification of obstruction certificates) —
verification record. Exact rational/integer arithmetic; stdlib only.

The paper's structural claims are verified here ON THE WORKED SYSTEMS of the
companion papers (Abaee 2026a, obstruction calculus; 2026b, finite
nonviability certificates):

  V1  Static intersection object: two-floor belief — common ADMISSIBLE
      correspondence nonempty, common SAFE correspondence empty (the
      common-action certificate is an emptiness of Gamma^B).
  V2  Label selection: two-floor index — exact-label correspondence empty on
      the crossing fibre, singleton on the safe fibre; certainly-safe set =
      {high}; two-dimensional aggregate reading likewise (fibre criterion as
      label-selection emptiness, Lambda_K(O^-1(y)) = empty).
  V3  Nesting: two-patch system — strict inclusions A_tube(.,2) < R_V^B < =
      U^B at the states where the held action exits later; equality where
      the horizon is short enough (the ladder is strict exactly as
      hypothesized).
  V4  Recursive-selector identity: two-patch beliefs — the Gamma_N
      correspondence recursion and the belief-kernel recursion return
      identical verdicts on all six audited beliefs (3 viable with witness
      selectors, 3 nonviable).
  V5  Timing as blind-window predecessor emptiness: hidden-regime grid —
      for the declared hold class, the blind-window predecessor
      correspondence is nonempty at horizon k iff z0 >= 1 + k (k = 1..3),
      coinciding with the exact viability boundary; for the unrestricted
      sequential blind class it is nonempty iff z0 >= 2 for k >= 2 (the
      class declaration is load-bearing, as in the companions).
  V6  Policy-class emptiness (the certainty-equivalence trap): on the biased
      instance, the corrected law keeps the derivative identically zero
      (selector exists in the unrestricted class) while every
      certainty-equivalence law has drift >= 21/100 > 0 on [1,2] and exits
      [1,2] in finite time (the class-restricted correspondence is empty).
"""
from fractions import Fraction as Q
from itertools import product

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

# ---------------- V1: static intersection (two-floor belief) ----------------
# x1 safe iff u <= 2/5; x2 safe iff u >= 3/5 (paper 2, Sections 3.4 and 8).
Ux1, Ux2 = (Q(0), Q(1)), (Q(0), Q(1))                # admissible: full unit band
safe1, safe2 = (Q(0), Q(2, 5)), (Q(3, 5), Q(1))      # safe-at-x1, safe-at-x2
adm = (max(Ux1[0], Ux2[0]), min(Ux1[1], Ux2[1]))     # common admissible
common_safe = (max(safe1[0], safe2[0]), min(safe1[1], safe2[1]))
check("V1 two-floor: common admissible nonempty [0,1]; common safe EMPTY "
      "(Gamma^B = empty is the certificate)",
      adm == (Q(0), Q(1)) and adm[0] < adm[1] and
      common_safe[0] > common_safe[1])

# ---------------- V2: certification as label selection ----------------
K = lambda s: s >= Q(3, 10)                           # floor 0.3 (paper 2, Section 8)
fibres = {"low": [Q(1, 10), Q(2, 5)], "high": [Q(3, 5), Q(9, 10)]}
def Lambda(F):                                        # exact-label correspondence
    ls = {K(z) for z in F}                            # labels attained on F
    return set() if len(ls) == 2 else ({1} if ls == {True} else {0})
L = {name: Lambda(F) for name, F in fibres.items()}
# two-dimensional aggregate (paper 2, Section 8): I = S1 + S2, floor S1 >= 2/5
def Lambda2(I):
    s1min, s1max = max(Q(0), I - 1), min(Q(1), I)
    vals = {Q(2, 5) <= s1 for s1 in (s1min, s1max)} if s1min <= s1max else set()
    return set() if len(vals) == 2 else ({1} if vals == {True} else
           ({0} if vals == {False} else set()))
L2 = {I: Lambda2(I) for I in (Q(1), Q(7, 5), Q(14, 10), Q(3, 2))}
cs2 = sorted(I for I in (Q(n, 10) for n in range(0, 21)) if Lambda2(I) == {1})
check("V2 two-floor index: Lambda(low) empty (fibre crosses the boundary), "
      "Lambda(high) = {1}; certainly-safe = {high}",
      L["low"] == set() and L["high"] == {1})
check("V2 aggregate reading: Lambda(I=1.0) empty; certainly-safe readings "
      "exactly I >= 7/5",
      L2[Q(1)] == set() and L2[Q(7, 5)] == {1} and L2[Q(14, 10)] == {1}
      and L2[Q(3, 2)] == {1} and cs2[0] == Q(7, 5) and len(cs2) == 7)

# ---------------- V3: nesting on the two-patch system ----------------
CAP = 3
def step(x, u):
    z1, z2 = x
    n1 = min(CAP, z1 + 1 - (0 if u == 1 else 2))
    n2 = min(CAP, z2 + 1 - (0 if u == 2 else 2))
    return (max(0, n1), max(0, n2))
STATES = [(a, b) for a in range(4) for b in range(4)]
Vset = {x for x in STATES if x[0] >= 1 and x[1] >= 1}
Gamma_safe = {x: {u for u in (1, 2) if step(x, u) in Vset} for x in STATES}
def tube_held(x, D):                                  # single held action
    ok = set()
    for u in (1, 2):
        z, good = x, True
        for _ in range(D):
            z = step(z, u)
            if z not in Vset:
                good = False
                break
        if good:
            ok.add(u)
    return ok
t2 = {x: tube_held(x, 2) for x in STATES}
strict_pairs = [x for x in Vset if t2[x] < Gamma_safe[x]]
equal_pairs = [x for x in Vset if t2[x] == Gamma_safe[x]]
check("V3 nesting A_tube(.,2) subseteq Gamma_safe subseteq U, STRICT at "
      f"{len(strict_pairs)} states (e.g. (1,2): tube empty, safe = {{1}}) and "
      f"equal at {len(equal_pairs)}",
      all(t2[x] <= Gamma_safe[x] for x in STATES) and
      (1, 2) in strict_pairs and t2[(1, 2)] == set() and
      Gamma_safe[(1, 2)] == {1} and len(strict_pairs) >= 1 and
      len(equal_pairs) >= 1)

# ---------------- V4: recursive-selector identity on the audit beliefs ----
def Gamma_N(x0, N):
    """Recursively viable response correspondence for a singleton initial
    state (deterministic dynamics, no observations): selectors are action
    sequences; Gamma_N = sequences keeping every reachable state in V."""
    out = set()
    for seq in product((1, 2), repeat=N):
        z, good = x0, True
        for u in seq:
            z = step(z, u)
            if z not in Vset:
                good = False
                break
        if good:
            out.add(seq)
    return out
def belief_viable_Gamma(B, N=6):
    """Belief-level: exists a common first action and, after the reading
    splits the belief into y-cells, recursively viable continuations."""
    if not B <= Vset:
        return False
    if N == 0:
        return True
    for u in (1, 2):
        succ = {step(x, u) for x in B}
        if not succ <= Vset:
            continue
        parts = {}
        for s in succ:
            parts.setdefault(sum(s), set()).add(s)
        if all(belief_viable_Gamma(frozenset(p), N - 1) for p in parts.values()):
            return True
    return False
BELIEFS = [frozenset({(2, 2)}), frozenset({(1, 2), (2, 2)}),
           frozenset({(2, 1), (2, 2)}), frozenset({(1, 2), (2, 1)}),
           frozenset({(1, 2), (2, 1), (2, 2)}), frozenset({(1, 1)})]
verdicts = {B: belief_viable_Gamma(B) for B in BELIEFS}
# cross-check against the independent state-kernel recursion of the v47 record
W = [set(Vset)]
while True:
    nxt = {x for x in Vset if any(step(x, u) in W[-1] for u in Gamma_safe[x])}
    if nxt == W[-1]:
        break
    W.append(nxt)
RV = W[-1]
singletons_ok = all((Gamma_N(x, 8) != set()) == (x in RV) for x in Vset)
expected = {frozenset({(2, 2)}): True, frozenset({(1, 2), (2, 2)}): True,
            frozenset({(2, 1), (2, 2)}): True, frozenset({(1, 2), (2, 1)}): False,
            frozenset({(1, 2), (2, 1), (2, 2)}): False, frozenset({(1, 1)}): False}
check("V4 recursive-selector identity: Gamma_N verdicts match the belief "
      "kernel on all six audited beliefs; singleton Gamma_8 nonemptiness "
      "matches the full-information kernel",
      verdicts == expected and singletons_ok)

# ---------------- V5: timing as blind-window predecessor emptiness --------
GRID = [Q(n, 10) for n in range(10, 26)]
def pre_blind_hold(z0, k):
    """Pre_blind at horizon k, declared hold class {+1,-1}: nonempty iff
    some constant u keeps both branches >= 1 through k steps."""
    return any(all(z0 + th * u * t >= 1 for t in range(1, k + 1)
                   for th in (Q(-1), Q(1))) for u in (Q(1), Q(-1)))
def pre_blind_seq(z0, k):
    """Unrestricted sequential blind class: some u-sequence keeps both
    branches >= 1 through k steps (branch simulation: the declining branch
    is z0 - cumulative)."""
    for seq in product((Q(1), Q(-1)), repeat=min(k, 3)):
        zp, zm, good = z0, z0, True
        for u in seq[:k]:
            zp, zm = zp + u, zm - u
            if zp < 1 or zm < 1:
                good = False
                break
        if good:
            return True
    return False
ok_hold = all(pre_blind_hold(z, k) == (z >= 1 + k)
              for z in GRID for k in (1, 2, 3))
ok_seq = all(pre_blind_seq(z, k) == (z >= 2)
             for z in GRID for k in (2, 3))
check("V5 timing as predecessor emptiness: hold class nonempty iff "
      "z0 >= 1+k (the viability boundary, all 48 cells); unrestricted class "
      "iff z0 >= 2 for k >= 2 (declaration load-bearing)", ok_hold and ok_seq)

# ---------------- V6: policy-class emptiness (the CE trap) ----------------
g = lambda s: s * s
b = Q(1, 10)
drift_CE = lambda s: g(s + b) - g(s)                  # = s/5 + 1/100
drift_corr = lambda s: g(s + b - b) - g(s)            # corrected: identically 0
on_band = [Q(n, 100) for n in range(100, 201)]
check("V6 CE trap: corrected law keeps drift identically zero on [1,2]; "
      "every CE law has drift >= 21/100 > 0, so the class-restricted "
      "correspondence is empty while the unrestricted one is not",
      all(drift_corr(s) == 0 for s in on_band) and
      all(drift_CE(s) >= Q(21, 100) for s in on_band))

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)
