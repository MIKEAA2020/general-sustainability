#!/usr/bin/env python3
"""Figures for paper02 v16 -- all data recomputed from p02_core (exact), then plotted."""
import os, sys
from fractions import Fraction as Q
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p02_core as C

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 9, "axes.titlesize": 9.5, "legend.fontsize": 8, "figure.dpi": 150})

def save(fig, name):
    fig.savefig(os.path.join(OUT, name + ".pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUT, name + ".png"), bbox_inches="tight", dpi=170)
    plt.close(fig)

# ---------------- Figure 1: closed forms + class map ----------------
def fig1():
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.9), gridspec_kw={"width_ratios": [1.15, 1]})
    ax = axes[0]
    zs = np.linspace(0.5, 4.5, 801)
    w = Q(1, 2)
    cols = {1: "#1f77b4", 2: "#d62728", 3: "#2ca02c"}
    for ell in (1, 2, 3):
        vh = [float(C.closed_hold(Q(z).limit_denominator(10000), w, ell)) for z in zs]
        ax.step(zs, vh, where="post", color=cols[ell], lw=1.6, label=rf"hold, $\ell={ell}$")
    vo = [float(C.closed_openloop(Q(z).limit_denominator(10000), w, 1)) for z in zs]
    ax.step(zs, vo, where="post", color="k", lw=1.1, ls="--", label=r"open-loop, any $\ell$")
    ax.set_xlabel(r"initial state $z_0$"); ax.set_ylabel(r"safety value at $w=1/2$")
    ax.set_yticks([0, 0.5, 1]); ax.set_ylim(-0.05, 1.08); ax.set_xlim(0.5, 4.5)
    ax.axvspan(1, 2, color="0.92", zorder=0); ax.text(1.5, 0.08, "value of\nobservation", ha="center", fontsize=7.5)
    ax.annotate("", xy=(2.5, 0.52), xytext=(2.5, 0.98), arrowprops=dict(arrowstyle="<->", color="0.3", lw=0.8))
    ax.text(2.58, 0.75, "value of\nflexibility", ha="left", va="center", fontsize=7.5, color="0.3")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.28), ncol=2, frameon=False, handlelength=1.6, fontsize=7)
    ax.set_title("(a) closed forms, Theorem 5.1")
    # (b) class map on the certified grid
    ax = axes[1]
    grid = C.GRID
    combos = [(T, k) for T in C.TOBS for k in C.HORIZONS]
    img = np.zeros((len(grid), len(combos)))
    for i, z0 in enumerate(grid):
        for j, (T, k) in enumerate(combos):
            ell = C.effective_window(k, T)
            vh = C.bf_hold(z0, Q(1, 2), ell); vo = C.bf_openloop(z0, Q(1, 2), ell)
            if vh == 1:
                img[i, j] = 2          # both classes value one
            elif vo == 1:
                img[i, j] = 1          # open-loop one, hold 1/2 : class difference
            else:
                img[i, j] = 0          # both 1/2
    cmap = matplotlib.colors.ListedColormap(["#f7d4d4", "#f4b942", "#bfe3c0"])
    ax.imshow(img, origin="lower", aspect="auto", cmap=cmap, vmin=-0.5, vmax=2.5)
    ax.set_yticks(range(0, 16, 3)); ax.set_yticklabels([f"{float(z):.1f}" for z in grid[::3]])
    ax.set_xticks(range(len(combos))); ax.set_xticklabels([f"{k}" for _, k in combos], fontsize=7)
    for j in (3.5, 7.5):
        ax.axvline(j, color="k", lw=0.8)
    for T, xpos in zip(C.TOBS, (1.5, 5.5, 9.5)):
        ax.text(xpos, 16.1, rf"$T_{{\rm obs}}={T}$", ha="center", va="bottom", fontsize=8)
    ax.set_xlabel(r"horizon $k$ (within each $T_{\rm obs}$ block)"); ax.set_ylabel(r"$z_0$")
    ax.set_title("(b) certified grid: class comparison", pad=14)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color="#bfe3c0", label="both classes 1"),
                       Patch(color="#f4b942", label="open-loop 1, hold 1/2"),
                       Patch(color="#f7d4d4", label="both 1/2")],
              loc="upper center", bbox_to_anchor=(0.5, -0.30), ncol=3, frameon=False, fontsize=7, handlelength=1.2)
    fig.tight_layout(w_pad=1.5)
    save(fig, "fig2_closedforms")

