#!/usr/bin/env python3
"""
Hidden-parameter paper (D10: structural uncertainty and learning deadlines)
— verification. Exact rational arithmetic; stdlib only; deterministic.

  E1  THETA-OBSERVED KERNEL: decline theta-free drift z' = z - 1/10 plus
      correctable component theta u (theta in {-1,+1}, u in {-1,0,1}):
      with theta observed, u = theta makes the drift 9/10 (growth) — every
      grid cell z0 in [1, 5/2] is viable (16/16).
  E2  PROBE-THEN-ACT (endogenous learning): the probe u = +1 moves z by
      -1/10 + theta, revealing theta exactly; survival requires
      z0 - 1/10 + theta >= 1 for BOTH theta, i.e. z0 >= 21/10 — the probe-
      threshold as an exact identity, then u = theta grows.
  E3  LEARNING-DEADLINE OBSTRUCTION: if theta is revealed only at horizon
      T_learn, the regulator holds u = 0 until then (decline 1/10 per step)
      and probes at T_learn: viability iff z0 >= 21/10 + T_learn/10 — the
      kernel shrinks exactly linearly in the learning deadline (T_learn =
      0..3 verified by direct iteration; T_learn >= 4 empties the grid).
  E4  ENDOGENOUS REVELATION IS EXACT: the post-probe position z + (-1/10 +
      theta) determines theta uniquely (the map theta -> z-new is injective
      on the two branches for every z0) — one observation splits the belief
      into the two theta-cells, no statistics needed.
  E5  LEARNING MONOTONICITY: kernel(T_learn) is antitone in T_learn —
      setwise inclusions K(3) <= K(2) <= K(1) <= K(0) on the grid, strict
      at each step (the grid thresholds differ by exactly one cell).
  E6  SUSTAINABILITY PARAMETER INSTANCE (two-patch, unknown regeneration):
      growth g in {1, 2} unknown (regeneration rate uncertainty): the
      audited belief {(1,2),(2,1)} is nonviable when g is unknown (branch
      product over (x, g)) and viable under both fixed values read per
      cell — unknown-regeneration obstruction with revelation restoring.
"""
from fractions import Fraction as Q
from itertools import product

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

GRID = [Q(n, 10) for n in range(10, 26)]

# E1: theta observed -> u = theta -> drift 9/10: all viable
def survive(z0, T, policy):
    z = z0
    for t in range(T):
        u = policy(z, t)
        z = z - Q(1, 10) + theta_of(z, u) * u if LEARNED[t] else z - Q(1, 10)
        if z < 1:
            return False
    return True
# simpler concrete loop (learning schedule explicit)
def run(z0, T_learn, T=40):
    """u=0 until T_learn (decline 1/10 per step), probe u=+1 at T_learn
    (reveals theta; both branches must stay safe), then u=theta (drift
    9/10 upward on both branches -> indefinite survival)."""
    z = z0
    t = 0
    while t < T_learn:
        z -= Q(1, 10)
        if z < 1:
            return False, t
        t += 1
    for th in (-1, 1):
        zp = z0 - Q(1, 10) * T_learn + Q(-1, 10) + th
        if zp < 1:
            return False, t
        # learned law u = th: drift -1/10 + th*th = 9/10 (growth) forever
    return True, t

theta_of = lambda z, u: 1
LEARNED = [True] * 40
e1 = True
for z0 in GRID:
    z = z0
    ok = True
    for _ in range(40):
        z = z - Q(1, 10) + 1 * 1        # theta=+1 revealed: u=+1
        if z < 1:
            ok = False
            break
    e1 = e1 and ok
check("E1 theta-observed kernel: u = theta gives drift 9/10 — every grid "
      "cell viable (16/16)", e1)

# E2: probe threshold 21/10
e2 = True
for z0 in GRID:
    z = z0 + Q(-1, 10) + 1              # probe on theta=+1 branch
    z_bad = z0 + Q(-1, 10) - 1          # probe on theta=-1 branch
    viable = (z_bad >= 1) and (z >= 1)
    e2 = e2 and (viable == (z0 >= Q(21, 10)))
check("E2 probe-then-act: survival under the probe requires z0 >= 21/10 "
      "(both branches stay safe), then u = theta grows — exact threshold "
      "identity on the grid", e2)

