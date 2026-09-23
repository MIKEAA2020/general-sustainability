"""Benchmark figure, v45: the deposited v44 layout with a clarified fund
axis in panel (b) (external-audit follow-up gemini 1C).

Changes from v44, panel (b) only:
  * the STAGED legend entry names the plotted quantity: "quota sigma - 1/2
    (finances rebuild)" -- the curve is the quota, not the biomass;
  * the fund schedule joins the legend explicitly as the right-axis series
    (previously an in-plot text duplicate);
  * the right axis is labelled "fund x (STAGED)" in the fund colour.

All plotted values come from ``safetransition.benchmark.schedule_data()``
after the twenty-four exact checks pass; floats appear only in graphics.
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from fractions import Fraction as Q

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                "..", "src")))
from safetransition.benchmark import run_benchmark, schedule_data  # noqa: E402

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "..", "figs_p1"))
os.makedirs(OUT, exist_ok=True)

bench = run_benchmark(verbose=False)
assert bench.all_pass, "exact checks must pass before the figure is drawn"
d = schedule_data()
fl = [float(v) for v in d["t"]]

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.labelsize": 10.5, "axes.titlesize": 11,
    "xtick.labelsize": 9.5, "ytick.labelsize": 9.5, "axes.linewidth": 0.8,
})
GREEN, RED, ORANGE, GRAY, BLUE = "#2e8b57", "#c0392b", "#e08a1e", "#555555", "#1f6fb2"
LIGHTRED = "#f6d9d4"

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.0), dpi=300)

# ------------------------------------------------ (a) index vs the floor
ax1.axhspan(-1.4, 0, color=LIGHTRED, alpha=0.55, lw=0)
ax1.axhline(0, color=GRAY, lw=0.9, ls="--")
ax1.plot(fl, [float(v) for v in d["index_w11"]], color=GREEN, lw=2.2, marker="o",
         ms=4, label="composite index  $s_1+s_2$  (weight $w=(1,1)$)")
ax1.plot(fl, [float(v) for v in d["s1_adverse"]], color=RED, lw=2.2, marker="s",
         ms=4, label="ecological margin $s_1$ (heatwave)")
ax1.plot(fl, [float(v) for v in d["s1_benign"]], color=RED, lw=1.6, ls="--",
         label="ecological margin $s_1$ (no heatwave)")
i0 = [float(v) for v in d["index_w11"]].index(min(float(v) for v in d["index_w11"]))
ax1.annotate("index stays certified\n(min 2/5 > 0)", xy=(0.5, 0.42),
             xytext=(0.53, 1.72), fontsize=8.5, color=GREEN,
             arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.0))
ax1.annotate("floor breached\nmid-transition\n($s_1 = -4/5$)", xy=(0.5, -0.8),
             xytext=(0.06, -1.45), fontsize=8.5, color=RED,
             arrowprops=dict(arrowstyle="->", color=RED, lw=1.0))
ax1.set_xlim(-0.03, 1.03); ax1.set_ylim(-1.6, 3.1)
ax1.set_xticks([0, 0.5, 1]); ax1.set_xticklabels(["0", "1/2", "1"])
ax1.set_xlabel("time within the review period (yr)")
ax1.set_ylabel("margin (normalized units)")
ax1.set_title("(a) The index vs the floor (FAST plan)", loc="left")
ax1.legend(loc="upper right", fontsize=7.6, framealpha=0.95)

# ------------------------------------- (b) the plan menu as schedules
ax2.plot([0, 0.5, 1], [float(d["H_fast"][0]), float(d["H_fast"][1]),
                       float(d["H_fast"][2])],
         color=BLUE, lw=2.2, marker="o", ms=4, label="FAST: pulse + closed season")
ax2.plot([0, 1], [float(d["H_sy"]), float(d["H_sy"])], color=GRAY, lw=1.6,
         ls="-.", label="NO-SWITCH / SLOW: sustained yield $\\sigma(16/5)$")
ax2.plot([0, 0.5, 1], [float(d["H_staged"][0]), float(d["H_staged"][1]),
                       float(d["H_staged"][1])],
         color=GREEN, lw=2.2, marker="s", ms=4,
         label="STAGED: quota $\\sigma - 1/2$ (finances rebuild)")
ax2.axvspan(0.48, 0.52, color=ORANGE, alpha=0.25, lw=0)
ax2.text(0.5, 12.62, "heatwave strike", fontsize=8.5, color="#a06010", ha="center")
ax2.annotate("closed season", xy=(0.78, 0.0), xytext=(0.56, 2.9), fontsize=9,
             color=BLUE, arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.0))
ax2.set_xlim(-0.03, 1.03); ax2.set_ylim(-0.6, 13.6)
ax2.set_xticks([0, 0.5, 1]); ax2.set_xticklabels(["0", "1/2", "1"])
ax2.set_xlabel("time within the review period (yr)")
ax2.set_ylabel("quota  $H^*(t)$  (kt/yr)")
ax2.set_title("(b) The plan menu as management schedules")
ax3 = ax2.twinx()
fund_line, = ax3.plot([0, 0.5, 1], [float(v) for v in d["fund"]], color=ORANGE,
                      lw=1.8, ls=":", marker="d", ms=4,
                      label="fund $x(t)$, right axis (STAGED)")
ax3.set_ylim(-0.4, 14.4)
ax3.set_ylabel("fund $x$  (STAGED)", color="#a06010")
ax3.tick_params(axis="y", colors="#a06010")
h2, l2 = ax2.get_legend_handles_labels()
h3, l3 = ax3.get_legend_handles_labels()
ax2.legend(h2 + h3, l2 + l3, loc="upper right", fontsize=7.4, framealpha=0.95)

fig.tight_layout()
path = os.path.join(OUT, "fig_benchmark.png")
fig.savefig(path, dpi=300, facecolor="white")
print(f"wrote {path}")
