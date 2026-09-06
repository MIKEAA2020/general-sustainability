#!/usr/bin/env python3
"""P1 Figure 1, v22 build (owner-directed label-clearing fix).

Reproduces figs_p1/fig1_witness.png with one change class: the
"intermediate weights / license both" annotation and the "s_2 = 2" leg
label are repositioned into clear space. In the previous rendering the
"intermediate weights" text sat under the dotted rho_2 = 3 curve (the
curve passed through the words) and the rotated "s_2 = 2" label
overlapped "license both", making both unreadable.

Geometry (unchanged, from the paper's Section 4.5-4.7 contract):
  - square 0 <= s1, s2 <= 2; discrepancy region Q = the closed triangle
    (0,2), (2,0), (2,2) minus the strict legs s1 = 2 and s2 = 2;
  - solid black diagonal s1 + s2 = 2;
  - dashed gray legs s2 = 2 (top) and s1 = 2 (right);
  - dotted threshold curves rho_2 = 3 (s2 = 2 - s1/3) and
    rho_1 = 3 (s2 = (2 - s1)/3);
  - witness (6/5, 6/5) with label and leader;
  - "outside FP_0" below the rho_1 curve;
  - Panel A (x < 1, at x = 0): impossibility region I = FP_agg (red);
  - Panel B (x >= 1, at x = 1): rescue set R, STAGED-witnessed (green).

New placements:
  - "intermediate weights" / "license both": centred at (1.55, 1.02) /
    (1.55, 0.90) - inside Q, below the witness dot, above the diagonal,
    clear of the dotted curves, the leader line, and all other labels;
    the text sits inside the region it describes (the interior band
    where the threshold pair (rho_1, rho_2) brackets intermediate
    weights), so it still points at what it describes.
  - "s_2 = 2" (Panel A only, as before): horizontal, just below the
    dashed top border at s1 ~ 1.62, clear of the rho_2 = 3 curve and
    all text.
Writes: arena agent 1/paper rewrites/figs_p1/fig1_witness_v22.png
"""
from __future__ import annotations
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites/figs_p1/fig1_witness_v22.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "sans-serif", "font.size": 9, "axes.labelsize": 10,
    "xtick.labelsize": 8, "ytick.labelsize": 8, "figure.dpi": 200,
})

RED_FACE = "#ffb8b8"      # (255,184,184)
GREEN_FACE = "#b8dbb8"    # (184,219,184)
CURVE_GRAY = "#404040"    # (64,64,64) dotted threshold curves
LEG_GRAY = "#8c8c8c"      # (140,140,140) dashed legs
DIAG = "#262626"
TXT_A = (205, 120, 120)   # readable red tint for Panel A annotation
TXT_B = (120, 160, 120)   # readable green tint for Panel B annotation


def rgb(t):
    return "#%02x%02x%02x" % t


def draw_panel(ax, mode: str):
    x = np.linspace(0.0, 2.0, 400)
    # 1. shaded region Q: triangle (0,2), (2,0), (2,2)
    face = RED_FACE if mode == "A" else GREEN_FACE
    ax.fill([0, 2, 2], [2, 0, 2], color=face, zorder=0)
    # 2. solid diagonal s1 + s2 = 2
    ax.plot([0, 2], [2, 0], color=DIAG, lw=2.0, zorder=3)
    # 3. dashed strict legs s2 = 2 (top) and s1 = 2 (right)
    ax.plot([0, 2], [2, 2], color=LEG_GRAY, ls="--", lw=1.2, zorder=2)
    ax.plot([2, 2], [0, 2], color=LEG_GRAY, ls="--", lw=1.2, zorder=2)
    # 4. dotted threshold curves
    ax.plot(x, 2 - x / 3.0, color=CURVE_GRAY, ls=":", lw=1.4, zorder=2)   # rho_2 = 3
    ax.plot(x, (2 - x) / 3.0, color=CURVE_GRAY, ls=":", lw=1.4, zorder=2)  # rho_1 = 3
    # 5. curve labels
    ax.text(0.28, 1.74, r"$\rho_2 = 3$", fontsize=8.5, color=CURVE_GRAY,
            ha="left", va="center", zorder=4)
    ax.text(1.42, 0.30, r"$\rho_1 = 3$", fontsize=8.5, color=CURVE_GRAY,
            ha="center", va="center", zorder=4)
    # 6. outside FP_0
    ax.text(0.24, 0.46, "outside FP$_0$", fontsize=8, color="#595959",
            ha="center", va="center", zorder=4)
    # 7. witness dot + label + leader
    dotc = "#d32f2f" if mode == "A" else "#2e7d32"
    ax.plot([1.2], [1.2], "o", ms=7, mfc=dotc, mec="black", mew=0.8, zorder=5)
    ax.text(1.05, 1.45, "witness (6/5, 6/5)", fontsize=8.5, color="black",
            ha="center", va="center", zorder=4)
    ax.plot([1.13, 1.19], [1.39, 1.27], color="#808080", lw=0.8, zorder=4)
    # 8. repositioned annotation: inside Q's interior band, clear of curves
    tint = rgb(TXT_A) if mode == "A" else rgb(TXT_B)
    ax.text(1.55, 1.02, "intermediate weights", fontsize=8, color=tint,
            ha="center", va="center", zorder=4)
    ax.text(1.55, 0.90, "license both", fontsize=8, color=tint,
            ha="center", va="center", zorder=4)
    # 9. Panel A only: the s_2 = 2 leg label, horizontal, under the top border
    if mode == "A":
        ax.text(1.62, 1.94, "$s_2 = 2$", fontsize=8, color="#737373",
                ha="center", va="center", zorder=4)
    # axes
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0])
    ax.set_xlabel("$s_1$ (service surplus)")
    ax.set_ylabel("$s_2$ (remediation coverage)")
    title = ("Panel A: $x < 1$ — impossibility region $I = \\mathrm{FP}_{\\mathrm{agg}}$"
             if mode == "A" else
             "Panel B: $x \\geq 1$ — rescue set $R$ (STAGED-witnessed)")
    ax.set_title(title, fontsize=11)


fig, (axA, axB) = plt.subplots(1, 2, figsize=(9.6, 4.4))
draw_panel(axA, "A")
draw_panel(axB, "B")
fig.tight_layout()
fig.savefig(OUT, bbox_inches="tight")
plt.close(fig)
print("wrote", OUT)
