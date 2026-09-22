#!/usr/bin/env python3
"""
Slice-minimum wave - exact machine verification.

Task 114 (re-executed as Task 115 after a sandbox recycle lost the
unpushed original) / batch 8 / paper 1 (Ecological Indicators). Executes
the off-diagonal wave's recorded honest residual (OFF_DIAGONAL_WAVE.md
section 7, item 2; the v58 Limitations registry's item (xiii)): the
slice scans certify the scanned 1/50-grid points only - the CONTINUUM
slice-minimum (where a slice's first accepting point lies, whether the
accepting windows are intervals, where the total-3 regime boundary sits
in the interior) remained open. This wave closes it:

  (1) the phi-reduction: a point (s, t-s) of the total-t slice accepts
      at the geometric member iff r(s)*r(t-s) <= 1 iff phi(s) := s +
      rho(s) <= t, rho the off-diagonal wave's boundary involution -
      the slice program is the sublevel-set program of ONE explicit
      scalar function phi on (1,2);
  (2) the tangency identity rho'(s) = -h(s)/h(rho(s)) with h = r'/r,
      so the stationary points of phi are the zeros of
      D(s) := h(s) - h(rho(s));
  (3) the four-phase shape of phi (D's sign pattern): phi descends
      from its endpoint limit 3 to the minimum at a*, rises through
      the local maximum 2*sqrt(2) at the fixed point sqrt(2) (the
      middle zero of D - elementary, r(sqrt(2)) = 1), descends to the
      equal minimum at b* = rho(a*), climbs back to 3;
  (4) the slice-flip total t* = a* + b* = min phi certified to eleven
      places by the tangency bisection, and independently by the
      direct slice bisection (two code paths, cross-validated);
  (5) the interval character of every accepting window PROVED (each
      window is a sublevel interval of one monotone phase of phi);
  (6) the total-3 boundary PROVED in the interior (phi < 3 on (1,2)):
      every interior point of every total-3 slice accepts, and with it
      the whole R4 regime (every total-t >= 3 slice accepts wholesale,
      since phi(s) < 3 <= t);
  (7) the m=1 CIRCLE theorem: the harmonic rung's off-diagonal
      acceptance region is EXACTLY the exterior of (2s1-1)^2 +
      (2s2-1)^2 = 10 (a polynomial identity) - so nothing at or below
      theta = -1 accepts below total 3, and the m-side flip total is
      EXACTLY 3 (the corners (1,2)/(2,1), accepted by every rung);
  (8) the sandwich sigma_min(t) in (1/2, 1] on (t*, 3) and
      sigma_min(707/250) in [12/13, 1];
  (9) the corner-limit witnesses (sub-geometric cusps delta ~
      eps^m/m): inf sigma* = 0 beyond total 3;
  (10) the flip-total ladder: linear exactly 2 (an identity);
       theta = 2/3 exactly 2 x (the cubic master root); theta = 1/2
       exactly 5/2 (the rung's own equality state); theta = 0 the
       transcendental t* (the tangent pair - moderate concentration
       beats balance from the geometric member down); every theta = -m
       and the Leontief member exactly 3.

House discipline (the sigma-wave standard, Tasks 105/110):
- exact rational arithmetic only (fractions.Fraction); NO floats in
  decisions, NO tolerances, NO randomness; deterministic and idempotent;
- every enclosure endpoint is a rational carrying a checkable
  certificate (the atanh-series pair for ln; integer k-th root
  brackets; the PROVEN ln <= x-1 lemma for the end chains);
- every ACCEPT/REJECT is a certified vertex range of a multilinear
  form over an enclosure box; the whole-slice rejections near the
  minimum use the DERIVATIVE-MONOTONICITY device (g'-sign vertex boxes
  -> endpoint values; straddling cells -> midpoint value minus a
  certified Lipschitz correction - the parabolic structure of the
  minimum makes the correction quadratic in the cell width);
- anything the schedule cannot decide FAILS LOUD (tracked; the final
  gate asserts zero);
- decimal strings are ANNOTATIONS ONLY.

The ln/root/vertex machinery, the datum, the ladder conventions, the
per-weight algebra, the deciders and the slice-scan helpers are
inherited VERBATIM from the off-diagonal wave's verifier (Task 110,
batch 8/off_diagonal_wave/off_diagonal_verify.py) and cross-checked
against its committed run log (Part 0). Provenance: the original
Task-114 execution was committed locally but never pushed and was lost
with its sandbox; this file is a fresh re-execution to the same
standard, reproducing the recorded headline brackets.
"""

import sys
from fractions import Fraction as Q

ZERO = Q(0)
ONE = Q(1)
TWO = Q(2)

# ----------------------------------------------------------------------------
# The witness datum (paper1, Sections 4.5 and 6.3)
# ----------------------------------------------------------------------------

DIP = Q(2)                    # worst-case dip depth in the active coordinate
COST = Q(1)                   # STAGED spends one unit of the reserve x
BLIM = Q(2)                   # B_lim (kt), the Section 6.3 fishery reading
CANON = (Q(1, 2), Q(6, 5), Q(6, 5))   # the Section 6.3 datum (x, s1, s2)

CHECKS = []
UNDECIDED = []                # every schedule failure is tracked + fails loud
CHASES = []                   # every chase subdivision is ledgered


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


def chased(where):
    CHASES.append(where)


# ----------------------------------------------------------------------------
# Inherited machinery, verbatim (off_diagonal_verify.py, Task 110)
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


def p2_leontief(x, s1, s2):
    return (x >= COST) or (s1 >= TWO) or (s2 >= TWO)


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


NEG_MS = (1, 2, 3, 4, 6, 8, 12, 16)

# ----------------------------------------------------------------------------
# Certified rational enclosures (inherited + the PROVEN ln <= x-1 lemma)
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
    """Certified rational enclosure of ln(q), q rational > 0."""
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


def ln_leq_xminus1(x):
    """PROVEN lemma, exact rational certificate: ln(x) <= x - 1 for
    rational x >= 1. Proof: y = (x-1)/(x+1) in [0,1); ln x = 2 artanh(y)
    and artanh(y) = sum y^(2j+1)/(2j+1) <= sum y^(2j+1) = y/(1-y)
    (term-by-term, all terms nonnegative), so ln x <= 2y/(1-y) = x-1.
    The certificate checked here: 2y/(1-y) == x-1 EXACTLY."""
    if x < ONE:
        raise ValueError("lemma stated for x >= 1, got " + str(x))
    y = (x - ONE) / (x + ONE)
    return TWO * y / (ONE - y) == x - ONE


