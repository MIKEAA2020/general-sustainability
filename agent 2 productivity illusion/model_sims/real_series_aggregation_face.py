#!/usr/bin/env python3
"""Real-series figure — the aggregation face of the masking result (two-land v34).

Reads the public National Footprint and Biocapacity Accounts World series
(1961-2022) and plots, for the manuscript's §Discussion 'Application to the real
series':
  (a) aggregate biocapacity B and per-capita biocapacity B/P (index = 1 in 1961);
  (b) the log-change contributions d ln B = d ln(B/P) + d ln P, with the R_B = 1
      overshoot-onset line at 1971.
This is the *aggregation* face (per-capita halving hidden by population growth),
which the paper explicitly distinguishes from the two-land composition illusion.
Output: graphical_abstract/../reports/real_series_aggregation_face.png
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "nfa", "GFN_world_biocapacity_footprint_population_1961_2022.csv")
OUT = os.path.join(HERE, "..", "reports", "real_series_aggregation_face.png")

years, B, E, P = [], [], [], []
with open(DATA, newline="", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        years.append(int(row["Year"]))
        B.append(float(row["Biocapacity_gha"]))
        E.append(float(row["Footprint_gha"]))
        P.append(float(row["Population"]))
years = np.array(years); B = np.array(B); E = np.array(E); P = np.array(P)
# per-capita
Bpc = B / P
Ep = E / P
RB = E / B

fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.7), dpi=300)
FLOW, STOCK, GREY, ACCENT, BLUE = "#1f8a4c", "#b23a48", "#5c6b73", "#e0a458", "#3f7cac"
DARK = "#1f3a5f"

# (a) index of B vs B/P vs E/P
axes[0].plot(years, B / B[0], color=FLOW, lw=2.3, label="aggregate biocapacity $B$")
axes[0].plot(years, Bpc / Bpc[0], color=STOCK, lw=2.3, label="per-capita $B/P$")
axes[0].plot(years, Ep / Ep[0], color=GREY, lw=1.8, ls="--", label="per-capita footprint $E/P$")
axes[0].axhline(1, color=DARK, lw=1, ls=":")
axes[0].set_title("(a) 1961 = 1.0  — $B$ up, $B/P$ down", fontsize=10, color=DARK)
axes[0].legend(fontsize=6.6, frameon=False)
axes[0].set_xlabel("year"); axes[0].set_ylabel("index (1961 = 1)")
axes[0].grid(alpha=0.25)

# (b) R_B = E/B with overshoot onset
axes[1].plot(years, RB, color=BLUE, lw=2.3, label="$R_B=E/B$")
axes[1].axhline(1, color=STOCK, lw=1.6, ls="--")
i71 = int(np.argmin(np.abs(years - 1971)))
axes[1].axvline(1971, color=ACCENT, lw=1.4, ls=":")
axes[1].annotate("overshoot onset 1971", xy=(1971, RB[i71]), xytext=(1974, 1.55),
                 fontsize=7, color=ACCENT, arrowprops=dict(arrowstyle="->", color=ACCENT, lw=0.9))
axes[1].set_title("(b) $R_B=E/B$ crosses 1 in 1971", fontsize=10, color=DARK)
axes[1].legend(fontsize=7, frameon=False, loc="upper left")
axes[1].set_xlabel("year"); axes[1].set_ylabel("biocapacity ratio $R_B$")
axes[1].grid(alpha=0.25)

# (c) contribution split d ln B = d ln(B/P) + d ln P
dlB = np.log(B / B[0])
dlP = np.log(P / P[0])
dlBpc = np.log(Bpc / Bpc[0])
axes[2].bar(["per-capita\n$d\\ln(B/P)$", "population\n$d\\ln P$", "aggregate\n$d\\ln B$"],
            [dlBpc[-1], dlP[-1], dlB[-1]],
            color=[STOCK, FLOW, BLUE], alpha=0.85, edgecolor=DARK, lw=0.8)
axes[2].axhline(0, color=DARK, lw=1)
for i, v in enumerate([dlBpc[-1], dlP[-1], dlB[-1]]):
    axes[2].text(i, v + (0.03 if v > 0 else -0.09), f"{v:+.3f}",
                 ha="center", fontsize=8, color=DARK, fontweight="bold")
axes[2].set_title("(c) $d\\ln B = d\\ln(B/P)+d\\ln P$  (1961→2022)", fontsize=9.5, color=DARK)
axes[2].set_ylabel("log change 1961→2022")
axes[2].set_ylim(-0.9, 1.15)
axes[2].grid(alpha=0.25, axis="y")

fig.suptitle("The aggregation face of the masking result — National Footprint & Biocapacity Accounts (world, 1961–2022)",
             fontsize=11, color=DARK, y=1.02)
fig.tight_layout()
fig.savefig(OUT, dpi=300, bbox_inches="tight")
print("wrote", os.path.relpath(OUT, HERE))
print("  d ln(B/P)=%+.3f  d ln P=%+.3f  d ln B=%+.3f  (per-capita %+.1f%%, population %+.1f%%)"
      % (dlBpc[-1], dlP[-1], dlB[-1], dlBpc[-1]/dlB[-1]*100, dlP[-1]/dlB[-1]*100))
print("  R_cross(1971)=%.3f  R_B(1961)=%.3f R_B(2022)=%.3f" % (RB[i71], RB[0], RB[-1]))
