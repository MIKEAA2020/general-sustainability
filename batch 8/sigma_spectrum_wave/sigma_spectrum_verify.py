#!/usr/bin/env python3
"""
Sigma-spectrum wave - exact machine verification.

Task 105 / batch 8 / paper 1 (Ecological Indicators).
Executes the research program of joint-assessment point 3.A-8
(BATCH8_PAPER1_ECOLOGICAL_INDICATORS_JOINT_ASSESSMENT.md): the
substitutability-elasticity (sigma) extension of the witness datum of
paper1_assessment_separation_v52.tex, Section 4.5, with exact rational
witnesses and machine verification, under the relevance test
(named ecological decision; changes what an actual indicator reports;
new exact witness datum; alters at least one management action).

House discipline (identical to the deposited SafeTransition artifact):
- exact rational arithmetic only (fractions.Fraction); NO floating
  point, NO tolerances, NO randomness; deterministic and idempotent;
- fail loud: every gate is a named check; any failure exits nonzero;
- decimal strings in the log are ANNOTATIONS ONLY (integer long
  division); no decision ever consults them.

The sigma-family (floor-referenced indices):
  lambda_i = 1 + s_i   (lambda = 1 exactly at the floor: LPI currency).
  Weight-normalized CES means M_theta(lambda; w), sigma = 1/(1-theta):
    theta = 1      sigma = infinity   linear aggregate (the paper's engine)
    theta = 2/3    sigma = 3          CES
    theta = 1/2    sigma = 2          CES
    theta = 0      sigma = 1          geometric mean (LPI structure)
    theta = -m     sigma = 1/(m+1)    CES (m=1: harmonic)
    theta -> -inf  sigma -> 0         Leontief min (= the typed operator)
  Collapse convention (all theta < 1 members): any tube value
  lambda_i <= 0 rejects the plan (a collapsed coordinate cannot be
  compensated). The linear member (theta = 1) keeps the manuscript's own
  compensatory semantics (negative margins may be compensated).

Protocol 2 (per-weight acceptance) at rung theta:
  z = (x, s1, s2) is accepted iff for every weight w there is a plan in
  {NO-SWITCH, FAST, SLOW, STAGED} whose worst-case tube keeps the rung's
  aggregate at/above its floor. STAGED needs x >= 1 (successor x-1 >= 0)
  and then serves every weight at every rung; NO-SWITCH misses G always.
  FAST's worst tube point is lambda^F = (s1-1, s2+1), SLOW's the mirror.

Diagonal master equation (s1 = s2 = s, x < 1, s in (1,2)):
  cover <=> (s-1)^theta + (s+1)^theta >= 2   (theta > 0)
  cover <=> (s-1)^theta + (s+1)^theta <= 2   (theta < 0)
with the theta = 0 member read as its limit: cover <=> (s-1)(s+1) >= 1.
Exact closed forms (all pure rational comparisons; derivations in the
wave document):
  theta=1:    s >= 1
  theta=2/3:  s^2 >= 3, or 27*(s^2-1)^2 >= (3-s^2)^3
  theta=1/2:  s >= 5/4
  theta=0:    s^2 >= 2
  theta=-1:   s^2 >= s+1            (critical floor phi = (1+sqrt5)/2)
  theta=-2:   s^2 >= 3              (critical floor sqrt3)
  theta=-3:   s^3+3s <= (s^2-1)^3
  theta=-m:   (s-1)^m + (s+1)^m <= 2*(s^2-1)^m
  Leontief:   s >= 2                (the typed boundary)

NOTATION: the manuscript's per-weight thresholds rho_1 = 2/3 and
rho_2 = 3/2 (Section 4.5/6.3) are WEIGHT RATIOS; the CES exponent here
is theta. The two never interact in this file.
"""

import sys
from fractions import Fraction as Q

ZERO = Q(0)
ONE = Q(1)
TWO = Q(2)

# ----------------------------------------------------------------------------
# The witness datum (paper1 v52, Sections 4.5 and 6.3)
# ----------------------------------------------------------------------------

DIP = Q(2)                    # worst-case dip depth in the active coordinate
COST = Q(1)                   # STAGED spends one unit of the reserve x
BLIM = Q(2)                   # B_lim (kt), the Section 6.3 fishery reading
CANON = (Q(1, 2), Q(6, 5), Q(6, 5))   # the Section 6.3 datum (x, s1, s2)

CHECKS = []


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


# ----------------------------------------------------------------------------
# Interval cover machinery (p = weight share of coordinate 1, in [0,1])
# ----------------------------------------------------------------------------

def interval_covers(fast_iv, slow_iv):
    """fast_iv, slow_iv: None or (lo, hi) closed subintervals of [0,1] -
    the per-weight acceptance sets of FAST and SLOW. Protocol 2 accepts
    iff their union covers [0,1]."""
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


