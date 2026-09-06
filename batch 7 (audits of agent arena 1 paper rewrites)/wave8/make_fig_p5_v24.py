#!/usr/bin/env python3
"""P5 Figure 1, v24 build (owner-directed title-width fix).

Reproduces figs_p5/fig1_crossing_record.png with two changes:
  1. The title. The previous rendering carried one full-width title line
     ("...ing record of the logistic hold map — green stable, red
     unstable; diamond: complex unit-circle pair, triangle: r...") that
     spanned the entire 1839-px image width and was clipped at BOTH
     edges. The new figure carries a compact centred title
     ("Crossing record of the logistic hold map") and moves the
     colour/marker legend into a compact four-entry legend row under
     the title, well inside the figure width.
  2. The row labels use the paper's own channel vocabulary. The
     previous rendering labelled the extractive rows "Mobilising";
     the paper's text and Figure 1 caption use "extractive" (the
     companion delay study uses "mobilising"). The rows now read
     "Extractive, ..." and "Protective, ...", matching the caption's
     "forward-Euler and exact updates on the extractive and protective
     channels".

Data (unchanged, the registered crossing record of Section 3.3):
  Protective, exact held-assessment: stable [0.2, 200], no crossings.
  Protective, Euler update:          stable [0.2, 2.306], unstable
                                    [2.306, 200]; real -1 at 2.306 yr.
  Extractive, exact held-assessment: unstable [0.2, 6.501], stable
                                    [6.501, 200]; complex pair at 6.501 yr.
  Extractive, Euler update:          unstable [0.2, 47.536], stable
                                    [47.536, 79.143], unstable
                                    [79.143, 200]; complex pair at
                                    47.536 yr, real -1 at 79.143 yr.
Writes: arena agent 1/paper rewrites/figs_p5/fig1_crossing_record_v24.png
"""
from __future__ import annotations
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites/figs_p5/fig1_crossing_record_v24.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "sans-serif", "font.size": 9, "axes.labelsize": 10,
    "xtick.labelsize": 8, "ytick.labelsize": 8, "figure.dpi": 200,
})

GREEN = "#4d9051"   # (77,144,81)
RED = "#ce4848"     # (206,72,72)

ROWS = [
    # (y, label, segments [(x0, x1, colour)], markers [(x, kind, value)])
    (3, "Protective, exact held-assessment",
     [(0.2, 200.0, GREEN)], []),
    (2, "Protective, Euler update",
     [(0.2, 2.306, GREEN), (2.306, 200.0, RED)],
     [(2.306, "tri", "2.306")]),
    (1, "Extractive, exact held-assessment",
     [(0.2, 6.501, RED), (6.501, 200.0, GREEN)],
     [(6.501, "dia", "6.501")]),
    (0, "Extractive, Euler update",
     [(0.2, 47.536, RED), (47.536, 79.143, GREEN), (79.143, 200.0, RED)],
     [(47.536, "dia", "47.536"), (79.143, "tri", "79.143")]),
]

fig, ax = plt.subplots(figsize=(9.2, 4.6))
BARH = 0.56
for y, label, segs, marks in ROWS:
    for (x0, x1, c) in segs:
        ax.barh(y, x1 - x0, left=x0, height=BARH, color=c,
                edgecolor="none", zorder=2, linewidth=0)
    ax.text(0.205, y, label, fontsize=8.5, color="black",
            ha="left", va="center", zorder=4)
    for (x, kind, val) in marks:
        if kind == "dia":
            ax.plot([x], [y], "D", ms=8, mfc="white", mec="black",
                    mew=1.0, zorder=5)
        else:
            ax.plot([x], [y], "v", ms=8, mfc="white", mec="black",
                    mew=1.0, zorder=5)
        ax.text(x, y + 0.48, val, fontsize=8, color="black",
                ha="center", va="bottom", zorder=4)

ax.set_xscale("log")
ax.set_xlim(0.2, 200)
ax.set_ylim(-0.55, 3.62)
ax.set_yticks([])
ax.set_xticks([0.2, 1, 10, 100, 200])
ax.set_xticklabels(["0.2", "1", "10", "100", "200"])
ax.set_xlabel("review interval $T_r$ (yr, log scale)")
ax.set_title("Crossing record of the logistic hold map", fontsize=11)

legend_handles = [
    Patch(facecolor=GREEN, edgecolor="none", label="stable"),
    Patch(facecolor=RED, edgecolor="none", label="unstable"),
    Line2D([0], [0], marker="D", ms=7, mfc="white", mec="black",
           ls="none", label="complex unit-circle pair"),
    Line2D([0], [0], marker="v", ms=7, mfc="white", mec="black",
           ls="none", label="real $-1$ multiplier"),
]
ax.legend(handles=legend_handles, ncol=4, loc="lower center",
          bbox_to_anchor=(0.5, 1.01), frameon=False, fontsize=8,
          handlelength=1.2, columnspacing=1.4)

fig.tight_layout()
fig.savefig(OUT, bbox_inches="tight")
plt.close(fig)
print("wrote", OUT)
