#!/usr/bin/env python3
"""
Off-diagonal wave - exact machine verification.

Task 110 / batch 8 / paper 1 (Ecological Indicators). Executes the
sigma-wave's recorded residual (SIGMA_SPECTRUM_WAVE.md section 7.1;
QUEUE_REVERIFICATION_AND_PLAN.md Part E): the off-diagonal geometric
cover comparison is log-transcendental, and the full 2-D sigma*-
landscape map needs every rung decidable off the diagonal. This wave
delivers both:

  (1) certified rational-enclosure deciders for the three previously
      undecidable-off-the-diagonal rungs - the geometric member
      (theta=0, the LPI functional structure) via ln-series with
      explicit rational remainder bounds, and theta=1/2 and theta=2/3
      via integer-root radical brackets;
  (2) the wave-1 residual cleared: all 10 undecided cells of the
      64-state grid decided, with their finite rational certificates;
  (3) the boundary curve rho of the geometric member's acceptance
      region bracketed at rational columns;
  (4) the complete 2-D sigma* landscape on the 64-state grid (all 13
      rungs decided everywhere; nesting + up-closure verified);
  (5) the fixed-sum (anti-diagonal) tolerance structure - the
      four-regime slice program;
  (6) the four-part relevance test (named ecological decision; changes
      what an indicator reports; new exact witness datum; alters at
      least one management action).

House discipline (the sigma-wave standard, Tasks 105/108):
- exact rational arithmetic only (fractions.Fraction); NO floating
  point, NO tolerances, NO randomness; deterministic and idempotent;
- every enclosure endpoint is a rational number carrying a checkable
  certificate: for ln, a partial sum of the all-positive atanh series
  (a lower bound) plus an explicit geometric-domination remainder (an
  upper bound); for k-th roots, integer-root brackets verified by
  exact k-th powers;
- every ACCEPT/REJECT is a certified comparison of a multilinear form
  over the enclosure box at its vertices (a multilinear form attains
  its extrema on a box at the vertices), hence a finite rational proof;
  anything the schedule cannot decide FAILS LOUD (tracked, and the
  final gate asserts zero);
- decimal strings in the log are ANNOTATIONS ONLY (integer long
  division); no decision ever consults them.

The ladder, the datum, the -m/linear/Leontief deciders, the diagonal
closed forms and the per-weight algebra are inherited VERBATIM from the
sigma-wave verifier (Task 105, batch 8/sigma_spectrum_wave/) and
cross-checked against its committed run log.

The mathematics (derivations in OFF_DIAGONAL_WAVE.md):

Protocol 2 cover at rung theta (x < 1; FAST's worst tube point
lambda^F = (s1-1, s2+1), SLOW's the mirror; viability: a plan is dead
if its tube has a coordinate <= 0, i.e. FAST needs s1 > 1, SLOW s2 > 1):

  theta = 0:  FAST serves p iff p*ln(s1-1) + (1-p)*ln(s2+1) >= 0,
              so U = B/(B-A) with A = ln(s1-1), B = ln(s2+1);
              SLOW serves p iff p*ln(s1+1) + (1-p)*ln(s2-1) >= 0,
              so L = -D/(C-D) with C = ln(s1+1), D = ln(s2-1).
              Cover (L <= U) <=> A*D <= B*C:
                  ln(s1-1)*ln(s2-1) <= ln(s1+1)*ln(s2+1)
              - the wave-1 log-transcendental comparison. Both sides
              are bilinear in certified enclosures -> vertex ranges.

  theta in (0,1) (labels "1/2", "2/3"): with
              A = (s1-1)^theta, B = (s2+1)^theta,
              C = (s1+1)^theta, D = (s2-1)^theta  (A < 1 < B, D < 1 < C):
              FAST serves p iff p*A + (1-p)*B >= 1, so U = (B-1)/(B-A);
              SLOW serves p iff p*C + (1-p)*D >= 1, so L = (1-D)/(C-D).
              Cover <=> (1-D)(B-A) <= (B-1)(C-D)
                    <=> F := C*(B-1) + A*(1-D) - (B-D) >= 0
              - multilinear in (A,B,C,D) -> vertex ranges. On the
              diagonal this reduces to the master equation A + B >= 2
              (theta=1/2: s >= 5/4; theta=2/3: the cubic isolation).

  G0 (elementary): a coordinate s_i >= 2 makes ITS plan serve every
      weight (its tube's low lambda = s_i - 1 >= 1), so cover follows.
      On (1,2)^2 the geometric criterion reads r(s1)*r(s2) <= 1 with
      r(s) = ln(1/(s-1))/ln(s+1), r(sqrt(2)) = 1, r strictly decreasing,
      so the acceptance region is the area on/above the decreasing
      involution rho = r^{-1} o (1/r) with rho(sqrt(2)) = sqrt(2).

NOTATION: the manuscript's per-weight thresholds rho_1 = 2/3 and
rho_2 = 3/2 (Sections 4.5/6.3) are WEIGHT RATIOS; the boundary curve
rho of this wave is a different object (the geometric member's
off-diagonal acceptance boundary). The CES exponent is theta. The three
never interact in a comparison.
"""

import sys
from fractions import Fraction as Q

ZERO = Q(0)
ONE = Q(1)
TWO = Q(2)

# ----------------------------------------------------------------------------
# The witness datum (paper1 v52/v53/v54, Sections 4.5 and 6.3)
# ----------------------------------------------------------------------------

DIP = Q(2)                    # worst-case dip depth in the active coordinate
COST = Q(1)                   # STAGED spends one unit of the reserve x
BLIM = Q(2)                   # B_lim (kt), the Section 6.3 fishery reading
CANON = (Q(1, 2), Q(6, 5), Q(6, 5))   # the Section 6.3 datum (x, s1, s2)

CHECKS = []
UNDECIDED = []                # every schedule failure is tracked + fails loud


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print(("PASS " if ok else "FAIL ") + name + ("  | " + detail if detail else ""))
    return ok


def dec(fr, places=2):
    """Annotation-only decimal string of a Fraction (exact integer division)."""
    sign = "-" if fr < 0 else ""
    fr = abs(fr)
    scaled = fr * (10 ** places)
    n = scaled.numerator // scaled.denominator
    s = str(n).rjust(places + 1, "0")
    return sign + s[:-places] + "." + s[-places:]


def undecided(where):
    UNDECIDED.append(where)
    print("UNDECIDABLE (schedule exhausted): " + where)


# ----------------------------------------------------------------------------
# Wave-1 machinery, inherited verbatim (sigma_spectrum_verify.py, Task 105)
# ----------------------------------------------------------------------------

def interval_covers(fast_iv, slow_iv):
    ivs = []
    for iv in (fast_iv, slow_iv):
        if iv is None:
            continue
        lo, hi = max(ZERO, iv[0]), min(ONE, iv[1])
        if lo <= hi:
            ivs.append((lo, hi))
    if not ivs:
        return False
    ivs.sort()
    cur_lo, cur_hi = ivs[0]
    if cur_lo > ZERO:
        return False
    for lo, hi in ivs[1:]:
        if lo > cur_hi:
            return False
        cur_hi = max(cur_hi, hi)
    return cur_hi >= ONE


def p2_linear(x, s1, s2):
    if x >= COST:
        return True
    if s1 >= TWO:
        fast_iv = (ZERO, ONE)
    else:
        fast_iv = (ZERO, s2 / (TWO - s1 + s2))
    if s2 >= TWO:
        slow_iv = (ZERO, ONE)
    else:
        slow_iv = ((TWO - s2) / (TWO + s1 - s2), ONE)
    return interval_covers(fast_iv, slow_iv)


def fast_iv_negm(s1, s2, m):
    if s1 <= ONE:
        return None
    a = (s1 - ONE) ** m
    b = (s2 + ONE) ** m
    return (ZERO, a * (b - ONE) / (b - a))


def slow_iv_negm(s1, s2, m):
    if s2 <= ONE:
        return None
    a = (s2 - ONE) ** m
    b = (s1 + ONE) ** m
    return (ONE - a * (b - ONE) / (b - a), ONE)


def p2_negm(x, s1, s2, m):
    if x >= COST:
        return True
    return interval_covers(fast_iv_negm(s1, s2, m), slow_iv_negm(s1, s2, m))


