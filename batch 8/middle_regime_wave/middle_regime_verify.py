#!/usr/bin/env python3
"""The middle-regime (common-shock) exact computation - fail-loud verifier.

Task 108 / batch 8 / paper 1 (Ecological Indicators), queue point 3.A-6:
the three-regime disturbance-sensitivity table's middle cell ("common biomass
shock") must be COMPUTED, not asserted (point 3.E-42 standing). This
verifier executes the exact computation on the witness datum of paper1
Assessment Separation v53 Section 4.5, together with the regime-(i)
handshake (the action-indexed class reproduces Theorem 5 exactly) and the
regime-(iii) verification (the coupled class, both formalizations).

Discipline (the sigma-wave standard): standard library only;
fractions.Fraction exclusively - no floats, no tolerances, no randomness;
deterministic; any failed gate exits nonzero. Every decision is an exact
rational comparison; every interval endpoint is solved in closed form.

THE MODEL (documented in MIDDLE_REGIME_WAVE.md, the companion record).

The Section 4.5 datum decomposed per Section 6.3's own arithmetic: each
principal plan's announced schedule is a mid-interval tent drawdown of depth
3/2 in its characteristic coordinate (FAST: s1, the quota pulse; SLOW: s2,
the gradual burden); each environmental event is a transient tent dip of
depth delta in ONE floor coordinate, troughing at t = 1/2, recovered by
t = 1 (successors unchanged); the Section 4.5 worst-case depth 2 = 3/2
(own) + 1/2 (event), the Section 6.3 identity (quota 3/2 + heatwave 1/2).
STAGED spends x (tube [x-1, x]) while its floors grow linearly to s + e,
e = (1/4, 1/4); an event of depth delta on a growing floor dips it to
s + 1/8 - delta (the trough at t = 1/2 on the linear growth), i.e. by
max(0, delta - 1/8).

Disturbance classes (each a set of disturbances; a disturbance is a map
coordinate -> event depth; quantified universally innermost):

  action_indexed : each plan suffers only its own characteristic
                   coordinate's event (the Section 4.5 convention; STAGED
                   and NO-SWITCH suffer no floor event). At delta = 1/2
                   this reproduces the Section 4.5 datum EXACTLY (the
                   Part-0 handshake). The blend here is Theorem 9's: the
                   convex combination of the primitive WORST-CASE tubes
                   (each of depth 3/2 + delta).
  common         : the two coordinate events are SEPARATE disturbances,
                   each striking EVERY plan (regime ii - one shared shock
                   strikes the same floor coordinate of every plan).
  coupled        : ONE disturbance carrying BOTH coordinate events
                   simultaneously, striking every plan (regime iii,
                   additive reading: the events ride on top of the plans'
                   own schedules).
  coupled_total  : regime iii, replace reading: every announced-schedule
                   plan's worst case is a dip of the datum's full magnitude
                   2 in EACH floor (the tent schedules suppressed; FAST and
                   SLOW degenerate to the same tube object). Because the
                   dip is then plan- and weight-independent, the weak
                   test's weight-wise plan choice buys nothing and the
                   typed/weak separation COLLAPSES: V_weak = V_typ
                   (Theorem CT). STAGED keeps its growth mechanics (the
                   dip lands on the growing floor: threshold 15/8),
                   matching its coupled(2) branch - the rescue route
                   survives, and it is the ONLY surviving distinction
                   between the two tests' hypotheses (x >= 1), which both
                   tests apply identically.
  single         : the single-event sub-case of `common` (only the s1
                   event exists) - the row-(ii) literal reading.

Run:  python3 middle_regime_verify.py   # exit 0 and ALL CHECKS PASS
"""

import sys
from fractions import Fraction as Q

# ----------------------------------------------------------------------------
# Datum parameters (exact)
# ----------------------------------------------------------------------------
OWN = Q(3, 2)          # own-schedule tent depth in the plan's characteristic coordinate
DELTA = Q(1, 2)        # primary event depth (the Section 6.3 heatwave)
E1 = E2 = Q(1, 4)      # destination gain per floor
COST = Q(1)            # STAGED rescue cost (x-tube depth)
FULL = OWN + DELTA     # = 2: the Section 4.5 worst-case depth (handshake)

FAILURES = []
CHECKS = 0


def ok(label, cond):
    """Record one check; fail loud at the end (and count)."""
    global CHECKS
    CHECKS += 1
    if not cond:
        FAILURES.append(label)
        print(f"  [FAIL] {label}")
    else:
        print(f"PASS {label}")
    return bool(cond)


def finish():
    print()
    print(f"total checks: {CHECKS}   passed: {CHECKS - len(FAILURES)}   failed: {len(FAILURES)}")
    if FAILURES:
        print("FAILED CHECKS:")
        for f in FAILURES:
            print("  - " + f)
        print("CHECKS FAILED")
        sys.exit(1)
    print("ALL CHECKS PASS")
    sys.exit(0)


# ----------------------------------------------------------------------------
# The tube model, per (action, disturbance)
# ----------------------------------------------------------------------------
ACTIONS = ("NO-SWITCH", "FAST", "SLOW", "STAGED")

# Own-schedule tent depths per coordinate (0 = the coordinate is constant)
OWN_TENT = {
    "NO-SWITCH": (Q(0), Q(0)),
    "FAST": (OWN, Q(0)),
    "SLOW": (Q(0), OWN),
    "STAGED": (Q(0), Q(0)),      # floors grow (handled separately); x spends 1
}
# STAGED floor growth to s + e is linear: value at the trough time t = 1/2 is s + 1/8
GROWTH_AT_TROUGH = E1 / 2        # = 1/8


def own_tent(action, cls):
    """Own-schedule tents; suppressed entirely under the coupled-total reading."""
    if cls == "coupled_total":
        return (Q(0), Q(0))
    return OWN_TENT[action]


def events_for(action, cls, delta):
    """The disturbance class as a list of disturbances; a disturbance is a
    dict {1: depth, 2: depth} (missing key = 0)."""
    if cls == "action_indexed":
        if action == "FAST":
            return [{1: delta}]
        if action == "SLOW":
            return [{2: delta}]
        return [{}]                      # STAGED, NO-SWITCH: no floor event
    if cls == "common":
        return [{1: delta}, {2: delta}]
    if cls == "coupled":
        return [{1: delta, 2: delta}]
    if cls == "coupled_total":
        return [{1: FULL, 2: FULL}]
    if cls == "single":
        return [{1: delta}]
    raise ValueError(cls)


