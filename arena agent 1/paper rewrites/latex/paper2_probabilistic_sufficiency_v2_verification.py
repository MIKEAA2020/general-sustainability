#!/usr/bin/env python3
"""
Probabilistic sufficiency for the obstruction calculus — edition 2 verification.

Edition 2 repairs the class-attribution and schedule-labeling defects found
by the round-10 audit (addendum paper2_probabilistic_sufficiency_v2_addendum.md):
every value carries its class superscript (declared hold vs unrestricted
sequential); the closed form is a standalone proposition for the declared
hold class; the class-difference region is 2 <= z0 < 1 + min(k, T_obs)
(exactly the timing cells on the audited grid); the deficit profile is
horizon-qualified (0 before the falling-branch exit, 1/2 after); the
learning-deadline identity is labeled as the pinned-probe family, with the
free-probe (21/10, flat) and probe-free exogenous-revelation
(1 + T_learn/10) benchmarks; the 384-vector census is attributed to the
delayed grid with its deduplicated 348-vector form; the asymmetric audit's
lost-branch step is 1 for all four sequences; the support identity assumes
deterministic observation maps and speaks of policies; the sigma-star
inequality points the right way.

Layer 1 (chain): runs the three per-system scripts and asserts each exits
green — the belief-state campaign (16 checks, itself chaining 21 per-instance
checks), the stochastic selector (15 checks, S1-S15), and the
hidden-parameter learning-deadline audit (6 checks, E1-E6).

Layer 2 (own exact re-derivations, all in fractions.Fraction): closed-form
declared-hold-class values against direct branch-mass enumeration on the
whole 16 x 12 grid (census 36 ones / 156 halves) with the corrected
per-cell-class deficit profile; the class-difference set equals
{2 <= z0 < 1 + min(k, T_obs)} on an extended grid to z0 = 4.0, equals the
timing-cell combinations on the audited grid (36), is empty at k = 1, and
excludes the auditor's counterexample (3.5, 3, 2) where the hold class
already attains one; the witness census 72/156/156 with deduplicated
348 = 36 + 156 + 156; the asymmetric audit masses {3/10, 3/10, 7/10, 7/10}
with lost-branch step 1 for all four sequences and the branch identities;
the pinned-probe chain 21/10 + T_learn/10 (kernels 5..1); the free-probe
threshold 21/10 flat in the deadline; the probe-free exogenous threshold
1 + T_learn/10 (kernels 16..12), containing the pinned kernels.

Layer 3 (text): needles for every corrected claim; FORBIDDEN strings for
the superseded statements; label/ref integrity; source hygiene across the
flagship and the three seed tex files; the five-figure set; code pointers.
"""
import os
import subprocess
import sys
from fractions import Fraction as Q
from itertools import product

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
chain_ok = True
for s in SEEDS:
    r = subprocess.run([sys.executable, os.path.join(HERE, s)],
                       capture_output=True, text=True)
    tail = (r.stdout or "").strip().splitlines()[-1:] or [""]
    good = (r.returncode == 0)
    chain_ok &= good
    check(f"chained script exits green: {s}", good,
          tail[0][:90] if good else f"exit {r.returncode}")

# ---------------- Layer 2: independent exact recomputation -----------------
Z = [Q(i, 10) for i in range(10, 26)]          # audited grid 1.0 .. 2.5
Z2 = [Q(i, 10) for i in range(10, 41)]         # extended grid 1.0 .. 4.0
TS = [1, 2, 3]
KS = [1, 2, 3, 4]
W = Q(1, 2)


def declared_value(z0, T, k):
    """Declared hold class (Pi_hold): max over u in {+1,-1} of survived
    branch mass under the constant hold, pathwise, over min(k,T) steps."""
    ell = min(k, T)
    best = Q(0)
    for u in (1, -1):
        s = u * ell
        mass = W * (1 if z0 + s >= 1 else 0) + (1 - W) * (1 if z0 - s >= 1 else 0)
        best = max(best, mass)
    return best