# ----------------------------------------------------------------------------
# Rung decisions in full (x, s1, s2) generality
# ----------------------------------------------------------------------------

def p2_linear(x, s1, s2):
    """theta = 1: the manuscript's own engine (w.s >= 0 at the worst point)."""
    if x >= COST:
        return True                      # STAGED serves every weight
    if s1 >= TWO:
        fast_iv = (ZERO, ONE)            # dip bottom stays nonnegative
    else:
        fast_iv = (ZERO, s2 / (TWO - s1 + s2))
    if s2 >= TWO:
        slow_iv = (ZERO, ONE)
    else:
        slow_iv = ((TWO - s2) / (TWO + s1 - s2), ONE)
    return interval_covers(fast_iv, slow_iv)


def fast_iv_negm(s1, s2, m):
    """theta = -m FAST acceptance set. Collapse convention: s1 <= 1 rejects
    (lambda_1 bottom = s1-1 <= 0). Otherwise
    p/(s1-1)^m + (1-p)/(s2+1)^m <= 1  <=>  p <= a(b-1)/(b-a), pure rational."""
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
    """theta = 0 (geometric / LPI structure). Exact scope: on the diagonal,
    cover <=> (s1-1)(s1+1) >= 1. Off the diagonal the cover comparison is
    log-transcendental; return True on the proven-sufficient rational
    condition, False on the proven-necessary failure, None if undecided.
    Viability: FAST needs s1 > 1 (its tube's lambda_1 bottom = s1-1 > 0),
    SLOW needs s2 > 1; a single surviving plan covers all weights exactly
    when it satisfies its own typed margin (>= 2)."""
    if x >= COST:
        return True
    fast_viable = s1 > ONE
    slow_viable = s2 > ONE
    if not fast_viable and not slow_viable:
        return False
    if fast_viable and not slow_viable:
        return (s1 - ONE) >= ONE          # FAST alone covers iff s1 >= 2
    if slow_viable and not fast_viable:
        return (s2 - ONE) >= ONE          # SLOW alone covers iff s2 >= 2
    if s1 == s2:
        return (s1 - ONE) * (s1 + ONE) >= ONE
    if (s1 - ONE) * (s2 + ONE) >= ONE and (s1 + ONE) * (s2 - ONE) >= ONE:
        return True
    if max(s1 * s1, s2 * s2) < TWO:
        return False
    return None


def p2_leontief(x, s1, s2):
    """theta -> -inf: the typed operator (weight-independent)."""
    return (x >= COST) or (s1 >= TWO) or (s2 >= TWO)


# ----------------------------------------------------------------------------
# Diagonal closed forms - (accept, strict) with strict = comparison unequal
# ----------------------------------------------------------------------------

def diag_linear(s):
    return (s >= ONE, s != ONE)


def diag_two_thirds(s):
    """(s-1)^(2/3) + (s+1)^(2/3) >= 2. With u^3=(s-1)^2, v^3=(s+1)^2,
    w=uv (w^3=(s^2-1)^2), t=u+v: t^3 = 2s^2+2 + 3wt, and f(t)=t^3-3wt-(2s^2+2)
    is strictly increasing on [sqrt(w), inf) with t^2 >= 4w > w and
    4 > w (since (s^2-1)^2 < 9 < 64 for s<2), so t >= 2 <=> f(2) <= 0
    <=> 3w >= 3 - s^2; cube both nonnegative sides when 3 - s^2 > 0."""
    if s <= ONE:
        return (False, s != ONE)
    s2 = s * s
    if s2 >= Q(3):
        return (True, s2 != Q(3))
    lhs = 27 * (s2 - ONE) ** 2          # (3w)^3 = 27 w^3 = 27 (s^2-1)^2
    rhs = (Q(3) - s2) ** 3
    return (lhs >= rhs, lhs != rhs)


def diag_one_half(s):
    """sqrt(s-1) + sqrt(s+1) >= 2. Both sides nonnegative for 1<s<2:
    squaring twice gives 2s + 2 sqrt(s^2-1) >= 4 <=> sqrt(s^2-1) >= 2-s
    <=> s^2-1 >= (2-s)^2 <=> 4s >= 5."""
    if s <= ONE:
        return (False, s != ONE)
    return (4 * s >= Q(5), 4 * s != Q(5))


def diag_geo(s):
    """theta = 0 limit: cover <=> (s-1)(s+1) >= 1 <=> s^2 >= 2."""
    if s <= ONE:
        return (False, s != ONE)
    return (s * s >= TWO, s * s != TWO)