def floor_tube_min(action, i, s_i, event_depth, cls):
    """Exact minimum of floor i's tube for (action, disturbance)."""
    if action == "STAGED" and cls != "coupled_total":
        # growing floor, event tent troughing at t = 1/2 on the linear growth
        return s_i - max(Q(0), event_depth - GROWTH_AT_TROUGH)
    if action == "STAGED":
        # coupled-total: the full-magnitude dip on the growing floor
        return s_i - max(Q(0), event_depth - GROWTH_AT_TROUGH)
    return s_i - own_tent(action, cls)[i - 1] - event_depth


def agg_dip(action, p, event, cls):
    """Exact aggregate dip at the tube's worst point, weight share p on s1:
    min_t (w.s)(t) = A(p) - dip, dip >= 0."""
    d1 = own_tent(action, cls)[0] + event.get(1, Q(0))
    d2 = own_tent(action, cls)[1] + event.get(2, Q(0))
    if action == "STAGED":
        raw = d1 * p + d2 * (Q(1) - p)
        return max(Q(0), raw - GROWTH_AT_TROUGH)
    return d1 * p + d2 * (Q(1) - p)


def typed_admissible(action, z, cls, delta):
    """a in E_typ(z) on the given class: every disturbance's tube within
    S0 = {x >= 0, s >= 0} and successor in G."""
    x, s1, s2 = z
    if action == "NO-SWITCH":
        return False                        # successor (0, x, s) misses G
    if action == "STAGED" and x < Q(1):
        return False                        # x-tube [x-1, x] and successor
    for ev in events_for(action, cls, delta):
        if floor_tube_min(action, 1, s1, ev.get(1, Q(0)), cls) < 0:
            return False
        if floor_tube_min(action, 2, s2, ev.get(2, Q(0)), cls) < 0:
            return False
    return True


def in_typ(z, cls, delta):
    return any(typed_admissible(a, z, cls, delta) for a in ACTIONS)


# ---- weight-space admissibility, exactly ------------------------------------

def interval_of_affine_nonneg(c0, c1):
    """{p in [0,1] : c0 + c1*p >= 0} as an exact closed interval or None."""
    if c1 == 0:
        return (Q(0), Q(1)) if c0 >= 0 else None
    p_star = -c0 / c1
    if c1 > 0:
        lo, hi = max(Q(0), p_star), Q(1)
    else:
        lo, hi = Q(0), min(Q(1), p_star)
    if lo > hi:
        return None
    if c0 + c1 * lo < 0 or c0 + c1 * hi < 0:   # exactness guard
        return None
    return (lo, hi)


def intersect(iv1, iv2):
    if iv1 is None or iv2 is None:
        return None
    lo = max(iv1[0], iv2[0])
    hi = min(iv1[1], iv2[1])
    if lo > hi:
        return None
    return (lo, hi)


def serving_interval(action, z, cls, delta):
    """The exact set {p in [0,1] : the plan is w-admissible at weight share
    p on s1} as a closed interval (an intersection of affine half-line
    sets), or None. NO-SWITCH never serves.

    FAST/SLOW: the aggregate dip is affine in p (d1*p + d2*(1-p)), so the
    endpoint interpolation below is EXACT. STAGED: the aggregate dip
    max(0, raw(p) - 1/8) is KINKED (piecewise affine), so interpolating
    its endpoints would OVERESTIMATE the dip in the interior and shrink
    the interval; instead the requirement A(p) >= max(0, raw(p) - 1/8)
    is decomposed EXACTLY into the two affine conditions
    (A(p) - raw(p) + 1/8 >= 0) and (A(p) >= 0), with raw affine (STAGED's
    own tent is (0,0) in every class; its floors only grow)."""
    x, s1, s2 = z
    if action == "NO-SWITCH":
        return None
    if action == "STAGED" and x < Q(1):
        return None
    A0 = s2                      # A(p) = s2 + p*(s1 - s2)
    A1 = s1 - s2
    iv = (Q(0), Q(1))
    for ev in events_for(action, cls, delta):
        # conditions (all affine in p):
        #   (trough)  A(p) - dip(p) >= 0
        #   (start)   A(p) >= 0   (the tent recovers; the tube includes t = 0)
        if action == "STAGED":
            # exact kink decomposition: dip = max(0, raw - 1/8)
            #   A >= dip  <=>  (A - raw + 1/8 >= 0) and (A >= 0)
            d1 = ev.get(1, Q(0))
            d2 = ev.get(2, Q(0))
            r0 = d2                    # raw(p) = r0 + r1*p
            r1 = d1 - d2
            iv = intersect(iv, interval_of_affine_nonneg(
                A0 - r0 + GROWTH_AT_TROUGH, A1 - r1))
            if iv is None:
                return None
        else:
            dip0 = agg_dip(action, Q(0), ev, cls)   # affine in p: exact
            dip1 = agg_dip(action, Q(1), ev, cls) - dip0
            iv = intersect(iv, interval_of_affine_nonneg(A0 - dip0, A1 - dip1))
            if iv is None:
                return None
        iv = intersect(iv, interval_of_affine_nonneg(A0, A1))
        if iv is None:
            return None
    if iv is not None:
        (lo, hi) = iv
        for p in (lo, hi):
            if A0 + A1 * p < 0:
                return None
    return iv


def covers(s1, s2, x, cls, delta):
    """Exact per-weight cover: [0,1] contained in the union of the plans'
    serving intervals (computed exactly)."""
    ivs = []
    for a in ("FAST", "SLOW", "STAGED"):
        iv = serving_interval(a, (x, s1, s2), cls, delta)
        if iv is not None:
            ivs.append(iv)
    if not ivs:
        return False
    ivs.sort()
    cur = Q(0)
    for (lo, hi) in ivs:
        if lo > cur:
            return False
        cur = max(cur, hi)
        if cur >= Q(1):
            return True
    return cur >= Q(1)


