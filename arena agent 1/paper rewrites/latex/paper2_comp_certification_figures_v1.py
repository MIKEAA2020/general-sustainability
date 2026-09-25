#!/usr/bin/env python3
"""
Figures for the computational-certification paper — script-generated with
every plotted feature recomputed in exact rational arithmetic and asserted
against the paper's printed values (recompute-then-assert; a figure is
shipped only if every assertion passes).

figs_comp2/fig_trajectories.pdf — the critical position n_j^T p(t) on
[0, 6/5] for the five audited policies of the three-branch instance
(tau = 1/5): the full-information singleton brake (peak 93/50), the pair
{1,2} shared-braking policy (12345/6250), the pair {2,3} policy (2419/1250),
the falsified blind-window hold (103/50), and the falsified {2,3} mid-leg
variant (2501/1250 at t = 29/25); floor 2 drawn; blind window shaded.

figs_comp2/fig_hierarchy.pdf — the margin family Gamma_a(tau) =
tau - 7/50 - (a - 1)/2 for a in {1, 3/2, 2} (post-revelation authority
dilation), with the exact thresholds tau_max(a) in {7/50, 39/100, 16/25},
the pair delay thresholds (15 - sqrt(183))/6 and (10 - sqrt(58)/6), and
the zero line.
"""
import os
os.environ.setdefault("SOURCE_DATE_EPOCH", "1758825600")  # pin embedded PDF metadata to the round's pinned build epoch
from fractions import Fraction as Q
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figs_comp2")
os.makedirs(OUT, exist_ok=True)
PASS = []


def check(name, ok):
    PASS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


TAU = Q(1, 5)
T = Q(6, 5)
PPOS = Q(34, 25)


def crit_traj(a_blind, brake_from, a_leg=None):
    """Critical coordinate n_j^T p(t) for: blind acceleration a_blind on
    [0, tau]; optional constant a_leg on [tau, 2 tau]; full braking -1 from
    `brake_from` to rest; hold at the peak. Returns (times, values, peak)."""
    ts, vs = [], []
    t = Q(0)
    v = Q(1)
    p = PPOS
    while t < T:
        ts.append(t)
        vs.append(p)
        if brake_from == 0 or t >= T:
            dt = min(Q(1, 200), v if v > 0 else T - t, T - t)
            p_new = p + v * dt - dt * dt / 2
            v = v - dt
        elif t < TAU:
            dt = min(Q(1, 200), TAU - t)
            p_new = p + v * dt + a_blind * dt * dt / 2
            v = v + a_blind * dt
        elif a_leg is not None and t < 2 * TAU:
            dt = min(Q(1, 200), 2 * TAU - t)
            p_new = p + v * dt + a_leg * dt * dt / 2
            v = v + a_leg * dt
        elif v > 0:
            dt = min(Q(1, 200), v, T - t)
            p_new = p + v * dt - dt * dt / 2
            v = v - dt
        else:
            dt = min(Q(1, 200), T - t)
            p_new = p
        p = p_new
        t = t + dt
    ts.append(T)
    vs.append(p)
    return ts, vs, max(vs)


# policy 1: full information (brake from t = 0)
ts1, vs1, pk1 = crit_traj(Q(0), Q(0))
check("full-information peak = 93/50", pk1 == Q(93, 50))
# policy 2: pair {1,2} (blind u = -(n1+n2), a = -2/5, brake from tau)
ts2, vs2, pk2 = crit_traj(Q(-2, 5), TAU)
check("pair {1,2} peak = 12345/6250", pk2 == Q(12345, 6250))
# policy 3: pair {2,3} (blind u = n1, a = -3/5, brake from tau)
ts3, vs3, pk3 = crit_traj(Q(-3, 5), TAU)
check("pair {2,3} peak = 2419/1250", pk3 == Q(2419, 1250))
# policy 4: falsified blind hold on {1,2} with full braking after
ts4, vs4, pk4 = crit_traj(Q(0), TAU)
check("falsified blind hold peaks 103/50 > 2", pk4 == Q(103, 50) and pk4 > 2)
# policy 5: falsified {2,3} variant (blind -3/5, leg -3/5 on [tau, 2 tau])
ts5, vs5, pk5 = crit_traj(Q(-3, 5), 2 * TAU, a_leg=Q(-3, 5))
check("falsified {2,3} leg variant peaks 2501/1250 > 2", pk5 == Q(2501, 1250) and pk5 > 2)
# pair rest times (slack times) for annotations
v_tau_12 = Q(1) + Q(-2, 5) * TAU
check("pair {1,2} window exit velocity 23/25; {2,3} 22/25",
      v_tau_12 == Q(23, 25) and Q(1) + Q(-3, 5) * TAU == Q(22, 25))

f = float
fig, ax = plt.subplots(figsize=(7.0, 4.2))
ax.axhline(2, color="black", lw=1.2)
ax.text(1.208, 2.008, "floor 2", fontsize=8)
ax.axvspan(0, f(TAU), color="0.88", zorder=0)
ax.text(f(TAU) / 2, 2.12, "blind\nwindow", fontsize=7, ha="center")
series = [
    (ts1, vs1, "full information (singleton): peak $\\frac{93}{50}$", "tab:green", "-"),
    (ts2, vs2, "pair $\\{1,2\\}$ shared braking: peak $\\frac{12345}{6250}$", "tab:blue", "-"),
    (ts3, vs3, "pair $\\{2,3\\}$ shared braking: peak $\\frac{2419}{1250}$", "tab:cyan", "-"),
    (ts4, vs4, "falsified: blind hold then brake: $\\frac{103}{50} > 2$", "tab:red", "--"),
    (ts5, vs5, "falsified $\\{2,3\\}$ mid-leg: $\\frac{2501}{1250} > 2$ at $t = \\frac{29}{25}$",
     "tab:orange", ":"),
]
for ts, vs, lab, c, ls in series:
    ax.plot([f(x) for x in ts], [f(y) for y in vs], label=lab, color=c, ls=ls, lw=1.4)