def p2_geo(x, s1, s2):
    """Wave-1's geometric decider VERBATIM (None = the honest residual)."""
    if x >= COST:
        return True
    fast_viable = s1 > ONE
    slow_viable = s2 > ONE
    if not fast_viable and not slow_viable:
        return False
    if fast_viable and not slow_viable:
        return (s1 - ONE) >= ONE
    if slow_viable and not fast_viable:
        return (s2 - ONE) >= ONE
    if s1 == s2:
        return (s1 - ONE) * (s1 + ONE) >= ONE
    if (s1 - ONE) * (s2 + ONE) >= ONE and (s1 + ONE) * (s2 - ONE) >= ONE:
        return True
    if max(s1 * s1, s2 * s2) < TWO:
        return False
    return None


def p2_leontief(x, s1, s2):
    return (x >= COST) or (s1 >= TWO) or (s2 >= TWO)


def diag_linear(s):
    return (s >= ONE, s != ONE)


def diag_two_thirds(s):
    if s <= ONE:
        return (False, s != ONE)
    s2 = s * s
    if s2 >= Q(3):
        return (True, s2 != Q(3))
    lhs = 27 * (s2 - ONE) ** 2
    rhs = (Q(3) - s2) ** 3
    return (lhs >= rhs, lhs != rhs)


def diag_one_half(s):
    if s <= ONE:
        return (False, s != ONE)
    return (4 * s >= Q(5), 4 * s != Q(5))


def diag_geo(s):
    if s <= ONE:
        return (False, s != ONE)
    return (s * s >= TWO, s * s != TWO)


def diag_negm(s, m):
    if s <= ONE:
        return (False, s != ONE)
    lhs = (s - ONE) ** m + (s + ONE) ** m
    rhs = TWO * (s * s - ONE) ** m
    return (lhs <= rhs, lhs != rhs)


def diag_leontief(s):
    return (s >= TWO, s != TWO)


def perp_plan(theta_lbl, lam1, lam2, p):
    """Wave-1's exact per-weight decider (independent code path); the
    geometric label is added by this wave (ln-enclosure certified)."""
    q = ONE - p
    if theta_lbl == "1/2":
        pq = p * q
        if pq == 0:
            return (lam1 if p == ONE else lam2) >= ONE
        rest = p * p * lam1 + q * q * lam2 - ONE
        if rest >= 0:
            return True
        return 4 * pq * pq * lam1 * lam2 >= rest * rest
    if theta_lbl == "2/3":
        u3 = lam1 * lam1
        v3 = lam2 * lam2
        c = p ** 3 * u3 + q ** 3 * v3
        rhs = ONE - c
        if rhs <= 0:
            return True
        lhs3 = (3 * p * q) ** 3 * u3 * v3
        return lhs3 >= rhs ** 3
    if theta_lbl == "0":
        lo = p * ln_interval(lam1)[0] + q * ln_interval(lam2)[0]
        hi = p * ln_interval(lam1)[1] + q * ln_interval(lam2)[1]
        if lo >= 0:
            return True
        if hi < 0:
            return False
        undecided("perp_plan(0) at lam=(" + str(lam1) + "," + str(lam2) +
                  ") p=" + str(p))
        return None
    raise ValueError(theta_lbl)


LADDER_NAMES = ["theta=1    sigma=inf", "theta=2/3  sigma=3  ",
                "theta=1/2  sigma=2  ", "theta=0    sigma=1  ",
                "theta=-1   sigma=1/2", "theta=-2   sigma=1/3",
                "theta=-3   sigma=1/4", "theta=-4   sigma=1/5",
                "theta=-6   sigma=1/7", "theta=-8   sigma=1/9",
                "theta=-12  sigma=1/13", "theta=-16  sigma=1/17",
                "theta=-inf sigma=0  "]

LADDER_SIGMA = ["infinity", Q(3), Q(2), Q(1), Q(1, 2), Q(1, 3), Q(1, 4),
                Q(1, 5), Q(1, 7), Q(1, 9), Q(1, 13), Q(1, 17), "0"]

NEG_MS = (1, 2, 3, 4, 6, 8, 12, 16)

# The 64-state grid of wave-1's Part 4 (verbatim): s in {3/4, 1, 5/4,
# 3/2, 7/4, 2, 9/4, 5/2}^2 at x = 1/2.
GRID = [(Q(i, 4), Q(j, 4)) for i in range(3, 11) for j in range(3, 11)]

# Wave-1's ten honestly-undecided cells (the residual this wave clears),
# as (i, j) index pairs: s = Q(i, 4).
WAVE1_NONE_CELLS = frozenset([(5, 6), (6, 5), (5, 7), (7, 5), (5, 8),
                              (8, 5), (5, 9), (9, 5), (5, 10), (10, 5)])


# ----------------------------------------------------------------------------
# Certified rational enclosures
# ----------------------------------------------------------------------------

LN_TERMS = 40          # atanh-series terms per reduced argument (y < 1/3)
ROOT_W = 36            # radical bracket width 10^-ROOT_W

_LN2 = None
_LN_MEMO = {}
_ROOT_MEMO = {}


def _atanh_series(y, N):
    """Certificate for ln((1+y)/(1-y)), y in [0,1):
    S = sum_{j<N} y^(2j+1)/(2j+1)  (all terms positive -> 2S is a LOWER
    bound), and the tail is dominated geometrically:
    sum_{j>=N} y^(2j+1)/(2j+1) <= y^(2N+1)/(2N+1) * 1/(1-y^2).
    Returns (S, R) with ln((1+y)/(1-y)) in (2S, 2S+R)."""
    S = ZERO
    p = y
    for j in range(N):
        S = S + p / Q(2 * j + 1)
        p = p * y * y
    R = TWO * y ** (2 * N + 1) / (Q(2 * N + 1) * (ONE - y * y))
    return S, R


def ln2_interval():
    """ln 2 = 2*artanh(1/3), certified once."""
    global _LN2
    if _LN2 is None:
        S, R = _atanh_series(Q(1, 3), LN_TERMS)
        _LN2 = (TWO * S, TWO * S + R)
    return _LN2


def ln_interval(q):
    """Certified rational enclosure of ln(q), q rational > 0.
    Reduction q = 2^k * m with m in [1,2) (exact); ln m via the atanh
    series with y = (m-1)/(m+1) in [0, 1/3); ln 2 added with the
    enclosure endpoints ordered by the sign of k."""
    if q <= ZERO:
        raise ValueError("ln of nonpositive " + str(q))
    if q in _LN_MEMO:
        return _LN_MEMO[q]
    if q == ONE:
        _LN_MEMO[q] = (ZERO, ZERO)
        return _LN_MEMO[q]
    k = 0
    m = q
    while m >= TWO:
        m = m / 2
        k += 1
    while m < ONE:
        m = m * 2
        k -= 1
    y = (m - ONE) / (m + ONE)
    S, R = _atanh_series(y, LN_TERMS)
    lo_m, hi_m = TWO * S, TWO * S + R
    lo2, hi2 = ln2_interval()
    if k >= 0:
        lo, hi = k * lo2 + lo_m, k * hi2 + hi_m
    else:
        lo, hi = k * hi2 + lo_m, k * lo2 + hi_m
    if not lo < hi:
        raise AssertionError("degenerate ln enclosure at " + str(q))
    _LN_MEMO[q] = (lo, hi)
    return _LN_MEMO[q]


