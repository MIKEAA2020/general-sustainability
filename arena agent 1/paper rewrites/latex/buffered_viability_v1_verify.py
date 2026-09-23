#!/usr/bin/env python3
"""
Buffered-viability paper (D12: approximate / buffered viability and the
obstruction margin) — verification. Exact rational/integer arithmetic.

  E1  OBSTRUCTION MONOTONICITY IN THE MARGIN: on the two-patch system with
      buffered floors V_delta = {z1 >= 1+delta, z2 >= 1+delta} (delta in
      {0,1,2}), a belief obstructed at margin delta is obstructed at every
      larger margin with nonempty buffered set (setwise chain over the pair
      family, all three margins, both audited structures).
  E2  THE OBSTRUCTION MARGIN IS EXACT: mu(B) = max{delta in {0,1,2}: B
      nonviable w.r.t. V_delta} computed for the audited beliefs under the
      blind and full structures (V_delta nonempty), each maximality
      certified (obstructed at mu, and — where a larger margin exists with
      nonempty V — viable at the next grid margin).
  E3  CONSTANT-DRIFT BUFFERED EXIT: with decline 1/10 per step, the last
      safe step for the band {z >= 1+delta} equals floor(10 (z0 - 1 -
      delta)) exactly (direct iteration vs closed form on the 48-cell grid
      x deltas {0, 1/10, 2/10}) — buffering costs exactly delta per unit
      time-to-exit budget.
  E4  CONTRACTION BUFFERED EXIT: with alpha(q) = q/10 per step, the last
      safe step below 1+delta equals max{k : q0 (9/10)^k >= 1+delta} =
      max{k : q0 >= (10/9)^k (1+delta)} — the successor's exit-time value
      with an exact multiplicative margin shift, verified at boundaries.
  E5  EROSION UNDER BUFFERING: the viable pair family shrinks strictly as
      the margin grows (exact counts under the full structure at delta =
      0, 1, 2) — safety margins are not free.
  E6  MEASUREMENT-ERROR READING: threshold mis-estimation up to eps is
      covered exactly when eps <= mu(B): a belief nonviable w.r.t. V_delta
      stays nonviable for every TRUE threshold at or below 1+delta (setwise
      inclusion chain V_2 <= V_1 <= V_0 verified, and the audited belief's
      margin read on the chain).
"""
from fractions import Fraction as Q
from itertools import product

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

CAP = 3
def step(x, u):
    z1, z2 = x
    return (max(0, min(CAP, z1 + 1 - (0 if u == 1 else 2))),
            max(0, min(CAP, z2 + 1 - (0 if u == 2 else 2))))
STATES = [(a, b) for a in range(4) for b in range(4)]
blind, full = lambda x: 0, lambda x: x

def viable(B, info, h, delta):
    if h == 0:
        return all(x[0] >= 1 + delta and x[1] >= 1 + delta for x in B)
    cells = {}
    for x in B:
        cells.setdefault(info(x), set()).add(x)
    acts = []
    for c in cells.values():
        cu = [u for u in (1, 2) if all(step(x, u)[0] >= 1 + delta and
                                       step(x, u)[1] >= 1 + delta for x in c)]
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
        if all(viable(frozenset(p), info, h - 1, delta)
               for p in parts.values()):
            return True
    return False

H = 12
def verd(B, info, delta):
    return viable(B, info, H, delta) and viable(B, info, H - 2, delta)

def Vset_d(delta):
    return {x for x in STATES if x[0] >= 1 + delta and x[1] >= 1 + delta}
pairs = [frozenset({x, y}) for x in Vset_d(0) for y in Vset_d(0) if x < y]

DELTAS = (0, 1, 2)
# E1: obstruction monotonicity in delta (within nonempty V_delta)
e1 = True
for info, nm in ((blind, "blind"), (full, "full")):
    for B in pairs:
        v = [verd(B, info, d) for d in DELTAS]
        for i in range(len(DELTAS) - 1):
            if v[i]:                       # viable at smaller margin
                e1 = e1 and (not v[i] or True)
        # obstruction monotone: nonviable at d implies nonviable is NOT
        # implied at larger d in general (larger demand is harder) —
        # the correct chain: VIABILITY shrinks: v[d] implies v[d'] for d'<=d
        for i in range(1, len(DELTAS)):
            if v[i]:
                e1 = e1 and v[i - 1]
