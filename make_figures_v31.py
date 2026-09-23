#!/usr/bin/env python3
"""Generate Figure 2 (weight-interval view) and Figure 3 (path view) for v31.
All numbers follow the witness datum: (x, s1, s2) = (1/2, 6/5, 6/5),
rho_1 = 2/3, rho_2 = 3/2, worst-case dip depth 2, gain e = (1/4, 1/4)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

OUT = "/home/user/arena agent 1/paper rewrites/figs_p1/"
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
RED = "#c0392b"; LIGHTRED = "#f6d9d4"; LIGHTGREEN = "#d8ead2"

# ---------------------------------------------------------------- Figure 2
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
        ax.set_xlabel("weight ratio  $r = w_2 / w_1$")
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

    handles = [
        Line2D([0], [0], color=BLUE, lw=8, label=r"FAST licensed: $r \geq \rho_1$"),
        Line2D([0], [0], color=ORANGE, lw=8, label=r"SLOW licensed: $r \leq \rho_2$"),
        Line2D([0], [0], color=GREEN, lw=8, label=r"STAGED licensed: all $r$"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout()
    fig.savefig(OUT + "fig2_weight_intervals_v31.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote fig2")

# ---------------------------------------------------------------- Figure 3
def fig3():
    t = np.linspace(0, 1, 400)
    s0 = 6/5
    def v(t, dip=2, floor0=s0):  # V-shaped dip of the stressed floor
        return np.where(t <= 0.5, floor0 - dip*2*t, floor0 - dip*2*(1 - t))

    def index_line(t, s_stressed, s_other, r):
        w1, w2 = 1/(1+r), r/(1+r)
        return w1 * s_stressed + w2 * s_other

    fig, axes = plt.subplots(3, 2, figsize=(9.6, 9.2))
    zero = 0.0

    # Row 1: FAST
    ax = axes[0, 0]
    ax.plot(t, v(t), color=BLUE, lw=2, label=r"$s_1(t)$")
    ax.plot(t, np.full_like(t, s0), color=ORANGE, lw=2, label=r"$s_2(t)$")
    ax.fill_between(t, v(t), zero, where=v(t) < zero, color=LIGHTRED, interpolate=True)
    ax.axhline(zero, color="k", lw=0.9, ls="--")
    ax.set_ylim(-1.0, 1.5); ax.set_xticks([]); ax.set_yticks([-0.8, 0, 1.2])
    ax.set_title("FAST: floor path", fontsize=11)
    ax = axes[0, 1]
    for r, c in [(2, "k"), (1, GRAY), (0.5, BLUE)]:
        idx = index_line(t, v(t), s0, r)
        ax.plot(t, idx, color=c, lw=1.7, label=rf"$r={r}$")
    ax.axhline(zero, color="k", lw=0.9, ls="--")
    ax.set_ylim(-0.4, 1.5); ax.set_xticks([]); ax.set_yticks([-0.2, 0, 1.2])
    ax.legend(loc="lower center", fontsize=9, ncol=3, frameon=False)
    ax.set_title("FAST: scalarized index", fontsize=11)

    # Row 2: SLOW (mirror)
    ax = axes[1, 0]
    ax.plot(t, np.full_like(t, s0), color=BLUE, lw=2, label=r"$s_1(t)$")
    ax.plot(t, v(t), color=ORANGE, lw=2, label=r"$s_2(t)$")
    ax.fill_between(t, v(t), zero, where=v(t) < zero, color=LIGHTRED, interpolate=True)
    ax.axhline(zero, color="k", lw=0.9, ls="--")
    ax.set_ylim(-1.0, 1.5); ax.set_xticks([]); ax.set_yticks([-0.8, 0, 1.2])
    ax.set_title("SLOW: floor path", fontsize=11)
    ax = axes[1, 1]
    for r, c in [(2, ORANGE), (1, GRAY), (0.5, "k")]:
        idx = index_line(t, s0, v(t), r)
        ax.plot(t, idx, color=c, lw=1.7, label=rf"$r={r}$")
    ax.axhline(zero, color="k", lw=0.9, ls="--")
    ax.set_ylim(-0.4, 1.5); ax.set_xticks([]); ax.set_yticks([-0.2, 0, 1.2])
    ax.legend(loc="lower center", fontsize=9, ncol=3, frameon=False)
    ax.set_title("SLOW: scalarized index", fontsize=11)

    # Row 3: STAGED reserve for x=1/2 (left) and x=1 (right)
    # Per the action table: x(t) = x - t (linear spend, slope -1); floors grow linearly to s+e.
    def x_path(t, x0):
        return x0 - t
    ax = axes[2, 0]
    ax.plot(t, x_path(t, 0.5), color=GREEN, lw=2, label=r"$x(t)$")
    ax.plot(t, s0 + 0.25*t, color=GRAY, lw=1.4, ls=":", label=r"floors $\to s+e$")
    ax.fill_between(t, x_path(t, 0.5), zero, where=x_path(t, 0.5) < zero, color=LIGHTRED, interpolate=True)
    ax.axhline(zero, color="k", lw=0.9, ls="--")
    ax.set_ylim(-0.8, 1.6); ax.set_xticks([]); ax.set_yticks([-0.5, 0, 1.4])
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    ax.set_title(r"STAGED at $x=\frac{1}{2}$: reserve sinks below zero", fontsize=11)
    ax = axes[2, 1]
    ax.plot(t, x_path(t, 1.0), color=GREEN, lw=2, label=r"$x(t)$")
    ax.plot(t, s0 + 0.25*t, color=GRAY, lw=1.4, ls=":", label=r"floors $\to s+e$")
    ax.fill_between(t, x_path(t, 1.0), zero, where=x_path(t, 1.0) < zero, color=LIGHTGREEN, interpolate=True)
    ax.axhline(zero, color="k", lw=0.9, ls="--")
    ax.set_ylim(-0.2, 1.6); ax.set_xticks([]); ax.set_yticks([0, 1.4])
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    ax.set_title(r"STAGED at $x=1$: reserve stays nonnegative", fontsize=11)

    for a in axes.flat:
        a.set_xlabel("time $t$", fontsize=9)
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT + "fig3_path_view_v31.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote fig3")

if __name__ == "__main__":
    fig2()
    fig3()