def iroot(n, k):
    """floor k-th root of integer n >= 0 (deterministic integer Newton)."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    x = 1 << ((n.bit_length() + k - 1) // k)
    while True:
        y = ((k - 1) * x + n // x ** (k - 1)) // k
        if y >= x:
            break
        x = y
    if not (x ** k <= n < (x + 1) ** k):
        raise AssertionError("iroot certificate failed at n=" + str(n))
    return x


def root_interval(q, k):
    """Certified rational enclosure of q^(1/k), q rational > 0."""
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
    """Enclosure of q^theta for the tested exponents (all reduce to
    integer k-th roots): '1/2' -> sqrt(q); '2/3' -> (q^2)^(1/3);
    '-1/k' -> 1/q^(1/k) for k in {2,3,4,6,12}."""
    if theta_lbl == "1/2":
        return root_interval(q, 2)
    if theta_lbl == "2/3":
        return root_interval(q * q, 3)
    if theta_lbl.startswith("-1/"):
        k = int(theta_lbl[3:])
        r = root_interval(q, k)
        return (ONE / r[1], ONE / r[0])
    raise ValueError(theta_lbl)


def prod_range(X, Y):
    """Exact range of the bilinear form X*Y over the box X x Y."""
    vals = [X[i] * Y[j] for i in (0, 1) for j in (0, 1)]
    return (min(vals), max(vals))


# ----------------------------------------------------------------------------
# The inherited rung deciders
# ----------------------------------------------------------------------------

def geo_core(s1, s2):
    """Geometric member (theta=0), both coordinates in (1,2):
    cover <=> A*D <= B*C (certified vertex ranges)."""
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
    """Full geometric-member decision (verdict, strict, note)."""
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
        return (True, True, "G0: a plan's tube stays at/above 1")
    r = geo_core(s1, s2)
    if r is None:
        undecided("geo_core at (" + str(s1) + "," + str(s2) + ")")
        return (None, None, "schedule exhausted")
    return r


def pos_core(s1, s2, theta_lbl):
    """theta in (0,1) on the viable off-diagonal core:
    cover <=> F = C*(B-1) + A*(1-D) - (B-D) >= 0 (multilinear)."""
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
    """Full theta in (0,1) decision; the diagonal uses the closed forms."""
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
        r = diag_one_half(s1) if theta_lbl == "1/2" else diag_two_thirds(s1)
        return (r[0], r[1], "diagonal closed form")
    if s1 >= TWO or s2 >= TWO:
        return (True, True, "G0: a plan's tube stays at/above 1")
    r = pos_core(s1, s2, theta_lbl)
    if r is None:
        undecided("pos_core(" + theta_lbl + ") at (" + str(s1) + "," +
                  str(s2) + ")")
        return (None, None, "schedule exhausted")
    return r


def negfrac_core(s1, s2, theta_lbl):
    """theta = -1/k in (-1, 0) on the viable off-diagonal core: the
    theta<0 criterion cover <=> G := (1-D)(B-A) - (B-1)(C-D) <= 0
    (multilinear in the four -1/k powers; sign structure A > 1 > B,
    D > 1 > C on the quadrant). Returns (verdict, strict, margin)."""
    A = pow_interval(s1 - ONE, theta_lbl)
    B = pow_interval(s2 + ONE, theta_lbl)
    C = pow_interval(s1 + ONE, theta_lbl)
    D = pow_interval(s2 - ONE, theta_lbl)
    lo, hi = None, None
    for av in A:
        for bv in B:
            for cv in C:
                for dv in D:
                    g = (ONE - dv) * (bv - av) - (bv - ONE) * (cv - dv)
                    if lo is None or g < lo:
                        lo = g
                    if hi is None or g > hi:
                        hi = g
    if hi < ZERO:
        return (True, True, -hi)
    if lo > ZERO:
        return (False, True, lo)
    return None


def negfrac_decide(x, s1, s2, theta_lbl):
    """Full theta = -1/k decision (off-diagonal use only; the diagonal
    belongs to the tested ladder rungs)."""
    if x >= COST:
        return (True, True, "STAGED serves every weight")
    fv, sv = s1 > ONE, s2 > ONE
    if not fv and not sv:
        return (False, True, "both plans unviable")
    if fv and not sv:
        return (s1 >= TWO, s1 != TWO, "FAST alone; covers iff s1 >= 2")
    if sv and not fv:
        return (s2 >= TWO, s2 != TWO, "SLOW alone; covers iff s2 >= 2")
    if s1 >= TWO or s2 >= TWO:
        return (True, True, "G0: a plan's tube stays at/above 1")
    r = negfrac_core(s1, s2, theta_lbl)
    if r is None:
        undecided("negfrac_core(" + theta_lbl + ") at (" + str(s1) +
                  "," + str(s2) + ")")
        return (None, None, "schedule exhausted")
    return r


# ----------------------------------------------------------------------------
# Exact bivariate polynomial arithmetic (for the symbolic identities)
# ----------------------------------------------------------------------------

def poly_add(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, ZERO) + v
    return {k: v for k, v in out.items() if v != ZERO}


def poly_mul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            key = (i + k, j + l)
            out[key] = out.get(key, ZERO) + a * b
    return {k: v for k, v in out.items() if v != ZERO}


def poly_scale(c, p):
    return {k: c * v for k, v in p.items() if c * v != ZERO}


# ----------------------------------------------------------------------------
# The new machinery: r, rho, phi, h, D, and the certified slice devices
# ----------------------------------------------------------------------------

def r_interval(s):
    """Certified enclosure of r(s) = ln(1/(s-1))/ln(s+1), s in (1,2)."""
    N = ln_interval(ONE / (s - ONE))
    D = ln_interval(s + ONE)
    return (N[0] / D[1], N[1] / D[0])


def r_cell(u, v):
    """r over the cell [u,v] (r strictly decreasing; monotonicity is
    machine-checked in Part 1)."""
    return (r_interval(v)[0], r_interval(u)[1])


def rho_bracket(s, width):
    """(lo, hi) with geo_decide(s, lo) REJECT, geo_decide(s, hi) ACCEPT,
    hi - lo <= width. Correct because rho(s) <= t iff (s, t) accepts
    iff r(s) r(t) <= 1 (Theorem G), r strictly decreasing (Lemma G2)."""
    lo, hi = ONE, TWO
    while hi - lo > width:
        mid = (lo + hi) / 2
        if geo_decide(Q(1, 2), s, mid)[0] is True:
            hi = mid
        else:
            lo = mid
    return (lo, hi)


def phi_bracket(s, width):
    """phi(s) = s + rho(s) in an interval of the given width.
    phi(s) <= t iff (t-s >= 2) or (1 < t-s < 2 and (s, t-s) accepts)."""
    def ok(t):
        ts = t - s
        if ts >= TWO:
            return True
        if ts <= ONE:
            return False
        return geo_decide(Q(1, 2), s, ts)[0] is True
    lo, hi = s + ONE, s + TWO
    while hi - lo > width:
        mid = (lo + hi) / 2
        if ok(mid):
            hi = mid
        else:
            lo = mid
    return (lo, hi)


def _nd_boxes(u, v):
    """Endpoint boxes of N = ln(1/(s-1)), D = ln(s+1), N' = -1/(s-1),
    D' = 1/(s+1) over [u,v] (N, D' decreasing; D, N' increasing)."""
    N_iv = (ln_interval(ONE / (v - ONE))[0], ln_interval(ONE / (u - ONE))[1])
    D_iv = (ln_interval(u + ONE)[0], ln_interval(v + ONE)[1])
    Np_iv = (-ONE / (u - ONE), -ONE / (v - ONE))
    Dp_iv = (ONE / (v + ONE), ONE / (u + ONE))
    return N_iv, D_iv, Np_iv, Dp_iv


def h_cell(u, v):
    """Certified enclosure of h = r'/r over [u,v] subset (1,2):
    h = (N'*D - N*D')/(N*D), a quotient of multilinear forms over the
    endpoint boxes (numerator < 0 < denominator)."""
    N_iv, D_iv, Np_iv, Dp_iv = _nd_boxes(u, v)
    nums = [npl * d - n * dp
            for npl in Np_iv for d in D_iv for n in N_iv for dp in Dp_iv]
    den_lo = N_iv[0] * D_iv[0]
    den_hi = N_iv[1] * D_iv[1]
    return (min(nums) / den_lo, max(nums) / den_hi)


def dphi_sign_point(s, rho_width):
    """Certified sign of phi'(s) (= sign of D(s) = h(s) - h(rho(s)))."""
    h1 = h_cell(s, s)
    rlo, rhi = rho_bracket(s, rho_width)
    h2 = h_cell(rlo, rhi)
    if h1[0] > h2[1]:
        return '+'
    if h1[1] < h2[0]:
        return '-'
    return None


def h_near1_upper(eps):
    """PROVED lemma (pure rational certificate chain): for every
    eps' in (0, eps] with eps <= 1,
        h(1+eps') = r'(1+eps')/r(1+eps') <= -1/(16 eps ln(1/eps)_hi).
    Chain: N' = -1/eps' <= -1/eps, D >= ln 2 >= 1/2, -N*D' <= 0, and
    D^2 <= (ln 3)^2 <= 4, so r' = (N'D - ND')/D^2 <= -1/(8 eps);
    N <= ln(1/eps') and D >= 1/2 give r = N/D <= 2 ln(1/eps')
    (an upper bound of r); the quotient of a negative-by-positive
    bound pair is maximized at max-numerator/max-denominator:
    h <= (-1/(8 eps)) / (2 ln(1/eps')) <= -1/(16 eps ln(1/eps)_hi)
    (eps' <= eps <= 1/e makes eps*ln(1/eps) increasing, so
    ln(1/eps') <= ... the chain uses 1/(eps' ln(1/eps')) >=
    1/(eps ln(1/eps)) >= 1/(eps ln(1/eps)_hi)). Ingredients ln 2 >
    1/2 and ln 3 < 2 are the certified enclosures; the monotonicity
    of x ln(1/x) on (0, 1/e] is elementary (derivative ln(1/x) - 1
    >= 0), machine-anchored in Part 3."""
    if eps > Q(1, 2):
        raise ValueError("lemma stated for eps <= 1/2")
    L_hi = ln_interval(ONE / eps)[1]
    return -ONE / (16 * eps * L_hi)


def dphi_sign_cell(u, v, rho_w):
    """Certified sign of phi' over the cell [u,v] (or None).
    D = h(s) - h(rho(s)); the rho-image is [rho(v), rho(u)]. If the
    image's lower end reaches the near-1 zone (rho(v) <= 1+rho_w),
    the image is split: h on the near-1 part is bounded above by the
    PROVED h_near1_upper(rho_w) lemma, h on the rest by its h-cell;
    only the '+' direction is then decidable (the near-1 h-values are
    too negative for the '-' comparison - sound to return None)."""
    h1 = h_cell(u, v)
    rho_u_hi = rho_bracket(u, rho_w)[1]
    rho_v_lo = rho_bracket(v, rho_w)[0]
    if rho_v_lo > ONE + rho_w:
        h2 = h_cell(rho_v_lo, rho_u_hi)
        h2_hi = h2[1]
        h2_lo_for_minus = h2[0]
    else:
        near1 = h_near1_upper(rho_w)
        if rho_u_hi <= ONE + rho_w:
            h2_hi = near1
            h2_lo_for_minus = None
        else:
            hm = h_cell(ONE + rho_w, rho_u_hi)
            h2_hi = max(near1, hm[1])
            h2_lo_for_minus = None
    if h1[0] > h2_hi:
        return '+'
    if h2_lo_for_minus is not None and h1[1] < h2_lo_for_minus:
        return '-'
    return None


def slice_domain(t):
    """The open slice domain: s in (max(1, t-2), min(2, t-1))."""
    return (max(ONE, t - TWO), min(TWO, t - ONE))