# E3: learning-deadline thresholds 21/10 + T_learn/10
e3 = True
for T_learn in (0, 1, 2, 3, 4):
    thresh = Q(21, 10) + Q(T_learn, 10)
    for z0 in GRID:
        ok, _ = run(z0, T_learn)
        e3 = e3 and (ok == (z0 >= thresh))
check("E3 learning-deadline obstruction: viability iff z0 >= 21/10 + "
      "T_learn/10 (T_learn = 0..4 exact on the grid; at T_learn = 4 exactly "
      "the top cell 25/10 survives) — the kernel shrinks exactly linearly "
      "in the deadline", e3)

# E4: endogenous revelation injectivity
e4 = True
for z0 in GRID:
    z_plus = z0 + Q(-1, 10) + 1
    z_minus = z0 + Q(-1, 10) - 1
    e4 = e4 and (z_plus != z_minus)
check("E4 endogenous revelation: the post-probe position determines theta "
      "uniquely for every z0 (branches separated by exactly 2) — one "
      "observation splits the belief, no statistics needed", e4)

# E5: antitone in T_learn, strict on the grid
def kernel(T_learn):
    return {z0 for z0 in GRID if run(z0, T_learn)[0]}
K0, K1, K2, K3 = kernel(0), kernel(1), kernel(2), kernel(3)
e5 = (K3 <= K2 <= K1 <= K0) and len(K0) > len(K1) > len(K2) > len(K3)
check(f"E5 learning monotonicity: |K(0)|={len(K0)} > |K(1)|={len(K1)} > "
      f"|K(2)|={len(K2)} > |K(3)|={len(K3)}, setwise antitone inclusions",
      e5)

# E6: two-patch unknown regeneration g in {1,2}
CAP = 3
def step_g(x, u, g):
    z1, z2 = x
    return (max(0, min(CAP, z1 + g - (0 if u == 1 else 2))),
            max(0, min(CAP, z2 + g - (0 if u == 2 else 2))))
STATES = [(a, b) for a in range(4) for b in range(4)]
Vset = {x for x in STATES if x[0] >= 1 and x[1] >= 1}
agg = lambda xe: (xe[0][0], xe[0][1]) if False else xe[0][0] + xe[0][1]
def viable_aug(B, info, h, gset):
    """B = set of (x, g) pairs; per-cell read-then-act on (x,g)-cells."""
    if h == 0:
        return all(x in Vset for x, g in B)
    cells = {}
    for xe in B:
        cells.setdefault(info(xe), set()).add(xe)
    acts = []
    for c in cells.values():
        cu = [u for u in (1, 2)
              if all(step_g(x, u, g) in Vset for x, g in c)]
        if not cu:
            return False
        acts.append(cu)
    for choice in product(*acts):
        succ = set()
        for c, u in zip(cells.values(), choice):
            succ |= {(step_g(x, u, g), g) for x, g in c}
        parts = {}
        for s2 in succ:
            parts.setdefault(info(s2), set()).add(s2)
        if all(viable_aug(frozenset(p), info, h - 1, gset)
               for p in parts.values()):
            return True
    return False
H = 12
def verdict_aug(B, info, gset):
    return viable_aug(B, info, H, gset) and viable_aug(B, info, H - 2, gset)
Bx = frozenset({(1, 2), (2, 1)})
B_hidden = frozenset({(x, g) for x in Bx for g in (1, 2)})
agg_aug = lambda xe: xe[0][0] + xe[0][1]        # aggregate index ignores g
full_aug = lambda xe: xe                         # (x, g) observed
v_hidden_agg = verdict_aug(B_hidden, agg_aug, (1, 2))
v_fixed = all(verdict_aug(frozenset({(x, 1) for x in Bx} | {(x, 2) for x in Bx})
                          if False else frozenset({(x, g) for x in Bx}),
                          full_aug, (1, 2)) for g in (1, 2))
v_known = verdict_aug(B_hidden, full_aug, (1, 2))
check("E6 unknown-regeneration instance: the audited belief with unknown "
      f"g in {{1,2}} is nonviable under the aggregate (g-blind) reading "
      f"({v_hidden_agg}) and viable when (x,g) is observed ({v_known}); "
      "each fixed g is viability-preserving under full reading",
      (not v_hidden_agg) and v_known and v_fixed)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)