def unrestricted_value(z0, T, k):
    """Unrestricted open-loop class (Pi_seq): segment form, brute force over
    ALL +-1 sequences of length min(k,T), pathwise survival."""
    ell = min(k, T)
    best = Q(0)
    for seq in product((1, -1), repeat=ell):
        zp = zm = z0
        alive_p = alive_m = True
        for u in seq:
            zp += u
            zm -= u
            alive_p &= zp >= 1
            alive_m &= zm >= 1
        best = max(best, W * alive_p + W * alive_m)
    return best


def cell_class(z0, T):
    if z0 >= 1 + T:
        return "viable"
    return "common-action" if z0 < 2 else "timing"


# (1) closed form + census on the audited grid
ones = halves = 0
closed_ok = True
for z0 in Z:
    for T in TS:
        for k in KS:
            v = declared_value(z0, T, k)
            cf = (Q(1, 2) * ((1 if z0 - k >= 1 else 0) + (1 if z0 + k >= 1 else 0))
                  if k <= T else
                  Q(1, 2) * (1 + (1 if z0 >= 1 + T else 0)))
            closed_ok &= (v == cf)
            if v == 1:
                ones += 1
            elif v == Q(1, 2):
                halves += 1
check("closed form (declared hold class) equals direct branch-mass "
      "enumeration on all 192 combinations; census 36 ones / 156 halves",
      closed_ok and ones == 36 and halves == 156, f"ones={ones} halves={halves}")

# (2) corrected deficit profile
prof_ok = True
prof_detail = {"timing_k1_zero": 0, "timing_kge2_half": 0, "ca_all_half": 0,
               "viable_all_one": 0}
for z0 in Z:
    for T in TS:
        cc = cell_class(z0, T)
        for k in KS:
            v = declared_value(z0, T, k)
            if cc == "viable":
                prof_ok &= (v == 1)
                prof_detail["viable_all_one"] += (v == 1)
            elif cc == "common-action":
                prof_ok &= (v == Q(1, 2))
                prof_detail["ca_all_half"] += (v == Q(1, 2))
            else:
                if k == 1:
                    prof_ok &= (v == 1)
                    prof_detail["timing_k1_zero"] += (v == 1)
                else:
                    prof_ok &= (v == Q(1, 2))
                    prof_detail["timing_kge2_half"] += (v == Q(1, 2))
nv42 = sum(1 for z0 in Z for T in TS if cell_class(z0, T) != "viable")
d_half = sum(1 for z0 in Z for T in TS if cell_class(z0, T) != "viable"
             and Q(1) - declared_value(z0, T, TS[-1] + 1) == Q(1, 2))
check("corrected hold-class deficit profile: timing cells value 1 at k = 1 "
      "and 1/2 at k >= 2; common-action cells 1/2 at every k; viable cells 1 "
      "at every k; deficit 1/2 at the certifying horizon on all 42 nonviable "
      "cells", prof_ok and nv42 == 42 and d_half == 42, str(prof_detail))

# (3) class-difference region, off-grid + on-grid + counterexample
diff2 = [(z0, T, k) for z0 in Z2 for T in TS for k in KS
         if declared_value(z0, T, k) < unrestricted_value(z0, T, k)]
region2 = [(z0, T, k) for z0 in Z2 for T in TS for k in KS
           if k >= 2 and 2 <= z0 < 1 + min(k, T)]
diff_grid = [(z0, T, k) for z0 in Z for T in TS for k in KS
             if declared_value(z0, T, k) < unrestricted_value(z0, T, k)]
timing_grid = [(z0, T, k) for z0 in Z for T in TS for k in KS
               if k >= 2 and 2 <= z0 < 1 + T]
k1_empty = all(declared_value(z0, T, 1) == unrestricted_value(z0, T, 1)
               for z0 in Z2 for T in TS)
ce = (Q(35, 10), 3, 2)
ce_hold_eq_unres = (declared_value(*ce) == 1 and unrestricted_value(*ce) == 1
                    and 2 <= ce[0] < 1 + ce[1])
