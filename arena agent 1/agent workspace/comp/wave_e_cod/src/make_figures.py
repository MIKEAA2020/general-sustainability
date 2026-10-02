#!/usr/bin/env python3
"""Publication figures for the Wave E ladder."""

from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results"
FIG = ROOT / "manuscript"
FIG.mkdir(exist_ok=True)

tab = pd.read_csv(DATA / "ncam_2016_table_a2.csv")
years, ssb = tab["year"].to_numpy(), tab["ssb_kt"].to_numpy()
lrp = float(np.mean(ssb[(years >= 1983) & (years <= 1989)]))
paths_raw = json.loads((OUT / "paths.json").read_text())
# pass 2 uses annual catch for the published path figure
paths = paths_raw["annual"] if "annual" in paths_raw else paths_raw
roll = pd.read_csv(OUT / "rolling_summary.csv")
# rolling bars: annual catch + naive + survey start
roll = roll[roll["catch"].isin(["annual", "na"])]

# Figure 1 — series and LRP
fig, ax = plt.subplots(figsize=(7.2, 3.6))
ax.plot(years, ssb, color="#1b4f72", lw=2.0, marker="o", ms=3.5, label="NCAM M-shift SSB")
ax.axhline(lrp, color="#922b21", ls="--", lw=1.2, label=f"LRP (1983–89 mean) = {lrp:.0f} kt")
ax.axvline(1992, color="#7d3c98", ls=":", lw=1.2, label="Moratorium (1992)")
ax.fill_between([1991, 1995], 0, 1100, color="#f5b7b1", alpha=0.35, label="Collapse test")
ax.fill_between([2008, 2015], 0, 1100, color="#aed6f1", alpha=0.35, label="Recovery test")
ax.set_ylim(0, 1100)
ax.set_xlim(1982.5, 2015.5)
ax.set_xlabel("Year")
ax.set_ylabel("SSB (kt)")
ax.legend(fontsize=8, loc="upper right", frameon=False)
ax.set_title("Northern cod 2J3KL — locked observation series")
fig.tight_layout()
fig.savefig(FIG / "fig1_series.png", dpi=160)
fig.savefig(FIG / "fig1_series.svg")
plt.close()

# Figure 2 — collapse and recovery paths
fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.5), sharey=False)
want = [
    ("M1_autonomous_Schaefer", "#922b21", "M1 autonomous"),
    ("M2_stockflow_regimeC", "#1a5276", "M2 annual catch"),
    ("M3_AR_residual", "#117a65", "M3 AR residual"),
    ("M4_delayed_info", "#b9770e", "M4 delayed info"),
]
for ax, window, title in (
    (axes[0], "collapse", "Collapse window (train 1983–90)"),
    (axes[1], "recovery", "Recovery window (train 1995–2007)"),
):
    # observed
    key0 = f"{window}:M1_autonomous_Schaefer"
    ax.plot(paths[key0]["year"], paths[key0]["obs"], "k-o", lw=2, ms=4, label="Observed SSB")
    ax.axhline(lrp, color="#922b21", ls="--", lw=0.9)
    for m, col, lab in want:
        p = paths[f"{window}:{m}"]
        ax.plot(p["year"], p["pred"], color=col, lw=1.6, label=lab)
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("Year")
    ax.set_ylabel("SSB (kt)")
axes[0].legend(fontsize=7, frameon=False)
fig.tight_layout()
fig.savefig(FIG / "fig2_windows.png", dpi=160)
fig.savefig(FIG / "fig2_windows.svg")
plt.close()

# Figure 3 — rolling RMSE vs naive
fig, ax = plt.subplots(figsize=(7.2, 3.6))
order = [
    "naive_persist",
    "M1_autonomous_Schaefer",
    "M1b_autonomous_Allee",
    "M2_stockflow_regimeC",
    "M3_AR_residual",
    "M4_delayed_info",
    "M2_survey_start",
    "naive_train_mean",
]
labels = {
    "naive_persist": "Naive persist",
    "naive_train_mean": "Naive train-mean",
    "M1_autonomous_Schaefer": "M1 Schaefer",
    "M1b_autonomous_Allee": "M1b Allee",
    "M2_stockflow_regimeC": "M2 annual catch",
    "M3_AR_residual": "M3 AR residual",
    "M4_delayed_info": "M4 delayed",
    "M2_survey_start": "M2 survey start",
}
def _rmse(m, h):
    sub = roll[(roll.model == m) & (roll.horizon == h)]
    return float(sub["rmse"].iloc[0]) if len(sub) else np.nan

order = [m for m in order if len(roll[roll.model == m])]
x = np.arange(len(order))
w = 0.38
r1 = [_rmse(m, 1) for m in order]
r5 = [_rmse(m, 5) for m in order]
ax.bar(x - w / 2, r1, w, color="#1b4f72", label="1-year")
ax.bar(x + w / 2, r5, w, color="#d4ac0d", label="5-year")
ax.set_xticks(x)
ax.set_xticklabels([labels[m] for m in order], rotation=30, ha="right")
ax.set_ylabel("RMSE (kt SSB)")
ax.set_title("Rolling-origin RMSE — structural models vs naive baselines")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(FIG / "fig3_rmse.png", dpi=160)
fig.savefig(FIG / "fig3_rmse.svg")
plt.close()
print("wrote figures")
