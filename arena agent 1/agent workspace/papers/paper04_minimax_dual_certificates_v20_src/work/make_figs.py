#!/usr/bin/env python3
"""Figures for paper04 v20; every number is taken from p04_core / results.json."""
import os, sys, json
from fractions import Fraction as Q
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p04_core as C

ROOT = os.path.dirname(HERE)
FIGS = os.path.join(ROOT, "figs")
os.makedirs(FIGS, exist_ok=True)
RES = json.load(open(os.path.join(HERE, "results.json")))
plt.rcParams.update({"font.size": 8.5, "axes.titlesize": 9, "legend.fontsize": 7.5, "axes.labelsize": 8.5})
BLUE, RED, GREEN, GREY, ORANGE = "#1f4e79", "#b03a2e", "#2e7d32", "#777777", "#d98b1a"


def f(x):
    return float(Q(x))


# ------------------------------------------------------------------ Figure 1
fig, axs = plt.subplots(2, 2, figsize=(7.2, 5.6))
u = np.linspace(0, 1, 201)
ax = axs[0, 0]
p1, p2 = 0.4 - u, u - 0.6
ax.plot(u, p1, color=BLUE, label=r"$\psi_1(u)=\frac{2}{5}-u$")
ax.plot(u, p2, color=RED, label=r"$\psi_2(u)=u-\frac{3}{5}$")
ax.fill_between(u, np.minimum(p1, p2), -0.7, color=GREY, alpha=0.15, label=r"$\min_i\psi_i$ (lower envelope)")
ax.axhline(-0.1, color=GREEN, ls="--", label=r"pooled row $\frac{1}{2}\psi_1+\frac{1}{2}\psi_2\equiv-\frac{1}{10}$")
ax.axhline(0, color="k", lw=0.6)
ax.plot([0.5], [-0.1], "o", color=GREEN, ms=5)
ax.set_ylim(-0.7, 0.5); ax.set_xlabel(r"$u\in U=[0,1]$"); ax.set_title("(a) two-floor instance: obstructed, margin 1/10")
ax.legend(loc="upper right", frameon=False)
ax = axs[0, 1]
p2b = u - 0.2
ax.plot(u, p1, color=BLUE, label=r"$\psi_1(u)=\frac{2}{5}-u$")
ax.plot(u, p2b, color=RED, label=r"$\psi_2(u)=u-\frac{1}{5}$")
ax.fill_between(u, np.minimum(p1, p2b), -0.7, color=GREY, alpha=0.15)
ax.axhline(0, color="k", lw=0.6)
ax.plot([0.3], [0.1], "o", color=GREEN, ms=5)
ax.annotate(r"lower value $+\frac{1}{10}$ at $u=\frac{3}{10}$", (0.3, 0.1), (0.42, 0.3), arrowprops=dict(arrowstyle="->", lw=0.6))
for lam in (0.25, 0.5, 0.75):
    ax.plot(u, lam * p1 + (1 - lam) * p2b, color=GREEN, lw=0.6, alpha=0.6)