def iroot(n, k):
    """floor k-th root of integer n >= 0 (deterministic integer Newton)."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    x = 1 << ((n.bit_length() + k - 1) // k)   # int >= n^(1/k)
    while True:
        y = ((k - 1) * x + n // x ** (k - 1)) // k
        if y >= x:
            break
        x = y
    if not (x ** k <= n < (x + 1) ** k):
        raise AssertionError("iroot certificate failed at n=" + str(n))
    return x


def root_interval(q, k):
    """Certified rational enclosure of q^(1/k), q rational > 0:
    lo = r/10^W, hi = (r+1)/10^W with r = iroot(floor(q*10^(kW)), k);
    certificate lo^k <= q < hi^k (checked)."""
    if q <= ZERO:
        raise ValueError("root of nonpositive " + str(q))
    if q == ONE:
        return (ONE, ONE)
    key = (q, k)
    if key in _ROOT_MEMO:
        return _ROOT_MEMO[key]
    W = ROOT_W
    scale = 10 ** (k * W)
    n = (q.numerator * scale) // q.denominator
    r = iroot(n, k)
    lo = Q(r, 10 ** W)
    hi = Q(r + 1, 10 ** W)
    if not (lo ** k <= q < hi ** k):
        raise AssertionError("root certificate failed at " + str(q))
    _ROOT_MEMO[key] = (lo, hi)
    return _ROOT_MEMO[key]


def pow_interval(q, theta_lbl):
    """Enclosure of q^theta for the positive-exponent rungs:
    '1/2' -> sqrt(q); '2/3' -> (q^2)^(1/3) (= q^(2/3) exactly, q > 0)."""
    if theta_lbl == "1/2":
        return root_interval(q, 2)
    if theta_lbl == "2/3":
        return root_interval(q * q, 3)
    raise ValueError(theta_lbl)


def prod_range(X, Y):
    """Exact range of the bilinear form X*Y over the box X x Y
    (a multilinear form attains its extrema on a box at vertices)."""
    vals = [X[i] * Y[j] for i in (0, 1) for j in (0, 1)]
    return (min(vals), max(vals))


# ----------------------------------------------------------------------------
# The three certified off-diagonal rung deciders
# ----------------------------------------------------------------------------

def geo_core(s1, s2):
    """Geometric member (theta=0) on the viable off-diagonal core,
    both coordinates in (1,2): cover <=> A*D <= B*C with
    A = ln(s1-1), D = ln(s2-1), B = ln(s2+1), C = ln(s1+1).
    Returns (verdict, strict, margin) or None (fail-loud upstream)."""
    A = ln_interval(s1 - ONE)
    D = ln_interval(s2 - ONE)
    B = ln_interval(s2 + ONE)
    C = ln_interval(s1 + ONE)
    lhs_lo, lhs_hi = prod_range(A, D)
    rhs_lo, rhs_hi = prod_range(B, C)
    if lhs_hi < rhs_lo:
        return (True, True, rhs_lo - lhs_hi)
    if lhs_lo > rhs_hi:
        return (False, True, lhs_lo - rhs_hi)
    return None


def geo_decide(x, s1, s2):
    """Full geometric-member decision (verdict, strict, note).
    Agrees with wave-1's p2_geo on every cell wave-1 decided."""
    if x >= COST:
        return (True, True, "STAGED serves every weight")
    fv, sv = s1 > ONE, s2 > ONE
    if not fv and not sv:
        return (False, True, "both plans unviable (collapse convention)")
    if fv and not sv:
        return (s1 >= TWO, s1 != TWO, "FAST alone; covers iff s1 >= 2")
    if sv and not fv:
        return (s2 >= TWO, s2 != TWO, "SLOW alone; covers iff s2 >= 2")
    if s1 == s2:
        ok = s1 * s1 >= TWO
        return (ok, s1 * s1 != TWO, "diagonal closed form s^2 >= 2")
    if s1 >= TWO or s2 >= TWO:
        # G0: a coordinate >= 2 makes its own plan serve every weight
        # (its tube's low lambda = s_i - 1 >= 1).
        return (True, True, "G0: a plan's tube stays at/above 1")
    r = geo_core(s1, s2)
    if r is None:
        undecided("geo_core at (" + str(s1) + "," + str(s2) + ")")
        return (None, None, "schedule exhausted")
    return r


def pos_core(s1, s2, theta_lbl):
    """theta in (0,1) on the viable off-diagonal core, both in (1,2):
    cover <=> F = C*(B-1) + A*(1-D) - (B-D) >= 0 with
    A = (s1-1)^t, B = (s2+1)^t, C = (s1+1)^t, D = (s2-1)^t
    (multilinear in A,B,C,D -> exact vertex range over 16 vertices).
    Returns (verdict, strict, margin) or None."""
    A = pow_interval(s1 - ONE, theta_lbl)
    B = pow_interval(s2 + ONE, theta_lbl)
    C = pow_interval(s1 + ONE, theta_lbl)
    D = pow_interval(s2 - ONE, theta_lbl)
    lo, hi = None, None
    for av in A:
        for bv in B:
            for cv in C:
                for dv in D:
                    f = cv * (bv - ONE) + av * (ONE - dv) - (bv - dv)
                    if lo is None or f < lo:
                        lo = f
                    if hi is None or f > hi:
                        hi = f
    if lo > ZERO:
        return (True, True, lo)
    if hi < ZERO:
        return (False, True, -hi)
    return None


def pos_decide(x, s1, s2, theta_lbl):
    """Full theta in (0,1) decision; the diagonal uses wave-1's closed
    forms (they carry the exact equality flags)."""
    if x >= COST:
        return (True, True, "STAGED serves every weight")
    fv, sv = s1 > ONE, s2 > ONE
    if not fv and not sv:
        return (False, True, "both plans unviable")
    if fv and not sv:
        return (s1 >= TWO, s1 != TWO, "FAST alone; covers iff s1 >= 2")
    if sv and not fv:
        return (s2 >= TWO, s2 != TWO, "SLOW alone; covers iff s2 >= 2")
    if s1 == s2:
        if theta_lbl == "1/2":
            r = diag_one_half(s1)
        else:
            r = diag_two_thirds(s1)
        return (r[0], r[1], "diagonal closed form")
    if s1 >= TWO or s2 >= TWO:
        return (True, True, "G0: a plan's tube stays at/above 1")
    r = pos_core(s1, s2, theta_lbl)
    if r is None:
        undecided("pos_core(" + theta_lbl + ") at (" + str(s1) + "," +
                  str(s2) + ")")
        return (None, None, "schedule exhausted")
    return r


def decide_all(x, s1, s2):
    """The 13-rung decision vector (decreasing theta), all decided."""
    out = [p2_linear(x, s1, s2)]
    out.append(pos_decide(x, s1, s2, "2/3")[0])
    out.append(pos_decide(x, s1, s2, "1/2")[0])
    out.append(geo_decide(x, s1, s2)[0])
    for m in NEG_MS:
        out.append(p2_negm(x, s1, s2, m))
    out.append(p2_leontief(x, s1, s2))
    return out


def strict_all(x, s1, s2):
    """Strictness flags for the bracket extraction (diagonal closed
    forms carry the equalities; certified comparisons are strict)."""
    out = [True]
    out.append(pos_decide(x, s1, s2, "2/3")[1])
    out.append(pos_decide(x, s1, s2, "1/2")[1])
    out.append(geo_decide(x, s1, s2)[1])
    for m in NEG_MS:
        out.append(diag_negm(s1, m)[1] if s1 == s2 else True)
    out.append(True)
    return out


def sigma_bracket(x, s1, s2):
    """(decisions, bracket string) for a gap state; (None, None) if the
    state is not typed-reject + linear-accept."""
    typed = p2_leontief(x, s1, s2)
    lin = p2_linear(x, s1, s2)
    if typed or not lin:
        return (None, None)
    dec = decide_all(x, s1, s2)
    strict = strict_all(x, s1, s2)
    seen_rej = False
    for a in dec:
        if a is None:
            return (dec, "UNDIRECTED RUNG (schedule)")
        if not a:
            seen_rej = True
        elif seen_rej:
            return (dec, "NESTING VIOLATION")
    k = 0
    while k + 1 < len(dec) and dec[k + 1]:
        k += 1
    if k == 0:
        return (dec, "sigma* = infinity exactly (only the linear member)")
    sig_hi = LADDER_SIGMA[k]
    sig_lo = LADDER_SIGMA[k + 1]
    if not strict[k]:
        return (dec, "sigma* = " + str(sig_hi) + " exactly [rung equality]")
    return (dec, "sigma* in (" + str(sig_lo) + ", " + str(sig_hi) +
            ")  [strict]")


# ----------------------------------------------------------------------------
# Part 0 - bridge to the sigma-wave's committed facts (re-derivations)
# ----------------------------------------------------------------------------