def in_weak(z, cls, delta):
    return covers(z[1], z[2], z[0], cls, delta)


# ----------------------------------------------------------------------------
# Closed forms (the theorems of the wave record), as predicates
# ----------------------------------------------------------------------------
def typ_action_indexed(z, delta):
    x, s1, s2 = z
    return x >= Q(1) or s1 >= OWN + delta or s2 >= OWN + delta


def weak_action_indexed(z, delta):
    x, s1, s2 = z
    return x >= Q(1) or s1 + s2 >= OWN + delta


def typ_shared(z, delta):
    """V_typ for common and coupled (identical: per-coordinate tube minima
    are event-combination independent)."""
    x, s1, s2 = z
    f = max(Q(0), delta - GROWTH_AT_TROUGH)
    return ((s1 >= OWN + delta and s2 >= delta)
            or (s2 >= OWN + delta and s1 >= delta)
            or (x >= Q(1) and s1 >= f and s2 >= f))


def weak_common(z, delta):
    x, s1, s2 = z
    f = max(Q(0), delta - GROWTH_AT_TROUGH)
    if x >= Q(1):
        return s1 >= f and s2 >= f
    return s1 >= delta and s2 >= delta and s1 + s2 >= OWN + delta


def weak_coupled(z, delta):
    x, s1, s2 = z
    f = max(Q(0), delta - GROWTH_AT_TROUGH)
    if x >= Q(1):
        return s1 >= f and s2 >= f
    return s1 >= delta and s2 >= delta and s1 + s2 >= OWN + 2 * delta


def typ_single(z, delta):
    x, s1, s2 = z
    f = max(Q(0), delta - GROWTH_AT_TROUGH)
    return (s1 >= OWN + delta
            or (s2 >= OWN and s1 >= delta)
            or (x >= Q(1) and s1 >= f))


def weak_single(z, delta):
    x, s1, s2 = z
    f = max(Q(0), delta - GROWTH_AT_TROUGH)
    if x >= Q(1):
        return s1 >= f
    return s1 >= delta and s1 + s2 >= OWN + delta


def typ_coupled_total(z):
    x, s1, s2 = z
    f = FULL - GROWTH_AT_TROUGH
    return (s1 >= FULL and s2 >= FULL) or (x >= Q(1) and s1 >= f and s2 >= f)


def weak_coupled_total(z):
    x, s1, s2 = z
    f = FULL - GROWTH_AT_TROUGH
    if x >= Q(1):
        return s1 >= f and s2 >= f
    # FAST and SLOW share the same requirement A(p) >= 2 (weight-
    # independent), so coverage of [0,1] needs min A = min(s) >= 2 - the
    # aggregation advantage is GONE (Theorem CT: V_weak = V_typ).
    return s1 >= FULL and s2 >= FULL


CLOSED = {
    "action_indexed": (typ_action_indexed, weak_action_indexed),
    "common": (typ_shared, weak_common),
    "coupled": (typ_shared, weak_coupled),
    "single": (typ_single, weak_single),
}


# ----------------------------------------------------------------------------
# The blend window (exact), per class
# ----------------------------------------------------------------------------
def blend_window(z, cls, delta):
    """Exact typed-admissibility window of BLEND_db (db = FAST share) on the
    class: the set of db in [0,1] such that every disturbance's per-
    coordinate tube minima are >= 0, as an interval, or None.

    action_indexed: Theorem 9's blend - the convex combination of the
    primitive worst-case tubes (depths 3/2 + delta per characteristic
    coordinate): s1 >= (OWN+delta)*db and s2 >= (OWN+delta)*(1-db).
    common/coupled/single: the events ride on the plans' own schedules;
    per disturbance: s1 >= ev1 + OWN*db and s2 >= ev2 + OWN*(1-db).
    coupled_total: each floor dips the full magnitude 2 regardless of db
    (FAST and SLOW share the same tube object): s1 >= 2 and s2 >= 2.
    """
    x, s1, s2 = z
    lo, hi = Q(0), Q(1)

    def req(db_lo, db_hi):
        nonlocal lo, hi
        lo = max(lo, db_lo)
        hi = min(hi, db_hi)

    if cls == "action_indexed":
        total = OWN + delta
        if s1 < 0 or s2 < 0:
            return None
        req(Q(0) if s2 >= total else Q(1), Q(1) if False else Q(0)) if False else None
        # db <= s1/total and db >= 1 - s2/total
        req(1 - s2 / total, s1 / total)
    elif cls == "coupled_total":
        if s1 < FULL or s2 < FULL:
            return None
        req(Q(0), Q(1))
    else:
        evs = events_for("FAST", cls, delta)
        for ev in evs:
            e1 = ev.get(1, Q(0))
            e2 = ev.get(2, Q(0))
            # s1 >= e1 + OWN*db  →  db <= (s1 - e1)/OWN
            # s2 >= e2 + OWN*(1-db)  →  db >= 1 - (s2 - e2)/OWN
            req(1 - (s2 - e2) / OWN, (s1 - e1) / OWN)
    if lo > hi:
        return None
    return (lo, hi)


# ----------------------------------------------------------------------------
# Grids
# ----------------------------------------------------------------------------
def grid(xs, ss):
    for x in xs:
        for s1 in ss:
            for s2 in ss:
                yield (x, s1, s2)


def grid_I(xs, ss):
    """Enumerate the action-indexed gap region I at delta = 1/2:
    {x < 1, s1 < 2, s2 < 2, s1 + s2 >= 2}."""
    for x in xs:
        if x >= Q(1):
            continue
        for s1 in ss:
            if s1 >= FULL:
                continue
            for s2 in ss:
                if s2 >= FULL:
                    continue
                if s1 + s2 >= FULL:
                    yield (x, s1, s2)


