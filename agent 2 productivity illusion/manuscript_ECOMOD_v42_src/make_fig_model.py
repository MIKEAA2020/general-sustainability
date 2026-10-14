"""Figure 1 of ECOMOD v42: model dynamics of the two-land model.
(a) frozen-demand demonstration run (E=0.825; A_f0=0.6, A_c0=1.5, q0=0.9, A_tot=2.5);
(b) frozen-demand equilibrium branch B_eq(A_c) with the demand ceiling and the typed floor;
(c) capital-drawdown demand threshold P0 vs initial capital A_c0 (endogenous demand; Table 2 values).
Recompute-then-assert: every plotted model number is regenerated from twoland_fixed.simulate
and checked against the manuscript's stated values before the file is written."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import twoland_fixed as tf

p = tf.FixPara(rho_c=0.08, b_f0=0.85, b_c=0.05, b_Gc=0.80, alpha=0.03, eta_f=0.05, e=0.55, r=0.02, eta=0.05,
               tau_g=20.0, tau_p=25.0, A_tot=2.5, deltab=1.0, t_wave=40.0, kappa_w=0.1, mu=0.06, tau_conv=1.0)
E = 0.825
r = tf.simulate(p, T=400.0, dt=0.05, A_c0=1.5, A_f0=0.6, q0=0.9, E_fixed=E)
best, B, Ac, Af = tf.longest_illusion(p, r)
t = np.arange(len(B)) * r["dt"]
win = best[0] * r["dt"]
# --- assertions against the manuscript (v41 'Demonstration' paragraph) ---
assert abs(B[0] - 0.594) < 2e-3 and abs(B[best[2]+1] - 0.825) < 2e-3
assert abs(Ac[0] - 1.500) < 1e-9 and abs(Ac[best[2]+1] - 0.808) < 2e-3
assert abs(Af[0] - 0.600) < 1e-9 and abs(Af[best[2]+1] - 0.923) < 2e-3
assert 148 <= win <= 152, win
assert r["maxcon"] < 1e-12

k = p.mu / (p.mu + p.eta_f)
slope = p.b_f0 * k - p.b_c
B_eq = lambda A: p.b_f0 * k * p.A_tot - A * slope
E_ceil = B_eq(p.Ac_min)
assert abs(E_ceil - 1.138) < 1e-3, E_ceil
Es = [0.70, 0.90, 1.00, 1.10, 1.13]
Acs = [(p.b_f0 * k * p.A_tot - e) / slope for e in Es]
for a, ref in zip(Acs, [1.110, 0.626, 0.385, 0.143, 0.070]):
    assert abs(a - ref) < 1.5e-3, (a, ref)

Ac0s = [0.40, 0.70, 1.00, 1.18]; P0s = [2.41, 2.70, 2.98, 3.14]   # Table 2 (dt = 0.05, T = 1000 yr)

fig = plt.figure(figsize=(9.0, 7.4))
gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.0], hspace=0.38, wspace=0.28)
axs = [fig.add_subplot(gs[0, :]), fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])]
# (a)
ax = axs[0]
m = t <= 60
ax.axvspan(0, win, color="#fff3b0", alpha=0.7, lw=0)
ax.plot(t[m], B[m], color="#c0392b", lw=2.2, label=r"biocapacity $B$")
ax.axhline(E, color="#c0392b", ls=":", lw=1.2, label=r"frozen demand $E=0.825$")
ax.plot(t[m], Ac[m], color="#1f618d", lw=2.2, label=r"capital land $A_c$")
ax.plot(t[m], Af[m], color="#239b56", lw=2.0, label=r"fast land $A_f$")
ax.plot(t[m], r["Ar"][m], color="#7f8c8d", lw=1.4, ls="--", label=r"reserve $A_r$")
ax.set_xlim(0, 60); ax.set_ylim(0, 1.6)
ax.set_xlabel("time (yr)"); ax.set_ylabel("ha  or  gha yr$^{-1}$")
ax.set_title("(a) Composition mask at frozen demand", fontsize=10.5, loc="left")
ax.text(59, 1.49, r"$\dot B>0$ and $\dot A_c<0$ for %.0f yr" % win + "\n(shown: first 60 yr)", fontsize=8.5, ha="right", va="top")
ax.legend(fontsize=8.5, loc="lower right", frameon=False, ncol=2)
# (b)
ax = axs[1]
A = np.linspace(0, 2.4, 200)
ax.plot(A, B_eq(A), color="k", lw=2.0, label=r"$B_{eq}(A_c)$ (no-conversion face)")
ax.scatter(Acs, Es, color="#c0392b", zorder=5, s=22, label=r"verified $A_c^*(E)$")
ax.axvline(p.Ac_min, color="#7f8c8d", ls="--", lw=1.2)
ax.axhline(E_ceil, color="#1f618d", ls=":", lw=1.4)
ax.text(0.09, E_ceil + 0.02, r"$E_{ceil}=B_{eq}(A_c^{\min})\approx%.3f$" % E_ceil, fontsize=8.5, color="#1f618d")
ax.text(p.Ac_min + 0.05, 0.32, r"typed floor $A_c^{\min}=0.05$", fontsize=8.5, color="#555")
ax.fill_between([0, 2.4], E_ceil, 1.35, color="#f5b7b1", alpha=0.45, lw=0)
ax.text(1.25, 1.24, "no interior equilibrium:\ncapital book driven to the floor", fontsize=8.5, ha="center")
ax.set_xlim(0, 2.4); ax.set_ylim(0.15, 1.35)
ax.set_xlabel(r"capital land $A_c$ (ha)"); ax.set_ylabel(r"frozen demand $E$ (gha yr$^{-1}$)")
ax.set_title("(b) Monotone branch: floor collision, no fold", fontsize=10.5, loc="left")
ax.legend(fontsize=8, loc="center right", bbox_to_anchor=(1.0, 0.62), frameon=False)
# (c) drawdown depth vs initial demand (endogenous demand), from si_drawdown_depth.csv
import csv
rows=list(csv.DictReader(open("../si_drawdown_depth.csv")))
ax = axs[2]
cols={"0.4":"#aed6f1","0.7":"#5dade2","1.0":"#2e86c1","1.18":"#1b4f72"}
for a0 in ["0.4","0.7","1.0","1.18"]:
    sel=[r for r in rows if float(r["A_c0"])==float(a0)]
    x=[float(r["P0"]) for r in sel]; y=[float(r["minAc_chi0.10"]) for r in sel]
    ax.plot(x,y,"-",color=cols[a0],lw=2.0,label=r"$A_{c0}=%s$"%a0)
ax.axhline(p.Ac_min,color="#7f8c8d",ls="--",lw=1.2)
ax.text(1.05,p.Ac_min+0.025,r"typed floor $A_c^{\min}$",fontsize=8,color="#555")
for a0,P0 in zip(Ac0s,P0s):
    ax.plot([P0],[p.Ac_min],marker="v",color="#c0392b",ms=5,zorder=6)
ax.text(3.05,0.30,"floor-contact\nthresholds\n(Table 2)",fontsize=7.5,color="#c0392b",ha="center")
ax.annotate("",xy=(2.98,0.065),xytext=(3.05,0.27),arrowprops=dict(arrowstyle="->",color="#c0392b",lw=0.8))
ax.set_xlim(1.0,4.0); ax.set_ylim(0,1.25)
ax.set_xlabel(r"initial population $P_0$ (demand $E_0=eP_0$)"); ax.set_ylabel(r"minimum capital land $\min_t A_c$ (ha)")
ax.set_title("(c) Drawdown depth vs demand", fontsize=10.5, loc="left")
ax.legend(fontsize=7.5, frameon=False, loc="upper right", title="initial capital", title_fontsize=7.5)
for a in axs:
    a.spines[["top", "right"]].set_visible(False)
fig.subplots_adjust(left=0.08, right=0.98, top=0.95, bottom=0.08)
fig.savefig("../fig1_model_dynamics.pdf"); fig.savefig("../fig1_model_dynamics.png", dpi=170)
print("fig3 written; window=%.1f yr, E_ceil=%.4f" % (win, E_ceil))
