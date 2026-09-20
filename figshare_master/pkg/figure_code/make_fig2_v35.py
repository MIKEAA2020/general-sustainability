#!/usr/bin/env python3
"""Regenerate Figure 2 (weight-interval view) for v35: a single x-axis label on the
bottom panel only (was duplicated under both panels), with a little extra labelpad.
All numbers follow the witness datum: (x, s1, s2) = (1/2, 6/5, 6/5),
rho_1 = 2/3, rho_2 = 3/2, worst-case dip depth 2, gain e = (1/4, 1/4)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

OUT = "./"
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "axes.linewidth": 0.8,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
})

BLUE = "#1f6fb2"; ORANGE = "#e08a1e"; GREEN = "#2e8b57"; GRAY = "#555555"

def fig2():
    fig, axes = plt.subplots(2, 1, figsize=(9.6, 3.8), sharex=True,
                             gridspec_kw={"height_ratios": [1, 1], "hspace": 0.55})
    rmax = 3.0
    rho1, rho2 = 2/3, 3/2
    for ax in axes:
        ax.set_xlim(0, rmax)
        ax.set_ylim(-0.5, 1.5)
        ax.axhline(0, color="k", lw=1.0)
        ax.set_yticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.axvline(rho1, color=GRAY, lw=0.9, ls=(0, (4, 3)))
        ax.axvline(rho2, color=GRAY, lw=0.9, ls=(0, (4, 3)))
        ax.text(rho1, 1.28, r"$\rho_1=\frac{2}{3}$", ha="center", fontsize=10)
        ax.text(rho2, 1.28, r"$\rho_2=\frac{3}{2}$", ha="center", fontsize=10)

    ax = axes[0]  # impossibility region: FAST [rho1, inf), SLOW [0, rho2]
    ax.barh(0.9, rmax - rho1, left=rho1, height=0.34, color=BLUE, alpha=0.85, label="FAST")
    ax.barh(0.1, rho2, left=0, height=0.34, color=ORANGE, alpha=0.85, label="SLOW")
    ax.axvspan(rho1, rho2, color=GRAY, alpha=0.18)
    ax.text((rho1+rho2)/2, 0.27, "overlap", ha="center", va="center", fontsize=9, color="k")
    ax.annotate("", xy=(rmax-0.03, 0.9), xytext=(rmax-0.8, 0.9),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.4))
    ax.set_title(r"Impossibility region $I$: every $r$ licenses a plan, none licenses a common plan",
                 fontsize=11)

    ax = axes[1]  # rescue set: STAGED licenses [0, inf)
    ax.barh(0.5, rmax, left=0, height=0.34, color=GREEN, alpha=0.85, label="STAGED")
    ax.text(rmax/2, 0.67, "STAGED (reserve-financed) serves every $r$", ha="center", fontsize=10)
    ax.set_title(r"Rescue set $R$: one plan (STAGED) is licensed at every $r$", fontsize=11)

    # single shared xlabel, on the bottom panel only, with breathing room
    axes[1].set_xlabel("weight ratio  $r = w_2 / w_1$", labelpad=10)

    handles = [
        Line2D([0], [0], color=BLUE, lw=8, label=r"FAST licensed: $r \geq \rho_1$"),
        Line2D([0], [0], color=ORANGE, lw=8, label=r"SLOW licensed: $r \leq \rho_2$"),
        Line2D([0], [0], color=GREEN, lw=8, label=r"STAGED licensed: all $r$"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout()
    fig.savefig(OUT + "fig2_weight_intervals_v35.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote fig2_weight_intervals_v35.png")

if __name__ == "__main__":
    fig2()