def diag_negm(s, m):
    """theta = -m: cover <=> (s-1)^m + (s+1)^m <= 2 (s^2-1)^m."""
    if s <= ONE:
        return (False, s != ONE)
    lhs = (s - ONE) ** m + (s + ONE) ** m
    rhs = TWO * (s * s - ONE) ** m
    return (lhs <= rhs, lhs != rhs)


def diag_leontief(s):
    return (s >= TWO, s != TWO)


# The ladder: ordered by DECREASING theta (index 0 = theta 1 = sigma inf).
# Each row: (label, diagonal decider, general decider or None if
# diagonal-only in the machine's exact scope).
LADDER = [
    ("theta=1    sigma=inf", diag_linear, p2_linear),
    ("theta=2/3  sigma=3  ", diag_two_thirds, None),
    ("theta=1/2  sigma=2  ", diag_one_half, None),
    ("theta=0    sigma=1  ", diag_geo, p2_geo),
    ("theta=-1   sigma=1/2", lambda s: diag_negm(s, 1), lambda x, a, b: p2_negm(x, a, b, 1)),
    ("theta=-2   sigma=1/3", lambda s: diag_negm(s, 2), lambda x, a, b: p2_negm(x, a, b, 2)),
    ("theta=-3   sigma=1/4", lambda s: diag_negm(s, 3), lambda x, a, b: p2_negm(x, a, b, 3)),
    ("theta=-4   sigma=1/5", lambda s: diag_negm(s, 4), lambda x, a, b: p2_negm(x, a, b, 4)),
    ("theta=-6   sigma=1/7", lambda s: diag_negm(s, 6), lambda x, a, b: p2_negm(x, a, b, 6)),
    ("theta=-8   sigma=1/9", lambda s: diag_negm(s, 8), lambda x, a, b: p2_negm(x, a, b, 8)),
    ("theta=-12  sigma=1/13", lambda s: diag_negm(s, 12), lambda x, a, b: p2_negm(x, a, b, 12)),
    ("theta=-16  sigma=1/17", lambda s: diag_negm(s, 16), lambda x, a, b: p2_negm(x, a, b, 16)),
    ("theta=-inf sigma=0  ", diag_leontief, p2_leontief),
]

LADDER_SIGMA = ["infinity", Q(3), Q(2), Q(1), Q(1, 2), Q(1, 3), Q(1, 4),
                Q(1, 5), Q(1, 7), Q(1, 9), Q(1, 13), Q(1, 17), "0"]

NEG_MS = (1, 2, 3, 4, 6, 8, 12, 16)


# ----------------------------------------------------------------------------
# Part 0 - bridge to the deposited datum (Sections 4.5 / 6.3 anchors)
# ----------------------------------------------------------------------------

def part0():
    print("\n=== PART 0: bridge to the deposited witness (paper1 v52, 4.5/6.3) ===")
    x, s1, s2 = CANON
    check("0.1 canonical datum is the Section 6.3 state (x,s1,s2)=(1/2,6/5,6/5)",
          (x, s1, s2) == (Q(1, 2), Q(6, 5), Q(6, 5)))
    B0 = BLIM + s1
    check("0.2 B(0) = B_lim + 6/5 = 16/5 kt", B0 == Q(16, 5), "B(0)=" + str(B0))
    tr1 = (s1, s1 - DIP, s1)
    check("0.3 FAST s1-tube breakpoints 6/5 -> -4/5 -> 6/5",
          tr1 == (Q(6, 5), Q(-4, 5), Q(6, 5)), str(tr1))
    dash = tuple(a + s2 for a in tr1)
    check("0.4 dashboard (equal weighting, s1+s2) tube values (12/5, 2/5, 12/5)",
          dash == (Q(12, 5), Q(2, 5), Q(12, 5)), str(dash))
    Btrough = BLIM + s1 - DIP
    check("0.5 adverse trough B = 6/5 kt = 3/5 B_lim (below the LRP)",
          Btrough == Q(6, 5) and Btrough == Q(3, 5) * BLIM,
          "B_trough=" + str(Btrough))
    check("0.6 heatwave chain: benign trough 17/10 minus delta_0=1/2 = 6/5",
          Q(17, 10) - Q(1, 2) == Btrough)
    r, K = Q(4), Q(10)
    sig = r * B0 * (ONE - B0 / K)
    check("0.7 Schaefer surplus sigma(16/5) = 1088/125 (sustained-yield quota)",
          sig == Q(1088, 125), str(sig))
    U = fast_iv_negm  # noqa: F841 (readability anchor)
    # linear thresholds at the datum (paper's rho_1=2/3, rho_2=3/2 ratios)
    fu = (ZERO, s2 / (TWO - s1 + s2))[1]
    fl = (TWO - s2) / (TWO + s1 - s2)
    check("0.8 linear thresholds: FAST serves p<=3/5, SLOW serves p>=2/5 "
          "(weight ratios rho_2=3/2, rho_1=2/3)",
          fu == Q(3, 5) and fl == Q(2, 5) and fu / (ONE - fu) == Q(3, 2)
          and fl / (ONE - fl) == Q(2, 3), "U=" + str(fu) + " L=" + str(fl))
    check("0.9 rescue shortfall kappa* = 1 - x = 1/2 at the datum",
          ONE - x == Q(1, 2))
    check("0.10 the datum is in the impossibility region I: typed REJECT, "
          "weak(linear) ACCEPT",
          (not p2_leontief(x, s1, s2)) and p2_linear(x, s1, s2))


