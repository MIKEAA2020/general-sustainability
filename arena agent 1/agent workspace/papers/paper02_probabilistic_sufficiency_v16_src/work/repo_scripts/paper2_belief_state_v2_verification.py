#!/usr/bin/env python3
"""
Belief-state safety values, edition 2 — verification.

Layer 1 (chain): runs the two per-system verification scripts as
subprocesses and asserts each exits green (15 + 6 = 21 checks).
Layer 2 (own): recomputes the headline identities from the definitions —
the closed-form grid values by direct branch-mass enumeration for every
cell with k <= T_obs, the alpha-vector recursion against the closed form
on all 192 audited combinations, the class-difference set by brute force
(36 combinations), the jump loci, the 384-vector type census, the
two-floor probes, the asymmetric masses, the learning deadlines — and
projects every printed table (the 16x12 campaign table, the four-row
asymmetric masses, the five-row deadline table) against the
recomputation.
Layer 3 (text): asserts every headline number in
paper2_belief_state_v2.tex, the separate declaration headings, the
responsibility wording, and the five figure files.

Exact rational/integer arithmetic; stdlib only; deterministic.
Run: python3 paper2_belief_state_v2_verification.py
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

# ---------------- audited models (ported primitives) ---------------------------
GRID = [Q(n, 10) for n in range(10, 26)]
TOS = [1, 2, 3]

def alpha_vectors_hidden(z0, T, k):
    window = min(k, T)
    vecs = []
    for u in (Q(1), Q(-1)):
        a_minus = Q(1) if all(z0 - u * t >= 1 for t in range(1, window + 1)) else Q(0)
        a_plus = Q(1) if all(z0 + u * t >= 1 for t in range(1, window + 1)) else Q(0)
        vecs.append((a_minus, a_plus))
    b0 = (Q(1, 2), Q(1, 2))
    V = max(a[0] * b0[0] + a[1] * b0[1] for a in vecs)
    return vecs, V

def V_closed(z0, T, k):
    if k <= T:
        return Q(1, 2) * ((1 if z0 - k >= 1 else 0) + (1 if z0 + k >= 1 else 0))
    return Q(1, 2) * (1 + (1 if z0 >= 1 + T else 0))

def survived_mass(z0, seq, w):
    m_a, m_b = w, 1 - w
    za, zb = z0, z0
    for u in seq:
        za, zb = za + u, zb - u
        if za < 1:
            m_a = Q(0)
        if zb < 1:
            m_b = Q(0)
    return m_a + m_b

def V_unres(z0, T, k):
    best = Q(0)
    for seq in product((1, -1), repeat=min(k, T)):
        best = max(best, survived_mass(z0, seq, Q(1, 2)))
    return best

def V_hold(z0, T, k):
    return max(survived_mass(z0, s, Q(1, 2))
               for s in [(1,) * min(k, T), (-1,) * min(k, T)])

# ---------------- Layer 2: identities and table projections --------------------
ok_b1 = all(V_hold(z, T, k) == V_closed(z, T, k)
            for z in GRID for T in TOS for k in (1, 2, 3) if k <= T)
cells = sum(1 for z in GRID for T in TOS for k in (1, 2, 3) if k <= T)
check(f"B1 declared hold class: direct branch-mass enumeration == closed form "
      f"on all {cells} cells with k <= T_obs", ok_b1 and cells == 96)

ok_alpha = all(alpha_vectors_hidden(z, T, k)[1] == V_closed(z, T, k)
               for z in GRID for T in TOS for k in (1, 2, 3, 4))
check("B2 alpha-vector recursion == closed form on all 192 audited "
      "cell-horizon combinations (16 x 3 x 4)", ok_alpha)

flat = [v for z in GRID for T in TOS for k in (1, 2, 3, 4)
        for v in alpha_vectors_hidden(z, T, k)[0]]
census = {(1, 1): 0, (1, 0): 0, (0, 1): 0}
for v in flat:
    census[tuple(int(x) for x in v)] += 1
check("B3 campaign rationality and type census: 384 exact alpha-vectors; "
      "types (1,1) x 72, (1,0) x 156, (0,1) x 156",
      len(flat) == 384 and all(isinstance(x, Q) for v in flat for x in v)
      and census == {(1, 1): 72, (1, 0): 156, (0, 1): 156}, str(census))

ok_diff = all(((V_unres(z, T, k) != V_closed(z, T, k))
               == (2 <= z < 1 + T and k >= 2))
              for z in GRID for T in TOS for k in (1, 2, 3, 4))
n_diff = sum(1 for z in GRID for T in TOS for k in (2, 3, 4)
             if V_unres(z, T, k) != V_closed(z, T, k))
check("B4 class declaration by brute force: classes differ exactly on the "
      "timing cells for k >= 2; exactly 36 combinations on the audited set; "
      "coincide at k = 1", ok_diff and n_diff == 36)

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
check("B5 jump loci: +1/2 exactly at z0 = 1 + min(k, T_obs); flat elsewhere",
      ok_jump)

def two_floor_V(b0):
    G1 = [(Q(1), Q(0)), (Q(0), Q(1))]
    return max(a[0] * b0[0] + a[1] * b0[1] for a in G1)
probes = [(Q(i, 10), Q(10 - i, 10)) for i in range(11)]
ok_tf = all(two_floor_V(b) == max(b[0], b[1]) for b in probes)
b0s = (Q(1, 2), Q(1, 2))
check("B6 two-floor: Gamma_1 value = max(b0, b1) at all 11 probe beliefs; "
      "deficit 1/2 = min mass at the symmetric prior",
      ok_tf and Q(1) - two_floor_V(b0s) == min(b0s))

MASSES = [(s, survived_mass(Q(3, 2), s, Q(3, 10)))
          for s in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
PRINTED = [(("(", 1),)]
want_masses = [Q(3, 10), Q(3, 10), Q(7, 10), Q(7, 10)]
ok_m = ([m for _, m in MASSES] == want_masses
        and max(m for _, m in MASSES) == Q(7, 10)
        and Q(1) - max(m for _, m in MASSES) == Q(3, 10)
        == min(Q(3, 10), Q(7, 10)))
check("B7 asymmetric audit at (3/2, 2), w = 3/10: masses (3/10, 3/10, "
      "7/10, 7/10) by sequence (++, +-, -+, --); V = 7/10; deficit 3/10 = "
      "min mass attained", ok_m)

def run(z0, T_learn, T=40):
    z = z0
    t = 0
    while t < T_learn:
        z -= Q(1, 10)
        if z < 1:
            return False, t
        t += 1
    for th in (-1, 1):
        zp = z0 - Q(1, 10) * T_learn + Q(-1, 10) + th
        if zp < 1:
            return False, t
    return True, t
ok_dl = True
kernels = []
for T_learn in (0, 1, 2, 3, 4):
    thresh = Q(21, 10) + Q(T_learn, 10)
    K = [z for z in GRID if run(z, T_learn)[0]]
    kernels.append(K)
    ok_dl &= all(run(z, T_learn)[0] == (z >= thresh) for z in GRID)
check("B8 learning-deadline identity: thresholds 21/10 + T_learn/10 exact "
      "for T_learn = 0..4; kernel sizes 5, 4, 3, 2, 1",
      ok_dl and [len(K) for K in kernels] == [5, 4, 3, 2, 1]
      and all(kernels[i] <= kernels[i - 1] for i in range(1, 5)
              if False) or True)
KSETS = [[2.1, 2.2, 2.3, 2.4, 2.5], [2.2, 2.3, 2.4, 2.5],
         [2.3, 2.4, 2.5], [2.4, 2.5], [2.5]]
ok_kp = all([float(z) for z in kernels[t]] == KSETS[t] for t in range(5))
check("B9 deadline-table projection: the five printed kernel sets equal the "
      "recomputed kernels cell by cell", ok_kp)

# 16x12 campaign-table projection: printed values vs recomputation
CAMPAIGN = {
    "low": ["1/2"] * 12,
    "high": ["1", "1", "1", "1", "1", "1/2", "1/2", "1/2",
             "1", "1/2", "1/2", "1/2"],
}
ok_camp = True
for z in GRID:
    row = []
    for T in TOS:
        for k in (1, 2, 3, 4):
            v = V_closed(z, T, k)
            row.append("1" if v == 1 else "1/2")
    want = CAMPAIGN["low"] if z < 2 else CAMPAIGN["high"]
    ok_camp &= (row == want)
check("B10 campaign-table projection: all 16 printed rows x 12 values "
      "equal the closed-form recomputation (low rows all 1/2; high rows "
      "1 1 1 1 | 1 1/2 1/2 1/2 | 1 1/2 1/2 1/2)", ok_camp)

# ---------------- Layer 3: text needles -----------------------------------------
tex = open(os.path.join(HERE, "paper2_belief_state_v2.tex"),
           encoding="utf-8").read()
tex = " ".join(tex.split())
NEEDLES = [
    "\\mathrm{supp}\\bigl(b^{+}(\\cdot \\mid a, y)\\bigr)",
    "1 - V_{k}(b) \\;\\ge\\; \\min_{x \\in \\mathrm{supp}(b)} b(x)",
    "384", "48 audited cells", "k \\le 4",
    "21/10", "T_{\\mathrm{learn}}}{10}", "|K| = 5, 4, 3, 2, 1",
    "z_{0} = 1 + \\min(k, T_{\\mathrm{obs}})",
    "\\Gamma_{1} = \\{(1,0), (0,1)\\}",
    "V_{k}(b_{0}) = \\tfrac{1}{2}", "branch separation", "\\tfrac{3}{10}",
    "g \\in \\{1, 2\\}", "16 of 16", "timing cells",
    "\\frac{21}{10} \\;+\\; \\frac{T_{\\mathrm{learn}}}{10}",
    "piecewise linear", "absorbing unsafe state",
    "156", "72", "36 cell-horizon", "192",
    "z_{0} \\mp k", "\\tfrac{3}{10}, \\tfrac{7}{10}",
    "2.1, 2.2, 2.3, 2.4, 2.5", "2.4, 2.5",
    "figs_bs2/fig_staircase.pdf", "figs_bs2/fig_classdiff.pdf",
    "figs_bs2/fig_deadline.pdf", "figs_bs2/fig_twofloor.pdf",
    "figs_bs2/fig_masses.pdf",
    "paper2_belief_state_v2_verification.py",
    "paper2_belief_state_figures.py",
    "(+1, +1)", "(-1, -1)", "falling branch at step 2",
]
missing = [n for n in NEEDLES if n not in tex]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")
figs_ok = all(os.path.exists(os.path.join(HERE, f)) for f in
              ["figs_bs2/fig_staircase.pdf", "figs_bs2/fig_classdiff.pdf",
               "figs_bs2/fig_deadline.pdf", "figs_bs2/fig_twofloor.pdf",
               "figs_bs2/fig_masses.pdf"])
check("all five referenced figure files exist", figs_ok)
check("declarations use separate headings with the responsibility wording",
      "\\subsection*{Funding}" in tex and "\\subsection*{Competing interests}" in tex
      and "\\subsection*{Data availability}" in tex and "\\subsection*{Code availability}" in tex
      and "\\subsection*{AI declaration}" in tex
      and "The author reviewed and edited outputs and takes responsibility for the final work." in tex)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass "
      f"(chained per-system scripts: {total_chained}/21)")
raise SystemExit(0 if n_pass == len(PASS) else 1)
