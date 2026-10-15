#!/usr/bin/env python3
"""Source-year publication figures, v3 edition (paperE2_cod_intervention_v29).

Supersedes make_figs_v16.py with two provenance-only changes: it imports the
promoted runner run_intervention_v3.py (run_intervention_srcyear.py carries a
verbatim v2 docstring that falsely claims bit-identity with the registered
runner, and writes to results_srcyear/) and it reads the v3 elevation outputs
in results_srcyear_v3/ (campaign_e2_elevation_v3.py), whose floor classes are
derived rather than frozen at the registered values. The two runners are
functionally identical, so the figures are unchanged; the difference is that
the provenance chain now names v3 scripts throughout.

Regenerates figs_e2_v3/fig1..fig7 under the source-year convention:
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
import run_intervention_v3 as ri
import pandas as pd

FIG = COD / "figs_e2_v3"
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
kdf = pd.read_csv(COD / "results_srcyear_v3" / "e2_elevation_k_grid.csv")
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
cdf = pd.read_csv(COD / "results_srcyear_v3" / "e2_elevation_stochastic_constructive.csv")
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

print("wrote figs_e2_v3/fig1..fig7 under source-year (v3 provenance).")
print("  fig5 replay:", {nm: [round(v, 1) for v in replay(f)] for nm, f, _, _ in policies})


# ===========================================================================
# v18 additions -- the two figures the structural pass needs.
#
#   fig8  the protection-supply budget (Proposition 2.1) and the three regimes
#         of the surplus-proportional family (Proposition 2.3)
#   fig9  identification: the profile likelihood over K, and the two
#         functionals the results actually depend on
#
# Both are computed from the same committed fit and the same closed forms the
# paper states, so nothing here is a new number.
# ===========================================================================
import csv as _csv
import math as _math

E_Q10 = float(fit["train_residual_q10"])
E_Q05 = float(fit["train_residual_q05"])
E_MIN = float(fit["train_residual_min"])
G_KSTAR = float(g(K_star))
G_MAX = r0 * K0 / 4.0
CSTAR = G_KSTAR - abs(E_Q10)
CVAC = G_MAX - abs(E_Q10)


def _lower_root(target):
    """Smaller root of g(S) = target on the increasing branch, or None."""
    if target > G_MAX:
        return None
    lo, hi = 0.0, K0 / 2.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if g(m) < target:
            lo = m
        else:
            hi = m
    return hi


# ---------------------------------------------------------------- fig8
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.7))

ax = axes[0]
xs = np.linspace(0.0, 240.0, 200)
ax.plot(xs, CSTAR - xs, "k-", lw=1.6,
        label=r"budget: margin $= C^* - C(K^*)$")
ax.axhline(0.0, color="0.55", lw=0.8)
ax.axvline(CSTAR, color="0.35", ls="--", lw=0.9)
ax.axvline(CVAC, color="0.35", ls=":", lw=1.1)
ax.text(CSTAR - 4, -96, r"$C^*=91.6$", ha="right", fontsize=8, color="0.25")
ax.text(CVAC - 4, -96, r"$C_{vac}=215.2$", ha="right", fontsize=8, color="0.25")
pts = [("BAU 5 kt", 5.0), ("flat 60", 60.0), (r"$\phi=0.25$", 0.25 * G_KSTAR),
       (r"$\phi=0.50$", 0.50 * G_KSTAR), (r"$\phi=0.60$", 0.60 * G_KSTAR),
       (r"$\phi=0.75$", 0.75 * G_KSTAR), ("flat 120", 120.0), ("flat 180", 180.0)]
for lab, c in pts:
    ax.plot([c], [CSTAR - c], "o", ms=5, color="#1f4e79" if c <= CSTAR else "#b03a2e")
    ax.annotate(lab, (c, CSTAR - c), textcoords="offset points", xytext=(4, 3),
                fontsize=7.5)
ax.set_xlabel("catch at the reference point  $C(K^*)$  (kt)", fontsize=8.5)
ax.set_ylabel("protection margin (kt)", fontsize=8.5)
ax.set_xlim(-8, 250)
ax.set_ylim(-110, CSTAR + 12)
ax.tick_params(labelsize=8)
ax.legend(fontsize=7.5, loc="upper right", frameon=False)
ax.set_title("(a)  harvest and protection are one budget", fontsize=9, loc="left")

ax = axes[1]
# The boundary curve diverges as phi -> 0.727 (the lower root of
# (1-phi)g(S) = |e| runs to K/2), so the regimes are shown on the two MARGINS,
# which are straight lines and cannot clip.
phis = np.linspace(0.0, 0.90, 300)
m_safe = (1.0 - phis) * G_KSTAR - abs(E_Q10)      # >0  <=> whole safe set
m_nonempty = (1.0 - phis) * G_MAX - abs(E_Q10)    # >0  <=> kernel nonempty
p_safe = 1.0 - abs(E_Q10) / G_KSTAR
p_non = 1.0 - abs(E_Q10) / G_MAX
ax.axvspan(0.0, p_safe, color="#1f4e79", alpha=0.10)
ax.axvspan(p_safe, p_non, color="0.55", alpha=0.14)
ax.axvspan(p_non, 0.90, color="#b03a2e", alpha=0.10)
ax.plot(phis, m_safe, "k-", lw=1.6,
        label=r"safe-set margin  $(1-\phi)g(K^*)-|e_{q10}|$")
ax.plot(phis, m_nonempty, "k--", lw=1.3,
        label=r"nonemptiness margin  $(1-\phi)g_{\max}-|e_{q10}|$")
ax.axhline(0.0, color="0.4", lw=0.9)
ax.axvline(p_safe, color="#1f4e79", ls=":", lw=1.1)
ax.axvline(p_non, color="#b03a2e", ls=":", lw=1.1)
ax.text(0.012, -88, "whole safe set", fontsize=8, color="#1f4e79")
ax.text(0.545, -88, "viable above the LRP", fontsize=8, color="0.25")
ax.text(0.735, -88, "empty", fontsize=8, color="#b03a2e")
ax.text(p_safe - 0.008, 118, "0.531", ha="right", fontsize=8, color="#1f4e79")
ax.text(p_non + 0.008, 118, "0.727", fontsize=8, color="#b03a2e")
for pp in (0.25, 0.50, 0.60, 0.75):
    mm = (1.0 - pp) * G_KSTAR - abs(E_Q10)
    col = ("#1f4e79" if pp <= p_safe + 1e-9
           else "#b03a2e" if pp >= p_non - 1e-9 else "#7f7f7f")
    ax.plot([pp], [mm], "o", ms=5, color=col)
    ax.annotate(r"$\phi=%.2f$" % pp, (pp, mm), textcoords="offset points",
                xytext=(5, 3), fontsize=7.5)
ax.set_xlabel(r"harvest fraction  $\phi$", fontsize=8.5)
ax.set_ylabel("margin (kt)", fontsize=8.5)
ax.set_xlim(0.0, 0.90)
ax.set_ylim(-100, 150)
ax.tick_params(labelsize=8)
ax.legend(fontsize=7.5, loc="upper right", frameon=False)
ax.set_title("(b)  three regimes of the reactive family", fontsize=9, loc="left")

fig.tight_layout()
fig.savefig(FIG / "fig8_frontier.png", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- fig9
prof = list(_csv.DictReader(open(COD / "results_ident_v3" / "e2_profile_K.csv")))
Ks = np.array([float(p["K"]) for p in prof])
sse = np.array([float(p["sse"]) for p in prof])
gk = np.array([float(p["g_Kstar"]) for p in prof])
fp = np.array([float(p["Fp"]) for p in prof])
cs = np.array([float(p["Cstar"]) for p in prof])
n = 24
cut = sse.min() * (1.0 + 4.3009 / (n - 2))

fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.6))
ax = axes[0]
ax.semilogx(Ks, sse / 1e3, "k-", lw=1.5)
ax.axhline(cut / 1e3, color="#b03a2e", ls="--", lw=1.0)
ax.axvline(5000.0, color="#1f4e79", ls=":", lw=1.2)
ax.axvline(2 * K_star, color="0.35", ls="-.", lw=1.0)
ax.text(5200, sse.max() / 1e3 * 0.93, "declared box edge\n$K=5000$ (committed)",
        fontsize=7.5, color="#1f4e79")
ax.text(2 * K_star * 1.05, sse.max() / 1e3 * 0.62,
        "$2K^*=1769$: expansion\nbegins here", fontsize=7.5, color="0.25")
ax.text(Ks[3], cut / 1e3 * 1.008, "profile 95% cut", fontsize=7.5, color="#b03a2e")
ax.set_xlabel(r"carrying capacity  $K$  (kt, log scale)", fontsize=8.5)
ax.set_ylabel(r"profiled sum of squares  ($10^3$ kt$^2$)", fontsize=8.5)
ax.tick_params(labelsize=8)
ax.set_title("(a)  $K$ is not identified from above", fontsize=9, loc="left")

ax = axes[1]
inset = Ks <= cut
ax.plot(Ks, gk, "k-", lw=1.4, label=r"$g(K^*)$")
ax.plot(Ks, cs, "#1f4e79", lw=1.4, label=r"$C^*=g(K^*)-|e_{q10}|$")
ax.fill_between(Ks, 0, 1, where=inset, color="0.85", alpha=0.5,
                transform=ax.get_xaxis_transform(), label="profile 95% set")
ax2 = ax.twinx()
ax2.plot(Ks, fp, "#b03a2e", lw=1.2, ls="--", label=r"$F'(K^*)$")
ax2.axhline(1.0, color="0.55", lw=0.8)
ax2.axvline(2 * K_star, color="0.35", ls="-.", lw=1.0)
ax2.set_ylabel(r"$F'(K^*)$", fontsize=8.5, color="#b03a2e")
ax2.tick_params(labelsize=8, colors="#b03a2e")
ax.set_xscale("log")
ax.set_xlabel(r"carrying capacity  $K$  (kt, log scale)", fontsize=8.5)
ax.set_ylabel("kt yr$^{-1}$", fontsize=8.5)
ax.tick_params(labelsize=8)
ax.legend(fontsize=7.5, loc="center right", frameon=False)
ax.set_title("(b)  but the functionals are", fontsize=9, loc="left")
fig.tight_layout()
fig.savefig(FIG / "fig9_identification.png", bbox_inches="tight")
plt.close(fig)
print("v18: wrote fig8_frontier.png and fig9_identification.png "
      "(fig1-fig7 regenerated unchanged)")
