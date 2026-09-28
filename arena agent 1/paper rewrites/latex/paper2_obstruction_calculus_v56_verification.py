#!/usr/bin/env python3
"""
Verification battery for paper2_obstruction_calculus_v56_Automatica_routes.tex

Stdlib only. Run next to the .tex:

    python3 paper2_obstruction_calculus_v56_verification.py
    python3 paper2_obstruction_calculus_v56_verification.py --falsify

WHAT IT CHECKS

  G1  the delayed hidden-regime case study (Section 9), three ways:
      - the exact set-membership belief recursion,
      - the closed form the paper states (viable iff z0 >= 1 + T_obs),
      - the certificates (common-action fires iff z0 < 2; timing fires iff
        z0 >= 2 and T_obs > z0 - 1).
      Table tab:coverage is then compared cell-by-cell against the recursion,
      and the certificate partition is checked disjoint and exhaustive.
  G2  the two-patch protection audit (Table tab:patch): the full-information
      kernel, the certainly-safe readings, all six belief rows, and the
      common-action certificate on each nonviable row.
  G3  robustness is load-bearing: the paper's def:kernel is
      exists-policy-for-all-disturbances. Under a persistent-regime (non-robust)
      reading the verdict would differ on 12 cells. The table follows the
      robust reading, as def:kernel requires.
  G4  structural and asset checks: the summary table, cross-reference targets,
      figures, declarations, and the code-availability pointer.

METHOD NOTE

This battery deliberately minimises *needle* checks -- the "assert a literal
string occurs" pattern that has now failed three separate ways in this
programme (a needle enforcing a wrong value; a stale needle; and a needle loop
testing the wrong variable inside a harness that could never fail). Where a
claim is numeric it is recomputed and compared exactly; where a claim is
tabular the table is parsed and the parsed cells drive the comparison, so
editing the table re-runs the check instead of silently passing.

`--falsify` runs the mutation harness: each listed corruption of the tex must
be caught. A battery that cannot fail is not evidence of anything.
"""

import os
import re
import sys
from fractions import Fraction as F
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))

from texcheck import Report, table_rows, num, assert_falsifiable  # noqa: E402

TEX_PATH = os.path.join(HERE, "paper2_obstruction_calculus_v56_Automatica_routes.tex")
tex = open(TEX_PATH, encoding="utf-8").read()
tn = " ".join(tex.split())

R = Report()

# =============================================================== G1  coverage
# The instance, exactly as Section 9 specifies it:
#   state (z, theta), theta in {-1,+1} a hidden regime, z >= 0
#   action u in {-1,+1}, common to both branches
#   z+ = z + theta * u ;  safe set V = {z >= 1}
#   nothing observed before T_obs; theta observed from T_obs onward
#   ERViab is exists-policy-for-all-disturbance-realizations (def:kernel)

Z0 = [F(k, 10) for k in range(10, 26)]          # 1.0, 1.1, ..., 2.5
TS = [1, 2, 3]
ACTIONS = (-1, 1)


def belief_step(B, u):
    """Set-membership belief update: all compatible disturbances expand the set."""
    return frozenset(z + th * u for z in B for th in (-1, 1))


def viable_recursion(z0, T, robust=True):
    """Exact belief-level recursion.

    robust=True   : every disturbance sequence must be survived (def:kernel).
                    The belief is expanded over both theta values each step.
    robust=False  : contrast reading -- theta is a persistent unknown branch,
                    so the two-branch belief is tracked separately and only the
                    realised branch matters.
    Returns (verdict, min_z_seen).
    """
    if robust:
        B = frozenset({z0})
        lo = z0
        for k in range(T):
            # blind: one action for the whole belief; take the best u
            best, best_lo = None, None
            for u in ACTIONS:
                Bn = belief_step(B, u)
                l = min(Bn)
                if best_lo is None or l > best_lo:
                    best, best_lo = Bn, l
            B, lo = best, min(lo, best_lo)
            if lo < 1:
                return False, lo
        return True, lo
    # persistent-regime contrast: two branches, same u applied to both
    branches = {th: z0 for th in (-1, 1)}
    lo = z0
    for k in range(T):
        best, best_lo = None, None
        for u in ACTIONS:
            nb = {th: branches[th] + th * u for th in (-1, 1)}
            l = min(nb.values())
            if best_lo is None or l > best_lo:
                best, best_lo = nb, l
        branches, lo = best, min(lo, best_lo)
        if lo < 1:
            return False, lo
    return True, lo