CANON = (Q(1, 2), Q(6, 5), Q(6, 5))          # the Section 6.3 canonical datum
WITNESS_LIST = [
    CANON,
    (Q(1, 2), Q(1, 10), Q(19, 10)),           # action-indexed gap, sub-half floor
    (Q(1, 2), Q(1), Q(1)),                    # convexification-fragile witness
    (Q(1, 2), Q(19, 10), Q(19, 10)),          # deep I state (coupled-1/2 survivor)
    (Q(1, 2), Q(4, 3), Q(4, 3)),              # coupled-1/2 gap witness
    (Q(1, 2), Q(13, 10), Q(13, 10)),
    (Q(1, 2), Q(3), Q(3)),                    # coupled-2 relocated gap witness
    (Q(1, 2), Q(3), Q(5, 2)),                 # coupled-2 gap boundary state
    (Q(1, 2), Q(3), Q(1)),                    # coupled-total new-gap witness
    (Q(3, 2), Q(6, 5), Q(6, 5)),              # the rescue witness (the deposit's)
    (Q(1, 2), Q(1, 4), Q(7, 4)),              # sub-half floor, sum = 2
    (Q(1, 2), Q(79, 40), Q(79, 40)),          # near-boundary deep I state
]


# ============================================================================
# PART 0 - datum and the action-indexed handshake (regime i)
# ============================================================================
print("middle-regime (common-shock) wave - exact machine verification")
print("witness: paper1_assessment_separation_v53.tex Section 4.5 datum; "
      "Section 6.3 fishery reading; Table 5 (Section 5.4) the middle cell")
print("arithmetic: fractions.Fraction only; no floats, no tolerances, "
      "no randomness")
print()
print("PART 0 - datum parameters and the action-indexed handshake")
ok("0.1 parameters: own 3/2, event 1/2, full depth 2, e = 1/4, c = 1",
   OWN == Q(3, 2) and DELTA == Q(1, 2) and FULL == Q(2)
   and E1 == Q(1, 4) and COST == Q(1))
ok("0.2 the Section 6.3 identity: quota 3/2 + heatwave 1/2 = the Section 4.5 depth 2",
   OWN + DELTA == FULL == Q(2))
ok("0.3 STAGED trough growth 1/8 = e/2 on the linear floor schedule",
   GROWTH_AT_TROUGH == Q(1, 8))

z = CANON
ok("0.4 action-indexed FAST tube [s1-2, s1] at the canonical datum (min = -4/5)",
   floor_tube_min("FAST", 1, z[1], DELTA, "action_indexed") == z[1] - FULL == Q(-4, 5)
   and floor_tube_min("FAST", 2, z[2], Q(0), "action_indexed") == z[2])
ok("0.5 action-indexed SLOW mirror (min = -4/5 in s2)",
   floor_tube_min("SLOW", 2, z[2], DELTA, "action_indexed") == Q(-4, 5)
   and floor_tube_min("SLOW", 1, z[1], Q(0), "action_indexed") == z[1])
ok("0.6 action-indexed STAGED: floors grow (no dip), x-tube needs x >= 1",
   floor_tube_min("STAGED", 1, z[1], Q(0), "action_indexed") == z[1]
   and floor_tube_min("STAGED", 2, z[2], Q(0), "action_indexed") == z[2]
   and not typed_admissible("STAGED", z, "action_indexed", DELTA)
   and typed_admissible("STAGED", (Q(1), Q(6, 5), Q(6, 5)), "action_indexed", DELTA))

G0 = list(grid([Q(0), Q(1, 2), Q(1), Q(3, 2)], [Q(k, 4) for k in range(0, 13)]))
ok("0.7 Theorem 5(1) handshake: V_typ(action-indexed) = {x>=1} U {s1>=2} U {s2>=2} "
   + f"on {len(G0)} grid states + witnesses",
   all((in_typ(zz, "action_indexed", DELTA) ==
        (zz[0] >= Q(1) or zz[1] >= Q(2) or zz[2] >= Q(2))) for zz in G0 + WITNESS_LIST))
ok("0.8 Theorem 5(2) handshake: V_weak(action-indexed) = {x>=1} U {s1+s2>=2} "
   + f"on {len(G0)} grid states + witnesses",
   all((in_weak(zz, "action_indexed", DELTA) ==
        (zz[0] >= Q(1) or zz[1] + zz[2] >= Q(2))) for zz in G0 + WITNESS_LIST))

ok("0.9 licensing handshake at the canonical datum: FAST serves p in [0, 3/5] "
   "(r >= rho_1 = 2/3), SLOW serves [2/5, 1] (r <= rho_2 = 3/2)",
   serving_interval("FAST", CANON, "action_indexed", DELTA) == (Q(0), Q(3, 5))
   and serving_interval("SLOW", CANON, "action_indexed", DELTA) == (Q(2, 5), Q(1)))
ok("0.10 the p-threshold equals 1/(1+rho_1) with rho_1 = (2-s1)/s2 at the canon datum",
   serving_interval("FAST", CANON, "action_indexed", DELTA)[1] == Q(3, 5)
   and (Q(2) - CANON[1]) / CANON[2] == Q(2, 3)
   and Q(1) / (Q(1) + Q(2, 3)) == Q(3, 5))
ok("0.11 the impossible-point check: (1/2, 1/10, 1/10) fails even the weak test "
   "(Theorem 5(5)'s second strictness witness)",
   not in_weak((Q(1, 2), Q(1, 10), Q(1, 10)), "action_indexed", DELTA))

# ============================================================================
# PART 1 - the common-shock class at delta = 1/2 (regime ii - the middle cell)
# ============================================================================
print("PART 1 - the common-shock class (regime ii), event depth 1/2")
G1 = list(grid([Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1), Q(5, 4), Q(3, 2), Q(2)],
               [Q(k, 8) for k in range(0, 25)]))
ok("1.1 V_typ(common) closed form on "
   + f"{len(G1)} grid states + witnesses",
   all((in_typ(zz, "common", DELTA) == typ_shared(zz, DELTA)) for zz in G1 + WITNESS_LIST))
ok("1.2 V_weak(common) closed form {x<1: s_i >= 1/2, sum >= 2} U {x>=1: s_i >= 3/8} on "
   + f"{len(G1)} grid states + witnesses",
   all((in_weak(zz, "common", DELTA) == weak_common(zz, DELTA)) for zz in G1 + WITNESS_LIST))


def three_point(z):
    x, s1, s2 = z
    if x >= Q(1):
        return s1 >= Q(3, 8) and s2 >= Q(3, 8)
    return s2 >= Q(1, 2) and (s1 + s2) >= Q(2) and s1 >= Q(1, 2)