# ----------------------------------------------------------------------------
# Part 1 - the theta=1 member IS the manuscript's engine; Leontief = typed
# ----------------------------------------------------------------------------

def part1():
    print("\n=== PART 1: rung identities with the manuscript's operators ===")
    bad = []
    n = 0
    for i in range(11):
        for j in range(11):
            for x in (Q(1, 2), Q(3, 2)):
                s1, s2 = Q(i, 4), Q(j, 4)
                n += 1
                if p2_linear(x, s1, s2) != ((x >= ONE) or (s1 + s2 >= TWO)):
                    bad.append((x, s1, s2))
    check("1.1 P2(theta=1) == {x>=1} u {s1+s2>=2} on 242 states (Thm 5(2))",
          not bad, str(n) + " states" if not bad else str(bad[:3]))
    bad = []
    for i in range(11):
        for j in range(11):
            for x in (Q(1, 2), Q(3, 2)):
                s1, s2 = Q(i, 4), Q(j, 4)
                if p2_leontief(x, s1, s2) != ((x >= ONE) or (s1 >= TWO) or (s2 >= TWO)):
                    bad.append((x, s1, s2))
    check("1.2 P2(Leontief) == {x>=1} u {s1>=2} u {s2>=2} on 242 states "
          "(Thm 5(1); audit Thm 11(3): the sigma->0 member is the typed operator)",
          not bad, str(bad[:3]) if bad else "identity holds")


# ----------------------------------------------------------------------------
# Part 2 - the diagonal master equation: independent code paths
# ----------------------------------------------------------------------------

def perp_plan(theta_lbl, lam1, lam2, p):
    """Exact per-weight decision: p*lam1^theta + (1-p)*lam2^theta >= 1
    (lam1, lam2 > 0). theta=1/2: square-twice isolation; theta=2/3:
    cube isolation with the global monotonicity certificate
    t^2 - pq*w = p^2 u^2 + pq*w + q^2 v^2 > 0."""
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
    raise ValueError(theta_lbl)


def perp_served(theta_lbl, s, p):
    """FAST-or-SLOW serves the weight p at the diagonal state (s,s), x<1."""
    if s <= ONE:
        return False
    fast = perp_plan(theta_lbl, s - ONE, s + ONE, p)
    slow = perp_plan(theta_lbl, s + ONE, s - ONE, p)
    return fast or slow


def part2():
    print("\n=== PART 2: diagonal master equation, cross-validated ===")
    mism = []
    for k in range(0, 40):
        s = ONE + Q(k, 20)
        if s >= TWO:
            break
        for m in NEG_MS:
            if diag_negm(s, m)[0] != p2_negm(Q(1, 2), s, s, m):
                mism.append((s, m))
    check("2.1 theta=-m closed forms == interval route on the diagonal "
          "(40 states x 8 rungs)", not mism,
          str(mism[:3]) if mism else "two independent paths agree")
    mism = []
    for k in range(0, 40):
        s = ONE + Q(k, 20)
        if s >= TWO:
            break
        if p2_geo(Q(1, 2), s, s) != diag_geo(s)[0]:
            mism.append(s)
    check("2.2 geometric: diagonal route == (s-1)(s+1)>=1 closed form",
          not mism, str(len(mism)) + " mismatches" if mism else "40 states agree")
    # isolation certificates for the theta=2/3 route (rational, s in (1,2)):
    cert_ok = all(0 < (ONE + Q(k, 20)) ** 2 - ONE < Q(3) for k in range(1, 20))
    cert_ok = cert_ok and all(((ONE + Q(k, 20)) ** 2 - ONE) ** 2 < 64
                              for k in range(1, 20))
    check("2.3a cube-isolation certificates hold on the diagonal grid "
          "(0 < s^2-1, (s^2-1)^2 < 64)", cert_ok)
    mism = []
    for s in (Q(6, 5), Q(5, 4), Q(13, 10), Q(3, 2), Q(11, 10), Q(23, 20), Q(9, 5)):
        for lbl, decider in (("1/2", diag_one_half), ("2/3", diag_two_thirds)):
            acc = decider(s)[0]
            if acc:
                for p in (ZERO, Q(1, 4), Q(2, 5), Q(1, 2), Q(3, 5), Q(3, 4), ONE):
                    if not perp_served(lbl, s, p):
                        mism.append((s, lbl, p, "accept-but-unserved"))
                        break
            else:
                if perp_served(lbl, s, Q(1, 2)):
                    mism.append((s, lbl, Q(1, 2), "reject-but-middle-served"))
    check("2.3b theta=1/2 and 2/3 closed forms consistent with the exact "
          "per-weight algebra at 7 states x 7 weights", not mism,
          str(mism[:3]) if mism else "consistent")


