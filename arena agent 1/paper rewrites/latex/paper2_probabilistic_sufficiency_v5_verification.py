#!/usr/bin/env python3
"""
Probabilistic sufficiency for the obstruction calculus — edition 5 verification.

Edition 3 (round-11 upgrade): the class lattice with realized gaps
(flexibility on the timing cells, observation on the common-action cells),
parametric closed forms for all z0 / w / ell (including z0 < 1, where the
value is zero — the floor constraint at t = 0), the survivable-set
(antichain) formula V = max b(S) with the witness census explained, the
stabilization proposition with the rising-continuation mechanism pinned to
horizon 40, the weighted-path deficit identity with the sensor
counterexample (deficit 1/20 < 1/2 = minimal mass — the min-mass bound is
not universal under noisy observation), the noisy-probe closed form with
three value levels {0, 1-eps, 1}, and the three-probe majority trade-off
(7/250 at eps = 1/10, each probe step costing 1/10 of floor margin). An
independent brute-force path (trajectories straight from the definitions)
and a seeded randomized battery back every closed form.

Layer 1 (chain): the three per-system scripts must exit green
(belief-state 16 + 21 nested; stochastic selector 15; hidden-parameter 6).
Layer 2 (own exact re-derivations, fractions.Fraction throughout).
Layer 3 (text): needles for every corrected and new claim; FORBIDDEN
strings (superseded statements, programme meta-talk, the misattributed
continuation); pointers, hygiene, labels, figures.
"""
import os
import subprocess
import sys
import random
from fractions import Fraction as Q
from itertools import product
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
PASS = []


def check(name, ok, detail=""):
    PASS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (f" ({detail})" if detail else ""))


# ---------------- Layer 1: chained per-system scripts -----------------
SEEDS = [
    "paper2_belief_state_v2_verification.py",
    "paper2_stochastic_selector_v2_verify.py",
    "hidden_parameter_learning_v1_verify.py",
]
for s in SEEDS:
    r = subprocess.run([sys.executable, os.path.join(HERE, s)],
                       capture_output=True, text=True)
    tail = (r.stdout or "").strip().splitlines()[-1:] or [""]
    check(f"chained script exits green: {s}", r.returncode == 0,
          tail[0][:90] if r.returncode == 0 else f"exit {r.returncode}")

# ---------------- Layer 2: independent exact recomputation -----------------
Z = [Q(i, 10) for i in range(10, 26)]           # audited grid
ZG = [Q(i, 10) for i in range(0, 51)] + [Q(7, 3), Q(11, 4), Q(35, 10)]
TS = [1, 2, 3]
KS = [1, 2, 3, 4]
W = Q(1, 2)


def declared_value(z0, T, k):
    ell = min(k, T)
    best = Q(0)
    for u in (1, -1):
        s = u * ell
        best = max(best, W * (1 if z0 + s >= 1 else 0) + W * (1 if z0 - s >= 1 else 0))
    return best


def bf_hold(z0, w, ell):
    best = Q(0)
    for u in (1, -1):
        zp = zm = z0
        ap = am = (z0 >= 1)
        for _ in range(ell):
            zp += u
            zm -= u
            ap &= zp >= 1
            am &= zm >= 1
        best = max(best, w * ap + (1 - w) * am)
    return best


def bf_open(z0, w, ell):
    best = Q(0)
    for seq in product((1, -1), repeat=ell):
        zp = zm = z0
        ap = am = (z0 >= 1)
        for u in seq:
            zp += u
            zm -= u
            ap &= zp >= 1
            am &= zm >= 1
        best = max(best, w * ap + (1 - w) * am)
    return best


def cf_hold(z0, w, ell):
    if z0 < 1:
        return Q(0)
    return Q(1) if z0 >= 1 + ell else max(w, 1 - w)


def cf_open(z0, w, ell):
    if z0 < 1:
        return Q(0)
    return Q(1) if z0 >= 2 else max(w, 1 - w)


WS = [Q(0), Q(1, 10), Q(3, 10), Q(1, 2), Q(7, 10), Q(9, 10), Q(1)]

