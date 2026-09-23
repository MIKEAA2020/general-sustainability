#!/usr/bin/env python3
"""Regenerate Figure 1 (floor-margin view) for v40.
Fixes vs v38:
- "FAST dip (-2)" and "SLOW dip (-2)" labels moved OUT of the plotted region
  into the whitespace next to the arrow each one describes.
- The reserve gauge is no longer an inset drawn over the panel; it is a
  separate axes to the right of each floor plane, so it hides nothing.
All numbers follow the witness datum: witness (s1,s2)=(6/5,6/5), dip depth 2,
rho_1 = 2/3, rho_2 = 3/2. Panels: A shows x<1, B shows x>=1."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

OUT = "/home/user/arena agent 1/paper rewrites/figs_p1/"
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10.5,
    "axes.labelsize": 11,
})

GREEN  = "#2e8b57"
RED    = "#c0392b"
ORANGE = "#e08a1e"
BLUE   = "#1f6fb2"
GRAY   = "#555555"
LIGHTRED   = "#f6d9d4"
LIGHTGREEN = "#d8ead2"
LIGHTGRAY  = "#ececec"

WIT = (6/5, 6/5)
RHO1, RHO2 = 2/3, 3/2

XL, XR, YB, YT = -1.35, 2.45, -1.35, 2.45   # expanded for labels in whitespace

def draw_plane(ax, panel):
    ax.set_xlim(XL, XR); ax.set_ylim(YB, YT)
    ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # axis labels (manual, in whitespace)
    ax.text(1.0, -1.28, r"$s_1$", ha="center", va="center", fontsize=11)
    ax.text(-1.30, 1.0, r"$s_2$", ha="center", va="center", fontsize=11, rotation=90)

    # zero floors
    ax.axhline(0, color="k", lw=0.9)
    ax.axvline(0, color="k", lw=0.9)

    # square [0,2]^2
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, ec=GRAY, lw=0.8, ls=(0, (2, 2))))

    # below-diagonal region (verdict is panel-dependent; see caption)
    ax.fill(np.array([0, 2, 0]), np.array([0, 0, 2]), color=LIGHTGRAY, alpha=0.9)
    ax.text(0.42, 0.42, r"$s_1 + s_2 < 2$", ha="center", va="center",
            fontsize=9, color=GRAY)

    # discrepancy triangle (Q): red = I (Panel A), green = R (Panel B)
    if panel == "A":
        fc, ec, tag = LIGHTRED, RED, r"$I$"
    else:
        fc, ec, tag = LIGHTGREEN, GREEN, r"$R$"
    ax.add_patch(Polygon([(0, 2), (2, 0), (2, 2)], closed=True, facecolor=fc,
                         edgecolor=ec, lw=1.6, hatch="////", alpha=0.75))
    ax.text(1.58, 1.70, tag, fontsize=20, color=ec, ha="center", va="center",
            fontweight="bold")

    # diagonal s1 + s2 = 2 (label ON the line)
    ax.plot([0, 2], [2, 0], color="k", lw=1.2)
    ax.text(0.55, 1.45, r"$s_1 + s_2 = 2$", fontsize=9, rotation=-45,
            ha="center", va="center", color="k")

    # witness point + annotation (below-right of the point)
    ax.plot(*WIT, "ko", ms=5, zorder=5)
    ax.annotate(r"$(6/5,\,6/5)$", xy=WIT, xytext=(1.38, 1.02),
                fontsize=9.5, zorder=5)

    # outside point (Panel A only), annotated in whitespace with a connector
    if panel == "A":
        ax.plot(0.1, 0.1, marker="o", ms=4, color=GRAY, zorder=5)
        ax.annotate(r"$(1/10,\,1/10)$, $x=1/2$", xy=(0.1, 0.1), xytext=(0.14, -0.62),
                    fontsize=8.5, color=GRAY,
                    arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.7))

    # (1) dip arrows from the witness point, crossing the zero floors
    ax.fill_betweenx([1.00, 1.40], -0.85, 0.0, color=LIGHTRED, alpha=0.45, zorder=1)
    ax.fill_between([1.00, 1.40], -0.85, 0.0, color=LIGHTRED, alpha=0.45, zorder=1)
    ax.annotate("", xy=(-0.80, WIT[1]), xytext=WIT,
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.0))
    ax.annotate("", xy=(WIT[0], -0.80), xytext=WIT,
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.0))

    # labels in whitespace next to their arrows
    ax.text(-0.62, 1.52, "FAST dip ($-2$)", fontsize=9, color=RED, ha="center")
    ax.text(1.20, -1.12, "SLOW dip ($-2$)", fontsize=9, color=RED, ha="center")

    ax.set_title(("Panel A:  $x < 1$  \u2192  impossibility region $I$"
                  if panel == "A" else
                  "Panel B:  $x \geq 1$  \u2192  rescue set $R$"), fontsize=10.5)

def draw_bar(ax, panel):
    """Separate reserve gauge: never overlaps the floor plane."""
    ax.set_xlim(0, 1); ax.set_ylim(-0.35, 1.45); ax.axis("off")
    ax.text(0.35, 1.38, "reserve $x$", ha="center", va="center", fontsize=7.5, color=GRAY)
    # baseline
    ax.plot([0.35, 0.35], [-0.15, 1.25], color="#999999", lw=1.0)
    # threshold c = 1
    ax.plot([0.12, 0.92], [1.0, 1.0], color=RED, lw=1.1, ls=(0, (4, 3)))
    ax.text(0.62, 1.08, r"$c=1$", fontsize=7.5, color=RED, ha="center")
    if panel == "A":
        ax.plot([0.35], [0.0], marker="o", ms=4.5, color=RED, zorder=5)
        ax.text(0.35, -0.25, r"$x=0$", fontsize=8, ha="center", color=GRAY)
    else:
        ax.add_patch(Rectangle((0.20, 0.0), 0.30, 1.0, facecolor=GREEN, alpha=0.85))
        ax.text(0.35, -0.25, r"$x=1$", fontsize=8, ha="center", color=GREEN)

def draw_rstrip(ax):
    """Endorsement zones: which plan is licensed at weight ratio r,
    at the witness point (6/5, 6/5)."""
    rmax = 3.0
    ax.set_xlim(0, rmax); ax.set_ylim(0, 1)
    ax.set_yticks([])
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    h = 0.32; y0 = 0.34
    ax.barh(y0, RHO1, left=0, height=h, color=ORANGE, alpha=0.85)
    ax.barh(y0, RHO2 - RHO1, left=RHO1, height=h, color=GRAY, alpha=0.75)
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
    fig = plt.figure(figsize=(11.0, 6.2))
    # manual rects: planes, side gauges, and bottom strip never overlap
    axA = fig.add_axes([0.030, 0.28, 0.400, 0.64])
    barA = fig.add_axes([0.443, 0.47, 0.030, 0.26])
    axB = fig.add_axes([0.535, 0.28, 0.400, 0.64])
    barB = fig.add_axes([0.948, 0.47, 0.030, 0.26])
    axR = fig.add_axes([0.030, 0.045, 0.945, 0.16])
    draw_plane(axA, "A")
    draw_plane(axB, "B")
    draw_bar(barA, "A")
    draw_bar(barB, "B")
    draw_rstrip(axR)
    fig.savefig(OUT + "fig1_witness_v40.png", dpi=200, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print("wrote fig1_witness_v40.png")

if __name__ == "__main__":
    main()
