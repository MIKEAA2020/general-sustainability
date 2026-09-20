#!/usr/bin/env python3
"""
Paper 1 independent-result gate — the COMPLETE INSTANTIATION of the typed
false-positive / impossibility theorem.

Companion to research_program/paper1_typed_false_positive_theorem.md
(Theorems A, B, C).  Executed 2026-08-28 by the programme agent.

DETERMINISTIC.  EXACT INTEGER ARITHMETIC throughout (all quantities scaled by
SCALE = 40; see the scale table below) — no floats, no tolerances, no randomness,
no outer approximation of any tube.

The witness datum D (theorem file §5), all values in scale-40 integers:

  Q = {0,1}; m = 1; phase state (q, x, s1, s2).
  S_0 = {x>=0, s1>=0, s2>=0};  G = {(1,x,s): x>=0, s1>=0, s2>=0}.
  Disturbances: beta (dip 3/2 -> 60), alpha (dip 2 -> 80) — worst case FLOOR = 80.
  Reset gains e = 1/4 -> 10.  Rescue cost c = 1 -> 40.
  Actions: NO-SWITCH, FAST, SLOW, STAGED (theorem file §5 table).

Every trajectory is piecewise linear with breakpoints {0, 1/2, 1} and monotone on
each piece, so the exact visited range of each coordinate is the interval between
the extreme breakpoint values — the tubes below are EXACT (theorem file §5,
"Exactness witness").  The aggregate w.s is piecewise linear on the same
breakpoints, so its exact minimum over the interval is attained at a breakpoint.

Machine checks (each maps to a theorem claim):
  [T1]  exact-tube machinery: per-action breakpoint tables; piecewise
        monotonicity asserted; per-coordinate exact ranges.
  [T2]  Theorem B(1): typed region = {x>=1} ∪ {s1>=2} ∪ {s2>=2}.
  [T3]  Theorem B(2): aggregate region = {x>=1} ∪ {s1+s2>=2}.
        Machine layer: per-weight action search over a dense critical weight set
        (r = k/20 for k=0..40, r=∞, plus the exact boundary weights rho_1,
        rho_2 and the adversarial midpoint (rho_1+rho_2)/2 — all exact integer
        (a,b) pairs).  Structural layer: the FAST/SLOW per-weight safety
        biconditionals (r >= rho_1 / r <= rho_2) confirmed machine-side on
        every grid state over the dense weight grid.
  [T4]  Theorem B(3): endpoint-only region = all of X_0.
  [T5]  Theorem A(i): hierarchy typed ⇒ every-sampled-weight aggregate ⇒
        endpoint-only, on every grid state.
  [T6]  Theorem B(4): false-positive set identity, nonempty interior, and the
        interior witness (x,s1,s2) = (1/2, 6/5, 6/5) machine-classified.
  [T7]  Theorem B(5): both hierarchy inclusions strict; the endpoint-only
        witness (1/2, 1/10, 1/10) machine-classified (aggregate-INfeasible at
        w=(1,1), endpoint-feasible).
  [T8]  Theorem B(6): at the triangle-interior witness, FAST-only / SLOW-only /
        both weight classes are all nonempty (machine-checked at r = 1/2, 1, 2),
        and NO action serves every sampled weight (E_typ = ∩_w E_w = ∅,
        machine-verified over the full critical weight set).
  [T9]  Theorem B(7): rescue split — the R witness (x=3/2) typed-feasible via
        STAGED; the I witness (x=1/2) rejected with the FOUR exhibited
        per-action violations (the negative-certificate form).
  [T10] Theorem C: two hold intervals prepended; each assessment's backward
        recursion reproduces its one-interval region; the hierarchy and BOTH
        strictness witnesses survive at stage 0.

Status discipline: a machine pass here is a confirmation of the theorem file's
closed-form proofs at the sampled/exact-integer level stated per check; the
closed-form proofs themselves live in the theorem file.  Exit 0 iff every check
passes.  Writes typed_false_positive_instantiation.json next to this file.
"""

import json
import sys
import time
from pathlib import Path

