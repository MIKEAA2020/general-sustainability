#!/usr/bin/env python3
"""figs_p4/fig2_five_regime_topology.py — five-regime topology figure for P4.

Drawn ONLY from the committed five-regime campaign records:
  research_program/validated_computations/p4_five_regime_campaign/
    p4_branch_small_lower.csv / p4_branch_large_lower.csv / p4_branch_small_upper.csv
    p4_basin_archive.csv / p4_campaign_results.json
(commit 295d4f4, executed 2026-09-02 under the pre-registered plan; first run,
no independent rerun yet). No inherited (legacy) number is drawn.

Panels: (a) lower S-branch; (b) upper region; (c) multiplier tracks; (d) basin grid.
"""
import pandas as pd
import numpy as np
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = "/home/user/arena agen1/repo_assets_mirror/p4_five_regime_campaign"
BASE2 = "/home/user/arena agen1/repo_assets_mirror/a025_second_fold"
small_lower = pd.read_csv(f"{BASE}/p4_branch_small_lower.csv")
large_lower = pd.read_csv(f"{BASE}/p4_branch_large_lower.csv")
small_upper = pd.read_csv(f"{BASE}/p4_branch_small_upper.csv")
sf_branch = pd.read_csv(f"{BASE2}/second_fold_branch.csv")
sf_basin = pd.read_csv(f"{BASE2}/second_fold_basin.csv")
basin = pd.read_csv(f"{BASE}/p4_basin_archive.csv")
res = json.load(open(f"{BASE}/p4_campaign_results.json"))

TAU_MINUS = 3.6661490142741          # certified Hopf (lower), interval midpoint
TAU_PLUS = 150.3584773101415         # certified Hopf (upper), interval midpoint
FOLD = 5.5872361986901               # certified fold (m=64 MS; Krawczyk box)
FOLD2 = 64.4023272033699              # certified second fold (m=64 MS; Krawczyk box)
CAP_LO, CAP_HI = 148.6, 149.5        # basin-grid capture onset bracket

fig, axs = plt.subplots(2, 2, figsize=(9.2, 7.4))
C = {"settles": "#2b6cb0", "captured": "#c53030", "intermediate": "#d69e2e"}

# ---- (a) lower S-branch ----
ax = axs[0, 0]
ax.plot(small_lower.tau, small_lower.N_ptp, color="#c53030", lw=1.6,
        label="small arm (subcritical Hopf; $\\mu_1>1$, unstable)")
ax.plot(large_lower.tau, large_lower.N_ptp, color="#2b6cb0", lw=1.6,
        label="large arm ($\\mu_1<1$, stable)")
ax.axvline(TAU_MINUS, color="0.55", ls="--", lw=1)
ax.text(TAU_MINUS + 0.02, 1.25, "$\\tau_-=3.66615$ (cert.)", fontsize=8, rotation=90, va="bottom")
ax.axvline(FOLD, color="0.2", ls="--", lw=1.1)
ax.text(FOLD + 0.015, 1.25, "$\\tau_f=5.5872362$ (Krawczyk-cert.)", fontsize=8, rotation=90, va="bottom")
ax.set_yscale("log")
ax.set_xlim(1.5, 5.95)
ax.set_ylim(1, 90)
ax.set_xlabel("delay $\\tau$ (yr)")
ax.set_ylabel("peak-to-peak $N$-amplitude (log)")
ax.set_title("(a) lower boundary: one S-shaped branch, one fold", fontsize=9)
ax.legend(fontsize=7, loc="upper left", framealpha=0.9)
ax.grid(alpha=0.25, lw=0.4)

# ---- (b) upper region ----
ax = axs[0, 1]
ax.plot(small_upper.tau, small_upper.N_ptp, color="#2b6cb0", lw=1.6,
        label="Hopf small branch (collocated)")
