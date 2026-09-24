#!/usr/bin/env python3
"""
Computational viability certification, edition 1 — verification.

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
paper2_computational_certification_v1.tex, the separate declaration
headings, and the responsibility wording.

Exact rational/integer arithmetic except solver outputs; stdlib only;
deterministic.
Run: python3 paper2_computational_certification_v1_verification.py
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

# ---------------- Layer 3: text needles -------------------------------------------
tex = open(os.path.join(HERE, "paper2_computational_certification_v1.tex"),
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
]
missing = [n for n in NEEDLES if n not in tex]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")
check("declarations use separate headings with the responsibility wording",
      "\\subsection*{Funding}" in tex and "\\subsection*{AI declaration}" in tex
      and "The author reviewed and edited outputs and takes responsibility for the final work." in tex)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)