ax.set_ylim(-0.7, 0.5); ax.set_xlabel(r"$u\in U=[0,1]$"); ax.set_title("(b) feasible contrast: no certificate exists")
ax.legend(loc="lower right", frameon=False)
ax = axs[1, 0]
q1, q2 = 2 * u - 1, 1 - 2 * u
ax.plot(u, q1, color=BLUE, label=r"$\psi_1(u)=2u-1$")
ax.plot(u, q2, color=RED, label=r"$\psi_2(u)=1-2u$")
ax.plot([0, 1], [-1, -1], "s", color="k", ms=6, label=r"$U=\{0,1\}$: $\min_i\psi_i=-1$")
ax.plot([0.5], [0], "o", color=GREEN, ms=6, label=r"conv$\,U\ni\frac{1}{2}$: value 0")
ax.axhline(0, color="k", lw=0.6)
ax.set_ylim(-1.3, 1.3); ax.set_xlabel(r"$u$"); ax.set_title(r"(c) non-convex $U$: the dual sees conv$\,U$ (gap 1)")
ax.legend(loc="upper center", frameon=False, ncol=2)
ax = axs[1, 1]
ax.add_patch(plt.Rectangle((0, 0), 2, 2, fill=False, lw=1, color="k"))
ax.fill_between([1, 2], 0, 2, color=BLUE, alpha=0.12)
ax.fill_between([0, 2], 1, 2, color=RED, alpha=0.12)
ax.fill_between([0, 1], [1, 0], 0, color=GREEN, alpha=0.18)
ax.plot([1, 1], [0, 2], color=BLUE, label=r"$u_1\geq 1$")
ax.plot([0, 2], [1, 1], color=RED, label=r"$u_2\geq 1$")
ax.plot([0, 1], [1, 0], color=GREEN, label=r"$u_1+u_2\leq 1$")
ax.plot([1, 0, 1], [1, 1, 0], "o", color="k", ms=4)
ax.text(1.08, 1.08, "pairwise\nconsistent", fontsize=7)
ax.set_xlim(-0.05, 2.05); ax.set_ylim(-0.05, 2.05); ax.set_aspect("equal")
ax.set_xlabel(r"$u_1$"); ax.set_ylabel(r"$u_2$")
ax.set_title(r"(d) tight family $k=2$, $U=[0,2]^2$: value $-\frac{1}{3}$")
ax.legend(loc="lower right", frameon=True, framealpha=0.9, fontsize=6.8)
fig.tight_layout()
fig.savefig(os.path.join(FIGS, "fig1_dual_geometry.pdf")); plt.close(fig)

# ------------------------------------------------------------------ Figure 2
fig, axs = plt.subplots(1, 3, figsize=(7.4, 2.7))
Y = np.linspace(4, 14, 401)
cap1 = 1.5 - (Y - 2) / 10
cap2 = 59 / 50 - (Y - 2) / 10
ax = axs[0]
ax.plot(Y, cap1, color=BLUE, label=r"$\mathrm{cap}_1(Y)$")
ax.plot(Y, cap2, color=RED, label=r"$\mathrm{cap}_2(Y)$")
ax.plot(Y, cap1 + cap2, color="k", label=r"$\mathrm{cap}_1+\mathrm{cap}_2$")
ax.axhline(2, color=GREEN, ls="--", label=r"demand floor $D=2$")
ax.axvline(5.4, color=GREY, lw=0.6); ax.axvline(13.8, color=GREY, lw=0.6)
ax.axvspan(5.4, 13.8, color=ORANGE, alpha=0.12)
ax.text(5.55, 2.75, r"$Y^\ast=\frac{27}{5}$", fontsize=7.5)
ax.text(10.4, 1.55, "epistemic +\ninstitutional", fontsize=7, ha="center")
ax.text(13.85, 0.9, r"$\frac{69}{5}$", fontsize=7.5)
ax.set_xlabel(r"aggregate stock $Y=x_1+x_2$"); ax.set_ylim(-0.3, 3.1)
ax.set_title("(a) corner caps and the floor"); ax.legend(loc="lower left", frameon=False, fontsize=6.3)
ax = axs[1]
poly = [(2, 0), (2, 2), (0, 2)]
ax.add_patch(plt.Polygon(poly, closed=True, color=GREY, alpha=0.2, label=r"$U=\{u\in[0,2]^2: u_1+u_2\geq 2\}$"))
ax.add_patch(plt.Rectangle((0, 0), 1.1, 0.78, color=BLUE, alpha=0.3, label=r"$u_1\leq\frac{11}{10},\ u_2\leq\frac{39}{50}$"))
ax.plot([0, 2], [2, 0], color=GREEN, ls="--", label=r"$u_1+u_2=2$")
ax.plot([0, 47 / 25], [47 / 25, 0], color=RED, ls=":", label=r"$u_1+u_2=\frac{47}{25}$ (pooled)")
ax.set_xlim(0, 2.05); ax.set_ylim(0, 2.05); ax.set_aspect("equal")
ax.set_xlabel(r"$u_1$"); ax.set_ylabel(r"$u_2$")
ax.set_title(r"(b) $Y=6$: cap box misses $U$, margin $-\frac{3}{50}$"); ax.legend(loc="upper right", frameon=True, framealpha=0.95, fontsize=5.6, handlelength=1.4, borderpad=0.3)
ax = axs[2]
D = np.linspace(0, 2.6, 300)
Ys = np.minimum(77 / 5 - 5 * D, 69 / 5)
ax.plot(D, Ys, color="k", label=r"$Y^\ast(D)=\min(\frac{77}{5}-5D,\ \frac{69}{5})$")
ax.axhline(4, color=GREY, lw=0.6)
ax.axvline(8 / 25, color=GREY, lw=0.6, ls=":"); ax.axvline(57 / 25, color=GREY, lw=0.6, ls=":")
ax.plot([2], [5.4], "o", color=RED, ms=5)
ax.annotate(r"$D=2:\ Y^\ast=\frac{27}{5}$", (2, 5.4), (1.0, 7.5), arrowprops=dict(arrowstyle="->", lw=0.6), fontsize=7.5)
ax.text(0.36, 14.1, "physical (corner 2)", fontsize=6.5)
ax.text(1.0, 10.5, "epistemic + institutional", fontsize=6.5)
ax.text(2.33, 6.5, "no viable\nfibre", fontsize=6.5)
ax.set_xlabel(r"demand floor $D$"); ax.set_ylabel(r"critical aggregate $Y^\ast$")
ax.set_ylim(2.5, 15.6); ax.set_title("(c) demand-floor law"); ax.legend(loc="lower left", frameon=False, fontsize=6.3)
fig.tight_layout()
fig.savefig(os.path.join(FIGS, "fig2_benchmark.pdf")); plt.close(fig)

