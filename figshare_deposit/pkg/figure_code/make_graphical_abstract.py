#!/usr/bin/env python3
"""Graphical abstract v3 for 'Aggregate Indices and Transition Safety'.
Elsevier spec: min 531 x 1328 px (h x w) or proportionally more; readable at
5 x 13 cm; preferred TIFF / EPS / PDF. Canvas aspect 2.5 : 1 (w : h).
v4: green index line moved down to hug the zero line (it must stay >= 0, so it
belongs just above the dashed zero line, not at the top of the panel).
v3: auto-fit title/footer text width (no overflow past the canvas edges).
v2: index line separated from the breach curves; reserve panel raised into the
same band as the other panels."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT = "./"

GREEN  = "#2e8b57"
RED    = "#c0392b"
ORANGE = "#e08a1e"
BLUE   = "#1f6fb2"
GRAY   = "#555555"
INK    = "#101010"
LIGHTRED   = "#f6d9d4"
LIGHTGREEN = "#d8ead2"

DPI = 508.0
FIG_W, FIG_H = 2656 / DPI, 1062 / DPI   # 13.28 cm x 5.31 cm
CANVAS_PX = 2656.0
MAX_FRAC = 0.86                          # text may span at most 86% of width

TITLE_1 = "The index approves —"
TITLE_2 = "but no plan keeps both floors safe"
FOOTER = "Convexifying the plan menu closes the gap exactly; alternating plans over time does not."

def panel(ax, title):
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title(title, fontsize=9, pad=3, color=INK)

def fit_size(fig, text, lo, hi, weight):
    """Largest fontsize in [lo, hi] whose rendered width is <= MAX_FRAC * canvas."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    best = lo
    for size in np.arange(hi, lo - 0.25, -0.25):
        t = fig.text(0.5, 0.5, text, fontsize=size, fontweight=weight)
        w = t.get_window_extent(renderer=r).width
        t.remove()
        if w <= MAX_FRAC * CANVAS_PX:
            best = size
            break
    return best

fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI)
gs = GridSpec(1, 4, left=0.020, right=0.965, bottom=0.18, top=0.62, wspace=0.26)
axes = [fig.add_subplot(gs[0, i]) for i in range(4)]

title_size = 12.0
footer_size = fit_size(fig, FOOTER, 6.0, 8.5, "normal")
print(f"title fontsize={title_size:.2f}  footer fontsize={footer_size:.2f}")

fig.text(0.5, 0.870, TITLE_1, ha="center", va="center",
         fontsize=title_size, fontweight="bold", color=INK)
fig.text(0.5, 0.805, TITLE_2, ha="center", va="center",
         fontsize=title_size, fontweight="bold", color=INK)
fig.text(0.5, 0.052, FOOTER, ha="center", va="center",
         fontsize=footer_size, style="italic", color=GRAY)

# ---- Panel 1: two binding floors ----
ax = axes[0]; panel(ax, "Two binding floors")
for y in (6.0, 2.7):
    ax.plot([0.6, 9.3], [y, y], color="k", lw=0.8, ls=(0, (3, 2)))
ax.add_patch(plt.Rectangle((1.2, 6.15), 7.6, 1.3, facecolor=GREEN, edgecolor="none", alpha=0.85))
ax.add_patch(plt.Rectangle((1.2, 2.85), 7.6, 1.3, facecolor=GREEN, edgecolor="none", alpha=0.85))
ax.text(0.35, 6.8, r"$s_1$", ha="left", va="center", fontsize=9)
ax.text(0.35, 3.5, r"$s_2$", ha="left", va="center", fontsize=9)
ax.text(9.3, 6.0, "0", ha="right", va="center", fontsize=7, color=GRAY)
ax.text(9.3, 2.7, "0", ha="right", va="center", fontsize=7, color=GRAY)
ax.text(5.0, 1.15, "each floor must hold\non its own", ha="center", va="center",
        fontsize=6.5, color=GRAY)