ok("1.3 the three-point reduction (p in {0, 1/2, 1}) equals the exact cover on the grid",
   all(covers(zz[1], zz[2], zz[0], "common", DELTA) == three_point(zz) for zz in G1))


def in_gap_common(z):
    x, s1, s2 = z
    return (x < Q(1) and s1 >= Q(1, 2) and s2 >= Q(1, 2)
            and s1 < Q(2) and s2 < Q(2) and s1 + s2 >= Q(2))


ok("1.4 the gap identity FP_cs = V_weak \\ V_typ = {x<1, 1/2 <= s_i < 2, sum >= 2} "
   "on the grid + witnesses",
   all((in_weak(zz, "common", DELTA) and not in_typ(zz, "common", DELTA)) ==
       in_gap_common(zz) for zz in G1 + WITNESS_LIST))
ok("1.5 the gap is nonempty with interior: the canonical datum (1/2, 6/5, 6/5) is a "
   "common-shock gap state (weak-accept, typed-reject)",
   in_gap_common(CANON)
   and in_weak(CANON, "common", DELTA) and not in_typ(CANON, "common", DELTA))
ok("1.6 the canonical datum's licensing intervals are UNCHANGED from the "
   "action-indexed class: FAST [0, 3/5], SLOW [2/5, 1]",
   serving_interval("FAST", CANON, "common", DELTA) == (Q(0), Q(3, 5))
   and serving_interval("SLOW", CANON, "common", DELTA) == (Q(2, 5), Q(1)))

GAP1 = [zz for zz in G1 if in_gap_common(zz)]
ok(f"1.7 licensing invariance: on all {len(GAP1)} grid gap states, FAST's common-class "
   "interval endpoint equals the action-indexed endpoint s2/(2-s1+s2) (= 1/(1+rho_1)), "
   "SLOW's the mirror",
   len(GAP1) > 0
   and all(serving_interval("FAST", zz, "common", DELTA) is not None
       and serving_interval("FAST", zz, "common", DELTA)[1] ==
       zz[2] / (Q(2) - zz[1] + zz[2])
       and serving_interval("FAST", zz, "common", DELTA)[1] ==
       serving_interval("FAST", zz, "action_indexed", DELTA)[1]
       and serving_interval("SLOW", zz, "common", DELTA)[0] ==
       (Q(2) - zz[2]) / (Q(2) - zz[2] + zz[1])
       for zz in GAP1))

SUB_HALF = [zz for zz in G0
            if zz[0] < Q(1) and zz[1] < Q(2) and zz[2] < Q(2)
            and zz[1] + zz[2] >= Q(2) and (zz[1] < Q(1, 2) or zz[2] < Q(1, 2))]
ok(f"1.8 the exact cut: all {len(SUB_HALF)} enumerated action-indexed gap states with "
   "min(s1,s2) < 1/2 are weak-REJECTED under the common class (universal rejection), "
   "e.g. (1/2, 1/10, 19/10)",
   len(SUB_HALF) > 0
   and all(not in_weak(zz, "common", DELTA) for zz in SUB_HALF)
   and not in_weak((Q(1, 2), Q(1, 10), Q(19, 10)), "common", DELTA))

DIAG = [(x, Q(k, 40), Q(k, 40)) for x in (Q(0), Q(1, 2), Q(1))
        for k in range(15, 101)]
ok("1.9 diagonal coincidence: on the diagonal slice s1 = s2 = s >= 3/8, the "
   "common-class typed and weak verdicts coincide with the action-indexed ones",
   all(in_typ(zz, "common", DELTA) == in_typ(zz, "action_indexed", DELTA)
       and in_weak(zz, "common", DELTA) == in_weak(zz, "action_indexed", DELTA)
       for zz in DIAG))


def staged_req(p):
    return max(p, Q(1) - p) / 2 - Q(1, 8)


PGRID = [Q(k, 40) for k in range(0, 41)]
PROBES = [(Q(6, 5), Q(6, 5)), (Q(1, 2), Q(1, 2)), (Q(3, 8), Q(3, 8)),
          (Q(1), Q(2)), (Q(2), Q(1)), (Q(3, 8), Q(2)),
          (Q(1, 4), Q(1)), (Q(1), Q(1)), (Q(5, 2), Q(1)), (Q(3, 4), Q(3, 4))]
ok("1.10 STAGED's common-class requirement g(p) = max(p,1-p)/2 - 1/8: on every "
   "probe state, p is served iff A(p) >= g(p), on the whole p-grid",
   all(
       (lambda iv, s1, s2: all(
           ((p >= iv[0] and p <= iv[1])
            == (s2 + (s1 - s2) * p >= staged_req(p))) for p in PGRID))
       (serving_interval("STAGED", (Q(1), s1, s2), "common", DELTA), s1, s2)
       for (s1, s2) in PROBES
       if serving_interval("STAGED", (Q(1), s1, s2), "common", DELTA) is not None)
   and all(serving_interval("STAGED", (Q(1), s1, s2), "common", DELTA) is not None
           or all(s2 + (s1 - s2) * p < staged_req(p) for p in PGRID)
           for (s1, s2) in PROBES))


def kappa_star_common(z):
    """Closed form: 0 on V_typ; (1-x)+ on {s_i >= 3/8}\\V_typ; None = infinity."""
    x, s1, s2 = z
    if in_typ(z, "common", DELTA):
        return Q(0)
    if s1 >= Q(3, 8) and s2 >= Q(3, 8):
        return max(Q(0), Q(1) - x)
    return None


KGRID = [zz for zz in G1 if zz[0] < Q(1)]
ok("1.11 the rescue threshold under the common class: kappa* = 0 on V_typ, "
   "(1-x)+ on {s_i >= 3/8}\\V_typ, and INFINITE on {min(s) < 3/8}\\V_typ "
   "(the resource route no longer rescues every failure state)",
   all(
       (lambda zz: (
           (lambda kmin: (
               (kmin is not None) == (kappa_star_common(zz) is not None)
               and (kmin is None or kmin == kappa_star_common(zz))
           ))(next((k for k in [Q(i, 40) for i in range(0, 121)]
                    if (typed_admissible("FAST", zz, "common", DELTA)
                        or typed_admissible("SLOW", zz, "common", DELTA)
                        or typed_admissible("STAGED", (zz[0] + k, zz[1], zz[2]),
                                            "common", DELTA))), None))
       ))(zz) for zz in KGRID))
