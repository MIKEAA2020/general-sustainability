#!/usr/bin/env python3
"""Source-year publication figures for paperE2_cod_intervention_v16.

Regenerates figs_e2/fig1..fig7 under the source-year convention:
  floors q10 -80.87, q05 -287.36, worst -328.97;
  g(K*)=172.46, gmax=296.09, constructive 91.59, F'(K*)=1.1531.
Fixes stale hardcoded destination-year labels and the mislabelled "flat 60 / S1"
replay curve (S1 is a switch rule and is plotted separately).
"""
from __future__ import annotations
import importlib.util, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

COD = Path(__file__).resolve().parent
sys.path.insert(0, str(COD))
import run_ladder as rl
import run_intervention_srcyear as ri
import pandas as pd

FIG = COD / "figs_e2"
FIG.mkdir(exist_ok=True)

years, ssb, c_reg, c_ann, idx, lrp = rl.load()
fit = ri.fit_surplus()
r0, K0 = float(fit["r"]), float(fit["K"])
K_star = ri.K_STAR
g = lambda S: r0 * S * (1.0 - S / K0)

# --- source-year floors / derived ------------------------------------------
res = {}
for j in range(len(years) - 1):
    res[years[j + 1]] = ssb[j + 1] - (ssb[j] + g(ssb[j]) - c_ann[j])
res_tr = np.array([res[y] for y in sorted(res) if y <= ri.TRAIN_END])
e_q10, e_q05, e_min = (float(np.percentile(res_tr, 10)),
                       float(np.percentile(res_tr, 5)),
                       float(res_tr.min()))
gK = g(K_star)
gmax = r0 * K0 / 4.0
Fp_K = 1.0 + r0 * (1.0 - 2.0 * K_star / K0)
cons = gK - abs(e_q10)
print(f"r={r0:.4f} K={K0:.0f} g(K*)={gK:.2f} gmax={gmax:.2f} F'(K*)={Fp_K:.4f} "
      f"constructive={cons:.2f}")
print(f"floors: q10={e_q10:.2f} q05={e_q05:.2f} worst={e_min:.2f}")

plt.rcParams.update({
    "font.family": "serif", "font.size": 9, "axes.labelsize": 10,
    "axes.titlesize": 10, "legend.fontsize": 8, "xtick.labelsize": 8,
    "ytick.labelsize": 8, "figure.dpi": 200,
})