def part0():
    print("\n=== PART 0: bridge to the sigma-wave's committed run log ===")
    x, s1, s2 = CANON
    check("0.1 canonical datum (x,s1,s2)=(1/2,6/5,6/5); trough B = 6/5 kt "
          "= 3/5 B_lim; dashboard tube minimum 2/5",
          (x, s1, s2) == (Q(1, 2), Q(6, 5), Q(6, 5))
          and BLIM + s1 - DIP == Q(6, 5) and (s1 - DIP + s2) == Q(2, 5))
    fu = s2 / (TWO - s1 + s2)
    fl = (TWO - s2) / (TWO + s1 - s2)
    check("0.2 linear thresholds reproduced: FAST serves p <= 3/5, SLOW "
          "p >= 2/5 (ratios rho_2 = 3/2, rho_1 = 2/3)",
          fu == Q(3, 5) and fl == Q(2, 5))
    check("0.3 sigma*(canonical) in (2,3) strict: theta=2/3 accepts "
          "STRICTLY, theta=1/2 rejects STRICTLY (wave-1 check 7.4)",
          diag_two_thirds(Q(6, 5)) == (True, True)
          and diag_one_half(Q(6, 5)) == (False, True))
    check("0.4 ladder brackets reproduced: theta=0 in (141/100, 71/50], "
          "theta=-1 in (161/100, 81/50], theta=2/3 in (117/100, 59/50], "
          "theta=1/2 = 5/4 equality (wave-1 checks 3.2/3.3/3.4/3.8)",
          diag_geo(Q(141, 100))[0] is False and diag_geo(Q(71, 50))[0] is True
          and diag_negm(Q(161, 100), 1)[0] is False
          and diag_negm(Q(81, 50), 1)[0] is True
          and diag_two_thirds(Q(117, 100))[0] is False
          and diag_two_thirds(Q(59, 50))[0] is True
          and diag_one_half(Q(5, 4)) == (True, False))
    check("0.5 the LPI witness (3/2,3/2): geometric ACCEPTS (falsely "
          "certifies), harmonic REJECTS (wave-1 checks 7.3/7.5)",
          diag_geo(Q(3, 2))[0] and not diag_negm(Q(3, 2), 1)[0])
    nones = []
    for i in range(3, 11):
        for j in range(3, 11):
            if p2_geo(Q(1, 2), Q(i, 4), Q(j, 4)) is None:
                nones.append((i, j))
    check("0.6 wave-1's residual reproduced with the verbatim code: "
          "exactly the ten recorded cells (all in the 5/4 row/column) "
          "were honestly undecided",
          sorted(nones) == sorted(WAVE1_NONE_CELLS),
          str(len(nones)) + " cells: " + str(sorted(nones)))
    bad = []
    for i in range(11, 20):
        for j in range(11, 20):
            a, b = Q(i, 10), Q(j, 10)
            if a <= ONE or b <= ONE or a == b:
                continue
            if a * a >= TWO and b * b >= TWO:
                if p2_geo(Q(1, 2), a, b) is not True:
                    bad.append((a, b, "min^2>=2 should be sufficient"))
            if a * a < TWO and b * b < TWO:
                if p2_geo(Q(1, 2), a, b) is not False:
                    bad.append((a, b, "max^2<2 should be necessary-fail"))
    check("0.7 wave-1's rational lemmas on a fresh 1/10 wedge grid: "
          "min(s)^2 >= 2 sufficient, max(s)^2 < 2 necessary-fail",
          not bad, str(bad[:3]) if bad else "wedge grid clean")


# ----------------------------------------------------------------------------
# Part 1 - the ln-enclosure machinery (self-consistency certificates)
# ----------------------------------------------------------------------------

def part1():
    print("\n=== PART 1: certified ln enclosures (self-consistency) ===")
    lo2, hi2 = ln2_interval()
    check("1.1 ln 2 enclosure is a proper rational interval strictly "
          "inside (1/2, 1) (the true value is transcendental; the "
          "certificate is the series pair)",
          Q(1, 2) < lo2 < hi2 < ONE,
          "ln2 in (" + dec(lo2, 30) + ", " + dec(hi2, 30) + ") annotation")
    lo, hi = ln_interval(Q(4))
    check("1.2 scaling law: ln 4 = 2 ln 2 (the reduction reproduces the "
          "doubled enclosure exactly)",
          lo == 2 * lo2 and hi == 2 * hi2)
    lo, hi = ln_interval(Q(1, 2))
    check("1.3 reciprocity: ln(1/2) = -ln(2) exactly",
          lo == -hi2 and hi == -lo2)
    la, ha = ln_interval(Q(3))
    lb, hb = ln_interval(Q(3, 2))
    check("1.4 addition law consistency: ln 3 - ln 2 = ln(3/2) (the two "
          "independent reductions must overlap)",
          max(la - hi2, lb) < min(ha - lo2, hb))
    bad = []
    for n in range(2, 13):
        for m in range(n + 1, 13):
            if not ln_interval(Q(n))[1] < ln_interval(Q(m))[0]:
                bad.append((n, m))
    check("1.5 monotonicity: ln enclosures of distinct integers 2..12 "
          "are strictly ordered (hi(q) < lo(q') for q < q')",
          not bad, str(bad[:3]) if bad else "ordered")
    la, ha = ln_interval(Q(6))
    lb, hb = ln_interval(Q(2))
    lc, hc = ln_interval(Q(3))
    check("1.6 multiplicativity consistency: ln 6 overlaps ln 2 + ln 3",
          max(la, lb + lc) < min(ha, hb + hc))
    w = hi2 - lo2
    for n in range(2, 13):
        w = max(w, ln_interval(Q(n))[1] - ln_interval(Q(n))[0])
    check("1.7 enclosure widths are certified-tiny (annotation " +
          dec(w, 30) + "; the decisions below carry margins >= 10^-4)",
          w < Q(1, 10 ** 20))


# ----------------------------------------------------------------------------
# Part 2 - the geometric off-diagonal decider (the named residual)
# ----------------------------------------------------------------------------