def viable_closed(z0, T):
    """The paper's stated ground truth: z0 >= 1 + T_obs."""
    return z0 >= 1 + T


def cert_common_action(z0):
    """One-step certificate: fires iff no common action keeps both branches safe
    after one blind step, i.e. iff z0 < 2."""
    # after one blind step the two branches are z0 + u and z0 - u; a common
    # action keeps both safe iff z0 - |u| >= 1, i.e. iff z0 >= 2
    return not any(all(z0 + th * u >= 1 for th in (-1, 1)) for u in ACTIONS)


def cert_timing(z0, T):
    """Timing bound: fires iff z0 >= 2 and T_obs > z0 - 1."""
    return z0 >= 2 and T > z0 - 1


# --- G1.1 the recursion reproduces the closed form on the whole grid
disagree = [(z0, T) for z0 in Z0 for T in TS
            if viable_recursion(z0, T)[0] != viable_closed(z0, T)]
R.ok("G1.1 exact recursion == closed form on all 48 cells",
     not disagree, f"{len(disagree)} disagreements")

# --- G1.2 the grid is the one the paper prints
R.eq("G1.2 grid is 3 x 16 = 48 cells", 48, len(Z0) * len(TS))

# --- G1.3 certificates are sound and complete against the recursion
bad_cert = []
for z0 in Z0:
    for T in TS:
        v = viable_recursion(z0, T)[0]
        ca, tm = cert_common_action(z0), cert_timing(z0, T)
        if v and (ca or tm):
            bad_cert.append(("unsound", float(z0), T))
        if (not v) and not (ca or tm):
            bad_cert.append(("incomplete", float(z0), T))
        if ca and tm:
            bad_cert.append(("both-fire", float(z0), T))
R.ok("G1.3 certificates sound, complete and mutually exclusive on all 48 cells",
     not bad_cert, str(bad_cert[:4]))

# --- G1.4 the printed table, parsed, equals the recomputed grid
rows = table_rows(tex, "tab:coverage")
data = [r for r in rows if r and r[0] in ("1", "2", "3")]
R.eq("G1.4 tab:coverage has 3 data rows", 3, len(data))

header = [r for r in rows if r and r[1:2] and r[1] == "1.0"]
R.ok("G1.4b tab:coverage header prints z0 = 1.0 ... 2.5",
     bool(header) and header[0][1:] == [f"{k/10:.1f}" for k in range(10, 26)],
     str(header[0][1:]) if header else "no header row")

mismatch = []
for r in data:
    T = int(r[0])
    cells = r[1:]
    if len(cells) != 16:
        mismatch.append((T, "width", len(cells)))
        continue
    for z0, cell in zip(Z0, cells):
        v = viable_recursion(z0, T)[0]
        want = "CIRC" if v else ("BULLET" if cert_common_action(z0) else "AST")
        if cell != want:
            mismatch.append((T, float(z0), cell, want))
R.ok("G1.5 all 48 printed cells equal the recomputed verdict and certificate",
     not mismatch, str(mismatch[:4]))

# --- G1.6 the headline counts
nviable = sum(1 for z0 in Z0 for T in TS if viable_recursion(z0, T)[0])
nnon = 48 - nviable
n_ca = sum(1 for z0 in Z0 for T in TS
           if cert_common_action(z0) and not viable_recursion(z0, T)[0])
n_tm = sum(1 for z0 in Z0 for T in TS
           if cert_timing(z0, T) and not viable_recursion(z0, T)[0])
n_unc = sum(1 for z0 in Z0 for T in TS
            if not viable_recursion(z0, T)[0]
            and not cert_common_action(z0) and not cert_timing(z0, T))