ok("1.12 the kappa* = infinity witness: (1/2, 1/4, 3) has min floor < 3/8 outside "
   "V_typ - no kappa rescues",
   kappa_star_common((Q(1, 2), Q(1, 4), Q(3))) is None
   and not any(typed_admissible("STAGED", (Q(1, 2) + k, Q(1, 4), Q(3)), "common", DELTA)
               for k in [Q(i, 40) for i in range(0, 121)]))
ok("1.13 the finite-kappa witness: the canonical datum's shortfall is 1/2 "
   "(= its action-indexed kappa*)",
   kappa_star_common(CANON) == Q(1, 2))

# ============================================================================
# PART 2 - the blend window and the convexification fragility (common class)
# ============================================================================
print("PART 2 - the blend window under the common class")
G2 = [zz for zz in G1 if zz[0] < Q(1)]
ok("2.1 the blend window is nonempty exactly on {s_i >= 1/2, s1+s2 >= 5/2} "
   "for the common class at delta = 1/2, on the grid",
   all(((blend_window(zz, "common", DELTA) is not None)
        == (zz[1] >= DELTA and zz[2] >= DELTA and zz[1] + zz[2] >= Q(5, 2)))
       for zz in G2))
ok("2.2 Theorem 9 handshake: the action-indexed blend window is nonempty exactly on "
   "{s1 + s2 >= 2}; at the canonical datum the window is [1 - s2/2, s1/2] = [2/5, 3/5]",
   all(((blend_window(zz, "action_indexed", DELTA) is not None)
        == (zz[1] + zz[2] >= Q(2))) for zz in G2)
   and blend_window(CANON, "action_indexed", DELTA) == (Q(2, 5), Q(3, 5)))
ok("2.3 the exact common-class windows: at the canonical datum (sum 12/5 < 5/2) "
   "the window is EMPTY - the datum sits in the fragile band; at (1/2, 4/3, 4/3) "
   "(sum 8/3 >= 5/2) the window is [4/9, 5/9]",
   blend_window(CANON, "common", DELTA) is None
   and blend_window((Q(1, 2), Q(4, 3), Q(4, 3)), "common", DELTA) == (Q(4, 9), Q(5, 9)))
ok("2.4 the convexification-fragility witness: (1/2, 1, 1) is a common-class gap "
   "state (weak-accept, typed-reject) with NO admissible blend (sum 2 < 5/2)",
   in_gap_common((Q(1, 2), Q(1), Q(1)))
   and blend_window((Q(1, 2), Q(1), Q(1)), "common", DELTA) is None)
ok("2.5 the fragile band: every grid gap state with sum in [2, 5/2) has no blend; "
   "every one with sum >= 5/2 has one",
   all(((blend_window(zz, "common", DELTA) is not None)
        == (zz[1] + zz[2] >= Q(5, 2))) for zz in GAP1))

# ============================================================================
# PART 3 - the coupled class (regime iii), both readings
# ============================================================================
print("PART 3 - the coupled class (regime iii)")
G3 = list(grid([Q(0), Q(1, 2), Q(1), Q(2)], [Q(k, 4) for k in range(0, 17)]))
ok("3.1 coupled(1/2) V_typ equals the common-class V_typ (per-coordinate minima are "
   "event-combination independent) on the grid",
   all(in_typ(zz, "coupled", DELTA) == typ_shared(zz, DELTA) for zz in G3))
ok("3.2 coupled(1/2) V_weak = {x<1: s_i >= 1/2, sum >= 5/2} U {x>=1: s_i >= 3/8} on "
   "the grid + witnesses",
   all(in_weak(zz, "coupled", DELTA) == weak_coupled(zz, DELTA)
       for zz in G3 + WITNESS_LIST))
ok("3.3 coupled(2) V_weak = {x<1: s_i >= 2, sum >= 11/2} U {x>=1: s_i >= 15/8} on "
   "the grid + witnesses",
   all(in_weak(zz, "coupled", Q(2)) == weak_coupled(zz, Q(2))
       for zz in G3 + WITNESS_LIST))
ok("3.4 coupled(2) V_typ = {s1 >= 7/2, s2 >= 2} U {s2 >= 7/2, s1 >= 2} U "
   "{x >= 1, s_i >= 15/8} on the grid",
   all(in_typ(zz, "coupled", Q(2)) ==
       ((zz[1] >= Q(7, 2) and zz[2] >= Q(2))
        or (zz[2] >= Q(7, 2) and zz[1] >= Q(2))
        or (zz[0] >= Q(1) and zz[1] >= Q(15, 8) and zz[2] >= Q(15, 8)))
       for zz in G3))

GI = list(grid_I([Q(0), Q(1, 2)], [Q(k, 8) for k in range(0, 16)]))
ok(f"3.5 the Section 5.4 coupled claim verified on I at the datum's full magnitude: "
   f"all {len(GI)} enumerated I-states are weak-REJECTED under coupled(2) "
   "(universal rejection on the witness's gap region)",
   len(GI) > 0 and all(not in_weak(zz, "coupled", Q(2)) for zz in GI))
ok("3.6 ... and the deep-I counterexample at heatwave magnitude: (1/2, 19/10, 19/10) "
   "is an I-state that SURVIVES as a coupled(1/2) gap (weak-accept, typed-reject) - "
   "the claim is depth-dependent",
   in_weak((Q(1, 2), Q(19, 10), Q(19, 10)), "coupled", DELTA)
   and not in_typ((Q(1, 2), Q(19, 10), Q(19, 10)), "coupled", DELTA))


def any_I_survives(delta, states):
    return any(in_weak(zz, "coupled", delta) for zz in states)


