#!/usr/bin/env python3
"""Structural campaign for E2 v29 -- the closed-form characterisation of Table 1,
and the correction of Result 3.4's reactive criterion.

Why this exists.  Table 1 of the paper was a *computed* object: twelve policies
times six readings, each produced by backward recursion, with the prose
narrating the result.  Narration of that kind is where errors hide, and one was
hiding there (section 4 below).  This campaign asks what the table *is*
algebraically, and then checks the algebra against the committed artifact cell
by cell.  Everything the paper states about Table 1 is reproduced here in
closed form and asserted against the archived numbers.

The three constants.  With the committed fit, the reference point K*, the floor
|e| and the surplus g:

  C*   = g(K*) - |e|     largest catch (of ANY form, evaluated at the LRP) for
                         which the LRP is held FROM ITSELF; the protection
                         margin of any policy is exactly C* - C(K*)
  Cvac = g_max - |e|     largest CONSTANT catch whose T=inf kernel is nonempty
  b_inf(C) = max(K*, lower root of g(S) = C + |e|)   the T=inf boundary itself
  T*   = max{ T : F^T(S_hi) >= K* + r_T }            the certified horizon

RESULT 3.4 (the defect this campaign exists to fix).  The paper stated the
criterion for Family A holding the whole safe set as (1 - phi) g_max > |e|,
i.e. phi < 1 - 80.87/296.09 = 0.727.  That is the criterion for the kernel
being NONEMPTY, not for it being the WHOLE SAFE SET.  The whole-safe-set
criterion is (1 - phi) g(K*) >= |e|, i.e. phi <= 1 - 80.87/172.46 = 0.531.
Between the two thresholds the kernel is a proper subset of the safe set:
viable, but only from above the reference point.  None of the declared members
{0.25, 0.50, 0.75} falls in that band, which is why every printed verdict was
right and the stated criterion was not.

Writes to src/results_struct_v3/.
"""
from __future__ import annotations

import csv
import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_intervention_v3 as ri          # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_struct_v3")
os.makedirs(OUT, exist_ok=True)

FIT = ri.fit_surplus()
R, K = float(FIT["r"]), float(FIT["K"])
K_STAR, S_HI = ri.K_STAR, ri.S_HI
E_MIN = float(FIT["train_residual_min"])
E_Q05 = float(FIT["train_residual_q05"])
E_Q10 = float(FIT["train_residual_q10"])
EPS = abs(E_MIN)


def g(S):
    v = ri.surplus(S, R, K)
    return float(v) if np.ndim(v) == 0 else np.asarray(v, dtype=float)


G_KSTAR = g(K_STAR)
G_MAX = R * K / 4.0
A_MAX = 1.0 + R * (1.0 - 2.0 * K_STAR / K)      # F'(K*)

rows, checks = [], []
_t0 = time.time()


def rec(label, value, note=""):
    rows.append({"quantity": label, "value": value, "note": note})
    print(f"  {label:50s} {value!s:>13}  {note}", flush=True)


def chk(label, ok, detail=""):
    checks.append((label, bool(ok), detail))
    print(("  OK   " if ok else "  FAIL ") + label
          + (("  -- " + detail) if detail else ""), flush=True)


def head(t):
    print()
    print("=" * 92)
    print(t)
    print("=" * 92, flush=True)


def lower_root(target):
    """Smaller root of g(S) = target on the increasing branch, or None."""
    if target > G_MAX:
        return None
    lo, hi = 0.0, K / 2.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if g(m) < target:
            lo = m
        else:
            hi = m
    return hi


# =============================================================== 1. constants
head("1. THE THREE CONSTANTS")
CSTAR = G_KSTAR - abs(E_Q10)
CVAC = G_MAX - abs(E_Q10)
rec("g(K*)", round(G_KSTAR, 4), "surplus at the reference point")
rec("g_max", round(G_MAX, 4), "rK/4")
rec("|e_q10|", round(abs(E_Q10), 4), "declared 10th-percentile floor")
rec("C_star = g(K*) - |e_q10|", round(CSTAR, 4),
    "largest catch holding the LRP from itself")
rec("C_vac = g_max - |e_q10|", round(CVAC, 4),
    "largest constant catch with a nonempty T=inf kernel")
chk("C_star reproduces the published constructive bound 91.59",
    abs(CSTAR - 91.59) < 0.005, "%.4f" % CSTAR)