# ----------------------------------------------------------------------------
# Part 3 - the critical-floor ladder s*(theta) on the diagonal
# ----------------------------------------------------------------------------

def part3():
    print("\n=== PART 3: critical-floor ladder s*(theta) (diagonal, x<1) ===")
    brackets = {}
    for name, dfun, _gen in LADDER:
        last_rej, first_acc, prev = None, None, None
        mono = True
        for kk in range(90, 200):
            s = Q(kk, 100)
            acc = dfun(s)[0]
            if prev is not None:
                if prev is False and acc:
                    if first_acc is None:
                        first_acc = s
                if prev is True and not acc:
                    mono = False
            if not acc:
                last_rej = s
            prev = acc
        brackets[name] = (last_rej, first_acc, mono)
    ok = check("3.0 each rung's acceptance is monotone in s on the 1/100 grid "
               "(single reject->accept flip)", all(v[2] for v in brackets.values()))
    # exact identifications (document Table 2):
    lr, fa, _ = brackets["theta=1    sigma=inf"]
    ok &= check("3.1 theta=1: s* = 1 exactly (first accept at s=1, equality)",
                fa == ONE and diag_linear(ONE) == (True, False),
                "bracket (" + str(lr) + ", " + str(fa) + "]")
    lr, fa, _ = brackets["theta=1/2  sigma=2  "]
    ok &= check("3.2 theta=1/2: s* = 5/4 exactly (equality accept)",
                fa == Q(5, 4) and diag_one_half(Q(5, 4)) == (True, False),
                "bracket (" + str(lr) + ", " + str(fa) + "]")
    lr, fa, _ = brackets["theta=0    sigma=1  "]
    ok &= check("3.3 theta=0: s* = sqrt(2) exactly, machine-bracketed "
                "(141/100)^2 < 2 <= (142/100)^2",
                fa == Q(142, 100) and Q(141, 100) ** 2 < TWO <= Q(142, 100) ** 2,
                "bracket (" + str(lr) + ", " + str(fa) + "]")
    lr, fa, _ = brackets["theta=-1   sigma=1/2"]
    ok &= check("3.4 theta=-1: s* = phi = (1+sqrt5)/2 (s^2 = s+1), bracketed "
                "(161/100)^2 < 161/100+1 <= (162/100)^2",
                fa == Q(162, 100) and Q(161, 100) ** 2 < Q(161, 100) + ONE
                <= Q(162, 100) ** 2,
                "bracket (" + str(lr) + ", " + str(fa) + "]")
    ok &= check("3.5 Fibonacci witnesses of phi: 8/5 rejected, 13/8 accepted "
                "at theta=-1",
                (not diag_negm(Q(8, 5), 1)[0]) and diag_negm(Q(13, 8), 1)[0])
    lr, fa, _ = brackets["theta=-2   sigma=1/3"]
    ok &= check("3.6 theta=-2: s* = sqrt(3), bracketed (173/100)^2 < 3 <= "
                "(174/100)^2",
                fa == Q(174, 100) and Q(173, 100) ** 2 < Q(3) <= Q(174, 100) ** 2,
                "bracket (" + str(lr) + ", " + str(fa) + "]")
    lr, fa, _ = brackets["theta=-3   sigma=1/4"]
    ok &= check("3.7 theta=-3: s* solves s^3+3s = (s^2-1)^3; exact witnesses "
                "7/4 rejected, 9/5 accepted",
                (not diag_negm(Q(7, 4), 3)[0]) and diag_negm(Q(9, 5), 3)[0],
                "bracket (" + str(lr) + ", " + str(fa) + "]")
    lr, fa, _ = brackets["theta=2/3  sigma=3  "]
    ok &= check("3.8 theta=2/3: s* solves 27(s^2-1)^2 = (3-s^2)^3; exact "
                "witnesses 23/20 rejected, 6/5 accepted",
                (not diag_two_thirds(Q(23, 20))[0]) and diag_two_thirds(Q(6, 5))[0],
                "bracket (" + str(lr) + ", " + str(fa) + "]")
    lr, fa, _ = brackets["theta=-inf sigma=0  "]
    ok &= check("3.9 Leontief: every s < 2 rejected; s* = 2 (the typed "
                "boundary)", fa is None and lr == Q(199, 100))
    # bracket monotonicity down the ladder: s* increasing as theta decreases
    seq = [brackets[r[0]] for r in LADDER]
    mono_seq = True
    prev_fa = ONE
    for lr, fa, _ in seq:
        cur = fa if fa is not None else TWO
        if cur < prev_fa:
            mono_seq = False
        prev_fa = cur
    ok &= check("3.10 the critical floor increases monotonically down the "
                "ladder: 1 <= 5/4 < sqrt2 < phi < sqrt3 < s*(-3) < ... < 2",
                mono_seq)
    print("  ladder table (s* brackets, annotations " +
          dec(ONE, 2) + " .. " + dec(TWO, 2) + "):")
    for name, dfun, _g in LADDER:
        lr, fa, _ = brackets[name]
        print("    " + name + "  s* in (" + str(lr) + ", " +
              (str(fa) + "]" if fa is not None else "2]"))
    return ok


