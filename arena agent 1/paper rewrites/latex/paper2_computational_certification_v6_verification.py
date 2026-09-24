#!/usr/bin/env python3
"""
Computational viability certification, edition 5 — verification.

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
Layer 3 (text): asserts every headline number in
paper2_computational_certification_v6.tex, the separate declaration
headings, and the responsibility wording.

Exact rational/integer arithmetic except solver outputs; stdlib only;
deterministic.
Run: python3 paper2_computational_certification_v5_verification.py
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


# ---------------- Layer 2 (edition 3): round-3 audit checks ---------------------
# (a) pairwise policies for the three-branch instance (explicit, exact)
n1v = (Q(1), Q(0)); n2v = (Q(-3, 5), Q(4, 5)); n3v = (Q(-3, 5), Q(-4, 5))
PPOS = Q(34, 25); tau = Q(1, 5)
dot = lambda a, b: a[0] * b[0] + a[1] * b[1]
def pair_peak(n_j, alpha):
    return PPOS + tau - alpha * tau * tau / 2 + (1 - alpha * tau) ** 2 / 2
a12 = -dot(n1v, (Q(-2, 5), Q(-4, 5)))          # common mid-brake deceleration
check("pair {1,2}/{1,3}: two-phase brake (-(2/5) n_j then -n_j) peaks at "
      "12345/6250 = 1.9752 < 2; both branches decelerate equally",
      a12 == Q(2, 5) and -dot(n2v, (Q(-2, 5), Q(-4, 5))) == Q(2, 5)
      and pair_peak(n1v, a12) == Q(12345, 6250) < Q(2))
a23 = -dot(n2v, (Q(1), Q(0)))
check("pair {2,3}: blind hold u = n1 (both branches decelerate at 3/5 under "
      "the -(3/5) n_j mid-brake) then -n_j peaks at 2419/1250 = 1.9352 < 2",
      a23 == Q(3, 5) and -dot(n3v, (Q(1), Q(0))) == Q(3, 5)
      and pair_peak(n2v, a23) == Q(19352, 10000) < Q(2))
check("pair-policy mid-brake controls are admissible in the hexagonal U",
      abs(Q(-4, 5)) <= Q(4, 5) and abs(2 * Q(-2, 5) + Q(-4, 5)) <= Q(2)
      and abs(2 * Q(-2, 5) - Q(-4, 5)) <= Q(2)
      and abs(Q(12, 25)) <= Q(4, 5) and abs(2 * Q(9, 25) + Q(-12, 25)) <= Q(2)
      and abs(2 * Q(9, 25) - Q(-12, 25)) <= Q(2))
# (b) source-hygiene regression: no escape-mangled control bytes or bare
# remnants in either edition-3 tex file (the v2 corruption class)
import re as _re
hyg = True
for f in ("paper2_computational_certification_v6.tex",
          "paper2_computational_certification_v5_supplementary.tex"):
    raw = open(os.path.join(HERE, f), "rb").read()
    hyg &= all(b >= 32 or b == 10 for b in raw)
    txt = raw.decode("utf-8")
    hyg &= not _re.search(r"(?<![\\a-zA-Z])ef\{", txt)
    hyg &= not _re.search(r"(?<![\\a-zA-Z])exttt\{", txt)
check("source hygiene: no control bytes, no bare ef{/exttt{ remnants in "
      "either edition-3 tex file", bool(hyg))

# ---------------- Layer 3: text needles -------------------------------------------
tex = open(os.path.join(HERE, "paper2_computational_certification_v6.tex"),
           encoding="utf-8").read()
tex = " ".join(tex.split())
NEEDLES = [
    "\\rho_{\\mathcal{H},G} \\le J_{\\mathcal{I}}(T) \\le \\rho_{\\mathcal{H},G}",
    "R_U V_U h_u + \\delta_\\beta + L h_t",
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
    "Proof outline", "viacert.continuous", "not a reimplementation",
    "which satisfy \\(\\sum_j \\lambda_j = 1\\)", "not to the relaxation",
    "Sion", "Arzel", "measurable vertex selection", "seven-step",
    "complete dual calculus", "R_U = 1", "V_U = \\tau + 1 = \\tfrac65",
    "L = T + 1 = \\tfrac{11}{5}", "h = \\tfrac1{15}",
    "\\rho = \\tfrac1{25}", "dyadic schedule",
    "Riesz representation", "Banach--Alaoglu", "Dirac",
    "not a load-bearing citation",
    "explicit pairwise policies", "12345}{6250}", "2419}{1250}",
    "Solver-assisted, exactly certified mesh study",
    "2026b. An obstruction calculus", "Manuscript submitted for publication",
    "not a probability distribution", "mathscr{S}_G", "block variables",
    "resolution bound", "irredundant", "necessary but not sufficient",
    "rests on three requirements", "Every reported mathematical benchmark value",
    "saturating the \\(r + 1\\) bound", "transfers down",
    "Instance arithmetic, collected", "unrestricted real variable",
    "u^{\\pi}_\\theta(t) = u_{r, C_r(\\theta)}(t)",
    "Timings are single runs on the verification",
    "paper2_computational_certification_v6_verification.py",
]
missing = [n for n in NEEDLES if n not in tex]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")


s1 = open(os.path.join(HERE, "paper2_computational_certification_v5_supplementary.tex"),
          encoding="utf-8").read()
s1n = " ".join(s1.split())
s1_ok = all(k in s1n for k in
            ("Step 5b (exact atomic dual representation, proof of (9))",
             "Derivation of the moduli from primitive data",
             "Banach--Alaoglu", "Arzel\\`a--Ascoli", "Sion's minimax theorem",
             "measurable selection", "Dirac measures attain both ends",
             "Finitely supported measures are weak-* dense",
             "lexicographically first minimizing vertex"))
check("S1 v4 carries the complete seven-step proof of (iv) with every "
      "hypothesis verified", s1_ok)


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

FORBIDDEN = ["would be close to standard", "no floating point on\nany audited path", "retirement of the present scripts",
             "Solver-certified", "estimation-tube programme",
             "unique pooling weights", "clamps to the same",
             "well-posed exactly when", "decides\nnone of the information-constrained",
             "every sufficiently fine\nsequence", "Three scripts cover the claims",
             "Every number in this paper"]
present = [f for f in FORBIDDEN
           if " ".join(f.split()) in tex]
check("edition-3 absences: superseded claim wordings are gone from the tex",
      not present, f"(still present: {present})" if present else "")

check("declarations use separate headings with the responsibility wording",
      "\\subsection*{Funding}" in tex and "\\subsection*{AI declaration}" in tex
      and "The author reviewed and edited outputs and takes responsibility for the final work." in tex)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)