ax.axvspan(CAP_LO, CAP_HI, color="#c53030", alpha=0.14)
ax.text((CAP_LO + CAP_HI) / 2, 1.02, "capture onset\n[148.6, 149.5]\n(basin grid)", ha="center", va="bottom", fontsize=7.5, color="#8f1d1d")
ax.axvline(TAU_PLUS, color="0.55", ls="--", lw=1)
ax.text(TAU_PLUS + 0.12, 1.02, "$\\tau_+=150.35848$ (cert.)", fontsize=8, rotation=90, va="bottom")
ax.set_yscale("log")
ax.set_xlim(128, 156)
ax.set_ylim(0.05, 3.2)
ax.set_xlabel("delay $\\tau$ (yr)")
ax.set_ylabel("peak-to-peak $N$-amplitude (log)")
ax.set_title("(b) upper region: face-cycle family (basin record only)", fontsize=9)
ax.legend(fontsize=7, loc="lower left", framealpha=0.9)
ax.grid(alpha=0.25, lw=0.4)

# ---- (c) multiplier tracks ----
ax = axs[1, 0]
ax.plot(small_lower.tau, small_lower.mu1_re, color="#c53030", lw=1.6, label="small arm $\\mu_1$")
ax.plot(large_lower.tau, large_lower.mu1_re, color="#2b6cb0", lw=1.6, label="large arm $\\mu_1$")
ax.axhline(1.0, color="0.2", lw=1.0)
ax.text(5.80, 1.0, "+1", fontsize=9, va="bottom", ha="left")
ax.axvline(FOLD, color="0.2", ls="--", lw=1.1)
ax.set_xlim(3.5, 5.95)
ax.set_ylim(0.0, 1.6)
ax.set_xlabel("delay $\\tau$ (yr)")
ax.set_ylabel("dominant real multiplier $\\mu_1$")
ax.set_title("(c) both arms cross +1 at the same fold (real at every record)", fontsize=9)
ax.legend(fontsize=7, loc="upper left", framealpha=0.9)
ax.grid(alpha=0.25, lw=0.4)

# ---- (d) basin grid ----
ax = axs[1, 1]
hist = {"H1 (large stock)": 0, "H2 (depleted)": 1, "H3 (near-eq.)": 2}
hmap = {"H1": "H1 (large stock)", "H2": "H2 (depleted)", "H3": "H3 (near-eq.)"}
for h in ["H1", "H2", "H3"]:
    sub = basin[(basin.history == h) & (basin.dt == 0.02)]
    y = hist[hmap[h]]
    for cls, grp in sub.groupby("classification"):
        ax.scatter(grp.tau, [y] * len(grp), s=34, color=C[cls],
                   edgecolor="0.3", lw=0.4, zorder=3,
                   label=None if h != "H1" else cls)
for b, lab in [(TAU_MINUS, "$\\tau_-$"), (FOLD, "fold"), (FOLD2, "$\\tau_{f2}$"), (CAP_LO, ""), (CAP_HI, ""), (TAU_PLUS, "$\\tau_+$")]:
    ax.axvline(b, color="0.55" if lab else "0.8", ls="--", lw=0.8)
    if lab:
        ax.text(b, 2.62, lab, fontsize=8, ha="center")
# second-fold grids (squares; grid A 133-146, grid B 62.4-66.4)
for h in ["H1", "H2", "H3"]:
    sub = sf_basin[(sf_basin.history == h) & (sf_basin.dt == 0.02)]
    y = hist[hmap[h]]
    for cls, grp in sub.groupby("classification"):
        ax.scatter(grp.tau, [y] * len(grp), s=26, color=C[cls], marker="s",
                   edgecolor="0.25", lw=0.3, zorder=3)
ax.set_yticks([0, 1, 2]); ax.set_yticklabels(list(hist.keys()), fontsize=8)
ax.set_xlim(0, 158)
ax.set_xlabel("delay $\\tau$ (yr)")
ax.set_title("(d) basin classifications: 27$\\times$3 grid (circles) + second-fold grids A/B (squares), dt = 0.02", fontsize=9)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=C[k], label=k) for k in ["captured", "settles", "intermediate"]],
          fontsize=7, loc="lower left", framealpha=0.9)
ax.grid(alpha=0.2, lw=0.4, axis="x")

fig.suptitle("Five-regime attractor topology — committed records, both campaigns (2026-09-02, first runs, "
             "no independent reruns yet; all data from the deposited p4_five_regime_campaign/ and "
             "a025_second_fold/ CSVs; no inherited number drawn)",
             fontsize=8.5, y=0.995)
fig.tight_layout(rect=[0, 0, 1, 0.985])
out = "/home/user/arena agen1/figs_p4/fig2_five_regime_topology_v2.png"
fig.savefig(out, dpi=160)
print("saved", out)
