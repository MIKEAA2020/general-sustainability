#!/usr/bin/env python3
"""Graphical abstract for the Northern cod intervention paper.

Built entirely from the archived result files, so it cannot drift from the
manuscript: every number plotted is read from results_ident_v3/ or
results_cadence_v3/ and then asserted against the value the paper prints. The
sidecar JSON records what was plotted; v29_battery.py re-derives it.

Three panels, one glance each:
  A  K is not identified from above; the bound is.
  B  The certified horizon is 6/6/7 years for every admissible catch.
  C  A year of the decision clock costs more than any catch cut tested.
"""
import csv
import io
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as _np
from matplotlib.ticker import FuncFormatter

ROOT = "/home/user/repo/wave_e_cod/src"
IDENT = os.path.join(ROOT, "results_ident_v3")
CAD = os.path.join(ROOT, "results_cadence_v3")
OUT_PNG = "/home/user/fam/e2/graphical_abstract_e2.png"
OUT_JSON = "/home/user/fam/e2/graphical_abstract_e2_data.json"

INK = "#1b1f23"
MUTED = "#6b7178"
GRID = "#d8dce0"
BLUE = "#2b5f8a"
ORANGE = "#c1652b"
GREEN = "#4a7c59"
GREY = "#9aa0a6"

# ---------------------------------------------------------------- read archive
prof = list(csv.DictReader(open(os.path.join(IDENT, "e2_profile_K.csv"))))
prof_K = [float(r["K"]) for r in prof]
prof_sse = [float(r["sse"]) for r in prof]
prof_C = [float(r["Cstar"]) for r in prof]
n = 24
cut = min(prof_sse) * (1.0 + 4.3009 / (n - 2))
inset = [i for i, s in enumerate(prof_sse) if s <= cut]
C_lo, C_hi = min(prof_C[i] for i in inset), max(prof_C[i] for i in inset)

cad_rows = list(csv.DictReader(open(os.path.join(CAD, "e2_cadence_v3.csv"))))
horizon = {}
for r in cad_rows:
    q = r["quantity"]
    if q.startswith("T*|C=") and "|" in q[3:]:
        c = float(q.split("|")[1][2:])
        lab = q.rsplit("|", 1)[1]
        horizon.setdefault(c, {})[lab] = int(r["value"])
catches = sorted(horizon)

facts = {r["quantity"]: r["value"] for r in cad_rows}
r_T = [float(x) for x in facts["erosion margin r_T, T = 1..7 (kt)"].split(",")]
inc = [float(x) for x in
       facts["year-on-year increment of r_T (kt)"].split(",")]
cad = json.load(open(os.path.join(CAD, "e2_cadence_v3.json")))
Fp = cad["Fprime_Kstar"]
Cstar, Cvac, eps = (cad["C_star_schaefer"], cad["C_vac_schaefer"], cad["eps"])

# ------------------------------------------------- assert against the paper
# the values the manuscript prints, so a re-run that changes the archive is loud
assert abs(C_lo - 67.90) < 0.01 and abs(C_hi - 95.19) < 0.01, (C_lo, C_hi)
# the minimum is ON the grid edge, not in the interior: that is why there is no
# upper confidence limit on K. Panel 1 must show a monotone decline, so assert it.
assert min(prof_sse) == prof_sse[-1] and max(prof_K) == prof_K[-1], "SSE min on edge"
assert all(prof_sse[i] >= prof_sse[i + 1] - 1e-9 for i in range(len(prof_sse) - 1)), \
    "SSE not monotone in K"
assert 32.0 < max(prof_K) / min(K for K, s in zip(prof_K, prof_sse) if s <= cut) < 34.0
assert r_T == [329, 708, 1146, 1650, 2232, 2902, 3675], r_T
assert inc == [379, 437, 504, 582, 671, 773], inc
assert all(horizon[c]["worst"] == 6 for c in catches if c <= 150.0), "worst"
assert all(horizon[c]["q05"] == 6 for c in catches if c <= 180.0), "q05"
assert all(horizon[c]["q10"] == 7 for c in catches if c <= 150.0), "q10"
assert abs(Fp - 1.1530555) < 1e-6 and abs(Cstar - 91.594) < 1e-3

# ------------------------------------------------------------------- canvas
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "axes.edgecolor": MUTED, "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": MUTED, "ytick.color": MUTED, "axes.linewidth": 0.9,
})
fig = plt.figure(figsize=(14.4, 8.2), facecolor="white")
fig.text(0.045, 0.968, "The decision clock: a viability certificate for Northern cod",
         fontsize=23, fontweight="bold", color=INK, va="top")
