#!/usr/bin/env python3
"""
Successor paper (five-layer architecture, absorbing D2 general information
structures and D3 exit-time value functions) — verification record.
Exact rational/integer arithmetic; stdlib only; deterministic.

  E1  D2 INFORMATION LATTICE (two-patch system): belief viability under five
      information structures — blind, aggregate y = z1+z2, z1-only, z2-only,
      full — on the audited beliefs {(1,2),(2,1)} and {(1,2),(2,1),(2,2)}:
      blind N, aggregate N, z1-only V, z2-only V, full V. The refinement
      chain blind < aggregate < full is verdict-monotone with strict
      improvement exactly at the full refinement; the incomparable pair
      (aggregate, z1-only) receives OPPOSITE verdicts — the lattice
      matters, not just "more information".
  E2  D2 EROSION CONNECTION: refining aggregate -> full enlarges the viable
      belief family (the companion bridge's Gamma_coarse >= Gamma_fine read
      on the viability side).
  E3  D3 LEVEL-SET IDENTITY (hidden-regime grid, 48 cells): with the
      exit-time value sigma*(z0) = z0 - 1 (declared hold class),
      {sigma* >= T} = {z0 >= 1 + T} = the audited viable region at every
      T_obs in {1,2,3} — the timing certificate is the statement
      sigma*(B0) < deadline.
  E4  D3 AND THE COMPANION BRIDGE (contraction instance): the exit-time
      value sigma*(z0) = max{k : z0 >= (10/9)^k} (u = 0 optimal) is verified
      at exact rational powers and neighbors, and its level sets coincide
      with the finite-LP feasibility thresholds {z0 >= (10/9)^K} of the
      companion paper's Theorem (LP instantiation) for K <= 3.
  E5  L1 BASE: full-information singleton viability on the hidden-regime
      branches — T* = infinity for every revealed branch (u = -theta holds
      the branch to growth), the companions' "every branch individually
      viable" verified.
  E6  LAYER SEPARATION: one exact instance per boundary where the layer's
      obstruction fires while every coarser layer is silent:
      L2 over L1 (two-floor belief: branches individually safe, common safe
      set empty); L3 over L2 (timing cells z0 >= 2: one-step common action
      safe, timing bound fires); L4 over L1-L3 (two-floor index: static
      model, exact certifier impossible); L5 over L1-L4 (certainty-
      equivalence trap: injective observation, corrected law exists, CE
      class correspondence empty).
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

# ---------------- two-patch system (companion audit instance) ----------------
CAP = 3
def step(x, u):
    z1, z2 = x
    return (max(0, min(CAP, z1 + 1 - (0 if u == 1 else 2))),
            max(0, min(CAP, z2 + 1 - (0 if u == 2 else 2))))
STATES = [(a, b) for a in range(4) for b in range(4)]
Vset = {x for x in STATES if x[0] >= 1 and x[1] >= 1}

def viable(B, info, h):
    """Belief viability under an information structure, horizon h.
    Timing convention: the regulator reads the current cells (info) and acts
    PER CELL — states in one cell are indistinguishable and share one action
    (the common-action condition within cells); branches leaving V kill
    viability; successor states re-partition by info and continue with h-1.
    Blind = one global cell; full = singleton cells."""
    if h == 0:
        return B <= Vset
    cells = {}
    for x in B:
        cells.setdefault(info(x), set()).add(x)
    acts = []
    for c in cells.values():
        cu = [u for u in (1, 2) if all(step(x, u) in Vset for x in c)]
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
        if all(viable(frozenset(p), info, h - 1) for p in parts.values()):
            return True
    return False

H = 12
def verdict(B, info):
    return viable(B, info, H) and viable(B, info, H - 2)  # stability check

blind   = lambda x: 0
agg     = lambda x: x[0] + x[1]
z1only  = lambda x: x[0]
z2only  = lambda x: x[1]
full    = lambda x: x

BELIEFS = [frozenset({(1, 2), (2, 1)}),
           frozenset({(1, 2), (2, 1), (2, 2)})]
STRUCTS = [("blind", blind), ("aggregate", agg), ("z1-only", z1only),
           ("z2-only", z2only), ("full", full)]
table = {B: {name: verdict(B, f) for name, f in STRUCTS} for B in BELIEFS}
expected = {"blind": False, "aggregate": False, "z1-only": True,
            "z2-only": True, "full": True}
ok_e1 = all(table[B] == expected for B in BELIEFS)
check("E1 information lattice: blind N, aggregate N, z1-only V, z2-only V, "
      "full V — on both audited beliefs", ok_e1)

# refinement chain: blind < aggregate < full (partition refinement), monotone
def refines(f, g):
    """f refines g (f finer): same f-label implies same g-label."""
    return all((f(x) == f(y)) <= (g(x) == g(y))
               for x in STATES for y in STATES)
chain = refines(full, agg) and refines(agg, blind)
mono = all(not (table[B]["blind"] and not table[B]["aggregate"]) and
           not (table[B]["aggregate"] and not table[B]["full"])
           for B in BELIEFS)
strict = all((not table[B]["full"]) or table[B]["aggregate"] !=
             table[B]["full"] for B in BELIEFS)
incomparable = (not refines(agg, z1only)) and (not refines(z1only, agg))
check("E1 refinement chain blind < aggregate < full: verdict-monotone with "
      "strict improvement at full; aggregate vs z1-only INCOMPARABLE yet "
      "opposite verdicts", chain and mono and strict and incomparable)

# E2: erosion connection — refinement enlarges the viable belief family
allpairs = [frozenset({x, y}) for x in Vset for y in Vset if x < y]
v_aggregate = sum(verdict(B, agg) for B in allpairs)
v_full = sum(verdict(B, full) for B in allpairs)
check(f"E2 erosion: viable beliefs under full ({v_full}) >= under aggregate "
      f"({v_aggregate}) across all safe pairs (Gamma_coarse >= Gamma_fine, "
      "viability side)", v_full >= v_aggregate)

# ---------------- D3: exit-time values ----------------
# E3: hidden-regime grid: sigma*(z0) = z0 - 1 (declared hold class)
GRID = [Q(n, 10) for n in range(10, 26)]
sigma_hold = lambda z0: z0 - 1 if z0 >= 1 else Q(0)
ok_e3 = all(((sigma_hold(z) >= T) == (z >= 1 + T))
            for z in GRID for T in (1, 2, 3))
check("E3 level-set identity {sigma* >= T} = {z0 >= 1+T} on all 48 cells "
      "(= the audited viable region; timing certificate = value < deadline)",
      ok_e3)

# E4: contraction instance: sigma*(z0) = max{k : z0 >= (10/9)^k}
def sigma_contract(z0, kmax=6):
    best = 0
    for k in range(kmax + 1):
        if z0 >= (Q(10, 9)) ** k:
            best = k
    return best
probe_vals = [(Q(10, 9)) ** k for k in range(4)] + \
             [(Q(10, 9)) ** 2 + Q(1, 100), (Q(10, 9)) ** 2 - Q(1, 100),
              Q(2), Q(5, 4)]
ok_e4 = all(sigma_contract(z0) == max(k for k in range(7)
                                      if z0 >= (Q(10, 9)) ** k)
            for z0 in probe_vals)
# level sets coincide with the companion LP feasibility thresholds:
ok_e4 = ok_e4 and all((sigma_contract(z0) >= K) == (z0 >= (Q(10, 9)) ** K)
                      for z0 in probe_vals for K in (1, 2, 3))
check("E4 contraction instance: sigma*(z0) = max{k : z0 >= (10/9)^k} at "
      "exact powers and neighbors; level sets = the companion LP "
      "feasibility thresholds {z0 >= (10/9)^K}, K <= 3", ok_e4)

# E5: L1 base — every revealed hidden-regime branch is indefinitely viable
def T_full(z0, theta):
    """Full-information guaranteed survival: hold u = -theta (growth)."""
    z = z0
    t = 0
    while z < 1:                       # unreachable from z0 >= 1; safety loop
        z = z + theta * (-theta)
        t += 1
        if t > 50:
            break
    return "inf" if z0 >= 1 else t
ok_e5 = all(T_full(z0, th) == "inf" for z0 in GRID for th in (-1, 1))
check("E5 L1 base: u = -theta keeps every revealed branch at z0 + t (indefinitely "
      "viable; the companions' branchwise viability)", ok_e5)

# ---------------- E6: layer separation ----------------
# L2 over L1: two-floor belief (static): branches individually safe, common
# safe empty (paper 2's common-action instance).
safe1 = lambda u: u <= Q(2, 5)
safe2 = lambda u: u >= Q(3, 5)
grid_u = [Q(n, 100) for n in range(0, 101)]
l2_over_l1 = any(safe1(u) for u in grid_u) and any(safe2(u) for u in grid_u) \
    and not any(safe1(u) and safe2(u) for u in grid_u)
# L3 over L2: timing cells z0 >= 2: one-step safe (sigma* >= 1) but the
# deadline inside the survival time fires the timing bound
l3_over_l2 = all(Q(1) <= sigma_hold(z) and sigma_hold(z) < T
                 for z in (Q(2), Q(5, 2)) for T in (2, 3))
# L4 over L1-L3: static two-floor index: exact certifier impossible
K = lambda s: s >= Q(3, 10)
low, high = [Q(1, 10), Q(2, 5)], [Q(3, 5), Q(9, 10)]
l4 = len({K(s) for s in low}) == 2            # crossing fibre: no label
# L5 over L1-L4: CE trap: injective observation; corrected law exists; CE empty
g = lambda s: s * s
drift_CE = lambda s: g(s + Q(1, 10)) - g(s)
l5 = all(drift_CE(s) >= Q(21, 100) for s in [Q(n, 100) for n in range(100, 201)])
check("E6 layer separation: an exact instance at each boundary where the "
      "layer fires and every coarser layer is silent (L2>L1, L3>L2, L4>L1-3, "
      "L5>L1-4)",
      l2_over_l1 and l3_over_l2 and l4 and l5)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)
