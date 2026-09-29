#!/usr/bin/env python3
"""Figure 10 -- the certified horizon is not a property of the policy.

Adds one figure to the nine of make_figs_v18.py:

  fig10  (a) the certified horizon T* against the constant catch, under each
             declared floor class -- flat at 6/6/7 years across the whole
             admissible range including a moratorium, and shortening only
             outside the constructive bound;
         (b) why: the year-on-year growth of the erosion margin, against the
             entire admissible catch range.

Nothing here is a new number. The horizon curve is Proposition 2.4's exact
crossing, the same expression campaign_e2_cadence_v3.py evaluates, and the
script REFUSES to write the figure unless every tabulated catch reproduces the
archived campaign output (src/results_cadence_v3/e2_cadence_v3.csv) exactly.
If the two ever disagree the figure is stale, and a stale figure is worse than
no figure.
"""
from __future__ import annotations

import csv
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

COD = Path(__file__).resolve().parent
sys.path.insert(0, str(COD))
import run_intervention_v3 as ri            # noqa: E402

FIG = COD / "figs_e2_v3"
FIG.mkdir(exist_ok=True)
OUT = COD / "results_cadence_v3"

# --- the same committed object and the same closed forms -------------------
FIT = ri.fit_surplus()
R, K = float(FIT["r"]), float(FIT["K"])
K_STAR, S_HI = ri.K_STAR, ri.S_HI
E_MIN = float(FIT["train_residual_min"])
E_Q05 = float(FIT["train_residual_q05"])
E_Q10 = float(FIT["train_residual_q10"])
EPS = abs(E_MIN)
A_MAX = 1.0 + R * (1.0 - 2.0 * K_STAR / K)
CLASSES = (("q10", E_Q10), ("q05", E_Q05), ("worst", E_MIN))
G_KSTAR = float(ri.surplus(K_STAR, R, K))
CSTAR = G_KSTAR - abs(E_Q10)
CVAC = R * K / 4.0 - abs(E_Q10)


def g(S):
    v = ri.surplus(S, R, K)
    return float(v) if np.ndim(v) == 0 else np.asarray(v, dtype=float)


def r_ladder(T):
    return EPS * (A_MAX ** T - 1.0) / (A_MAX - 1.0)


def crossing(policy_fn, e):
    """max{T : F^T(S_hi) >= K* + r_T} -- Proposition 2.4."""
    best, S = 0, S_HI
    for T in range(1, 15):
        S = S + g(S) - policy_fn(S) + e
        if S < K_STAR + r_ladder(T):
            break
        best = T
    return best


# ---------------------------------------------------------------- self-check
# The figure must not silently drift from the archived campaign.
arch = {}
for row in csv.DictReader(open(OUT / "e2_cadence_v3.csv", encoding="utf-8")):
    if row["section"] == "horizon" and row["quantity"].startswith("T*|C="):
        arch[row["quantity"]] = int(row["value"])
bad = []
for C in (0.0, 5.0, 30.0, 60.0, 91.59, 120.0, 150.0, 180.0, 200.0, 215.2):
    for cname, e in CLASSES:
        got, want = crossing(lambda S, C=C: C, e), arch["T*|C=%.2f|%s" % (C, cname)]
        if got != want:
            bad.append("C=%.2f %s: figure %d vs archived %d" % (C, cname, got, want))
if bad:
    raise SystemExit("fig10 REFUSED -- disagrees with the archived campaign:\n  "
                     + "\n  ".join(bad))
if abs(CSTAR - 91.59) > 0.01 or abs(CVAC - 215.2) > 0.2:
    raise SystemExit("fig10 REFUSED -- constants moved: C*=%.4f C_vac=%.4f"
                     % (CSTAR, CVAC))
print("fig10: all 30 archived (catch, class) horizons reproduced")

# ------------------------------------------------------------------ panel (a)
grid = np.arange(0.0, 235.1, 1.0)
hor = {cname: np.array([crossing(lambda S, c=float(C): c, e) for C in grid])
       for cname, e in CLASSES}

fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.6))
ax = axes[0]
style = {"q10": ("#1f4e79", "-", "10th pct. (informative)"),
         "q05": ("#b03a2e", "--", "5th pct."),
         "worst": ("k", ":", "perpetual worst")}
for cname, _ in CLASSES:
    col, ls, lab = style[cname]
    # offset the two harsher classes a hair so all three steps stay visible
    off = {"q10": 0.0, "q05": 0.10, "worst": -0.10}[cname]
    ax.step(grid, hor[cname] + off, where="post", color=col, ls=ls, lw=1.6,
            label=lab)
ax.axvspan(0.0, CSTAR, color="0.88", zorder=0)
ax.axvline(CSTAR, color="0.35", lw=1.0, ls="-.")
ax.axvline(CVAC, color="0.55", lw=1.0, ls="-.")
ax.text(CSTAR * 0.5, 7.75, "admissible range", ha="center", fontsize=7.5,
        color="0.3")
ax.text(CSTAR + 3, 7.75, "$C^*$", fontsize=8, color="0.3")
ax.text(CVAC - 4, 7.75, "$C_{\\rm vac}$", ha="right", fontsize=8, color="0.4")
ax.text(2, 6.35, "moratorium", fontsize=7.5, color="0.25")
ax.set_xlim(0, 235)
ax.set_ylim(4.5, 8.1)
ax.set_yticks([5, 6, 7, 8])
ax.set_xlabel("constant catch  $C$  (kt yr$^{-1}$)", fontsize=8.5)
ax.set_ylabel("certified horizon  $T^*$  (years)", fontsize=8.5)
ax.tick_params(labelsize=8)
ax.legend(fontsize=7.5, loc="lower left", frameon=False)
ax.set_title("(a)  no catch reduction buys a certified year", fontsize=9,
             loc="left")

# ------------------------------------------------------------------ panel (b)
ax = axes[1]
r = np.array([r_ladder(T) for T in range(1, 9)])
inc = np.diff(r)                      # growth from year T to year T+1
yrs = np.arange(2, 9)
ax.bar(yrs, inc, color="#1f4e79", width=0.62)
ax.axhline(CSTAR, color="#b03a2e", ls="--", lw=1.3)
# every bar is taller than the labelled line, so the label needs its own
# ground rather than a guess about where the whitespace is
ax.text(8.45, CSTAR + 95, "whole admissible catch range\n$C^*=91.59$ kt",
        fontsize=7.5, color="#b03a2e", ha="right", va="bottom",
        bbox=dict(fc="white", ec="none", pad=1.5))
for x, v in zip(yrs, inc):
    ax.text(x, v + 18, "%.0f" % v, ha="center", fontsize=7.5)
ax.set_xticks(yrs)
ax.set_xticklabels(["%d$\\to$%d" % (t - 1, t) for t in yrs], fontsize=7.5)
ax.set_ylim(0, 1000)
ax.set_xlabel("margin growth from year $T-1$ to $T$", fontsize=8.5)
ax.set_ylabel("growth of the erosion margin  (kt)", fontsize=8.5)
ax.tick_params(labelsize=8)
ax.set_title("(b)  one year of margin growth dwarfs the whole catch range",
             fontsize=9, loc="left")

fig.tight_layout()
fig.savefig(FIG / "fig10_cadence.png", bbox_inches="tight", dpi=300)
plt.close(fig)
print("v19: wrote fig10_cadence.png "
      "(horizons %s)" % {c: sorted(set(hor[c].tolist())) for c in hor})
