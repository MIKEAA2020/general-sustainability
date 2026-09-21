#!/usr/bin/env python3
"""Schematic figures for paper 2 (v17): fibre crossing, common-action gap,
delayed information. 300 dpi PNGs into latex/figs_p2/."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

OUT = "arena agent 1/paper rewrites/latex/figs_p2"
os.makedirs(OUT, exist_ok=True)

# ---------------- Fig 1: fibre crossing a floor ----------------
fig, ax = plt.subplots(figsize=(4.6, 3.6), dpi=300)
ax.axhspan(0.5, 1.0, color="#2e7d32", alpha=0.22)      # safe (q>=0)
ax.axhspan(0.0, 0.5, color="#c62828", alpha=0.14)      # unsafe
ax.axhline(0.5, color="black", ls=(0,(5,4)), lw=1.2)   # floor
ax.plot([0.6, 0.6], [0.0, 1.0], color="#1565c0", lw=1.8, label=r"fibre $O^{-1}(y)$")
ax.plot(0.6, 0.8, "o", color="#2e7d32", ms=9, mec="black")
ax.plot(0.6, 0.3, "o", color="#c62828", ms=9, mec="black")
ax.annotate(r"$x_1$ (safe)", (0.6, 0.8), textcoords="offset points", xytext=(8, 6), fontsize=9)
ax.annotate(r"$x_2$ (unsafe)", (0.6, 0.3), textcoords="offset points", xytext=(8, -14), fontsize=9)
ax.annotate(r"floor $q=0$", (0.05, 0.52), textcoords="offset points", xytext=(0, 2), fontsize=8)
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.set_xlabel(r"state $x_1$", fontsize=9); ax.set_ylabel(r"state $x_2$", fontsize=9)
ax.set_xticks([]); ax.set_yticks([])
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.set_title(r"One observation fibre crosses the floor", fontsize=9)
fig.tight_layout()
fig.savefig(f"{OUT}/fig_p2_fibre.png", dpi=300)
plt.close(fig)

# ---------------- Fig 2: incompatible safe controls ----------------
fig, ax = plt.subplots(figsize=(5.2, 2.2), dpi=300)
ax.plot([0, 1], [0.5, 0.5], color="black", lw=1.0)
ax.plot([0, 0.4], [0.5, 0.5], color="#c62828", lw=7, solid_capstyle="butt")
ax.plot([0.6, 1.0], [0.5, 0.5], color="#1565c0", lw=7, solid_capstyle="butt")
ax.annotate(r"safe actions at $x_1$:  $u\leq 0.4$", (0.2, 0.5), textcoords="offset points", xytext=(0, 12), ha="center", fontsize=9, color="#c62828")
ax.annotate(r"safe actions at $x_2$:  $u\geq 0.6$", (0.8, 0.5), textcoords="offset points", xytext=(0, 12), ha="center", fontsize=9, color="#1565c0")
ax.annotate("", xy=(0.4, -0.28), xytext=(0.6, -0.28), arrowprops=dict(arrowstyle="<->", color="black", lw=1))
ax.text(0.5, -0.44, "no common safe action", ha="center", fontsize=9)
ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.6, 0.9)
ax.set_xticks([0, 0.4, 0.6, 1.0]); ax.set_yticks([])
ax.set_xlabel(r"control $u$", fontsize=9)
for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(f"{OUT}/fig_p2_common_action.png", dpi=300)
plt.close(fig)

# ---------------- Fig 3: delayed information ----------------
fig, ax = plt.subplots(figsize=(5.2, 3.0), dpi=300)
q0, eps, Tobs = 1.0, 0.25, 6.0
tstar = q0 / eps
tt = [0, tstar]
ax.plot(tt, [q0 - eps*t for t in tt], color="#2e7d32", lw=2, label=r"$q(t)=q_0-\varepsilon t$")
ax.plot([tstar, Tobs], [0, -eps*(Tobs-tstar)], color="#c62828", lw=2, ls=(0,(4,3)))
ax.axhline(0, color="black", lw=1)
ax.axvline(tstar, color="#2e7d32", ls=(0,(5,4)), lw=1)
ax.axvline(Tobs, color="#1565c0", ls=(0,(5,4)), lw=1.4)
ax.fill_betweenx([-1.2, 0], tstar, Tobs, color="#c62828", alpha=0.12)
ax.annotate(r"$t^*=q_0/\varepsilon$", (tstar, 0), textcoords="offset points", xytext=(-58, 8), fontsize=9, color="#2e7d32")
ax.annotate(r"$T_{\mathrm{obs}}$", (Tobs, 0), textcoords="offset points", xytext=(4, 8), fontsize=9, color="#1565c0")
ax.annotate("information arrives\ntoo late", (5.2, -0.55), ha="center", fontsize=8.5, color="#c62828")
ax.set_xlim(-0.4, 7.6); ax.set_ylim(-1.15, 1.15)
ax.set_xlabel(r"time $t$", fontsize=9); ax.set_ylabel(r"constraint margin $q$", fontsize=9)
ax.set_xticks([0, tstar, Tobs]); ax.set_xticklabels(["0", r"$t^*$", r"$T_{\mathrm{obs}}$"])
for s in ("top", "right"): ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(f"{OUT}/fig_p2_timing.png", dpi=300)
plt.close(fig)

print("figures written to", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f, os.path.getsize(os.path.join(OUT, f)), "bytes")