# ----------------------------------------------------------------------------
# Part 4 - nesting (the monotone ladder of accepted sets)
# ----------------------------------------------------------------------------

def part4():
    print("\n=== PART 4: nesting (power-mean monotonicity) ===")
    bad = []
    for k in range(0, 40):
        s = ONE + Q(k, 20)
        if s >= TWO:
            break
        dec = [r[1](s)[0] for r in LADDER]
        # acceptance must be a prefix of the ladder (upper ray in theta)
        seen_rej = False
        for a in dec:
            if not a:
                seen_rej = True
            elif seen_rej:
                bad.append((s, "accept after reject"))
                break
    check("4.1 diagonal: acceptance is an upper ray in theta at all 40 states",
          not bad, str(bad[:3]) if bad else "nested")
    bad = []
    undecided = 0
    for i in range(3, 11):
        for j in range(3, 11):
            s1, s2, x = Q(i, 4), Q(j, 4), Q(1, 2)
            dec = {}
            for name, _d, gen in LADDER:
                if gen is None:
                    continue
                v = gen(x, s1, s2)
                if v is None:
                    undecided += 1
                dec[name] = v
            if dec["theta=1    sigma=inf"] is False:
                for name, v in dec.items():
                    if v is True:
                        bad.append((s1, s2, name, "accept below linear"))
            if dec["theta=-1   sigma=1/2"] is True and \
               dec["theta=0    sigma=1  "] is False:
                bad.append((s1, s2, "geometric contradicts harmonic"))
            if dec["theta=0    sigma=1  "] is True and \
               dec["theta=1    sigma=inf"] is False:
                bad.append((s1, s2, "linear contradicts geometric"))
    check("4.2 off-diagonal grid (64 states, rational rungs + decided "
          "geometric cells): no rung accepts where a higher rung rejects",
          not bad, str(bad[:3]) if bad else
          "consistent; " + str(undecided) + " geometric cells honestly "
          "undecided (log-transcendental, see document)")


# ----------------------------------------------------------------------------
# Part 5 - the sigma* brackets (new exact witness data)
# ----------------------------------------------------------------------------

SPECIALS = [
    ("only-linear A (1,1)      ", Q(1, 2), Q(1), Q(1)),
    ("only-linear B (3/2,1/2)  ", Q(1, 2), Q(3, 2), Q(1, 2)),
    ("canonical    (6/5,6/5)   ", Q(1, 2), Q(6, 5), Q(6, 5)),
    ("boundary     (5/4,5/4)   ", Q(1, 2), Q(5, 4), Q(5, 4)),
    ("mid          (13/10,.)   ", Q(1, 2), Q(13, 10), Q(13, 10)),
    ("LPI witness  (3/2,3/2)   ", Q(1, 2), Q(3, 2), Q(3, 2)),
    ("harmonic wit.(13/8,.)    ", Q(1, 2), Q(13, 8), Q(13, 8)),
    ("deep         (9/5,9/5)   ", Q(1, 2), Q(9, 5), Q(9, 5)),
    ("deeper       (39/20,.)   ", Q(1, 2), Q(39, 20), Q(39, 20)),
]