ax.annotate("$\\frac{103}{50}$", (f(Q(7, 10)), f(Q(103, 50)) + 0.012), fontsize=8,
            color="tab:red", ha="center")
ax.annotate("$\\frac{12345}{6250}$", (f(Q(17, 20)), f(Q(12345, 6250)) - 0.033), fontsize=8,
            color="tab:blue", ha="center")
ax.annotate("$\\frac{2419}{1250}$", (f(Q(11, 10)), f(Q(2419, 1250)) - 0.035), fontsize=8,
            color="tab:cyan", ha="center")
ax.annotate("$\\frac{2501}{1250}$", (f(Q(29, 25)) - 0.005, f(Q(2501, 1250)) + 0.014),
            fontsize=8, color="tab:orange", ha="right")
ax.annotate("$\\frac{93}{50}$", (0.35, f(Q(93, 50)) + 0.008), fontsize=8, color="tab:green")
ax.set_xlim(0, 1.25)
ax.set_ylim(1.30, 2.16)
ax.set_xlabel("$t$")
ax.set_ylabel("critical position $n_j^{\\top} p_j(t)$")
ax.set_title("The three-branch instance at $\\tau = \\frac{1}{5}$: the policies and their exact peaks")
ax.legend(fontsize=6.5, loc="lower right", framealpha=0.9)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig_trajectories.pdf"))
plt.close(fig)
check("fig_trajectories.pdf written", os.path.exists(os.path.join(OUT, "fig_trajectories.pdf")))

# hierarchy figure
import math
def Gam(a, tau):
    return tau - Q(7, 50) - (a - 1) / 2

TH = [Q(7, 50), Q(39, 100), Q(16, 25)]
check("thresholds 7/50, 39/100, 16/25 solve Gamma_a = 0 at a = 1, 3/2, 2",
      Gam(Q(1), TH[0]) == 0 and Gam(Q(3, 2), TH[1]) == 0 and Gam(Q(2), TH[2]) == 0)
T12 = (15 - math.sqrt(183)) / 6
T23 = (10 - math.sqrt(58)) / 6
check("pair thresholds (15-sqrt183)/6 ~ 0.2453 and (10-sqrt58)/6 ~ 0.3971 in range",
      0.24 < T12 < 0.25 and 0.39 < T23 < 0.40)

fig, ax = plt.subplots(figsize=(7.0, 4.0))
grid = [Q(i, 400) for i in range(0, 281)]  # tau in [0, 0.7]
for a, c, lab in ((Q(1), "tab:blue", "$a = 1$ (audited hexagon)"),
                  (Q(3, 2), "tab:purple", "$a = \\frac{3}{2}$"),
                  (Q(2), "tab:red", "$a = 2$")):
    ax.plot([f(t) for t in grid], [f(Gam(a, t)) for t in grid], color=c, label=lab, lw=1.5)
ax.axhline(0, color="black", lw=1)
for th, a, c, lab in ((TH[0], Q(1), "tab:blue", "$\\frac{7}{50}$"),
                      (TH[1], Q(3, 2), "tab:purple", "$\\frac{39}{100}$"),
                      (TH[2], Q(2), "tab:red", "$\\frac{16}{25}$")):
    ax.plot([f(th)], [0], "o", color=c, ms=5)
    ax.text(f(th), -0.045, lab, fontsize=8, ha="center", color=c)
ax.axvline(T12, color="tab:cyan", ls=":", lw=1.2)
ax.text(T12 + 0.006, 0.30, "pairs $\\{1,2\\},\\{1,3\\}$:\n$\\frac{15-\\sqrt{183}}{6}$",
        fontsize=7, color="tab:cyan")
ax.axvline(T23, color="tab:green", ls=":", lw=1.2)
ax.text(T23 + 0.006, 0.16, "pair $\\{2,3\\}$:\n$\\frac{10-\\sqrt{58}}{6}$",
        fontsize=7, color="tab:green")
ax.text(0.30, 0.50, "viable above 0, obstructed below:\n"
        "$\\Gamma_a(\\tau) = \\tau - \\frac{7}{50} - \\frac{a-1}{2}$", fontsize=8)
ax.set_xlim(0, 0.7)
ax.set_ylim(-0.12, 0.60)
ax.set_xlabel("$\\tau$ (observation time)")
ax.set_ylabel("$\\Gamma_a(\\tau)$")
ax.set_title("The delay hierarchy under authority dilation: rate one in $\\tau$, rate one half in $a$")
ax.legend(fontsize=7.5, loc="upper left")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig_hierarchy.pdf"))
plt.close(fig)
check("fig_hierarchy.pdf written", os.path.exists(os.path.join(OUT, "fig_hierarchy.pdf")))

n = sum(PASS)
print(f"\ncomp figures: {n}/{len(PASS)} assertions pass")
raise SystemExit(0 if n == len(PASS) else 1)