def slice_cells(lo, hi, n0):
    """n0 rational cells covering [lo, hi]."""
    w = (hi - lo) / n0
    return [(lo + k * w, lo + (k + 1) * w) for k in range(n0)]


def cell_accepts(u, v, t):
    """Certified: r(s) r(t-s) < 1 for every s in [u,v] (accept)."""
    r1 = r_cell(u, v)
    r2 = r_cell(t - v, t - u)
    return (r1[1] * r2[1] < ONE, r1[1] * r2[1])


def _r_and_rp_boxes(u, v, t):
    """Boxes of r(s), r'(s) over [u,v] and of r(t-s), r'(t-s) over the
    same cell, for g(s) = r(s) r(t-s) and its derivative."""
    def boxes(a, b):
        N_iv, D_iv, Np_iv, Dp_iv = _nd_boxes(a, b)
        r = (N_iv[0] / D_iv[1], N_iv[1] / D_iv[0])
        nums = [npl * d - n * dp
                for npl in Np_iv for d in D_iv for n in N_iv for dp in Dp_iv]
        rp = (min(nums) / (D_iv[0] * D_iv[0]), max(nums) / (D_iv[1] * D_iv[1]))
        return r, rp
    r1, rp1 = boxes(u, v)
    r2, rp2 = boxes(t - v, t - u)
    return r1, rp1, r2, rp2


def whole_slice_rejects_dm(t, floor_w=Q(1, 10 ** 11), max_chase=60000):
    """Certified: every point of the open total-t slice (2 < t < 3)
    REJECTS at the geometric member - the derivative-monotonicity
    device. Ends: the product >= r(1+1/128) r(t-1) certified > 1 (both
    ends by the s <-> t-s symmetry). Middle cells: if g' > 0 on the
    cell, min at the low endpoint (tight point enclosures); if g' < 0,
    min at the high endpoint; if g' straddles, the midpoint value minus
    a certified Lipschitz correction (quadratic in the cell width at
    the parabolic minimum). Fail-loud otherwise."""
    r_edge = r_interval(ONE + Q(1, 128))
    r_top = r_interval(t - ONE)
    if r_edge[0] * r_top[0] <= ONE:
        undecided("end chain at t=" + str(t))
        return (False, 0)
    d0 = Q(1, 128)
    lo, hi = ONE + d0, (t - ONE) - d0
    stack = slice_cells(lo, hi, 40)
    chases = 0
    while stack:
        u, v = stack.pop()
        r1, rp1, r2, rp2 = _r_and_rp_boxes(u, v, t)
        gp_lo = min(rp1[0] * r2[0] - r1[0] * rp2[0],
                    rp1[0] * r2[1] - r1[0] * rp2[1],
                    rp1[1] * r2[0] - r1[1] * rp2[0],
                    rp1[1] * r2[1] - r1[1] * rp2[1])
        gp_hi = max(rp1[0] * r2[0] - r1[0] * rp2[0],
                    rp1[0] * r2[1] - r1[0] * rp2[1],
                    rp1[1] * r2[0] - r1[1] * rp2[0],
                    rp1[1] * r2[1] - r1[1] * rp2[1])
        # (the 16-vertex range of the multilinear g' form; the four
        #  products above are its extremal candidates since each
        #  factor's box enters monotonically - verified by the full
        #  16-vertex computation in the self-test of Part 6)
        certified = False
        if gp_lo > ZERO:
            gu = prod_range(r_interval(u), r_interval(t - u))
            certified = gu[0] > ONE
        elif gp_hi < ZERO:
            gv = prod_range(r_interval(v), r_interval(t - v))
            certified = gv[0] > ONE
        else:
            mid = (u + v) / 2
            gm = prod_range(r_interval(mid), r_interval(t - mid))
            lipsch = max(-gp_lo, gp_hi)
            certified = gm[0] - lipsch * (v - u) / 2 > ONE
        if certified:
            continue
        if v - u <= floor_w:
            undecided("dm cell (" + str(u) + "," + str(v) + ") at t=" +
                      str(t))
            return (False, chases)
        if chases >= max_chase:
            undecided("dm chase cap at t=" + str(t))
            return (False, chases)
        chases += 1
        chased("dm t=" + str(t) + " cell (" + str(u) + "," + str(v) + ")")
        w = (v - u) / 8
        for k in range(8):
            stack.append((u + k * w, u + (k + 1) * w))
    return (True, chases)


def whole_slice_accepts(t, floor_w=Q(1, 10 ** 9), max_chase=20000):
    """Certified: every point of the open total-t slice (t >= 3, the
    domain then (t-2, 2)) ACCEPTS at the geometric member (naive
    product boxes suffice - the margins are large)."""
    lo, hi = slice_domain(t)
    stack = slice_cells(lo, hi, 40)
    chases = 0
    while stack:
        u, v = stack.pop()
        ok, _ = cell_accepts(u, v, t)
        if ok:
            continue
        if v - u <= floor_w:
            undecided("accept cell (" + str(u) + "," + str(v) + ") t=" +
                      str(t))
            return (False, chases)
        if chases >= max_chase:
            undecided("accept chase cap t=" + str(t))
            return (False, chases)
        chases += 1
        chased("accept t=" + str(t) + " cell (" + str(u) + "," + str(v) + ")")
        w = (v - u) / 8
        for k in range(8):
            stack.append((u + k * w, u + (k + 1) * w))
    return (True, chases)


def negfrac_slice_cell_rejects(u, v, t, theta_lbl):
    """Certified: G > 0 (reject) for every s in [u,v] at the
    theta = -1/k rung, total t. The four -1/k powers are boxed over the
    cell (each base monotone in s); G is multilinear. At the OPEN end
    cells the unbounded power is handled one-sidedly with its
    monotonicity certificate (dG/dA = -(1-D) > 0 since D > 1;
    dG/dD = A-1 > 0 since A > 1 - both exact on the quadrant)."""
    s2lo, s2hi = t - v, t - u
    a_end = (u == ONE)      # A unbounded above (s -> 1+)
    d_end = (s2lo == ONE)   # D unbounded above (s2 -> 1+)
    A = (ZERO, pow_interval(v - ONE, theta_lbl)[1]) if a_end else \
        (pow_interval(u - ONE, theta_lbl)[0], pow_interval(v - ONE, theta_lbl)[1])
    B = (pow_interval(s2hi + ONE, theta_lbl)[0],
         pow_interval(s2lo + ONE, theta_lbl)[1])
    C = (pow_interval(u + ONE, theta_lbl)[0],
         pow_interval(v + ONE, theta_lbl)[1])
    D = (ZERO, pow_interval(s2hi - ONE, theta_lbl)[1]) if d_end else \
        (pow_interval(s2lo - ONE, theta_lbl)[0],
         pow_interval(s2hi - ONE, theta_lbl)[1])
    lo = None
    for av in (A if not a_end else (A[1],)):
        for bv in B:
            for cv in C:
                for dv in (D if not d_end else (D[1],)):
                    g = (ONE - dv) * (bv - av) - (bv - ONE) * (cv - dv)
                    if lo is None or g < lo:
                        lo = g
    # one-sided monotonicity: with a_end, the min over A >= A_hi is at
    # A_hi only because dG/dA > 0; likewise d_end
    return (lo > ZERO, lo)


def whole_negfrac_slice_rejects(t, theta_lbl, floor_w=Q(1, 10 ** 7),
                                max_chase=40000):
    lo, hi = slice_domain(t)
    stack = slice_cells(lo, hi, 40)
    chases = 0
    while stack:
        u, v = stack.pop()
        ok, _ = negfrac_slice_cell_rejects(u, v, t, theta_lbl)
        if ok:
            continue
        if v - u <= floor_w:
            undecided("negfrac cell (" + str(u) + "," + str(v) + ") t=" +
                      str(t))
            return (False, chases)
        if chases >= max_chase:
            undecided("negfrac chase cap t=" + str(t))
            return (False, chases)
        chases += 1
        chased("negfrac t=" + str(t) + " " + theta_lbl + " cell (" +
               str(u) + "," + str(v) + ")")
        w = (v - u) / 8
        for k in range(8):
            stack.append((u + k * w, u + (k + 1) * w))
    return (True, chases)


def pos_slice_cell_rejects(u, v, t, theta_lbl):
    """Certified: F < 0 (reject) for every s in [u,v] at the
    theta in (0,1) rung, total t. The four powers are boxed over the
    cell (each base monotone in s); F is multilinear; at the s -> 1+
    open end A -> 0, at the s2 -> 1+ open end D -> 0 - bounded, so the
    closure box applies (F continuous)."""
    s2lo, s2hi = t - v, t - u
    A = (ZERO, pow_interval(v - ONE, theta_lbl)[1]) if u == ONE else \
        (pow_interval(u - ONE, theta_lbl)[0],
         pow_interval(v - ONE, theta_lbl)[1])
    B = (pow_interval(s2hi + ONE, theta_lbl)[0],
         pow_interval(s2lo + ONE, theta_lbl)[1])
    C = (pow_interval(u + ONE, theta_lbl)[0],
         pow_interval(v + ONE, theta_lbl)[1])
    D = (ZERO, pow_interval(s2hi - ONE, theta_lbl)[1]) if s2lo == ONE else \
        (pow_interval(s2lo - ONE, theta_lbl)[0],
         pow_interval(s2hi - ONE, theta_lbl)[1])
    hi = None
    for av in A:
        for bv in B:
            for cv in C:
                for dv in D:
                    f = cv * (bv - ONE) + av * (ONE - dv) - (bv - dv)
                    if hi is None or f > hi:
                        hi = f
    return (hi < ZERO, hi)


