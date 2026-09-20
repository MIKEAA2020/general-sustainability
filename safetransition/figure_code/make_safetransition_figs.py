#!/usr/bin/env python3
"""Figure pipeline for the SafeTransition EMS manuscript (paper 3).

Generates, from exact rational quantities (floats only in plotting):
  figs_p3/graphical_abstract.png  -- EMS graphical abstract (1328 x 531 px)
  figs_p3/fig_readings.png        -- dashboard readings figure (licensing
                                     band; rescue threshold)
Also copies the deposited benchmark figure into figs_p3/ (byte-faithful).

Deterministic; no floats in any computed quantity.
"""
from fractions import Fraction as Q
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import shutil, os

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs_p3"))
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.labelsize": 10.5, "axes.titlesize": 11,
    "xtick.labelsize": 9.5, "ytick.labelsize": 9.5, "axes.linewidth": 0.8,
})
GREEN, RED, ORANGE, GRAY, BLUE = "#2e8b57", "#c0392b", "#e08a1e", "#555555", "#1f6fb2"
LIGHTRED = "#f6d9d4"

# --------------------------------------------------------------- exact values
RHO1, RHO2 = Q(2, 3), Q(3, 2)
IDX = (Q(12, 5), Q(2, 5), Q(12, 5))          # composite index along FAST, w=(1,1)
S1A = (Q(6, 5), Q(-4, 5), Q(6, 5))           # ecological margin, adverse branch
TS = (0, Q(1, 2), 1)

# ------------------------------------------------- graphical abstract (EMS)
fig = plt.figure(figsize=(13.28, 5.31), dpi=100)
gs = fig.add_gridspec(1, 3, left=0.045, right=0.985, top=0.80, bottom=0.16, wspace=0.28)
fig.text(0.045, 0.925, "SafeTransition: exact rational certification of transition safety",
         fontsize=16, fontweight="bold", color="#1c1c1c", ha="left")
fig.text(0.045, 0.855, "Typed operators, recursions, and Farkas certificates in exact rational "
         "arithmetic \u2014 floats only in graphics", fontsize=10.5, color="#555", ha="left")

# (a) index vs floor
ax = fig.add_subplot(gs[0])
ax.axhspan(-1.4, 0, color=LIGHTRED, alpha=0.55, lw=0)
ax.axhline(0, color=GRAY, lw=0.9, ls="--")
ft = [float(t) for t in TS]
ax.plot(ft, [float(v) for v in IDX], color=GREEN, lw=2.2, marker="o", ms=4.5,
        label="composite index $w\\!\\cdot\\! s$  (min 2/5 > 0)")
ax.plot(ft, [float(v) for v in S1A], color=RED, lw=2.2, marker="s", ms=4.5,
        label="floor $s_1$  (min $-4/5$ < 0)")
ax.set_ylim(-1.4, 3.1); ax.set_xlim(-0.04, 1.04)
ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "1/2", "1"])
ax.set_xlabel("time within the review period")
ax.set_title("(a) What the index sees vs the floor", loc="left")
ax.legend(loc="upper right", fontsize=8, framealpha=0.95)

# (b) licensing band
ax = fig.add_subplot(gs[1])
top = 1.0
ax.axvspan(float(RHO1), 2.2, ymin=0.18, ymax=0.86, color=BLUE, alpha=0.12, lw=0)
ax.axvspan(0, float(RHO2), ymin=0.18, ymax=0.86, color=GREEN, alpha=0.12, lw=0)
ax.axvline(float(RHO1), color=BLUE, lw=1.6)
ax.axvline(float(RHO2), color=GREEN, lw=1.6)
ax.axvline(1.0, color=GRAY, lw=1.0, ls=":")
ax.text(float(RHO1) - 0.02, 0.93, "$\\rho_1 = 2/3$", color=BLUE, fontsize=10,
        ha="right", va="top")
ax.text(float(RHO2) + 0.02, 0.93, "$\\rho_2 = 3/2$", color=GREEN, fontsize=10,
        ha="left", va="top")
ax.text(1.36, 0.70, "FAST licensed\n($r \\geq \\rho_1$)", color=BLUE, fontsize=9, ha="center")
ax.text(0.68, 0.28, "SLOW licensed\n($r \\leq \\rho_2$)", color="#1e6e42", fontsize=9,
        ha="center")
ax.text(1.1, 0.47, "both", fontsize=8.5, color="#444", ha="center")
ax.text(1.1, 0.09, "no $r$ licenses a typed-safe plan at the witness",
        fontsize=8.3, color=RED, ha="center")
ax.set_xlim(0, 2.2); ax.set_ylim(0, 1)
ax.set_yticks([])
ax.set_xlabel("weight ratio $r = w_2/w_1$")
ax.set_title("(b) Per-weight licensing, exactly", loc="left")

# (c) certificates card
ax = fig.add_subplot(gs[2])
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
box = FancyBboxPatch((0.02, 0.06), 0.96, 0.88, boxstyle="round,pad=0.012",
                     fc="#fbfaf6", ec="#c9c4b4", lw=1.0)