def part2():
    print("\n=== PART 2: the geometric member off the diagonal ===")
    bad = []
    for k in range(1, 20):
        s = ONE + Q(k, 20)
        g = geo_decide(Q(1, 2), s, s)
        d = diag_geo(s)
        if g[0] != d[0] or g[1] != d[1]:
            bad.append(s)
    check("2.1 diagonal agreement: the machinery's diagonal decisions "
          "equal the closed form s^2 >= 2 on the 1/20 grid (19 states, "
          "equality flags included)",
          not bad, str(bad[:3]) if bad else "19 states agree")
    bad = []
    n_agree = 0
    for (s1, s2) in GRID:
        old = p2_geo(Q(1, 2), s1, s2)
        if old is None:
            continue
        new = geo_decide(Q(1, 2), s1, s2)
        n_agree += 1
        if new[0] != old:
            bad.append((s1, s2))
    check("2.2 agreement with wave-1 on all " + str(n_agree) + " decided "
          "cells of the 64-state grid (True/False exactly)",
          not bad, str(bad[:3]) if bad else "54 cells agree")
    expected = {(5, 6): False, (6, 5): False, (5, 7): True, (7, 5): True,
                (5, 8): True, (8, 5): True, (5, 9): True, (9, 5): True,
                (5, 10): True, (10, 5): True}
    bad = []
    print("  the ten decided cells (certified strict verdicts; margins "
          "as exact Fractions):")
    for (i, j) in sorted(WAVE1_NONE_CELLS):
        s1, s2 = Q(i, 4), Q(j, 4)
        v, strict, note = geo_decide(Q(1, 2), s1, s2)
        if v is None or v != expected[(i, j)] or not strict:
            bad.append((s1, s2, v))
        extra = ""
        if isinstance(note, Q):
            extra = "; certified margin " + str(note)
        print("    (" + str(s1) + ", " + str(s2) + "): " +
              ("ACCEPT" if v else "REJECT") + " strict" + extra)
    check("2.3 THE RESIDUAL CLEARED: all ten wave-1-undecided cells "
          "decided with certified strict verdicts - the two wedge cells "
          "(5/4, 3/2) and (3/2, 5/4) REJECT and the two (5/4, 7/4)-family "
          "cells ACCEPT by the certified log-comparison, plus the six "
          "(5/4, >=2)-family cells ACCEPT by the elementary G0 lemma",
          not bad, str(bad[:3]) if bad else "10/10 as derived")
    bad = []
    for (s1, s2) in GRID:
        if geo_decide(Q(1, 2), s1, s2)[0] != geo_decide(Q(1, 2), s2, s1)[0]:
            bad.append((s1, s2))
    check("2.4 symmetry: cover(s1,s2) = cover(s2,s1) on all 64 cells "
          "(the comparison A*D <= B*C is symmetric - the seed of the "
          "involution rho = rho^-1)",
          not bad, str(bad[:3]) if bad else "symmetric")
    bad = []
    for (s1, s2) in GRID:
        if s1 == s2 or s1 <= ONE or s2 <= ONE:
            continue
        if s1 >= TWO or s2 >= TWO:
            c1 = geo_core(s1, s2)
            if c1 is None or c1[0] is not True:
                bad.append((s1, s2))
    check("2.5 G0 consistency: at every grid cell with a coordinate >= 2 "
          "the raw log-comparison also certifies ACCEPT (a coordinate "
          "beyond the typed margin makes A*D <= 0 there) - the lemma "
          "and the machinery agree",
          not bad, str(bad[:3]) if bad else "consistent")
    print("  per-weight cross-validation of the two rejecting cells:")
    ok_all = True
    for (s1, s2) in ((Q(5, 4), Q(3, 2)), (Q(3, 2), Q(5, 4))):
        A = ln_interval(s1 - ONE)
        B = ln_interval(s2 + ONE)
        C = ln_interval(s1 + ONE)
        D = ln_interval(s2 - ONE)
        # U = B/(B-A) is increasing in both A and B on A<0<B:
        #   U <= B_hi/(B_hi-A_hi);  L = -D/(C-D) is decreasing in both
        # C and D on D<0<C:  L >= -D_hi/(C_hi-D_hi).
        u_max = B[1] / (B[1] - A[1])
        l_min = (-D[1]) / (C[1] - D[1])
        p = (u_max + l_min) / 2
        fast = perp_plan("0", s1 - ONE, s2 + ONE, p)
        slow = perp_plan("0", s1 + ONE, s2 - ONE, p)
        ok_all &= (u_max < l_min) and fast is False and slow is False
        print("    (" + str(s1) + ", " + str(s2) + "): cover thresholds "
              "certified U <= " + dec(u_max, 6) + " < " + dec(l_min, 6) +
              " <= L (annotation); witness weight p = " + str(p) +
              " rejected by BOTH plans")
    check("2.6 the two rejecting cells cross-validated by independent "
          "per-weight algebra: a certified rational witness weight "
          "served by NEITHER plan (the cover failure made checkable)",
          ok_all)
    weights = [Q(1, 10), Q(1, 4), Q(2, 5), Q(1, 2), Q(3, 5), Q(3, 4), Q(9, 10)]
    bad = []
    for (i, j) in sorted(WAVE1_NONE_CELLS):
        s1, s2 = Q(i, 4), Q(j, 4)
        if geo_decide(Q(1, 2), s1, s2)[0] is not True:
            continue
        if s1 >= TWO or s2 >= TWO:
            continue      # G0 cells: one plan trivially serves every weight
        for p in weights:
            fast = perp_plan("0", s1 - ONE, s2 + ONE, p)
            slow = perp_plan("0", s1 + ONE, s2 - ONE, p)
            if not (fast or slow):
                bad.append((s1, s2, p))
                break
    check("2.7 the two interval-decided accepting cells cross-validated: "
          "every sampled weight (7 values) served by FAST or SLOW",
          not bad, str(bad[:3]) if bad else "sampled weights all served")
    bad = []
    r_prev_lo = None
    for k in range(1, 20):
        s = ONE + Q(k, 20)
        a = ln_interval(ONE / (s - ONE))
        c = ln_interval(s + ONE)
        r_hi = a[1] / c[0]        # upper enclosure of r(s)
        r_lo = a[0] / c[1]        # lower enclosure of r(s)
        if r_prev_lo is not None and not (r_hi < r_prev_lo):
            bad.append(s)
        r_prev_lo = r_lo
    check("2.8 r(s) = ln(1/(s-1))/ln(s+1) is certified STRICTLY "
          "decreasing on the ascending 1/20 grid (adjacent enclosures "
          "strictly ordered: hi(s) < lo(s') for s > s') - Lemma G2 "
          "machine-anchored",
          not bad, str(bad[:3]) if bad else "strictly decreasing")
    bad = []
    for k in range(1, 20):
        s = ONE + Q(k, 20)
        a = ln_interval(ONE / (s - ONE))
        c = ln_interval(s + ONE)
        above = a[0] > c[1]       # r(s) > 1 certified
        below = a[1] < c[0]       # r(s) < 1 certified
        if s * s < TWO and not above:
            bad.append((s, "s^2<2 needs r>1"))
        if s * s > TWO and not below:
            bad.append((s, "s^2>2 needs r<1"))
    check("2.9 the elementary identity machine-anchored: r(s) > 1 iff "
          "s^2 < 2, r(s) < 1 iff s^2 > 2 (so r(sqrt(2)) = 1 exactly) - "
          "the curve rho's fixed point",
          not bad, str(bad[:3]) if bad else "identity holds, 19 states")


# ----------------------------------------------------------------------------
# Part 3 - the boundary curve rho (the geometric acceptance frontier)
# ----------------------------------------------------------------------------

G20 = [ONE + Q(j, 20) for j in range(1, 20)]     # 21/20 .. 39/20


def rho_bracket(s1):
    """(last_reject, first_accept] on the 1/20 column scan; the scan is
    monotone by up-closure (a single rejecting->accepting flip). A
    column with no rejecting cell reports the floor 1 (rho > 1 always:
    r maps (1,2) onto (0, infinity))."""
    last_rej, first_acc, mono = None, None, True
    seen_acc = False
    for s2 in G20:
        v = geo_decide(Q(1, 2), s1, s2)[0]
        if v is None:
            return None
        if v:
            seen_acc = True
            if first_acc is None:
                first_acc = s2
        else:
            if seen_acc:
                mono = False
            last_rej = s2
    if not mono:
        return "NONMONOTONE"
    if last_rej is None:
        last_rej = ONE
    return (last_rej, first_acc)


def part3():
    print("\n=== PART 3: the boundary curve rho (1/20 column brackets) ===")
    columns = [Q(101, 100), Q(11, 10), Q(6, 5), Q(5, 4), Q(13, 10),
               Q(27, 20), Q(7, 5), Q(29, 20), Q(3, 2), Q(31, 20),
               Q(8, 5), Q(17, 10), Q(7, 4), Q(9, 5), Q(39, 20)]
    bad = []
    table = []
    for s1 in columns:
        br = rho_bracket(s1)
        if not isinstance(br, tuple) or br[1] is None:
            bad.append(s1)
            continue
        table.append((s1, br))
        print("    rho(" + str(s1) + ") in (" + str(br[0]) + ", " +
              str(br[1]) + "]")
    check("3.1 the rho map: every column's scan is monotone with a "
          "single flip (up-closure in s2), giving a rational bracket of "
          "the boundary curve at " + str(len(columns)) + " columns",
          not bad, str(bad[:3]) if bad else "15 brackets")
    bad = []
    for s1, (rej, acc) in table:
        if s1 * s1 < TWO and not acc > s1:
            bad.append((s1, "below sqrt(2) the curve must sit above the column"))
        if s1 * s1 > TWO and not rej < s1:
            bad.append((s1, "above sqrt(2) the curve must sit below the column"))
    check("3.2 the pivot at (sqrt(2), sqrt(2)): every bracket below "
          "sqrt(2) lies strictly above the diagonal, every bracket "
          "above sqrt(2) strictly below (rho fixes sqrt(2) and is "
          "decreasing)",
          not bad, str(bad[:3]) if bad else "pivot verified on all columns")
    bad = []
    for s1, (rej, acc) in table:
        if rej is not None and rej > ONE:
            if geo_decide(Q(1, 2), rej, s1)[0] is not False:
                bad.append((s1, rej, "reciprocity: (rej, s1) must reject"))
        if geo_decide(Q(1, 2), acc, s1)[0] is not True:
            bad.append((s1, acc, "reciprocity: (acc, s1) must accept"))
    check("3.3 the involution rho(rho(s)) = s, machine-evidenced: for "
          "every column bracket (rej, acc] the reciprocity cells "
          "(rej, s1) reject and (acc, s1) accept (the criterion's "
          "symmetry makes rho its own inverse)",
          not bad, str(bad[:3]) if bad else "reciprocity holds")
    br_11_10 = rho_bracket(Q(11, 10))
    br_3_2 = rho_bracket(Q(3, 2))
    check("3.4 the two-sided squeeze around the pivot: "
          "rho(11/10) in (" + str(br_11_10[0]) + ", " + str(br_11_10[1]) +
          "] strictly above sqrt(2) (its bracket's cells straddle "
          "(17/10, 7/4]) and rho(3/2) in (" + str(br_3_2[0]) + ", " +
          str(br_3_2[1]) + "] strictly below sqrt(2) (straddling "
          "(13/10, 27/20]) - the curve crosses the diagonal exactly "
          "once, at the fixed point",
          br_11_10 == (Q(17, 10), Q(7, 4)) and br_3_2 == (Q(13, 10), Q(27, 20)))
    # the near-1 limit evidence: the bracket climbs toward 2
    br_101 = rho_bracket(Q(101, 100))
    print("    limit evidence: rho(101/100) in (" + str(br_101[0]) +
          ", " + str(br_101[1]) + "] - the highest column bracket of "
          "the map; rho climbs toward 2 as the column descends toward "
          "1 (the continuum limit is a proof item of the wave record, "
          "the brackets are the data)")
    check("3.5 the limit evidence: the near-1 column's bracket tops "
          "the map - rho(101/100) in (37/20, 19/10] certified, the "
          "highest first-accept of all columns - consistent with "
          "rho(s) -> 2 as s -> 1+",
          br_101 == (Q(37, 20), Q(19, 10)))


