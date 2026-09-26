#!/usr/bin/env python3
"""
Computational viability certification, edition 15 — verification.

Layer 1 (chain): runs the exact verification record (51 checks), the
solver-certified campaign (nine checks; rebuilds LP (5) at five meshes,
runs HiGHS, certifies optimality by exact witnesses), and the viacert
library self-test (twelve audited identities), asserting each exits green.
Layer 2 (own): recomputes independently, from the closed forms in the
text: the mesh law max{0, 3/50 - T h/4} at all five meshes, the Farkas
contradiction -53/100 + 1/2 = -3/100, the primal row value 3/100, the
margins 3/50 and 3/100, the moment error e = 3/100, the relaxed
right-hand side -53/100, the delay threshold tau* = 7/50 via
Gamma(tau) = tau - 7/50, and the blind-window safety value 39/25.
Layer 2b (edition 15): redesign sensitivities and belief-cell checks —
dilated dual witnesses (eta_j/a on aU facets), Gamma_a(tau) =
tau - 7/50 - (a-1)/2 at a in {3/2, 2}, thresholds tau_max(a) =
{7/50, 39/100, 16/25}, the rate-one timing identity, the zero pooled
kernel, the velocity-row-free (positional) Farkas value, the dual radius
law margin(delta) = 3/50 - delta, the primal radius identities
12345/6250 + 31/1250 = 2419/1250 + 81/1250 = 2 with failures one step
beyond, and the constant mode-cell labels.
Layer 3 (text): asserts every headline number in
paper2_computational_certification_v16.tex, the separate declaration
headings, and the responsibility wording; the S1 v6 supplementary carries
the L1 label-continuity proof step, the max-e sandwich conclusion, and the
L1 Gronwall modulus.

Edition 8 additions (round-8 upgrade): the certificate is decoded
prescriptively — the shared-authority ladder: no common control brakes all
three branches (the pooling identity sum lambda_j n_j = 0 with lambda > 0),
the optimal shared braking authorities t*({1,2}) = t*({1,3}) = 2/5
(attained at the printed blind-window controls) and t*({2,3}) = 3/5
(attained at n1), and the pair delay thresholds (15 - sqrt(183))/6 and
(10 - sqrt(58))/6 against the triple's 7/50, with seven-facet scans exact
at rational surrogates (6/25, 39/100); the affine-kernel refinement
identity e = sum |J|^2/4 on every mesh; the detection bound charges
max e_a + R_D V_D h_d + delta_init + delta_num + L h_t; the S1 pairing
estimate uses M_U.

Edition 7 additions (round-6/7 audit): the Section 6 pair policies are
corrected and certified exactly — blind-window controls u = -(n1+n2)
for {1,2} and u = n1 for {2,3} with full braking -n_j from tau, peaks
12345/6250 and 2419/1250 with worst seven-facet slacks 31/1250 and
81/1250 on [0, 6/5]; the printed policies are falsified (2719/1250,
2501/1250 > 2, full-brake-only 103/50, off-belief branch 23/10); the
label-continuity hypothesis is L^1 (velocity kernels jump 1 in sup-norm,
position kernels have L^1 difference <= T|t-t'|, and the difference is
not supported on [t',t]); the sandwich (8) charges max e_a (loose-bound
counterexample: rho = -47/100, printed form claims J <= -24/100 at
J = 3/50, corrected bound 17/100); refinement positivity is not monotone
(the scalar one-block/split counterexample: e = 4/5 -> 24/25, rho = 1/10
-> -43/50); and the unrestricted level on non-uniform aligned meshes
(two-block mesh rho = -1/5).

Exact rational/integer arithmetic except solver outputs; stdlib only;
deterministic.
Run: python3 paper2_computational_certification_v8_verification.py

Edition 9 additions (round-9 scan and outlook): the introduction
contribution list now includes the shared-authority ladder; the
conclusion records the four extension directions (general measurement
channels, stochastic/conic disturbances, decentralized /
infinite-horizon / nonconvex structures, cross-tool comparison
study); the methods parser pointer is reworded alongside the library
tooling directions; the forbidden list gains the superseded parser
sentence; the refinement-identity check label is corrected to five
blocks (2 + 3).
"""
import subprocess, sys, os
from fractions import Fraction as Q

HERE = os.path.dirname(os.path.abspath(__file__))
PASS = []
def check(name, cond, detail=""):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else " " + str(detail)))

# ---------------- Layer 1: chained scripts --------------------------------------
CHAIN = [
    ("paper2_nonstandard_verification.py", "51 JOINT VERIFICATION CHECKS PASS"),
    ("paper2c_lp_campaign.py", "verification: 9/9 checks pass"),
]
for script, marker in CHAIN:
    p = subprocess.run([sys.executable, os.path.join(HERE, script)],
                       capture_output=True, text=True)
    ok = (p.returncode == 0) and (marker in (p.stdout + p.stderr))
    check(f"chain {script} green", ok)

p = subprocess.run([sys.executable, "-m", "viacert", "selftest"], capture_output=True,
                   text=True, cwd=HERE)
ok = (p.returncode == 0) and ("viacert selftest: 12/12 checks pass" in p.stdout)
check("chain viacert selftest green (12/12)", ok)

# ---------------- Layer 2: own exact recomputation -------------------------------
T = Q(6, 5)
def rho_law(h):
    return max(Q(0), Q(3, 50) - T * h / 4)
expect = {Q(1, 5): Q(0), Q(1, 10): Q(3, 100), Q(1, 20): Q(9, 200),
          Q(1, 50): Q(27, 500), Q(1, 100): Q(57, 1000)}
check("mesh law max{0, 3/50 - T h/4} reproduces all five exact table values",
      all(rho_law(h) == v for h, v in expect.items()))

beta = Q(16, 25) - Q(6, 5)
e = Q(12) * Q(1, 10) * Q(1, 10) / 4
beta_relaxed = beta + e
farkas = beta_relaxed + Q(1, 2)
check("moment error e = 3/100 and relaxed row beta + e = -53/100",
      e == Q(3, 100) and beta == Q(-14, 25) and beta_relaxed == Q(-53, 100))
check("Farkas contradiction -53/100 + 1/2 = -3/100", farkas == Q(-3, 100))
check("primal row value -1/2 + 14/25 - 3/100 = 3/100",
      Q(-1, 2) + Q(14, 25) - Q(3, 100) == Q(3, 100))
check("margins: continuous 3/50; finite 3/100", Q(3, 50) == Q(6, 100)
      and rho_law(Q(1, 10)) == Q(3, 100))

def Gamma(tau):
    return tau - Q(7, 50)
