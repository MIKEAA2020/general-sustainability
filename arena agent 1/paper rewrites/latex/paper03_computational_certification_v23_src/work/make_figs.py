"""Figures for paper03 v23 (recompute-then-assert: every plotted exact value is
recomputed in rational arithmetic and asserted against the printed value)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from fractions import Fraction as Q
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from p03_core import *

OUT = os.path.join(os.path.dirname(__file__), "..", "figs")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 9, "axes.titlesize": 9.5, "legend.fontsize": 7.8,
                     "mathtext.fontset": "cm", "figure.dpi": 150})


def crit_curve(legs, j, npts=600):
    """exact piecewise-quadratic critical coordinate sampled for plotting"""
    ts, cs = [], []
    c, w, t = PPOS, Q(1), Q(0)
    sched = legs + [(T - sum(d for d, _ in legs), (Q(0), Q(0)))]
    for dur, u in sched:
        if dur <= 0:
            continue
        a = dot(n[j], u)
        N = max(2, int(npts * float(dur / T)))
        for k in range(N + 1):
            s = dur * k / N
            ts.append(float(t + s))
            cs.append(float(c + w * s + a * s * s / 2))
        c, w, t = c + w * dur + a * dur * dur / 2, w + a * dur, t + dur
    return ts, cs


def brake_to_rest(legs, j):
    """append full braking -n_j until the critical velocity reaches zero, then hold"""
    w = Q(1)
    for dur, u in legs:
        w += dot(n[j], u) * dur
    return legs + [(w, (-n[j][0], -n[j][1]))]


# ------------------------------------------------------------------ Figure 1
tau = TAU
pol = {}
pol["single"] = brake_to_rest([], 0)                                   # brake from 0
pol["pair12"] = brake_to_rest([(tau, (Q(-2, 5), Q(-4, 5)))], 0)        # branch 1 of {1,2}
pol["pair23"] = brake_to_rest([(tau, (Q(1), Q(0)))], 1)                # branch 2 of {2,3}
pol["hold"] = brake_to_rest([(tau, (Q(0), Q(0)))], 0)                  # failed: hold then brake
pol["midleg"] = brake_to_rest([(tau, (Q(1), Q(0))), (tau, (Q(3, 5) * n[1][0] * -1, Q(3, 5) * n[1][1] * -1))], 1)
peaks = {k: critical_peak(v, 0 if k in ("single", "pair12", "hold") else 1)[0] for k, v in pol.items()}
assert peaks["single"] == Q(93, 50), peaks["single"]
assert peaks["pair12"] == Q(12345, 6250)
assert peaks["pair23"] == Q(2419, 1250)
assert peaks["hold"] == Q(103, 50)
assert peaks["midleg"] == Q(2501, 1250)

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.axvspan(0, float(tau), color="0.92", zorder=0)
ax.axhline(2, color="k", lw=1.0)
styles = [("single", 0, "full information: brake from $t=0$, peak $93/50$", "tab:green", "-"),
          ("pair12", 0, r"pair $\{1,2\}$: shared braking at $2/5$, peak $12345/6250$", "tab:blue", "-"),
          ("pair23", 1, r"pair $\{2,3\}$: shared braking at $3/5$, peak $2419/1250$", "tab:cyan", "-"),
          ("hold", 0, r"blind hold $u=0$ then full braking: $103/50>2$", "tab:red", "--"),
          ("midleg", 1, r"$\{2,3\}$ with a $-\frac{3}{5}n_j$ leg: $2501/1250>2$ at $t=29/25$", "tab:orange", "--")]
for key, j, lab, col, ls in styles:
    ts, cs = crit_curve(pol[key], j)
    ax.plot(ts, cs, color=col, ls=ls, lw=1.4, label=lab)
ax.text(float(tau) / 2, 1.37, "blind\nwindow", ha="center", va="bottom", fontsize=7.5, color="0.35")
ax.set_xlim(0, float(T)); ax.set_ylim(1.35, 2.2)
ax.set_xlabel(r"time $t$"); ax.set_ylabel(r"critical coordinate $n_j^{\top}p_j(t)$")
ax.legend(loc="lower right", frameon=False)
ax.set_title(r"Audited policies on the three-branch instance at $\tau=1/5$ (safety ceiling 2)")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig1_trajectories.pdf")); fig.savefig(os.path.join(OUT, "fig1_trajectories.png"))
plt.close(fig)

# ------------------------------------------------------------------ Figure 2: mesh law and sandwich
hs = [Q(1, 5), Q(1, 15), Q(1, 10), Q(1, 20), Q(1, 50), Q(1, 100)]
hs = sorted(hs)
L = Q(11, 5)
rho = [mesh_law(uniform_mesh(h)) for h in hs]
assert [mesh_law(uniform_mesh(h)) for h in (Q(1, 10), Q(1, 15), Q(1, 100))] == [Q(3, 100), Q(1, 25), Q(57, 1000)]
ub = [r + T * h / 4 + L * h / 2 for r, h in zip(rho, hs)]
assert ub[hs.index(Q(1, 10))] == Q(17, 100) and ub[hs.index(Q(1, 5))] == Q(7, 25) and ub[hs.index(Q(1, 100))] == Q(71, 1000)
fig, ax = plt.subplots(figsize=(6.4, 3.3))
hh = [float(h) for h in hs]
ax.plot(hh, [float(r) for r in rho], "o-", color="tab:blue", lw=1.4, label=r"finite value $\rho(h)=3/50-Th/4$ (exact; solver agrees to $\leq 4.2\times10^{-17}$)")
ax.plot(hh, [float(u) for u in ub], "s--", color="tab:gray", lw=1.2, label=r"certified upper bound $\rho(h)+\bar e+Lh_t$, $h_t=h/2$ (Theorem 3.2(i))")
ax.axhline(float(Q(3, 50)), color="k", lw=1.0, label=r"continuous value $J(T)=3/50$")
ax.axhline(0, color="0.6", lw=0.8)
ax.axvline(float(Q(3, 340)), color="tab:red", lw=1.0, ls=":", label=r"a-priori halting resolution $h<3/340$ (Theorem 3.2(iii))")
ax.set_xscale("log"); ax.set_xlabel(r"uniform aligned mesh width $h$"); ax.set_ylabel("value")
ax.set_ylim(-0.02, 0.32)
ax.legend(loc="upper left", frameon=False)
ax.set_title("Mesh study: the finite value converges to the continuous value from below")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig2_meshlaw.pdf")); fig.savefig(os.path.join(OUT, "fig2_meshlaw.png"))
plt.close(fig)

# ------------------------------------------------------------------ Figure 3: ladder
import numpy as np
r12 = (15 - math.sqrt(183)) / 6
r23 = (10 - math.sqrt(58)) / 6
lo, hi = quad_root_bracket(-Q(2, 5) * Q(3, 5) / 2, Q(3, 5), -Q(7, 50), Q(0), Q(1, 2))
assert abs(float(lo) - r12) < 1e-12 and abs(float(hi) - r12) < 1e-12
lo, hi = quad_root_bracket(-Q(3, 5) * Q(2, 5) / 2, Q(2, 5), -Q(7, 50), Q(0), Q(1, 2))
assert abs(float(lo) - r23) < 1e-12 and abs(float(hi) - r23) < 1e-12
fig, ax = plt.subplots(figsize=(6.4, 3.4))
taus = np.linspace(0, 0.5, 400)
ax.plot(taus, taus - 0.14, color="tab:red", lw=1.6, label=r"triple $\{1,2,3\}$: $\Gamma(\tau)=\tau-7/50$")
m12 = taus <= 1 / 3
ax.plot(taus[m12], [float(pair_gamma(Q(2, 5), Q(x).limit_denominator(10**6))) for x in taus[m12]], color="tab:blue", lw=1.6,
        label=r"pairs $\{1,2\},\{1,3\}$: $\Gamma_B(\tau)$ with $t^*=2/5$")
m23 = taus <= 1 / 2
ax.plot(taus[m23], [float(pair_gamma(Q(3, 5), Q(x).limit_denominator(10**6))) for x in taus[m23]], color="tab:cyan", lw=1.6,
        label=r"pair $\{2,3\}$: $\Gamma_B(\tau)$ with $t^*=3/5$")
ax.axhline(0, color="k", lw=0.9)
for x, lab, col in [(0.14, r"$7/50$", "tab:red"), (r12, r"$\frac{15-\sqrt{183}}{6}$", "tab:blue"), (r23, r"$\frac{10-\sqrt{58}}{6}$", "tab:cyan")]:
    ax.axvline(x, color=col, lw=0.9, ls=":")
    ax.text(x, -0.185, lab, ha="center", va="bottom", fontsize=8, color=col)
ax.axvline(0.2, color="0.4", lw=0.9, ls="--")
ax.text(0.203, -0.14, r"audited delay $\tau=1/5$", fontsize=7.5, color="0.3", rotation=90, va="bottom")
ax.set_xlim(0, 0.5); ax.set_ylim(-0.2, 0.12)
ax.set_xlabel(r"observation delay $\tau$"); ax.set_ylabel("certificate margin")
ax.legend(loc="lower right", frameon=False)
ax.set_title("The shared-authority ladder: exact delay thresholds by belief (horizon $T=6/5$)")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig3_ladder.pdf")); fig.savefig(os.path.join(OUT, "fig3_ladder.png"))
plt.close(fig)

# ------------------------------------------------------------------ Figure 4: pricing an observer installed at tau_1
fs = frozenset
h = Q(1, 100)
mesh = uniform_mesh(h)
tau1s = [Q(k, 100) for k in range(0, 21)]
rows = []
for tau1 in tau1s:
    if tau1 == 0:
        info = [(Q(0), [fs({0}), fs({1, 2})]), (TAU, [fs({0}), fs({1}), fs({2})])]
    else:
        info = [(Q(0), [fs({0, 1, 2})]), (tau1, [fs({0}), fs({1, 2})]), (TAU, [fs({0}), fs({1}), fs({2})])]
    lp = build_lp(mesh, info)
    sol = solve_highs(lp)
    rows.append((tau1, sol[0] if sol else float("nan")))
gam = lambda t1: Q(3, 50) - Q(3, 8) * ((Q(6, 5) - t1) ** 2 - 1)
assert gam(Q(1, 5)) == Q(3, 50) and gam(Q(0)) == -Q(21, 200)
t1star = (6 - math.sqrt(29)) / 5
fig, ax = plt.subplots(figsize=(6.4, 3.3))
xx = np.linspace(0, 0.2, 200)
ax.plot(xx, [float(gam(Q(x).limit_denominator(10**6))) for x in xx], color="tab:red", lw=1.5,
        label=r"eroded triple certificate $\Gamma(\tau_1)=\frac{3}{50}-\frac{3}{8}\left[(\frac{6}{5}-\tau_1)^2-1\right]$ (exact)")
ax.plot([float(a) for a, _ in rows], [b for _, b in rows], "o", ms=3.5, color="tab:blue",
        label=r"finite program $\rho$ at $h=1/100$ (HiGHS; lower bound on $J$)")
ax.axhline(0, color="k", lw=0.9)
ax.axvline(float(Q(3, 25)), color="tab:green", lw=1.0, ls="--")
ax.axvline(t1star, color="tab:red", lw=1.0, ls=":")
ax.axvspan(float(Q(3, 25)), t1star, color="tab:olive", alpha=0.25)
ax.text(0.117, -0.1, r"threshold $\tau_1^*\in[\frac{3}{25},\frac{6-\sqrt{29}}{5}]$", fontsize=7.8, ha="right", va="center")
ax.text(0.06, 0.02, "viable with the\nexplicit schedule", fontsize=7.5, color="tab:green", ha="center")
ax.text(0.165, -0.04, "certified\nnonviable", fontsize=7.5, color="tab:red", ha="center")
ax.set_xlim(0, 0.2); ax.set_ylim(-0.12, 0.08)
ax.set_xlabel(r"installation time $\tau_1$ of the observer $\{1\}\,|\,\{2,3\}$ (full revelation at $\tau=1/5$)")
ax.set_ylabel("certificate margin / finite value")
ax.legend(loc="upper left", frameon=False)
ax.set_title("Pricing an observer: when does telling branch 1 apart restore viability?")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig4_observer.pdf")); fig.savefig(os.path.join(OUT, "fig4_observer.png"))
plt.close(fig)
with open(os.path.join(os.path.dirname(__file__), "observer_sweep.tsv"), "w") as f:
    f.write("tau1\trho_h100\tfixed_weight_dual\n")
    for a, b in rows:
        f.write(f"{a}\t{b:.9f}\t{float(gam(a)):.9f}\n")
print("figures written;", [(str(a), round(b, 6)) for a, b in rows])