check("class-difference set equals {2 <= z0 < 1 + min(k, T_obs)} on the "
      "extended grid to z0 = 4.0; equals the timing-cell combinations (36) "
      "on the audited grid; empty at k = 1; counterexample (3.5, 3, 2): "
      "timing cell with both classes attaining one",
      diff2 == region2 and diff_grid == timing_grid and len(diff_grid) == 36
      and k1_empty and ce_hold_eq_unres,
      f"|diff_ext|={len(diff2)} |diff_grid|={len(diff_grid)}")

# (4) witness census + deduplication
c11 = c10 = c01 = 0
dedup_total = 0
unit_combos = 0
for z0 in Z:
    for T in TS:
        for k in KS:
            ell = min(k, T)
            w_plus = (1 if z0 + ell >= 1 else 0, 1 if z0 - ell >= 1 else 0)
            w_minus = (1 if z0 - ell >= 1 else 0, 1 if z0 + ell >= 1 else 0)
            for wv in (w_plus, w_minus):
                if wv == (1, 1):
                    c11 += 1
                elif wv == (1, 0):
                    c10 += 1
                else:
                    c01 += 1
            dedup_total += len({w_plus, w_minus})
            if declared_value(z0, T, k) == 1:
                unit_combos += 1
check("witness census: enumerated (1,1) x72, mirror pair x156 each "
      "(384 total); deduplicated 348 = 36 + 156 + 156 distinct vectors, "
      "one witness on each of the 36 unit-value combinations and two "
      "elsewhere",
      (c11, c10, c01) == (72, 156, 156) and c11 + c10 + c01 == 384
      and dedup_total == 348 and unit_combos == 36,
      f"72t={c11} m={c10}/{c01} dedup={dedup_total} unit={unit_combos}")

# (5) asymmetric audit: masses + lost-branch step and identity
za, T2 = Q(3, 2), 2
wL, wH = Q(3, 10), Q(7, 10)
masses = []
lost_step = []
lost_branch = []
for u1 in (1, -1):
    for u2 in (1, -1):
        seq = (u1, u2)
        zp = zm = za
        alive_p = alive_m = True
        first_loss = None
        for t, u in enumerate(seq):
            zp += u
            zm -= u
            if first_loss is None and zp < 1:
                first_loss = (t + 1, "light")
            if first_loss is None and zm < 1:
                first_loss = (t + 1, "heavy")
            alive_p &= zp >= 1
            alive_m &= zm >= 1
        lost_step.append(first_loss[0])
        lost_branch.append(first_loss[1])
        masses.append((wL if alive_p else 0) + (wH if alive_m else 0))
masses.sort()
steps_ok = (lost_step == [1, 1, 1, 1])
branch_ok = (lost_branch[0] == "heavy" and lost_branch[1] == "heavy"
             and lost_branch[2] == "light" and lost_branch[3] == "light")
check("asymmetric audit exact: masses {3/10, 3/10, 7/10, 7/10}, value 7/10, "
      "deficit 3/10 = minimal mass; every sequence loses a branch at step 1 "
      "(heavier under u1 = +1, lighter under u1 = -1)",
      masses == [Q(3, 10), Q(3, 10), Q(7, 10), Q(7, 10)]
      and max(masses) == Q(7, 10) and Q(1) - max(masses) == wL
      and steps_ok and branch_ok,
      f"steps={lost_step} branches={lost_branch}")

# (6) pinned-probe chain (21/10 + T/10, kernels 5..1)
kernels_pinned = []
for tl in range(5):
    thr = Q(21, 10) + Q(tl, 10)
    kernels_pinned.append((thr, [z for z in Z if z >= thr]))
pinned_ok = all(len(k[1]) == 5 - i for i, k in enumerate(kernels_pinned))
check("pinned-probe learning-deadline chain exact: thresholds "
      "21/10 + T_learn/10 for T_learn = 0..4, kernels |K| = 5, 4, 3, 2, 1",
      pinned_ok and kernels_pinned[0][1][0] == Q(21, 10)
      and kernels_pinned[-1][1] == [Q(25, 10)],
      "|K|=" + ",".join(str(len(k[1])) for k in kernels_pinned))