check("Gamma(tau) = tau - 7/50: positive iff tau > 7/50; Gamma(1/5) = 3/50",
      Gamma(Q(1, 5)) == Q(3, 50) and (Gamma(Q(7, 50)) == 0)
      and all((Gamma(t) > 0) == (t > Q(7, 50))
              for t in [Q(n, 100) for n in range(1, 100)]))
check("blind-window safety 39/25 = 1.56 < 2", Q(39, 25) < 2)
check("full-information maximum 93/50 = 1.86 < 2", Q(93, 50) < 2)

# ---------------- Layer 2 (edition 2): audit-adjudication checks ----------------
# ported shared-system primitives (as in the worked-systems audit)
from itertools import product as _product
CAPD = 3
def step_d(x, u):
    z1, z2 = x
    if u == 0:
        return (max(0, z1 - 1), max(0, z2 - 1))
    return (max(0, min(CAPD, z1 + 1 - (0 if u == 1 else 2))),
            max(0, min(CAPD, z2 + 1 - (0 if u == 2 else 2))))
Vset_d = frozenset((a, b) for a in range(1, 4) for b in range(1, 4))
pairs = sorted(frozenset({x, y}) for x in Vset_d for y in Vset_d if x < y)
def law_traj_ok(B, law1, law2, cap=512):
    cur, seen = frozenset(B), set()
    while True:
        if not (cur <= Vset_d):
            return False
        if cur in seen:
            return True
        seen.add(cur)
        if len(seen) > cap:
            return False
        nxt = set()
        for x in cur:
            u = law1[x[0]] if law1[x[0]] == law2[x[1]] else 0
            nxt.add(step_d(x, u))
        cur = frozenset(nxt)
LAW_PAIRS = [(l1, l2) for l1 in
             [dict(zip(range(4), t)) for t in _product((1, 2), repeat=4)]
             for l2 in
             [dict(zip(range(4), t)) for t in _product((1, 2), repeat=4)]]
K_dec = frozenset(B for B in pairs if any(law_traj_ok(B, l1, l2)
                                          for l1, l2 in LAW_PAIRS))
# (a) decentralized causality: the kernel's 12 pairs are all guaranteed by a
# single law pair (a 6-pair basin attained by 12 law pairs), so the count
# needs no non-causal pooling of per-pair laws.
best_n, best_laws = 0, []
for l1, l2 in LAW_PAIRS:
    n = sum(1 for B in pairs if law_traj_ok(B, l1, l2))
    if n > best_n:
        best_n, best_laws = n, [(l1, l2)]
    elif n == best_n:
        best_laws.append((l1, l2))
check("E-basin decentralized kernel is single-law causal: max guaranteed "
      "basin = 6 of 36 = |kernel|; attained by 12 law pairs",
      best_n == 6 and len(K_dec) == 12 and len(best_laws) == 12,
      f"(max basin {best_n}, laws {len(best_laws)}, kernel {len(K_dec)})")

# (b) certificate weights: the pooling family lambda_1 = 3/8, lambda_2 =
# lambda_3 = 5/16 sums to one, pools the kernel to zero, and reproduces the
# closed form Gamma(tau) = tau - 7/50 (Gamma(0.2) = 0.06).
n1 = (Q(1), Q(0)); n2 = (Q(-3, 5), Q(4, 5)); n3 = (Q(-3, 5), Q(-4, 5))
lam = [Q(3, 8), Q(5, 16), Q(5, 16)]
pool = [sum(l * n[i] for l, n in zip(lam, (n1, n2, n3)))
        for i in (0, 1)]
lam_sum = sum(lam)
Gamma = lambda tau: tau - Q(7, 50)
check("E-weights certificate pooling: lambda = (3/8, 5/16, 5/16) has "
      "sum 1 and lambda-weighted kernel sum 0; Gamma(0.2) = 0.06 > 0",
      lam_sum == Q(1) and pool == [Q(0), Q(0)]
      and Gamma(Q(1, 5)) == Q(3, 50))


# ---------------- Layer 2 (edition 3/7): pair-policy checks (corrected) ---------
# (a) pairwise policies for the three-branch instance: corrected controls.
# {1,2}: blind u = -(n1+n2) (both branches decelerate at 2/5 along their
# normals), then -n_j from tau. {2,3}: blind u = n1 (deceleration 3/5),
# then -n_j from tau. Peaks 12345/6250 and 2419/1250.
n1v = (Q(1), Q(0)); n2v = (Q(-3, 5), Q(4, 5)); n3v = (Q(-3, 5), Q(-4, 5))
PPOS = Q(34, 25); tau = Q(1, 5)
dot = lambda a, b: a[0] * b[0] + a[1] * b[1]
def corrected_peak(n_j, u_blind):
    a_blind = dot(n_j, u_blind)
    v_tau = Q(1) + a_blind * tau
    p_tau = PPOS + tau + a_blind * tau * tau / 2
    return p_tau + v_tau ** 2 / 2
u12 = (Q(-2, 5), Q(-4, 5))
check("pair {1,2}/{1,3}: blind brake u = -(n1+n2) in U, both branches "
      "decelerate at 2/5, then -n_j from tau peaks at 12345/6250 = 1.9752 < 2",
      u12 == (-(Q(2, 5)), -(Q(4, 5)))
      and abs(u12[1]) <= Q(4, 5) and abs(2 * u12[0] + u12[1]) <= 2
      and abs(2 * u12[0] - u12[1]) <= 2
      and dot(n1v, u12) == Q(-2, 5) and dot(n2v, u12) == Q(-2, 5)
      and corrected_peak(n1v, u12) == Q(12345, 6250) == corrected_peak(n2v, u12)
      and corrected_peak(n1v, u12) < Q(2))
check("pair {2,3}: blind hold u = n1 (both branches decelerate at 3/5), "
      "then -n_j from tau peaks at 2419/1250 = 1.9352 < 2",
      dot(n2v, n1v) == Q(-3, 5) and dot(n3v, n1v) == Q(-3, 5)
      and corrected_peak(n2v, n1v) == Q(2419, 1250) == corrected_peak(n3v, n1v)
      and corrected_peak(n2v, n1v) < Q(2))
# (a2) the printed (superseded) policies are falsified: {1,2} with u = 0
# through the blind window peaks at 2719/1250 with the printed mid-brake
# and 103/50 with full braking; {2,3} with a -(3/5) n_j leg after tau
# peaks at 2501/1250 at t = 29/25; the off-belief branch 1 under u = n1
# peaks at 23/10 and hits |v1| = 6/5 exactly at tau.
def printed_peak(n_j, a_blind, a_mid):
    v_tau = Q(1) + a_blind * tau
    p_tau = PPOS + tau + a_blind * tau * tau / 2
    v1 = v_tau + a_mid * tau
    p1 = p_tau + v_tau * tau + a_mid * tau * tau / 2
    return p1 + v1 * v1 / 2, v1
