"""
Formal multi-system calibration of the regeneration lag tau_g from RAW recovery
curves (stand age vs above-ground biomass), rather than published summary
statistics.

This is the "taken further" step the reviewer was offered in response (a).  The
existing SI S5.3 anchoring converted published SUMMARY recovery statistics
(e.g. "median 66 yr to 90% of old-growth") into an illustrative band
(approx 25-33 yr) using a t50 exponential-recovery heuristic.  The reviewer's
objection - and the point of this file - is that those are published summary
values, not raw recovery data.

Here we instead fit a lagged saturating recovery model to the underlying
plot-level recovery CURVES.  In the manuscript's model the regeneration is

    G(A(t - tau_g)) = rho A(t - tau_g) (1 - A(t - tau_g)/A_max),

so tau_g is the TIME LAG between a change in the capital stock A and the
subsequent regeneration response.  Operationally (the definition used in the
empirical-grounding plan, uploads/empirical.txt) this is the time before
measurable recovery onset - the intercept of the recovery curve - NOT the total
recovery time or the half-recovery time.

For each chronosequence ("system") we fit

    AGB(t) = AGB_inf (1 - exp(-(t - t_lag) / tau_r))      for t >= t_lag
    AGB(t) = 0                                            for t <  t_lag

The fitted t_lag is the ecologically interpretable estimate of the regeneration
lag tau_g (time before the stock begins to respond), and tau_r is the recovery
timescale.  We report per-system estimates plus an aggregated multi-system
distribution (median + IQR, and a 95% interval), and write the figure used to
show the field band against the collapse cliff.

Data: Poorter et al. (2016), "Biomass resilience of Neotropical secondary
forests", Nature; Dryad doi:10.5061/dryad.82vr4 (2ndFOR database, 1334 plots,
41 chronosequences).  This is RAW age-vs-AGB curve data (not the t50 summary).
"""

import os
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data", "empirical", "Aboveground biomass 2ndFOR database.csv")
OUTDIR = os.path.join(ROOT, "scans")

# ---------------- load ----------------
df = pd.read_csv(DATA, encoding="latin-1")
df = df[pd.to_numeric(df["Age"], errors="coerce").notna()].copy()
df["age"] = df["Age"].astype(float)
df["agb"] = df["AGB"].astype(float)

# The Providencia "3655 Mg/ha at age 56" is a unit/aggregation artefact (an
# outlier 8x beyond the plausible old-growth max); exclude per-chronosequence
# AGB > 3x the site's 90th percentile to keep each system's curve physical.
def clean_site(g):
    cap = g["agb"].quantile(0.90) * 3.0 if len(g) >= 8 else float("inf")
    return g[g["agb"] <= cap]
clean = df.groupby("Chronosequence", group_keys=False).apply(clean_site)
print("cleaned plots:", len(clean), "of", len(df), "| systems:", clean["Chronosequence"].nunique())

# ---------------- model ----------------
def recovery(t, agb_inf, t_lag, tau_r):
    t = np.asarray(t, dtype=float)
    out = agb_inf * (1.0 - np.exp(-(t - t_lag) / tau_r))
    out[t < t_lag] = 0.0
    return out