fig.text(0.045, 0.922,
         "Carrying capacity is not identified from above \u2014 but the viable-catch bound is, "
         "and the horizon over\nwhich it can be certified is 6\u20137 years for every admissible catch. "
         "No tested policy lengthens it.",
         fontsize=13, color=MUTED, va="top", linespacing=1.4)

gs = fig.add_gridspec(1, 3, left=0.045, right=0.975, top=0.772,
                      bottom=0.150, wspace=0.30)


def panel_head(ax, tag, title, sub):
    ax.set_title("")
    fig.text(ax.get_position().x0, 0.828, tag, fontsize=11.5,
             fontweight="bold", color="white", ha="left", va="center",
             bbox=dict(fc=BLUE, ec="none", pad=4.5))
    fig.text(ax.get_position().x0 + 0.052, 0.828, title, fontsize=15,
             fontweight="bold", color=INK, ha="left", va="center")
    fig.text(ax.get_position().x0, 0.798, sub, fontsize=11.5, color=MUTED,
             ha="left", va="center", style="italic")


# ------------------------------------------------- A: identification
ax = fig.add_subplot(gs[0, 0])
panel_head(ax, " 1 ", "K has no upper limit.",
           "Profile fit over carrying capacity, 24 transitions")
ax.plot(prof_K, prof_sse, color=BLUE, lw=2.4)
ax.axhline(cut, color=ORANGE, ls=(0, (6, 3)), lw=1.6)
ax.axvline(max(prof_K), color=INK, ls=(0, (2, 2)), lw=1.2, alpha=0.55)
ax.text(max(prof_K) * 0.97, ax.get_ylim()[1] * 0.86, "grid edge \u2014\nthe fit is\nstill improving",
        color=INK, fontsize=9.5, ha="right", va="top", alpha=0.8)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("carrying capacity  K  (kt, log)", fontsize=11.5, labelpad=4)
ax.set_ylabel("residual sum of squares (log)", fontsize=11.5, labelpad=2)
ax.set_ylim(min(prof_sse) * 0.93, max(prof_sse) * 1.25)
_f = ((_np.log(cut) - _np.log(ax.get_ylim()[0]))
      / (_np.log(ax.get_ylim()[1]) - _np.log(ax.get_ylim()[0])))
ax.text(0.97, _f + 0.035, "95% profile cut", color=ORANGE, fontsize=10.5,
        ha="right", transform=ax.transAxes, va="bottom")
ax.text(0.5, 0.075, "the fit improves to the edge of the grid\n"
                    "K is not identified from above\n"
                    "\u2014 a 33-fold range",
        transform=ax.transAxes, fontsize=10.5, color=INK, ha="center",
        va="baseline", linespacing=1.35,
        bbox=dict(fc="white", ec=GRID, pad=5, alpha=0.95))
ax2 = ax.twinx()
ax2.set_ylim(ax.get_ylim())
ax2.set_yscale("log")
ax2.set_yticks([])
axc = ax.inset_axes([0.10, 0.60, 0.80, 0.30], facecolor="#f7f8f9")
axc.plot([p[0] for p in zip(prof_K, prof_sse) if p[1] <= cut],
         [c for c, s in zip(prof_C, prof_sse) if s <= cut], color=GREEN, lw=2.2)
axc.set_xscale("log")
axc.axhspan(C_lo, C_hi, color=GREEN, alpha=0.13)
axc.set_ylim(0, 110)
axc.set_xlim(1500, 50000)
axc.tick_params(labelsize=8.5)
axc.set_xticks([1500, 5000, 15000, 50000])
axc.set_xticklabels(["1.5k", "5k", "15k", "50k"])
axc.set_yticks([0, 50, 100])
axc.grid(axis="y", color=GRID, lw=0.6)
for s in ("top", "right"):
    axc.spines[s].set_visible(False)
ax.text(0.5, 1.03, "C* moves only %.1f \u2192 %.1f kt" % (C_lo, C_hi),
        transform=axc.transAxes, fontsize=10, color=GREEN, ha="center",
        va="baseline", fontweight="bold")
ax.grid(color=GRID, lw=0.6, alpha=0.7)

# ------------------------------------------------- B: the horizon plateau
ax = fig.add_subplot(gs[0, 1])
panel_head(ax, " 2 ", "The horizon does not move.",
           "Certified horizon T* against constant catch")
admissible = [c for c in catches if c <= 150.0]
ax.plot(catches, [horizon[c]["q10"] for c in catches], marker="o", ms=6,
        lw=2.4, color=BLUE, label="informative residual class (q10)")