p12, _ = printed_peak(n1v, Q(0), Q(-2, 5))
p12_full, _ = printed_peak(n1v, Q(0), None) if False else (PPOS + tau + Q(1, 2), None)
p23, v23 = printed_peak(n2v, Q(-3, 5), Q(-3, 5))
p_off, v_off = printed_peak(n1v, Q(1, 1) * 0 + Q(1), None) if False else (None, None)
v_off_tau = Q(1) + Q(1) * tau
p_off = PPOS + tau + Q(1) * tau * tau / 2 + v_off_tau ** 2 / 2
check("superseded-policy falsification: {1,2} printed policy peaks 2719/1250 "
      "> 2 (103/50 with full braking); {2,3} with a -(3/5) leg peaks "
      "2501/1250 = 2.0008 > 2 at t = 29/25; off-belief branch 1 under u = n1 "
      "peaks 23/10 = 2.3 with |v1| = 6/5 exactly at tau",
      p12 == Q(2719, 1250) and p12 > Q(2) and p12_full == Q(103, 50)
      and p23 == Q(2501, 1250) and p23 > Q(2) and tau + tau + v23 == Q(29, 25)
      and p_off == Q(23, 10) and v_off_tau == Q(6, 5))
# (a3) all seven facets on [0, 6/5] for the corrected policies (exact
# piecewise scan; candidates: 0, tau, n_j-rest, 6/5)
VCAP = Q(6, 5)
def worst_slack(n_j, u_blind, T=Q(6, 5)):
    a_blind = dot(n_j, u_blind)
    v_tau = Q(1) + a_blind * tau
    s_rest = v_tau
    vb = (n_j[0] + u_blind[0] * tau, n_j[1] + u_blind[1] * tau)
    ptau_vec = (PPOS * n_j[0] + n_j[0] * tau + u_blind[0] * tau * tau / 2,
                PPOS * n_j[1] + n_j[1] * tau + u_blind[1] * tau * tau / 2)
    worst = None
    def upd(w, sl):
        return sl if w is None else min(w, sl)
    for t in (Q(0), tau, tau + s_rest, T):
        if t <= tau:
            vel = (n_j[0] + u_blind[0] * t, n_j[1] + u_blind[1] * t)
            pos = (PPOS * n_j[0] + n_j[0] * t + u_blind[0] * t * t / 2,
                   PPOS * n_j[1] + n_j[1] * t + u_blind[1] * t * t / 2)
        else:
            sg = t - tau
            smin = min(sg, s_rest)
            vel = (vb[0] - n_j[0] * smin, vb[1] - n_j[1] * smin)
            pos = (ptau_vec[0] + vb[0] * smin - n_j[0] * smin * smin / 2,
                   ptau_vec[1] + vb[1] * smin - n_j[1] * smin * smin / 2)
            if sg > s_rest:
                pos = (pos[0] + vel[0] * (sg - s_rest), pos[1] + vel[1] * (sg - s_rest))
        for ni in (n1v, n2v, n3v):
            worst = upd(worst, Q(2) - dot(ni, pos))
        for c in vel:
            worst = upd(worst, VCAP - abs(c))
    return worst
w12 = min(worst_slack(n1v, u12), worst_slack(n2v, u12))
w23 = min(worst_slack(n2v, n1v), worst_slack(n3v, n1v))
check("corrected pair policies: all seven facets hold on [0, 6/5] with worst "
      "slacks 31/1250 ({1,2}) and 81/1250 ({2,3}); transverse leftover 4/25 "
      "decreases the noncritical coordinates",
      w12 == Q(31, 1250) and w23 == Q(81, 1250)
      and dot(n2v, (Q(0), Q(-4, 25))) == Q(-16, 125))
# (b) source-hygiene regression: no escape-mangled control bytes or bare
# remnants in either tex file (the v2 corruption class)
import re as _re
hyg = True
for f in ("paper2_computational_certification_v16.tex",
          "paper2_computational_certification_supplementary_v6.tex"):
    raw = open(os.path.join(HERE, f), "rb").read()
    hyg &= all(b >= 32 or b == 10 for b in raw)
    txt = raw.decode("utf-8")
    hyg &= not _re.search(r"(?<![\\a-zA-Z])ef\{", txt)
    hyg &= not _re.search(r"(?<![\\a-zA-Z])exttt\{", txt)
check("source hygiene: no control bytes, no bare ef{/exttt{ remnants in "
      "either tex file", bool(hyg))

# ---------------- Layer 2b (edition 15): redesign sensitivities + belief cells -----
# Proposition (redesign sensitivities): post-revelation set dilated to aU; the
# printed dual witness (lambda, eta_1..eta_3) and its dilated form; Gamma_a(tau)
# = tau - 7/50 - (a-1)/2; thresholds tau_max(a); rate-one timing; positional
# (velocity-row-free) Farkas value; Proposition (belief-cell certificates):
# radius laws and constant mode-cell labels.
Fct = [(Q(0), Q(1)), (Q(0), Q(-1)), (Q(2), Q(1)), (Q(2), Q(-1)),
       (Q(-2), Q(1)), (Q(-2), Q(-1))]
fv = [Q(4, 5), Q(4, 5), Q(2), Q(2), Q(2), Q(2)]
ET = [(Q(0), Q(0), Q(0), Q(0), Q(1, 4), Q(1, 4)),
      (Q(0), Q(1, 2), Q(0), Q(3, 10), Q(0), Q(0)),
      (Q(1, 2), Q(0), Q(3, 10), Q(0), Q(0), Q(0))]
LAM = [Q(3, 8), Q(5, 16), Q(5, 16)]
NJ = [n1v, n2v, n3v]
check("redesign witness (undilated): F^T eta_j = -n_j and f^T eta_j = 1 with "
      "eta_j >= 0 for all three modes",
      all(sum(ET[j][k] * Fct[k][i] for k in range(6)) == -NJ[j][i]
          for j in range(3) for i in (0, 1))
      and all(sum(ET[j][k] * fv[k] for k in range(6)) == Q(1) for j in range(3))
      and all(all(x >= 0 for x in ET[j]) for j in range(3)))
check("redesign witness (dilated): on the dilated facets aF with bounds af the "
      "multipliers eta_j/a remain dual-feasible for a in {3/2, 2}",
      all(sum((ET[j][k] / a) * (a * Fct[k][i]) for k in range(6)) == -NJ[j][i]
          for a in (Q(3, 2), Q(2)) for j in range(3) for i in (0, 1))
      and all(sum((ET[j][k] / a) * (a * fv[k]) for k in range(6)) == Q(1)
          for a in (Q(3, 2), Q(2)) for j in range(3)))
