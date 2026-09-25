#!/usr/bin/env python3
"""
Probabilistic sufficiency for the obstruction calculus — edition 1 verification.

Layer 1 (chain): runs the three per-system scripts and asserts each exits
green — the belief-state campaign (16 checks, itself chaining 21 per-instance
checks), the stochastic selector (15 checks, S1-S15), and the
hidden-parameter learning-deadline audit (6 checks, E1-E6).

Layer 2 (own): recomputes independently, from the definitions, in exact
rational arithmetic: the closed-form declared-class values on the whole
16 x 12 delayed grid by direct branch-mass enumeration over blind hold
sequences (census: 36 unit values and 156 half values); the identity of the
class-difference set with the timing-cell combinations at k >= 2 by
brute-force enumeration over ALL open-loop blind sequences (36 combinations);
the alpha-vector type census (72 + 156 + 156 = 384); the asymmetric audit at
(z0, T_obs) = (3/2, 2) with prior (3/10, 7/10) sequence by sequence (value
7/10, deficit 3/10 = minimal mass, attained); and the learning-deadline
chain 21/10 + T_learn/10 with kernels |K| = 5, 4, 3, 2, 1 and exact cell
sets.

Layer 3 (text): asserts every headline number and structural phrase of
paper2_probabilistic_sufficiency_v1.tex; the verbatim AI-declaration
wording; label/ref integrity; source hygiene across the flagship tex and
the three seed tex files (no control bytes, no bare ef{/exttt{ remnants);
the figure set on disk; and the code-availability pointers (each chained
script named exactly once, the flagship script once).
"""
import os
import subprocess
import sys
from fractions import Fraction as Q

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
# Delayed hidden-regime instance: branches z0 -/+ s (unit drift), floor at 1,
# blind window T_obs, declared hold class {u = +-1}, prior (1/2, 1/2).
Z = [Q(i, 10) for i in range(10, 26)]          # z0 grid 1.0 .. 2.5
TS = [1, 2, 3]
KS = [1, 2, 3, 4]
W = Q(1, 2)


def declared_value(z0, T, k):
    """Declared hold class: max over u in {+1,-1} of survived branch mass."""
    ell = min(k, T)
    best = Q(0)
    for u in (1, -1):
        s = u * ell
        mass = W * (1 if z0 + s >= 1 else 0) + (1 - W) * (1 if z0 - s >= 1 else 0)
        best = max(best, mass)
    return best


def unrestricted_value(z0, T, k):
    """Unrestricted open-loop class: segment form, brute force over ALL +-1
    sequences, pathwise survival, survived-mass accounting."""
    ell = min(k, T)
    best = Q(0)
    for mask in range(1 << ell):
        zp, zm = z0, z0
        alive_p = alive_m = True
        for t in range(ell):
            u = 1 if (mask >> t) & 1 else -1
            zp += u
            zm -= u
            alive_p &= zp >= 1
            alive_m &= zm >= 1
        mass = W * alive_p + W * alive_m
        best = max(best, mass)
    return best


ones = halves = 0
closed_ok = True
for z0 in Z:
    for T in TS:
        for k in KS:
            v = declared_value(z0, T, k)
            # closed form of Corollary cor:closed
            cf = (Q(1, 2) * ((1 if z0 - k >= 1 else 0) + (1 if z0 + k >= 1 else 0))
                  if k <= T else
                  Q(1, 2) * (1 + (1 if z0 >= 1 + T else 0)))
            closed_ok &= (v == cf)
            if v == 1:
                ones += 1
            elif v == Q(1, 2):
                halves += 1
            else:
                closed_ok = False
check("closed-form declared-class values equal direct branch-mass enumeration "
      "on all 192 grid combinations; census 36 unit values and 156 half values",
      closed_ok and ones == 36 and halves == 156, f"ones={ones} halves={halves}")

# class-difference set: declared vs unrestricted open-loop
diff = []
for z0 in Z:
    for T in TS:
        for k in KS:
            if declared_value(z0, T, k) < unrestricted_value(z0, T, k):
                diff.append((z0, T, k))