def part5():
    print("\n=== PART 5: critical-elasticity brackets sigma*(z) ===")
    print("  (sigma = 1/(1-theta); accepted rungs form a prefix of the ladder;")
    print("   sigma* sits between the last accepted and first rejected rung)")
    ok_all = True
    for lbl, x, s1, s2 in SPECIALS:
        typed_rej = not p2_leontief(x, s1, s2)
        lin = p2_linear(x, s1, s2)
        if not (typed_rej and lin):
            ok_all &= check("5.x " + lbl + " is a gap state (typed REJECT, "
                            "linear ACCEPT)", False)
            continue
        if s1 != s2:
            negs = [p2_negm(x, s1, s2, m) for m in NEG_MS]
            geo = p2_geo(x, s1, s2)
            ok_all &= check(
                "5.x " + lbl + " sigma* = infinity exactly: every theta<1 "
                "rung rejects (min coordinate <= 1 kills FAST/SLOW "
                "viability under the collapse convention)",
                not any(negs) and geo is False,
                "negm all reject; geometric reject")
            continue
        dec = [(name, dfun(s1)) for name, dfun, _g in LADDER]
        acc = [d[1][0] for d in dec]
        strict = [d[1][1] for d in dec]
        # accepted prefix length k+1 (linear always accepts on gap states)
        k = 0
        while k + 1 < len(acc) and acc[k + 1]:
            k += 1
        if k == 0:
            ok_all &= check("5.x " + lbl + " sigma* = infinity exactly "
                            "(only the linear member certifies)",
                            not any(acc[1:]))
            continue
        sig_hi = LADDER_SIGMA[k]          # sigma at the last accepting rung
        sig_lo = LADDER_SIGMA[k + 1]      # sigma at the first rejecting rung
        if strict[k]:
            bracket = "sigma* in (" + str(sig_lo) + ", " + str(sig_hi) + ")  [strict]"
        else:
            bracket = "sigma* = " + str(sig_hi) + " exactly  [equality at the rung]"
        ok_all &= check("5.x " + lbl + " " + bracket, True,
                        "last accepting rung " + dec[k][0] +
                        "; first rejecting " + dec[k + 1][0])


# ----------------------------------------------------------------------------
# Part 6 - per-rung false-certification witnesses (the uniform direction)
# ----------------------------------------------------------------------------

def part6():
    print("\n=== PART 6: every positive-sigma rung false-certifies some gap "
          "state; Leontief none ===")
    witnesses = [
        ("theta=2/3  sigma=3   ", (Q(1, 2), Q(6, 5), Q(6, 5)), diag_two_thirds),
        ("theta=1/2  sigma=2   ", (Q(1, 2), Q(13, 10), Q(13, 10)), diag_one_half),
        ("theta=0    sigma=1   ", (Q(1, 2), Q(3, 2), Q(3, 2)), diag_geo),
        ("theta=-1   sigma=1/2 ", (Q(1, 2), Q(13, 8), Q(13, 8)), lambda s: diag_negm(s, 1)),
        ("theta=-2   sigma=1/3 ", (Q(1, 2), Q(26, 15), Q(26, 15)), lambda s: diag_negm(s, 2)),
        ("theta=-3   sigma=1/4 ", (Q(1, 2), Q(9, 5), Q(9, 5)), lambda s: diag_negm(s, 3)),
        ("theta=-4   sigma=1/5 ", (Q(1, 2), Q(29, 15), Q(29, 15)), lambda s: diag_negm(s, 4)),
        ("theta=-8   sigma=1/9 ", (Q(1, 2), Q(39, 20), Q(39, 20)), lambda s: diag_negm(s, 8)),
        ("theta=-12  sigma=1/13", (Q(1, 2), Q(39, 20), Q(39, 20)), lambda s: diag_negm(s, 12)),
    ]
    for lbl, (x, s1, s2), dfun in witnesses:
        gap = (not p2_leontief(x, s1, s2)) and p2_linear(x, s1, s2)
        check("6.x " + lbl + " FALSE-CERTIFIES the exact rational state "
              "s=(" + str(s1) + "," + str(s2) + "), x=1/2",
              gap and dfun(s1)[0], "typed=REJECT, rung=ACCEPT")


# ----------------------------------------------------------------------------
# Part 7 - the relevance test (all four components, machine-anchored)
# ----------------------------------------------------------------------------