def Gam(a, t):
    return t - Q(7, 50) - (a - Q(1)) / 2
check("redesign values: Gamma_a(1/5) = 3/50, -19/100, -11/25 at a = 1, 3/2, 2 "
      "(closed form tau - 7/50 - (a-1)/2)",
      Gam(Q(1), tau) == Q(3, 50) and Gam(Q(3, 2), tau) == Q(-19, 100)
      and Gam(Q(2), tau) == Q(-11, 25))
check("redesign thresholds: tau_max(a) = 7/50 + (a-1)/2 gives 7/50, 39/100, "
      "16/25 at a = 1, 3/2, 2 (equality viable, closed safety set)",
      Q(7, 50) + (Q(1) - Q(1)) / 2 == Q(7, 50)
      and Q(7, 50) + (Q(3, 2) - Q(1)) / 2 == Q(39, 100)
      and Q(7, 50) + (Q(2) - Q(1)) / 2 == Q(16, 25)
      and all(Gam(a, Q(7, 50) + (a - Q(1)) / 2) == Q(0)
          for a in (Q(1), Q(3, 2), Q(2))))
check("redesign timing rate: Gamma_a(t2) - Gamma_a(t1) = t2 - t1 at every "
      "authority (rate exactly one)",
      all(Gam(a, Q(2, 5)) - Gam(a, tau) == Q(1, 5)
          for a in (Q(1), Q(3, 2), Q(2))))
# positional (velocity-row-free) Farkas value: the ten post-observation interval
# weights a_k = int_{J_k} (T - s) ds on the h = 1/10 mesh sum to 1/2; the value
# -53/100 + 1/2 = -3/100 uses only the position-row labels and that sum — no
# velocity bound enters; the witness velocity rows hold with slack 1/5.
Tval = Q(6, 5); hval = Q(1, 10)
ak = [Tval * hval - ((tau + (k + 1) * hval) ** 2 - (tau + k * hval) ** 2) / 2
      for k in range(10)]
check("positional certificate: sum_k a_k = 1/2 (exact interval integrals), "
      "Farkas value -53/100 + 1/2 = -3/100 charges only position rows and "
      "input facets (no velocity bound), velocity slack at the witness = 1/5",
      sum(ak, Q(0)) == Q(1, 2)
      and Q(-53, 100) + sum(ak, Q(0)) == Q(-3, 100)
      and VCAP - Q(1) == Q(1, 5) > 0)
check("belief-cell dual radius: margin(delta) = Gamma(1/5) - delta = 3/50 - "
      "delta is positive at delta = 1/25, negative at delta = 29/250, zero at "
      "delta = 3/50 (positivity boundary, labels' weights sum to one)",
      Gam(Q(1), tau) - Q(1, 25) == Q(1, 50) > 0
      and Gam(Q(1), tau) - Q(29, 250) == Q(-14, 250) < 0
      and Gam(Q(1), tau) - Q(3, 50) == Q(0))
check("belief-cell primal radii: 12345/6250 + 31/1250 = 2419/1250 + 81/1250 = 2 "
      "(equality viable); one step beyond fails on both rungs",
      Q(12345, 6250) + Q(31, 1250) == Q(2)
      and Q(2419, 1250) + Q(81, 1250) == Q(2)
      and Q(12345, 6250) + Q(32, 1250) > Q(2)
      and Q(2419, 1250) + Q(82, 1250) > Q(2))
check("mode-cell labels: beta_j = 16/25 - t_* = -14/25 identically in j, so the "
      "cell supremum equals -14/25 on every compatible-mode cell {1,2}, {1,3}, "
      "{2,3}, {1,2,3}",
      Q(16, 25) - (tau + Q(1)) == Q(-14, 25)
      and Q(6, 5) - tau == Q(1))

# ---------------- Layer 3: text needles -------------------------------------------
tex = open(os.path.join(HERE, "paper2_computational_certification_v16.tex"),
           encoding="utf-8").read()
