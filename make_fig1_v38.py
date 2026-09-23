#!/usr/bin/env python3
"""Regenerate Figure 1 (floor-margin view) for v38 with Qwen's four devices:
(1) worst-case dip arrows from the witness point crossing the zero floors,
(2) endorsement zones (which plan is licensed at weight ratio r) as an r-strip,
(3) a reserve bar beside each panel showing x against the rescue cost c=1,
(4) red (impossibility I) / green (rescue R) color coding of the triangle.
All numbers follow the witness datum: witness (s1,s2)=(6/5,6/5), dip depth 2,
rho_1 = 2/3, rho_2 = 3/2. Panels: A shows x<1, B shows x>=1."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

OUT = "/home/user/arena agent 1/paper rewrites/figs_p1/"
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10.5,
    "axes.labelsize": 11,
    "xtick.labelsize": 9.5,
    "ytick.labelsize": 9.5,
})

BLUE   = "#1f6fb2"
ORANGE = "#e08a1e"
GREEN  = "#2e8b57"
RED    = "#c0392b"
GRAY   = "#555555"
LIGHTRED   = "#f6d9d4"
LIGHTGREEN = "#d8ead2"
LIGHTGRAY  = "#ececec"

WIT = (6/5, 6/5)     # witness point in the (s1, s2) plane
RHO1, RHO2 = 2/3, 3/2

def draw_plane(ax, panel):
    ax.set_xlim(-1.05, 2.45)
    ax.set_ylim(-1.05, 2.45)
    ax.set_aspect("equal")
    ax.set_xlabel(r"$s_1$")
    ax.set_ylabel(r"$s_2$")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # zero floors
    ax.axhline(0, color="k", lw=0.9)
    ax.axvline(0, color="k", lw=0.9)

    # square [0,2]^2
    sq = plt.Rectangle((0, 0), 2, 2, fill=False, ec=GRAY, lw=0.8, ls=(0, (2, 2)))
    ax.add_patch(sq)

    # below-diagonal region (verdict is panel-dependent; see caption)
    ax.fill(np.array([0, 2, 0]), np.array([0, 0, 2]), color=LIGHTGRAY, alpha=0.9)
    ax.text(0.40, 0.40, r"$s_1 + s_2 < 2$", ha="center", va="center",
            fontsize=9, color=GRAY)

    # discrepancy triangle (Q): red = I (Panel A), green = R (Panel B)
    if panel == "A":
        fc, ec, tag = LIGHTRED, RED, r"$I$"
    else:
        fc, ec, tag = LIGHTGREEN, GREEN, r"$R$"
    tri = plt.Polygon([(0, 2), (2, 0), (2, 2)], closed=True, facecolor=fc,
                      edgecolor=ec, lw=1.6, hatch="////", alpha=0.75)
    ax.add_patch(tri)
    ax.text(1.62, 1.62, tag, fontsize=20, color=ec, ha="center", va="center",
            fontweight="bold")

    # diagonal s1 + s2 = 2
    ax.plot([0, 2], [2, 0], color="k", lw=1.2)
    ax.text(0.62, 1.30, r"$s_1 + s_2 = 2$", fontsize=9, rotation=-45,
            ha="center", va="center", color="k")

    # witness point
    ax.plot(*WIT, "ko", ms=5, zorder=5)
    ax.annotate(r"$(6/5,\,6/5)$", xy=WIT, xytext=(1.36, 1.52),
                fontsize=9.5, zorder=5)

    # outside point (annotated in Panel A only)
    if panel == "A":
        ax.plot(0.1, 0.1, marker="o", ms=4, color=GRAY, zorder=5)
        ax.annotate(r"$(1/10,\,1/10)$, $x=1/2$", xy=(0.1, 0.1),
                    xytext=(0.16, -0.72), fontsize=8.5, color=GRAY)

    # (1) dip arrows from the witness point, crossing the zero floors
    ax.fill_betweenx([1.00, 1.40], -0.85, 0.0, color=LIGHTRED, alpha=0.45, zorder=1)
    ax.fill_between([1.00, 1.40], -0.85, 0.0, color=LIGHTRED, alpha=0.45, zorder=1)
    ax.annotate("", xy=(-0.80, WIT[1]), xytext=WIT,
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.0, shrinkA=0, shrinkB=0))
    ax.annotate("", xy=(WIT[0], -0.80), xytext=WIT,
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.0, shrinkA=0, shrinkB=0))
    ax.text(0.42, 1.44, "FAST dip ($-2$)", fontsize=8.5, color=RED, ha="center")
    ax.text(1.46, 0.55, "SLOW dip ($-2$)", fontsize=8.5, color=RED, ha="left", rotation=90)

    # (3) reserve bar beside the panel
    axin = inset_axes(ax, width="16%", height="52%", loc="center right",
                      borderpad=0.2)
    axin.set_ylim(0, 1.3)
    axin.set_xlim(0, 1)
    axin.set_xticks([])
    axin.set_yticks([])
    for s in axin.spines.values():
        s.set_visible(False)
    axin.axhline(1.0, color=RED, lw=1.2, ls=(0, (4, 3)))
    axin.text(1.02, 1.0, r"$c = 1$", fontsize=8, color=RED, va="center")
    if panel == "A":
        axin.bar(0.5, 0.0, bottom=0.0, width=0.55, color=GRAY, alpha=0.7)
        axin.text(1.02, 0.0, r"$x = 0$", fontsize=8, va="center", color=GRAY)
    else:
        axin.bar(0.5, 1.0, bottom=0.0, width=0.55, color=GREEN, alpha=0.85)
        axin.text(1.02, 0.5, r"$x = 1$", fontsize=8, va="center", color=GREEN)
    axin.set_title("reserve $x$", fontsize=8, pad=2)

    ax.set_title(("Panel A:  $x < 1$  \u2192  impossibility region $I$"
                  if panel == "A" else
                  "Panel B:  $x \\geq 1$  \u2192  rescue set $R$"), fontsize=10.5)

def draw_rstrip(ax):
    """(2) endorsement zones: which plan is licensed at weight ratio r,
    at the witness point (6/5, 6/5)."""
    rmax = 3.0
    ax.set_xlim(0, rmax)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    h = 0.32
    y0 = 0.32
    # SLOW-only [0, rho1)
    ax.barh(y0, RHO1, left=0, height=h, color=ORANGE, alpha=0.85)
    # both [rho1, rho2]
    ax.barh(y0, RHO2 - RHO1, left=RHO1, height=h, color=GRAY, alpha=0.75)
    # FAST-only (rho2, rmax]
    ax.barh(y0, rmax - RHO2, left=RHO2, height=h, color=BLUE, alpha=0.85)
    ax.text(RHO1/2, y0 + h/2, "SLOW-only", ha="center", va="center", fontsize=8.5, color="k")
    ax.text((RHO1 + RHO2)/2, y0 + h/2, "both", ha="center", va="center", fontsize=8.5, color="k")
    ax.text((RHO2 + rmax)/2, y0 + h/2, "FAST-only", ha="center", va="center", fontsize=8.5, color="k")
    for rv, lab in [(RHO1, r"$\rho_1=\frac{2}{3}$"), (RHO2, r"$\rho_2=\frac{3}{2}$")]:
        ax.axvline(rv, color="k", lw=1.0, ls=(0, (4, 3)))
        ax.text(rv, y0 + h + 0.06, lab, ha="center", fontsize=9)
    ax.set_xlabel(r"weight ratio  $r = w_2 / w_1$", labelpad=6)
    ax.set_title("Endorsement zones at the witness point $(6/5, 6/5)$: "
                 "every $r$ licenses some plan, no plan is licensed by every $r$",
                 fontsize=9, style="italic")

def main():
    fig = plt.figure(figsize=(9.6, 5.6))
    gs = GridSpec(2, 2, height_ratios=[2.55, 0.72], width_ratios=[1, 1],
                  hspace=0.30, wspace=0.30)
    axA = fig.add_subplot(gs[0, 0])
    axB = fig.add_subplot(gs[0, 1])
    axR = fig.add_subplot(gs[1, :])
    draw_plane(axA, "A")
    draw_plane(axB, "B")
    draw_rstrip(axR)
    fig.savefig(OUT + "fig1_witness_v38.png", dpi=200, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print("wrote fig1_witness_v38.png")

if __name__ == "__main__":
    main()