# ---------------- Figure 2: two-floor value and sensor deficit ----------------
def fig2():
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.5))
    ax = axes[0]
    b = np.linspace(0, 1, 201)
    ax.plot(b, np.maximum(b, 1 - b), "k", lw=1.6, label=r"$V_k(b)=\max(b_0,b_1)$")
    ax.plot(b, b, color="#1f77b4", lw=1, ls=":", label=r"$\alpha=(1,0)$")
    ax.plot(b, 1 - b, color="#d62728", lw=1, ls=":", label=r"$\alpha=(0,1)$")
    ax.fill_between(b, np.maximum(b, 1 - b), 1, color="0.9", label=r"deficit $1-V_k$")
    ax.set_xlabel(r"$b_0$ (mass on state 0)"); ax.set_ylabel("value"); ax.set_ylim(0, 1.02)
    ax.set_title("(a) two-floor instance, all $k\\geq 1$"); ax.legend(frameon=True, framealpha=0.95, edgecolor="0.8", loc="upper center", fontsize=7)
    ax = axes[1]
    for eps, col in ((Q(1, 20), "#1f77b4"), (Q(1, 4), "#d62728")):
        d = [float(min(C.sensor_deficits(Q(x).limit_denominator(10000), 1 - Q(x).limit_denominator(10000), eps).values())) for x in b]
        ax.plot(b, d, color=col, lw=1.6, label=rf"$\varepsilon={eps}$")
    ax.plot(b, np.minimum(b, 1 - b), "k--", lw=1, label=r"min-mass $\min(b_1,b_2)$")
    ax.set_xlabel(r"$b_1$ (mass on $x_1$)"); ax.set_ylabel(r"one-step deficit $\Delta_1(b)$"); ax.set_ylim(0, 0.52)
    ax.set_title("(b) noisy sensor: $\\Delta_1=\\min\\{\\varepsilon,b_1,b_2\\}$"); ax.legend(frameon=False, fontsize=7)
    fig.tight_layout(w_pad=1.5)
    save(fig, "fig1_deficits")

# ---------------- Figure 3: learning deadlines ----------------
def fig3():
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.5))
    TL = list(range(0, 7))
    pinned = [float(C.pinned_threshold(t)) for t in TL]
    free = [2.1 for _ in TL]
    pf = [1 + t / 10 for t in TL]
    ax = axes[0]
    ax.plot(TL, pinned, "o-", color="#d62728", label=r"pinned probe: $21/10+T/10$")
    ax.plot(TL, free, "s--", color="#1f77b4", label=r"free probe: $21/10$")
    ax.plot(TL, pf, "^:", color="#2ca02c", label=r"exogenous revelation: $1+T/10$")
    ax.set_xlabel(r"deadline $T_{\rm learn}$"); ax.set_ylabel(r"viability threshold on $z_0$")
    ax.set_title("(a) thresholds, Proposition 6.1"); ax.legend(frameon=False, fontsize=7, loc="upper left")
    ax = axes[1]
    kp = [len(C.threshold_on_grid(lambda z: C.pinned_probe_viable(z, t), C.GRID)) for t in TL]
    kf = [len(C.threshold_on_grid(lambda z: C.probe_free_viable(z, t), C.GRID)) for t in TL]
    ax.bar([t - 0.18 for t in TL], kp, width=0.36, color="#d62728", label="pinned probe")
    ax.bar([t + 0.18 for t in TL], kf, width=0.36, color="#2ca02c", label="exogenous revelation")
    ax.set_xlabel(r"deadline $T_{\rm learn}$"); ax.set_ylabel(r"viable grid states $|K|$ (of 16)")
    ax.set_title("(b) kernel on the 16-state grid"); ax.legend(frameon=False, fontsize=7)
    fig.tight_layout(w_pad=1.5)
    save(fig, "fig3_deadlines")

# ---------------- Figure 4: noisy probes and repetition ----------------
def fig4():
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.5))
    ax = axes[0]
    zs = np.linspace(0.8, 5.0, 841)
    eps = Q(1, 10); tp = 0; k = 2
    v1 = [float(C.noisy_probe_value_formula(Q(z).limit_denominator(10000), tp, k, eps)) for z in zs]
    v3 = [float(C.majority3_value_formula(Q(z).limit_denominator(10000), tp, k + 2, eps)) for z in zs]
    ax.step(zs, v1, where="post", color="#1f77b4", lw=1.6, label=r"one reading at $t=0$, horizon $k=2$")
    ax.step(zs, v3, where="post", color="#d62728", lw=1.6, ls="--", label=r"three readings (majority), $k=4$")
    ax.set_xlabel(r"initial state $z_0$"); ax.set_ylabel(r"$V_k(b_0)$ at $\varepsilon=1/10$")
    ax.set_yticks([0, 0.9, 1]); ax.set_yticklabels(["0", "9/10", "1"]); ax.set_ylim(-0.05, 1.12)
    ax.annotate("243/250", xy=(2.4, 0.972), xytext=(2.0, 0.55), fontsize=7, color="#d62728",
                arrowprops=dict(arrowstyle="->", color="#d62728", lw=0.7))
    ax.annotate("floor margin\n2/10 later", xy=(1.2, 0.3), xytext=(1.6, 0.25), fontsize=7, color="0.3",
                arrowprops=dict(arrowstyle="->", color="0.3", lw=0.7))
    ax.set_title("(a) noisy-probe values, Proposition 7.2"); ax.legend(frameon=False, fontsize=7, loc="lower right")
    ax = axes[1]
    ns = [1, 3, 5, 7, 9, 11, 13, 15]
    pw = [float(C.majority_wrong(n, Q(1, 10))) for n in ns]
    bd = [0.6 ** n for n in ns]
    ax.semilogy(ns, pw, "o-", color="#1f77b4", label=r"exact $p_{\rm wrong}(n)$, $\varepsilon=1/10$")
    ax.semilogy(ns, bd, "s--", color="#d62728", label=r"bound $(3/5)^n$")
    ax.set_xticks(ns)
    ax.set_xlabel(r"number of readings $n$"); ax.set_ylabel("wrong-majority probability")
    ax.set_title("(b) repetition, Proposition 7.3"); ax.legend(frameon=False, fontsize=7)
    fig.tight_layout(w_pad=1.5)
    save(fig, "fig4_probes")

if __name__ == "__main__":
    fig1(); fig2(); fig3(); fig4()
    print("figures written to", OUT)