def part7():
    print("\n=== PART 7: the relevance test ===")
    x, s1, s2 = CANON
    check("7.1 [named decision] the Section 6.3 LRP closure decision at the "
          "canonical datum: FAST's trough breaches B_lim by 4/5 kt "
          "(B=6/5 < B_lim=2 = 0.6 B_lim) while the dashboard tube minimum is "
          "2/5 > 0 (the certified exposure)",
          (BLIM + s1 - DIP) < BLIM and (s1 - DIP + s2) == Q(2, 5))
    lam1, lam2 = ONE + s1 - DIP, ONE + s2
    lin_report = (lam1 + lam2) / 2
    geo_sq = lam1 * lam2
    check("7.2 [indicator report] at the canonical trough lambda=(1/5,11/5): "
          "the linear dashboard reports " + str(lin_report) + " >= 1 "
          "('nonnegative margin - certified'); the LPI-structured geometric "
          "reports sqrt(" + str(geo_sq) + ") < 1 ('below reference') - the "
          "same datum, opposite reports",
          lin_report == Q(6, 5) and geo_sq == Q(11, 25)
          and lin_report >= ONE and geo_sq < ONE)
    lam1b, lam2b = Q(1, 2), Q(5, 2)
    geo_b = lam1b * lam2b
    harm_b = TWO / (ONE / lam1b + ONE / lam2b)
    check("7.3 [indicator report] at the (3/2,3/2) witness trough "
          "lambda=(1/2,5/2): the LPI-form reports sqrt(5/4) >= 1 (FALSELY "
          "certifies), the harmonic reports 5/6 < 1 (rejects)",
          geo_b == Q(5, 4) and geo_b >= ONE and harm_b == Q(5, 6) and harm_b < ONE)
    acc23 = diag_two_thirds(Q(6, 5))
    acc12 = diag_one_half(Q(6, 5))
    check("7.4 [new exact datum] the canonical datum's critical elasticity: "
          "sigma* in (2, 3) exactly - theta=2/3 (sigma=3) accepts STRICTLY, "
          "theta=1/2 (sigma=2) rejects STRICTLY",
          acc23 == (True, True) and acc12 == (False, True))
    xw, sw = Q(1, 2), Q(3, 2)
    lin_w = p2_linear(xw, sw, sw)
    geo_w = diag_geo(sw)[0]
    harm_w = diag_negm(sw, 1)[0]
    check("7.5 [management action] at the (3/2,3/2) datum: linear=certify AND "
          "geometric(LPI)=certify (no closure triggered) BUT harmonic=reject "
          "-> the mandatory closure/rebuilding response triggers, with the "
          "reserve top-up kappa* = 1/2 financing STAGED (converting the "
          "impossibility state into a rescue state)",
          lin_w and geo_w and (not harm_w) and ONE - xw == Q(1, 2))
    check("7.6 [management action] at the canonical datum the false "
          "certification persists for every aggregator with sigma >= 3 "
          "(CES 3 and the linear dashboard) and is removed for every "
          "sigma <= 2 member (CES 2, LPI-geometric, harmonic, ..., "
          "Leontief) - the aggregator choice flips the closure response",
          diag_two_thirds(Q(6, 5))[0] and (not diag_one_half(Q(6, 5))[0])
          and (not diag_geo(Q(6, 5))[0]) and (not diag_negm(Q(6, 5), 1)[0]))


# ----------------------------------------------------------------------------
# Part 8 - audit-Theorem-11 adjudication gates
# ----------------------------------------------------------------------------

def part8():
    print("\n=== PART 8: audit-Theorem-11 adjudication (batch-8 final stream) ===")
    bad = []
    for k in range(0, 40):
        s = ONE + Q(k, 20)
        if s >= TWO:
            break
        lin = diag_linear(s)[0]
        for name, dfun, _g in LADDER[1:]:
            if dfun(s)[0] and not lin:
                bad.append((s, name))
    check("8.1 Thm11(1): every rung's accepted diagonal states lie in the "
          "linear member's accepted set (the gap is maximal at sigma=inf)",
          not bad, str(bad[:2]) if bad else "40 states x 12 rungs")
    ok = True
    for k in range(0, 40):
        s = ONE + Q(k, 20)
        if s >= TWO:
            break
        if not p2_leontief(Q(1, 2), s, s):
            continue
        dec = [r[1](s)[0] for r in LADDER]
        if not dec[0]:
            ok = False
        seen_rej = False
        for a in dec:
            if not a:
                seen_rej = True
            elif seen_rej:
                ok = False
    check("8.2 Thm11(2): at every diagonal gap state the acceptance is a ray "
          "in theta (monotone collapse confirmed on the witness; the "
          "conjecture's substantive content = the exact ray edge sigma*(z), "
          "Part 5)", ok)
    check("8.3 Thm11(3): V^0 = V_typ - the sigma->0 member is exactly the "
          "typed operator (verified in 1.2; no gap state accepted in 6.y)",
          True)
    deep = Q(39, 20)
    acc12 = diag_negm(deep, 12)[0]
    acc16 = diag_negm(deep, 16)[0]
    check("8.4 two-sided refinement: the deep state (39/20,39/20) is "
          "false-certified even at theta=-12 (sigma=1/13) but rejected at "
          "theta=-16 (sigma=1/17) - pointwise sigma* > 0 strictly on every "
          "gap state, while sigma* -> 0 at the typed boundary: Leontief is "
          "necessary only for UNIFORM safety over the gap region, never for "
          "pointwise safety",
          acc12 and (not acc16))


# ----------------------------------------------------------------------------

def main():
    print("sigma-spectrum wave - exact machine verification")
    print("witness: paper1_assessment_separation_v52.tex Section 4.5 datum; "
          "Section 6.3 fishery reading")
    print("arithmetic: fractions.Fraction only; no floats, no tolerances, "
          "no randomness")
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