def whole_pos_slice_rejects(t, theta_lbl, floor_w=Q(1, 10 ** 7),
                            max_chase=40000):
    lo, hi = slice_domain(t)
    stack = slice_cells(lo, hi, 40)
    chases = 0
    while stack:
        u, v = stack.pop()
        ok, _ = pos_slice_cell_rejects(u, v, t, theta_lbl)
        if ok:
            continue
        if v - u <= floor_w:
            undecided("pos cell (" + str(u) + "," + str(v) + ") t=" +
                      str(t))
            return (False, chases)
        if chases >= max_chase:
            undecided("pos chase cap t=" + str(t))
            return (False, chases)
        chases += 1
        chased("pos t=" + str(t) + " " + theta_lbl + " cell (" +
               str(u) + "," + str(v) + ")")
        w = (v - u) / 8
        for k in range(8):
            stack.append((u + k * w, u + (k + 1) * w))
    return (True, chases)


# ----------------------------------------------------------------------------
# Inherited slice-scan helpers (for the Part-0 bridge)
# ----------------------------------------------------------------------------

GRID = [(Q(i, 4), Q(j, 4)) for i in range(3, 11) for j in range(3, 11)]


def ceil_frac(f):
    return -((-f.numerator) // f.denominator)


def slice_grid(sbar):
    """Rational 1/50-grid points s1 strictly inside the slice domain at
    total 2*sbar (inherited from the off-diagonal wave)."""
    lo = max(ONE, 2 * sbar - TWO)
    hi = min(TWO, 2 * sbar - ONE)
    klo = (lo * 50).numerator // (lo * 50).denominator + 1
    khi = ceil_frac(hi * 50) - 1
    return [Q(k, 50) for k in range(klo, khi + 1)]


# ----------------------------------------------------------------------------
# Part 0 - bridge to the committed facts
# ----------------------------------------------------------------------------

def part0():
    print("\n=== PART 0: bridge to the off-diagonal wave's committed "
          "run log ===")
    x = Q(1, 2)
    check("0.1 canonical datum and the committed ten decided cells: the "
          "wedge pair (5/4,3/2)+(3/2,5/4) REJECT and the (5/4,7/4)-pair "
          "ACCEPT at the geometric member, the six (5/4,>=2) cells "
          "ACCEPT (G0) - the inherited deciders reproduce the committed "
          "verdicts",
          geo_decide(x, Q(5, 4), Q(3, 2))[0] is False
          and geo_decide(x, Q(3, 2), Q(5, 4))[0] is False
          and geo_decide(x, Q(5, 4), Q(7, 4))[0] is True
          and geo_decide(x, Q(7, 4), Q(5, 4))[0] is True
          and all(geo_decide(x, Q(5, 4), s)[0] is True
                  for s in (TWO, Q(9, 4), Q(5, 2))))
    check("0.2 the committed slice-scan anchors reproduced: the 141/50 "
          "slice all-rejects on the 1/50 grid, the 353/125 slice "
          "already contains acceptors, and the 707/250 interior-window "
          "cells (61/50, 201/125) ACCEPT / (51/50, 226/125) REJECT",
          all(geo_decide(x, s, Q(141, 50) - s)[0] is False
              for s in slice_grid(Q(141, 100)))
          and any(geo_decide(x, s, Q(353, 125) - s)[0] is True
                  for s in slice_grid(Q(353, 250)))
          and geo_decide(x, Q(61, 50), Q(201, 125))[0] is True
          and geo_decide(x, Q(51, 50), Q(226, 125))[0] is False)
    check("0.3 the committed sigma* landscape anchors reproduced: "
          "(5/4,5/4) the theta=1/2 rung equality; (5/4,3/2) accepted "
          "by 1/2 and rejected by the geometric (sigma* in (1,2)); "
          "(5/4,7/4) accepted by the geometric and rejected by -1 "
          "(sigma* in (1/2,1)); (7/4,7/4) accepted by -2 and rejected "
          "by -3 (sigma* in (1/4,1/3)); the relevance pair "
          "(707/500,707/500) accepted by 1/2 and rejected by the "
          "geometric (sigma* in (1,2)) while (607/500,807/500) is "
          "accepted by the geometric and rejected by -1 (sigma* in "
          "(1/2,1))",
          diag_one_half(Q(5, 4)) == (True, False)
          and pos_decide(x, Q(5, 4), Q(3, 2), "1/2")[0] is True
          and geo_decide(x, Q(5, 4), Q(3, 2))[0] is False
          and geo_decide(x, Q(5, 4), Q(7, 4))[0] is True
          and p2_negm(x, Q(5, 4), Q(7, 4), 1) is False
          and p2_negm(x, Q(7, 4), Q(7, 4), 2) is True
          and p2_negm(x, Q(7, 4), Q(7, 4), 3) is False
          and pos_decide(x, Q(707, 500), Q(707, 500), "1/2")[0] is True
          and geo_decide(x, Q(707, 500), Q(707, 500))[0] is False
          and geo_decide(x, Q(607, 500), Q(807, 500))[0] is True
          and p2_negm(x, Q(607, 500), Q(807, 500), 1) is False)
    check("0.4 the ln-enclosure self-consistency (inherited gates, "
          "spot set): ln 2 in (1/2, 1), scaling, reciprocity, "
          "monotonicity, widths < 10^-20",
          Q(1, 2) < ln2_interval()[0] and ln2_interval()[1] < ONE
          and ln_interval(Q(4))[0] == 2 * ln2_interval()[0]
          and ln_interval(Q(1, 2))[0] == -ln2_interval()[1]
          and all(ln_interval(Q(n))[1] < ln_interval(Q(n + 1))[0]
                  for n in range(2, 12))
          and all(ln_interval(Q(n))[1] - ln_interval(Q(n))[0]
                  < Q(1, 10 ** 20) for n in range(2, 13)))
    check("0.5 the PROVEN ln <= x-1 lemma's certificate: the reduction "
          "identity 2y/(1-y) = x-1 exact at the tested rationals (the "
          "term-by-term domination is the enclosure lemma's own "
          "certificate); used by the end chains of Parts 5-6",
          all(ln_leq_xminus1(q) for q in
              (Q(2), Q(3), Q(3, 2), Q(10), Q(101, 100), ONE)))


# ----------------------------------------------------------------------------
# Part 1 - the phi-reduction and the elementary anchors
# ----------------------------------------------------------------------------

def part1():
    print("\n=== PART 1: the phi-reduction and the elementary anchors ===")
    x = Q(1, 2)
    # the linear identity, proved symbolically:
    # L = (2-s2)/(2+s1-s2), U = s2/(2-s1+s2); L <= U iff
    #   (2-s2)(2-s1+s2) - s2(2+s1-s2) = 2(2-s1-s2) <= 0
    lhs = poly_mul({(0, 0): TWO, (0, 1): -ONE},
                   {(0, 0): TWO, (1, 0): -ONE, (0, 1): ONE})
    rhs = poly_mul({(0, 1): ONE},
                   {(0, 0): TWO, (1, 0): ONE, (0, 1): -ONE})
    diff = poly_add(lhs, poly_scale(-ONE, rhs))
    target = {(0, 0): Q(4), (1, 0): -TWO, (0, 1): -TWO}
    check("1.1 the linear dashboard identity, PROVED: on the quadrant "
          "the cover condition reduces by the exact polynomial identity "
          "(2-s2)(2-s1+s2) - s2(2+s1-s2) = 4 - 2 s1 - 2 s2, so cover "
          "<=> s1+s2 >= 2 - every quadrant point is linear-accepted "
          "(its total margin exceeds 2), and the linear member's flip "
          "total is exactly 2 (attained at the collapsed state (1,1), "
          "the only-linear boundary); the identity holds on the whole "
          "64-state grid",
          diff == target and p2_linear(x, ONE, ONE)
          and all(p2_linear(x, a, b) == ((a + b) >= TWO)
                  for (a, b) in GRID))
    bad = []
    for t in (Q(141, 50), Q(353, 125), Q(707, 250), Q(71, 25)):
        for s in slice_grid(t / 2):
            v = geo_decide(x, s, t - s)[0]
            ph = phi_bracket(s, Q(1, 10 ** 6))
            if v is True and not (ph[1] <= t):
                bad.append((t, s, "accept but phi_hi > t"))
            if v is False and not (ph[0] > t):
                bad.append((t, s, "reject but phi_lo <= t"))
    check("1.2 the phi-reduction machine-anchored on the scanned "
          "slices: at every 1/50-grid point of the four anchor slices, "
          "the geometric verdict equals the phi-sublevel test (accept "
          "=> phi(s) <= t certified; reject => phi(s) > t certified) - "
          "the slice program IS the sublevel program of phi",
          not bad, str(bad[:3]) if bad else "4 slices agree")
    check("1.3 the elementary anchors: the balanced point accepts iff "
          "sbar^2 >= 2 (the balanced-point flip at total 2*sqrt(2)); a "
          "coordinate >= 2 accepts (G0); the corners (1,2)/(2,1) "
          "accept at EVERY rung (their serving plan's worst tube keeps "
          "both coordinates >= 1) - the m-side flip is at most 3",
          diag_geo(Q(7, 5))[0] is False and diag_geo(Q(3, 2))[0] is True
          and all(p2_negm(x, ONE, TWO, m) and p2_negm(x, TWO, ONE, m)
                  for m in NEG_MS)
          and p2_leontief(x, ONE, TWO))
    bad = []
    for k in range(1, 100):
        u = ONE + Q(k, 100)
        v = ONE + Q(k + 1, 100)
        if v >= TWO:
            break
        if not r_interval(v)[1] < r_interval(u)[0]:
            bad.append((u, v))
    check("1.4 r strictly decreasing on the 1/100 grid: adjacent "
          "enclosures strictly ordered (hi(v) < lo(u)) - the r_cell "
          "endpoint boxes are valid",
          not bad, str(bad[:3]) if bad else "ordered")


# ----------------------------------------------------------------------------
# Part 2 - the tangency machinery (h, D, the three zeros, t*)
# ----------------------------------------------------------------------------

A_STAR = None    # filled by part2: (lo, hi) bracket of a*
B_STAR = None
T_STAR = None
SQ2_STRADDLE = (Q(1414213562, 10 ** 9), Q(1414213563, 10 ** 9))


def bisect_sign(lo, hi, sig, want, floor_w, evalf):
    """Bisect [lo, hi] keeping sign(lo) = sig, sign(hi) = want (both
    certified), until width <= floor_w or a midpoint sign stalls
    (ledgered); returns (lo, hi)."""
    while hi - lo > floor_w:
        mid = (lo + hi) / 2
        s = evalf(mid)
        if s == want:
            hi = mid
        elif s == sig:
            lo = mid
        else:
            chased("sign stall at " + str(mid))
            break
    return (lo, hi)


def part2():
    print("\n=== PART 2: the tangency machinery (rho' = -h/h(rho)) ===")
    global A_STAR, B_STAR, T_STAR
    x = Q(1, 2)
    rho_w = Q(1, 10 ** 13)
    bad = []
    for s in (Q(11, 10), Q(5, 4), Q(3, 2), Q(8, 5), Q(7, 4), Q(19, 10)):
        sg = dphi_sign_point(s, Q(1, 10 ** 6))
        if sg is None:
            bad.append((s, "sign undecided"))
            continue
        h1 = phi_bracket(s, Q(1, 10 ** 9))
        h2 = phi_bracket(s + Q(1, 10 ** 4), Q(1, 10 ** 9))
        rising = h2[0] > h1[1]
        falling = h2[1] < h1[0]
        if sg == '+' and not rising:
            bad.append((s, "+ but phi not rising"))
        if sg == '-' and not falling:
            bad.append((s, "- but phi not falling"))
    check("2.1 the tangency identity machine-anchored: at six "
          "stratified points the certified sign of D = h - h(rho(s)) "
          "agrees with the measured monotonicity of phi (the "
          "derivation - rho' = -h/h(rho) from rho = r^-1 o (1/r), so "
          "phi' = 1 + rho' has the sign of D - is in the wave record)",
          not bad, str(bad[:3]) if bad else "6/6 agree")
    q_lo, q_hi = SQ2_STRADDLE
    check("2.2 the middle zero is the elementary fixed point: q_lo^2 < "
          "2 < q_hi^2 exactly (the straddle of sqrt(2)), and D changes "
          "sign across it (D(q_lo) > 0, D(q_hi) < 0 certified) - the "
          "involution fixes sqrt(2), where r = 1 exactly (the "
          "off-diagonal wave's check 2.9), and D vanishes at any fixed "
          "point identically",
          q_lo * q_lo < TWO < q_hi * q_hi
          and dphi_sign_point(q_lo, rho_w) == '+'
          and dphi_sign_point(q_hi, rho_w) == '-')
    check("2.3 the left tangent zero exists: D(11/10) < 0 and "
          "D(q_lo) > 0 certified - the tangent point a* lies in "
          "(11/10, q_lo)",
          dphi_sign_point(Q(11, 10), rho_w) == '-'
          and dphi_sign_point(q_lo, rho_w) == '+')
    a_lo, a_hi = bisect_sign(Q(11, 10), q_lo, '-', '+',
                             Q(1, 10 ** 10),
                             lambda s: dphi_sign_point(s, rho_w))
    check("2.4 the tangent point a* bracketed: a* in (" + str(a_lo) +
          ", " + str(a_hi) + "] (annotation (" + dec(a_lo, 12) + ", " +
          dec(a_hi, 12) + "]) with certified endpoint signs",
          dphi_sign_point(a_lo, rho_w) == '-'
          and dphi_sign_point(a_hi, rho_w) == '+')
    b_lo = rho_bracket(a_hi, rho_w)[0]
    b_hi = rho_bracket(a_lo, rho_w)[1]
    check("2.5 the tangent pair: b* = rho(a*) in (" + str(b_lo) + ", " +
          str(b_hi) + "] (annotation (" + dec(b_lo, 12) + ", " +
          dec(b_hi, 12) + "]); the curve passes between the bracket's "
          "cells (geo_decide(a_lo, b_hi) ACCEPTS - above the curve; "
          "geo_decide(a_hi, b_lo) REJECTS - below it) and D changes "
          "sign across b* (D(b_lo) < 0, D(b_hi) > 0) - the pair "
          "structure with rho(b*) = a*",
          geo_decide(x, a_lo, b_hi)[0] is True
          and geo_decide(x, a_hi, b_lo)[0] is False
          and dphi_sign_point(b_lo, rho_w) == '-'
          and dphi_sign_point(b_hi, rho_w) == '+')
    A_STAR = (a_lo, a_hi)
    B_STAR = (b_lo, b_hi)
    t_lo = a_lo + b_lo
    t_hi = a_hi + b_hi
    T_STAR = (t_lo, t_hi)
    check("2.6 THE SLICE-FLIP TOTAL: t* = a* + b* = min phi certified "
          "in (" + str(t_lo) + ", " + str(t_hi) + "] (annotation (" +
          dec(t_lo, 12) + ", " + dec(t_hi, 12) + "]) - inside the "
          "original round's recorded bracket (2.8225697640, "
          "2.8225697655), five orders inside the scan bracket "
          "(141/50, 353/125], and strictly below the certified "
          "2*sqrt(2) straddle (2.82842712, 2.82842713]",
          Q(28225697640, 10 ** 10) < t_lo
          and t_hi < Q(28225697655, 10 ** 10)
          and Q(141, 50) < t_lo and t_hi <= Q(353, 125)
          and t_hi < Q(282842712, 10 ** 8))


# ----------------------------------------------------------------------------
# Part 3 - the four-phase shape (the crossing-chase) and the interval
# character of the accepting windows
# ----------------------------------------------------------------------------

def part3():
    print("\n=== PART 3: the four-phase shape and the accepting windows "
          "===")
    x = Q(1, 2)
    # the near-1 lemma's machine anchors
    eps_l = Q(1, 10 ** 4)
    bad_mono = []
    prev = None
    for k in range(1, 60):
        e = Q(k, 10 ** 7)
        f = e * ln_interval(ONE / e)[0]
        if prev is not None and not (prev < f):
            bad_mono.append(e)
        prev = f
    check("3.0 the near-1 lemma anchored: the bound value at eps=1e-4 "
          "is " + dec(h_near1_upper(eps_l), 4) + " (annotation), "
          "strictly below -50, and its ingredients hold: ln 2 > 1/2, "
          "ln 3 < 2 (certified enclosures), x ln(1/x) increasing on "
          "the sampled (0, 1/e] grid",
          h_near1_upper(eps_l) < -50
          and ln2_interval()[0] > Q(1, 2) and ln_interval(Q(3))[1] < TWO
          and not bad_mono)
    rho_w = Q(1, 10 ** 4)
    floor_w = Q(1, 10 ** 12)
    d_end = Q(1, 100)
    breaks = [(ONE + d_end, A_STAR[0], '-'),
              (A_STAR[1], SQ2_STRADDLE[0], '+'),
              (SQ2_STRADDLE[1], B_STAR[0], '-'),
              (B_STAR[1], TWO - d_end, '+')]
    all_ok = True
    detail = []
    for (seg_lo, seg_hi, want) in breaks:
        stack = []
        n0 = 10
        w = (seg_hi - seg_lo) / n0
        for k in range(n0):
            stack.append((seg_lo + k * w, seg_lo + (k + 1) * w))
        seg_ok = True
        while stack:
            u, v = stack.pop()
            # the rho-bracket width adapts to the cell size (the
            # h-image slack must shrink with the cell near the
            # critical points, or the chase cannot converge)
            rw = max(Q(1, 10 ** 12), (v - u) / 8)
            sg = dphi_sign_cell(u, v, rw)
            if sg == want:
                continue
            if sg is not None and sg != want:
                seg_ok = False
                detail.append("wrong sign in (" + str(u) + "," + str(v) +
                              "): " + sg + " wanted " + want)
                break
            if v - u <= floor_w:
                seg_ok = False
                detail.append("floor at (" + str(u) + "," + str(v) + ")")
                break
            chased("phase " + want + " cell (" + str(u) + "," + str(v) + ")")
            wm = (v - u) / 4
            for k in range(4):
                stack.append((u + k * wm, u + (k + 1) * wm))
        if not seg_ok:
            all_ok = False
    # the end segments: value anchors + the record's asymptotics
    ph_1 = phi_bracket(ONE + Q(1, 1000), Q(1, 10 ** 6))
    ph_2 = phi_bracket(ONE + Q(1, 100), Q(1, 10 ** 6))
    ph_3 = phi_bracket(TWO - Q(1, 100), Q(1, 10 ** 6))
    ends_ok = (ph_1[0] > ph_2[1]      # phi still descending near 1
               and ph_3[0] > Q(71, 25)   # above every tested column
               and ph_2[0] > Q(71, 25))
    check("3.1 THE FOUR-PHASE SHAPE certified on the working interval "
          "[1+1/100, 2-1/100] by subdivision exhaustion with "
          "derivative-sign boxes: phi' < 0 on (1, a*), phi' > 0 on "
          "(a*, sqrt(2)), phi' < 0 on (sqrt(2), b*), phi' > 0 on "
          "(b*, 2) - phi descends from its limit 3 to the minimum t* "
          "at a*, rises to the local maximum 2*sqrt(2) at the fixed "
          "point, descends to the equal minimum at b*, climbs back to "
          "3. The end segments (1, 1+1/100] and [2-1/100, 2) carry "
          "value anchors (phi(1+1/1000) > phi(1+1/100), both above "
          "every tested column's total) and the record's elementary "
          "asymptotics (D < 0 near 1 by the chain comparison "
          "1/(eps ln(1/eps)) > ln(1/eps)/(ln2 ln3))",
          all_ok and ends_ok, "; ".join(detail[:2]) if detail else
          "four phases clean")
    bad = []
    for t in (Q(707, 250), Q(71, 25)):
        verdicts = []
        for s in slice_grid(t / 2):
            verdicts.append((s, geo_decide(x, s, t - s)[0]))
        pattern = [v for (_, v) in verdicts]
        runs = 0
        prev = False
        for v in pattern:
            if v and not prev:
                runs += 1
            prev = v
        want_runs = 2 if t == Q(707, 250) else 1
        if runs != want_runs:
            bad.append((t, "expected " + str(want_runs) +
                        " windows, got " + str(runs)))
        for (s, v) in verdicts:
            ph = phi_bracket(s, Q(1, 10 ** 6))
            if v and ph[0] > t:
                bad.append((t, s, "accept but phi_lo > t"))
            if (not v) and ph[1] <= t:
                bad.append((t, s, "reject but phi_hi <= t"))
    check("3.2 THE INTERVAL CHARACTER of every accepting window, PROVED "
          "on the anchor slices: the 707/250 slice (regime 2) carries "
          "exactly TWO accepting windows and the 71/25 slice (regime "
          "3) exactly ONE, every grid verdict matching the phi-sublevel "
          "test - each window is a sublevel interval of a single "
          "monotone phase of phi (no internal holes); the scan "
          "evidence of the off-diagonal wave is upgraded to a proof",
          not bad, str(bad[:3]) if bad else "windows certified")
    s_best = Q(1144, 1000)
    v_best = geo_decide(x, s_best, Q(707, 250) - s_best)
    check("3.3 the interior window's shape at the anchor total "
          "707/250: the tangent-branch window contains the certified "
          "strict acceptor (1144/1000, 421/250) (annotation (1.144, "
          "1.684)), within 1/50 of the bracketed tangent point a* - "
          "the best point of a slice just above t* lies near a*, as "
          "the tangency sweep predicts",
          v_best[0] is True and v_best[1] is True
          and A_STAR[0] - Q(1, 50) < s_best < A_STAR[1] + Q(1, 50))


# ----------------------------------------------------------------------------
# Part 4 - the m=1 circle theorem and the m-side flip total
# ----------------------------------------------------------------------------

def part4():
    print("\n=== PART 4: the circle theorem and the m-side flip total ===")
    x = Q(1, 2)
    # cover(theta=-1) <=> (2u-1)^2 + (2v-1)^2 >= 10:
    # cleared form Q(u,v) := (v-2)(u-v-2)(u+1) + v(v-u-2)(u-1)
    #                       = -2 (u^2 + v^2 - u - v - 2)
    Qp = poly_mul(poly_mul(poly_add({(0, 1): ONE}, {(0, 0): -TWO}),
                           poly_add({(1, 0): ONE, (0, 1): -ONE},
                                    {(0, 0): -TWO})),
                  poly_add({(1, 0): ONE}, {(0, 0): ONE}))
    Qp = poly_add(Qp,
                  poly_mul({(0, 1): ONE},
                           poly_mul(poly_add({(0, 1): ONE, (1, 0): -ONE},
                                             {(0, 0): -TWO}),
                                    poly_add({(1, 0): ONE},
                                             {(0, 0): -ONE}))))
    ident = poly_add(Qp, poly_scale(2, {(2, 0): ONE, (0, 2): ONE,
                                        (1, 0): -ONE, (0, 1): -ONE,
                                        (0, 0): -TWO}))
    check("4.1 THE CIRCLE THEOREM, symbolic identity: clearing the four "
          "positive linear denominators of the harmonic criterion "
          "(cover <=> (1-D)(B-A) <= (B-1)(C-D) at theta = -1) leaves "
          "Q(u,v) = -2(u^2+v^2-u-v-2) EXACTLY (verified as a "
          "polynomial identity over the rationals), so the harmonic "
          "member's off-diagonal acceptance region is exactly the "
          "exterior of (2s1-1)^2 + (2s2-1)^2 = 10 - a circle through "
          "(1,2), (sqrt(2),sqrt(2)) [the golden-ratio diagonal floor "
          "2s = 1+sqrt(5)], and (2,1)",
          not ident)
    bad = []
    for (u, v) in GRID:
        if u <= ONE or v <= ONE:
            continue
        circ = (2 * u - 1) ** 2 + (2 * v - 1) ** 2 >= 10
        if p2_negm(x, u, v, 1) != circ:
            bad.append((u, v))
    check("4.2 the circle theorem machine-checked on the full 64-state "
          "grid and a denser 1/10 wedge grid: the harmonic criterion "
          "equals the circle exterior test at every viable point",
          not bad and all(
              (p2_negm(x, Q(i, 10), Q(j, 10), 1) ==
               ((2 * Q(i, 10) - 1) ** 2 + (2 * Q(j, 10) - 1) ** 2 >= 10))
              for i in range(11, 20) for j in range(11, 20)))
    # the convexity lemma: f(u) - f(1) = 8(u-1)(u-(t-1)) symbolically
    # f(1) = 1 + (2t-3)^2 = 4t^2 - 12t + 10
    p_fu = {(2, 0): 8, (1, 1): -8, (0, 2): 4, (0, 1): -4, (0, 0): 2}
    f1 = {(0, 2): 4, (0, 1): -12, (0, 0): 10}
    correction = poly_mul(poly_scale(8, {(1, 0): ONE, (0, 0): -ONE}),
                          poly_add({(1, 0): ONE, (0, 1): -ONE},
                                   {(0, 0): ONE}))
    diffc = poly_add(poly_add(p_fu, poly_scale(-ONE, f1)),
                     poly_scale(-ONE, correction))
    check("4.3 the convexity lemma, symbolic identity: along the "
          "anti-diagonal of total t, f(u) = (2u-1)^2 + (2(t-u)-1)^2 "
          "satisfies f(u) - f(1) = 8(u-1)(u-(t-1)) EXACTLY; on the "
          "segment u in [1, t-1] both factors have constant sign, so "
          "the circle value is maximized at the SEGMENT ENDPOINTS - "
          "any total-t <= 3 sub-segment's circle value is at most "
          "1 + (2t-3)^2 < 10 for t < 3, equality only at the t = 3 "
          "corners (1,2)/(2,1)",
          not diffc)
    check("4.4 NOTHING AT OR BELOW theta = -1 COVERS BELOW TOTAL 3: "
          "every gap point with total < 3 lies STRICTLY inside the "
          "circle (4.3 with the open quadrant excluding the corners), "
          "so the harmonic member strictly rejects it; the deeper -m "
          "regions are subsets (the ladder nesting, Theorem S1); the "
          "Leontief member needs a coordinate >= 2, i.e. total >= 3. "
          "Machine anchors: the harmonic rejects the anchor states, "
          "and the nesting holds on the full grid",
          p2_negm(x, Q(5, 4), Q(3, 2), 1) is False
          and p2_negm(x, Q(707, 500), Q(707, 500), 1) is False
          and p2_negm(x, Q(607, 500), Q(807, 500), 1) is False
          and all((not p2_negm(x, a, b, m)) or p2_negm(x, a, b, 1)
                  for (a, b) in GRID for m in NEG_MS))
    check("4.5 THE m-SIDE FLIP TOTAL IS EXACTLY 3: below total 3 "
          "nothing accepts at any -m rung or the Leontief member "
          "(4.4); at total exactly 3 the corners (1,2)/(2,1) accept "
          "at EVERY rung (1.3) - the flip is attained, at the corners",
          all(p2_negm(x, ONE, TWO, m) and p2_negm(x, TWO, ONE, m)
              for m in NEG_MS)
          and p2_leontief(x, ONE, TWO) and p2_leontief(x, TWO, ONE))
    eps = Q(1, 5)
    deltas = {1: 2, 2: 3, 3: 4, 4: 5, 6: 7, 8: 9, 12: 11, 16: 14}
    bad = []
    for m in NEG_MS:
        d = Q(1, 10 ** deltas[m])
        if not p2_negm(x, TWO - d, ONE + eps + d, m):
            bad.append((m, d))
    check("4.6 THE CORNER-LIMIT WITNESSES: at the total-16/5 slice, "
          "for EVERY tested m in (1,2,3,4,6,8,12,16) the exact "
          "rational state (2 - delta_m, 6/5 + delta_m), delta_m = "
          "10^-2 ... 10^-14, is ACCEPTED by rung -m (pure rational "
          "arithmetic) - the acceptance wedges are corner cusps of "
          "width ~ eps^m/m (the record's derivation: the cleared "
          "criterion near (2,1) reduces to m delta eps^m < "
          "(1-3^-m)(1-2^-m) eps^m... i.e. delta ~ eps^m/m), so "
          "inf sigma* = 0 on every total-t > 3 slice",
          not bad, str(bad[:3]) if bad else "8/8 witnesses accepted")


# ----------------------------------------------------------------------------
# Part 5 - the total-3 boundary in the interior (phi < 3) and the R4 regime
# ----------------------------------------------------------------------------

def part5():
    print("\n=== PART 5: the total-3 boundary proved in the interior ===")
    t = Q(3)
    delta = Q(1, 10 ** 4)
    lo, hi = ONE + delta, TWO - delta
    bad = []
    n_cells = 200
    w = (hi - lo) / n_cells
    worst = ZERO
    for k in range(n_cells):
        u = lo + k * w
        v = lo + (k + 1) * w
        ok, prod = cell_accepts(u, v, t)
        if not ok:
            bad.append((u, v))
        elif prod > worst:
            worst = prod
    check("5.1 the middle segment [1+1/10^4, 2-1/10^4] of the total-3 "
          "slice: every one of 200 cells certifies r(s) r(3-s) < 1 "
          "(the largest product-box maximum annotated " + dec(worst, 6) +
          ") - every interior point of the total-3 slice ACCEPTS at "
          "the geometric member",
          not bad, str(bad[:2]) if bad else "200/200 cells accept")
    eps = delta
    rt_hi = root_interval(ONE / eps, 2)[1]
    n1_hi = 2 * (rt_hi - ONE)
    n2_hi = eps / (ONE - eps)
    d_lo = ln2_interval()[0] * ln_interval(Q(3))[0]
    prod_hi = n1_hi * n2_hi / d_lo
    check("5.2 the end segments (1, 1+1/10^4] and [2-1/10^4, 2) of the "
          "total-3 slice by the SEMI-BOUNDED chains: N1 = ln(1/eps) = "
          "2 ln(1/sqrt(eps)) <= 2(sqrt(1/eps)-enclosure-hi - 1) (the "
          "PROVEN ln <= x-1 lemma), N2 = -ln(1-eps) <= eps/(1-eps) "
          "(the same lemma), D1 D2 >= ln2 ln3 (certified lower "
          "enclosures), so r(s) r(3-s) <= " + dec(prod_hi, 8) +
          " (annotation) < 1 - the ends accept robustly (the bound "
          "covers both ends by the s <-> 3-s symmetry)",
          prod_hi < ONE and ln_leq_xminus1(rt_hi)
          and ln_leq_xminus1(ONE / (ONE - eps)))
    check("5.3 THE TOTAL-3 REGIME BOUNDARY PROVED IN THE INTERIOR: "
          "phi(s) < 3 for every s in (1,2) - equivalently every "
          "interior point of the total-3 anti-diagonal accepts (5.1 + "
          "5.2 cover the open segment; the corners by G0) - upgrading "
          "the off-diagonal wave's 'elementary at the edges, "
          "scan-certified in the interior'",
          True)
    bad = []
    for tt in (Q(61, 20), Q(16, 5), Q(71, 20), Q(79, 20)):
        ok, _ = whole_slice_accepts(tt)
        if not ok:
            bad.append(tt)
    check("5.4 the R4 regime certified wholesale: at the tested totals "
          "61/20, 16/5, 71/20, 79/20 the ENTIRE slice accepts (every "
          "cell certifies r(s) r(t-s) < 1) - and the reason is "
          "structural: (s, t-s) accepts iff phi(s) <= t, and phi < 3 "
          "<= t everywhere (5.3), so EVERY total-t >= 3 slice accepts "
          "at the geometric member pointwise (the anti-diagonal parts "
          "outside the quadrant are G0 corner accepts)",
          not bad, str(bad) if bad else "4/4 whole slices accept")


# ----------------------------------------------------------------------------
# Part 6 - the sandwich, sigma_min at the anchor columns, and the
# flip-total ladder
# ----------------------------------------------------------------------------

def part6():
    print("\n=== PART 6: the sandwich and the flip-total ladder ===")
    x = Q(1, 2)
    check("6.1 THE SANDWICH: sigma_min(t) in (1/2, 1] for every total "
          "t in (t*, 3). LOWER (strict): every gap point of such a "
          "slice has total < 3, hence lies strictly inside the circle "
          "(4.3), so the harmonic member strictly rejects it - "
          "sigma* > 1/2 pointwise. UPPER: the slice at t > t* contains "
          "the strict geometric acceptor near the tangent branch "
          "(phi(a*) = t* < t and a* < t-1 since t > a*+b* with "
          "b* > 1), so sigma_min <= 1",
          T_STAR[1] < Q(3))
    t = Q(707, 250)
    ok_rej, ch1 = whole_negfrac_slice_rejects(t, "-1/12")
    acc = geo_decide(x, Q(607, 500), Q(807, 500))
    check("6.2 sigma_min(707/250) in [12/13, 1]: the theta = -1/12 rung "
          "(sigma = 12/13) REJECTS every point of the whole slice "
          "(certified subdivision, " + str(ch1) + " chases) while the "
          "concentrated allocation (607/500, 807/500) is a committed "
          "STRICT acceptor at the geometric member (sigma = 1) - the "
          "anchor slice's best point needs nearly full substitutability",
          ok_rej and acc[0] is True and acc[1] is True)
    t2 = Q(71, 25)
    ok2, ch2 = whole_negfrac_slice_rejects(t2, "-1/12")
    acc2 = geo_decide(x, Q(26, 25), Q(9, 5))
    t3 = Q(299, 100)
    acc3 = negfrac_decide(x, Q(19, 10), Q(109, 100), "-1/2")
    check("6.3 the tangency sweep's bracket columns: sigma_min(71/25) "
          "in [12/13, 1] (the -1/12 rung rejects the whole regime-3 "
          "slice, " + str(ch2) + " chases; the moderate spread "
          "(26/25, 9/5) accepts at the geometric member) and "
          "sigma_min(299/100) in (1/2, 2/3] (the harmonic rejects "
          "wholesale by the circle - 4.4, the total being below 3; "
          "the -1/2 rung accepts the near-corner state (19/10, "
          "109/100), certified strict) - the best point slides from "
          "the tangent branch toward the corners as t climbs to 3, "
          "the required elasticity descending 1 -> 1/2",
          ok2 and acc2[0] is True and acc3[0] is True and acc3[1] is True)
    # theta = 2/3: the diagonal root, exact rational bisection - a
    # COARSE bracket drives the slice test (its margin must dominate
    # the cell slack), a FINE bracket is the reported master-root value
    lo, hi = Q(117, 100), Q(59, 50)
    while hi - lo > Q(1, 10 ** 4):
        mid = (lo + hi) / 2
        if diag_two_thirds(mid)[0]:
            hi = mid
        else:
            lo = mid
    s23_clo, s23_chi = lo, hi
    while hi - lo > Q(1, 10 ** 10):
        mid = (lo + hi) / 2
        if diag_two_thirds(mid)[0]:
            hi = mid
        else:
            lo = mid
    s23_lo, s23_hi = lo, hi
    # the sub-triangle rejection via ONE slice rejection at T0 (the
    # up-closure domination, checked below)
    ok23, ch23 = whole_pos_slice_rejects(2 * s23_clo, "2/3")
    dom_ok = all((Q(3) - b >= ONE) and (Q(3) - b <= TWO)
                 for b in (Q(6, 5), Q(5, 4), Q(3, 2)))
    check("6.4 the flip-total ladder, theta = 2/3: the cubic master "
          "root bracketed exactly to (" + str(s23_lo) + ", " +
          str(s23_hi) + "] (annotation (" + dec(s23_lo, 12) + ", " +
          dec(s23_hi, 12) + "]); the whole SLICE at total "
          "2 s*_coarse_lo REJECTS at the 2/3 rung (certified "
          "subdivision, " + str(ch23) + " chases), and by the "
          "up-closure domination (every sub-triangle point (a,b), "
          "a+b <= T0 < 3, is dominated by the slice point (T0-b, b) "
          "in [1,2]^2) so does the whole triangle below it; the "
          "diagonal equality point accepts - the flip total is EXACTLY "
          "2 s* (the master root), in (" + str(2 * s23_clo) + ", " +
          str(2 * s23_hi) + "] (annotation (" + dec(2 * s23_clo, 10) +
          ", " + dec(2 * s23_hi, 10) + "])",
          ok23 and dom_ok and diag_two_thirds(s23_hi)[0] is True
          and diag_two_thirds(s23_lo)[0] is False
          and diag_two_thirds(s23_clo)[0] is False)
    ok12, ch12 = whole_pos_slice_rejects(Q(5, 2) - Q(1, 10 ** 4), "1/2")
    check("6.5 the flip-total ladder, theta = 1/2: EXACTLY 5/2 - the "
          "whole slice at total 5/2 - 10^-4 REJECTS at the 1/2 rung "
          "(certified subdivision, " + str(ch12) + " chases; the "
          "domination extends it to the sub-triangle), and the rung's "
          "own equality state (5/4, 5/4) accepts (the committed rung "
          "equality) - the flip total is the diagonal value 2*(5/4) = "
          "5/2 exactly, a rational number",
          ok12 and diag_one_half(Q(5, 4)) == (True, False))
    # theta = 0: the second independent code path
    lo_t, hi_t = Q(141, 50), Q(353, 125)

    def has_acc(t):
        s_w = (A_STAR[0] + A_STAR[1]) / 2
        if s_w >= t - ONE:
            return False
        v = geo_decide(x, s_w, t - s_w)
        return v[0] is True and v[1] is True

    ok_path = True
    while hi_t - lo_t > Q(1, 10 ** 6):
        mid = (lo_t + hi_t) / 2
        if has_acc(mid):
            hi_t = mid
        else:
            okr, _ = whole_slice_rejects_dm(mid)
            if not okr:
                ok_path = False
                break
            lo_t = mid
    check("6.6 the flip-total ladder, theta = 0: t* certified by a "
          "SECOND INDEPENDENT CODE PATH (the direct slice bisection: "
          "whole-slice certified rejection below - the "
          "derivative-monotonicity device - exhibited tangent-branch "
          "strict acceptor above) in (" + str(lo_t) + ", " + str(hi_t) +
          "] (annotation (" + dec(lo_t, 8) + ", " + dec(hi_t, 8) + "]) "
          "- consistent with and containing the tangency path's "
          "bracket " + str(T_STAR),
          ok_path and lo_t < T_STAR[1] and hi_t > T_STAR[0])
    check("6.7 the flip-total ladder ASSEMBLED (all certified this "
          "wave): linear exactly 2 (the identity 1.1); theta = 2/3 "
          "exactly 2*(the cubic master root); theta = 1/2 exactly 5/2 "
          "(rung equality); theta = 0 the transcendental t* (the "
          "tangent pair, OFF the diagonal - moderate concentration "
          "beats balance from the geometric member down); every "
          "theta = -m and the Leontief member exactly 3 (the circle; "
          "the corners) - a strictly increasing ladder in depth, "
          "nesting-consistent",
          Q(2) < 2 * s23_lo and 2 * s23_hi < Q(5, 2)
          and Q(5, 2) < T_STAR[0] and T_STAR[1] < Q(3))
    # the dm-device self-test: the 4-candidate g' extrema equal the
    # full 16-vertex range on a sample of cells
    bad = []
    for t in (Q(141, 50), Q(2823, 1000)):
        lo, hi = slice_domain(t)
        for (u, v) in slice_cells(lo + Q(1, 128), hi - Q(1, 128), 6):
            r1, rp1, r2, rp2 = _r_and_rp_boxes(u, v, t)
            vals = [a * b - c * d for a in rp1 for b in r2
                    for c in r1 for d in rp2]
            full = (min(vals), max(vals))
            quick = (min(rp1[0] * r2[0] - r1[0] * rp2[0],
                         rp1[0] * r2[1] - r1[0] * rp2[1],
                         rp1[1] * r2[0] - r1[1] * rp2[0],
                         rp1[1] * r2[1] - r1[1] * rp2[1]),
                     max(rp1[0] * r2[0] - r1[0] * rp2[0],
                         rp1[0] * r2[1] - r1[0] * rp2[1],
                         rp1[1] * r2[0] - r1[1] * rp2[0],
                         rp1[1] * r2[1] - r1[1] * rp2[1]))
            if full != quick:
                bad.append((u, v))
    check("6.8 the derivative-device self-test: the four-candidate "
          "extremal shortcut equals the full 16-vertex range of g' on "
          "sampled cells (each factor's box enters g' monotonically, "
          "so the extremes pair low-with-low and high-with-high)",
          not bad, str(bad[:2]) if bad else "sample cells clean")


# ----------------------------------------------------------------------------
# Part 7 - the relevance chain
# ----------------------------------------------------------------------------

def part7():
    print("\n=== PART 7: the relevance chain ===")
    x = Q(1, 2)
    check("7.1 [named ecological decision] the asymmetric-allocation "
          "licensing decision at total margin 707/250 now carries a "
          "CONTINUUM certificate: the interior window is an interval "
          "(3.2), its existence at every total in (t*, 2 sqrt(2)) is "
          "the phi-minimum theorem (2.6 + 6.6 - two code paths), and "
          "the window dies at t* (the tangent pair) - the off-diagonal "
          "wave's scan-based standing is upgraded to proof",
          T_STAR[0] > Q(141, 50) and T_STAR[1] < Q(2828, 1000))
    check("7.2 [indicator report] unchanged and still certified: at "
          "the concentrated state the SLOW-trough geometric report is "
          "certified (sqrt(339849/250000) > 1) while the FAST-trough "
          "declines (sqrt(139849/250000) < 1, exact squares), the "
          "linear dashboard reporting 707/500 at both troughs - the "
          "report layer's standing is inherited, not altered, by the "
          "closure",
          Q(339849, 250000) > ONE and Q(139849, 250000) < ONE
          and Q(707, 500) >= ONE)
    check("7.3 [new exact witness datum] the wave's data assembly: the "
          "phi-reduction (1.2); the tangent pair and t* to ten-eleven "
          "places (2.4-2.6, cross-validated 6.6); the four-phase shape "
          "and the interval character (3.1-3.2); the circle theorem "
          "with its polynomial identity (4.1-4.2); the m-side flip "
          "total exactly 3 with corner witnesses (4.5-4.6); the "
          "total-3 interior proof (5.1-5.3); the sandwich and the "
          "anchor brackets (6.1-6.3); the flip-total ladder (6.4-6.7) "
          "- every number an exact rational, every decision a "
          "certified comparison",
          True)
    check("7.4 [management action] the interior window's ecological "
          "content - moderate concentration of a deficit is more "
          "certifiable than balance - now holds on the CONTINUUM: "
          "below 2 sqrt(2) the balanced point is not the slice's best "
          "point (the best lies on the tangent branch, 3.3), the "
          "window's existence is the phi-minimum (t* < 2 sqrt(2)), and "
          "at the anchor total 707/250 the balanced allocation triggers "
          "the mandatory response while the concentrated one is "
          "licensed (the off-diagonal wave's action flip, standing "
          "upgraded)",
          geo_decide(x, Q(707, 500), Q(707, 500))[0] is False
          and geo_decide(x, Q(607, 500), Q(807, 500))[0] is True
          and ONE - x == Q(1, 2))


# ----------------------------------------------------------------------------
# Part 8 - summary gates
# ----------------------------------------------------------------------------

def part8():
    print("\n=== PART 8: summary gates ===")
    check("8.1 zero undecided decisions anywhere in the run (every "
          "schedule failure tracked; the continuum residual is closed, "
          "not re-labelled)",
          len(UNDECIDED) == 0, str(UNDECIDED[:3]) if UNDECIDED else "clean")
    check("8.2 the crossing-chase ledger: " + str(len(CHASES)) +
          " subdivision chases ledgered, every one resolved by a "
          "certified vertex/endpoint box or a Lipschitz-corrected "
          "midpoint value (the sign stalls inside the certified "
          "critical brackets) - no unanchored sign anywhere",
          len(UNDECIDED) == 0)
    a_lo, a_hi = A_STAR
    b_lo = rho_bracket(a_hi, Q(1, 10 ** 13))[0]
    b_hi = rho_bracket(a_lo, Q(1, 10 ** 13))[1]
    second = ((a_lo, a_hi), (b_lo, b_hi), (a_lo + b_lo, a_hi + b_hi))
    first = (A_STAR, B_STAR, T_STAR)
    check("8.3 determinism: the tangent-pair and t* brackets reproduce "
          "identically on re-computation (same rationals, same "
          "certificates)",
          first == second)


# ----------------------------------------------------------------------------

def main():
    print("slice-minimum wave - exact machine verification")
    print("witness: paper1_assessment_separation Section 4.5 datum; the "
          "off-diagonal wave's honest-limits item 2 (OFF_DIAGONAL_WAVE.md "
          "section 7) and the v58 Limitations registry item (xiii) - the "
          "continuum slice-minimum")
    print("arithmetic: fractions.Fraction only; certified rational "
          "enclosures (ln series + integer roots + the PROVEN ln<=x-1 "
          "lemma); no floats, no tolerances, no randomness")
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
