"""
Fishery leg of the regeneration-timescale estimate: fit a saturating recovery
curve to the post-depletion recovery of each stock, using the RAM Legacy
B/BMSY time series.

Analogous to the forest leg (calibrate_tau_g_recovery_curves.py): there we fit
AGB(t) = AGB_inf (1 - exp(-(t - t_lag)/tau_r)) on stand age t.  Here the
"recovery" object is the stock biomass relative to MSY (B/BMSY) recovering from
a depleted trough toward a rebuilt reference (~1).  For each stock we locate the
depletion trough and fit the rising tail

    rel(t) = 1 - exp(-(t - t_lag) / tau_r)          (relative recovery 0 -> 1)

where t is years since the trough (so t_lag is the lag before recovery begins,
tau_r the recovery timescale; t_50 = t_lag + tau_r ln 2).  The model-consistent
quantity is, as in the forest leg, a *recovery timescale* (the rate rho object),
mapped to tau_g only via the stated effective-timescale heuristic -- it is NOT a
direct measurement of the lag tau_g.

Data: RAM Legacy Stock Assessment Database (B/BMSY by stock and year, 2001-2015),
via the OHI 2019 Food Provision / Fisheries processing (doi:10.5281/zenodo.2542919;
https://raw.githubusercontent.com/OHI-Science/ohiprep_v2019/master/globalprep/fis/v2019/int/ram_bmsy.csv).
This is raw per-stock, per-year relative-biomass curves, not published recovery
summaries.  Caveat: the window is 2001-2015, so slow rebuilds are right-censored;
we flag that rather than treating a censored trajectory as a completed recovery.
"""

import os, json
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data", "empirical", "ram_bmsy.csv")
OUTDIR = os.path.join(ROOT, "scans")

df = pd.read_csv(DATA)
df = df.dropna(subset=["ram_bmsy"]).copy()
# one record per stock-year (the raw DB has per-assessment duplicates)
df["year"] = df["year"].astype(int)
df = df.sort_values(["stockid", "year"]).groupby(["stockid", "year"], as_index=False).agg(
    ram_bmsy=("ram_bmsy", "mean"), stocklong=("stocklong", "first"))
print("stocks:", df["stockid"].nunique(), "| stock-years:", len(df))


def recovery(t, t_lag, tau_r):
    t = np.asarray(t, dtype=float)
    out = 1.0 - np.exp(-(t - t_lag) / tau_r)
    out[t < t_lag] = 0.0
    return out


rows = []
for sid, g in df.groupby("stockid"):
    g = g.sort_values("year").reset_index(drop=True)
    y = g["ram_bmsy"].values
    yrs = g["year"].values
    if len(y) < 6:
        continue
    # require a depletion trough then a meaningful rise
    imin = int(np.argmin(y))
    if y[imin] > 0.55:          # never dropped below ~0.55 MSY: not a recovery episode
        continue
    tail = y[imin:]
    yrs_tail = yrs[imin:]
    if tail.max() < 0.75:       # no substantial rebuild in-window (right-censored)
        continue
    # relative recovery from trough toward the post-trough max/reference
    y0 = y[imin]
    yref = tail.max()
    rel = (tail - y0) / (yref - y0) if yref > y0 else np.nan
    t = yrs_tail - yrs[imin]     # years since trough
    if np.nanmax(rel) < 0.5 or len(rel) < 4:
        continue
    rel = np.nan_to_num(rel, nan=0.0)
    try:
        popt, _ = curve_fit(recovery, t, rel, p0=[0.0, 5.0],
                            bounds=([-2.0, 1.0], [12.0, 60.0]), maxfev=20000)
    except Exception:
        continue
    t_lag, tau_r = popt
    pred = recovery(t, *popt)
    ss_res = float(np.sum((rel - pred) ** 2)); ss_tot = float(np.sum((rel - rel.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    rows.append({"stock": sid, "name": g["stocklong"].iloc[0], "n": len(t),
                 "trough_B": y[imin], "peak_B": yref, "t_lag": t_lag, "tau_r": tau_r,
                 "t50": t_lag + tau_r * np.log(2.0), "r2": r2, "censored": bool(rel[-1] < 0.95)})

fit = pd.DataFrame(rows)
good = fit[fit["r2"] > 0.3].copy()
print("recovery episodes fit:", len(fit), "| usable (r2>0.3):", len(good))


def q(a, p): return float(np.percentile(a, p))
tr = good["tau_r"].values; t50 = good["t50"].values
summary = {
    "n_episodes": len(good), "n_stocks_considered": int(df["stockid"].nunique()),
    "tau_r_median": float(np.median(tr)), "tau_r_iqr": [q(tr, 25), q(tr, 75)],
    "tau_r_95": [q(tr, 2.5), q(tr, 97.5)],
    "t50_median": float(np.median(t50)), "t50_iqr": [q(t50, 25), q(t50, 75)],
    "t50_95": [q(t50, 2.5), q(t50, 97.5)],
    "n_censored": int(good["censored"].sum()), "r2_median": float(good["r2"].median()),
}
print("\n=== FISHERY RAW-CURVE RECOVERY-TIMESCALE (RAM Legacy B/BMSY) ===")
print(f"recovery episodes used: {summary['n_episodes']}  (of {summary['n_stocks_considered']} stocks)")
print(f"t_lag (onset): {np.median(good['t_lag']):.1f} yr")
print(f"recovery timescale tau_r: {summary['tau_r_median']:.1f} yr  (IQR {summary['tau_r_iqr'][0]:.1f}-{summary['tau_r_iqr'][1]:.1f})")
print(f"time to 50% t_50: {summary['t50_median']:.1f} yr  (IQR {summary['t50_iqr'][0]:.1f}-{summary['t50_iqr'][1]:.1f})")
print(f"right-censored trajectories in the good set: {summary['n_censored']}")

with open(os.path.join(OUTDIR, "tau_g_calibration_fisheries.json"), "w") as f:
    json.dump(summary, f, indent=2, default=float)
good.to_csv(os.path.join(OUTDIR, "tau_g_calibration_fisheries.csv"), index=False)
print("wrote:", os.path.join(OUTDIR, "tau_g_calibration_fisheries.json"))

# figure
fig, ax = plt.subplots(figsize=(8.6, 4.4), dpi=400)
tt = np.linspace(0, 16, 300)
show = good.sort_values("tau_r").iloc[[0, len(good)//4, len(good)//2, 3*len(good)//4, -1]]
colors = ["#1f77b4", "#2ca02c", "#ff7f0e", "#9467bd", "#d62728"]
for (_, r), c in zip(show.iterrows(), colors):
    ax.plot(tt, recovery(tt, r.t_lag, r.tau_r), color=c, lw=1.8,
            label=f"{str(r.name)[:26]} (t50={r.t50:.0f} yr)")
ax.set_xlabel("years since depletion trough"); ax.set_ylabel("relative recovery (0 to 1)")
ax.set_title("Fishery recovery curves (RAM Legacy B/BMSY, 2001-2015)", fontsize=11, fontweight="bold")
ax.legend(fontsize=7.0, frameon=False); ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(os.path.join(OUTDIR, "S1c_fishery_recovery.png"), dpi=400)
print("wrote:", os.path.join(OUTDIR, "S1c_fishery_recovery.png"))