# ---- Panel 2: weighted index ----
ax = axes[1]; panel(ax, "Weighted index")
ax.plot([0.6, 9.3], [5.2, 5.2], color="k", lw=0.8, ls=(0, (3, 2)))
ax.add_patch(plt.Rectangle((1.2, 5.35), 7.6, 1.3, facecolor=BLUE, edgecolor="none", alpha=0.8))
ax.text(1.35, 7.05, r"$w\cdot s \,\geq\, 0$", fontsize=9)
ax.text(8.7, 8.9, "\u2713", fontsize=17, color=GREEN, fontweight="bold", ha="center")
ax.text(5.0, 3.55, "every weighting\napproves", ha="center", va="center",
        fontsize=6.5, color=GRAY)

# ---- Panel 3: no common plan (index hugs the zero line; floors plunge below) ----
ax = axes[2]; panel(ax, "No common plan")
t = np.linspace(0.8, 9.2, 300)
zero = 5.0
ax.plot([0.6, 9.3], [zero, zero], color="k", lw=0.9, ls=(0, (3, 2)))
ax.text(9.25, zero + 0.18, "0", fontsize=7, color=GRAY, ha="right")
# weighted index: always above the zero line, hugging it (true minimum ~ +0.53)
idx = 5.55 + 0.10 * np.sin(np.linspace(0, 4 * np.pi, 300))
ax.plot(t, idx, color=GREEN, lw=1.6)
ax.text(1.15, 5.72, "index  \u2265 0", fontsize=6.5, color=GREEN, ha="left")
# the two floors plunge below zero under their own plan
s1 = np.where(t <= 5, 7.4 - 1.2 * (t - 0.8), 7.4 - 1.2 * (9.2 - t))   # bottom 2.36
s2 = np.where(t <= 5, 6.6 - 1.2 * (t - 0.8), 6.6 - 1.2 * (9.2 - t))   # bottom 1.56
ax.plot(t, s1, color=RED, lw=1.5)
ax.plot(t, s2, color=ORANGE, lw=1.5)
ax.fill_between(t, s1, zero, where=s1 < zero, color=LIGHTRED, interpolate=True)
ax.fill_between(t, s2, zero, where=s2 < zero, color=LIGHTRED, interpolate=True)
ax.text(1.15, 7.55, r"$s_1$ (FAST)", fontsize=6.5, color=RED, ha="left")
ax.text(1.15, 6.85, r"$s_2$ (SLOW)", fontsize=6.5, color=ORANGE, ha="left")
ax.text(8.7, 8.9, "\u2717", fontsize=17, color=RED, fontweight="bold", ha="center")
ax.text(5.0, 0.85, "each plan breaches\none floor", ha="center", va="center",
        fontsize=6.5, color=GRAY)

# ---- Panel 4: a reserve decides (drawing raised into the same band) ----
ax = axes[3]; panel(ax, "A reserve decides")
ax.plot([1.3, 9.0], [7.2, 7.2], color=RED, lw=0.9, ls=(0, (4, 3)))
ax.text(9.0, 7.2, r"$c = 1$", fontsize=7, color=RED, va="center", ha="right")
ax.add_patch(plt.Rectangle((1.9, 5.0), 1.5, 0.5, facecolor=RED, edgecolor="none", alpha=0.85))
ax.text(2.65, 4.1, r"$x < 1$", fontsize=6.5, color=RED, ha="center")
ax.text(2.65, 6.2, "\u2717", fontsize=15, color=RED, fontweight="bold", ha="center")
ax.add_patch(plt.Rectangle((6.6, 5.0), 1.5, 2.2, facecolor=GREEN, edgecolor="none", alpha=0.85))
ax.text(7.35, 4.1, r"$x \geq 1$", fontsize=6.5, color=GREEN, fontweight="bold", ha="center")
ax.text(7.35, 7.9, "\u2713", fontsize=15, color=GREEN, fontweight="bold", ha="center")
ax.text(5.0, 0.85, "the reserve bridges\nthe gap", ha="center", va="center",
        fontsize=6.5, color=GRAY)

fig.savefig(OUT + "graphical_abstract.pdf", facecolor="white")
fig.savefig(OUT + "graphical_abstract.png", dpi=DPI, facecolor="white")
plt.close(fig)
print("wrote graphical_abstract.pdf and graphical_abstract.png (v3)")