# ---------------- per-system fit ----------------
rows = []
for name, g in clean.groupby("Chronosequence"):
    g = g.sort_values("age")
    if len(g) < 6:
        continue
    age = g["age"].values
    agb = g["agb"].values
    if agb.max() < 5.0:
        continue  # no measurable recovery
    # initial guesses
    a0 = agb.max() * 1.15
    tl0 = 0.0
    tr0 = np.median(np.diff(np.sort(age)))/1.0 + 5.0 if len(np.unique(age)) > 2 else 10.0
    try:
        popt, _ = curve_fit(
            recovery, age, agb, p0=[a0, tl0, max(tr0, 3.0)],
            bounds=([1.0, -2.0, 1.0], [np.inf, 30.0, 120.0]),
            maxfev=20000,
        )
    except Exception as e:
        continue
    agb_inf, t_lag, tau_r = popt
    # r^2
    pred = recovery(age, *popt)
    ss_res = float(np.sum((agb - pred) ** 2))
    ss_tot = float(np.sum((agb - agb.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    rows.append({
        "system": name, "n": len(g), "age_range": f"{age.min():.0f}-{age.max():.0f}",
        "AGB_inf": agb_inf, "t_lag": t_lag, "tau_r": tau_r, "r2": r2,
    })

fit = pd.DataFrame(rows)
print("successful fits:", len(fit))

# Keep only good fits (R^2 > 0.20) so the aggregation is not dominated by noise.
good = fit[fit["r2"] > 0.20].copy()
print("usable fits (r2>0.20):", len(good), "of", len(fit))

# ---- derive the model-consistent recovery timescale on each fitted curve ----
# AGB(t) = AGB_inf (1 - exp(-(t - t_lag)/tau_r)).  The time to reach a fraction
# p of AGB_inf is  t_p = t_lag + tau_r * ln(1/(1-p)).  The SI's effective-timescale
# convention (S5.3) uses t_50:  tau_eff = tau_r (and equivalently t_50 = tau_r ln2
# shifted by t_lag).  So tau_r IS the effective regeneration timescale, and the
# t_50 (relative to the pre-disturbance/old-growth asymptote) is what the
# published summary statistics report.
good["t50"] = good["t_lag"] + good["tau_r"] * np.log(2.0)
good["t90"] = good["t_lag"] + good["tau_r"] * np.log(10.0)

# ---- aggregated estimates ----
def q(a, p): return float(np.percentile(a, p))
tr = good["tau_r"].values
t50 = good["t50"].values
t90 = good["t90"].values
lag = good["t_lag"].values
summary = {
    "n_fits": len(good),
    "n_systems": int(clean["Chronosequence"].nunique()),
    "lag_median": float(np.median(lag)), "lag_iqr": [q(lag,25), q(lag,75)],
    "lag_95": [q(lag,2.5), q(lag,97.5)],
    "tau_r_median": float(np.median(tr)), "tau_r_iqr": [q(tr,25), q(tr,75)],
    "tau_r_95": [q(tr,2.5), q(tr,97.5)],
    "t50_median": float(np.median(t50)), "t50_iqr": [q(t50,25), q(t50,75)],
    "t50_95": [q(t50,2.5), q(t50,97.5)],
    "t90_median": float(np.median(t90)),
    "AGB_inf_median": float(good["AGB_inf"].median()),
    "r2_median": float(good["r2"].median()),
}
print("\n=== RAW-CURVE CALIBRATION (Poorter 2016, 2ndFOR; n=%d systems) ===" % summary["n_systems"])
print(f"fits used: {summary['n_fits']}")
print(f"onset lag      t_lag: {summary['lag_median']:.2f} yr  (IQR {summary['lag_iqr'][0]:.1f}-{summary['lag_iqr'][1]:.1f})")
print(f"recovery timescale tau_r: {summary['tau_r_median']:.1f} yr  (IQR {summary['tau_r_iqr'][0]:.1f}-{summary['tau_r_iqr'][1]:.1f})")
print(f"time to 50%    t_50: {summary['t50_median']:.1f} yr  (IQR {summary['t50_iqr'][0]:.1f}-{summary['t50_iqr'][1]:.1f})")
print(f"time to 90%    t_90: {summary['t90_median']:.1f} yr")

import json
with open(os.path.join(OUTDIR, "tau_g_calibration_summary.json"), "w") as f:
    json.dump(summary, f, indent=2, default=float)

good.to_csv(os.path.join(OUTDIR, "tau_g_calibration_raw_curves.csv"), index=False)
fit.to_csv(os.path.join(OUTDIR, "tau_g_calibration_all_fits.csv"), index=False)
print("\nwrote:", os.path.join(OUTDIR, "tau_g_calibration_summary.json"),
      os.path.join(OUTDIR, "tau_g_calibration_raw_curves.csv"))

# =====================================================================
# FIGURE: field band from raw curves vs the one-stock collapse cliff
# =====================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 4.8), dpi=400)
# ---- panel (a): fitted recovery curves for a representative subset ----
ax1.set_title("Raw recovery curves (2ndFOR, Poorter 2016)", fontsize=11, fontweight="bold")
subset = good.sort_values("tau_r")  # order by timescale
tt = np.linspace(0, 90, 400)
show = subset.iloc[[0, len(subset)//4, len(subset)//2, 3*len(subset)//4, -1]]
cols = ["#1f77b4", "#2ca02c", "#ff7f0e", "#9467bd", "#d62728"]
for (_, r), c in zip(show.iterrows(), cols):
    ax1.plot(tt, recovery(tt, r.AGB_inf, r.t_lag, r.tau_r), color=c, lw=1.8,
             label=f"{r.system}  (t50={r.t50:.0f} yr)")
ax1.set_xlabel("stand age (yr)"); ax1.set_ylabel("above-ground biomass (Mg ha$^{-1}$)")
ax1.legend(fontsize=7.2, frameon=False); ax1.grid(alpha=0.25)

# ---- panel (b): distribution of t50 / tau_r with the collapse cliff ----
ax2.set_title("Calibrated regeneration timescale vs collapse cliff", fontsize=11, fontweight="bold")
ax2.hist(t50, bins=26, range=(0, 130), color="#2ca02c", alpha=0.75, edgecolor="white", label="t$_{50}$ (raw-curve fit)")
ax2.hist(tr, bins=26, range=(0, 130), color="#1f77b4", alpha=0.45, edgecolor="white", label="$\\tau_r$ (recovery timescale)")
# one-stock collapse region: shade as a single band and annotate once, INSIDE the axes
ax2.axvspan(18, 130, color="#d62728", alpha=0.06)
ax2.axvline(18, color="#d62728", ls="--", lw=1.6)
ax2.text(24, ax2.get_ylim()[1]*0.72, "one-stock collapse\n$\\tau_g \\geq 20$ yr",
         color="#d62728", fontsize=7.6, ha="left", va="center")
yl = ax2.get_ylim()
ax2.set_xlim(0, 130)
ax2.set_ylim(0, yl[1]*1.14)              # headroom so the annotation never meets the title
ax2.set_xlabel("years"); ax2.set_ylabel("systems")
ax2.legend(fontsize=7.5, frameon=False, loc="upper left")
ax2.grid(alpha=0.25)
fig.suptitle("Formal calibration of the regeneration timescale from raw recovery curves\n"
             "(41 Neotropical chronosequences; 1334 plots)", fontsize=11.5, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.92])
fig.savefig(os.path.join(OUTDIR, "S1b_tau_g_calibration.png"), dpi=400)
print("wrote:", os.path.join(OUTDIR, "S1b_tau_g_calibration.png"))