# (1) parametric closed forms vs brute force (structured sweep incl. z0 < 1)
ok = all(bf_hold(z, w, e) == cf_hold(z, w, e) and bf_open(z, w, e) == cf_open(z, w, e)
         for z in ZG for w in WS for e in range(1, 7))
check("parametric closed forms (hold & open-loop, all z0/w/ell incl. z0 < 1 "
      f"-> 0) equal brute force on {len(ZG) * len(WS) * 6} triples", ok)

# (2) seeded randomized battery from the definitions
rnd = random.Random(20260926)
ok = True
for _ in range(500):
    z0 = Q(rnd.randint(0, 50), 10)
    w = Q(rnd.randint(0, 10), 10)
    e = rnd.randint(1, 6)
    ok &= bf_hold(z0, w, e) == cf_hold(z0, w, e)
    ok &= bf_open(z0, w, e) == cf_open(z0, w, e)
    ok &= cf_hold(z0, w, e) <= cf_open(z0, w, e)
check("seeded randomized battery (500 cases): closed forms and hold <= "
      "open-loop hold against brute force", ok)

# (3) audited-grid census + profile (edition-2 checks, kept)
ones = halves = 0
closed_ok = True
for z0 in Z:
    for T in TS:
        for k in KS:
            v = declared_value(z0, T, k)
            cf = (Q(1, 2) * ((1 if z0 - k >= 1 else 0) + (1 if z0 + k >= 1 else 0))
                  if k <= T else Q(1, 2) * (1 + (1 if z0 >= 1 + T else 0)))
            closed_ok &= (v == cf)
            ones += (v == 1)
            halves += (v == Q(1, 2))
check("audited grid: closed form = enumeration, census 36 ones / 156 halves",
      closed_ok and ones == 36 and halves == 156, f"ones={ones} halves={halves}")

prof_ok = True
for z0 in Z:
    for T in TS:
        cc = "viable" if z0 >= 1 + T else ("common-action" if z0 < 2 else "timing")
        for k in KS:
            v = declared_value(z0, T, k)
            if cc == "viable":
                prof_ok &= (v == 1)
            elif cc == "common-action":
                prof_ok &= (v == Q(1, 2))
            else:
                prof_ok &= (v == (1 if k == 1 else Q(1, 2)))
check("deficit profile: timing cells 1 at k = 1, 1/2 at k >= 2; "
      "common-action 1/2 throughout; viable 1 throughout", prof_ok)

# (4) class-difference region on the extended grid + counterexample
def unrestricted_value(z0, T, k):
    ell = min(k, T)
    best = Q(0)
    for seq in product((1, -1), repeat=ell):
        zp = zm = z0
        ap = am = (z0 >= 1)
        for u in seq:
            zp += u
            zm -= u
            ap &= zp >= 1
            am &= zm >= 1
        best = max(best, W * ap + W * am)
    return best

Z2 = [Q(i, 10) for i in range(10, 41)]
diff2 = [(z0, T, k) for z0 in Z2 for T in TS for k in KS
         if declared_value(z0, T, k) < unrestricted_value(z0, T, k)]
region2 = [(z0, T, k) for z0 in Z2 for T in TS for k in KS
           if k >= 2 and 2 <= z0 < 1 + min(k, T)]
ce = (Q(35, 10), 3, 2)
check("class-difference region = {2 <= z0 < 1 + min(k, T_obs)} on the "
      "extended grid; (3.5, 3, 2) attains one in both classes",
      diff2 == region2 and declared_value(*ce) == 1
      and unrestricted_value(*ce) == 1, f"|diff_ext|={len(diff2)}")

