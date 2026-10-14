#!/usr/bin/env python3
"""Figures for Paper 01 v73.  All data are exact and recomputed here."""
from fractions import Fraction as F
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Patch
import numpy as np, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "figs"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})

# ------------------------------------------------------------------ 1. diagnostic map
fig, ax = plt.subplots(figsize=(8.2, 5.0))
ax.set_xlim(0, 10); ax.set_ylim(0, 6.3); ax.axis("off")
def box(x, y, w, h, text, fc="#eef4ee", ec="#3a6b3a", fs=9.2, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=fc, ec=ec, lw=1.2))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal")
def arrow(x0, y0, x1, y1, text="", dx=0.08):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", lw=1.1, color="#333333"))
    if text:
        ax.text((x0+x1)/2 + dx, (y0+y1)/2, text, fontsize=8.2, color="#333333", ha="left", va="center")
# left column: tests, in the order of the ladder
box(0.3, 5.25, 3.9, 0.8, "Information state $B$ at a review\n(post-observation cell)", fc="#f4f4f4", ec="#555555", bold=True)
box(0.3, 4.05, 3.9, 0.85, "Finite-time exit certificate\n(Thm. 4.10): adverse drift on a strip", fc="#e9eef8", ec="#2b4b8c")
box(0.3, 2.85, 3.9, 0.85, "Common-action obstruction\n(Thm. 4.1): $\\mathcal{R}^B_{\\mathcal{V}}(B)=\\varnothing$")
box(0.3, 1.65, 3.9, 0.85, "Delayed-information obstruction\n(Thm. 4.6): $\\inf q/\\varepsilon < T_{\\mathrm{obs}}$")
box(0.3, 0.45, 3.9, 0.85, "Recourse obstruction (Prop. 4.12)\nor exact recursion (Thm. 3.1)")
for y0, y1 in [(5.25, 4.9), (4.05, 3.7), (2.85, 2.5), (1.65, 1.3)]:
    arrow(2.25, y0, 2.25, y1, "silent" if y0 < 5.2 else "")
# right column: verdict + remedy
box(5.6, 4.05, 4.1, 0.85, "Nonviable for every policy and every\nsensor: dynamics, not information", fc="#fbeaea", ec="#a33")
box(5.6, 2.85, 4.1, 0.85, "Nonviable at $B$; remedy: an observation\nthat separates the incompatible states", fc="#fbeaea", ec="#a33")
box(5.6, 1.65, 4.1, 0.85, "Nonviable in the blind class; remedy:\nan earlier informative observation", fc="#fbeaea", ec="#a33")
box(5.6, 0.45, 4.1, 0.85, "Nonviable by insufficient recourse;\nremedy: more post-observation authority", fc="#fbeaea", ec="#a33")
for y in (4.475, 3.275, 2.075, 0.875):
    arrow(4.2, y, 5.6, y, "fires", dx=-0.55)
ax.text(7.65, 5.65, "Static verdicts are a separate layer:\nthe fibre criterion (Prop. 5.2) limits\nobservation-only certifiers, not policies.",
        ha="center", va="center", fontsize=8.6, style="italic", color="#444444")
fig.tight_layout()
fig.savefig(OUT / "fig_v73_diagnostic.png", dpi=200, facecolor="white"); plt.close(fig)

# ------------------------------------------------------------------ 2. obstruction ladder (corrected labels)
fig, ax = plt.subplots(figsize=(7.6, 5.4))
ax.set_xlim(0, 10); ax.set_ylim(0, 7.4); ax.axis("off")
rungs = [(5.5, 3.2, "$U^B(B)$", "common admissible actions\nadmissibility obstruction (Thm. 4.1, Prop. 4.5)"),
         (4.3, 2.7, "$\\mathcal{R}^B_{\\mathcal{V}}(B)$", "common safe actions\ncommon-action obstruction, safety case (Thm. 4.1)"),
         (3.1, 2.2, "$\\mathcal{A}_{\\mathrm{tube}}(B,\\Delta)$", "held commands safe over one review\ntube obstruction, declared hold class (Prop. 4.2)"),
         (1.9, 1.7, "$\\mathcal{A}_N(B)$", "recursive witness actions (finite systems)\nexact on every finite horizon (Thm. 3.1)")]
for y, w, lab, desc in rungs:
    x = 2.6 - w/2
    ax.add_patch(FancyBboxPatch((x, y), w, 0.8, boxstyle="round,pad=0.02,rounding_size=0.1", fc="#eef4ee", ec="#9bb59b", lw=1.2))
    ax.text(2.6, y + 0.4, lab, ha="center", va="center", fontsize=12)
    ax.plot([x + w + 0.05, 4.9], [y + 0.4, y + 0.4], ls=":", color="#555555", lw=1)
    ax.text(5.0, y + 0.4, desc, ha="left", va="center", fontsize=9)
