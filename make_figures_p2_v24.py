#!/usr/bin/env python3
"""Paper 2 (v24) figures: the obstruction ladder and the one-step
obstruction tree. Matches the existing figs_p2 style: matplotlib, 300 dpi,
palette #2e7d32 (green) / #c62828 (red) / #1565c0 (blue), mathtext labels,
no theorem numbers inside the PNG (numbers live in the LaTeX captions).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

OUT = "arena agent 1/paper rewrites/latex/figs_p2"
os.makedirs(OUT, exist_ok=True)

GREEN = "#2e7d32"
RED = "#c62828"
BLUE = "#1565c0"
EDGE = "#1a1a1a"


def rung(ax, x0, x1, y0, y1, sym, name, cert, name_color="black"):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                boxstyle="round,pad=0.004,rounding_size=0.02",
                                linewidth=1.2, edgecolor=EDGE,
                                facecolor=GREEN, alpha=0.10))
    ax.text((x0 + x1) / 2, (y0 + y1) / 2, sym, ha="center", va="center",
            fontsize=11)
    # leader to right annotation
    ax.plot([x1, 0.70], [(y0 + y1) / 2, (y0 + y1) / 2],
            color=EDGE, lw=0.7, ls=(0, (2, 2)))
    ax.text(0.72, (y0 + y1) / 2, f"{name}\n{cert}",
            ha="left", va="center", fontsize=8.2, color=name_color)


# ---------------- Fig 5: obstruction ladder ----------------
fig, ax = plt.subplots(figsize=(6.6, 4.4), dpi=300)
ax.set_xlim(-0.34, 1.62)
ax.set_ylim(-0.75, 4.35)
ax.axis("off")

# rungs, decreasing width (nesting  A_N \subseteq A_tube \subseteq R^B_V \subseteq U^B )
rung(ax, 0.02, 0.62, 3.55, 4.20, r"$U^B(B)$",
     "common admissible actions",
     "admissibility obstruction:\nepistemic emptiness by admissibility")
rung(ax, 0.09, 0.55, 2.75, 3.40, r"$\mathcal{R}_{\mathcal{V}}^B(B)$",
     "common safe actions",
     "common-action obstruction\n(safety case)")
rung(ax, 0.16, 0.48, 1.95, 2.60, r"$\mathcal{A}_{\mathrm{tube}}(B,\Delta)$",
     "tube-safe actions",
     "tube obstruction, every\nreview length (uniform margin)")
rung(ax, 0.23, 0.41, 1.15, 1.80, r"$\mathcal{A}_N(B)$",
     "recursive witness actions",
     "recursive obstruction:\nexact on finite horizon")

# emptiness-descends arrow along the left edge of the stack
ar = FancyArrowPatch((0.06, 3.30), (0.06, 1.15),
                     arrowstyle="-|>", mutation_scale=14,
                     color=RED, lw=1.4)
ax.add_patch(ar)
ax.text(-0.15, 2.22, "emptiness\ndescends", rotation=90, ha="center",
        va="center", fontsize=8, color=RED)
ax.text(0.32, -0.28, "emptiness of any rung certifies\n$B\\notin\\mathrm{ERViab}_{\\mathcal{I}}(\\mathcal{V})$",
        ha="center", va="top", fontsize=8.4, color=RED)

# exit certificate below the ladder
ax.add_patch(FancyBboxPatch((0.02, -0.02), 0.60, 0.60,
                            boxstyle="round,pad=0.004,rounding_size=0.02",
                            linewidth=1.2, edgecolor=BLUE,
                            facecolor=BLUE, alpha=0.08))
ax.text(0.32, 0.28, "finite-time exit certificate:\nsits below the ladder",
        ha="center", va="center", fontsize=8.6, color=BLUE)
ax.plot([0.32, 0.32], [0.58, 1.15], color=BLUE, lw=0.8, ls=(0, (2, 2)))
ax.text(0.72, 0.28,
        "defeats every control under\nfull information — no\nobservation argument needed",
        ha="left", va="center", fontsize=8.2)

fig.tight_layout()
fig.savefig(f"{OUT}/fig_p2_ladder.png", dpi=300)
plt.close(fig)

# ---------------- Fig 6: one-step obstruction tree ----------------
fig, ax = plt.subplots(figsize=(5.4, 3.4), dpi=300)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# root
root = FancyBboxPatch((0.24, 0.72), 0.52, 0.20,
                      boxstyle="round,pad=0.006,rounding_size=0.03",
                      linewidth=1.3, edgecolor=EDGE, facecolor="white")
ax.add_patch(root)
ax.text(0.50, 0.86, r"belief $B_0=\{(0,-1),(0,+1)\}$", ha="center",
        va="center", fontsize=10)
ax.text(0.50, 0.78, r"$(B_0,1),\ \ U^B(B_0)=\{-1,+1\}$", ha="center",
        va="center", fontsize=8.6, color="gray")

# edges to violations
ax.plot([0.42, 0.26], [0.72, 0.36], color=EDGE, lw=1.2)
ax.plot([0.58, 0.74], [0.72, 0.36], color=EDGE, lw=1.2)
ax.text(0.30, 0.55, r"$\theta=-1$", ha="center", va="center", fontsize=9.5,
        color=BLUE)
ax.text(0.34, 0.48, "(defeats $u=+1$)", ha="center", va="center",
        fontsize=7.6, color="gray")
ax.text(0.70, 0.55, r"$\theta=+1$", ha="center", va="center", fontsize=9.5,
        color=BLUE)
ax.text(0.66, 0.48, "(defeats $u=-1$)", ha="center", va="center",
        fontsize=7.6, color="gray")

# violation nodes
for cx in (0.24, 0.76):
    ax.add_patch(FancyBboxPatch((cx - 0.10, 0.18), 0.20, 0.18,
                                boxstyle="round,pad=0.006,rounding_size=0.03",
                                linewidth=1.3, edgecolor=RED,
                                facecolor=RED, alpha=0.12))
    ax.text(cx, 0.30, r"violation", ha="center", va="center", fontsize=9.5,
            color=RED)
    ax.text(cx, 0.225, r"$z^+ = -1$", ha="center", va="center", fontsize=9.5,
            color=RED)

fig.tight_layout()
fig.savefig(f"{OUT}/fig_p2_obstruction_tree.png", dpi=300)
plt.close(fig)

print("figures written to", OUT)
for f in ("fig_p2_ladder.png", "fig_p2_obstruction_tree.png"):
    p = os.path.join(OUT, f)
    print("  ", f, os.path.getsize(p), "bytes")