GI_FINE = list(grid_I([Q(0), Q(1, 2)], [Q(k, 40) for k in range(0, 80)]))
ok(f"3.7 the exact depth boundary: coupled(delta) kills every I-state iff "
   f"delta >= 5/4 (fine {len(GI_FINE)}-state I-grid: none survive at 5/4; some "
   "survive at 5/4 - 1/40, e.g. (1/2, 79/40, 79/40) with sum 79/20)",
   len(GI_FINE) > 0
   and not any_I_survives(Q(5, 4), GI_FINE)
   and any_I_survives(Q(5, 4) - Q(1, 40), GI_FINE)
   and in_weak((Q(1, 2), Q(79, 40), Q(79, 40)), "coupled", Q(5, 4) - Q(1, 40))
   and not in_weak((Q(1, 2), Q(79, 40), Q(79, 40)), "coupled", Q(5, 4))
   and not any_I_survives(Q(3, 2), GI_FINE) and not any_I_survives(Q(2), GI_FINE))
ok("3.8 the relocation: the coupled(2) gap {x<1, 2 <= s_i < 7/2, sum >= 11/2} is "
   "nonempty - (1/2, 3, 3) is weak-accepted and typed-rejected",
   in_weak((Q(1, 2), Q(3), Q(3)), "coupled", Q(2))
   and not in_typ((Q(1, 2), Q(3), Q(3)), "coupled", Q(2))
   and all((in_weak(zz, "coupled", Q(2)) and not in_typ(zz, "coupled", Q(2))) ==
       (zz[0] < Q(1) and zz[1] >= Q(2) and zz[2] >= Q(2)
        and zz[1] < Q(7, 2) and zz[2] < Q(7, 2) and zz[1] + zz[2] >= Q(11, 2))
       for zz in G3))
ok("3.9 Theorem 9 restored under the coupled class: the coupled blend window "
   "nonemptiness {s_i >= delta, sum >= 3/2+2delta} EQUALS the coupled weak "
   "boundary - the coupled gap is exactly blend-closed (grid, delta = 1/2 and 2)",
   all(((blend_window(zz, "coupled", d) is not None)
        == (zz[1] >= d and zz[2] >= d and zz[1] + zz[2] >= OWN + 2 * d))
       for zz in G2 for d in (DELTA, Q(2))))
ok("3.10 ... while the common gap is NOT blend-closed on the shallow band "
   "[3/2+delta, 3/2+2delta) - the class-conditional fragility (grid, delta = 1/2)",
   any(blend_window(zz, "common", DELTA) is None
       and in_weak(zz, "common", DELTA) and not in_typ(zz, "common", DELTA)
       for zz in G2))

print("PART 3b - the coupled-total reading (regime iii, replace formalization)")
ok("3.11 coupled-total: FAST and SLOW degenerate to the SAME tube requirement "
   "A(p) >= 2 (weight-independent) - identical serving intervals at every "
   "probe: both None at the canonical datum (they fail together at EVERY "
   "weight), both (0,1) at (1/2, 5/2, 5/2), both [1/2, 1] at (1/2, 3, 1)",
   serving_interval("FAST", CANON, "coupled_total", DELTA) is None
   and serving_interval("SLOW", CANON, "coupled_total", DELTA) is None
   and serving_interval("FAST", (Q(1, 2), Q(5, 2), Q(5, 2)),
                        "coupled_total", DELTA) == (Q(0), Q(1))
   and serving_interval("SLOW", (Q(1, 2), Q(5, 2), Q(5, 2)),
                        "coupled_total", DELTA) == (Q(0), Q(1))
   and serving_interval("FAST", (Q(1, 2), Q(3), Q(1)),
                        "coupled_total", DELTA) == (Q(1, 2), Q(1))
   and serving_interval("SLOW", (Q(1, 2), Q(3), Q(1)),
                        "coupled_total", DELTA) == (Q(1, 2), Q(1))
   and agg_dip("FAST", Q(1, 2), {1: FULL, 2: FULL}, "coupled_total") == Q(2)
   and agg_dip("SLOW", Q(1, 2), {1: FULL, 2: FULL}, "coupled_total") == Q(2))
ok("3.12 coupled-total V_typ = {s1 >= 2, s2 >= 2} U {x >= 1, s_i >= 15/8} and "
   "V_weak EQUALS it (THE COLLAPSE) on the grid",
   all(in_typ(zz, "coupled_total", DELTA) == typ_coupled_total(zz)
       and in_weak(zz, "coupled_total", DELTA) == weak_coupled_total(zz)
       and weak_coupled_total(zz) == typ_coupled_total(zz)
       for zz in G3))
ok("3.13 coupled-total: the typed/weak separation COLLAPSES (V_weak = V_typ; "
   "the gap is EMPTY on the grid + witnesses) - the replace reading strips "
   "the weak test of its aggregation advantage: every announced-schedule "
   "plan faces the same full-magnitude dip, so weight-wise plan choice buys "
   "nothing. Witness (1/2, 3, 1): action-indexed typed-ACCEPT (s1 >= 2) yet "
   "coupled-total FULL REJECT on BOTH tests (the replace reading is strictly "
   "more demanding); the canonical datum is likewise a full reject",
   all(not (in_weak(zz, "coupled_total", DELTA)
            and not in_typ(zz, "coupled_total", DELTA))
       for zz in G3 + WITNESS_LIST)
   and in_typ((Q(1, 2), Q(3), Q(1)), "action_indexed", DELTA)
   and not in_weak((Q(1, 2), Q(3), Q(1)), "coupled_total", DELTA)
   and not in_typ((Q(1, 2), Q(3), Q(1)), "coupled_total", DELTA)
   and not in_weak(CANON, "coupled_total", DELTA)
   and not in_typ(CANON, "coupled_total", DELTA))

# ============================================================================
# PART 4 - the delta-family identities (all classes, tested depths)
# ============================================================================
print("PART 4 - the delta-family closed forms at tested depths")
DELTAS = [Q(0), Q(1, 4), Q(1, 2), Q(1), Q(5, 4), Q(3, 2), Q(2)]
G4 = list(grid([Q(0), Q(1, 2), Q(1), Q(2)], [Q(k, 4) for k in range(0, 15)]))
for d in DELTAS:
    tcf, wcf = CLOSED["action_indexed"]
    ok(f"4.a action-indexed closed forms at delta = {d}: V_typ, V_weak on the grid",
       all(in_typ(zz, "action_indexed", d) == tcf(zz, d)
           and in_weak(zz, "action_indexed", d) == wcf(zz, d) for zz in G4))
