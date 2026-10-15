"""Figure 4 of v63: the substitutability ladder (Theorem 4) on the gap-region diagonal z=(x<1, s, s).
Left: the critical floor s*(theta) solving the master equation, with the exact algebraic rungs marked.
Right: the critical elasticity sigma*(s) = 1/(1-theta*(s)) on the diagonal, with the paper's exact brackets overlaid."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from fractions import Fraction as Fr

def master(s, th):
    # accept iff g>=2 (th>0), s^2>=2 (th=0), g<=2 (th<0); return signed 'accept margin' positive when accepted
    if th > 0:  return (s-1)**th + (s+1)**th - 2
    if th == 0: return s*s - 2
    return 2 - ((s-1)**th + (s+1)**th)

def crit_floor(th, lo=1.0+1e-9, hi=2.0-1e-12):
    # monotone in s on (1,2): accept region is s >= s*(th)
    for _ in range(200):
        mid = 0.5*(lo+hi)
        if master(mid, th) >= 0: hi = mid
        else: lo = mid
    return hi

def crit_theta(s):
    # theta*(s): largest theta that rejects... accepted rungs form a prefix (theta large accepts); find theta with master=0
    if s*s > 2:   # theta* < 0
        lo, hi = -400.0, 0.0
        for _ in range(200):
            mid = 0.5*(lo+hi)
            if master(s, mid) >= 0: hi = mid     # accepted at mid -> boundary below
            else: lo = mid
        return hi
    elif s*s < 2:
        lo, hi = 0.0, 1.0
        for _ in range(200):
            mid = 0.5*(lo+hi)
            if master(s, mid) >= 0: hi = mid
            else: lo = mid
        return hi
    return 0.0

thetas = np.concatenate([np.linspace(-60, -12, 200), np.linspace(-12, -0.001, 600), [0.0], np.linspace(0.001, 1.0, 300)])
floors = np.array([crit_floor(t) for t in thetas])
sig = 1.0/(1.0-np.minimum(thetas, 0.999))
fig, axs = plt.subplots(1, 2, figsize=(10.6, 4.4))
ax = axs[0]
ax.plot(sig, floors, "k-", lw=1.6)
ax.set_xscale("log"); ax.set_xlabel(r"elasticity of substitution $\sigma=1/(1-\theta)$ (log scale)")
ax.set_ylabel(r"critical floor $s^*(\theta)$ on the diagonal $(s,s)$")
ax.axhline(2.0, color="0.4", ls=":", lw=1); ax.text(1.4e-2, 2.01, r"typed boundary $s=2$ (Leontief, $\sigma\to0$)", fontsize=8.5, va="bottom")
ax.axhline(1.0, color="0.4", ls=":", lw=1)
rungs = [(1.0, 1.0, r"$1$"), (0.5, 1.25, r"$5/4$"), (0.0, np.sqrt(2), r"$\sqrt{2}$"), (-1.0, (1+np.sqrt(5))/2, r"$\varphi$"), (-2.0, np.sqrt(3), r"$\sqrt{3}$")]
for th, fl, lab in rungs:
    sg = 1/(1-th) if th < 1 else 1.0
    if th == 1.0: sg = 1e3
    ax.plot(sg, fl, "o", color="#c62828", ms=6)
    txt = (lab + (r"  ($\theta=%g$)" % th)) if th < 1 else (lab + r"  ($\theta=1$, $\sigma=\infty$)")
    ax.annotate(txt, (sg, fl), xytext=(7, -12) if th < 1 else (-95, 8), textcoords="offset points", fontsize=8.5)
ax.set_xlim(1.2e-2, 1.6e3); ax.set_ylim(0.95, 2.05)
ax.set_title("(a) the exact ladder of critical floors", fontsize=10.5)
ax.fill_between(sig, floors, 2.0, color="#f4b6b6", alpha=0.6)
ax.text(9, 1.72, "gap states falsely certified\nby the $\\sigma$-aggregator", fontsize=8.5, color="#8e0000")
ax.text(0.03, 1.2, "rejected: the rung\nexposes the breach", fontsize=8.5, color="0.3")
# right panel
ss = np.linspace(1.001, 1.999, 800)
sigstar = np.array([1/(1-crit_theta(s)) for s in ss])
ax = axs[1]
ax.plot(ss, sigstar, "k-", lw=1.6); ax.set_yscale("log")
ax.set_xlabel(r"diagonal gap state $(x<1,\,s,\,s)$: floor margin $s$"); ax.set_ylabel(r"critical elasticity $\sigma^*(s)$ (log scale)")
brackets = [(Fr(6,5), 2, 3), (Fr(5,4), 2, 2), (Fr(13,10), 1, 2), (Fr(3,2), Fr(1,2), 1), (Fr(13,8), Fr(1,3), Fr(1,2)), (Fr(9,5), Fr(1,5), Fr(1,4)), (Fr(39,20), Fr(1,17), Fr(1,13))]
for s, lo, hi in brackets:
    ax.plot([float(s), float(s)], [float(lo), float(hi)], color="#1565c0", lw=5, alpha=0.75, solid_capstyle="butt")
ax.plot([], [], color="#1565c0", lw=5, alpha=0.75, label="exact rational brackets (Table 4)")
ax.plot([], [], "k-", lw=1.6, label=r"master-equation root $\sigma^*(s)$")
ax.axvline(np.sqrt(2), color="0.5", ls=":", lw=1); ax.text(np.sqrt(2)+0.015, 1.9, r"$s=\sqrt{2}$: $\sigma^*=1$" "\n" r"(geometric mean)", fontsize=8.5)
ax.axhline(1.0, color="0.5", ls=":", lw=1)
ax.set_xlim(1.0, 2.0); ax.set_ylim(0.03, 100); ax.legend(fontsize=8.5, frameon=False, loc="upper right")
ax.set_title(r"(b) the critical elasticity along the diagonal", fontsize=10.5)
ax.text(1.02, 0.042, r"$\sigma^*\to\infty$ as $s\to1^+$;  $\sigma^*\to0$ as $s\to2^-$", fontsize=8.5)
fig.tight_layout()
fig.savefig("../figs/fig_substitutability_ladder.pdf"); fig.savefig("../figs/fig_substitutability_ladder.png", dpi=170)
# print checks
for th, fl, lab in rungs: print(th, crit_floor(th) if th<1 else 1.0, fl)
for s, lo, hi in brackets: print(s, float(lo), float(hi), 1/(1-crit_theta(float(s))))