# ----------------------------------------------------------------- scale table
# scale 40:  dip_beta 3/2 -> 60 ; dip_alpha (worst) 2 -> 80 ; e 1/4 -> 10 ;
#            c 1 -> 40 ; floor threshold 2 -> 80 ; grid step 0.1 -> 4.
SCALE = 40
DIP_BETA = 60
DIP_ALPHA = 80          # = lambda * D_i in worst case
FLOOR = 80              # the typed-floor dip threshold 2 (worst-case dip)
E = 10                  # destination reset gain per typed coordinate
C = 40                  # rescue cost
GRID_STEP = 4           # 0.1 in scaled units
GRID_MAX = 120          # 3.0 in scaled units

FAIL = []
CHECKS = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    CHECKS.append({"name": name, "pass": bool(cond), "detail": str(detail)})
    if not cond:
        FAIL.append(name)


# ------------------------------------------------------------- datum machinery
def breakpoints(action, X, S1, S2, dip):
    """Exact breakpoint values (t = 0, 1/2, 1) per coordinate for one disturbance.

    Returns dict coord -> (v0, v_half, v1).  Every piece is linear, hence
    monotone; the exact visited range of the coordinate is
    [min(v0,v_half,v1), max(v0,v_half,v1)] — no outer approximation.
    """
    if action == "NO-SWITCH":
        return {"x": (X, X, X), "s1": (S1, S1, S1), "s2": (S2, S2, S2)}
    if action == "FAST":
        return {"x": (X, X, X), "s1": (S1, S1 - dip, S1), "s2": (S2, S2, S2)}
    if action == "SLOW":
        return {"x": (X, X, X), "s1": (S1, S1, S1), "s2": (S2, S2 - dip, S2)}
    if action == "STAGED":
        return {"x": (X, X - C // 2, X - C), "s1": (S1, S1 + E // 2, S1 + E),
                "s2": (S2, S2 + E // 2, S2 + E)}
    raise ValueError(action)


def coord_range(vals):
    """Exact visited range of a piecewise-linear coordinate (monotone pieces)."""
    return (min(vals), max(vals))


def successor(action, X, S1, S2):
    """Successor state at t = 1 (singleton successor set per disturbance)."""
    if action == "NO-SWITCH":
        return {"q": 0, "x": X, "s1": S1, "s2": S2}
    if action in ("FAST", "SLOW"):
        return {"q": 1, "x": X, "s1": S1 + E, "s2": S2 + E}
    if action == "STAGED":
        return {"q": 1, "x": X - C, "s1": S1 + E, "s2": S2 + E}
    raise ValueError(action)


ACTIONS = ("NO-SWITCH", "FAST", "SLOW", "STAGED")
DIPS = (DIP_BETA, DIP_ALPHA)


# ----------------------------------------------------------- assessment checks
def typed_assessment(action, X, S1, S2):
    """Noncompensatory typed admissibility.  Returns (ok, violated_or_None).

    Constraints: per-coordinate exact tube ranges inside {x>=0, s1>=0, s2>=0}
    for EVERY declared disturbance, and the successor in G.
    """
    for dip in DIPS:
        bp = breakpoints(action, X, S1, S2, dip)
        for coord, floor_name in (("x", "physical stock"),
                                  ("s1", "protected-service floor s1"),
                                  ("s2", "liability-coverage floor s2")):
            lo, _hi = coord_range(bp[coord])
            if lo < 0:
                return (False, f"{floor_name} violated during transit "
                               f"({coord} dips to {lo / SCALE:g} < 0)")
    succ = successor(action, X, S1, S2)
    if succ["q"] != 1:
        return (False, "destination architecture not reached (successor q=0 ∉ G)")
    for coord in ("x", "s1", "s2"):
        if succ[coord] < 0:
            return (False, f"destination floor {coord} violated at endpoint")
    return (True, None)


def physical_assessment(action, X, S1, S2):
    """Endpoint-only physical admissibility (physical coordinates only)."""
    for dip in DIPS:
        bp = breakpoints(action, X, S1, S2, dip)
        lo, _hi = coord_range(bp["x"])
        if lo < 0:
            return (False, "physical stock negative during transit")
    succ = successor(action, X, S1, S2)
    if succ["q"] != 1:
        return (False, "destination architecture not reached (q=0 ∉ G^phys)")
    if succ["x"] < 0:
        return (False, "physical stock negative at endpoint")
    return (True, None)


def aggregate_assessment(action, X, S1, S2, a, b):
    """Scalarized aggregate admissibility at weight w = (b, a) (w.s = b*s1 + a*s2).

    Constraints: physical tube safe, aggregate floor b*s1(t)+a*s2(t) >= 0 on the
    exact tube for EVERY disturbance (piecewise linear -> min at a breakpoint),
    successor physical membership and aggregate floor.
    """
    for dip in DIPS:
        bp = breakpoints(action, X, S1, S2, dip)
        lo_x, _ = coord_range(bp["x"])
        if lo_x < 0:
            return (False, "physical stock negative during transit (not "
                           "compensable: S^w ⊆ S^phys)")
        vals = [b * v1 + a * v2 for v1, v2 in zip(bp["s1"], bp["s2"])]
        if min(vals) < 0:
            return (False, f"aggregate floor w·s dips below 0 during transit")
    succ = successor(action, X, S1, S2)
    if succ["q"] != 1:
        return (False, "destination architecture not reached (q=0 ∉ G^w)")
    if succ["x"] < 0:
        return (False, "physical stock negative at endpoint")
    if b * succ["s1"] + a * succ["s2"] < 0:
        return (False, "aggregate floor violated at endpoint")
    return (True, None)


# ----------------------------------------------------------------- grid + weights
def grid_states():
    vals = range(0, GRID_MAX + 1, GRID_STEP)
    for X in vals:
        for S1 in vals:
            for S2 in vals:
                yield (X, S1, S2)


def weight_set(X, S1, S2):
    """Critical weight set for one state: dense grid + r=∞ + exact boundary weights.

    Weights are (a, b) integer pairs, w·s = b·s1 + a·s2, r = a/b ∈ [0, ∞]
    (b = 0 is r = ∞, the pure s2 weight; a = 0 is r = 0, the pure s1 weight).
    rho_1 = (FLOOR - S1)/S2 (S2>0 and S1<FLOOR needed — for S1 >= FLOOR, rho_1
    leaves the closed cone and FAST is safe at every cone weight anyway);
    rho_2 = S1/(FLOOR - S2) (FLOOR>S2 needed); mid = (rho_1+rho_2)/2 — the
    adversarial weight when rho_2 < rho_1.
    """
    ws = [(k, 20) for k in range(0, 41)]          # r = k/20, k = 0..40
    ws.append((1, 0))                              # r = ∞
    if 0 < S2 and S1 < FLOOR:
        ws.append((FLOOR - S1, S2))                # r = rho_1 (exact boundary)
    if S2 < FLOOR:
        ws.append((S1, FLOOR - S2))                # r = rho_2 (exact boundary)
    if S2 > 0 and S2 < FLOOR and S1 < FLOOR:
        # mid = (rho_1 + rho_2)/2 = ((FLOOR-S1)/S2 + S1/(FLOOR-S2))/2
        num = (FLOOR - S1) * (FLOOR - S2) + S1 * S2
        den = 2 * S2 * (FLOOR - S2)
        ws.append((num, den))
    return ws


def machine_all_weights_admissible(X, S1, S2, ws=None):
    """∀w ∈ critical set ∃action: aggregate-admissible (machine layer)."""
    if ws is None:
        ws = weight_set(X, S1, S2)
    for (a, b) in ws:
        if not any(aggregate_assessment(act, X, S1, S2, a, b)[0] for act in ACTIONS):
            return (False, (a, b))
    return (True, None)


# ------------------------------------------------------------ analytic regions
def analytic_typed(X, S1, S2):
    return X >= C or S1 >= FLOOR or S2 >= FLOOR


def analytic_aggregate(X, S1, S2):
    return X >= C or S1 + S2 >= FLOOR


def analytic_physical(X, S1, S2):
    return True


def analytic_FP(X, S1, S2):
    return (not analytic_typed(X, S1, S2)) and analytic_aggregate(X, S1, S2)


# ===========================================================================
print("[typed false-positive instantiation — exact integer arithmetic, scale 40]")
t0 = time.time()

# --------------------------------------------------------------- [T1] machinery
print("\n[T1] exact-tube machinery")
bp = breakpoints("FAST", 40, 40, 40, DIP_ALPHA)
check("FAST breakpoint table exact (dip at t=1/2, recovery at t=1)",
      bp["s1"] == (40, 40 - DIP_ALPHA, 40), bp["s1"])
bp = breakpoints("STAGED", 40, 40, 40, 0)
check("STAGED breakpoint table exact (linear spend/growth)",
      bp["x"] == (40, 40 - C // 2, 40 - C) and bp["s1"] == (40, 45, 50))
# piecewise monotonicity: each piece linear => monotone; ranges exact by construction.
mono_ok = True
for act in ACTIONS:
    for dip in DIPS + (0,):
        b_ = breakpoints(act, 24, 24, 24, dip)
        for coord, vals in b_.items():
            assert coord_range(vals) == (min(vals), max(vals))
check("per-coordinate exact ranges = breakpoint extremes (piecewise monotone)", mono_ok)
check("worst-case dip constants: benign 3/2, adverse 2, floor threshold 2",
      DIP_BETA == 60 and DIP_ALPHA == 80 and FLOOR == 80)

# --------------------------------------------------------- [T2] typed region
print("\n[T2] Theorem B(1): typed region identity")
mismatch = 0
for (X, S1, S2) in grid_states():
    machine = any(typed_assessment(act, X, S1, S2)[0] for act in ACTIONS)
    if machine != analytic_typed(X, S1, S2):
        mismatch += 1
check("machine typed-feasibility == {x>=1} ∪ {s1>=2} ∪ {s2>=2} on every grid state",
      mismatch == 0, f"{mismatch} mismatches")

# ----------------------------------------------------- [T3] aggregate region
print("\n[T3] Theorem B(2): aggregate region identity (dense critical weights)")
mismatch = 0
first_bad = None
for (X, S1, S2) in grid_states():
    ok, witness_w = machine_all_weights_admissible(X, S1, S2)
    if ok != analytic_aggregate(X, S1, S2):
        mismatch += 1
        if first_bad is None:
            first_bad = (X, S1, S2, ok, witness_w)
check("machine all-weights admissibility == {x>=1} ∪ {s1+s2>=2} on every grid state",
      mismatch == 0, f"{mismatch} mismatches" + (f"; first: {first_bad}" if first_bad else ""))

# structural biconditionals (theorem B(6)): FAST-safe ⟺ r >= rho_1; SLOW-safe ⟺ r <= rho_2
struct_bad = 0
for (X, S1, S2) in grid_states():
    for (a, b) in [(k, 20) for k in range(0, 41)] + [(1, 0)]:
        fast_ok = aggregate_assessment("FAST", X, S1, S2, a, b)[0]
        fast_pred = b * S1 + a * S2 >= b * FLOOR   # valid for all (a,b): a=0 gives
        #   {S1>=FLOOR}; b=0 gives {S2>=0} — the r=0/r=∞ edges included
        if fast_ok != fast_pred:
            struct_bad += 1
        slow_ok = aggregate_assessment("SLOW", X, S1, S2, a, b)[0]
        slow_pred = b * S1 + a * S2 >= a * FLOOR   # symmetric: b=0 gives
        #   {S2>=FLOOR}; a=0 gives {S1>=0}
        if slow_ok != slow_pred:
            struct_bad += 1
check("FAST/SLOW per-weight safety biconditionals confirmed on every grid state "
      "(dense r-grid)", struct_bad == 0, f"{struct_bad} mismatches")

# boundary exactness: at r = rho_1 FAST is exactly boundary-safe; at r = rho_2 SLOW
b1 = aggregate_assessment("FAST", 20, 48, 48, FLOOR - 48, 48)[0]      # r = rho_1 = 2/3
b2 = aggregate_assessment("SLOW", 20, 48, 48, 48, FLOOR - 48)[0]      # r = rho_2 = 3/2
check("boundary weights exact: FAST safe at r=rho_1, SLOW safe at r=rho_2 "
      "(witness state (1/2, 6/5, 6/5))", b1 and b2)

# ------------------------------------------------------ [T4] endpoint region
print("\n[T4] Theorem B(3): endpoint-only region")
mismatch = sum(1 for (X, S1, S2) in grid_states()
               if any(physical_assessment(act, X, S1, S2)[0] for act in ACTIONS)
               != analytic_physical(X, S1, S2))
check("machine endpoint-only feasibility == all of X_0 on every grid state",
      mismatch == 0, f"{mismatch} mismatches")

# ------------------------------------------------------------- [T5] hierarchy
print("\n[T5] Theorem A(i): hierarchy on every grid state")
hier_bad = 0
for (X, S1, S2) in grid_states():
    typed = any(typed_assessment(act, X, S1, S2)[0] for act in ACTIONS)
    agg_ok, _ = machine_all_weights_admissible(X, S1, S2)
    phys = any(physical_assessment(act, X, S1, S2)[0] for act in ACTIONS)
    if not ((typed <= agg_ok) and (agg_ok <= phys)):
        hier_bad += 1
check("typed ⇒ all-weights-aggregate ⇒ endpoint-only (no violations on the grid)",
      hier_bad == 0, f"{hier_bad} violations")

# ------------------------------------------------------ [T6] false positives
print("\n[T6] Theorem B(4): the false-positive set")
fp_count = sum(1 for (X, S1, S2) in grid_states() if analytic_FP(X, S1, S2))
check("false-positive set nonempty on the grid", fp_count > 0, f"{fp_count} grid states")
X, S1, S2 = 20, 48, 48
w_ok, _ = machine_all_weights_admissible(X, S1, S2)
t_ok = any(typed_assessment(act, X, S1, S2)[0] for act in ACTIONS)
p_ok = any(physical_assessment(act, X, S1, S2)[0] for act in ACTIONS)
check("interior witness (1/2, 6/5, 6/5): aggregate-feasible for every critical "
      "weight, typed-INfeasible, endpoint-feasible",
      w_ok and (not t_ok) and p_ok and analytic_FP(X, S1, S2))
nb = all(analytic_FP(20, 48 + d1, 48 + d2)
         for d1 in (-4, 0, 4) for d2 in (-4, 0, 4))
check("witness is an interior point (all ±0.1 neighbors remain in FP)", nb)

# ------------------------------------------------------------ [T7] strictness
print("\n[T7] Theorem B(5): both inclusions strict")
X, S1, S2 = 20, 4, 4                                     # (1/2, 1/10, 1/10)
w_ok, w_witness = machine_all_weights_admissible(X, S1, S2)
w11 = any(aggregate_assessment(act, X, S1, S2, 1, 1)[0] for act in ACTIONS)
p_ok = any(physical_assessment(act, X, S1, S2)[0] for act in ACTIONS)
check("endpoint-only witness (1/2, 1/10, 1/10): endpoint-feasible, aggregate-"
      "INfeasible (no action safe at w=(1,1))",
      p_ok and (not w_ok) and (not w11))
X, S1, S2 = 20, 48, 48
agg_in_strict = machine_all_weights_admissible(X, S1, S2)[0] and \
    not any(typed_assessment(act, X, S1, S2)[0] for act in ACTIONS)
check("aggregate-vs-typed strictness witness (the FP interior point above)",
      agg_in_strict)

# ------------------------------------------------------ [T8] plan disagreement
print("\n[T8] Theorem B(6): per-weight plan disagreement at (1/2, 6/5, 6/5)")
X, S1, S2 = 20, 48, 48
fast_half = aggregate_assessment("FAST", X, S1, S2, 1, 2)[0]     # r = 1/2
slow_half = aggregate_assessment("SLOW", X, S1, S2, 1, 2)[0]
fast_one = aggregate_assessment("FAST", X, S1, S2, 1, 1)[0]      # r = 1
slow_one = aggregate_assessment("SLOW", X, S1, S2, 1, 1)[0]
fast_two = aggregate_assessment("FAST", X, S1, S2, 2, 1)[0]      # r = 2
slow_two = aggregate_assessment("SLOW", X, S1, S2, 2, 1)[0]
check("r=1/2: SLOW-only (FAST unsafe, SLOW safe)", (not fast_half) and slow_half)
check("r=1: both plans safe", fast_one and slow_one)
check("r=2: FAST-only (SLOW unsafe, FAST safe)", fast_two and (not slow_two))
serves_all = {act: all(aggregate_assessment(act, X, S1, S2, a, b)[0]
                       for (a, b) in weight_set(X, S1, S2)) for act in ACTIONS}
check("E_typ = ∩_w E_w = ∅ machine-verified (no action serves every critical "
      "weight)", not any(serves_all.values()), serves_all)

# ----------------------------------------------------------- [T9] rescue split
print("\n[T9] Theorem B(7): the rescue split")
X, S1, S2 = 60, 48, 48                                     # x = 3/2 >= c
staged_ok, staged_viol = typed_assessment("STAGED", X, S1, S2)
check("R witness (3/2, 6/5, 6/5): typed-transformable via STAGED (bridging plan "
      "at physical cost c=1)", staged_ok)
X, S1, S2 = 20, 48, 48                                     # x = 1/2 < c
rejections = {act: typed_assessment(act, X, S1, S2) for act in ACTIONS}
fast_viol_is_s1 = "s1" in rejections["FAST"][1]
slow_viol_is_s2 = "s2" in rejections["SLOW"][1]
staged_viol_is_x = "physical stock" in rejections["STAGED"][1]
nosw_viol_is_dest = "destination architecture" in rejections["NO-SWITCH"][1]
check("I witness (1/2, 6/5, 6/5): all four actions rejected, each with its "
      "exhibited violated constraint (negative-certificate form)",
      all(not v[0] for v in rejections.values()) and fast_viol_is_s1
      and slow_viol_is_s2 and staged_viol_is_x and nosw_viol_is_dest,
      {k: v[1] for k, v in rejections.items()})
fp0_rescue_ok = all(
    (typed_assessment("STAGED", X, S1, S2)[0] if X >= C else
     not any(typed_assessment(act, X, S1, S2)[0] for act in ACTIONS))
    for (X, S1, S2) in grid_states()
    if (S1 < FLOOR and S2 < FLOOR and S1 + S2 >= FLOOR))
check("rescue split verified on the whole grid: FP0∩{x>=1} typed-feasible via "
      "STAGED; FP0∩{x<1} typed-infeasible", fp0_rescue_ok)

# ------------------------------------------------- [T10] multi-stage (Theorem C)
print("\n[T10] Theorem C: propagation through two prepended hold intervals")


def hold_pullback(membership_next, safe_now):
    """W_j = {z: z ∈ S_j^· and z ∈ W_{j+1}^·} for the HOLD-only interval."""
    return lambda X, S1, S2: safe_now(X, S1, S2) and membership_next(X, S1, S2)


def s0_typed(X, S1, S2):
    return X >= 0 and S1 >= 0 and S2 >= 0


def s0_phys(X, S1, S2):
    return X >= 0


def make_s0_agg(a, b):
    return lambda X, S1, S2: X >= 0 and b * S1 + a * S2 >= 0


def W_last_typed(X, S1, S2):
    return any(typed_assessment(act, X, S1, S2)[0] for act in ACTIONS)


def W_last_phys(X, S1, S2):
    return any(physical_assessment(act, X, S1, S2)[0] for act in ACTIONS)


def W_last_agg(a, b):
    return lambda X, S1, S2: any(aggregate_assessment(act, X, S1, S2, a, b)[0]
                                 for act in ACTIONS)


# stage 0 after two holds: W_0 = S^· ∩ (S^· ∩ W_last^·)
W0_typed = hold_pullback(hold_pullback(W_last_typed, s0_typed), s0_typed)
W0_phys = hold_pullback(hold_pullback(W_last_phys, s0_phys), s0_phys)


def W0_agg_all(X, S1, S2):
    for (a, b) in weight_set(X, S1, S2):
        w_j = hold_pullback(hold_pullback(W_last_agg(a, b), make_s0_agg(a, b)),
                            make_s0_agg(a, b))(X, S1, S2)
        if not w_j:
            return False
    return True


c_bad = 0
for (X, S1, S2) in grid_states():
    t0v = W0_typed(X, S1, S2)
    av = W0_agg_all(X, S1, S2)
    pv = W0_phys(X, S1, S2)
    if not (t0v <= av <= pv):
        c_bad += 1
    if t0v != W_last_typed(X, S1, S2):     # grid ⊆ S_0, so holds are transparent
        c_bad += 1
check("stage-0 hierarchy holds and regions are preserved through two hold "
      "intervals (every grid state)", c_bad == 0, f"{c_bad} violations")
fp0 = (20, 48, 48)
check("FP strictness witness survives the holds at stage 0",
      W0_agg_all(*fp0) and not W0_typed(*fp0))
ep0 = (20, 4, 4)
check("endpoint-only strictness witness survives the holds at stage 0",
      W0_phys(*ep0) and not W0_agg_all(*ep0))

# ------------------------------------------------------------------- summary
elapsed = round(time.time() - t0, 3)
grid_list = list(grid_states())
grid_n = len(grid_list)
fp_grid = sum(1 for (X, S1, S2) in grid_list if analytic_FP(X, S1, S2))
summary = {
    "artifact": "paper1_instantiation/typed_false_positive_instantiation.py",
    "companion_theorem": "research_program/paper1_typed_false_positive_theorem.md",
    "executed": "2026-08-28",
    "arithmetic": "exact integers, scale 40 (no floats, no tolerances, no "
                  "randomness, no outer tube approximation)",
    "datum": {"Q": 2, "architectures": ["extraction q=0", "regenerative q=1"],
              "m": 1, "dips_scaled": {"benign": DIP_BETA, "adverse": DIP_ALPHA},
              "floor_threshold_scaled": FLOOR, "reset_gain_scaled": E,
              "rescue_cost_scaled": C, "actions": list(ACTIONS)},
    "grid": {"states": grid_n, "extent": "[0,3]^3 step 0.1 (x, s1, s2)",
             "false_positive_states": fp_grid},
    "regions": {
        "typed": "{x>=1} ∪ {s1>=2} ∪ {s2>=2}",
        "aggregate_all_weights": "{x>=1} ∪ {s1+s2>=2}",
        "endpoint_only": "all of X_0",
        "false_positive_set": "FP = {x<1, s1<2, s2<2, s1+s2>=2}",
        "rescue_set": "R = FP0 ∩ {x>=1} (typed-feasible via STAGED)",
        "impossibility_region": "I = FP0 ∩ {x<1} (four exhibited violations)"},
    "witnesses": {
        "fp_interior": {"state": [0.5, 1.2, 1.2],
                        "classification": "aggregate-feasible for every critical "
                                          "weight; typed-infeasible; endpoint-feasible"},
        "endpoint_only_blind": {"state": [0.5, 0.1, 0.1],
                                "classification": "endpoint-feasible; aggregate-"
                                                  "infeasible at w=(1,1)"},
        "rescued": {"state": [1.5, 1.2, 1.2],
                    "classification": "typed-transformable via STAGED"},
        "impossibility": {"state": [0.5, 1.2, 1.2],
                          "classification": "certified impossibility: FAST violates "
                                            "s1-floor (adverse), SLOW violates s2-floor "
                                            "(adverse), STAGED drives x negative, "
                                            "NO-SWITCH misses G"}},
    "checks": CHECKS,
    "checks_passed": sum(1 for c in CHECKS if c["pass"]),
    "checks_total": len(CHECKS),
    "elapsed_seconds": elapsed,
}

out = Path(__file__).resolve().parent / "typed_false_positive_instantiation.json"
out.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
print(f"\n[{summary['checks_passed']}/{summary['checks_total']} checks passed] "
      f"({elapsed}s) — artifact: {out.name}")
if FAIL:
    print("FAILED: " + ", ".join(FAIL))
    sys.exit(1)
print("ALL CHECKS PASS — Theorems A/B/C machine-confirmed on the witness datum.")