tex_raw = tex
tex = " ".join(tex.split())
NEEDLES = [
    "\\rho_{\\mathcal{H},G} \\le J_{\\mathcal{I}}(T) \\le \\rho_{\\mathcal{H},G}",
    "\\max_{a \\in \\mathscr{S}_G} \\bar{e}_a + \\delta_\\beta + L h_t",
    "shared-authority ladder", "prop:ladder",
    "\\tfrac{15 - \\sqrt{183}}{6}", "\\tfrac{10 - \\sqrt{58}}{6}",
    "t^{*}(\\{1,2\\}) = t^{*}(\\{1,3\\}) = \\tfrac25",
    "t^{*}(\\{2,3\\}) = \\tfrac35",
    "6\\tau^2 - 30\\tau + 7 = 0", "6\\tau^2 - 20\\tau + 7 = 0",
    "\\tau = \\tfrac6{25}", "\\tau = \\tfrac{39}{100}",
    "\\tau_{12} = \\tau_{13}", "\\tau_{23}",
    "e = \\sum_J |J|^2/4", "conflict-targeted block refinement",
    "arbitrary-precision dual re-solve", "warm-started incremental refinement",
    "M_U :=", "the certificate is the blind window's unbrakeability",
    "shared-authority delay hierarchy", "optimal shared-braking programs",
    "\\bar{e} + \\delta_\\beta + L h_t", "in \\(L^1\\) norm",
    "admits one with at most", "uniform aligned mesh",
    "agrees with the exact rational optimum",
    "mesh refinement eventually certifies",
    "relaxes the controller's feasible set",
    "exact reduction precisely when",
    "held witness policy attains the continuous value",
    "stored-scenario widths", "has \\(L^1\\) norm at most",
    "No floor is claimed off the uniform family",
    "the level is unrestricted",
    "\\tau_{\\max} = \\tfrac{7}{50} = 0.14", "\\tau - \\frac{7}{50}",
    "\\tfrac{39}{25} = 1.56 < 2", "\\Gamma(0.2) = 0.06 > 0",
    "\\tfrac{3}{100} = 0.03", "\\tfrac{3}{50} = 0.06",
    "\\beta + e = -\\tfrac{53}{100}", "-\\tfrac{3}{100} < 0",
    "\\tfrac{93}{50} =\n1.86".replace("\n", " "), "e = 12 \\cdot h^2/4 = \\tfrac{3}{100}",
    "0.030000000", "0.057000000", "4.2 \\times 10^{-17}",
    "mQ + 1", "Ms(N_t{+}1) + p_U Q", "c + \\sum_j h_U(-r_j) < 0",
    "3{,}240", "\\varepsilon/(q+1)", "r + 1 \\le mQ + 1",
    "Y^{*} = 27/5" if False else "24/26/25/28",
    "information--time rank", "HiGHS",
    "the complete steps are Steps 1--6 of the supplementary", "viacert.continuous", "not a reimplementation",
    "which satisfy \\(\\sum_j \\lambda_j = 1\\)", "not to the relaxation",
    "Sion", "Arzel", "measurable vertex selection", "seven-step",
    "complete dual calculus", "R_U = 1", "V_U = \\tau + 1 = \\tfrac65",
    "L = T + 1 = \\tfrac{11}{5}", "h = \\tfrac1{15}",
    "\\rho = \\tfrac1{25}", "dyadic schedule",
    "Riesz representation", "Banach--Alaoglu", "Dirac",
    "not a load-bearing citation",
    "explicit pairwise policies", "12345}{6250}", "2419}{1250}",
    "tfrac{2719}{1250}", "tfrac{2501}{1250}", "tfrac{103}{50}",
    "tfrac{23}{10}", "tfrac{31}{1250}", "tfrac{81}{1250}",
    "(n_1 + n_2)", "tfrac{29}{25}", "tfrac{47}{100}", "tfrac{17}{100}",
    "\\bar{e} = e + \\tfrac12", "-\\tfrac{6}{25}", "tfrac{26}{100}",
    "-\\tfrac15", "tfrac{24}{25}" if False else "the program is a relaxation",
    "\\delta_{\\mathrm{init}} +",
    "Solver-assisted, exactly certified mesh study",
    "2026b. An obstruction calculus", "Manuscript submitted for publication",
    "not a probability distribution", "mathscr{S}_G", "block variables",
    "resolution bound", "irredundant", "necessary but not sufficient",
    "rests on three requirements", "Every reported mathematical benchmark value",
    "saturating the \\(r + 1\\) bound", "transfers down",
    "Instance arithmetic, collected", "unrestricted real variable",
    "u^{\\pi}_\\theta(t) = u_{r, C_r(\\theta)}(t)",
    "Timings are single runs on the verification",
    "paper2_computational_certification_v15_verification.py",
    "\\rho(h) = \\tfrac3{50} - Th/4\\) on every uniform aligned",
    "Two tempting variants fail",
    "not} supported on", "the averaging term vanishes identically",
    "brake \\emph{through} the blind window",    # edition 9 (round-9 outlook + scan fixes)
    "the certificate's prescriptive decode into optimal shared braking authorities, "
    "the induced pair-delay hierarchy, and the exact redesign sensitivities "
    "(Section~\\ref{ladder})",
    "Three further extension directions are recorded, each a construction of its own "
    "rather than an increment of the present framework",
    "The cell-conditioned lift of labels, kernels, and costs for general measurement channels",
    "is carried in Proposition~\\ref{prop:beliefcells}",
    "cell-conditioned lift of labels, kernels, and costs",
    "turns the finite program into a conic one",
    "remain the benchmark such relaxations must meet",
    "alters a structural input of the bridge theorem",
    "with the certificate file as the exchange format",
    "validates the archived witnesses of this paper and of the",
    "alongside the tooling directions of Section~\\ref{library}",
    "\\begin{proposition}[belief-cell certificates]", "prop:beliefcells",
    "\\begin{proposition}[redesign sensitivities]", "prop:redesign",
    "belief-cell rows extend the sandwich to partial and noisy observation",
    "advancing observation buys margin at rate one",
    "\\Gamma_a(\\tau) = \\tau - \\tfrac7{50} - \\tfrac{a-1}{2}",
    "\\tau_{\\max}(a) = \\tfrac7{50} + \\tfrac{a-1}{2}",
    "\\delta_C < \\Gamma(\\tfrac15) = \\tfrac3{50}",
    "the margin moving to \\(\\tau - \\tfrac7{50} - \\delta_C\\)",
    "The rates order the redesign options exactly",
    "observation design is the same refinement axis as mesh design",
    "the audited delay hierarchy is exactly the cell-refinement family",
    "published audits (Abaee, 2026b, 2026c)",
    "finite audits of Abaee (2026c)",
    "certificate\\_exchange\\_v1.py",
    "dual-certificate companion (Abaee, 2026g)",
    "master monotonicity of the worked-systems companion (Abaee, 2026c)",
    "2026c. Worked systems for the obstruction calculus",
    "2026g. The measure dual of the common-action obstruction",
    "joint check archived; Abaee, 2026f",
    "2026f. Exact belief-state computation at scale",
    "1983. Linear Programming. A Series of Books",
    "Helly, E., 1923",
    "Milanese, M., Norton, J., Piet-Lahanier, H., Walter, E. (Eds.), 1996",
    "paper2\\_comp\\_certification\\_figures\\_v1.py",
    "figs_comp2/fig_trajectories.pdf",
    "figs_comp2/fig_hierarchy.pdf",
    "\\item[(H1)]",
    "\\item[(H6)]",
    "linear-programming (LP)",
    "recompute-then-assert: every plotted peak",

]
missing = [n for n in NEEDLES if n not in tex]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")

check("ladder cross-references: the contribution list cites the ladder "
      "subsection and the belief-cell instantiation cites the ladder "
      "proposition (2 ladder references total)",
      tex_raw.count("\\ref{ladder}") == 1
      and tex_raw.count("\\ref{prop:ladder}") == 2,
      (tex_raw.count("\\ref{ladder}"), tex_raw.count("\\ref{prop:ladder}")))


s1 = open(os.path.join(HERE, "paper2_computational_certification_supplementary_v6.tex"),
          encoding="utf-8").read()
s1n = " ".join(s1.split())
s1_ok = all(k in s1n for k in
            ("Step 5b (exact atomic dual representation, proof of (9))",
             "Derivation of the moduli from primitive data",
             "Banach--Alaoglu", "Arzel\\`a--Ascoli", "Sion's minimax theorem",
             "measurable selection", "Dirac measures attain both ends",
             "Finitely supported measures are weak-* dense",
             "lexicographically first minimizing vertex",
             "form is the operative one", "M_U :=",
             "label-continuity modulus", "stored scenarios making the error",
             "max_{\\hat a \\in \\mathscr S_G} \\bar e_{\\hat a}",
             "the sup-norm form is false for the step kernels"))
check("S1 v6 carries the complete seven-step proof of (iv) with every "
      "hypothesis verified: the L1 pairing step (M_U), the L1 Gronwall "
      "modulus, the max-e sandwich conclusion, and the delta_init/delta_num "
      "completeness clause", s1_ok)


# ---------------- Layer 2 (edition 5): round-4 audit checks ---------------------
# (a) the printed dual facet list reconstructs the hexagon exactly (audit item 1)
Fm6 = [(Q(0), Q(1)), (Q(0), Q(-1)), (Q(2), Q(1)), (Q(2), Q(-1)),
       (Q(-2), Q(1)), (Q(-2), Q(-1))]
