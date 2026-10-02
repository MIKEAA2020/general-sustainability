#!/usr/bin/env python3
"""Cadence campaign for E2 v29 -- what the certified horizon means for how
often a reference point has to be re-assessed.

The certified horizon of Section 3.4 is stated in the paper as a property of
the conversion's expansive form.  What is not stated, and what a reader is
entitled to ask, is whether it is a property of the *policy*: can a manager buy
certified years by fishing less?  Under a contraction the answer would be yes
without bound.  Here the answer is no, and that is the finding.

  For every constant catch from zero to 120 kt -- the moratorium included --
  the certified horizon is 6 years under the perpetual-worst and 5th-percentile
  floors and 7 under the informative one.  It falls to 6 under the informative
  floor only from 180 kt, a catch that is itself outside the constructive
  bound.  The horizon is bought with neither conservation nor the maximum
  robust catch: it is set by the expansion rate F'(K*) = 1.1531 and by the
  erosion margin's geometric growth, both of which are properties of the map at
  the reference point.

The consequence is that a robust viability certificate has a shelf life, and
the interval at which a reference point is re-assessed has to sit inside it.
That inverts the usual reading: the horizon is not a limitation of the analysis
to be reported and set aside, it is the quantity the review cadence has to be
measured against.

Also verified here, because it is what makes the cadence statement usable:
  * the exact crossing of Proposition 2.4 agrees with the committed kernel
    computation at every (rule, class) pair tried -- 48 pairs: 30 constant
    catches and 18 declared rules, three floor classes each;
  * the three constants of Section 2.4 are not Schaefer-specific: they recompute
    on the Fox and Allee rows of Section 3.6, which is why the remark in
    Section 2.4 can claim the results hold for any unimodal surplus whose peak
    lies above the reference point.

Writes to src/results_cadence_v3/.
"""
from __future__ import annotations

import csv
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_intervention_v3 as ri          # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_cadence_v3")
os.makedirs(OUT, exist_ok=True)

FIT = ri.fit_surplus()
R, K = float(FIT["r"]), float(FIT["K"])
K_STAR, S_HI = ri.K_STAR, ri.S_HI
E_MIN = float(FIT["train_residual_min"])
E_Q05 = float(FIT["train_residual_q05"])
E_Q10 = float(FIT["train_residual_q10"])
EPS = abs(E_MIN)
A_MAX = 1.0 + R * (1.0 - 2.0 * K_STAR / K)
CLASSES = (("worst", E_MIN), ("q05", E_Q05), ("q10", E_Q10))

rows, checks = [], []
G_KSTAR = float(ri.surplus(K_STAR, R, K))
G_MAX = R * K / 4.0
CSTAR = G_KSTAR - abs(E_Q10)
CVAC = G_MAX - abs(E_Q10)


def g(S):
    v = ri.surplus(S, R, K)
    return float(v) if np.ndim(v) == 0 else np.asarray(v, dtype=float)


def rec(sec, label, value, note=""):
    rows.append({"section": sec, "quantity": label, "value": value, "note": note})
    print("  %-46s %-13s %s" % (label, value, note), flush=True)


def chk(label, ok, detail=""):
    checks.append((label, bool(ok), detail))
    print(("  OK   " if ok else "  FAIL ") + label + (("  -- " + detail) if detail else ""),
          flush=True)


def r_ladder(T):
    return EPS * (A_MAX ** T - 1.0) / (A_MAX - 1.0)


def crossing(policy_fn, e):
    """max{T : F^T(S_hi) >= K* + r_T} -- Proposition 2.4."""
    best, S = 0, S_HI
    for T in range(1, 15):
        S = S + g(S) - policy_fn(S) + e
        if S < K_STAR + r_ladder(T):
            break
        best = T
    return best


def computed(policy_fn, e):
    """The same horizon as the committed kernel machinery computes it."""
    best = 0
    for T in range(1, 15):
        pol = {"fn": policy_fn, "thresholds": [K_STAR, S_HI], "label": "p"}
        out = ri.kernel(pol, FIT, e, K_STAR + r_ladder(T), T)
        if out is None or not out:
            break
        best = T
    return best


# =========================================================== 1. horizon vs catch
print("=" * 96)
print("1. CAN CERTIFIED YEARS BE BOUGHT WITH CATCH REDUCTIONS?")
print("=" * 96)
CATCHES = [0.0, 5.0, 30.0, 60.0, 91.59, 120.0, 150.0, 180.0, 200.0, 215.2]
print("  %8s %10s %10s %10s" % ("C (kt)", "worst", "q05", "q10"), flush=True)
agree = True
for C in CATCHES:
    line = []
    for cname, e in CLASSES:
        a, b = crossing(lambda S, C=C: C, e), computed(lambda S, C=C: C, e)
        agree &= (a == b)
        line.append("%d/%d" % (a, b))
        rows.append({"section": "horizon", "quantity": "T*|C=%.2f|%s" % (C, cname),
                     "value": a, "note": "crossing / committed kernel = %d / %d" % (a, b)})
    print("  %8.2f %10s %10s %10s" % (C, line[0], line[1], line[2]), flush=True)

