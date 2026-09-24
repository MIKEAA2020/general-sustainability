#!/usr/bin/env python3
"""
Belief-state safety values, edition 1 — verification.

Layer 1 (chain): runs the two per-system verification scripts as
subprocesses and asserts each exits green (15 + 6 = 21 checks).
Layer 2 (own): recomputes the headline identities from the definitions —
the closed-form grid values by direct branch-mass enumeration for every
cell with k <= T_obs, the minimal-mass bound attained on the two-floor
instance, and the jump loci from the closed form.
Layer 3 (text): asserts every headline number in
paper2_belief_state_v1.tex, the separate declaration headings, and the
responsibility wording.

Exact rational/integer arithmetic; stdlib only; deterministic.
Run: python3 paper2_belief_state_v1_verification.py
"""
import subprocess, sys, os
from fractions import Fraction as Q
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
PASS = []
def check(name, cond, detail=""):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else " " + str(detail)))

# ---------------- Layer 1: chained per-system scripts --------------------------
CHAIN = [
    ("paper2_stochastic_selector_v2_verify.py", 15),
    ("hidden_parameter_learning_v1_verify.py", 6),
]
total_chained = 0
for script, expected in CHAIN:
    p = subprocess.run([sys.executable, os.path.join(HERE, script)],
                       capture_output=True, text=True)
    tail = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else ""
    ok = (p.returncode == 0) and (f"{expected}/{expected} checks pass" in tail)
    total_chained += expected if ok else 0
    check(f"chain {script} green ({expected}/{expected})", ok)
check("chained total = 21 checks", total_chained == 21, f"({total_chained})")

# ---------------- Layer 2a: closed form by direct branch enumeration -----------
GRID = [Q(n, 10) for n in range(10, 26)]
TOS = [1, 2, 3]

def V_closed(z0, T, k):
    if k <= T:
        return Q(1, 2) * ((1 if z0 - k >= 1 else 0) + (1 if z0 + k >= 1 else 0))
    return Q(1, 2) * (1 + (1 if z0 >= 1 + T else 0))

def V_class(z0, k, constant_only):
    """Direct enumeration of the definition: blind sequences, both branches
    traced stepwise, mass of branches never leaving [1, inf). The declared
    hold class uses the two constant sequences; the unrestricted class
    enumerates all of them."""
    seqs = [(1,) * k, (-1,) * k] if constant_only else list(product((1, -1), repeat=k))
    best = Q(0)
    for seq in seqs:
        za = zb = z0
        sa = sb = True
        for u in seq:
            za += u
            zb -= u
            if za < 1: sa = False
            if zb < 1: sb = False
        best = max(best, Q(1, 2) * (int(sa) + int(sb)))
    return best

cells = [(z, T, k) for z in GRID for T in TOS for k in (1, 2, 3) if k <= T]
ok_b1 = all(V_class(z, k, True) == V_closed(z, T, k) for z, T, k in cells)
check(f"B1 declared hold class: direct branch-mass enumeration == closed form "
      f"on all {len(cells)} cells with k <= T_obs", ok_b1 and len(cells) == 96)

ok_b1b = all(
    ((V_class(z, k, False) == 1) == (z >= 2))
    and ((V_class(z, k, False) == Q(1, 2)) == (z < 2))
    for z in GRID for T in TOS for k in (1, 2, 3))
check("B1b unrestricted class by brute force: V = 1 exactly on {z0 >= 2}, "
      "= 1/2 on {z0 < 2}, all 48 cells, k = 1, 2, 3", ok_b1b)
ok_b1c = all(
    ((V_class(z, k, False) != V_closed(z, T, k))
     == (2 <= z < 1 + T and k >= 2))
    for z in GRID for T in TOS for k in (1, 2, 3, 4))
check("B1c class difference located exactly: timing cells (2 <= z0 < 1+T_obs) "
      "for k >= 2; coincide at k = 1 and elsewhere", ok_b1c)

# ---------------- Layer 2b: minimal-mass bound attained (two-floor) ------------
def two_floor_V(b0):
    G1 = [(Q(1), Q(0)), (Q(0), Q(1))]
    return max(a[0] * b0[0] + a[1] * b0[1] for a in G1)
b0 = (Q(1, 2), Q(1, 2))
V1 = two_floor_V(b0)
check("B2 two-floor: Gamma_1 value = 1/2 at symmetric prior; deficit = 1/2 = "
      "1 - min mass attained", V1 == Q(1, 2) and Q(1) - V1 == min(b0))

# ---------------- Layer 2c: jump loci from the closed form ---------------------
ok_jump = True
for T in TOS:
    for k in (1, 2, 3):
        threshold = 1 + min(k, T) if k <= T else 1 + T
        for i, z in enumerate(GRID[:-1]):
            d = V_closed(GRID[i + 1], T, k) - V_closed(z, T, k)
            if z == threshold - Q(1, 10):
                ok_jump &= (d == Q(1, 2))
            else:
                ok_jump &= (d == 0)
check("B3 jump loci: +1/2 exactly at z0 = 1 + min(k, T_obs); flat elsewhere",
      ok_jump)

# ---------------- Layer 3: text needles -----------------------------------------
tex = open(os.path.join(HERE, "paper2_belief_state_v1.tex"), encoding="utf-8").read()
tex = " ".join(tex.split())
NEEDLES = [
    "\\mathrm{supp}\\bigl(b^{+}(\\cdot \\mid a, y)\\bigr)",
    "1 - V_{k}(b) \\;\\ge\\; \\min_{x \\in \\mathrm{supp}(b)} b(x)",
    "384", "48 audited cells", "k \\le 4",
    "21/10", "T_{\\mathrm{learn}}}{10}", "|K| = 5, 4, 3, 2",
    "z_{0} = 1 + \\min(k, T_{\\mathrm{obs}})", "(2, 1)" if False else "\\Gamma_{1} = \\{(1,0), (0,1)\\}",
    "V_{k}(b_{0}) = \\tfrac{1}{2}", "branch separation", "\\tfrac{3}{10}",
    "g \\in \\{1, 2\\}", "16 of 16", "timing cells",
    "\\frac{21}{10} \\;+\\; \\frac{T_{\\mathrm{learn}}}{10}",
    "piecewise linear", "absorbing unsafe state",
]
missing = [n for n in NEEDLES if n not in tex]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")
check("declarations use separate headings with the responsibility wording",
      "\\subsection*{Funding}" in tex and "\\subsection*{Competing interests}" in tex
      and "\\subsection*{Data availability}" in tex and "\\subsection*{Code availability}" in tex
      and "\\subsection*{AI declaration}" in tex
      and "The author reviewed and edited outputs and takes responsibility for the final work." in tex)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass "
      f"(chained per-system scripts: {total_chained}/21)")
raise SystemExit(0 if n_pass == len(PASS) else 1)