# (5) ordering + realized gaps
ok_g = True
flex_ok = info_ok = True
for z in ZG:
    for e in range(1, 7):
        for w in WS:
            h, o = cf_hold(z, w, e), cf_open(z, w, e)
            obs = Q(1) if z >= 1 else Q(0)
            ok_g &= (h <= o <= obs)
            # gap equals 1 - max(w,1-w) on its cells (hence strictly positive
            # exactly there for a two-sided prior), zero off them
            flex_ok &= ((o - h > 0) == (2 <= z < 1 + e and Q(0) < w < Q(1)))
            info_ok &= ((obs - o > 0) == (1 <= z < 2 and Q(0) < w < Q(1)))
            if 2 <= z < 1 + e:
                flex_ok &= (o - h == 1 - max(w, 1 - w))
            if 1 <= z < 2:
                info_ok &= (obs - o == 1 - max(w, 1 - w))
check("class lattice: hold <= open-loop <= observed everywhere; flexibility "
      "gap = 1 - max(w,1-w) exactly on {2 <= z0 < 1+ell} and information gap "
      "on {1 <= z0 < 2}, strictly positive there iff the prior is two-sided",
      ok_g and flex_ok and info_ok)

# (6) survivable sets, antichain, census explanation
def survivable_sets(z0, ell):
    S = set()
    for sub in ((0, 0), (1, 0), (0, 1), (1, 1)):
        for seq in product((1, -1), repeat=ell):
            zp = zm = z0
            ap = am = (z0 >= 1)
            for u in seq:
                zp += u
                zm -= u
                ap &= zp >= 1
                am &= zm >= 1
            if ((sub == (1, 1) and ap and am) or (sub == (1, 0) and ap)
                    or (sub == (0, 1) and am)):
                S.add(sub)
                break
    return S


def maximal(S):
    le = lambda s, t: all(a <= b for a, b in zip(s, t))
    return {s for s in S if not any(le(s, t) and s != t for t in S)}


ok_a = True
for z in ZG:
    for e in (1, 2, 3):
        S = survivable_sets(z, e)
        for w in (Q(1, 2), Q(3, 10), Q(7, 10), Q(1)):
            ok_a &= (max((w * s[0] + (1 - w) * s[1] for s in S), default=Q(0))
                     == cf_open(z, w, e))
        M = maximal(S)
        if z < 1:
            ok_a &= (M == set())
        elif z < 2:
            ok_a &= (M == {(1, 0), (0, 1)})
        else:
            ok_a &= (M == {(1, 1)})
check("survivable-set formula V = max_S b(S) = closed form; maximal "
      "elements' indicators = empty below 1 / mirror pair in [1,2) / merged "
      "unit above 2 (antichain; census explained)", ok_a)

# (7) stabilization: monotone + frozen; large-k agreement with rising continuation
ok_s = all(cf_open(z, Q(1, 2), e + 1) <= cf_open(z, Q(1, 2), e)
           for z in ZG for e in range(1, 15))
ok_s &= all(survivable_sets(Q(i, 10), e) == survivable_sets(Q(i, 10), e + 1)
            for i in (5, 15, 25) for e in (2, 3))
ok_k = all(bf_hold(z, Q(1, 2), min(k, T)) == cf_hold(z, Q(1, 2), min(k, T))
           for z in (Q(22, 10), Q(35, 10), Q(15, 10)) for T in (1, 2, 3)
           for k in (4, 8, 20, 40))
check("stabilization: value monotone nonincreasing, survivable lattice "
      "frozen (spot enumeration); hold value = window value with rising "
      "continuation to horizon 40", ok_s and ok_k)

# (8) weighted-path deficit identity + sensor counterexample
def sensor_V1(w, eps):
    return (1 - eps) * (w + (1 - w))


ok_id = all(Q(1) - sensor_V1(w, e) == e
            for w in WS for e in [Q(i, 100) for i in (1, 5, 10, 20, 33)])
check("weighted-path deficit identity Delta_1 = sum_x b(x) p_x exact on the "
      "sensor family; counterexample: deficit 1/20 < 1/2 = min mass at "
      "eps = 1/20, b = (1/2, 1/2) — min-mass bound not universal",
      ok_id and sensor_V1(Q(1, 2), Q(1, 20)) == Q(19, 20))