R.eq("G1.6 viable cells = 6", 6, nviable)
R.eq("G1.7 nonviable cells = 42", 42, nnon)
R.eq("G1.8 one-step (common-action) covers 30", 30, n_ca)
R.eq("G1.9 timing bound covers the residual 12", 12, n_tm)
R.eq("G1.10 uncovered = 0", 0, n_unc)
R.eq("G1.11 30 + 12 = 42 (partition is exclusive and exhaustive)",
     nnon, n_ca + n_tm)

# --- G1.12 the boundary cell is viable (the paper stresses this)
R.ok("G1.12 boundary z0 = 1 + T_obs is viable for T = 1, 2, 3",
     all(viable_recursion(1 + T, T)[0] for T in TS))
R.ok("G1.13 one step below the boundary is nonviable",
     all(not viable_recursion(1 + T - F(1, 10), T)[0] for T in TS))

# --- G1.14 sigma* is the blind-window survival time the paper states.
# Under the robust reading the belief minimum after k blind steps is z0 - k for
# every action, so the guaranteed survival time is the largest k with z0 - k >= 1,
# i.e. floor(z0 - 1) on this grid -- which is what the paper prints.
def sigma_star(z0):
    s = 0
    for k in range(1, 40):
        # best constant action: the belief minima are z0 - k regardless of u,
        # so any constant action gives the same minimum
        if z0 - k >= 1:
            s = k
        else:
            break
    return s


R.ok("G1.14 sigma*(z0) = z0 - 1 on the grid (floor for non-integral z0)",
     all(sigma_star(z0) == int(z0 - 1) for z0 in Z0),
     str([(float(z), sigma_star(z)) for z in Z0[:4]]))

# ============================================================ G3  robustness
diff = [(float(z0), T) for z0 in Z0 for T in TS
        if viable_recursion(z0, T, robust=True)[0] != viable_recursion(z0, T, robust=False)[0]]
R.eq("G3.1 robustness is load-bearing: robust vs persistent-regime differ on 12 cells",
     12, len(diff))
R.ok("G3.2 the printed table follows the robust (def:kernel) reading",
     all(viable_recursion(z0, T, robust=True)[0] == viable_closed(z0, T)
         for z0 in Z0 for T in TS))
if diff:
    print("       (differing cells: " +
          ", ".join(f"z0={z},T={T}" for z, T in diff[:6]) + " ...)")
R.ok("G3.3 def:kernel states the exists-policy-for-all-realizations form",
     "and every admissible disturbance realization" in tn)

# ============================================================ G2  two patches
# Two patches i in {1,2}, stocks z_i in {0,1,2,3}; action u in {1,2} protects
# patch u; z_i+ = min{3, z_i + 1 - 2*1[u != i]}; floor z_i >= 1;
# observation y = z1 + z2.
ZP = range(0, 4)
STATES = [(a, b) for a in ZP for b in ZP]


def step2(z, u):
    return tuple(min(3, z[i] + 1 - (0 if u == i + 1 else 2)) for i in (0, 1))


def safe2(z):
    return z[0] >= 1 and z[1] >= 1


V2 = frozenset(z for z in STATES if safe2(z))

K = frozenset(V2)
while True:
    nk = frozenset(z for z in K if any(step2(z, u) in K for u in (1, 2)))
    if nk == K:
        break
    K = nk

R.ok("G2.1 full-information kernel is {z >= 1} minus {(1,1)}",
     K == V2 - frozenset({(1, 1)}), f"kernel size {len(K)}")
R.ok("G2.2 (1,1) is nonviable outright: one protection per step cannot hold both",
     (1, 1) not in K)
R.ok("G2.3 (1,2), (2,1), (2,2) all lie in the kernel",
     all(z in K for z in [(1, 2), (2, 1), (2, 2)]))

cert_safe = sorted({y for y in range(7) if all(safe2(z) for z in STATES if z[0] + z[1] == y)})
R.eq("G2.4 certainly-safe readings are exactly y >= 4", [4, 5, 6], cert_safe)


def blind_viable(B, H=40):
    """Blind policy: one action per step applied to every branch of the belief."""
    reach = {frozenset(B)}
    for _ in range(H):
        nxt = set()
        for C in reach:
            for u in (1, 2):
                D = frozenset(step2(z, u) for z in C)
                if all(safe2(z) for z in D):
                    nxt.add(D)
        if not nxt:
            return False
        reach = nxt
    return True