ax.plot(catches, [horizon[c]["q05"] for c in catches], marker="s", ms=5.5,
        lw=2.0, color=GREEN, label="q05 class")
ax.plot(catches, [horizon[c]["worst"] for c in catches], marker="^", ms=6,
        lw=2.0, color=ORANGE, label="worst class")
ax.axvspan(min(admissible), 150.0, color=BLUE, alpha=0.07)
ax.axvline(Cstar, color=GREY, ls=(0, (4, 3)), lw=1.4)
ax.text(Cstar + 3, 7.45, "C* = 91.6", color=MUTED, fontsize=10)
ax.axvline(Cvac, color=GREY, ls=(0, (4, 3)), lw=1.4)
ax.text(Cvac - 4, 7.45, "C_vac = 215.2", color=MUTED, fontsize=10, ha="right")
ax.set_ylim(4.6, 8.7)
ax.set_yticks([5, 6, 7, 8])
ax.set_xticks([0, 60, 120, 180, 215])
ax.set_xlabel("constant catch  C  (kt)", fontsize=11.5, labelpad=4)
ax.set_ylabel("certified horizon  T*  (years)", fontsize=11.5, labelpad=2)
ax.text(0.5, 0.10, "6 / 6 / 7 years for every catch \u2264 150 kt\n\u2014 including zero \u2014 "
                   "and every declared rule",
        transform=ax.transAxes, fontsize=11.5, color=INK, ha="center",
        bbox=dict(fc="white", ec=GRID, pad=5, alpha=0.95))
ax.legend(fontsize=9.5, loc="upper center", ncol=3, frameon=False,
          bbox_to_anchor=(0.5, 0.99), handlelength=1.4, columnspacing=1.2)
ax.grid(color=GRID, lw=0.6, alpha=0.7)

# ------------------------------------------------- C: clock vs lever
ax = fig.add_subplot(gs[0, 2])
panel_head(ax, " 3 ", "The clock outruns the lever.",
           "Year-on-year growth of the erosion margin")
xs = list(range(2, 8))
bars = ax.bar(xs, inc, color=BLUE, width=0.62, zorder=3)
for lev, col, lab in ((60, GREEN, "60 kt cut"), (120, ORANGE, "120 kt cut"),
                      (180, MUTED, "180 kt cut")):
    ax.axhline(lev, color=col, ls=(0, (5, 3)), lw=1.5, zorder=2)
    ax.text(1.53, lev + 12, lab, color=col, fontsize=10, ha="left", va="bottom")
ax.set_xlim(1.5, 8.05)
ax.set_ylim(0, 1020)
ax.set_xticks(xs)
ax.set_xticklabels(["T=2", "3", "4", "5", "6", "7"])
ax.set_xlabel("horizon year", fontsize=11.5, labelpad=4)
ax.set_ylabel("margin growth in that year  (kt)", fontsize=11.5, labelpad=2)
for b, v in zip(bars, inc):
    ax.text(b.get_x() + b.get_width() / 2, v + 16, "%d" % v, ha="center",
            fontsize=10, color=INK)
ax.text(0.5, 0.995, "the margin grows geometrically at\nF\u2032(K*) = %.4f per year; "
                   "from T = 4 one\nyear's growth exceeds every cut tested"
        % Fp, transform=ax.transAxes, fontsize=11.5, color=INK, ha="center",
        va="top", bbox=dict(fc="white", ec=GRID, pad=5, alpha=0.95))
ax.grid(axis="y", color=GRID, lw=0.6, alpha=0.7)
ax.set_axisbelow(True)

fig.text(0.045, 0.078,
         "Northern cod (2J3KL), 1983\u20132007.  C* = %.2f kt is the constructive viable-catch "
         "bound; C_vac = %.1f kt is where it becomes vacuous.\nT* is the last horizon at which "
         "the committed viability kernel is non-empty.  Every number plotted is recomputed from "
         "the archived result files." % (Cstar, Cvac),
         fontsize=10.5, color=MUTED, va="top", linespacing=1.5)

fig.savefig(OUT_PNG, dpi=200, facecolor="white")
json.dump({"C_profile_lo": C_lo, "C_profile_hi": C_hi, "r_T": r_T,
           "increments": inc, "Fprime_Kstar": Fp, "C_star": Cstar,
           "C_vac": Cvac, "eps": eps,
           "horizon_by_catch": {str(c): horizon[c] for c in catches},
           "n_transitions": n},
          open(OUT_JSON, "w"), indent=1)
print("wrote %s (%d bytes)" % (OUT_PNG, os.path.getsize(OUT_PNG)))
print("wrote %s" % OUT_JSON)