# ================================== 2. Table 1's q10 T=inf column, closed form
head("2. TABLE 1's q10 T=inf COLUMN, IN CLOSED FORM")
TABLE1 = {0.0: 884.6, 5.0: 884.6, 60.0: 884.6, 120.0: 1082.3,
          180.0: 1637.8, 240.0: None}
print(f"  {'C':>6} {'C+|e|':>9} {'closed form':>13} {'Table 1':>11}", flush=True)
for C in sorted(TABLE1):
    b = lower_root(C + abs(E_Q10))
    got = None if b is None else round(max(b, K_STAR), 1)
    want = TABLE1[C]
    ok = (want is None and got is None) or (
        want is not None and got is not None and abs(want - got) < 0.06)
    print(f"  {C:6.1f} {C + abs(E_Q10):9.2f} "
          f"{('empty' if got is None else '%13.1f' % got):>13} "
          f"{('empty' if want is None else '%11.1f' % want):>11}", flush=True)
    rows.append({"quantity": "b_inf(C=%.0f)" % C,
                 "value": "empty" if got is None else got,
                 "note": "closed form; Table 1 prints %s"
                         % ("empty" if want is None else want)})
    chk("b_inf(C=%.0f) matches Table 1" % C, ok, "%s vs %s" % (got, want))

# ============================================ 3. the protection-supply budget
head("3. PROTECTION-SUPPLY BUDGET:  margin + harvest at the LRP = C*")
print(f"  {'policy':22s} {'C(K*)':>9} {'margin':>9} {'sum':>9}  holds LRP from itself",
      flush=True)
for name, ck in (("BAU (5 kt)", 5.0), ("flat 60 kt", 60.0), ("flat 120 kt", 120.0),
                 ("flat 180 kt", 180.0), ("flat 240 kt", 240.0),
                 ("S1 / cascade at LRP", 60.0),
                 ("Family A phi=0.25", 0.25 * G_KSTAR),
                 ("Family A phi=0.50", 0.50 * G_KSTAR),
                 ("Family A phi=0.60", 0.60 * G_KSTAR),
                 ("Family A phi=0.75", 0.75 * G_KSTAR),
                 ("graded2 at LRP", 60.0), ("graded3 at LRP", 30.0)):
    margin = CSTAR - ck
    print(f"  {name:22s} {ck:9.2f} {margin:9.2f} {ck + margin:9.2f}  "
          f"{'yes' if margin >= -1e-9 else 'no'}", flush=True)
    rows.append({"quantity": "margin|%s" % name, "value": round(margin, 2),
                 "note": "C* - C(K*)"})
# the identity is definitional; what is testable is that the T=1 boundary IS the
# LRP exactly when the margin is non-negative
GRID = sorted(set([1.0 + 25.0 * i for i in range(56)]
                  + [1400.0 + 200.0 * i for i in range(44)] + [S_HI]))
ok_budget = True
for C in (0.0, 5.0, 30.0, 60.0, 86.232, 91.594, 120.0, 180.0):
    pol = {"fn": lambda S, C=C: C, "thresholds": GRID, "label": "flat"}
    out = ri.kernel(pol, FIT, E_Q10, K_STAR, 1)
    b = min(lo for lo, _ in out)
    held = b <= K_STAR + 1e-9
    ok_budget &= (held == (CSTAR - C >= -1e-9))
    print(f"    C={C:7.3f}  T=1 boundary {b:8.2f}  held={held!s:5s}  "
          f"margin={CSTAR - C:8.2f}", flush=True)
chk("the LRP is held from itself exactly when the margin is non-negative",
    ok_budget)

# ============================== 4. Family A: three regimes, two thresholds
head("4. FAMILY A -- THREE REGIMES, TWO THRESHOLDS")
PHI_SAFE = 1.0 - abs(E_Q10) / G_KSTAR
PHI_NONEMPTY = 1.0 - abs(E_Q10) / G_MAX
rec("phi* (whole safe set) = 1 - |e|/g(K*)", round(PHI_SAFE, 4),
    "CORRECT criterion for the claim the paper makes")
rec("phi* (nonempty)       = 1 - |e|/g_max", round(PHI_NONEMPTY, 4),
    "what the paper printed (0.727) -- right question, wrong claim")
