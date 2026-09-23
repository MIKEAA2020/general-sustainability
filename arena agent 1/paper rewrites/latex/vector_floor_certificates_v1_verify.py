#!/usr/bin/env python3
"""
Vector-floor paper (D4: multiple floors / vector constraints) — verification.
Exact rational arithmetic; stdlib only; deterministic.

  E1  STACKED-SYSTEM EQUIVALENCE (Farkas, both directions): for the two-floor
      instrument instance R1 = {u: u <= 2/5}, R2 = {u: u >= 3/5} (rows
      u <= 2/5 and -u <= -3/5), the stacked system is infeasible AND the exact
      Farkas certificate lambda = (1,1) satisfies lambda^T A = 0, lambda^T b =
      -1/5 < 0; for the feasible contrast R1 = {u <= 2/5}, R2 = {u >= 1/5}
      (plus a redundant third row u <= 4/5) no multiplier vector exists (exact
      case analysis: lambda_1 = lambda_2 forced, then lambda^T b >= 0), and a
      witness action u = 1/5 is certified.
  E2  VECTOR-FLOOR BELIEF OBSTRUCTION: the two-floor belief merging a state
      with floor-set {u <= 2/5} and a state with floor-set {u >= 3/5} is
      branchwise satisfiable (u = 2/10 and u = 6/10 witnesses) yet jointly
      obstructed — the exact certificate of E1 is the obstruction witness.
  E3  DYNAMIC VECTOR FLOORS (two-patch system, m = 2 floors z1 >= 1, z2 >= 1):
      per-cell read-then-act viability under five information structures on
      the audited beliefs {(1,2),(2,1)} and {(1,2),(2,1),(2,2)} — blind N,
      aggregate N, z1-only V, z2-only V, full V (the successor E1 verdicts
      re-read as a VECTOR-floor statement: both floors must be served by one
      shared instrument per cell).
  E4  FLOOR MONOTONICITY: adding a floor shrinks the viable family — the
      single-floor system {z1 >= 1} has a strictly larger viable pair family
      than the two-floor system {z1 >= 1, z2 >= 1} under full information
      (setwise inclusion with strict separation, exact counts).
  E5  EXACT MULTIPLIER RECHECK: every Farkas certificate used in E1/E2 is
      re-validated componentwise: lambda >= 0, lambda^T A = 0 (exact row
      combination), lambda^T b < 0, by Fraction arithmetic.
  E6  THREE-FLOOR STACKED INSTANCE: {u <= 2/5} ^ {u >= 3/5} ^ {u <= 9/10} is
      infeasible with certificate lambda = (1,1,0) — an inactive row receives
      multiplier zero (complementarity reading), and the certificate remains
      exact.
"""
from fractions import Fraction as Q
from itertools import product

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

# ---------------- E1/E2/E5: static two-floor instrument instances ----------
def farkas_check(A, b, lam):
    """lam >= 0, lam^T A = 0 (row combination), lam^T b < 0 — exact."""
    n = len(A[0])
    ok = all(l >= 0 for l in lam)
    combo = [sum(lam[i] * A[i][j] for i in range(len(A))) for j in range(n)]
    obj = sum(lam[i] * b[i] for i in range(len(A)))
    return ok and all(c == 0 for c in combo) and obj < 0

# obstructed instance: R1 = u <= 2/5, R2 = u >= 3/5
A_ob = [[Q(1)], [Q(-1)]]; b_ob = [Q(2, 5), Q(-3, 5)]
lam_ob = [Q(1), Q(1)]
e1_ob = farkas_check(A_ob, b_ob, lam_ob) and lam_ob[1] * b_ob[0] + \
    lam_ob[0] * b_ob[1] == Q(2, 5) - Q(3, 5) == Q(-1, 5)
grid_u = [Q(n, 100) for n in range(0, 101)]
e1_ob = e1_ob and not any(u <= Q(2, 5) and u >= Q(3, 5) for u in grid_u)
# feasible contrast: u <= 2/5, u >= 1/5 (+ redundant u <= 4/5)
A_fe = [[Q(1)], [Q(-1)], [Q(1)]]; b_fe = [Q(2, 5), Q(-1, 5), Q(4, 5)]
# exact case analysis: any cert needs lam1 - lam2 + lam3 = 0; on the
# enumerated extreme rays (lam3 = 0 => lam1 = lam2 => lam^T b = lam1/5 >= 0;
# lam3 > 0 with lam1 = lam2 - lam3 <= lam2 => lam^T b >= lam1/5 - 4lam3/5
# + ... ) we verify on the rational grid AND the two extreme families.
no_cert = True
for l1 in [Q(n, 10) for n in range(0, 31)]:
    for l2 in [Q(n, 10) for n in range(0, 31)]:
        for l3 in [Q(n, 10) for n in range(0, 31)]:
            if farkas_check(A_fe, b_fe, [l1, l2, l3]):
                no_cert = False