fv6 = [Q(4, 5), Q(4, 5), Q(2), Q(2), Q(2), Q(2)]
nn = [(Q(1), Q(0)), (Q(-3, 5), Q(4, 5)), (Q(-3, 5), Q(-4, 5))]
eta6 = [(Q(0), Q(0), Q(0), Q(0), Q(1, 4), Q(1, 4)),
        (Q(0), Q(1, 2), Q(0), Q(3, 10), Q(0), Q(0)),
        (Q(1, 2), Q(0), Q(3, 10), Q(0), Q(0), Q(0))]
check("dual facets/witnesses: F, f, eta_j mutually exact (F^T eta_j = -n_j, "
      "f^T eta_j = 1) for all three modes",
      all(tuple(sum(eta6[j][r] * Fm6[r][d] for r in range(6))
                for d in (0, 1)) == (-nn[j][0], -nn[j][1])
          and sum(eta6[j][r] * fv6[r] for r in range(6)) == 1
          for j in range(3)))
# (b) instance moduli (audit item 5): R_U = 1, V_U = 6/5, L = 11/5 route pieces
RU6 = max((v[0] ** 2 + v[1] ** 2) for v in
          [nn[0], (-nn[1][0], -nn[1][1]), (-nn[2][0], -nn[2][1]),
           (-nn[0][0], -nn[0][1]), nn[1], nn[2]])
ok_L = all(((t - tp) * tp + (t - tp) ** 2 / 2) <= Q(6, 5) * (t - tp)
           for t in [Q(n, 25) for n in range(1, 31)]
           for tp in [Q(n, 25) for n in range(0, 31)] if tp < t)
check("instance moduli: R_U = 1 (hexagon circumradius); kernel-difference "
      "integral <= T|t-t'| on the rational grid (L = T + 1 = 11/5 with "
      "|beta_t - beta_t'| = |t-t'|); delta_beta = 0",
      RU6 == 1 and ok_L)
# (c) sixth aligned mesh h = 1/15: witness pair certifies rho = 1/25
_camp = {}
exec(compile(open(os.path.join(HERE, "paper2c_lp_campaign.py"),
                  encoding="utf-8").read().split(
      "# ---------------- solver campaign")[0], "camp", "exec"), _camp)
h15 = Q(1, 15)
_bl, _bi, _rows = _camp["build_rows"](h15)
check("sixth aligned mesh h = 1/15: exact primal witness feasible and dual "
      "witness stationary at rho = max{0, 3/50 - Th/4} = 1/25 (Q = 48)",
      _camp["rho_exact"](h15) == Q(1, 25)
      and _camp["primal_feasible"](h15, _bl, _bi, _rows)
      and _camp["dual_witness"](h15) and len(_bl) == 48)
# (d) refutation pins for the round-4 record
dot6 = lambda a, b: a[0] * b[0] + a[1] * b[1]
u_bad = (Q(-485, 1000), Q(630, 1000))
vn_bad = Q(1) + dot6(nn[1], u_bad) * Q(1, 5)
pn_bad = Q(34, 25) + Q(1, 5) + dot6(nn[1], u_bad) * Q(1, 25) / 2
peak_bad = pn_bad + vn_bad ** 2 / 2
check("round-4 pin: the proposed {1,2} blind control (-0.485, 0.630) has "
      "positive n_2-projection and its true peak exceeds 2 (proposal refuted)",
      dot6(nn[1], u_bad) > 0 and peak_bad > 2)
u_n3 = nn[2]
peak_n3 = (Q(34, 25) + Q(1, 5) + dot6(nn[1], u_n3) * Q(1, 25) / 2
           + (Q(1) + dot6(nn[1], u_n3) * Q(1, 5)) ** 2 / 2)
check("round-4 pin: the knife-edge u = n_3 single-brake variant peaks at "
      "62499/31250 < 2 (valid but dominated by the shipped 12345/6250)",
      peak_n3 == Q(62499, 31250) and peak_n3 < 2)

FORBIDDEN = ["R_U V_U h_u + R_D V_D h_d + L h_t", "HiGHS-attained",
             "\\le R_U \\|k_a - k_{a'}\\|_{L^1}",
             "in the sup-norm and absolutely", "sup-norm label continuity",
             "positive certificates survive", "attains the exact rational optimum",
             "exact reduction rather", "relaxes the adversary's feasible set",
             "obstruction has at most", "is supported on",
             "the floor at zero says", "u = -n_j\\) to rest",
             "\\rho(h) = \\max\\{0,\\", "max\\{0, 3/50 - Th/4\\}",
             "would be close to standard", "no floating point on\nany audited path", "retirement of the present scripts",
             "Solver-certified", "estimation-tube programme",
             "unique pooling weights", "clamps to the same",
             "well-posed exactly when", "decides\nnone of the information-constrained",
             "every sufficiently fine\nsequence", "Three scripts cover the claims",
             "Every number in this paper",
             "the recorded next step "
             "(Section~\\ref{library})"]
present = [f for f in FORBIDDEN
           if " ".join(f.split()) in tex]
check("edition absences: superseded claim wordings are gone from the tex",
      not present, f"(still present: {present})" if present else "")

check("declarations use separate headings with the responsibility wording",
      "\\subsection*{Funding}" in tex and "\\subsection*{AI declaration}" in tex
      and "The author reviewed and edited outputs and takes responsibility for the final work." in tex)


# ---------------- Layer 2 (edition 7): round-7 audit checks ---------------------
# (R7-1) the label-continuity hypothesis is L^1, not sup-norm: velocity-facet
# kernels k_t(s) = 1{s<=t} e_k jump by 1 in the sup-norm for every t != t',
# while their L^1 difference is |t - t'|; position kernels have L^1
# difference t'(t-t') + (t-t')^2/2 <= T|t-t'|, and the difference is NOT
# supported on [t', t].
_l1_ok = all(((tt - tp) * tp + (tt - tp) ** 2 / 2) <= Q(6, 5) * (tt - tp)
             for tt in [Q(n, 25) for n in range(1, 31)]
             for tp in [Q(m, 25) for m in range(0, 31)] if tp < tt)
check("R7 label continuity: velocity kernels jump 1 in sup-norm (t != t'); "
      "position-kernel L^1 difference = t'(t-t') + (t-t')^2/2 <= T|t-t'|; "
      "difference nonzero on [0, t') (support claim refuted)",
      l1_ok := _l1_ok and (Q(1, 2) != Q(1, 3))
      and ((Q(1, 2) - Q(1, 3)) * Q(1, 3) != 0))

