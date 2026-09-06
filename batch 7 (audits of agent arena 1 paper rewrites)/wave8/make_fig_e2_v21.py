#!/usr/bin/env python3
"""E2 Figure 2, v21 build (owner-directed label-clearing fix).

Reproduces figs_e2/fig2_kernel_vs_catch.png with one change class: the
labels that sat on the horizontal flat segment of the boundary curves
are raised into the empty band above it.

Previous rendering: the "BAU" and "60 kt / S1" labels were placed on
the flat segment at y ~ 885 kt, superimposing on the horizontal line
(and each other), and the "91.6 kt: maximal robust flat catch"
annotation rode the same segment. New placements:
  - "BAU":          above the flat segment, at (8, 930);
  - "60 kt / S1":   above the flat segment, at (63, 930);
  - "91.6 kt: maximal robust flat catch": ends at (89, 985), with the
    leader arrow dropping to the constructive point (91.59, 884.6).
The band y in (900, 1000) for C in [0, 90] is empty: the T=inf and T=1
boundaries are flat at 884.6 kt up to the constructive catch, the
legend sits at the top-left of the axes, and the rising part of the
T=inf curve begins only beyond C ~ 92.

Data (unchanged, the registered values of the source-year convention):
  r = 0.2368694030002864, K = 5000 kt (pinned), K* (LRP) = 884.6 kt,
  10th-percentile floor e_q10 = -80.8697790157355 kt,
  constructive catch = g(K*) - |e_q10| = 91.59402037298193 kt;
  boundaries computed by the same algorithms as the registered figure
  generator (T=inf by the monotone preimage recursion, T=1 by the
  one-step scan).
Writes: arena agent 1/paper rewrites/figs_e2/fig2_kernel_vs_catch_v21.png
"""
from __future__ import annotations
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites/figs_e2/fig2_kernel_vs_catch_v21.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif", "font.size": 9, "axes.labelsize": 10,
    "legend.fontsize": 8, "xtick.labelsize": 8, "ytick.labelsize": 8,
    "figure.dpi": 200,
})

# registered source-year values (exact, as computed by the fit)
r0 = 0.2368694030002864
K0 = 5000.0
K_star = 884.6
e_q10 = -80.8697790157355
g = lambda S: r0 * S * (1.0 - S / K0)
cons = g(K_star) - abs(e_q10)
assert abs(cons - 91.59402037298193) < 1e-9


def t1_boundary(c, e, r, K, Ks):
    # smallest S on [Ks, 10000] with S+g(S)-c+e >= Ks
    Sg = np.linspace(Ks, 10000, 40000)
    ok = Sg + r * Sg * (1 - Sg / K) - c + e >= Ks
    return Sg[np.argmax(ok)] if ok.any() else None


def tinf_boundary(c, e, r, K, Ks):
    # stable fixed point iteration on preimage; solve for lowest S0 s.t. orbit stays >=Ks
    b = Ks
    for _ in range(20000):
        Sg = np.linspace(Ks, 10000, 40000)
        delta = Sg + r * Sg * (1 - Sg / K) - c + e - b
        cand = Sg[delta >= 0]
        if len(cand) == 0:
            return None
        nb = cand[0]
        if abs(nb - b) < 1e-3:
            b = nb
            break
        b = nb
    return b


C = np.linspace(0, 240, 200)
b_inf = [tinf_boundary(c, e_q10, r0, K0, K_star) for c in C]
b_1 = [t1_boundary(c, e_q10, r0, K0, K_star) for c in C]

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(C, b_inf, "k-", lw=1.4, label="$T=\\infty$ lower boundary (q10 floor)")
ax.plot(C, b_1, "0.55", ls="--", lw=1.2, label="$T=1$ lower boundary (q10 floor)")
ax.axvline(cons, color="0.6", ls=":", lw=0.9)
# The object this label names is the vertical dotted line at C=cons. The
# whole region LEFT of that line and ABOVE the flat boundaries is empty,
# so the label sits above the base point with the leader dropping to it.
ax.annotate(f"{cons:.1f} kt: maximal robust flat catch",
            xy=(cons, 884.6),
            xytext=(89, 985), fontsize=8, ha="right",
            arrowprops=dict(arrowstyle="->", color="0.4", lw=0.7))
for c_mark, lab, dx, dy, ha in ((5, "BAU", 3, 45, "left"),
                                (60, "60 kt / S1", 3, 45, "left"),
                                (120, "flat 120", 6, -55, "left"),
                                (180, "flat 180", 6, -55, "left"),
                                (240, "flat 240", -4, 70, "right")):
    bm = tinf_boundary(c_mark, e_q10, r0, K0, K_star)
    if bm is not None:
        ax.plot([c_mark], [bm], "ks", ms=3.5)
        ax.text(c_mark + dx, bm + dy, lab, fontsize=7, ha=ha)
ax.set_xlabel("Constant catch $C$ (kt yr$^{-1}$)")
ax.set_ylabel("Kernel lower boundary (kt)")
ax.set_xlim(0, 240)
ax.set_ylim(850, 2600)
ax.grid(alpha=0.25)
ax.legend(loc="upper left")
fig.tight_layout()
fig.savefig(OUT, bbox_inches="tight")
plt.close(fig)
print("wrote", OUT)