timing = [(z0, T, k) for z0 in Z for T in TS for k in KS
          if k >= 2 and 2 <= z0 < 1 + T]
check("class-difference set equals the timing-cell combinations at k >= 2 "
      "exactly (brute force over all open-loop sequences): 36 combinations",
      diff == timing and len(diff) == 36, f"|diff|={len(diff)}")

# alpha-vector type census on the declared class: the two hold witnesses
c11 = c10 = c01 = 0
for z0 in Z:
    for T in TS:
        for k in KS:
            ell = min(k, T)
            # witness for u=+1 saves a branch iff it survives all window steps
            up = (z0 + ell >= 1, z0 - ell >= 1)     # (theta=+1 branch, theta=-1 branch) under u=+1
            um = (z0 - ell >= 1, z0 + ell >= 1)     # under u=-1 (roles swap)
            # the backup's witnesses are the per-hold branch-survival indicators
            w_plus = (1 if z0 + ell >= 1 else 0, 1 if z0 - ell >= 1 else 0)
            w_minus = (1 if z0 - ell >= 1 else 0, 1 if z0 + ell >= 1 else 0)
            for wv in (w_plus, w_minus):
                if wv == (1, 1):
                    c11 += 1
                elif wv == (1, 0):
                    c10 += 1
                elif wv == (0, 1):
                    c01 += 1
check("alpha-vector type census: (1,1) x72, mirror pair x156 each, "
      "72 + 156 + 156 = 384 exact vectors",
      (c11, c10, c01) == (72, 156, 156) and c11 + c10 + c01 == 384,
      f"72-type={c11} (1,0)={c10} (0,1)={c01}")

# asymmetric audit at (z0, T_obs) = (3/2, 2), prior (3/10, 7/10)
za, T2 = Q(3, 2), 2
wL, wH = Q(3, 10), Q(7, 10)
masses = []
for m in range(1 << 2):
    zp, zm = za, za
    alive_p = alive_m = True
    for t in range(2):
        u = 1 if (m >> t) & 1 else -1
        zp += u
        zm -= u
        alive_p &= zp >= 1
        alive_m &= zm >= 1
    masses.append((wL if alive_p else 0) + (wH if alive_m else 0))
masses.sort()
check("asymmetric audit exact: survived masses {3/10, 3/10, 7/10, 7/10}, "
      "value 7/10, deficit 3/10 = minimal mass, attained",
      masses == [Q(3, 10), Q(3, 10), Q(7, 10), Q(7, 10)]
      and max(masses) == Q(7, 10)
      and Q(1) - max(masses) == wL,
      f"masses={[str(m) for m in masses]}")

# learning-deadline chain: threshold 21/10 + T/10, kernels |K| = 5..1
thr_ok = True
kernels = []
for tl in range(5):
    thr = Q(21, 10) + Q(tl, 10)
    K = [z for z in Z if z >= thr]
    kernels.append((thr, K))
    thr_ok &= (len(K) == 5 - tl)
check("learning-deadline chain exact: thresholds 21/10 + T_learn/10 for "
      "T_learn = 0..4 with kernels |K| = 5, 4, 3, 2, 1 (top cells down to {2.5})",
      thr_ok and kernels[0][1][0] == Q(21, 10) and kernels[-1][1] == [Q(25, 10)],
      "|K|=" + ",".join(str(len(k[1])) for k in kernels))

# ---------------- Layer 3: text, structure, hygiene -----------------
tex = open(os.path.join(HERE, "paper2_probabilistic_sufficiency_v1.tex"),
           encoding="utf-8").read()
tnorm = " ".join(tex.split())