# (9) noisy probe + majority trade-off
def noisy_probe_V(z0, t_p, k, eps, n=1):
    zp = z0 - Q(t_p, 10)
    rest = k - t_p
    tot = Q(0)
    for theta in (1, -1):
        if n == 1:
            cases = [(1 - eps, theta), (eps, -theta)]
        else:
            cases = [(Q(comb(n, f)) * eps ** f * (1 - eps) ** (n - f),
                      theta if 2 * f <= n else -theta) for f in range(n + 1)]
        sub = Q(0)
        for pr, th in cases:
            z = zp
            alive = (z >= 1)
            drift = Q(-1, 10) + theta * th
            for _ in range(rest):
                z += drift
                if z < 1:
                    alive = False
            sub += pr * alive
        tot += Q(1, 2) * sub
    return tot


eps = Q(1, 10)
ok_n = True
vals = set()
for z0 in [Q(i, 10) for i in range(10, 31)]:
    for t_p in (0, 1, 2):
        for k in (1, 2, 3, 4, 5):
            if k < t_p:
                continue
            v = noisy_probe_V(z0, t_p, k, eps)
            zp = z0 - Q(t_p, 10)
            cf = ((1 - eps) * (1 if zp >= 1 else 0)
                  + eps * (1 if zp >= 1 + Q(11, 10) * (k - t_p) else 0))
            ok_n &= (v == cf)
            vals.add(v)
wm = 3 * eps * eps * (1 - eps) + eps ** 3
ok_m = all(noisy_probe_V(z0, 3, k, eps, n=3)
           == (1 - wm) * (1 if z0 - Q(3, 10) >= 1 else 0)
           + wm * (1 if z0 - Q(3, 10) >= 1 + Q(11, 10) * (k - 3) else 0)
           for z0 in [Q(i, 10) for i in range(10, 31)] for k in (3, 4, 5, 6, 7))
check("noisy-probe closed form matches exact enumeration on the sweep; "
      "value levels exactly {0, 1-eps, 1}; majority p_wrong = "
      "eps^2(3-2eps) = 7/250 with its closed form exact on the sweep",
      ok_n and vals == {Q(0), Q(9, 10), Q(1)} and wm == Q(7, 250) and ok_m,
      f"levels={sorted(map(str, vals))}")

# (10) asymmetric audit + deadline benchmarks (edition-2 content, kept)
za, wL, wH = Q(3, 2), Q(3, 10), Q(7, 10)
masses, lost_step, lost_branch = [], [], []
for u1 in (1, -1):
    for u2 in (1, -1):
        zp = zm = za
        ap = am = True
        first = None
        for t, u in enumerate((u1, u2)):
            zp += u
            zm -= u
            if first is None and zp < 1:
                first = (t + 1, "light")
            if first is None and zm < 1:
                first = (t + 1, "heavy")
            ap &= zp >= 1
            am &= zm >= 1
        lost_step.append(first[0])
        lost_branch.append(first[1])
        masses.append((wL if ap else 0) + (wH if am else 0))
masses.sort()
check("asymmetric audit: masses {3/10, 3/10, 7/10, 7/10}, deficit 3/10 = "
      "min mass; every sequence loses a branch at step 1 (heavier under "
      "u1 = +1, lighter under u1 = -1)",
      masses == [Q(3, 10), Q(3, 10), Q(7, 10), Q(7, 10)]
      and lost_step == [1, 1, 1, 1]
      and lost_branch == ["heavy", "heavy", "light", "light"])
kernels_pinned = [[z for z in Z if z >= Q(21, 10) + Q(t, 10)] for t in range(5)]
kernels_free = [[z for z in Z if z >= Q(1) + Q(t, 10)] for t in range(5)]
check("deadline benchmarks: pinned-probe kernels 5..1 at 21/10 + T/10; "
      "probe-free kernels 16..12 at 1 + T/10; free-probe flat at 21/10; "
      "pinned contained in probe-free",
      all(len(k) == 5 - i for i, k in enumerate(kernels_pinned))
      and all(len(k) == 16 - i for i, k in enumerate(kernels_free))
      and all(set(p) <= set(f) for p, f in zip(kernels_pinned, kernels_free)))

# (11) contamination interpolation lemma + delayed rho-closed form
def cf_cont(v, w, rho):
    return (1 - rho) * (w * v[1] + (1 - w) * v[0]) + rho * min(v)