# ===========================================================================
# Figure 1 — surplus curve and the three persistent floors (source-year)
# ===========================================================================
S = np.linspace(0, 2500, 600)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(S, g(S), "k-", lw=1.4, label="Schaefer $g(S)$ (registered fit)")
ax.axvline(K_star, color="0.35", ls="--", lw=0.9)
ax.text(K_star + 12, 400, "LRP 884.6", rotation=90, fontsize=8, va="bottom", color="0.25")
ax.axhline(gK, color="0.5", ls=":", lw=0.8)
ax.plot([K_star], [gK], "ko", ms=4)
# g(K*) label placed low-left in the clearly empty band beneath the curve,
# with a leader to the marked point
ax.annotate("$g(K^*) = 172.5$", xy=(K_star, gK), xytext=(430, 118),
            fontsize=8, ha="center", arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
ax.axhline(gmax, color="0.5", ls=":", lw=0.8)
ax.plot([K0 / 2], [gmax], "k^", ms=4)
# g_max label placed above the dotted g_max line in the empty top region
ax.annotate("$g_{\\max}=296.1$", xy=(K0 / 2, gmax), xytext=(1750, 335),
            fontsize=8, ha="center", arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
for y, lab in ((e_q10, "q10 floor $-80.9$"), (e_q05, "q05 floor $-287.4$"),
               (e_min, "worst floor $-329.0$")):
    ax.axhline(y, color="0.8", lw=1.2, ls=(0, (4, 2)))
    ax.text(90, y - 26, lab, fontsize=8)
# only the perpetual-worst floor lies beyond gmax -> that class is vacuous
# placed in the empty band between the q05 and q10 floors, right side
ax.text(1300, -185, "only the worst floor is vacuous: $|e|>g_{\\max}$",
        fontsize=8, ha="center")
ax.set_xlabel("Spawning-stock biomass $S$ (kt)")
ax.set_ylabel("Surplus production $g(S)$ (kt yr$^{-1}$)")
ax.set_xlim(0, 2500); ax.set_ylim(-520, 430); ax.grid(alpha=0.25)
fig.tight_layout(); fig.savefig(FIG / "fig1_surplus.png", bbox_inches="tight"); plt.close(fig)

# ===========================================================================
# Figure 2 — kernel lower boundary vs constant catch under the q10 floor
# ===========================================================================
def eq_boundary(c, r, K, Ks):
    """T=inf lower boundary of the monotone map S'=S+g(S)-c+e_q10."""
    # fixed point where S+g(S)-c+e_q10 = S  =>  g(S)=c-|e_q10|... solve
    # f(S)=S+g(S)-c+e_q10 ; fixed pt S*=g-c+... use root of g(S)=c-|e_q10|
    # robust: preimage recursion. Use the committed machinery instead.
    return None

C = np.linspace(0, 240, 200)
def t1_boundary(c, e, r, K, Ks):
    # smallest S on [Ks,10000] with S+g(S)-c+e >= Ks
    Sg = np.linspace(Ks, 10000, 40000)
    ok = Sg + r * Sg * (1 - Sg / K) - c + e >= Ks
    return Sg[np.argmax(ok)] if ok.any() else None

def tinf_boundary(c, e, r, K, Ks):
    # stable fixed point iteration on preimage; solve for lowest S0 s.t. orbit stays >=Ks
    # monotone: iterate preimage boundary
    b = Ks
    for _ in range(20000):
        # preimage of b: S + g(S) - c + e = b  (lower root)
        # solve quadratic: r/K S^2 + (1-r)S - (b+c-e) smaller root == -?  -> use scan
        Sg = np.linspace(Ks, 10000, 40000)
        delta = Sg + r * Sg * (1 - Sg / K) - c + e - b
        # want smallest S with F(S)>=b ; the lower crossing
        cand = Sg[delta >= 0]
        if len(cand) == 0:
            return None
        nb = cand[0]
        if abs(nb - b) < 1e-3:
            b = nb; break
        b = nb
    return b

b_inf = [tinf_boundary(c, e_q10, r0, K0, K_star) for c in C]
b_1 = [t1_boundary(c, e_q10, r0, K0, K_star) for c in C]
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(C, b_inf, "k-", lw=1.4, label="$T=\\infty$ lower boundary (q10 floor)")
ax.plot(C, b_1, "0.55", ls="--", lw=1.2, label="$T=1$ lower boundary (q10 floor)")
ax.axvline(cons, color="0.6", ls=":", lw=0.9)
# The object this label names is the vertical dotted line at C=cons. The whole
# region LEFT of that line and ABOVE the dashed T=1 boundary (y~884.6) is empty,
# so the label sits snug beside the vertical, just above the base point, and a
# short leader drops to the line.
ax.annotate(f"{cons:.1f} kt: maximal robust flat catch",
            xy=(cons, 884.6),
            xytext=(89, 905), fontsize=8, ha="right",
            arrowprops=dict(arrowstyle="->", color="0.4", lw=0.7))
for c_mark, lab, dx, dy in ((5, "BAU", 2, -55), (60, "60 kt / S1", 6, -55),
                            (120, "flat 120", 6, -55), (180, "flat 180", 6, -55),
                            (240, "flat 240", 2, -55)):
    bm = tinf_boundary(c_mark, e_q10, r0, K0, K_star)
    if bm is not None:
        ax.plot([c_mark], [bm], "ks", ms=3.5)
        ax.text(c_mark + dx, bm + dy, lab, fontsize=7)
ax.set_xlabel("Constant catch $C$ (kt yr$^{-1}$)")
ax.set_ylabel("Kernel lower boundary (kt)")
ax.set_xlim(0, 240); ax.set_ylim(850, 2600); ax.grid(alpha=0.25)
ax.legend(loc="upper left")
fig.tight_layout(); fig.savefig(FIG / "fig2_kernel_vs_catch.png", bbox_inches="tight"); plt.close(fig)

# ===========================================================================
# Figure 3 — reactive families: Family A (phi*g) and Family B (graded)
# ===========================================================================
S3 = np.linspace(K_star, 3600, 600)
fig, (axA, axB) = plt.subplots(1, 2, figsize=(12, 4.8))
# panel (a): surplus-proportional Family A
for ph, col in ((0.25, "#2ca02c"), (0.50, "#ff7f0e"), (0.75, "#1f77b4")):
    axA.plot(S3, ph * g(S3), lw=2, color=col, label=f"$\\phi$={ph:.2f}  ($\\phi\\,g(S)$)")
axA.axhline(60, color="#7f7f7f", ls="--", lw=1.5, label="flat 60 kt")
axA.axvline(K_star, color="red", ls=":", lw=1.5)
axA.set_xlabel(r"$S$ (kt)"); axA.set_ylabel(r"catch $C(S)$ (kt yr$^{-1}$)")
axA.set_xlim(K_star, 3600); axA.set_ylim(-5, 260)
# legend in empty lower-right of panel (a)
axA.legend(fontsize=8, loc="lower right", bbox_to_anchor=(1.0, 0.02))
axA.set_title("(a) surplus-proportional family A", fontsize=11)
axA.grid(alpha=0.3)
# panel (b): graded Family B
def graded2(S):
    return np.where(S < K_star, 0.0, np.where(S < 1.25 * K_star, 60.0, 90.0))
def graded3(S):
    out = np.zeros_like(S); out[S < K_star] = 0
    out[(S >= K_star) & (S < 1.15 * K_star)] = 30
    out[(S >= 1.15 * K_star) & (S < 1.35 * K_star)] = 60
    out[S >= 1.35 * K_star] = 90
    return out
axB.plot(S3, graded2(S3), lw=2, label="graded2: 0/60/90")
axB.plot(S3, graded3(S3), lw=2, label="graded3: 0/30/60/90")
axB.axhline(60, color="#7f7f7f", ls="--", lw=1.5, label="flat 60 kt")
for x in [K_star, 1.15 * K_star, 1.25 * K_star, 1.35 * K_star]:
    axB.axvline(x, color="lightgray", ls=":", lw=1)
axB.axvline(K_star, color="red", ls=":", lw=1.5)
axB.set_xlabel(r"$S$ (kt)"); axB.set_ylabel(r"catch $C(S)$ (kt yr$^{-1}$)")
axB.set_xlim(K_star, 3600); axB.set_ylim(-5, 110)
# legend in the empty lower-left region of panel (b)
axB.legend(fontsize=8, loc="lower left", bbox_to_anchor=(0.0, 0.02))
axB.set_title("(b) graded family B", fontsize=11)
axB.grid(alpha=0.3)
fig.tight_layout(); fig.savefig(FIG / "fig3_reactive_rules.png", bbox_inches="tight"); plt.close(fig)

# ===========================================================================
# Figure 4 — F'(S) and the expansion region (source-year, unchanged values)
# ===========================================================================
Sp = np.linspace(0, 3000, 600)
Fp = 1.0 + r0 * (1.0 - 2.0 * Sp / K0)
fig, ax = plt.subplots(figsize=(6.4, 3.2))
ax.plot(Sp, Fp, "k-", lw=1.4)
ax.axhline(1.0, color="0.4", ls="--", lw=0.9)
ax.axvline(K0 / 2, color="0.6", ls=":", lw=0.9)
ax.axvline(K_star, color="0.35", ls="--", lw=0.7)
ax.text(K_star + 10, 0.86, "LRP", fontsize=8, color="0.3")
ax.text(K0 / 2 + 10, 0.86, "$K/2 = 2500$", fontsize=8, color="0.35")
ax.fill_between(Sp, 1.0, 1.3, where=(Sp < K0 / 2), color="0.88", alpha=0.8)
# label moved into the empty band above the curve with a leader to the point
ax.annotate(f"expansive at the LRP: $F'(K^*) = {Fp_K:.3f}$",
            xy=(K_star, Fp[np.argmin(np.abs(Sp - K_star))]),
            xytext=(1000, 1.24), fontsize=8, ha="center",
            arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
ax.plot([K_star], [Fp[np.argmin(np.abs(Sp - K_star))]], "ko", ms=4)
ax.set_xlabel("Stock $S$ (kt)"); ax.set_ylabel("$F'(S) = 1 + r(1 - 2S/K)$")
ax.set_xlim(0, 3000); ax.set_ylim(0.75, 1.3); ax.grid(alpha=0.25)
fig.tight_layout(); fig.savefig(FIG / "fig4_fprime.png", bbox_inches="tight"); plt.close(fig)

# ===========================================================================
# Figure 5 — 1990 replay with observed residuals (source-year; S1 separate)
# ===========================================================================
def replay(cfn, s0=861.9):
    S = s0; path = [S]
    for j in range(5):
        y = 1991 + j; e = res.get(y, 0.0)
        S = max(0.0, S + g(S) - cfn(S) + e); path.append(S)
    return path
def S1(S): return 60.0 if S >= K_star else 0.0
def cpm(S):
    if S >= K_star: return 60.0
    if S >= 0.75 * K_star: return 30.0
    if S >= 0.5 * K_star: return 5.0
    return 0.0
policies = (("BAU (5 kt)", lambda S: 5.0, "-", "#1f77b4"),
            ("flat 0", lambda S: 0.0, "--", "#ff7f0e"),
            ("flat 60", lambda S: 60.0, "-.", "#2ca02c"),
            ("S1 (switch)", S1, ":", "#d62728"),
            ("cascade", cpm, ":", "#9467bd"))
yrs = np.arange(1990, 1996)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
for nm, f, ls, col in policies:
    ax.plot(yrs, replay(f), ls, lw=1.3, label=nm, color=col)
obs = [861.9] + [float(ssb[np.where(years == y)[0][0]]) for y in range(1991, 1996)]
ax.plot(yrs, obs, "k-", lw=2.2, label="observed SSB (Table A2)")
ax.axhline(K_star, color="0.4", ls="--", lw=0.9)
# LRP label seated right on top of the horizontal dashed line it names, in the
# empty area to the right (the forecast traces all run below y=884.6 there)
ax.text(1993.3, 890, "LRP 884.6", fontsize=8, ha="left", va="bottom", color="0.25")
ax.set_xlabel("Year"); ax.set_ylabel("Spawning-stock biomass (kt)")
ax.set_xlim(1989.55, 1995.6); ax.set_ylim(0, 1100); ax.grid(alpha=0.25)
# legend in the empty lower-left where only the black observed line descends
ax.legend(loc="lower left", fontsize=7.0)
fig.tight_layout(); fig.savefig(FIG / "fig5_replay.png", bbox_inches="tight"); plt.close(fig)

# ===========================================================================
# Figure 6 — K-grid sensitivity (source-year floors)
# ===========================================================================
kdf = pd.read_csv(COD / "results_srcyear" / "e2_elevation_k_grid.csv")
kk = kdf["K"].to_numpy()
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 3.4))
a1.plot(kk, kdf["g_max"], "ko-", ms=4, lw=1.2)
a1.axhline(abs(e_q05), color="0.7", ls="--", lw=1)
a1.axhline(abs(e_min), color="0.5", ls="--", lw=1)
# floor labels placed above their lines, clear of the rising curve
a1.text(1020, abs(e_q05) + 16, f"q05 floor {abs(e_q05):.1f}", fontsize=7.5)
a1.text(1020, abs(e_min) + 16, f"worst floor {abs(e_min):.1f}", fontsize=7.5)
a1.axhline(gmax, color="0.8", ls=":", lw=0.9)
a1.set_xlabel("Carrying capacity $K$ (kt)")
a1.set_ylabel("$g_{\\max}=rK/4$ (kt yr$^{-1}$)")
a1.set_ylim(100, 700); a1.grid(alpha=0.25)
a2.plot(kk, kdf["Fp_Kstar"], "ko-", ms=4, lw=1.2)
a2.axhline(1.0, color="0.4", ls="--", lw=0.9)
a2.axvline(2 * K_star, color="0.6", ls=":", lw=0.9)
# label seated above the (rising) curve and clear of the y-axis spine on the
# left; short leader to the marked vertical
a2.annotate("$K = 2K^* = 1769.2$", xy=(2 * K_star, 1.0),
            xytext=(1560, 1.115), fontsize=7.5, ha="center",
            arrowprops=dict(arrowstyle="->", color="0.4", lw=0.7))
a2.set_xlabel("Carrying capacity $K$ (kt)")
a2.set_ylabel("$F'(K^*)$ at the LRP")
a2.set_ylim(0.9, 1.25); a2.grid(alpha=0.25)
fig.tight_layout(); fig.savefig(FIG / "fig6_k_sensitivity.png", bbox_inches="tight"); plt.close(fig)

# ===========================================================================
# Figure 7 — stochastic constructive analogue
# ===========================================================================
cdf = pd.read_csv(COD / "results_srcyear" / "e2_elevation_stochastic_constructive.csv")
fig, ax = plt.subplots(figsize=(6.4, 3.6))
for scheme, ls, lab in (("iid", "-", "i.i.d. residual draws"),
                        ("block4", "--", "block bootstrap (length 4)"),
                        ("iid_no1992", ":", "i.i.d., 1992 residual removed")):
    sub = cdf[cdf["scheme"] == scheme]
    ax.plot(sub["C"], sub["P_stay"], ls, lw=1.4, label=lab)
ax.axhline(0.9, color="0.5", ls=":", lw=0.9)
# P=0.9 label placed in the empty region right of the curves' upper plateau,
# below the green no-1992 curve and above the blue i.i.d. curve
ax.text(40, 0.905, "$P = 0.9$", fontsize=8, ha="left")
ax.set_xlabel("Constant catch $C$ (kt yr$^{-1}$)")
ax.set_ylabel("$P($stay $\\geq$ LRP for 20 yr$)$ from the LRP")
ax.set_xlim(0, 122); ax.set_ylim(0.0, 1.02); ax.grid(alpha=0.25)
ax.legend(loc="lower left")
fig.tight_layout(); fig.savefig(FIG / "fig7_stochastic.png", bbox_inches="tight"); plt.close(fig)

print("wrote figs_e2/fig1,2,4,5,6,7 under source-year.")
print("  fig5 replay:", {nm: [round(v, 1) for v in replay(f)] for nm, f, _, _ in policies})