chk("the printed 0.727 is the nonempty threshold, not the safe-set one",
    abs(PHI_NONEMPTY - 0.727) < 0.001 and abs(PHI_SAFE - 0.531) < 0.001,
    "%.4f vs %.4f" % (PHI_NONEMPTY, PHI_SAFE))

fam_rows = []
for phi in (0.25, 0.50, 0.60, 0.70, 0.75):
    pol = {"fn": lambda S, phi=phi: phi * g(S) if S >= K_STAR else 0.0,
           "thresholds": GRID, "label": "A_phi%.2f" % phi}
    o1 = ri.kernel(pol, FIT, E_Q10, K_STAR, 1)
    oi = ri.kernel(pol, FIT, E_Q10, K_STAR, "inf")
    b1 = None if o1 is None else round(min(lo for lo, _ in o1), 2)
    bi = None if oi is None else round(min(lo for lo, _ in oi), 2)
    regime = ("whole safe set" if bi is not None and bi <= K_STAR + 1e-9
              else "viable above the LRP" if bi is not None else "empty")
    pred = ("whole safe set" if phi <= PHI_SAFE + 1e-9
            else "viable above the LRP" if phi < PHI_NONEMPTY - 1e-9 else "empty")
    fam_rows.append({"phi": phi, "C_at_LRP": round(phi * G_KSTAR, 2), "T1": b1,
                     "Tinf": ("empty" if bi is None else bi), "regime": regime,
                     "predicted": pred})
    print(f"  phi={phi:5.2f}  C(K*)={phi * G_KSTAR:7.2f}  T=1 {str(b1):>8}  "
          f"T=inf {str(bi):>8}   {regime:20s} (closed form: {pred})", flush=True)
    rows.append({"quantity": "FamilyA phi=%.2f" % phi,
                 "value": "%s / %s / %s" % (b1, bi, regime),
                 "note": "T=1 / T=inf / regime under the q10 class"})
    chk("Family A phi=%.2f regime matches the closed form" % phi, regime == pred,
        "%s vs %s" % (regime, pred))
with open(os.path.join(OUT, "e2_familyA_regimes.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["phi", "C_at_LRP", "T1", "Tinf", "regime",
                                       "predicted"])
    w.writeheader()
    w.writerows(fam_rows)

# realised safe-set threshold, by bisection on the CHEAP T=1 kernel
lo, hi = 0.0, 1.0
for _ in range(40):
    m = 0.5 * (lo + hi)
    pol = {"fn": lambda S, m=m: m * g(S) if S >= K_STAR else 0.0,
           "thresholds": GRID, "label": "A"}
    o = ri.kernel(pol, FIT, E_Q10, K_STAR, 1)
    if o is not None and min(x for x, _ in o) <= K_STAR + 1e-9:
        lo = m
    else:
        hi = m
rec("phi* (safe set) realised on the 25 kt grid", round(lo, 4),
    "exact %.4f" % PHI_SAFE)
chk("the realised threshold is within one grid step of the exact one",
    abs(lo - PHI_SAFE) < 0.005, "realised %.4f vs exact %.4f" % (lo, PHI_SAFE))

# ================================================ 5. the certified horizon
head("5. CERTIFIED HORIZON -- THE EXACT CROSSING")


def r_ladder(T):
    return EPS * (A_MAX ** T - 1.0) / (A_MAX - 1.0)


def attractor(policy_fn, e):
    """Upper (attracting) fixed point of the worst-case loop, or None.

    Bracket from the LOWER root, not from K*: below the lower root the loop
    declines too, so a bracket starting at K* collapses to K* and reads as a
    plausible number instead of 'no attractor'.
    """
    need = policy_fn(1e9) + abs(e)                 # g(S) = C + |e|
    S = np.linspace(K_STAR, S_HI, 200001)
    if float(np.max(g(S) - policy_fn(S))) <= need:
        return None
    lo_ = lower_root(need) or K_STAR
    lo_b, hi_b = max(lo_, K_STAR), S_HI
    F = lambda s: s + g(s) - policy_fn(s) + e
    for _ in range(200):
        m = 0.5 * (lo_b + hi_b)
        if F(m) > m:
            lo_b = m
        else:
            hi_b = m
    return hi_b


def crossing(policy_fn, e):
    """max{ T : F^T(S_hi) >= K* + r_T } -- the exact certified horizon."""
    best, S = 0, S_HI
    for T in range(1, 15):
        S = S + g(S) - policy_fn(S) + e
        if S < K_STAR + r_ladder(T):
            break
        best = T
    return best


