#!/usr/bin/env python3
# Numerical audit for the Automatica-routes case study (paper 2, v30).
# Produces:
#   (1) a LaTeX-ready coverage table (printed),
#   (2) figs_p2/fig_p2_coverage.png -- a coverage-audit heatmap.
#
# Model for the audit ("delayed hidden regime", the paper's thm:delayed setting):
#   two regimes theta in {-1,+1}, scalar stock z >= 1 (safe set V = {z>=1}),
#   dynamics z^+ = z + theta*u, controls u in {-1,+1}, initial z0 observed
#   only at time 0 and at multiples of T_obs (blind window of T_obs steps).
#   The regime theta is revealed at the first observation (T_obs); before that
#   the policy must hold a single open-loop action.
#
# True epistemic viability (finite horizon, sound & complete per Theorem 4):
#   exists a held action u such that BOTH regime branches stay in V through the
#   blind window; after the reveal both branches are individually viable (u=theta
#   grows z). Hence viable  <=>  z0 >= 1 + T_obs.

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------- grid & states ----------------
z_grid = np.arange(1.0, 2.51, 0.1)          # initial positions
T_grid = [1, 2, 3]                            # blind-window length (steps)
V_floor = 1.0                                 # safe set {z >= 1}
U = [-1.0, +1.0]                              # controls
THETA = [-1.0, +1.0]                          # regimes (adversarial)

def inV(z):
    return z >= V_floor - 1e-12

# ---------------- exact finite-horizon recursion ----------------
# Belief = tuple of possible z values (one per regime branch), all >= floor for
# survival. The policy observes nothing during the blind window, so it holds one
# action for T_obs steps; at the reveal the regime is known and z=theta grows,
# so every surviving branch is individually viable.
def viable_exact(z0, T_obs):
    # open-loop step with held u for t=1..T_obs, both branches must stay in V
    for u in U:
        ok = True
        for th in THETA:
            z = z0
            for _ in range(T_obs):
                z = z + th * u
                if not inV(z):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return True
    return False

# one-step common-action certificate: common u keeps both branches in V for 1 step
def one_step_certificate(z0):
    for u in U:
        if all(inV(z0 + th * u) for th in THETA):
            return False  # a common safe action exists -> certificate silent
    return True           # no common safe action -> certificate fires

# timing certificate (threshold form): sigma* = z0 - V_floor ; fires iff T_obs > sigma*
def timing_certificate(z0, T_obs):
    return T_obs > (z0 - V_floor)

# ---------------- run the audit ----------------
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
            cell = "timing"     # the gap: nonviable, one-step silent, timing catches it
        else:
            cell = "UNCOVERED"  # should never happen here
        rows.append((T_obs, z0, v, c1, cT, cell))

# ---------------- coverage summary ----------------
nonv = [r for r in rows if not r[2]]
gap = [r for r in rows if r[5] == "timing"]
uncovered = [r for r in rows if r[5] == "UNCOVERED"]
print(f"total cells: {len(rows)}")
print(f"nonviable cells: {len(nonv)}")
print(f"  one-step certificate covers: {sum(1 for r in nonv if r[3])}")
print(f"  timing certificate covers (the residual gap): {len(gap)}")
print(f"  uncovered: {len(uncovered)}")
print()
print("T_obs  z0    viable  one-step  timing   verdict")
for r in rows:
    print(f"{r[0]:>3}   {r[1]:.1f}   {str(r[2]):>6}   {str(r[3]):>8}  {str(r[4]):>8}   {r[5]}")

# ---------------- figure ----------------
fig, ax = plt.subplots(figsize=(6.4, 2.9))
cmap = {"viable": "#2e7d32", "one-step": "#c62828", "timing": "#ef6c00", "UNCOVERED": "#111111"}
for (T_obs, z0, v, c1, cT, cell) in rows:
    ax.scatter(z0, T_obs, s=340, color=cmap[cell], marker="s",
               edgecolor="white", linewidth=0.7, zorder=3)
# true-viability boundary z0 = 1 + T_obs
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
import matplotlib.patches as mpatches
handles = [mpatches.Patch(color=cmap[k], label=l) for k, l in [
    ("viable", "viable"),
    ("one-step", "nonviable: one-step cert."),
    ("timing", "nonviable: timing cert. (residual gap)")]]
ax.legend(handles=handles + ax.get_legend_handles_labels()[0][3:5],
          loc="upper right", fontsize=7.5, framealpha=0.95)
ax.set_title("Coverage audit: common-action + timing certificates are jointly complete", fontsize=9)
plt.tight_layout()
out = "/home/user/arena agent 1/paper rewrites/latex/figs_p2/fig_p2_coverage.png"
plt.savefig(out, dpi=220)
print(f"\nfigure written: {out}")

# ---------------- LaTeX table rows ----------------
print("\n--- LaTeX rows ---")
for T_obs in T_grid:
    cells = []
    for z0 in z_grid:
        z0 = round(float(z0), 2)
        r = [r_ for r_ in rows if r_[0] == T_obs and abs(r_[1] - z0) < 1e-9][0]
        if r[5] == "viable":
            cells.append(r"$\circ$")
        elif r[5] == "one-step":
            cells.append(r"$\bullet$")
        elif r[5] == "timing":
            cells.append(r"$\ast$")
        else:
            cells.append(r"$\times$")
    print(" & ".join([str(T_obs)] + cells) + r" \\")