ax.annotate("", xy=(0.45, 1.9), xytext=(0.45, 5.5), arrowprops=dict(arrowstyle="-|>", lw=2.2, color="#b22222"))
ax.text(0.2, 3.7, "emptiness\ndescends", rotation=90, ha="center", va="center", fontsize=9.5, color="#b22222")
ax.add_patch(FancyBboxPatch((0.75, 0.35), 3.7, 0.8, boxstyle="round,pad=0.02,rounding_size=0.1", fc="#e9eef8", ec="#2b4b8c", lw=1.2))
ax.text(2.6, 0.75, "finite-time exit certificate\n(Thm. 4.10): below the ladder", ha="center", va="center", fontsize=9, color="#2b4b8c")
ax.plot([2.6, 2.6], [1.15, 1.85], ls="--", color="#2b4b8c", lw=1)
ax.text(5.0, 0.75, "defeats every control under full information;\nno observation argument is needed", ha="left", va="center", fontsize=9)
ax.text(5.0, 6.95, "Under the hold-class and adverse-path hypotheses the rungs are nested,\n"
        "$\\mathcal{A}_{\\mathrm{tube}}\\subseteq\\mathcal{R}^B_{\\mathcal{V}}\\subseteq U^B$, and emptiness of any rung\n"
        "at a reachable belief certifies $B\\notin\\mathrm{ERViab}_{\\mathcal{I}}(\\mathcal{V})$.",
        ha="left", va="center", fontsize=8.8, color="#333333")
fig.tight_layout()
fig.savefig(OUT / "fig_v73_ladder.png", dpi=200, facecolor="white"); plt.close(fig)

# ------------------------------------------------------------------ 3. coverage audit (exact data)
rows = []
for T in (1, 2, 3):
    for k in range(10, 26):
        z = F(k, 10)
        if z < 2: st = "first-step"
        elif z >= 1 + T: st = "viable"
        else: st = "later-blind-step"
        rows.append((T, z, st))
colors = {"viable": "#2e7d32", "first-step": "#c62828", "later-blind-step": "#ef6c00"}
fig, ax = plt.subplots(figsize=(8.6, 4.3))
for T, z, st in rows:
    ax.scatter(float(z), T, s=150, color=colors[st], marker="s", edgecolor="white", linewidth=.6, zorder=3)
zz = np.linspace(2, 2.55, 10)
ax.plot(zz, zz - 1, "k--", lw=1.2, label=r"hold-class boundary $z_0 = 1+T_{\mathrm{obs}}$")
ax.axvline(2, color="#ae2525", lw=1.1, label=r"one-step boundary $z_0 = 2$ (also the per-step-class boundary)")
ax.set_xlim(.95, 2.55); ax.set_ylim(.7, 3.3); ax.set_yticks([1, 2, 3]); ax.set_xticks([1 + i/4 for i in range(7)])
ax.set_xlabel(r"initial position $z_0$"); ax.set_ylabel(r"blind window $T_{\mathrm{obs}}$ (steps)")
handles = [Patch(color=colors[k], label=l) for k, l in [("viable", "viable in the hold class (6)"),
           ("first-step", "nonviable: one-step test fires (30)"), ("later-blind-step", "nonviable in the hold class only: later blind step (12)")]]
ax.legend(handles=handles + ax.get_lines(), loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=2, frameon=False, fontsize=8)
fig.subplots_adjust(left=.08, right=.97, bottom=.36, top=.96)
fig.savefig(OUT / "fig_v73_coverage.png", dpi=200, facecolor="white"); plt.close(fig)

# ------------------------------------------------------------------ 4. three-branch recourse instance
tau = np.linspace(0, 0.35, 300)
triple = 93/50 + tau                                   # hold-then-brake peak, any single branch
def pair_peak(nw, t):                                   # constant blind control with n.w = nw, then unit braking
    s = 34/25 + t + nw * t**2 / 2
    sd = 1 + nw * t
    return s + sd**2 / 2
fig, ax = plt.subplots(figsize=(7.2, 3.6))
ax.plot(tau, triple, color="#c62828", lw=2, label="triple: best common blind control ($u\\equiv0$), then brake")
ax.plot(tau, pair_peak(-2/5, tau), color="#2b4b8c", lw=1.6, label="pairs $\\{1,2\\}$, $\\{1,3\\}$: edge control $(-2/5,\\mp 4/5)$, then brake")
ax.plot(tau, pair_peak(-3/5, tau), color="#2e7d32", lw=1.6, ls="--", label="pair $\\{2,3\\}$: vertex control $n_1$, then brake")
ax.axhline(2, color="k", lw=1); ax.text(0.005, 1.992, "safety facet $n_j^\\top p = 2$", fontsize=8.5, va="top")
ax.axvline(7/50, color="#c62828", ls=":", lw=1); ax.text(7/50 + 0.004, 1.62, r"$\tau^* = 7/50$", color="#c62828", fontsize=9)
ax.axvline(1/5, color="#555555", ls=":", lw=1); ax.text(1/5 + 0.004, 1.62, r"$\tau = 1/5$", color="#555555", fontsize=9)
ax.set_xlabel(r"blind-window length $\tau$"); ax.set_ylabel("peak critical coordinate")
ax.set_ylim(1.6, 2.15); ax.set_xlim(0, 0.35)
ax.legend(fontsize=8, loc="upper left", frameon=False)
ax2 = ax.twinx(); ax2.plot(tau, 7/50 - tau, color="#888888", lw=1, alpha=0.9)
ax2.set_ylabel(r"certificate $\Gamma_h(\tau) = 7/50-\tau$", color="#666666"); ax2.set_ylim(-0.55, 0.3)
ax2.axhline(0, color="#888888", lw=0.6, ls="--")
fig.tight_layout()
fig.savefig(OUT / "fig_v73_recourse.png", dpi=200, facecolor="white"); plt.close(fig)
print("figures written to", OUT)