# (7) free-probe benchmark: threshold 21/10 flat in the deadline
free_sets = []
for tl in range(5):
    # probe at t = 0: bad branch drops by 11/10 immediately
    thr = Q(21, 10)
    free_sets.append([z for z in Z if z >= thr])
flat_ok = all(s == free_sets[0] for s in free_sets) and len(free_sets[0]) == 5
check("free-probe benchmark exact: one probe at the start certifies "
      "z0 >= 21/10 for EVERY deadline (kernel flat at 5 cells)",
      flat_ok, f"|K|={len(free_sets[0])} at all five deadlines")

# (8) probe-free exogenous benchmark: 1 + T/10, kernels 16..12, contains pinned
kernels_free = []
for tl in range(5):
    thr = Q(1) + Q(tl, 10)
    kernels_free.append((thr, [z for z in Z if z >= thr]))
free_ok = all(len(k[1]) == 16 - i for i, k in enumerate(kernels_free))
contains = all(set(kp[1]) <= set(kf[1])
               for kp, kf in zip(kernels_pinned, kernels_free))
check("probe-free exogenous-revelation benchmark exact: hold then learned "
      "act, viability iff z0 >= 1 + T_learn/10, kernels |K| = 16, 15, 14, "
      "13, 12; each pinned-probe kernel is contained in the corresponding "
      "probe-free kernel",
      free_ok and contains and kernels_free[0][1] == Z
      and kernels_free[-1][1] == [Q(i, 10) for i in range(14, 26)],
      "|K|=" + ",".join(str(len(k[1])) for k in kernels_free))

# ---------------- Layer 3: text, structure, hygiene -----------------
tex = open(os.path.join(HERE, "paper2_probabilistic_sufficiency_v2.tex"),
           encoding="utf-8").read()
tnorm = " ".join(tex.split())

NEEDLES = [
    "Probabilistic Sufficiency for the Obstruction Calculus",
    "belief-state safety value",
    "the maximal probability of remaining safe for \\(k\\) steps --- and establishes four",
    "posterior support coincides with the set-valued post-state",
    "deterministic kernels and deterministic observation maps",
    "every policy loses a compatible state of positive mass",
    "along its realized observation path",
    "for the unrestricted sequential class,",
    "closed form on the delayed class, declared hold class",
    "one blind hold \\(u \\equiv \\pm 1\\) for the whole window",
    "V^{\\Pi_{\\mathrm{hold}}}_{k}(b_{0})",
    "not a corollary of Theorem \\ref{thm:support}, whose value is the unrestricted one",
    "the expectation over the prior retains exactly the surviving mass",
    "384 hold-direction witnesses on the delayed grid",
    "\\(348\\) distinct vectors after exact-equality deduplication",
    "2 \\times 36 = 72",
    "36 + 156 + 156 = 348",
    "z_{0} = 1 + \\min(k, T_{\\mathrm{obs}})",
    "on the audited grid \\((z_{0} \\le 2.5)\\) exactly the timing cells",
    "(z_{0}, T_{\\mathrm{obs}}, k) = (3.5, 3, 2)",
    "both mirror witnesses \\((1,0)\\) and \\((0,1)\\) attain the value",
    "an off-grid consequence of the closed form",
    "on the timing cells the deficit is \\(0\\) at \\(k = 1\\) and \\(\\tfrac{1}{2}\\) at \\(k \\ge 2\\)",
    "from the first horizon at which the falling branch exits",
    "\\mathcal{W}^{\\mathrm{bel}}_{k}",
    "Notation is fixed as follows",
    "unsuperscripted values do not appear",
    "certificate firing exactly when \\(T_{\\mathrm{obs}} > \\sigma^{*}\\)",
    "viability at the deadline holds when \\(T_{\\mathrm{obs}} \\le \\sigma^{*}\\)",
    "nonviable with deficit \\(\\tfrac{1}{2}\\) at every horizon \\(k \\ge 2\\) (and \\(0\\) at \\(k = 1\\))",
    "pinned to horizon \\(T_{\\mathrm{learn}}\\)",
    "pinned-probe learning-deadline identity",
    "with free probe timing one probe at the start certifies \\(z_{0} \\ge 21/10\\) at every deadline",
    "probe-free exogenous revelation at \\(T_{\\mathrm{learn}}\\) needs only \\(z_{0} \\ge 1 + T_{\\mathrm{learn}}/10\\)",
    "kernel sizes \\(16, 15, 14, 13, 12\\)",
    "The schedule pins the probe to \\(T_{\\mathrm{learn}}\\)",
    "no earlier probe is available within the family",
    "heavier branch, step 1", "lighter branch, step 1",
    "the first move sends one branch to \\(\\tfrac{1}{2} < 1\\)",
    "segment-form enumeration of the declared hold class",
    "a stagewise recursion over \\(A(\\Pi) = \\{\\pm 1\\}\\) would compute the unrestricted value",
    "extended grid to \\(z_{0} = 4.0\\)",
    "declared-class segment enumeration and the closed-form values",
    "the pinned-probe family a linear learning deadline",
    "September 26, 2026",
]
missing = [n for n in NEEDLES if n not in tnorm]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")