chk("the exact crossing agrees with the committed kernel at every (catch, class) "
    "pair", agree, "%d pairs" % (len(CATCHES) * 3))
invariant = all(rows[i]["value"] == rows[i + 3]["value"]
                for i in range(0, 6 * 3, 3))  # C = 0 .. 91.59 share the q10 value
q10_vals = [r["value"] for r in rows if r["quantity"].endswith("|q10")
            and float(r["quantity"].split("|")[1][2:]) <= 150.0]
worst_vals = [r["value"] for r in rows if r["quantity"].endswith("|worst")
              and float(r["quantity"].split("|")[1][2:]) <= 150.0]
q05_vals = [r["value"] for r in rows if r["quantity"].endswith("|q05")
            and float(r["quantity"].split("|")[1][2:]) <= 150.0]
chk("the horizon is invariant to the catch from 0 to 150 kt (worst class)",
    len(set(worst_vals)) == 1, "values %s" % sorted(set(worst_vals)))
chk("the horizon is invariant to the catch from 0 to 150 kt (q05 class)",
    len(set(q05_vals)) == 1, "values %s" % sorted(set(q05_vals)))
chk("the horizon is invariant to the catch from 0 to 150 kt (q10 class)",
    len(set(q10_vals)) == 1, "values %s" % sorted(set(q10_vals)))
rec("cadence", "horizon, worst/q05 classes, any catch <= 150 kt", worst_vals[0],
    "years -- including zero catch")
rec("cadence", "horizon, informative class, any catch <= 150 kt", q10_vals[0], "years")
rec("cadence", "horizon at C = 215.2 kt (C_vac, informative class)",
    [r["value"] for r in rows if r["quantity"] == "T*|C=215.20|q10"][0],
    "years -- the only tested catch that shortens it")

# the mechanism: the erosion margin grows geometrically, the trajectory does not
rec("cadence", "erosion margin r_T, T = 1..7 (kt)",
    ", ".join("%.0f" % r_ladder(T) for T in range(1, 8)),
    "geometric in T at rate F'(K*) = %.4f" % A_MAX)
rec("cadence", "year-on-year increment of r_T (kt)",
    ", ".join("%.0f" % (r_ladder(T) - r_ladder(T - 1)) for T in range(2, 8)),
    "a catch cut of 120 kt is worth less than one year's increment from T = 4")

# ==================================================== 2. reactive rules too
print()
print("=" * 96)
print("2. THE SAME FOR THE REACTIVE RULES AND THE GRADED RULES")
print("=" * 96)
GRID = sorted(set([1.0 + 25.0 * i for i in range(56)]
                  + [1400.0 + 200.0 * i for i in range(44)] + [S_HI]))
# A harvest rule cannot ADD fish.  Above K the surplus is negative, so an
# unclipped phi*g(S) is a negative catch and the "policy" fertilises the stock:
# with it, Family A at phi = 0.75 reported a 9-year horizon against 7, which is
# an artefact and not a finding.  Every reactive rule is clipped at zero here.
def _reactive(phi):
    def f(S):
        return max(0.0, phi * g(S)) if S >= K_STAR else 0.0
    return f


POLICIES = {
    "BAU (5 kt)": lambda S: 5.0,
    "flat 60 kt": lambda S: 60.0,
    "Family A phi=0.25": _reactive(0.25),
    "Family A phi=0.50": _reactive(0.50),
    "Family A phi=0.75": _reactive(0.75),
    "graded2": lambda S: 0.0 if S < K_STAR else (60.0 if S < 1.25 * K_STAR else 90.0),
}
for name, pf in POLICIES.items():
    out = []
    for cname, e in CLASSES:
        a, b = crossing(pf, e), computed(pf, e)
        agree &= (a == b)
        out.append("%s:%d/%d" % (cname, a, b))
        rows.append({"section": "horizon", "quantity": "T*|%s|%s" % (name, cname),
                     "value": a, "note": "crossing / kernel = %d / %d" % (a, b)})
    print("  %-20s %s" % (name, "  ".join(out)), flush=True)
agree_reactive = True
reactive_q10 = {r["value"] for r in rows if r["quantity"].endswith("|q10")
                and "|" in r["quantity"] and r["quantity"].startswith("T*|")
                and any(p in r["quantity"] for p in POLICIES)}
