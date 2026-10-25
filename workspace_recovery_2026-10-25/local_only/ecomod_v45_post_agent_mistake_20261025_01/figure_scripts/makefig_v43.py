"""Rebuild the one-stock overshoot/collapse comparator for ECOMOD v43 SI Figure S1.

Run from the package root: python figure_scripts/makefig_v43.py
The trajectory equations and numeric parameters are unchanged from v42; this
revision changes only annotation placement and GFN/NFA-facing unit labels.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from demo_unified import integrate

OUT = Path(__file__).resolve().parents[1] / "figures" / "S5_demo_overshoot_run.png"

# Clean overshoot -> collapse scenario (well-posed: smooth ramp + A_ext floor + K floor)
p = dict(rho=0.08, Amax=1.2, b0=0.5, bG=0.6, e=0.55, r=0.02, eta=0.03, alpha=0.2,
         sig=1.0, deltab=0.5, kappa=0.04, tw=120, tau_g=15, tau_p=25, Aext=0.02)
res = integrate(p, T=900.0, dt=0.1, A0=1.0, P0=0.45)
t, A, P, D, B = res["t"], res["A"], res["P"], res["D"], res["B"]

fig, ax = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
ax[0].plot(t, A, label="Stock A (model units)", color="#1f77b4", lw=2)
ax[0].plot(t, B, label="Biocapacity B (gha)", color="#2ca02c", lw=2)
ax[0].plot(t, P, label="Population P (cap)", color="#d62728", lw=2)
ax[0].set_ylabel("value (units differ)")
ax[0].legend(loc="upper right", fontsize=8)
ax[0].grid(alpha=.3)
ax[0].axvline(210, color="gray", ls=":", lw=1, zorder=1)

# Use two colour-matched leader arrows so the callout identifies both rising series.
i_boom = int(np.argmin(np.abs(t - 160.0)))
t_boom, b_boom, p_boom = float(t[i_boom]), float(B[i_boom]), float(P[i_boom])
anchor = (430.0, 0.95)
ax[0].annotate("", xy=(t_boom, b_boom), xytext=anchor,
               arrowprops=dict(arrowstyle="->", color="#2ca02c", lw=1.0,
                               shrinkA=2, shrinkB=3), zorder=4)
ax[0].annotate("", xy=(t_boom, p_boom), xytext=anchor,
               arrowprops=dict(arrowstyle="->", color="#d62728", lw=1.0,
                               shrinkA=2, shrinkB=3), zorder=4)
ax[0].text(442, 0.95, "boom: B & P rise\n(weak sustainability)",
           fontsize=8, color="#333", ha="left", va="center", zorder=5)

# Keep the separate mask-window callout in its own blank region, below the boom leaders.
ax[0].annotate("masking window\n(B peak while A dips)", xy=(210, 1.1), xytext=(265, 0.48),
               fontsize=8, color="#1f77b4",
               arrowprops=dict(arrowstyle="->", color="#1f77b4", lw=0.9),
               ha="left", va="center", zorder=5)

ax[1].plot(t, D, label="Ecological debt D (gha yr)", color="#9467bd", lw=2)
ax[1].set_xlabel("time (yr)")
ax[1].set_ylabel("D (gha yr)")
ax[1].legend(loc="upper right", fontsize=8)
ax[1].grid(alpha=.3)
ax[1].annotate("overshoot→debt→collapse\n(A hits extinction floor, P→0)",
               xy=(250, 0.37), xytext=(420, 0.34), fontsize=8, color="#9467bd",
               arrowprops=dict(arrowstyle="->", color="#9467bd"))
fig.suptitle("Implemented unified stock–flow model: overshoot → collapse (Paper N′)", fontsize=11)
fig.tight_layout()
fig.savefig(OUT, dpi=120)
print(f"saved {OUT}")
print(f"B(t=160)={b_boom:.3f} gha; P(t=160)={p_boom:.3f} cap; Dmax={D.max():.3f} gha yr")
