#!/usr/bin/env python3
"""
Coverage audit for "An Obstruction Calculus for Viability under Incomplete
Observation" (paper 2, Section 8).

Reproduces Table 1 and Figure 1 (fig_p2_coverage.png) of the manuscript from
the delayed hidden-regime model:

    regimes  theta in {-1, +1}   (hidden during the blind window)
    state    z >= 1              (safe set V = { z >= 1 })
    dynamics z^+ = z + theta*u,  u in {-1, +1}
    observation: nothing before T_obs; theta revealed exactly at T_obs.

Ground truth (sound & complete per the finite-horizon recursion, Theorem 1):
    the belief after k < T_obs blind steps contains the two extreme branches
    (z0 - k, -1) and (z0 + k, +1); a blind policy holds one action for both.
    The best blind policy drives one branch down at unit rate, so the
    guaranteed blind-window survival time is sigma* = z0 - 1, and viability
    holds iff z0 - 1 >= T_obs, i.e. z0 >= 1 + T_obs.

Certificates:
    one-step (common-action, Theorem 2) fires iff no common action keeps both
    branches in V for one step, i.e. iff z0 < 2.
    timing (Theorem 3, threshold sigma*) fires iff z0 >= 2 and T_obs > z0 - 1.

Run:  python3 paper2_coverage_audit.py
Outputs: summary counts, the LaTeX table body, and fig_p2_coverage.png.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

LATEX_DIR = "/home/user/arena agent 1/paper rewrites/latex"
OUT_PNG = os.path.join(LATEX_DIR, "figs_p2", "fig_p2_coverage.png")

z_grid = np.arange(1.0, 2.51, 0.1)   # initial positions
T_grid = [1, 2, 3]                   # blind-window length (steps)
V_floor = 1.0
U = [-1.0, +1.0]
THETA = [-1.0, +1.0]


def inV(z):
    return z >= V_floor - 1e-12


def viable_exact(z0, T_obs):
    """Exact finite-horizon verdict: exists a held action keeping BOTH regime
    branches in V for the T_obs blind steps (after the reveal each surviving
    branch is individually viable with u = theta)."""
    for u in U:
        if all(inV(z0 + th * u * T_obs) for th in THETA):
            # linear dynamics: after T_obs steps branch th is at z0 + th*u*T_obs
            return True
    return False


def one_step_certificate(z0):
    """Common-action (one-step) certificate fires iff no common action keeps
    both branches in V for a single step."""
    return all(not all(inV(z0 + th * u) for th in THETA) for u in U)


def timing_certificate(z0, T_obs):
    """Timing certificate (threshold sigma* = z0 - 1) fires iff T_obs > sigma*."""
    return T_obs > (z0 - V_floor)


rows = []
for T_obs in T_grid:
    for z0 in z_grid:
        z0 = round(float(z0), 2)
        v = viable_exact(z0, T_obs)
        c1 = one_step_certificate(z0)
        cT = timing_certificate(z0, T_obs)
        if v:
            cell = "viable"
        elif c1:
            cell = "one-step"
        elif cT:
            cell = "timing"
        else:
            cell = "UNCOVERED"
        rows.append((T_obs, z0, v, c1, cT, cell))

nonv = [r for r in rows if not r[2]]
gap = [r for r in rows if r[5] == "timing"]
uncovered = [r for r in rows if r[5] == "UNCOVERED"]
print(f"total cells: {len(rows)}")
print(f"nonviable cells: {len(nonv)}")
print(f"  one-step certificate covers: {sum(1 for r in nonv if r[3])}")
print(f"  timing certificate covers (the residual gap): {len(gap)}")
print(f"  uncovered: {len(uncovered)}")

# ---- figure (matches the caption: green viable, red one-step, orange timing) ----
fig, ax = plt.subplots(figsize=(6.4, 2.9))
cmap = {"viable": "#2e7d32", "one-step": "#c62828", "timing": "#ef6c00", "UNCOVERED": "#111111"}
for (T_obs, z0, v, c1, cT, cell) in rows:
    ax.scatter(z0, T_obs, s=340, color=cmap[cell], marker="s",
               edgecolor="white", linewidth=0.7, zorder=3)
zb = np.linspace(1.0, 2.6, 200)
ax.plot(zb, np.maximum(zb - 1.0, 0.9), color="black", lw=1.2, ls="--",
        label=r"true boundary $z_0=1+T_{\mathrm{obs}}$", zorder=4)
ax.plot([2.0, 2.0], [0.85, 3.2], color="#c62828", lw=1.2,
        label=r"one-step certificate ($z_0=2$)", zorder=4)
ax.set_xlabel(r"initial position $z_0$")
ax.set_ylabel(r"blind window $T_{\mathrm{obs}}$ (steps)")
ax.set_xticks(np.arange(1.0, 2.51, 0.25))
ax.set_yticks([1, 2, 3])
ax.set_ylim(0.8, 3.2)
ax.set_xlim(0.95, 2.55)
handles = [mpatches.Patch(color=cmap[k], label=l) for k, l in [
    ("viable", "viable"),
    ("one-step", "nonviable: one-step cert."),
    ("timing", "nonviable: timing cert. (residual gap)")]]
ax.legend(handles=handles + ax.get_legend_handles_labels()[0][3:5],
          loc="upper right", fontsize=7.5, framealpha=0.95)
ax.set_title("Coverage audit: common-action + timing certificates are jointly complete", fontsize=9)
plt.tight_layout()
plt.savefig(OUT_PNG, dpi=220)
print(f"\nfigure written: {OUT_PNG}")

# ---- LaTeX table body ----
print("\n--- LaTeX table body (rows) ---")
for T_obs in T_grid:
    cells = []
    for z0 in z_grid:
        z0 = round(float(z0), 2)
        r = [r_ for r_ in rows if r_[0] == T_obs and abs(r_[1] - z0) < 1e-9][0]
        cells.append({ "viable": r"$\circ$", "one-step": r"$\bullet$",
                       "timing": r"$\ast$" }.get(r[5], r"$\times$"))
    print(" & ".join([str(T_obs)] + cells) + r" \\")
