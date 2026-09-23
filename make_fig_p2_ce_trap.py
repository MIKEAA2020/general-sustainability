#!/usr/bin/env python3
"""Fig 4 for paper 2: the certainty-equivalence trap (Remark 3)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

OUT = "arena agent 1/paper rewrites/latex/figs_p2"
os.makedirs(OUT, exist_ok=True)

Smin, Sstar, S0, c = 0.0, 1.0, 0.5, 0.25
tstar = (Sstar - S0) / c

fig, ax = plt.subplots(figsize=(4.6, 3.4), dpi=300)
# viable band V = [Smin, Sstar]
ax.axhspan(Smin, Sstar, color="#2e7d32", alpha=0.18)
ax.axhline(Smin, color="#2e7d32", lw=1.0)
ax.axhline(Sstar, color="black", ls=(0, (5, 4)), lw=1.4)
ax.annotate(r"$S^*$ (upper floor)", (5.3, Sstar), textcoords="offset points", xytext=(-64, 4), fontsize=9)
ax.annotate(r"$S_{\min}$", (5.3, Smin), textcoords="offset points", xytext=(-46, -12), fontsize=9)

# perfect-information feedback: flat
ax.plot([0, 5], [S0, S0], color="#2e7d32", lw=2.0, label=r"$u=g(S)$ (perfect feedback)")
# certainty-equivalence: drifts up
tt = [0, tstar]
ax.plot(tt, [S0, Sstar], color="#c62828", lw=2.0)
ax.plot([tstar, 5], [Sstar, Sstar + c * (5 - tstar)], color="#c62828", lw=2.0, ls=(0, (4, 3)))
ax.plot([tstar], [Sstar], "o", color="#c62828", ms=7, mec="black", zorder=5)
ax.annotate(r"$u=g(\hat S),\ \hat S=S+b$", (2.2, S0 + c * 2.2 + 0.06), fontsize=9, color="#c62828")
ax.annotate(r"$u=g(\hat S-b)$ recovers $g(S)$", (3.2, S0 - 0.10), fontsize=8, color="#2e7d32")

ax.set_xlim(0, 5.4); ax.set_ylim(-0.15, 1.55)
ax.set_xlabel(r"time $t$", fontsize=9); ax.set_ylabel(r"stock $S$", fontsize=9)
ax.set_xticks([0, tstar]); ax.set_xticklabels(["0", r"$t^*$"])
ax.set_yticks([Smin, Sstar]); ax.set_yticklabels([r"$S_{\min}$", r"$S^*$"])
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.legend(loc="upper left", fontsize=8, frameon=False)
fig.tight_layout()
fig.savefig(f"{OUT}/fig_p2_ce_trap.png", dpi=300)
plt.close(fig)
print("wrote", f"{OUT}/fig_p2_ce_trap.png", os.path.getsize(f"{OUT}/fig_p2_ce_trap.png"), "bytes")