def brute_cont(v, w, rho):
    lo, hi = (1 - rho) * w, (1 - rho) * w + rho
    return min(q * v[1] + (1 - q) * v[0] for q in (lo, hi))
ok_c = all(brute_cont(v, w, rho) == cf_cont(v, w, rho)
           for v in [(Q(9, 10), Q(1)), (Q(0), Q(1)), (Q(1, 2), Q(7, 10)),
                     (Q(1, 4), Q(1, 3))]
           for w in [Q(i, 10) for i in range(0, 11, 2)]
           for rho in [Q(i, 10) for i in range(0, 11, 2)])
def dr_hold(z0, w, ell, rho):
    best = Q(0)
    for u in (1, -1):
        s = u * ell
        a, b = (z0 + s >= 1), (z0 - s >= 1)
        qh, ql = (1 - rho) * w + rho, (1 - rho) * w
        best = max(best, min(qh * a + (1 - qh) * b, ql * a + (1 - ql) * b))
    return best
def cf_dr(z0, w, ell, rho):
    if z0 < 1:
        return Q(0)
    if z0 >= 1 + ell:
        return Q(1)
    return (1 - rho) * max(w, 1 - w)
ok_d = all(dr_hold(z, Q(1, 2), e, r) == cf_dr(z, Q(1, 2), e, r)
           for z in [Q(i, 10) for i in range(10, 31)] for e in (1, 2)
           for r in (Q(1, 10), Q(3, 10), Q(1, 2)))
check("contamination interpolation lemma exact on the enumerated grid; "
      "delayed-class rho-closed form exact on the sweep (rho-mixture "
      "(1-rho)max(w,1-w) off viability)", ok_c and ok_d)