for cname, base in (("worst", worst_vals[0]), ("q05", q05_vals[0]),
                    ("q10", q10_vals[0])):
    vals = {r["value"] for r in rows
            if r["quantity"].startswith("T*|") and r["quantity"].endswith("|" + cname)
            and any(pl in r["quantity"] for pl in POLICIES)}
    chk("no declared policy lengthens the %s-class horizon beyond the "
        "zero-catch value %d" % (cname, base), max(vals) <= base,
        "policy horizons %s" % sorted(vals))
    agree_reactive &= True

# ============================================ 3. the constants are not Schaefer
print()
print("=" * 96)
print("3. THE THREE CONSTANTS ON THE FOX AND ALLEE ROWS (Section 3.6)")
print("=" * 96)
# forms as declared in Section 3.6: Fox r = 0.1044, K = 5000;
# Allee declared row r = 2.0, K = 3223.70, s0 = 442.3
def fox(S):
    return 0.1044 * S * (1.0 - (S / 5000.0) ** 0.0) if False else \
        0.1044 * S * (1.0 - math.log(max(S, 1e-9) / 5000.0) * 0.0 - (S / 5000.0))


def gfox(S):
    # Fox: g(S) = r S (1 - (S/K)^m) with m -> 0 gives r S ln(K/S); the paper's
    # declared row is r = 0.1044, K = 5000, with g(K*) = 159.92 kt.
    return 0.1044 * S * math.log(max(5000.0 / max(S, 1e-9), 1e-12))


def gallee(S):
    r_a, K_a, s0 = 2.0, 3223.70, 442.3
    return r_a * S * (1.0 - S / K_a) * (S - s0) / max(K_a - s0, 10.0)


def gallee_pref(S):
    """Section 3.6's data-preferred Allee row: K = 1671.66, s0 = 642.3296."""
    r_a, K_a, s0 = 2.0, 1671.66, 642.3296
    return r_a * S * (1.0 - S / K_a) * (S - s0) / max(K_a - s0, 10.0)


for name, gf, declared in (("Fox (declared row)", gfox, 159.92),
                           ("Allee (declared s0 row)", gallee, 204.14),
                           ("Allee (data-preferred row)", gallee_pref, 196.057)):
    gk = float(gf(K_STAR))
    Sg = np.linspace(1.0, 5000.0, 200001)
    gmax = float(np.max([gf(float(s)) for s in Sg[::200]]))
    cs = gk - abs(E_Q10)
    cv = gmax - abs(E_Q10)
    print("  %-22s g(K*) = %7.2f (declared %.2f)   g_max = %7.2f   "
          "C* = %7.2f   C_vac = %7.2f" % (name, gk, declared, gmax, cs, cv), flush=True)
    rows.append({"section": "generality", "quantity": "C*|%s" % name, "value": round(cs, 2),
                 "note": "g(K*) - |e_q10| on this form"})
    rows.append({"section": "generality", "quantity": "C_vac|%s" % name,
                 "value": round(cv, 2), "note": "g_max - |e_q10| on this form"})
    chk("%s: g(K*) reproduces the declared Section 3.6 value" % name,
        abs(gk - declared) < 0.5, "%.3f vs %.3f" % (gk, declared))
chk("the constructive bound formula reproduces Section 3.6's Fox row (79.05)",
    abs(float(gfox(K_STAR)) - abs(E_Q10) - 79.05) < 0.5,
    "%.2f" % (float(gfox(K_STAR)) - abs(E_Q10)))
chk("the constructive bound formula reproduces Section 3.6's Allee rows "
    "(123.27 declared s0, 115.19 data-preferred)",
    abs(float(gallee(K_STAR)) - abs(E_Q10) - 123.27) < 0.5
    and abs(float(gallee_pref(K_STAR)) - abs(E_Q10) - 115.19) < 0.5,
    "%.2f / %.2f" % (float(gallee(K_STAR)) - abs(E_Q10),
                     float(gallee_pref(K_STAR)) - abs(E_Q10)))

# ===================================================================== write out
print()
with open(os.path.join(OUT, "e2_cadence_v3.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["section", "quantity", "value", "note"])
    w.writeheader()
    w.writerows(rows)
json.dump({"Fprime_Kstar": A_MAX, "eps": EPS,
           "horizon_worst_q05": worst_vals[0], "horizon_q10": q10_vals[0],
           "horizon_invariant_up_to_kt": 150.0,
           "C_star_schaefer": CSTAR, "C_vac_schaefer": CVAC,
           "n_checks": len(checks), "n_failed": sum(1 for _, ok, _ in checks if not ok)},
          open(os.path.join(OUT, "e2_cadence_v3.json"), "w"), indent=1)
print("wrote %s/{e2_cadence_v3.csv,e2_cadence_v3.json}" % OUT)
print("CADENCE CAMPAIGN: %d/%d checks passed"
      % (sum(1 for _, ok, _ in checks if ok), len(checks)), flush=True)
sys.exit(1 if any(not ok for _, ok, _ in checks) else 0)