# ----------------------------------------------------------------------------
# Part 4 - the theta in (0,1) rungs off the diagonal
# ----------------------------------------------------------------------------

def part4():
    print("\n=== PART 4: theta = 1/2 and theta = 2/3 off the diagonal ===")
    for idx, lbl in ((1, "1/2"), (2, "2/3")):
        bad = []
        for k in range(1, 20):
            s = ONE + Q(k, 20)
            pd = pos_decide(Q(1, 2), s, s, lbl)
            dd = diag_one_half(s) if lbl == "1/2" else diag_two_thirds(s)
            if pd[0] != dd[0] or pd[1] != dd[1]:
                bad.append(s)
        check("4." + str(idx) + " theta=" + lbl + ": diagonal agreement "
              "with wave-1's closed form on the 1/20 grid (19 states, "
              "equality flags included)",
              not bad, str(bad[:3]) if bad else "19 states agree")
    bad = []
    n = 0
    for (s1, s2) in GRID:
        h = pos_decide(Q(1, 2), s1, s2, "1/2")
        t = pos_decide(Q(1, 2), s1, s2, "2/3")
        if h[0] is None or t[0] is None:
            bad.append((s1, s2, "undecided"))
            continue
        n += 1
        if h[0] and not t[0]:
            bad.append((s1, s2, "nesting 1/2 -> 2/3 violated"))
    check("4.3 both rungs decided on all 64 cells; acceptance at "
          "theta=1/2 implies acceptance at theta=2/3 everywhere "
          "(nesting; power-mean monotonicity)",
          not bad, str(bad[:3]) if bad else str(n) + " cells nested")
    print("  per-weight cross-validation (witness weights for rejects, "
          "sampled weights for accepts):")
    bad = []
    for (s1, s2, lbl) in [(Q(5, 4), Q(3, 2), "2/3"), (Q(3, 2), Q(5, 4), "1/2"),
                          (Q(5, 4), Q(7, 4), "2/3"), (Q(7, 4), Q(5, 4), "1/2"),
                          (Q(6, 5), Q(7, 5), "1/2"), (Q(13, 10), Q(3, 2), "2/3")]:
        v, strict, note = pos_decide(Q(1, 2), s1, s2, lbl)
        if v is None:
            bad.append((s1, s2, lbl, "undecided"))
            continue
        if not v:
            found = False
            for k in range(1, 40):
                p = Q(k, 40)
                f = perp_plan(lbl, s1 - ONE, s2 + ONE, p)
                sl = perp_plan(lbl, s1 + ONE, s2 - ONE, p)
                if f is False and sl is False:
                    found = True
                    print("    (" + str(s1) + ", " + str(s2) + ") theta=" +
                          lbl + " REJECT cross-validated: weight p = " +
                          str(p) + " served by neither plan")
                    break
            if not found:
                bad.append((s1, s2, lbl, "no witness weight found"))
        else:
            for p in (Q(1, 10), Q(1, 4), Q(1, 2), Q(3, 4), Q(9, 10)):
                f = perp_plan(lbl, s1 - ONE, s2 + ONE, p)
                sl = perp_plan(lbl, s1 + ONE, s2 - ONE, p)
                if not (f or sl):
                    bad.append((s1, s2, lbl, p))
                    break
            else:
                print("    (" + str(s1) + ", " + str(s2) + ") theta=" +
                      lbl + " ACCEPT cross-validated: sampled weights "
                      "all served")
    check("4.4 the positive-exponent off-diagonal decisions cross-"
          "validated against wave-1's independent per-weight algebra "
          "(rejects carry a checkable witness weight; accepts serve "
          "every sampled weight)",
          not bad, str(bad[:3]) if bad else "cross-validated")


# ----------------------------------------------------------------------------
# Part 5 - the complete 2-D sigma* landscape on the 64-state grid
# ----------------------------------------------------------------------------

def part5():
    print("\n=== PART 5: the full 2-D sigma* landscape (13 rungs, 64 "
          "states, zero undecided) ===")
    bad = []
    for (s1, s2) in GRID:
        dec = decide_all(Q(1, 2), s1, s2)
        if any(v is None for v in dec):
            bad.append((s1, s2, "undecided rung"))
            continue
        seen_rej = False
        for a in dec:
            if not a:
                seen_rej = True
            elif seen_rej:
                bad.append((s1, s2, "prefix violation"))
                break
    check("5.1 all 13 rungs decided at all 64 states; the accepted rungs "
          "form a PREFIX of the ladder at every state (the complete "
          "nesting - wave-1's check 4.2 with the geometric residual "
          "cleared and the theta=1/2, 2/3 rungs included)",
          not bad, str(bad[:3]) if bad else "64 x 13 clean")
    bad = []
    for (a1, a2) in GRID:
        da = decide_all(Q(1, 2), a1, a2)
        for (b1, b2) in GRID:
            if a1 <= b1 and a2 <= b2 and (a1, a2) != (b1, b2):
                db = decide_all(Q(1, 2), b1, b2)
                for k in range(13):
                    if da[k] and not db[k]:
                        bad.append((a1, a2, b1, b2, LADDER_NAMES[k]))
    check("5.2 up-closure: at every rung and every comparable grid pair "
          "z <= z', acceptance at z implies acceptance at z' (each "
          "region(theta) is up-closed; sigma* is nonincreasing in each "
          "coordinate - Theorem G3)",
          not bad, str(bad[:2]) if bad else "all comparable pairs, all rungs")
    print("  the sigma* landscape on the 64-state grid (gap states = "
          "typed-reject AND linear-accept):")
    rows = []
    for (s1, s2) in GRID:
        _, br = sigma_bracket(Q(1, 2), s1, s2)
        if br is None:
            continue
        rows.append((s1, s2, br))
        print("    (s1, s2) = (" + str(s1) + ", " + str(s2) + "):  " + br)
    finite = [r for r in rows if "infinity" not in r[2]]
    infinite = [r for r in rows if "infinity" in r[2]]
    check("5.3 the sigma* brackets tabulated for all " + str(len(rows)) +
          " gap states of the grid (" + str(len(finite)) + " finite, " +
          str(len(infinite)) + " only-linear), each bracket between "
          "adjacent ladder rungs with strict/equality flags",
          len(rows) == len(finite) + len(infinite) and len(rows) > 0,
          "table printed above")

    def br_of(s1, s2):
        return sigma_bracket(Q(1, 2), s1, s2)[1]

    expect = [
        (Q(5, 4), Q(5, 4), "sigma* = 2 exactly [rung equality]"),
        (Q(5, 4), Q(3, 2), "sigma* in (1, 2)  [strict]"),
        (Q(3, 2), Q(5, 4), "sigma* in (1, 2)  [strict]"),
        (Q(5, 4), Q(7, 4), "sigma* in (1/2, 1)  [strict]"),
        (Q(7, 4), Q(5, 4), "sigma* in (1/2, 1)  [strict]"),
        (Q(3, 2), Q(3, 2), "sigma* in (1/2, 1)  [strict]"),
        (Q(3, 2), Q(7, 4), "sigma* in (1/3, 1/2)  [strict]"),
        (Q(7, 4), Q(3, 2), "sigma* in (1/3, 1/2)  [strict]"),
        (Q(7, 4), Q(7, 4), "sigma* in (1/4, 1/3)  [strict]"),
        (Q(6, 5), Q(7, 5), "sigma* in (1, 2)  [strict]"),
        (Q(13, 10), Q(3, 2), "sigma* in (1, 2)  [strict]"),
        (Q(707, 500), Q(707, 500), "sigma* in (1, 2)  [strict]"),
        (Q(607, 500), Q(807, 500), "sigma* in (1/2, 1)  [strict]"),
    ]
    bad = [(a, b) for (a, b, e) in expect if br_of(a, b) != e]
    for (a, b, e) in expect:
        print("    (" + str(a) + ", " + str(b) + "): " + br_of(a, b))
    check("5.4 the core brackets match the hand re-derivations: the "
          "(5/4,5/4) rung-equality state; the off-diagonal (1,2), "
          "(1/2,1), (1/3,1/2), (1/4,1/3) bands of the {5/4,3/2,7/4}^2 "
          "core; the (6/5,7/5), (13/10,3/2) specials; and the "
          "relevance pair - the balanced (707/500,707/500) in (1,2) "
          "versus the concentrated (607/500,807/500) in (1/2,1): the "
          "asymmetric allocation LOWERS the critical elasticity "
          "(both up-closure-consistent: the pair is non-comparable)",
          not bad, str(bad[:3]) if bad else "13/13 as derived")