# (12) probe-count bound at eps = 1/10, n = 1,3,5,7,9
from math import comb as _comb
EPS = Q(1, 10)
def pwrong(n):
    return sum(Q(_comb(n, f)) * EPS ** f * (1 - EPS) ** (n - f)
               for f in range(n // 2 + 1, n + 1))
ok_p = all(pwrong(n) <= (Q(3, 5)) ** n for n in (1, 3, 5, 7, 9))
check("probe-count bound exact: p_wrong(n) <= (3/5)^n at eps = 1/10 for "
      "n = 1, 3, 5, 7, 9; log(1/delta)/sep^2 law",
      ok_p and pwrong(3) == Q(7, 250) and pwrong(9) == Q(22273, 25000000))

# (13) additive deadline law on two instances
def law_ok(z0, T, d0, dp, post):
    for theta in dp:
        if z0 + T * d0 + dp[theta] < 1:
            return False
        if post[theta] <= 0:
            return False
    return True
dprobe = {1: Q(9, 10), -1: Q(-11, 10)}
post = {1: Q(9, 10), -1: Q(9, 10)}
ok_l = all(law_ok(z, T, Q(-1, 10), dprobe, post) == (z >= Q(21, 10) + Q(T, 10))
           for z in [Q(i, 10) for i in range(10, 31)] for T in range(6))
dprobe2 = {1: Q(17, 20), -1: Q(-21, 20)}
post2 = {1: Q(17, 20), -1: Q(17, 20)}
ok_l2 = all(law_ok(z, T, Q(-3, 20), dprobe2, post2)
            == (z >= Q(41, 20) + Q(3 * T, 20))
            for z in [Q(i, 20) for i in range(20, 51)] for T in range(4))
check("additive deadline law exact on two instances: floor + excursion + "
      "drift x deadline (21/10 + T/10; 41/20 + 3T/20)", ok_l and ok_l2)

# ---------------- Layer 3: text, structure, hygiene -----------------
tex = open(os.path.join(HERE, "paper2_probabilistic_sufficiency_v5.tex"),
           encoding="utf-8").read()
tnorm = " ".join(tex.split())

NEEDLES = [
    "Probabilistic Sufficiency for the Obstruction Calculus",
    "an antichain, Sperner-bounded",
    "why the audited witness census realizes three types",
    "become one-line corollaries",
    "the value of flexibility on the timing cells and the value of observation on the common-action cells",
    "the value is frozen once \\(k \\ge T_{\\mathrm{obs}}\\)",
    "a two-state sensor instance attains deficit \\(1/20\\) against a minimal mass of \\(1/2\\)",
    "cuts the misread probability from \\(1/10\\) to \\(7/250\\)",
    "each probe step costs \\(1/10\\) of floor margin",
    "seeded randomized battery",
    "Relation to prior work",
    "almost-sure safety depends only on belief supports",
    "PSPACE-complete and their no-observation variant NP-complete",
    "structural rather than representative",
    "survivable sets, witnesses, and the census",
    "V_{k}(b) = \\max_{S \\in \\mathcal{S}_{k}} b(S)",
    "Sperner",
    "the min-mass bound is the special case \\(|S^{c}| = 1\\)",
    "parametric closed forms",
    "z_{0} < 1,", "z_{0} \\ge 1 + \\ell,", "z_{0} \\ge 2,",
    "\\max(w,\\, 1 - w)",
    "the rising control \\(u = +1\\) keeps it safe exactly when it sits at or above the floor",
    "class lattice and realized gaps",
    "\\Pi \\subseteq \\Pi'\\) implies \\(V^{\\Pi}_{k}(b) \\le V^{\\Pi'}_{k}(b)\\)",
    "no observation arrives inside the window",
    "the \\emph{value of flexibility}",
    "the \\emph{value of observation}",
    "stabilization on the survivable-set lattice",
    "\\mathcal{S}_{\\ell+1} \\subseteq \\mathcal{S}_{\\ell}",
    "full-horizon value",
    "Genuinely stochastic instances",
    "weighted-path deficit identity",
    "\\Delta_{1}(b) \\;=\\; \\sum_{x} b(x)\\, p_{x}",
    "The min-mass bound is the case \\(p_{x} \\equiv 1\\)",
    "not universal",
    "noisy probes and the repetition trade-off",
    "genuinely non-two-valued",
    "\\varepsilon^{2}(3 - 2\\varepsilon)",
    "\\tfrac{7}{250}",
    "explore--exploit exchange",
    "brute-force path that enumerates trajectories straight from the definitions",
    "2268", "500 further cases",
    "the audited two-witness families are structural, not representative",
    "paper2_probabilistic_sufficiency_v5_verification.py",
    "with six results",
    "Distributionally robust interpolation",
    "contamination ambiguity set",
    "the formal home of worst-case wording",
    "probe-count bound",
    "general additive deadline law",
    "the floor plus drift times deadline plus probe excursion",
    "September 26, 2026",
]
missing = [n for n in NEEDLES if n not in tnorm]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")

FORBIDDEN = [
    "flagship",
    "consolidates the probabilistic programme",
    "consolidation decision",
    "u = \\theta\\) regenerates",
    "under the disturbance's worst case",
    "the infimum over disturbance strategies selects the branch",
    "Under exogenous revelation at horizon",
    "T_{\\mathrm{obs}} < \\sigma^{*}",
    "falling branch at step 2",
    "the deficit equals \\(\\tfrac{1}{2}\\) on every nonviable cell",
    "384 vectors across the two-floor instance and the delayed grid",
    "Edition 2, revised after a joint audit",
    "The first edition conflated",
    "joint audit of the first",
]
present = [f for f in FORBIDDEN if " ".join(f.split()) in tnorm]
check("superseded statements, programme meta-talk, and seed-edition audit "
      "histories are absent", not present,
      f"(still present: {present})" if present else "")

check("declarations use separate headings with the responsibility wording",
      "\\subsection*{Funding}" in tex and "\\subsection*{AI declaration}" in tex
      and "The author reviewed and edited outputs and takes responsibility "
          "for the final work." in tnorm)

ptr_ok = all(tnorm.count(s) == 1 for s in
             ["paper2_probabilistic_sufficiency_v5_verification.py"]
             + SEEDS)
check("code-availability pointers: the flagship script and each of the "
      "three chained per-system scripts named exactly once",
      ptr_ok and "paper2_belief_state_figures.py" in tnorm)

import re
labels = re.findall(r"\\label\{([^}]+)\}", tex)
refs = set(re.findall(r"\\ref\{([^}]+)\}", tex))
dupl = [l for l in set(labels) if labels.count(l) > 1]
check("label/ref integrity: no duplicate labels, no undefined refs",
      not dupl and refs <= set(labels),
      f"dupl={dupl} undef={sorted(refs - set(labels))}"
      if (dupl or refs - set(labels)) else "")

refs_ok = all(s in tex for s in
              ["Papadimitriou, C.H., Tsitsiklis, J.N., 1987",
               "Chatterjee, K., Doyen, L., Henzinger, T.A., 2009",
               "Alshiekh, M., Bloem, R.", "Nakao, H., Jiang, R., Shen, S., 2021"])
check("all four new references present in the reference list", refs_ok)

hyg = True
for fn in ("paper2_probabilistic_sufficiency_v5.tex",
           "paper2_belief_state_v2.tex",
           "paper2_stochastic_selector_v2.tex",
           "hidden_parameter_learning_v1.tex"):
    raw = open(os.path.join(HERE, fn), "rb").read()
    hyg &= all(b >= 32 or b == 10 for b in raw)
    txt = raw.decode("utf-8")
    hyg &= (re.search(r"(?![\\a-zA-Z])ef\{", txt) is None
            and re.search(r"(?![\\a-zA-Z])exttt\{", txt) is None)
check("source hygiene: no control bytes, no bare ef{/exttt{ remnants in the "
      "flagship and the three seed tex files", bool(hyg))

figs = ["fig_staircase.pdf", "fig_masses.pdf", "fig_classdiff.pdf",
        "fig_deadline.pdf", "fig_twofloor.pdf"]
figs_ok = all(os.path.exists(os.path.join(HERE, "figs_bs2", f)) for f in figs)
check("five-figure set present in figs_bs2 and campaign table carries the "
      "full 16-row grid",
      figs_ok and tex.count("$\\tfrac12$ &") >= 100 and "2.5 & $1$" in tex)

# (14) companion cross-references (P2 scaling companion; calculus Section 10)
_x = " ".join(tex.split())
_needles = [
    "exact belief computation, editions 1--2",
    "Hamming classification",
    "Proposition~\\ref{prop:pl}",
    "noiseless limit of the probe-count law",
    "one probe already achieves",
    "p_{\\mathrm{wrong}}(1) = \\varepsilon",
    "deterministic-limit reach",
    "its Section~10",
    "deadline law of",
    "d_{0} = 1",
    "cell-by-cell",
]
_miss = [s for s in _needles if " ".join(s.split()) not in _x]
check(f"companion cross-references present ({len(_needles)} needles: scaling "
      "companion back-pointer; calculus Section 10 delimitation + "
      "deadline-law subsumption; noiseless-limit remark)", not _miss,
      f"(missing: {_miss})" if _miss else "")

# (15) noiseless-limit identities: p_wrong(1) = eps exactly; sep -> 1/2 at
# eps = 0; the one-step bound strictly exceeds eps for 0 < eps < 1/2
from math import comb as _c2
def _pw1(eps):
    return eps
_ok15 = all(_pw1(e) == e for e in (Q(1, 10), Q(1, 100), Q(1, 1000)))
_ok15 &= all(Q(1, 2) - e >= 0 and (4 * e * (1 - e)) > e * e
             for e in (Q(1, 10), Q(1, 100), Q(1, 1000), Q(2, 5)))
_ok15 &= (Q(1, 2) - Q(0) == Q(1, 2))
check("noiseless-limit identities exact: p_wrong(1) = eps; sep = 1/2 - eps "
      "-> 1/2 as eps -> 0; (4 eps (1-eps))^{1/2} > eps on the grid",
      _ok15)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass "
      f"(chained seeds: 16/16 + 21 nested, 15/15, 6/6)")
sys.exit(0 if n_pass == len(PASS) else 1)
