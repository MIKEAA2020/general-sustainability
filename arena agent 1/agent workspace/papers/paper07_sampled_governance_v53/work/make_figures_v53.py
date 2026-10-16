#!/usr/bin/env python3
"""Render the v53 joint-box crossing summary from the retained 20,001-grid JSON."""
from pathlib import Path
import json
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
record = json.loads((ROOT / "work/joint_box_fullgrid.json").read_text())
boxes = record["boxes"]
fig, ax = plt.subplots(figsize=(9.2, 4.3), constrained_layout=True)
colors = {"0.5_percent": "#147d75", "1_percent": "#d97724"}
labels = {"0.5_percent": r"$\pm0.5\%$ box", "1_percent": r"$\pm1\%$ box"}
ypos = {"0.5_percent": 1.0, "1_percent": 0.0}
for key in ("0.5_percent", "1_percent"):
    b = boxes[key]
    vals = sorted(c["first_crossing"] for c in b["corners"] if c["first_crossing"] is not None)
    lo, hi = vals[0], vals[-1]
    med = vals[len(vals)//2]
    y = ypos[key]
    c = colors[key]
    ax.plot([lo, hi], [y, y], color=c, linewidth=7, solid_capstyle="round", zorder=2)
    ax.scatter([lo, hi], [y, y], color=c, s=40, edgecolor="white", linewidth=0.6, zorder=3)
    ax.scatter([med], [y], color="white", s=58, edgecolor=c, linewidth=2, zorder=4)
    ax.text(14.85, y + 0.12,
            f"{b['corners_with_crossing']}/64 crossing; "
            f"{b['corners_without_crossing']} no crossing, all grid-stable",
            ha="right", va="bottom", fontsize=9, color="#25313b")
    ax.text(lo, y - 0.18, f"{lo:.2f}", ha="center", va="top", fontsize=8, color=c)
    ax.text(hi, y - 0.18, f"{hi:.2f}", ha="center", va="top", fontsize=8, color=c)
ax.axvline(6.5012949481, color="#273444", linestyle="--", linewidth=1.4,
           label="baseline crossing 6.501 yr")
ax.set_yticks([1.0, 0.0], [labels["0.5_percent"], labels["1_percent"]])
ax.set_xlim(0, 15)
ax.set_ylim(-0.45, 1.52)
ax.set_xlabel("First unit-circle crossing among corners (years)")
ax.set_title("Joint parameter perturbations move or remove the baseline crossing", pad=12)
ax.grid(axis="x", color="#d9e0e6", linewidth=0.8)
ax.set_axisbelow(True)
ax.legend(loc="lower right", frameon=False, fontsize=9)
fig.text(0.5, -0.015,
         "No-crossing corners stayed stable on a 20,001-point Tr grid; this is a dense-grid numerical result, not a continuous proof.",
         ha="center", va="top", fontsize=8.5, color="#425466")
fig.savefig(ROOT / "figs/fig_joint_sensitivity_v53.png", dpi=220, bbox_inches="tight")
print(f"saved {ROOT / 'figs/fig_joint_sensitivity_v53.png'}")