for d in [dd for dd in DELTAS if dd <= Q(3, 2)]:
    tcf, wcf = CLOSED["common"]
    ok(f"4.b common closed forms at delta = {d} (<= 3/2): V_typ, V_weak on the grid",
       all(in_typ(zz, "common", d) == tcf(zz, d)
           and in_weak(zz, "common", d) == wcf(zz, d) for zz in G4))
for d in DELTAS:
    tcf, wcf = CLOSED["coupled"]
    ok(f"4.c coupled closed forms at delta = {d}: V_typ, V_weak on the grid",
       all(in_typ(zz, "coupled", d) == tcf(zz, d)
           and in_weak(zz, "coupled", d) == wcf(zz, d) for zz in G4))
for d in [Q(1, 4), Q(1, 2), Q(1)]:
    tcf, wcf = CLOSED["single"]
    ok(f"4.d single-event closed forms at delta = {d}: V_typ, V_weak on the grid",
       all(in_typ(zz, "single", d) == tcf(zz, d)
           and in_weak(zz, "single", d) == wcf(zz, d) for zz in G4))

ok("4.e the licensing invariance across depths: on the surviving common-class gap "
   "at each tested delta, FAST's endpoint equals the action-indexed endpoint "
   "s2/(3/2+delta-s1+s2)",
   all(
       serving_interval("FAST", zz, "common", d) is not None
       and serving_interval("FAST", zz, "common", d)[1] == zz[2] / (OWN + d - zz[1] + zz[2])
       and serving_interval("FAST", zz, "common", d)[1] ==
       serving_interval("FAST", zz, "action_indexed", d)[1]
       for d in [Q(1, 4), Q(1, 2), Q(1)]
       for zz in G4
       if zz[0] < Q(1) and zz[1] >= d and zz[2] >= d and zz[1] < OWN + d
       and zz[2] < OWN + d and zz[1] + zz[2] >= OWN + d))
ok("4.f the blend-window family: action-indexed window threshold 3/2+delta "
   "(Theorem 9 at every depth); common/coupled 3/2+2delta - grid check at "
   "delta in {1/4, 1/2, 1}",
   all(((blend_window(zz, "action_indexed", d) is not None)
        == (zz[1] + zz[2] >= OWN + d))
       and ((blend_window(zz, "common", d) is not None)
            == (zz[1] >= d and zz[2] >= d and zz[1] + zz[2] >= OWN + 2 * d))
       for d in [Q(1, 4), Q(1, 2), Q(1)] for zz in G4 if zz[0] < Q(1)))
ok("4.g the delta = 0 degenerate case recovers the benign (no-event) datum: "
   "all classes coincide there",
   all(in_weak(zz, "common", Q(0)) == in_weak(zz, "coupled", Q(0))
       == in_weak(zz, "action_indexed", Q(0)) for zz in G4))

# ============================================================================
# PART 5 - the single-event sub-case (the row-(ii) literal reading)
# ============================================================================
print("PART 5 - the single-event sub-case (only the s1 event exists), delta = 1/2")
ok("5.1 single-event V_typ = {s1 >= 2} U {s2 >= 3/2, s1 >= 1/2} U "
   "{x >= 1, s1 >= 3/8} on the grid",
   all(in_typ(zz, "single", DELTA) == typ_single(zz, DELTA) for zz in G1))
ok("5.2 single-event V_weak = {x<1: s1 >= 1/2, sum >= 2} U {x>=1: s1 >= 3/8} "
   "on the grid",
   all(in_weak(zz, "single", DELTA) == weak_single(zz, DELTA) for zz in G1))
ok("5.3 the single-event gap {x<1, 1/2 <= s1 < 2, s2 < 3/2, sum >= 2} is nonempty; "
   "the canonical datum is a member",
   all(((in_weak(zz, "single", DELTA) and not in_typ(zz, "single", DELTA)) ==
        (zz[0] < Q(1) and zz[1] >= Q(1, 2) and zz[1] < Q(2)
         and zz[2] < Q(3, 2) and zz[1] + zz[2] >= Q(2))) for zz in G1))
ok("5.4 the single-event verdict at the canonical datum: gap (weak-accept, "
   "typed-reject)",
   in_weak(CANON, "single", DELTA) and not in_typ(CANON, "single", DELTA))

# ============================================================================
# PART 6 - summary witnesses for the record (all exact)
# ============================================================================
print("PART 6 - summary witnesses")
ok("6.1 THE MIDDLE-CELL VERDICT: the acceptance gap SURVIVES the common-shock "
   "regime - FP_cs = {x<1, 1/2 <= s_i < 2, s1+s2 >= 2}, strictly smaller than I "
   "by the exact cut min(s) >= 1/2, nonempty interior, canonical datum a member",
   in_gap_common(CANON)
   and all(in_gap_common(zz) == (in_weak(zz, "common", DELTA)
                                 and not in_typ(zz, "common", DELTA))
           for zz in G1 + WITNESS_LIST))
ok("6.2 the audit's asserted 'Reduced / Shifted' cell, made exact: reduced by the "
   "1/2-cut (check 1.8), thresholds unshifted on the surviving region (check 1.7)",
   True)  # aggregates 1.7 + 1.8 (both already fail-loud above)
ok("6.3 the qualitative rescue change: kappa* = infinity on {min(s) < 3/8} "
   "(checks 1.11-1.12)",
   True)
ok("6.4 the convexification fragility: the common-class gap survives blending on "
   "the band sum in [2, 5/2) (checks 2.1, 2.4-2.5)",
   True)
ok("6.5 the coupled-regime precision: the Section 5.4 verdict holds on I at the "
   "full magnitude (3.5), is depth-dependent with exact boundary 5/4 (3.7), "
   "relocates rather than vanishes under the additive reading (3.8), and "
   "COLLAPSES the typed/weak separation under the replace reading (3.12-3.13)",
   True)

print()
print("Part 0: datum and action-indexed handshake  (regime i)")
print("Part 1: the common-shock class               (regime ii - the middle cell)")
print("Part 2: the blend window / convexification")
print("Part 3: the coupled class, both readings      (regime iii)")
print("Part 4: the delta-family closed forms")
print("Part 5: the single-event sub-case")
print("Part 6: summary witnesses")
finish()