# ------------------------------------------------------------------ Figure 3
fig, axs = plt.subplots(1, 2, figsize=(7.4, 3.0), gridspec_kw=dict(width_ratios=[1.15, 1]))
ax = axs[0]
ax.set_xlim(0, 10); ax.set_ylim(0, 6.2); ax.axis("off")
ax.text(5, 5.9, r"$z_0=2$, blind first action $u_1$", ha="center", fontsize=8.5)
tops = {-2: (1.5, 4.9, r"$u_1=-2$: value $\frac{1}{2}$"), 0: (5, 4.9, r"$u_1=0$: value $0$"), 2: (8.5, 4.9, r"$u_1=+2$: value $\frac{1}{2}$")}
for a, (x, y, s) in tops.items():
    ax.add_patch(plt.Rectangle((x - 1.4, y - 0.3), 2.8, 0.6, fill=True, color=GREEN if a != 0 else GREY, alpha=0.2))
    ax.text(x, y, s, ha="center", va="center", fontsize=7.5)
    ax.plot([5, x], [5.6, y + 0.3], color="k", lw=0.6)
cells = [(-1, r"$z_1=-1,\ s=-1$", "value 1", r"$u_2\in\{0,-2\}$"), (1, r"$z_1=+1,\ s=-1$", "value 1", r"$u_2\in\{0,+2\}$"),
         (3, r"$z_1=3,\ s=+1$", "value 1", r"$u_2=-2$"), (5, r"$z_1=5,\ s=+1$", r"value $-1$", r"$u_2=-2$")]
xs = [1.3, 3.8, 6.3, 8.8]
for (z1, lab, val, act), x in zip(cells, xs):
    ax.plot([8.5, x], [4.6, 3.3], color="k", lw=0.6)
    col = RED if z1 == 5 else BLUE
    ax.add_patch(plt.Rectangle((x - 1.15, 1.9), 2.3, 1.4, fill=True, color=col, alpha=0.12))
    ax.text(x, 3.05, lab, ha="center", fontsize=6.4)
    ax.text(x, 2.6, act, ha="center", fontsize=7)
    ax.text(x, 2.15, val, ha="center", fontsize=7)
    ax.text(x, 1.55, r"$\mu=\frac{1}{4}$", ha="center", fontsize=6.5, color=GREY)