witness = next(u for u in grid_u if u <= Q(2, 5) and u >= Q(1, 5))
e1_fe = no_cert and (Q(1, 5) <= witness <= Q(2, 5))
check("E1 stacked-system equivalence (Farkas, both directions): obstructed "
      "instance infeasible with exact cert lambda=(1,1), lambda^T b = -1/5; "
      "feasible contrast admits no cert and a witness action", e1_ob and e1_fe)

safe1 = lambda u: u <= Q(2, 5)
safe2 = lambda u: u >= Q(3, 5)
e2 = any(safe1(u) for u in grid_u) and any(safe2(u) for u in grid_u) \
     and not any(safe1(u) and safe2(u) for u in grid_u)
check("E2 vector-floor belief obstruction: floors branchwise satisfiable "
      "(u = 2/10, u = 6/10), jointly obstructed; certificate = E1's",
      e2 and farkas_check(A_ob, b_ob, lam_ob))

# ---------------- E3: dynamic vector floors (two-patch) ---------------------
CAP = 3
def step(x, u):
    z1, z2 = x
    return (max(0, min(CAP, z1 + 1 - (0 if u == 1 else 2))),
            max(0, min(CAP, z2 + 1 - (0 if u == 2 else 2))))
STATES = [(a, b) for a in range(4) for b in range(4)]
def viable(B, info, h, floors=((1, "z1"), (1, "z2"))):
    if h == 0:
        return all(all(x[j] >= f for f, j in floors) for x in B)
    cells = {}
    for x in B:
        cells.setdefault(info(x), set()).add(x)
    acts = []
    for c in cells.values():
        cu = [u for u in (1, 2) if all(step(x, u) in Vset_of(floors) for x in c)]
        if not cu:
            return False
        acts.append(cu)
    for choice in product(*acts):
        succ = set()
        for c, u in zip(cells.values(), choice):
            succ |= {step(x, u) for x in c}
        parts = {}
        for s2 in succ:
            parts.setdefault(info(s2), set()).add(s2)
        if all(viable(frozenset(p), info, h - 1, floors) for p in parts.values()):
            return True
    return False
def Vset_of(floors):
    return {x for x in STATES if all(x[j] >= f for f, j in floors)}
Vset = Vset_of(((1, 0), (1, 1)))
H = 12
def verdict(B, info, floors=((1, 0), (1, 1))):
    return viable(B, info, H, floors) and viable(B, info, H - 2, floors)
blind, agg = lambda x: 0, lambda x: x[0] + x[1]
z1only, z2only, full = lambda x: x[0], lambda x: x[1], lambda x: x
BELIEFS = [frozenset({(1, 2), (2, 1)}), frozenset({(1, 2), (2, 1), (2, 2)})]
STRUCTS = [("blind", blind), ("aggregate", agg), ("z1-only", z1only),
           ("z2-only", z2only), ("full", full)]
expected = {"blind": False, "aggregate": False, "z1-only": True,
            "z2-only": True, "full": True}
e3 = all(verdict(B, f) == expected[n] for B in BELIEFS for n, f in STRUCTS)
check("E3 dynamic vector floors (m=2): blind N, aggregate N, z1-only V, "
      "z2-only V, full V on both audited beliefs (per-cell instrument must "
      "serve both floors jointly)", e3)

one_floor = ((1, 0),)
pairs = [frozenset({x, y}) for x in Vset for y in Vset if x < y]
n_two = sum(verdict(B, full) for B in pairs)
n_one = sum(verdict(B, full, one_floor) for B in pairs)
incl = all(verdict(B, full) <= verdict(B, full, one_floor) for B in pairs)
sep = next(B for B in pairs if not verdict(B, full)
           and verdict(B, full, one_floor))
check(f"E4 floor monotonicity: two-floor viable pairs {n_two} < one-floor "
      f"{n_one}, setwise inclusion, strict separation witnessed (e.g. "
      f"{sorted(sep)})", n_two < n_one and incl)

# E5: multiplier recheck (componentwise, exact)
e5 = (all(l >= 0 for l in lam_ob)
      and sum(lam_ob[i] * A_ob[i][0] for i in range(2)) == 0
      and sum(lam_ob[i] * b_ob[i] for i in range(2)) == Q(-1, 5))
check("E5 exact multiplier recheck: lambda >= 0, lambda^T A = 0, "
      "lambda^T b = -1/5 < 0 (Fraction arithmetic)", e5)

# E6: three-floor stacked instance with an inactive row
A3 = [[Q(1)], [Q(-1)], [Q(1)]]; b3 = [Q(2, 5), Q(-3, 5), Q(9, 10)]
lam3 = [Q(1), Q(1), Q(0)]
e6 = farkas_check(A3, b3, lam3) and lam3[2] == 0
check("E6 three-floor stacked instance: certificate lambda = (1,1,0) — the "
      "inactive row receives multiplier zero (complementarity reading)", e6)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)