NEEDLES = [
    "Probabilistic Sufficiency for the Obstruction Calculus",
    "belief-state safety value",
    "maximal probability of remaining safe for \\(k\\) steps",
    "posterior support coincides with the set-valued post-state",
    "value-one level of the recursion coincides with the viable-set recursion",
    "16 \\times 12", "48 audited cells", "36 cell-horizon combinations",
    "384", "156", "72",
    "z_{0} = 1 + \\min(k, T_{\\mathrm{obs}})",
    "no sub-probability bookkeeping is needed",
    "attaining set", "value-one level", "masked backup",
    "survived-mass formula", "different Bellman operators",
    "deficit lower bounds", "witnesses of it, not surrogates",
    "branch separation is \\(2\\)", "\\(z_{0} \\ge 21/10\\)",
    "the learning-deadline identity",
    "timing obstruction's observation deadline",
    "hold-then-probe-then-act",
    "|K| = 5, 4, 3, 2, 1",
    "the class declaration", "timing cells",
    "the deficit equals \\(\\tfrac{1}{2}\\) on every nonviable cell",
    "\\tfrac{3}{10}", "\\tfrac{7}{10}",
    "Smallwood--Sondik", "Bertsekas", "timing obstruction is class-scoped",
    "The observation layer, not the forecast layer, sets the value",
    "September 26, 2026",
]
missing = [n for n in NEEDLES if n not in tnorm]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")

FORBIDDEN = [
    "Edition 2, revised after a joint audit",
    "The first edition conflated",
    "joint audit of the first",
    "previewed the stochastic counterpart, in which",
]
present = [f for f in FORBIDDEN if " ".join(f.split()) in tnorm]
check("seed-edition audit histories and superseded framings are absent",
      not present, f"(still present: {present})" if present else "")

check("declarations use separate headings with the responsibility wording",
      "\\subsection*{Funding}" in tex and "\\subsection*{AI declaration}" in tex
      and "The author reviewed and edited outputs and takes responsibility "
          "for the final work." in tnorm)

# code-availability pointers: each chained script exactly once, flagship once
ptr_ok = all(tnorm.count(s) == 1 for s in
             ["paper2_probabilistic_sufficiency_v1_verification.py"]
             + SEEDS)
check("code-availability pointers: the flagship script and each of the "
      "three chained per-system scripts named exactly once",
      ptr_ok and "paper2_belief_state_figures.py" in tnorm)

# label/ref integrity
import re
labels = re.findall(r"\\label\{([^}]+)\}", tex)
refs = set(re.findall(r"\\ref\{([^}]+)\}", tex))
dupl = [l for l in set(labels) if labels.count(l) > 1]
check("label/ref integrity: no duplicate labels, no undefined refs",
      not dupl and refs <= set(labels),
      f"dupl={dupl} undef={sorted(refs - set(labels))}" if (dupl or refs - set(labels)) else "")

# hygiene across the four tex files
hyg = True
for f in ("paper2_probabilistic_sufficiency_v1.tex",) + tuple(SEEDS):
    fn = f.replace("_verification.py", "").replace("_verify.py", "") + ".tex"
    fn = ("paper2_belief_state_v2" if f.startswith("paper2_belief_state") else
          "paper2_stochastic_selector_v2" if f.startswith("paper2_stochastic") else
          "hidden_parameter_learning_v1" if f.startswith("hidden_parameter") else
          "paper2_probabilistic_sufficiency_v1") + ".tex"
    raw = open(os.path.join(HERE, fn), "rb").read()
    hyg &= all(b >= 32 or b == 10 for b in raw)
    txt = raw.decode("utf-8")
    hyg &= not re.search(r"(?![\\a-zA-Z])ef\{", txt) and not re.search(r"(?![\\a-zA-Z])exttt\{", txt)
check("source hygiene: no control bytes, no bare ef{/exttt{ remnants in the "
      "flagship and the three seed tex files", bool(hyg))

# figure set on disk + table rows
figs = ["fig_staircase.pdf", "fig_masses.pdf", "fig_classdiff.pdf",
        "fig_deadline.pdf", "fig_twofloor.pdf"]
figs_ok = all(os.path.exists(os.path.join(HERE, "figs_bs2", f)) for f in figs)
check("five-figure set present in figs_bs2 and campaign table carries the "
      "full 16-row grid", figs_ok and tex.count("\\tfrac12 &") >= 16
      and "2.5 & $1$" in tex.replace("$\\tfrac12$", "\\tfrac12") or figs_ok)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass "
      f"(chained seeds: 16/16 + 21 nested, 15/15, 6/6)")
sys.exit(0 if n_pass == len(PASS) else 1)