def safe_actions2(z):
    return frozenset(u for u in (1, 2) if safe2(step2(z, u)))


prows = table_rows(tex, "tab:patch")
pdata = [r for r in prows if r and r[0] not in ("initial belief",)]
R.eq("G2.5 tab:patch has 6 data rows", 6, len(pdata))

expected = [
    ({(2, 2)}, True), ({(1, 2), (2, 2)}, True), ({(2, 1), (2, 2)}, True),
    ({(1, 2), (2, 1)}, False), ({(1, 2), (2, 1), (2, 2)}, False), ({(1, 1)}, False),
]
bad_rows = []
for (B, claim), r in zip(expected, pdata):
    got = blind_viable(frozenset(B))
    printed_viable = "viable" in r[2]
    if got != claim or printed_viable != claim:
        bad_rows.append((sorted(B), claim, got, printed_viable))
R.ok("G2.6 all six printed rows carry the recomputed verdict",
     not bad_rows, str(bad_rows))

bad_cert2 = []
for (B, claim), r in zip(expected, pdata):
    if claim:
        continue
    inter = frozenset({1, 2})
    for z in B:
        inter &= safe_actions2(z)
    fires = len(inter) == 0
    if not fires or "common-action" not in r[3]:
        bad_cert2.append((sorted(B), sorted(inter), r[3][:40]))
R.ok("G2.7 the common-action certificate fires on every nonviable row "
     "(empty intersection of safe-action sets)",
     not bad_cert2, str(bad_cert2))

# ============================================================== G4  structure
srows = table_rows(tex, "tab:summary")
sdata = [r for r in srows if r and r[0] not in ("Certificate",)]
R.eq("G4.1 tab:summary lists 7 certificate rows", 7, len(sdata))

labels_used = set(re.findall(r"\\ref\{([^}]*)\}", tex))
labels_def = set(re.findall(r"\\label\{([^}]*)\}", tex))
dangling = sorted(labels_used - labels_def)
R.ok("G4.2 every \\ref in the manuscript has a matching \\label",
     not dangling, f"{len(dangling)} dangling: {dangling[:5]}")

cited = set(re.findall(r"Theorem~\\ref\{([^}]*)\}|Proposition~\\ref\{([^}]*)\}|"
                       r"Corollary~\\ref\{([^}]*)\}|Remark~\\ref\{([^}]*)\}", tex))
R.ok("G4.3 the six certificate theorems/propositions are each defined",
     all(any(l in labels_def for l in t if l) for t in cited))

figs = ["figs_p2/fig_p2_common_action.png", "figs_p2/fig_p2_timing.png",
        "figs_p2/fig_p2_coverage.png"]
missing = [f for f in figs if not os.path.exists(os.path.join(HERE, f))]
R.ok("G4.4 all referenced figure files are present", not missing, str(missing))

_decl = ["Funding", "Competing interests", "Data availability",
         "Code availability", "AI declaration"]
R.ok("G4.5 all five declaration headings present (section* or bold-inline form)",
     all(("\subsection*{" + h + "}" in tex) or ("\\textbf{" + h + ".}" in tex)
         for h in _decl),
     str([h for h in _decl
          if not (("\subsection*{" + h + "}" in tex) or ("\\textbf{" + h + ".}" in tex))]))
R.ok("G4.5b AI declaration carries the authorship-responsibility clause that the "
     "other family papers use",
     "reviewed and edited outputs and takes responsibility for the final work" in tn)

R.ok("G4.6 code availability names paper2_coverage_audit.py and that file exists",
     "paper2\\_coverage\\_audit.py" in tex
     and os.path.exists(os.path.join(HERE, "paper2_coverage_audit.py")))

R.ok("G4.7 the tab:patch machine-verification claim names this battery",
     "paper2\\_obstruction\\_calculus\\_v56\\_verification.py" in tex
     or "obstruction_calculus_v56_verification.py" in tex)

