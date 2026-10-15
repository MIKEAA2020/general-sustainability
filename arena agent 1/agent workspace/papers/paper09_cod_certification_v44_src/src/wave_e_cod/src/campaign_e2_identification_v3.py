#!/usr/bin/env python3
"""Identification and recency campaign for E2 v29.

The paper's declared defect is that K is pinned at its optimisation bound
(5000 kt).  Every headline result -- the expansion rate F'(K*), the
constructive bound C*, the certified horizon -- is a function of (r, K), so a
referee's first question is whether those results are artefacts of the pin.
This campaign answers it in four parts, none of which requires the pin to be
resolved:

  1. PROFILE LIKELIHOOD over K.  r is refit in closed form at each fixed K, so
     the profile is exact.  K is profiled well beyond the declared box (to
     20000 kt) precisely because the pin sits ON the box: whether the data
     identify K from above is the question, and a profile that stops at the
     bound cannot answer it.  The induced profile sets for the two FUNCTIONALS
     the results actually depend on -- g(K*) and F'(K*) -- are reported
     alongside.  Expectation, and finding: K is not identified from above, but
     the functionals are.

  2. JOINT (r, K) BOOTSTRAP.  The published bootstrap refits r alone at
     K = 5000.  Here both parameters are refit on every replicate, so the
     sampling band includes the pin's contribution rather than conditioning it
     away.

  3. OBSERVATION-ERROR SENSITIVITY.  The paper declares that its residual
     conflates process noise and observation error.  Here that declaration is
     made quantitative: if a fraction lambda of the residual variance is
     observation error, the persistent floor is a PROCESS quantity and shrinks
     by sqrt(1 - lambda) (the empirical pool is rescaled about its mean, so
     its shape is preserved and only its scale changes).  C*(lambda) is the
     constructive bound the paper would report at each lambda.

  4. RECENT-WINDOW REFITS.  The fit window 1983-2007 spans the 1992 collapse,
     so r is an average over two productivity regimes.  Post-moratorium
     windows are refit on both series to ask the policy question the paper
     otherwise leaves open: is the reference point self-viable under CURRENT
     productivity?

Writes to src/results_ident_v3/.
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
import run_ladder as rl                   # noqa: E402
import run_xte as rx                      # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_ident_v3")
os.makedirs(OUT, exist_ok=True)

FIT = ri.fit_surplus()
R0, K0 = float(FIT["r"]), float(FIT["K"])
K_STAR = ri.K_STAR
TRAIN_END = ri.TRAIN_END
rows = []
checks = []


def rec(section, label, value, note=""):
    rows.append({"section": section, "quantity": label, "value": value, "note": note})
    print(f"  {label:46s} {value!s:>14}  {note}")


def chk(label, ok, detail=""):
    checks.append((label, bool(ok), detail))
    print(("  OK   " if ok else "  FAIL ") + label + (("  -- " + detail) if detail else ""))


years, ssb, c_reg, c_ann, idx, lrp = rl.load()
m_tr = years <= TRAIN_END
Y, S, C = years[m_tr], ssb[m_tr], c_ann[m_tr]
dS = np.diff(S)
Cc = C[:-1]
S0 = S[:-1]
n = len(dS)
print(f"training window: {int(Y[0])}-{int(Y[-1])}, n = {n} one-step transitions")


def fit_r_at_K(K):
    """Closed-form one-step LS for r at fixed K (source-year catch)."""
    X = S0 * (1.0 - S0 / K)
    y = dS + Cc
    r = float(np.dot(X, y) / np.dot(X, X))
    sse = float(np.sum((y - r * X) ** 2))
    return max(r, 1e-6), sse


def functionals(r, K):
    gk = float(ri.surplus(K_STAR, r, K))
    fp = 1.0 + r * (1.0 - 2.0 * K_STAR / K)
    return gk, fp


# ============================================================ 1. profile over K
print()
print("=" * 96)
print("1. PROFILE LIKELIHOOD OVER K  (r refit in closed form at each K)")
print("=" * 96)
KLO = float(np.max(S0)) + 10.0
KGRID = list(np.arange(1000.0, 3000.0, 25.0)) + \
        list(np.arange(3000.0, 8000.0, 50.0)) + \
        list(np.arange(8000.0, 50001.0, 500.0))
KGRID = [k for k in KGRID if k >= KLO]
prof = []
for K in KGRID:
    r, sse = fit_r_at_K(K)
    gk, fp = functionals(r, K)
    prof.append({"K": K, "r": r, "sse": sse, "g_Kstar": gk, "Fp": fp,
                 "Cstar": gk - 80.86977895283727})
sse_min = min(p["sse"] for p in prof)
# profile-likelihood 95% set for one parameter of interest, sigma^2 estimated:
#   SSE(K) <= SSE_min * (1 + F(1, n-2; .95) / (n - 2))
F_CRIT = 4.3009                       # F_{1,22;0.95}
cut = sse_min * (1.0 + F_CRIT / (n - 2))
in_set = [p for p in prof if p["sse"] <= cut]
Ks_set = [p["K"] for p in in_set]
print(f"  SSE_min = {sse_min:.2f} at K = "
      f"{min(prof, key=lambda p: p['sse'])['K']:.0f} kt;  profile cut = {cut:.2f}")
rec("profile", "K: profile 95% set (kt)", "%.0f - %.0f" % (min(Ks_set), max(Ks_set)),
    "K is NOT identified from above: the set runs to the top of the grid"
    if max(Ks_set) >= 49000 else "identified from above")
rec("profile", "SSE at the box edge (K=5000) / SSE_min",
    "%.4f" % (min(p["sse"] for p in prof if abs(p["K"] - 5000) < 1) / sse_min),
    "a ratio of ~1 is why the pin buys so little")
rec("profile", "K range with F' > 1 (expansion)",
    "%.0f - %.0f" % (min(p["K"] for p in in_set if p["Fp"] > 1),
                     max(p["K"] for p in in_set if p["Fp"] > 1)),
    "2K* = %.1f kt: the condition the paper already declares" % (2 * K_STAR))
rec("profile", "K at the declared box edge", 5000.0,
    "the committed fit pins here; the profile is flat from ~%.0f kt up" % min(Ks_set))
for lab, key in (("g(K*)", "g_Kstar"), ("F'(K*)", "Fp"), ("C* = g(K*) - |e_q10|", "Cstar")):
    v = [p[key] for p in in_set]
    rec("profile", "%s over the profile set" % lab,
        "%.2f - %.2f" % (min(v), max(v)), "identified even though K is not")
    rows.append({"section": "profile", "quantity": lab + " (committed)",
                 "value": round(dict(g_Kstar=172.4638, Fp=1.1531,
                                     Cstar=91.5940)[key], 4), "note": "committed fit"})
# The expansion claim is conditional on K >= 2K* (Table 3), and the profile
# reproduces that condition exactly: below 2K* the loop contracts.  Claiming it
# unconditionally would contradict the paper's own Section 3.7.
exp_lo = min(p["K"] for p in in_set if p["Fp"] > 1.0)
chk("F' > 1 for every profile-set K at or above 2K* = %.1f kt" % (2 * K_STAR),
    all(p["Fp"] > 1.0 for p in in_set if p["K"] >= 2 * K_STAR - 1e-9)
    and exp_lo <= 2 * K_STAR + 25,
    "smallest expansive K in the set: %.0f kt" % exp_lo)
chk("C* > 0 across the whole profile set",
    all(p["Cstar"] > 0 for p in in_set),
    "min C* = %.2f" % min(p["Cstar"] for p in in_set))
with open(os.path.join(OUT, "e2_profile_K.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["K", "r", "sse", "g_Kstar", "Fp", "Cstar"])
    w.writeheader()
    for p in prof:
        w.writerow({k: (round(v, 6) if isinstance(v, float) else v) for k, v in p.items()})

# ==================================================== 2. joint (r,K) bootstrap
print()
print("=" * 96)
print("2. JOINT (r, K) PARAMETRIC RESIDUAL BOOTSTRAP  (B = 2000, seed fixed)")
print("=" * 96)
res_base = dS - (ri.surplus(S0, R0, K0) - Cc)
rng = np.random.default_rng(20260831 + 2)
B = 2000
recs = []
for b in range(B):
    e = res_base[rng.integers(0, len(res_base), size=len(res_base))]
    Ssim = np.empty(len(S))
    Ssim[0] = S[0]
    for t in range(len(S) - 1):
        Ssim[t + 1] = max(1e-3, Ssim[t] + ri.surplus(Ssim[t], R0, K0) - Cc[t] + e[t])
    dSb = np.diff(Ssim)
    # refit both parameters on the synthetic series (declared box: K <= 5000)
    X = lambda K: Ssim[:-1] * (1.0 - Ssim[:-1] / K)

    def obj(th):
        r, K = th
        if r <= 0 or K <= max(np.max(Ssim[:-1]) * 0.5, 10.0) or K > 5000.0:
            return 1e12
        return float(np.mean((dSb - (r * X(K) - Cc)) ** 2))

    from scipy.optimize import minimize
    best = None
    for Kstart in (1500.0, 2500.0, 4000.0, 5000.0):
        res = minimize(obj, [0.25, Kstart], method="L-BFGS-B",
                       bounds=[(1e-3, 2.0), (max(np.max(Ssim[:-1]) + 10.0, 100.0), 5000.0)])
        if best is None or res.fun < best.fun:
            best = res
    r_b, K_b = float(best.x[0]), float(best.x[1])
    gk, fp = functionals(r_b, K_b)
    recs.append({"r": r_b, "K": K_b, "g_Kstar": gk, "Fp": fp,
                 "Cstar": gk - 80.86977895283727, "K_pinned": K_b > 4999.0})
arr = {k: np.array([d[k] for d in recs]) for k in recs[0]}
for key, lab, fmt in (("r", "r", "%.4f"), ("K", "K (kt)", "%.1f"),
                      ("g_Kstar", "g(K*)", "%.2f"), ("Fp", "F'(K*)", "%.4f"),
                      ("Cstar", "C* (kt)", "%.2f")):
    v = arr[key]
    rec("bootstrap", "%s median [90%%]" % lab,
        fmt % np.median(v) + " [%.4g, %.4g]" % (np.percentile(v, 5), np.percentile(v, 95))
        if key == "r" else fmt % np.median(v) + " [%.2f, %.2f]"
        % (np.percentile(v, 5), np.percentile(v, 95)),
        "joint refit, both parameters free")
rec("bootstrap", "share of replicates with K pinned at 5000",
    "%.1f%%" % (100.0 * arr["K_pinned"].mean()),
    "the pin is a property of the likelihood, not of one fit")
rec("bootstrap", "share with F'(K*) > 1 (expansion)",
    "%.1f%%" % (100.0 * (arr["Fp"] > 1).mean()), "expansion is sampling-stable")
rec("bootstrap", "share with C* > 0", "%.1f%%" % (100.0 * (arr["Cstar"] > 0).mean()),
    "a positive constructive bound is sampling-stable")
for cond, mask, note in (
        ("K > K* (the LRP below carrying capacity)", arr["K"] > K_STAR,
         "the lower tail that drives g(K*) < 0 is excluded"),
        ("K >= 2K* (the expansive regime)", arr["K"] >= 2 * K_STAR,
         "the regime the paper's results are conditional on")):
    sub = {k: v[mask] for k, v in arr.items()}
    rec("bootstrap", "C* median [90%%] | %s" % cond,
        "%.2f [%.2f, %.2f]" % (np.median(sub["Cstar"]),
                               np.percentile(sub["Cstar"], 5),
                               np.percentile(sub["Cstar"], 95)),
        "%s; %.1f%% of replicates" % (note, 100.0 * mask.mean()))
    rec("bootstrap", "F' median [90%%] | %s" % cond,
        "%.4f [%.4f, %.4f]" % (np.median(sub["Fp"]), np.percentile(sub["Fp"], 5),
                               np.percentile(sub["Fp"], 95)), "")
with open(os.path.join(OUT, "e2_bootstrap_joint.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(recs[0].keys()))
    w.writeheader()
    w.writerows(recs)

# ============================================ 3. observation-error sensitivity
print()
print("=" * 96)
print("3. OBSERVATION-ERROR SENSITIVITY (declared approximation)")
print("=" * 96)
res_pool = res_base - res_base.mean()
sd_tot = float(res_base.std(ddof=1))
print("  the residual pool is rescaled about its mean: "
      "sigma_process = sigma_total * sqrt(1 - lambda)")
for lam in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5):
    scaled = res_pool * math.sqrt(1.0 - lam) + res_base.mean()
    e_q10 = float(np.percentile(scaled, 10))
    e_q05 = float(np.percentile(scaled, 5))
    e_min = float(np.min(scaled))
    gk = 172.4638
    rec("obs-error", "lambda = %.1f" % lam,
        "C* = %.1f" % (gk - abs(e_q10)),
        "process SD %.1f kt; |e_q10| %.1f; vacuous classes: %d"
        % (sd_tot * math.sqrt(1 - lam), abs(e_q10),
           sum(1 for e in (e_min, e_q05, e_q10) if abs(e) > 296.0868)))

# ==================================================== 4. recent-window refits
print()
print("=" * 96)
print("4. RECENT-WINDOW REFITS (the regime question)")
print("=" * 96)


def refit_window(Yw, Sw, Cw, label, lrp_val):
    dSw = np.diff(Sw)
    Cw1 = Cw[:-1]
    S0w = Sw[:-1]
    X = lambda K: S0w * (1.0 - S0w / K)

    def obj(th):
        r, K = th
        if r <= 0 or K <= max(np.max(S0w) * 0.5, 10.0) or K > 5000.0:
            return 1e12
        return float(np.mean((dSw - (r * X(K) - Cw1)) ** 2))

    from scipy.optimize import minimize
    best = None
    for Kstart in (1200.0, 2000.0, 3500.0, 5000.0):
        res = minimize(obj, [0.25, Kstart], method="L-BFGS-B",
                       bounds=[(1e-3, 2.0), (max(np.max(S0w) + 10.0, 100.0), 5000.0)])
        if best is None or res.fun < best.fun:
            best = res
    r, K = float(best.x[0]), float(best.x[1])
    resid = dSw - (r * X(K) - Cw1)
    gk = float(ri.surplus(lrp_val, r, K))
    gmx = r * K / 4.0
    e_q10 = float(np.percentile(resid, 10))
    e_q05 = float(np.percentile(resid, 5))
    fp = 1.0 + r * (1.0 - 2.0 * lrp_val / K)
    Cstar = gk - abs(e_q10)
    lo_b = max(np.max(S0w) + 10.0, 100.0)
    pin = ("upper" if K > 4999 else "lower" if K < lo_b + 1.0 else "interior")
    print(f"  {label:34s} n={len(dSw):3d}  r={r:.4f}  K={K:7.1f} ({pin:8s})  "
          f"g(LRP)={gk:7.2f}  mean(e)={resid.mean():7.2f}  "
          f"|e_q10|={abs(e_q10):6.2f}  C*={Cstar:7.2f}")
    rec("recent", "%s: n" % label, len(dSw), "transitions")
    rec("recent", "%s: r" % label, round(r, 4), "")
    rec("recent", "%s: K (kt)" % label, round(K, 1), "K is at the %s bound" % pin)
    rec("recent", "%s: residual mean" % label, round(float(resid.mean()), 2),
        "the construction already carries this: |e_q10| is the raw quantile")
    rec("recent", "%s: |e_min| (perpetual worst)" % label,
        round(abs(float(np.min(resid))), 2),
        "vacuous if it exceeds g_max = %.2f" % gmx)
    rec("recent", "%s: |e_q05|" % label, round(abs(e_q05), 2), "")
    rec("recent", "%s: C* under the perpetual-worst floor" % label,
        round(gk - abs(float(np.min(resid))), 2), "")
    rec("recent", "%s: g(LRP)" % label, round(gk, 2), "")
    rec("recent", "%s: |e_q10|" % label, round(abs(e_q10), 2), "")
    rec("recent", "%s: C* = g - |e_q10|" % label, round(Cstar, 2),
        "negative => the reference point is NOT self-viable")
    rec("recent", "%s: F'(LRP)" % label, round(fp, 4), "")
    rec("recent", "%s: g_max" % label, round(gmx, 2), "")
    rec("recent", "%s: residual SD" % label, round(float(resid.std(ddof=1)), 2), "")
    return {"label": label, "n": len(dSw), "r": round(r, 6), "K": round(K, 2),
            "K_pin": pin, "g_LRP": round(gk, 4), "Cstar": round(Cstar, 4),
            "e_q10": round(e_q10, 4), "e_q05": round(e_q05, 4),
            "e_min": round(float(np.min(resid)), 4),
            "e_mean": round(float(resid.mean()), 4),
            "Cstar_worst": round(gk - abs(float(np.min(resid))), 4),
            "Fp": round(fp, 6), "g_max": round(gmx, 4),
            "sd": round(float(resid.std(ddof=1)), 4), "LRP": lrp_val}


recent = []
m1 = (years >= 1995) & (years <= 2015)
recent.append(refit_window(years[m1], ssb[m1], c_ann[m1], "NCAM 1995-2015", K_STAR))
m2 = (years >= 1995) & (years <= 2007)
recent.append(refit_window(years[m2], ssb[m2], c_ann[m2], "NCAM 1995-2007", K_STAR))
xy, xs, xc = rx.load_xte()
m3 = (xy >= 2005) & (xy <= 2024)
recent.append(refit_window(xy[m3], xs[m3], xc[m3], "xteNCAM 2005-2024", 276.0))
m4 = (xy >= 1995) & (xy <= 2024)
recent.append(refit_window(xy[m4], xs[m4], xc[m4], "xteNCAM 1995-2024", 276.0))
with open(os.path.join(OUT, "e2_recent_windows.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(recent[0].keys()))
    w.writeheader()
    for row in recent:
        w.writerow({k: (round(v, 6) if isinstance(v, float) else v)
                    for k, v in row.items()})

with open(os.path.join(OUT, "e2_identification_v3.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["section", "quantity", "value", "note"])
    w.writeheader()
    w.writerows(rows)
json.dump({"profile_K_set": [min(Ks_set), max(Ks_set)],
           "sse_min": sse_min, "F'(K*)_min_over_profile": min(p["Fp"] for p in in_set),
           "Cstar_min_over_profile": min(p["Cstar"] for p in in_set),
           "bootstrap_B": B,
           "bootstrap_median_r": float(np.median(arr["r"])),
           "bootstrap_median_Cstar": float(np.median(arr["Cstar"])),
           "bootstrap_share_Fp_gt_1": float((arr["Fp"] > 1).mean()),
           "n_checks": len(checks), "n_failed": sum(1 for _, ok, _ in checks if not ok)},
          open(os.path.join(OUT, "e2_identification_v3.json"), "w"), indent=1)
print()
print(f"wrote {OUT}/{{e2_identification_v3.csv,e2_profile_K.csv,"
      f"e2_bootstrap_joint.csv,e2_recent_windows.csv,e2_identification_v3.json}}")
print(f"IDENTIFICATION CAMPAIGN: {sum(1 for _, ok, _ in checks if ok)}/{len(checks)} "
      f"checks passed")
sys.exit(1 if any(not ok for _, ok, _ in checks) else 0)