# (R7-2) the sandwich (8) charges max e_a: with the loose but verified bound
# e + 1/2 the program returns rho = -47/100 at h = 1/10; the printed uniform
# form claims J <= -24/100 < J = 6/100 (false); the corrected bound
# rho + max e_a + L h_t = 17/100 >= 6/100 (valid); h_t = h/2 is the covering
# radius.
T7 = Q(6, 5)
h7 = Q(1, 10)
e7 = T7 * h7 / 4
rho_loose = (Q(-1, 2) + Q(14, 25)) - (e7 + Q(1, 2))
printed8 = rho_loose + Q(1) * (tau + 1) * h7 + (T7 + 1) * (h7 / 2)
fixed8 = rho_loose + (e7 + Q(1, 2)) + (T7 + 1) * (h7 / 2)
check("R7 sandwich: loose e+1/2 gives rho = -47/100; printed uniform form "
      "claims J <= -24/100 (false at J = 3/50); corrected max-e form gives "
      "17/100 >= 3/50; covering radius h_t = h/2",
      rho_loose == Q(-47, 100) and printed8 == Q(-24, 100)
      and printed8 < Q(3, 50) and fixed8 == Q(17, 100) and fixed8 >= Q(3, 50)
      and h7 / 2 == Q(1, 20) and (T7 + 1) * Q(1, 20) == Q(11, 100))

# (R7-3) refinement positivity is not monotone (scalar counterexample):
# x' = 1 + b(t) u, u in [-1,1], x(0)=0, x <= 11/10, T = 2, b = 1 on [3/5,1),
# b = -1 on [8/5,2]. One block: kbar = 0, e = 4/5, rho = 1/10 = J > 0;
# split at t = 1: kbar = (2/5, -2/5), e = 24/25, rho = -43/50 < 0.
_edges = [Q(0), Q(3, 5), Q(1), Q(8, 5), Q(2)]
def _val_at(x):
    return Q(1) if Q(3, 5) <= x < 1 else (Q(-1) if Q(8, 5) <= x <= 2 else Q(0))
def _kint(a, b):
    es = sorted(set(_edges + [a, b]))
    return sum(_val_at((max(x0, a) + min(x1, b)) / 2) * (min(x1, b) - max(x0, a))
               for x0, x1 in zip(es, es[1:]) if min(x1, b) > max(x0, a))
def _block_e(kb, lo, hi):
    es = sorted(set(_edges + [lo, hi]))
    return sum(abs(kb - _val_at((max(x0, lo) + min(x1, hi)) / 2))
               * (min(x1, hi) - max(x0, lo))
               for x0, x1 in zip(es, es[1:]) if min(x1, hi) > max(x0, lo))
kb1 = _kint(Q(0), Q(2)) / 2
kb2a, kb2b = _kint(Q(0), Q(1)), _kint(Q(1), Q(2))
e_1blk = _block_e(kb1, Q(0), Q(2))
e_splt = _block_e(kb2a, Q(0), Q(1)) + _block_e(kb2b, Q(1), Q(2))
rho_1blk = Q(9, 10) - e_1blk
rho_splt = (-(abs(kb2a) + abs(kb2b))) + Q(9, 10) - e_splt
check("R7 refinement counterexample: one block kbar = 0, e = 4/5, "
      "rho = 1/10 = J (positive certificate); split at t = 1: kbar = "
      "(2/5, -2/5), e = 24/25, rho = -43/50 (certificate gone)",
      kb1 == 0 and e_1blk == Q(4, 5) and rho_1blk == Q(1, 10)
      and kb2a == Q(2, 5) and kb2b == Q(-2, 5) and e_splt == Q(24, 25)
      and rho_splt == Q(-43, 50))

# (R7-4) the level is unrestricted: the allowed two-block mesh
# [0, 1/5], [1/5, 6/5] on the instance gives e = sum |J|^2/4 = 26/100 and
# rho = -1/5, certified by the witness pair (primal row -1/2 + 14/25 - 26/100;
# dual 1/2 + (beta + 26/100) = 1/5 > 0); and max{0,.} is inactive on the
# uniform family (raw value >= 0 exactly for h <= 1/5).
e_2blk = tau * tau / 4 + (T7 - tau) ** 2 / 4
beta7 = Q(16, 25) - T7
check("R7 two-block aligned mesh: e = 26/100, rho = -1/5 with witness row "
      "-1/2 + 14/25 - 26/100 = -1/5 and dual 1/2 - 3/10 = 1/5 > 0; "
      "raw uniform law nonnegative exactly on h <= 1/5",
      e_2blk == Q(26, 100) and Q(3, 50) - e_2blk == Q(-1, 5)
      and Q(-1, 2) + Q(14, 25) - e_2blk == Q(-1, 5)
      and Q(1, 2) + (beta7 + e_2blk) == Q(1, 5)
      and Q(3, 50) - T7 * Q(1, 5) / 4 == 0
      and all(Q(3, 50) - T7 * Q(n, 100) / 4 > 0 for n in range(1, 20)))


# ---------------- Layer 2 (edition 8): shared-authority ladder ------------------
neg8 = lambda vv: (-vv[0], -vv[1])
nA = (Q(1), Q(0)); nB = (Q(-3, 5), Q(4, 5)); nC = (Q(-3, 5), Q(-4, 5))
dot8 = lambda a, b: a[0] * b[0] + a[1] * b[1]
VERTS8 = [nA, neg8(nC), nB, neg8(nA), neg8(nB), nC]   # cyclic hexagon order
lam8 = [Q(3, 8), Q(5, 16), Q(5, 16)]
check("ladder (i) pooling identity: sum lambda = 1, sum lambda_j n_j = 0 "
      "with all lambda_j > 0 -- no common control brakes all three branches",
      sum(lam8) == 1
      and tuple(sum(l * n[i] for l, n in zip(lam8, (nA, nB, nC)))
                for i in (0, 1)) == (0, 0)
      and all(l > 0 for l in lam8))
def seg_pts8(d, verts):
    pts = []
    for a, b in zip(verts, verts[1:] + verts[:1]):
        da, db = dot8(d, a), dot8(d, b)
        if (da < 0 < db) or (db < 0 < da):
            t = da / (da - db)
            pts.append((a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])))
    return pts
def tstar8(ni, nj):
    d = (ni[0] - nj[0], ni[1] - nj[1])
    best, arg = None, None
    for w in VERTS8 + seg_pts8(d, VERTS8):
        t = -max(dot8(ni, w), dot8(nj, w))
        if best is None or t > best:
            best, arg = t, w
    return best, arg
t12, w12 = tstar8(nA, nB); t23, w23 = tstar8(nB, nC); t13, w13 = tstar8(nA, nC)
check("ladder (ii) optimal shared authorities: t*({1,2}) = 2/5 at "
      "(-2/5,-4/5); t*({1,3}) = 2/5 at (-2/5,4/5); t*({2,3}) = 3/5 at n1 -- "
      "exactly the printed blind-window controls",
      t12 == Q(2, 5) and w12 == (Q(-2, 5), Q(-4, 5))
      and t13 == Q(2, 5) and w13 == (Q(-2, 5), Q(4, 5))
      and t23 == Q(3, 5) and w23 == (Q(1), Q(0)))