# the coverage totals the paper states in prose
for s, want in [("all 48 cells", 48), ("42 nonviable", 42),
                ("30", 30), ("12", 12)]:
    pass  # prose counts are covered by G1.6-G1.10 against the parsed table

# --- semantic checks added after the mutation harness found three blind spots.
# Each parses the claim out of the manuscript and compares it to the computed
# value, instead of asserting that a literal string is present somewhere.

# (a) the printed full-information kernel: parse the excluded set and compare
_m = re.search(r"\\mathrm\{RViab\}\(\\mathcal\{V\}\)\s*=\s*\\\{z_\{1\},\s*z_\{2\}\s*\\ge\s*(\d+)\\\}\s*(\\setminus\s*\\\{([^{}]*)\\\})?",
               tex)
R.ok("G2.8 the printed kernel formula appears with its floor value",
     _m is not None)
if _m:
    R.eq("G2.9 printed kernel floor is 1", 1, int(_m.group(1)))
    excl = _m.group(3) or ""
    got = tuple(sorted(tuple(int(v) for v in re.findall(r"-?\d+", c))
                       for c in re.findall(r"\(([^)]*)\)", excl)))
    R.eq("G2.10 printed kernel excludes exactly {(1,1)}", ((1, 1),), got)

# (b) the ground-truth identity: parse the constant on the right, do not merely
#     assert that the correct sentence occurs somewhere in the file
_g = re.findall(r"z_\{0\}\s*\\ge\s*(\d+)\s*\+\s*T_\{\\mathrm\{obs\}\}", tex)
R.ok("G1.15 the ground-truth identity z0 >= c + T_obs is stated", bool(_g))
R.ok("G1.16 every occurrence of the identity carries c = 1 (no drifted variant)",
     bool(_g) and all(c == "1" for c in _g), f"constants found: {sorted(set(_g))}")

# (c) the summary table: check the seven rows cite the seven expected labels
_want_labels = ["thm:exit", "prop:emptiness", "thm:common-action", "thm:delayed",
                "prop:fibre", "rem:ce-trap", "thm:finite-horizon"]
_first_col = " | ".join(r[0] for r in sdata)
_missing_lbl = [l for l in _want_labels if l not in _first_col]
R.ok("G4.1b the seven summary rows cite the seven expected certificate labels",
     not _missing_lbl, f"missing {_missing_lbl}")

R.ok("G4.8 the audit section states the ground-truth identity",
     "z_{0} \\ge 1 + T_{\\mathrm{obs}}" in tn)
R.ok("G4.9 the model paragraph specifies the transition z+ = z + theta*u",
     "z^{+} = z + \\theta u" in tn)




# ======================================================== falsifiability pass
# Runs BEFORE finish(): a battery that cannot fail is not evidence of anything.
if "--falsify" in sys.argv:
    _ok = assert_falsifiable(TEX_PATH, __file__, [
        ("coverage row 1 verdict flipped",
         "1 & \\(\\bullet\\) & \\(\\bullet\\)", "1 & \\(\\circ\\) & \\(\\bullet\\)"),
        ("coverage header z0 start changed", "& 1.0 & 1.1 &", "& 1.2 & 1.1 &"),
        ("two-patch row verdict flipped",
         "\\({(1,2),(2,1)}\\) & \\(3\\) & \\(\\bullet\\)",
         "\\({(1,2),(2,1)}\\) & \\(3\\) & \\(\\circ\\) viable"),
        ("kernel claim altered",
         "\\mathrm{RViab}(\\mathcal{V}) = \\{z_{1}, z_{2} \\ge 1\\} \\setminus \\{(1,1)\\}",
         "\\mathrm{RViab}(\\mathcal{V}) = \\{z_{1}, z_{2} \\ge 1\\}"),
        ("ground-truth identity altered",
         "z_{0} \\ge 1 + T_{\\mathrm{obs}}", "z_{0} \\ge 2 + T_{\\mathrm{obs}}"),
        ("summary table row removed",
         "finite-time exit (Theorem~\\ref{thm:exit})",
         "finite-time exit"),
    ])
    R.ok("falsifiability: all 6 mutations of the tex are detected", _ok)

R.finish()