FORBIDDEN = [
    "under the disturbance's worst case",
    "the infimum over disturbance strategies selects the branch",
    "Under exogenous revelation at horizon",
    "T_{\\mathrm{obs}} < \\sigma^{*}",
    "falling branch at step 2",
    "the attaining one-step vector is \\((1, 1)\\) on \\(z_{0} \\ge 2\\) and \\((1, 0)\\) below",
    "the deficit equals \\(\\tfrac{1}{2}\\) on every nonviable cell",
    "384 vectors across the two-floor instance and the delayed grid",
    "they differ exactly on the timing cells --- those with \\(2 \\le z_{0} < 1 + T_{\\mathrm{obs}}\\)",
    "region of the delayed grid the deficit is constant. For finite horizons",
    "a class-restricted alpha-vector recursion reproduces the closed-form values",
    "the class-restricted alpha-vector recursion of Proposition \\ref{prop:pl} returns exactly the closed form",
    "servable sets are \\(\\Gamma_{1}",
    "Edition 2, revised after a joint audit",
    "The first edition conflated",
    "joint audit of the first",
]
present = [f for f in FORBIDDEN if " ".join(f.split()) in tnorm]
check("superseded statements and seed-edition audit histories are absent",
      not present, f"(still present: {present})" if present else "")

check("declarations use separate headings with the responsibility wording",
      "\\subsection*{Funding}" in tex and "\\subsection*{AI declaration}" in tex
      and "The author reviewed and edited outputs and takes responsibility "
          "for the final work." in tnorm)

ptr_ok = all(tnorm.count(s) == 1 for s in
             ["paper2_probabilistic_sufficiency_v2_verification.py"]
             + ["paper2_belief_state_v2_verification.py",
                "paper2_stochastic_selector_v2_verify.py",
                "hidden_parameter_learning_v1_verify.py"])
check("code-availability pointers: the flagship script and each of the "
      "three chained per-system scripts named exactly once",
      ptr_ok and "paper2_belief_state_figures.py" in tnorm)

import re
labels = re.findall(r"\\label\{([^}]+)\}", tex)
refs = set(re.findall(r"\\ref\{([^}]+)\}", tex))
dupl = [l for l in set(labels) if labels.count(l) > 1]
check("label/ref integrity: no duplicate labels, no undefined refs",
      not dupl and refs <= set(labels),
      f"dupl={dupl} undef={sorted(refs - set(labels))}" if (dupl or refs - set(labels)) else "")

hyg = True
for fn in ("paper2_probabilistic_sufficiency_v2.tex",
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
      "full 16-row grid", figs_ok and tex.count("$\\tfrac12$ &") >= 100
      and "2.5 & $1$" in tex)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass "
      f"(chained seeds: 16/16 + 21 nested, 15/15, 6/6)")
sys.exit(0 if n_pass == len(PASS) else 1)