ax.add_patch(box)
lines = [
    ("Farkas certificate (stacked menu window)", "#1c1c1c", 9.2, "bold"),
    ("$\\lambda = (1/2,\\, 1/2)$,  $\\lambda^{\\top}\\! A = 0$", "#1c1c1c", 10.5, "normal"),
    ("$-\\lambda^{\\top}\\! b = 1/10 > 0$, re-verified exactly", "#1c1c1c", 10.5, "normal"),
    ("", "#1c1c1c", 4, "normal"),
    ("Belief recursion: root belief in $\\mathcal{W}_1 \\setminus \\mathcal{W}_2$", "#1c1c1c", 10.2, "normal"),
    ("(post-observation recourse failure)", "#666", 9.0, "normal"),
    ("", "#1c1c1c", 4, "normal"),
    ("Benchmark: 24/24 exact checks pass", GREEN, 10.5, "bold"),
    ("$\\sigma(16/5) = 1088/125$;  $H^{*}_{max} = 1463/125$", "#1c1c1c", 10.0, "normal"),
    ("$\\kappa^{*} = 1 - x$;  witness shortfall $1/2$", "#1c1c1c", 10.0, "normal"),
]
y = 0.925
for text, color, size, weight in lines:
    if text:
        ax.text(0.06, y, text, fontsize=size, color=color, weight=weight,
                ha="left", va="top", transform=ax.transAxes)
    y -= 0.098
ax.set_title("(c) Certificates the library re-verifies", loc="left")
fig.text(0.985, 0.022, "Verification deposit: doi.org/10.6084/m9.figshare.33764023",
         fontsize=8.5, color="#666", ha="right")
ga_path = os.path.join(OUT, "graphical_abstract.png")
fig.savefig(ga_path, dpi=100, facecolor="white")
plt.close(fig)

# ------------------------------------------------------------- readings figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 3.9), dpi=300)

ax1.axvspan(float(RHO1), 2.5, color=BLUE, alpha=0.10, lw=0)
ax1.axvspan(0, float(RHO2), color=GREEN, alpha=0.10, lw=0)
ax1.axvline(float(RHO1), color=BLUE, lw=1.6)
ax1.axvline(float(RHO2), color=GREEN, lw=1.6)
ax1.axvline(1.0, color=GRAY, lw=1.0, ls=":")
ax1.text(float(RHO1) - 0.05, 0.94, "$\\rho_1 = 2/3$", color=BLUE, fontsize=10,
         ha="right", va="top")
ax1.text(float(RHO2) + 0.05, 0.94, "$\\rho_2 = 3/2$", color=GREEN, fontsize=10,
         ha="left", va="top")
ax1.text(0.30, 0.62, "only SLOW licensed\n($r < \\rho_1$)", color="#1e6e42", fontsize=9.5,
         ha="center")
ax1.text(2.05, 0.62, "only FAST licensed\n($r > \\rho_2$)", color=BLUE, fontsize=9.5,
         ha="center")
ax1.text(1.02, 0.46, "both licensed for\n$\\rho_1 \\leq r \\leq \\rho_2$", fontsize=8.8,
         color="#444", ha="center")
ax1.text(1.04, 0.27, "$w = (1,1)$:\n$r = 1$", fontsize=8.5, color="#444", ha="left")
ax1.text(1.25, 0.03, "no $r$ licenses a typed-safe plan at the witness "
         "(floors breached path-wise)", fontsize=8.6, color=RED, ha="center")
ax1.set_xlim(0, 2.5); ax1.set_ylim(0, 1); ax1.set_yticks([])
ax1.set_xlabel("weight ratio $r = w_2/w_1$")
ax1.set_title("(a) Licensing thresholds at the witness datum", loc="left")

xs = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
kappa = [max(0.0, 1.0 - x) for x in xs]     # kappa*(x) = max(0, 1 - x); plotting only
ax2.axhspan(0, 1.05, color=LIGHTRED, alpha=0.55, lw=0)
ax2.plot(xs, kappa, color="#1c1c1c", lw=2.2)
ax2.axvline(1.0, color=GRAY, lw=1.0, ls=":")
ax2.plot([0.5], [0.5], marker="o", ms=6, color=RED)
ax2.plot([1.5], [0.0], marker="o", ms=6, color=GREEN)
ax2.annotate("FP witness $(1/2,\\ 1/2)$:\nshortfall of $1/2$",
             xy=(0.5, 0.5), xytext=(0.62, 0.85), ha="center", va="center",
             fontsize=8.6, color=RED,
             arrowprops=dict(arrowstyle="->", color=RED, lw=1.0))
ax2.annotate("rescue witness $(3/2, 0)$:\n$c = 1$ financed, $1/2$ remains",
             xy=(1.5, 0.0), xytext=(1.02, 0.60), fontsize=8.6, color="#1e6e42",
             arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.0))
ax2.text(0.24, 0.30, "unfinanced region\n($\\kappa^{*} > 0$)", fontsize=8.3, color="#a03030",
         ha="center")
ax2.set_xlim(0, 2); ax2.set_ylim(0, 1.05)
ax2.set_xlabel("fund level $x$")
ax2.set_ylabel("rescue threshold $\\kappa^{*}(x) = \\max(0,\\, 1 - x)$")
ax2.set_title("(b) Rescue financing, exactly", loc="left")

fig.tight_layout()
readings_path = os.path.join(OUT, "fig_readings.png")
fig.savefig(readings_path, dpi=300, facecolor="white")
plt.close(fig)

# --------------------------------------------------- deposited benchmark figure
src = "/home/user/fig_benchmark_v44.png"
dst = os.path.join(OUT, "fig_benchmark.png")
shutil.copyfile(src, dst)

from PIL import Image
for p in (ga_path, readings_path, dst):
    im = Image.open(p)
    print(f"{os.path.basename(p)}: {im.size[0]}x{im.size[1]} px, {os.path.getsize(p)} B")
print("done")
