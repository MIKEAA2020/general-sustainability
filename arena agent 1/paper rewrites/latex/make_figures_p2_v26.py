#!/usr/bin/env python3
"""Paper 2 (v26) figure label-placement fixes for three figures.

Fixes, per user report:
  - timing (Fig 2): "information arrives too late" overlapped the red
    dashed line -> moved down into the shaded band, clear of the line.
  - obstruction tree (Fig 6): the theta and "defeats" labels sat on the
    connecting edges -> moved into the outer whitespace beside each edge.
  - certainty-equivalence trap (Fig 4): the u=g(hat S), hat S=S+b label
    crossed the red dashed line -> moved left, stacked in the wedge between
    the red trajectory and S*, close to the red line.

Style matches the existing figs_p2 set (matplotlib, 300 dpi, palette
#2e7d32 / #c62828 / #1565c0, mathtext labels, no theorem numbers in PNG).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

OUT = "arena agent 1/paper rewrites/latex/figs_p2"
os.makedirs(OUT, exist_ok=True)

GREEN = "#2e7d32"
RED = "#c62828"
BLUE = "#1565c0"
EDGE = "#1a1a1a"

# ---------------- Fig 2: delayed information (label moved down) ---------
fig, ax = plt.subplots(figsize=(5.2, 3.0), dpi=300)
q0, eps, Tobs = 1.0, 0.25, 6.0
tstar = q0 / eps
ax.plot([0, tstar], [q0 - eps * 0, q0 - eps * tstar], color=GREEN, lw=2,
        label=r"$q(t)=q_0-\varepsilon t$")
ax.plot([tstar, Tobs], [0, -eps * (Tobs - tstar)], color=RED, lw=2, ls=(0, (4, 3)))
ax.axhline(0, color="black", lw=1)
ax.axvline(tstar, color=GREEN, ls=(0, (5, 4)), lw=1)
ax.axvline(Tobs, color=BLUE, ls=(0, (5, 4)), lw=1.4)
ax.fill_betweenx([-1.2, 0], tstar, Tobs, color=RED, alpha=0.12)
ax.annotate(r"$t^*=q_0/\varepsilon$", (tstar, 0), textcoords="offset points",
            xytext=(-58, 8), fontsize=9, color=GREEN)
ax.annotate(r"$T_{\mathrm{obs}}$", (Tobs, 0), textcoords="offset points",
            xytext=(4, 8), fontsize=9, color=BLUE)
# moved down and centered inside the shaded band, clear of the dashed line
ax.annotate("information arrives\ntoo late", (5.0, -0.85), ha="center",
            fontsize=8.5, color=RED)
ax.set_xlim(-0.4, 7.6)
ax.set_ylim(-1.15, 1.15)
ax.set_xlabel(r"time $t$", fontsize=9)
ax.set_ylabel(r"constraint margin $q$", fontsize=9)
ax.set_xticks([0, tstar, Tobs])
ax.set_xticklabels(["0", r"$t^*$", r"$T_{\mathrm{obs}}$"])
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(f"{OUT}/fig_p2_timing.png", dpi=300)
plt.close(fig)

# ---------------- Fig 4: certainty-equivalence trap (label moved left) --
fig, ax = plt.subplots(figsize=(4.6, 3.4), dpi=300)
Smin, Sstar, S0, c = 0.0, 1.0, 0.5, 0.25
tstar = (Sstar - S0) / c
ax.axhspan(Smin, Sstar, color=GREEN, alpha=0.18)
ax.axhline(Smin, color=GREEN, lw=1.0)
ax.axhline(Sstar, color="black", ls=(0, (5, 4)), lw=1.4)
ax.annotate(r"$S^*$ (upper floor)", (5.3, Sstar), textcoords="offset points",
            xytext=(-64, 4), fontsize=9)
ax.annotate(r"$S_{\min}$", (5.3, Smin), textcoords="offset points",
            xytext=(-46, -12), fontsize=9)
ax.plot([0, 5], [S0, S0], color=GREEN, lw=2.0, label=r"$u=g(S)$ (perfect feedback)")
ax.plot([0, tstar], [S0, Sstar], color=RED, lw=2.0)
ax.plot([tstar, 5], [Sstar, Sstar + c * (5 - tstar)], color=RED, lw=2.0, ls=(0, (4, 3)))
ax.plot([tstar], [Sstar], "o", color=RED, ms=7, mec="black", zorder=5)
# label moved left into the wedge between the red trajectory and S*, clear of it
ax.annotate(r"$u=g(\hat S)$", (1.15, 0.93), fontsize=9, color=RED, ha="center")
ax.annotate(r"$\hat S=S+b$", (1.15, 0.855), fontsize=9, color=RED, ha="center")
ax.annotate(r"$u=g(\hat S-b)$ recovers $g(S)$", (3.2, S0 - 0.10), fontsize=8,
            color=GREEN)
ax.set_xlim(0, 5.4)
ax.set_ylim(-0.15, 1.55)
ax.set_xlabel(r"time $t$", fontsize=9)
ax.set_ylabel(r"stock $S$", fontsize=9)
ax.set_xticks([0, tstar])
ax.set_xticklabels(["0", r"$t^*$"])
ax.set_yticks([Smin, Sstar])
ax.set_yticklabels([r"$S_{\min}$", r"$S^*$"])
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(loc="upper left", fontsize=8, frameon=False)
fig.tight_layout()
fig.savefig(f"{OUT}/fig_p2_ce_trap.png", dpi=300)
plt.close(fig)

# ---------------- Fig 6: one-step obstruction tree (labels to the side) -
fig, ax = plt.subplots(figsize=(6.0, 3.6), dpi=300)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

root = FancyBboxPatch((0.28, 0.70), 0.44, 0.20,
                      boxstyle="round,pad=0.006,rounding_size=0.03",
                      linewidth=1.3, edgecolor=EDGE, facecolor="white")
ax.add_patch(root)
ax.text(0.50, 0.84, r"belief $B_0=\{(0,-1),(0,+1)\}$", ha="center",
        va="center", fontsize=10)
ax.text(0.50, 0.76, r"$(B_0,1),\ \ U^B(B_0)=\{-1,+1\}$", ha="center",
        va="center", fontsize=8.6, color="gray")

# connecting edges
ax.plot([0.44, 0.20], [0.70, 0.28], color=EDGE, lw=1.2)
ax.plot([0.56, 0.80], [0.70, 0.28], color=EDGE, lw=1.2)

# violation nodes
for cx in (0.18, 0.82):
    ax.add_patch(FancyBboxPatch((cx - 0.10, 0.10), 0.20, 0.18,
                                boxstyle="round,pad=0.006,rounding_size=0.03",
                                linewidth=1.3, edgecolor=RED,
                                facecolor=RED, alpha=0.12))
    ax.text(cx, 0.22, r"violation", ha="center", va="center", fontsize=9.5,
            color=RED)
    ax.text(cx, 0.15, r"$z^+ = -1$", ha="center", va="center", fontsize=9.5,
            color=RED)

# labels moved into the outer whitespace beside each edge
ax.text(0.08, 0.56, r"$\theta=-1$", ha="left", va="center", fontsize=9.5,
        color=BLUE)
ax.text(0.08, 0.47, "(defeats $u=+1$)", ha="left", va="center", fontsize=7.6,
        color="gray")
ax.text(0.92, 0.56, r"$\theta=+1$", ha="right", va="center", fontsize=9.5,
        color=BLUE)
ax.text(0.92, 0.47, "(defeats $u=-1$)", ha="right", va="center", fontsize=7.6,
        color="gray")

fig.tight_layout()
fig.savefig(f"{OUT}/fig_p2_obstruction_tree.png", dpi=300)
plt.close(fig)

print("figures written to", OUT)
for f in ("fig_p2_timing.png", "fig_p2_ce_trap.png", "fig_p2_obstruction_tree.png"):
    p = os.path.join(OUT, f)
    print("  ", f, os.path.getsize(p), "bytes")