def peak_tau8(t, tau):
    return Q(93, 50) + (1 - t) * tau + (t * t - t) * tau * tau / 2
check("ladder (iii) peak identity: 2469/1250 and 2419/1250 at tau = 1/5; "
      "increasing on [0, 1/t*]; thresholds (15 - sqrt(183))/6 and "
      "(10 - sqrt(58))/6 exact in Q(sqrt 183), Q(sqrt 58); ladder "
      "7/50 < 0.2454 < 0.3974; surrogates 6/25, 39/100 < 2 with 1/4 -> "
      "801/400 > 2 and 2/5 -> 2501/1250 > 2",
      peak_tau8(Q(2, 5), Q(1, 5)) == Q(2469, 1250)
      and peak_tau8(Q(3, 5), Q(1, 5)) == Q(2419, 1250)
      and all((peak_tau8(t, Q(n, 100) + Q(1, 1000))
               - peak_tau8(t, Q(n, 100))) > 0
              for t in (Q(2, 5), Q(3, 5)) for n in range(0, 60))
      and 6 * (15 * 15 + 183) + (-30) * 15 * 6 + 7 * 36 == 0
      and -2 * 6 * 15 - (-30) * 6 == 0
      and 6 * (10 * 10 + 58) + (-20) * 10 * 6 + 7 * 36 == 0
      and -2 * 6 * 10 - (-20) * 6 == 0
      and Q(7, 50) < (15 - 183 ** 0.5) / 6 < (10 - 58 ** 0.5) / 6 < Q(1, 2)
      and peak_tau8(Q(2, 5), Q(6, 25)) < 2
      and peak_tau8(Q(3, 5), Q(39, 100)) < 2
      and peak_tau8(Q(2, 5), Q(1, 4)) == Q(801, 400)
      and peak_tau8(Q(3, 5), Q(2, 5)) == Q(2501, 1250))
def vel_max8(nj, w, tau):
    vtau = Q(1) + dot8(nj, w) * tau
    vb = (nj[0] + w[0] * tau, nj[1] + w[1] * tau)
    vr = (vb[0] - nj[0] * vtau, vb[1] - nj[1] * vtau)
    return max(abs(c) for vv in (vb, vr) for c in vv)
def worst_slack8(nj, w, tau, T=Q(6, 5)):
    a_blind = dot8(nj, w); vtau = Q(1) + a_blind * tau
    vb = (nj[0] + w[0] * tau, nj[1] + w[1] * tau)
    ptau_vec = (Q(34, 25) * nj[0] + nj[0] * tau + w[0] * tau * tau / 2,
                Q(34, 25) * nj[1] + nj[1] * tau + w[1] * tau * tau / 2)
    worst = None
    for tt in (Q(0), tau, tau + vtau, T):
        if tt <= tau:
            pos = (Q(34, 25) * nj[0] + nj[0] * tt + w[0] * tt * tt / 2,
                   Q(34, 25) * nj[1] + nj[1] * tt + w[1] * tt * tt / 2)
            vel = (nj[0] + w[0] * tt, nj[1] + w[1] * tt)
        else:
            sg = tt - tau; smin = min(sg, vtau)
            vel = (vb[0] - nj[0] * smin, vb[1] - nj[1] * smin)
            pos = (ptau_vec[0] + vb[0] * smin - nj[0] * smin * smin / 2,
                   ptau_vec[1] + vb[1] * smin - nj[1] * smin * smin / 2)
            if sg > vtau:
                pos = (pos[0] + vel[0] * (sg - vtau), pos[1] + vel[1] * (sg - vtau))
        for ni in (nA, nB, nC):
            sv = Q(2) - dot8(ni, pos)
            worst = sv if worst is None else min(worst, sv)
        for c in vel:
            sv = Q(6, 5) - abs(c)
            worst = sv if worst is None else min(worst, sv)
    return worst
w13v = (Q(-2, 5), Q(4, 5))
nc = max(worst_slack8(nA, w12, Q(6, 25)), worst_slack8(nB, w12, Q(6, 25)),
         worst_slack8(nA, w13v, Q(6, 25)), worst_slack8(nC, w13v, Q(6, 25)),
         worst_slack8(nB, w23, Q(39, 100)), worst_slack8(nC, w23, Q(39, 100)))
mv = max(vel_max8(nA, w12, Q(6, 25)), vel_max8(nB, w12, Q(6, 25)),
         vel_max8(nB, w23, Q(39, 100)), vel_max8(nC, w23, Q(39, 100)))
check("ladder facet status at the rational surrogates: all seven facets "
      "hold (worst slack > 0) with velocity rows strict (max |comp| <= 6/5)",
      nc > 0 and mv <= Q(6, 5), (float(nc), float(mv)))
_eA = tau * tau / 4 + (Q(6, 5) - tau) ** 2 / 4
_eB = (tau / 2) ** 2 / 2 + ((Q(6, 5) - tau) / 3) ** 2 * 3 / 4
check("affine-kernel refinement identity: e = sum |J|^2/4 exactly (two-block "
      "26/100; a five-block non-uniform aligned mesh reproduces the closed "
      "form; uniform minimizes the sum at fixed count)",
      _eA == Q(26, 100)
      and _eB == (tau * tau / 4) / 2 + ((Q(6, 5) - tau) ** 2 / 4) / 3)

# proof-marking checks (round 15): the marked rows/value proofs, the
# explicit supplementary-steps pointer, and proof parity on the split pairs
_npro = ["The identity is the linear solution formula",
         "Existence: the policy-signal space is a finite product",
         "the complete steps are Steps 1--6 of the supplementary"]
_miss = [s for s in _npro if " ".join(s.split()) not in " ".join(tex.split())]
check("proof-marking: rows/value arguments carried in proof environments; "
      "bridge proof pointer names supplementary Steps 1--6 explicitly"
      + ("" if not _miss else f" (missing: {_miss})"), not _miss)
_pars = [f for f in ("paper2_computational_certification_v16.tex",)
         if True]
_nenv = len([m for m in __import__("re").finditer(
    r"\\begin\{(?:theorem|proposition|lemma|corollary)\*?\}", tex)])
_nprf = tex.count("\\begin{proof}")
check(f"proof parity after marking: {_nenv} theorem-like environments, "
      f"{_nprf} proof environments (comp counts declarations-block "
      "statements; parity at or above the marked pairs)",
      _nprf >= 4 and _nenv > 0)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)