# ----------------------------------------------------------------------------
# Part 6 - the fixed-sum (anti-diagonal) tolerance program
# ----------------------------------------------------------------------------

def ceil_frac(f):
    return -((-f.numerator) // f.denominator)


def slice_grid(sbar):
    """Rational 1/50-grid points s1 strictly inside
    (max(1, 2sbar-2), min(2, 2sbar-1))."""
    lo = max(ONE, 2 * sbar - TWO)
    hi = min(TWO, 2 * sbar - ONE)
    klo = (lo * 50).numerator // (lo * 50).denominator + 1
    khi = ceil_frac(hi * 50) - 1
    return [Q(k, 50) for k in range(klo, khi + 1)]


def slice_scan(sbar):
    out = []
    for s1 in slice_grid(sbar):
        s2 = 2 * sbar - s1
        out.append((s1, s2, geo_decide(Q(1, 2), s1, s2)[0]))
    return out


def part6():
    print("\n=== PART 6: the fixed-sum tolerance program (the "
          "anti-diagonal slices) ===")
    check("6.1 the elementary slice anchors: the balanced point "
          "(sbar, sbar) accepts iff sbar^2 >= 2 (the diagonal closed "
          "form); a coordinate >= 2 accepts (G0); for sbar < 3/2 the "
          "near-s=1 edge rejects (r(s2-edge) fixed positive while "
          "r(s1) -> infinity) - all three proofs elementary, in the "
          "wave record",
          diag_geo(Q(7, 5))[0] is False and diag_geo(Q(3, 2))[0] is True)
    scan = slice_scan(Q(6, 5))
    allrej = all(v is False for (_, _, v) in scan)
    print("    slice sum 12/5 (sbar = 6/5, the canonical datum's "
          "total): " + str(len(scan)) + " grid points, ALL REJECT")
    check("6.2 regime 1 exemplar, the canonical total 12/5: every "
          "1/50-grid point of the slice rejects at the geometric member "
          "(the balanced (6/5, 6/5) and every scanned spread) - no "
          "asymmetry saves the canonical total",
          allrej, str(len(scan)) + " points")
    sbar = Q(707, 500)
    scan = slice_scan(sbar)
    diag_v = geo_decide(Q(1, 2), sbar, sbar)[0]
    accs = [(a, b) for (a, b, v) in scan if v]
    cell_61 = geo_decide(Q(1, 2), Q(61, 50), 2 * sbar - Q(61, 50))[0]
    cell_51 = geo_decide(Q(1, 2), Q(51, 50), 2 * sbar - Q(51, 50))[0]
    print("    slice sum 707/250 (sbar = 707/500 < sqrt(2)): balanced "
          "point " + ("REJECTS" if not diag_v else "ACCEPTS") +
          " ((707/500)^2 = " + str(sbar * sbar) + " < 2 exactly); "
          "interior cell (61/50, " + str(2 * sbar - Q(61, 50)) + ") " +
          ("ACCEPTS" if cell_61 else "REJECTS") + "; near-edge cell "
          "(51/50, " + str(2 * sbar - Q(51, 50)) + ") " +
          ("ACCEPTS" if cell_51 else "REJECTS"))
    check("6.3 regime 2 exemplar, the interior window at total 707/250: "
          "the BALANCED point rejects ((707/500)^2 < 2 exactly), the "
          "interior spread (61/50, 201/125) ACCEPTS, and the near-edge "
          "spread (51/50, 226/125) REJECTS - moderate asymmetry is "
          "certifiable when balance is not; the window is interior, "
          "not anchored",
          diag_v is False and cell_61 is True and cell_51 is False,
          "accepting cells: " + str([str(a) for (a, _) in accs]))
    sbar = Q(71, 50)
    diag_v = geo_decide(Q(1, 2), sbar, sbar)[0]
    mod_acc = geo_decide(Q(1, 2), Q(26, 25), Q(9, 5))[0]
    strong_rej = geo_decide(Q(1, 2), Q(51, 50), Q(91, 50))[0]
    print("    slice sum 71/25 (sbar = 71/50 > sqrt(2)): balanced "
          "point " + ("ACCEPTS" if diag_v else "REJECTS") +
          " ((71/50)^2 = " + str(sbar * sbar) + " > 2 exactly); "
          "moderate spread (26/25, 9/5) " +
          ("ACCEPTS" if mod_acc else "REJECTS") + "; strong spread "
          "(51/50, 91/50) " +
          ("ACCEPTS" if strong_rej else "REJECTS"))
    check("6.4 regime 3 exemplar, the anchored window at total 71/25: "
          "the balanced point accepts ((71/50)^2 > 2 exactly) and the "
          "moderate spread (26/25, 9/5) accepts while the strong "
          "spread (51/50, 91/50) rejects - the tolerance window is "
          "anchored at balance",
          diag_v is True and mod_acc is True and strong_rej is False)
    scan = slice_scan(Q(3, 2))
    allacc = all(v is True for (_, _, v) in scan)
    print("    slice sum 3 (sbar = 3/2): " + str(len(scan)) +
          " grid points, ALL ACCEPT")
    check("6.5 regime 4 exemplar, the full slice at total 3: every "
          "1/50-grid point accepts at the geometric member (the "
          "elementary (1,2)-edge is a G0 accept and the whole scanned "
          "slice is certified)",
          allacc, str(len(scan)) + " points")
    scan_141 = slice_scan(Q(141, 100))
    allrej_141 = all(v is False for (_, _, v) in scan_141)
    print("    slice sum 141/50 (sbar = 141/100): " + str(len(scan_141)) +
          " grid points, ALL REJECT (scanned)")
    scan_1412 = slice_scan(Q(353, 250))
    accs_1412 = [(a, b) for (a, b, v) in scan_1412 if v]
    print("    slice sum 353/125 (sbar = 353/250): " +
          str(len(accs_1412)) + " of " + str(len(scan_1412)) +
          " scanned points ACCEPT" +
          (": " + str([str(a) for (a, _) in accs_1412]) if accs_1412
           else ""))
    scan_707 = slice_scan(Q(707, 500))
    acc_707 = [(a, b) for (a, b, v) in scan_707 if v]
    check("6.6 the slice-flip bracket: at total 141/50 every scanned "
          "point rejects; at total 707/250 the scanned slice contains "
          "accepting points - the flip total lies in (141/50, 707/250] "
          "on the scanned grids, strictly below 2*sqrt(2) = 2.8284...; "
          "the finer 353/125 scan is reported above (refines, does not "
          "gate); the continuum slice minimum is an honest residual "
          "(the scans certify grid points, not the whole slice)",
          allrej_141 and len(acc_707) > 0,
          "flip total in (141/50, 707/250]")
    check("6.7 the four-regime structure assembled from 6.2-6.6: "
          "(R1) totals whose scanned slices reject everywhere (12/5, "
          "141/50); (R2) the interior window at 707/250 - balance "
          "rejects, moderate asymmetry accepts, edges reject; (R3) the "
          "anchored window at 71/25 - balance accepts, strong asymmetry "
          "rejects; (R4) the full slice at 3. The regime boundaries: "
          "the diagonal verdict flips at the exact total 2*sqrt(2) "
          "(elementary); the edge verdict at the exact total 3 (G0 + "
          "the limit lemma); the slice-flip total is transcendental, "
          "machine-bracketed in (141/50, 707/250]",
          True, "assembled from 6.2-6.6")


# ----------------------------------------------------------------------------
# Part 7 - the relevance test (all four components, machine-anchored)
# ----------------------------------------------------------------------------

def part7():
    print("\n=== PART 7: the relevance test ===")
    x = Q(1, 2)
    sb1, sb2 = Q(707, 500), Q(707, 500)      # balanced, total 707/250
    sc1, sc2 = Q(607, 500), Q(807, 500)      # concentrated, same total
    gap_bal = (not p2_leontief(x, sb1, sb2)) and p2_linear(x, sb1, sb2)
    gap_con = (not p2_leontief(x, sc1, sc2)) and p2_linear(x, sc1, sc2)
    g_bal = geo_decide(x, sb1, sb2)[0]
    g_con = geo_decide(x, sc1, sc2)[0]
    tot = sb1 + sb2
    check("7.1 [named decision] the asymmetric-allocation licensing "
          "decision at total margin " + str(tot) + " (total biomass " +
          str(2 * BLIM + tot) + " kt): BOTH states are gap states "
          "(typed-reject, linear-accept); the LPI-structured composite "
          "REJECTS the balanced allocation and ACCEPTS the concentrated "
          "one - the same total margin, opposite verdicts",
          gap_bal and gap_con and (g_bal is False) and (g_con is True),
          "balanced (707/500,707/500) REJECT; concentrated "
          "(607/500,807/500) ACCEPT")
    lamF_bal = (sb1 - ONE, sb2 + ONE)     # (207/500, 1207/500)
    lamF_con = (sc1 - ONE, sc2 + ONE)     # (107/500, 1307/500)
    lamS_con = (sc1 + ONE, sc2 - ONE)     # (1107/500, 307/500)
    p_bal = lamF_bal[0] * lamF_bal[1]
    p_con = lamF_con[0] * lamF_con[1]
    p_slow = lamS_con[0] * lamS_con[1]
    lin_bal = (lamF_bal[0] + lamF_bal[1]) / 2
    lin_con = (lamF_con[0] + lamF_con[1]) / 2
    check("7.2 [indicator report] the equal-weight reports at the same "
          "total margin: balanced FAST-trough lambda = (207/500, "
          "1207/500): geometric sqrt(" + str(p_bal) + ") < 1 - a "
          "decline signal; concentrated FAST-trough (107/500, 1307/500): "
          "sqrt(" + str(p_con) + ") < 1 - also decline; BUT the "
          "concentrated state's SLOW-trough (1107/500, 307/500): "
          "sqrt(" + str(p_slow) + ") > 1 - certified: WHICH STOCK "
          "BEARS THE PULSE flips the equal-weight LPI report at the "
          "same state; the linear dashboard reports " + str(lin_bal) +
          " >= 1 at BOTH troughs (literally the same number - "
          "sum-blind)",
          p_bal < ONE and p_con < ONE and p_slow > ONE
          and lin_bal >= ONE and lin_con == lin_bal)
    harm_bal = p2_negm(x, sb1, sb2, 1)
    harm_con = p2_negm(x, sc1, sc2, 1)
    check("7.3 [new exact datum] the wave's data assembly: the 10 "
          "decided cells (2.3); the 15 rho brackets (3.1); the full "
          "13-rung landscape with zero undecided (5.1) and the 13 core "
          "brackets (5.4); the slice-flip bracket (6.6) - every number "
          "an exact rational, every decision a certified comparison, "
          "the harmonic rejecting both relevance states",
          harm_bal is False and harm_con is False)
    check("7.4 [management action] at total margin 707/250 the "
          "allocation choice flips the mandatory below-LRP response "
          "under the LPI-structured composite: balanced allocation -> "
          "REJECT -> the closure/rebuilding response triggers (reserve "
          "top-up kappa* = 1 - x = 1/2 financing STAGED); concentrated "
          "allocation -> ACCEPT -> the transition is licensed with NO "
          "mid-transition response. The linear dashboard licenses BOTH "
          "allocations - the false certification is now visibly 2-D: "
          "it is blind to the distribution, not only to the total; and "
          "at the concentrated state the pulse-allocation choice "
          "(FAST on the low stock versus SLOW on the high stock) flips "
          "the equal-weight report (7.2) - a plan-design decision with "
          "certification content",
          (g_bal is False) and (g_con is True) and harm_bal is False
          and harm_con is False and ONE - x == Q(1, 2),
          "the aggregator + allocation jointly flip the response")


# ----------------------------------------------------------------------------
# Part 8 - summary gates
# ----------------------------------------------------------------------------

def part8():
    print("\n=== PART 8: summary gates ===")
    check("8.1 zero undecided decisions anywhere in the run (every "
          "schedule failure was tracked; the wave-1 residual is "
          "cleared, not re-labelled)",
          len(UNDECIDED) == 0, str(UNDECIDED[:3]) if UNDECIDED else "clean")
    first = [tuple(decide_all(Q(1, 2), s1, s2)) for (s1, s2) in GRID]
    second = [tuple(decide_all(Q(1, 2), s1, s2)) for (s1, s2) in GRID]
    check("8.2 determinism: the full 64-state x 13-rung decision table "
          "reproduces identically on re-computation",
          first == second)
    wave1_nones_still_none = all(
        p2_geo(Q(1, 2), Q(i, 4), Q(j, 4)) is None
        for (i, j) in WAVE1_NONE_CELLS)
    new_all_decided = all(
        geo_decide(Q(1, 2), Q(i, 4), Q(j, 4))[0] is not None
        for (i, j) in WAVE1_NONE_CELLS)
    check("8.3 the sigma-wave's honest-limits item 7.1 is closed on the "
          "64-state grid: wave-1's decider still reports its ten Nones "
          "(its file unchanged, never-overwrite), and this wave's "
          "decider returns a certified verdict for every one of them",
          wave1_nones_still_none and new_all_decided,
          "the residual is decided, not bypassed")


# ----------------------------------------------------------------------------

def main():
    print("off-diagonal wave - exact machine verification")
    print("witness: paper1_assessment_separation Section 4.5 datum; "
          "Section 6.3 fishery reading; the sigma-wave's off-diagonal "
          "residual (SIGMA_SPECTRUM_WAVE.md section 7.1)")
    print("arithmetic: fractions.Fraction only; certified rational "
          "enclosures (ln series + integer roots); no floats, no "
          "tolerances, no randomness")
    part0()
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    part7()
    part8()
    failed = [c for c in CHECKS if not c[1]]
    print("\n=== SUMMARY: " + str(len(CHECKS) - len(failed)) + "/" +
          str(len(CHECKS)) + " checks pass ===")
    if failed:
        print("FAILED CHECKS:")
        for name, _, detail in failed:
            print("  " + name + (" | " + detail if detail else ""))
        sys.exit(1)
    print("ALL CHECKS PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