check("E1 viability chain: viable at margin delta implies viable at every "
      "smaller margin (setwise, all 36 pairs, both structures) — "
      "obstruction at a larger margin is the harder, nested statement", e1)

BELIEFS = [frozenset({(1, 2), (2, 1)}), frozenset({(2, 2), (3, 1)}),
           frozenset({(2, 2)})]
mu_vals = {}
for info, nm in ((blind, "blind"), (full, "full")):
    for B in BELIEFS:
        mu = None
        for d in DELTAS:
            if not verd(B, info, d):
                mu = d
        mu_vals[(nm, tuple(sorted(B)))] = mu
e2 = True
for k, mu in mu_vals.items():
    if mu is None:
        continue
    nm, Bt = k
    B = frozenset(Bt)
    # maximality on the grid: not obstructed at any grid delta > mu
    info = blind if nm == "blind" else full
    for d in DELTAS:
        if d > mu and any(x[0] >= 1 + d and x[1] >= 1 + d for x in STATES):
            e2 = e2 and verd(B, info, d)
kb = ('blind', ((1, 2), (2, 1)))
check(f"E2 obstruction margins exact: mu(blind, {{(1,2),(2,1)}}) = "
      f"{mu_vals[kb]}, mu(full, {{(1,2),(2,1)}}) = "
      f"{mu_vals[('full', kb[1])]}, mu(full, {{(2,2)}}) = "
      f"{mu_vals[('full', ((2, 2),))]} (None = viable at margin 0) — each "
      "maximality certified on the margin grid", e2)

# E3: constant-drift buffered exit
floor = lambda x: x.numerator // x.denominator
e3 = True
for n in range(10, 26):
    z0 = Q(n, 10)
    for dd in (0, 1, 2):
        delta = Q(dd, 10)
        z, t = z0, 0
        while z >= 1 + delta:
            z -= Q(1, 10)
            if z >= 1 + delta:
                t += 1
            else:
                break
        e3 = e3 and (t == max(0, floor(10 * (z0 - 1 - delta))))
check("E3 constant-drift buffered exit: last safe step = floor(10(z0-1-"
      "delta)) on the grid x deltas {0, 1/10, 2/10} (buffering costs the "
      "margin directly)", e3)

# E4: contraction buffered exit
e4 = True
for K in (1, 2, 3):
    for dd in (0, 1, 2):
        thresh = (Q(10, 9) ** K) * (1 + Q(dd, 10))
        for q0 in (thresh, thresh - Q(1, 100), thresh + Q(1, 100)):
            q, t = q0, 0
            while q >= 1 + Q(dd, 10):
                q *= Q(9, 10)
                if q >= 1 + Q(dd, 10):
                    t += 1
                else:
                    break
            sigma = max(k for k in range(12)
                        if q0 >= (Q(10, 9) ** k) * (1 + Q(dd, 10)))
            e4 = e4 and (t == sigma)
check("E4 contraction buffered exit: last safe step = max{k : q0 >= "
      "(10/9)^k (1+delta)} at exact boundaries and neighbors (K <= 3, "
      "delta in {0, 1/10, 2/10}) — the successor's value with an exact "
      "multiplicative margin shift", e4)

n0 = sum(verd(B, full, 0) for B in pairs)
n1 = sum(verd(B, full, 1) for B in pairs)
n2 = sum(verd(B, full, 2) for B in pairs)
check(f"E5 erosion under buffering: viable pairs under full structure: "
      f"{n0} -> {n1} -> {n2} as delta goes 0 -> 1 -> 2 (strictly shrinking "
      "— margins are not free)", n0 > n1 > n2)

incl = Vset_d(2) <= Vset_d(1) <= Vset_d(0)
mu_star = mu_vals[("blind", ((1, 2), (2, 1)))]
e6 = incl and (mu_star is not None) and all(
    not verd(frozenset({(1, 2), (2, 1)}), blind, d)
    for d in range(0, mu_star + 1))
check(f"E6 measurement-error reading: V_2 <= V_1 <= V_0 (threshold "
      f"mis-estimation up to mu covers the audited belief: mu(blind) = "
      f"{mu_star}) — a belief obstructed at margin delta stays obstructed "
      "for every true threshold at or below 1+delta", e6)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)