ax.text(5, 0.8, r"$Q_0=\frac{1}{4}(1+1+1-1)=\frac{1}{2}$;  171 adapted trees, 8 optimal;  open-loop supremum 0", ha="center", fontsize=7.5)
ax.text(5, 0.3, r"review cells after $u_1=+2$: $z_1=2+2s+d_1$", ha="center", fontsize=7, color=GREY)
ax.set_title("(a) the two-window review tree")
ax = axs[1]
sw = RES["two_window"]["sweep"]
z = sorted(int(k) for k in sw)
ax.plot(z, [f(sw[str(k)]["Q0"]) for k in z], "o-", color=BLUE, label=r"envelope $Q_0(z_0)$ (product prior)")
ax.plot(z, [f(sw[str(k)]["openloop"]) for k in z], "s--", color=GREY, label="open-loop supremum")
if sw["2"]["Rplus"] is not None:
    ax.plot(z, [f(sw[str(k)]["Rplus"]) for k in z], "^:", color=RED, label=r"$R^+=\min_\mu\max_\pi$ over couplings")
    ax.plot(z, [f(sw[str(k)]["Rminus"]) for k in z], "v:", color=GREEN, label=r"$R^-=\max_\pi\min_\mu$")
ax.axhline(0, color="k", lw=0.6)
ax.axvspan(3.5, 8.5, color=ORANGE, alpha=0.12)
ax.text(5.8, 0.6, "dynamic obstruction:\nevery tree defeated", fontsize=7, ha="center")
ax.set_xlabel(r"initial distance $z_0$"); ax.set_ylabel("value"); ax.set_ylim(-6.3, 1.6)
ax.set_title("(b) initial distance and the coupling class"); ax.legend(loc="lower left", frameon=False, fontsize=6.5)
fig.tight_layout()
fig.savefig(os.path.join(FIGS, "fig3_review.pdf")); plt.close(fig)

# ------------------------------------------------------------------ Figure 4
fig, axs = plt.subplots(1, 2, figsize=(7.4, 2.8))
ax = axs[0]
H = RES["helly"]
keys = [k for k in ("k1", "k2", "k3", "k3_rank1", "k4") if k in H]
labels = {"k1": "k=1", "k2": "k=2", "k3": "k=3", "k3_rank1": "k=3\nrank-1", "k4": "k=4"}
sizes = [1, 2, 3, 4, 5]
cols = [BLUE, GREEN, ORANGE, RED, "#6a1b9a"]
x = np.arange(len(keys))
bottom = np.zeros(len(keys))
for s, c in zip(sizes, cols):
    vals = np.array([H[k]["hist"].get(str(s), 0) / H[k]["infeasible"] for k in keys])
    ax.bar(x, vals, bottom=bottom, color=c, label=f"size {s}", width=0.6)
    bottom += vals
for i, k in enumerate(keys):
    ax.text(i, 1.02, f"n={H[k]['infeasible']}", ha="center", fontsize=6.5)
ax.set_xticks(x); ax.set_xticklabels([labels[k] for k in keys])
ax.set_ylim(0, 1.12); ax.set_ylabel("share of infeasible systems")
ax.set_title("(a) minimal infeasible subfamily sizes (random rows)"); ax.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0), frameon=False, fontsize=6.5)
ax = axs[1]
tau = np.linspace(0, 0.5, 200)
ax.plot(tau, 7 / 50 - tau, color=BLUE, label=r"$\Gamma_h(\tau)=\frac{7}{50}-\tau$ (this paper; $<0$ obstructed)")
ax.plot(tau, tau - 7 / 50, color=GREY, ls="--", label=r"$\Gamma(\tau)=\tau-\frac{7}{50}$ (companion; $>0$ obstructed)")
ax.axhline(0, color="k", lw=0.6); ax.axvline(7 / 50, color=RED, lw=0.8, ls=":")
ax.plot([0.2], [-0.06], "o", color=RED, ms=5)
ax.annotate(r"$\tau=\frac{1}{5}$: $-\frac{3}{50}$", (0.2, -0.06), (0.27, 0.12), arrowprops=dict(arrowstyle="->", lw=0.6), fontsize=7.5)
ax.text(0.148, 0.3, r"$\tau^\ast=\frac{7}{50}$", fontsize=7.5, color=RED)
ax.set_xlabel(r"review time $\tau$ (horizon $T=\tau+1$)"); ax.set_ylabel("integrated certificate")
ax.set_title(r"(b) three-branch instance: $\Gamma_h(\tau)$"); ax.legend(loc="lower left", frameon=False, fontsize=6.5)
fig.tight_layout()
fig.savefig(os.path.join(FIGS, "fig4_helly_gamma.pdf")); plt.close(fig)
print("figures written to", FIGS)