def computed_horizon(policy_fn, e):
    """The horizon as the committed machinery computes it (kernel emptiness)."""
    best = 0
    for T in range(1, 15):
        pol = {"fn": policy_fn, "thresholds": [K_STAR, S_HI], "label": "p"}
        out = ri.kernel(pol, FIT, e, K_STAR + r_ladder(T), T)
        if out is None or not out:
            break
        best = T
    return best


for label, pf in (("BAU (5 kt)", lambda S: 5.0), ("zero catch", lambda S: 0.0)):
    for cname, e in (("worst", E_MIN), ("q05", E_Q05), ("q10", E_Q10)):
        Sat = attractor(pf, e)
        T_cr = crossing(pf, e)
        T_co = computed_horizon(pf, e)
        if Sat is None:
            print(f"  {label:12s} {cname:6s} attractor=     none   "
                  f"crossing T*={T_cr}   computed T*={T_co}", flush=True)
        else:
            T_asym = math.floor(math.log(1.0 + (Sat - K_STAR) * (A_MAX - 1.0) / EPS)
                                / math.log(A_MAX))
            print(f"  {label:12s} {cname:6s} attractor={Sat:8.1f}   "
                  f"crossing T*={T_cr}   computed T*={T_co}   "
                  f"asymptotic bound={T_asym}", flush=True)
            rows.append({"quantity": "horizon_asymptotic|%s|%s" % (label, cname),
                         "value": T_asym,
                         "note": "lower bound: F^T(S_hi) >= S* for all T"})
        rows.append({"quantity": "horizon|%s|%s" % (label, cname),
                     "value": "%s / %s" % (T_cr, T_co),
                     "note": "exact crossing / committed kernel computation"})
        chk("the exact crossing reproduces the computed horizon (%s, %s)"
            % (label, cname), T_cr == T_co, "crossing %s computed %s" % (T_cr, T_co))

# ============================================ 6. monotone comparative statics
head("6. MONOTONE COMPARATIVE STATICS (the ordering Tables 1 and 5 assume)")
prev, mono_C = -1.0, True
for C in (0.0, 5.0, 60.0, 120.0, 180.0, 240.0):
    pol = {"fn": lambda S, C=C: C, "thresholds": [K_STAR, S_HI], "label": "flat"}
    b = min(lo for lo, _ in ri.kernel(pol, FIT, E_Q10, K_STAR, 1))
    mono_C &= b >= prev - 1e-9
    prev = b
chk("the T=1 boundary is nondecreasing in the catch", mono_C)
prev, mono_e = -1.0, True
for e in (abs(E_Q10), abs(E_Q05), abs(E_MIN)):
    pol = {"fn": lambda S: 60.0, "thresholds": [K_STAR, S_HI], "label": "flat60"}
    b = min(lo for lo, _ in ri.kernel(pol, FIT, -e, K_STAR, 1))
    mono_e &= b >= prev - 1e-9
    prev = b
chk("the T=1 boundary is nondecreasing in the floor magnitude", mono_e)

# ================================================================ 7. write out
head("7. OUTPUT")
with open(os.path.join(OUT, "e2_structure_v3.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["quantity", "value", "note"])
    w.writeheader()
    w.writerows(rows)
json.dump({"g_Kstar": G_KSTAR, "g_max": G_MAX, "e_q10": E_Q10,
           "C_star": CSTAR, "C_vac": CVAC,
           "phi_safe": PHI_SAFE, "phi_nonempty": PHI_NONEMPTY,
           "phi_safe_realised": lo, "Fprime_Kstar": A_MAX,
           "n_checks": len(checks),
           "n_failed": sum(1 for _, ok, _ in checks if not ok)},
          open(os.path.join(OUT, "e2_structure_v3.json"), "w"), indent=1)
print(f"wrote {OUT}/{{e2_structure_v3.csv,e2_familyA_regimes.csv,"
      f"e2_structure_v3.json}}  ({time.time() - _t0:.0f}s)", flush=True)
print(f"STRUCTURE CAMPAIGN: {sum(1 for _, ok, _ in checks if ok)}/{len(checks)} "
      f"checks passed", flush=True)
sys.exit(1 if any(not ok for _, ok, _ in checks) else 0)
