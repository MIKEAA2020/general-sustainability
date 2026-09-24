#!/usr/bin/env python3
"""
Belief-state safety values, edition 2 — figure and table-data generation.

Recomputes every plotted or tabulated quantity from the audited models in
exact integer/rational arithmetic (the same primitives as
paper2_belief_state_v2_verification.py), asserts the data, writes five
vector figures to figs_bs2/, and prints the tex-ready table data.
Deterministic; matplotlib used only for rendering.

Run: python3 paper2_belief_state_figures.py
"""
import os
from fractions import Fraction as Q
from itertools import product
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figs_bs2")
os.makedirs(OUT, exist_ok=True)
PASS = []
def check(name, cond, detail=""):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else " " + str(detail)))

plt.rcParams.update({"font.size": 7.5, "axes.linewidth": 0.6,
                     "mathtext.fontset": "cm"})
GREEN, RED, BLUE, GRAY = "#2a7f62", "#b04a3a", "#345f8a", "#8a8a8a"

GRID = [Q(n, 10) for n in range(10, 26)]
TOS = [1, 2, 3]

def alpha_vectors_hidden(z0, T, k):
    window = min(k, T)
    vecs = []
    for u in (Q(1), Q(-1)):
        a_minus = Q(1) if all(z0 - u * t >= 1 for t in range(1, window + 1)) else Q(0)
        a_plus = Q(1) if all(z0 + u * t >= 1 for t in range(1, window + 1)) else Q(0)
        vecs.append((a_minus, a_plus))
    b0 = (Q(1, 2), Q(1, 2))
    V = max(a[0] * b0[0] + a[1] * b0[1] for a in vecs)
    return vecs, V

def V_closed(z0, T, k):
    if k <= T:
        return Q(1, 2) * ((1 if z0 - k >= 1 else 0) + (1 if z0 + k >= 1 else 0))
    return Q(1, 2) * (1 + (1 if z0 >= 1 + T else 0))

def V_unres(z0, T, k):
    """Unrestricted sequential blind class: open-loop time-variation within
    the blind window (min(k, T_obs) steps), revelation at T_obs."""
    best = Q(0)
    for seq in product((1, -1), repeat=min(k, T)):
        best = max(best, survived_mass(z0, seq, Q(1, 2)))
    return best

def survived_mass(z0, seq, w):
    m_a, m_b = w, 1 - w
    za, zb = z0, z0
    for u in seq:
        za, zb = za + u, zb - u
        if za < 1:
            m_a = Q(0)
        if zb < 1:
            m_b = Q(0)
    return m_a + m_b

# ---------------- exact data checks ---------------------------------------------
ok1 = all(alpha_vectors_hidden(z, T, k)[1] == V_closed(z, T, k)
          for z in GRID for T in TOS for k in (1, 2, 3, 4))
check("alpha recursion == closed form on all 192 audited combinations",
      ok1)

allvecs = [tuple(alpha_vectors_hidden(z, T, k)[0]) for z in GRID for T in TOS
           for k in (1, 2, 3, 4)]
flat = sorted(v for vs in allvecs for v in vs)
types = {}
for v in flat:
    types[v] = types.get(v, 0) + 1
check("campaign carries 384 alpha-vectors realizing exactly three types",
      len(flat) == 384 and set(types) == {(Q(1), Q(1)), (Q(1), Q(0)),
                                          (Q(0), Q(1))},
      str(types))
TYPE_CENSUS = sorted(((f"{int(a)}|{int(b)}", n) for (a, b), n in types.items()),
                     key=lambda t: (-t[1], t[0]))

ok2 = (V_unres(Q(19, 10), 2, 2) == V_closed(Q(19, 10), 2, 2)
       and V_unres(Q(21, 10), 2, 2) != V_closed(Q(21, 10), 2, 2)
       and all(V_unres(z, T, 1) == V_closed(z, T, 1)
               for z in GRID for T in TOS))
diff_cells = [(z, T, k) for z in GRID for T in TOS for k in (2, 3, 4)
              if V_unres(z, T, k) != V_closed(z, T, k)]
check("class declaration by brute force: differences exactly the 12 timing "
      "cells x k = 2, 3, 4 (36 combinations); coincide at k = 1 and off the "
      "timing cells",
      ok2 and len(diff_cells) == 36
      and all(2 <= z < 1 + T for z, T, k in diff_cells))

# learning deadlines (ported from hidden_parameter_learning_v1)
def run(z0, T_learn, T=40):
    z = z0
    t = 0
    while t < T_learn:
        z -= Q(1, 10)
        if z < 1:
            return False, t
        t += 1
    for th in (-1, 1):
        zp = z0 - Q(1, 10) * T_learn + Q(-1, 10) + th
        if zp < 1:
            return False, t
    return True, t
KERNELS = []
DEADLINES = []
for T_learn in (0, 1, 2, 3, 4):
    K = [z for z in GRID if run(z, T_learn)[0]]
    KERNELS.append(K)
    DEADLINES.append((T_learn, Q(21, 10) + Q(T_learn, 10), K))
check("learning-deadline identity: thresholds 21/10 + T_learn/10 exact for "
      "T_learn = 0..4; kernel sizes 5, 4, 3, 2, 1",
      all(all(run(z, t)[0] == (z >= th) for z in GRID)
          for t, th, _ in DEADLINES)
      and [len(K) for _, _, K in DEADLINES] == [5, 4, 3, 2, 1])

G1 = [(Q(1), Q(0)), (Q(0), Q(1))]
PROBES = [(Q(i, 10), Q(10 - i, 10)) for i in range(11)]
ok5 = all(max(a[0] * b[0] + a[1] * b[1] for a in G1) == max(b[0], b[1])
          for b in PROBES)
check("two-floor instance: Gamma_1 = {(1,0),(0,1)}; V(b) = max(b0, b1) at "
      "all 11 probe beliefs (exact)", ok5)

MASSES = [(s, survived_mass(Q(3, 2), s, Q(3, 10)))
          for s in product((1, -1), repeat=2)]
ok6 = (sorted(m for _, m in MASSES) == [Q(3, 10), Q(3, 10), Q(7, 10), Q(7, 10)]
       and max(m for _, m in MASSES) == Q(7, 10))
check("asymmetric prior (3/2, 2) with w = 3/10: blind two-step masses "
      "{3/10, 3/10, 7/10, 7/10}; V = 7/10; deficit = 3/10 = min mass attained",
      ok6 and Q(1) - max(m for _, m in MASSES) == Q(3, 10))

# ---------------- FIGURE A: closed-form staircase ================================
fig, axes = plt.subplots(1, 3, figsize=(3.4, 1.7), sharey=True,
                         constrained_layout=True)
for axp, T in zip(axes, TOS):
    ks = (1, 2, 3, 4)
    colors = {1: BLUE, 2: "#7a5aa0", 3: GREEN, 4: "#222"}
    for k in ks:
        xs, ys = [], []
        prev = None
        for z in [Q(n, 200) for n in range(200, 501)]:
            v = V_closed(z, T, k)
            if prev is None or v != prev:
                xs.append(float(z)); ys.append(float(v))
                prev = v
        xs.append(2.5); ys.append(ys[-1])
        axp.step(xs, ys, where="post", lw=1.1, color=colors[k],
                 label=f"$k={k}$")
    axp.set_title(f"$T_{{\\mathrm{{obs}}}}={T}$", fontsize=7)
    axp.set_xlabel(r"$z_0$", labelpad=1)
    axp.set_ylim(0.35, 1.15)
    axp.set_yticks([0.5, 1]); axp.set_yticklabels([r"$\frac{1}{2}$", "1"])
    axp.set_xticks([1, 1.5, 2, 2.5])
    for s_ in ("top", "right"):
        axp.spines[s_].set_visible(False)
axes[0].set_ylabel(r"$V_k(b_0)$", labelpad=1)
axes[2].legend(fontsize=5.4, loc="center right", frameon=False,
               handlelength=1.2, bbox_to_anchor=(1.02, 0.5))
fig.savefig(os.path.join(OUT, "fig_staircase.pdf"))
plt.close(fig)

# ---------------- FIGURE B: class-difference map =================================
fig = plt.figure(figsize=(3.4, 1.55))
ax = fig.add_axes([0.09, 0.18, 0.88, 0.74])
for j, T in enumerate(TOS):
    for i in range(16):
        for m, k in enumerate((2, 3, 4)):
            x = i + m / 3.0
            differs = V_unres(GRID[i], T, k) != V_closed(GRID[i], T, k)
            ax.add_patch(Rectangle((x, j - .38), 1 / 3.0, .76,
                                   facecolor=RED if differs else "#e8e2dc",
                                   edgecolor="white", lw=0.3))
ax.set_xlim(-0.05, 16.05); ax.set_ylim(-0.75, 2.85)
ax.set_yticks(range(3)); ax.set_yticklabels(["1", "2", "3"])
ax.set_xticks([0, 5, 10, 15])
ax.set_xticklabels(["1.0", "1.5", "2.0", "2.5"])
ax.set_xlabel(r"$z_0$", labelpad=1); ax.set_ylabel(r"$T_{\mathrm{obs}}$",
                                                   labelpad=1)
for s_ in ("top", "right"):
    ax.spines[s_].set_visible(False)
ax.add_patch(Rectangle((3.4, 2.52), 0.55, 0.30, facecolor=RED,
                       edgecolor="none"))
ax.annotate("hold class below open loop", (4.15, 2.67), fontsize=6,
            va="center")
ax.add_patch(Rectangle((11.6, 2.52), 0.55, 0.30, facecolor="#e8e2dc",
                       edgecolor="none"))
ax.annotate("classes agree", (12.35, 2.67), fontsize=6, va="center")
ax.annotate("three sub-cells per column: $k = 2, 3, 4$", (8, -0.62),
            ha="center", fontsize=5.8, color="#444")
fig.savefig(os.path.join(OUT, "fig_classdiff.pdf"))
plt.close(fig)

# ---------------- FIGURE C: learning deadlines ===================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(3.4, 1.8), width_ratios=[3, 2],
                               constrained_layout=True)
tls = list(range(5))
ths = [float(th) for _, th, _ in DEADLINES]
ax1.plot(tls, ths, "o-", ms=3.5, lw=1.1, color=BLUE)
for t, th, K in DEADLINES:
    ax1.annotate(f"$|K|={len(K)}$", (t, float(th) + 0.06), fontsize=5.6,
                 ha="center", color="#333")
    ax1.axhline(float(th), color=GRAY, lw=0.3, ls=":")
ax1.set_xticks(tls)
ax1.set_xlabel(r"$T_{\mathrm{learn}}$", labelpad=1)
ax1.set_ylabel("threshold on $z_0$", labelpad=1)
ax1.set_ylim(1.9, 2.75)
for s_ in ("top", "right"):
    ax1.spines[s_].set_visible(False)
ax1.annotate(r"$\frac{21}{10} + \frac{T_{\mathrm{learn}}}{10}$", (3.1, 2.05),
             fontsize=7, color=BLUE)
ks_ = [len(K) for _, _, K in DEADLINES]
ax2.bar([t - 0.36 for t in tls], ks_, width=0.55, color=GREEN)
ax2.set_xticks(tls)
ax2.set_xlabel(r"$T_{\mathrm{learn}}$", labelpad=1)
ax2.set_ylabel(r"$|K|$ on the grid", labelpad=1)
ax2.set_ylim(0, 6.2)
for t, n in zip(tls, ks_):
    ax2.annotate(str(n), (t - 0.36, n + 0.12), ha="center", fontsize=6)
for s_ in ("top", "right"):
    ax2.spines[s_].set_visible(False)
fig.savefig(os.path.join(OUT, "fig_deadline.pdf"))
plt.close(fig)

# ---------------- FIGURE D: two-floor piecewise-linear value =====================
fig = plt.figure(figsize=(3.4, 2.1))
ax = fig.add_axes([0.13, 0.15, 0.84, 0.80])
bs = [Q(n, 200) for n in range(0, 201)]
ax.plot([float(b) for b in bs], [float(max(b, 1 - b)) for b in bs],
        lw=1.4, color="#222")
for i, b in enumerate(PROBES):
    mark = "o" if i != 5 else "o"
    fc = RED if i == 5 else GREEN
    ax.plot([float(b[0])], [float(max(b[0], b[1]))], mark, ms=3.2, color=fc)
ax.annotate(r"$V_1(b) = \max(b_0, b_1)$", (0.32, 0.79), fontsize=7)
ax.annotate(r"$\Gamma_1 = \{(1,0),(0,1)\}$:" + "\nattaining alpha-vectors\n"
            r"(bottom coordinate $0$)", (0.40, 0.30), fontsize=6, color=BLUE)
ax.plot([0.5], [0.5], "s", ms=4, color=BLUE)
ax.annotate(r"$b_0 = (\frac{1}{2},\frac{1}{2})$: $V = \frac{1}{2}$,"
            " deficit" + r"$\ = \frac{1}{2}$", (0.53, 0.46), fontsize=6,
            color=BLUE)
ax.set_xlabel(r"$b_0$ (mass on state 0)", labelpad=1)
ax.set_ylabel(r"$V_1(b)$", labelpad=1)
ax.set_xticks([0, 0.5, 1]); ax.set_yticks([0, 0.5, 1])
ax.set_yticklabels(["0", r"$\frac{1}{2}$", "1"])
for s_ in ("top", "right"):
    ax.spines[s_].set_visible(False)
fig.savefig(os.path.join(OUT, "fig_twofloor.pdf"))
plt.close(fig)

# ---------------- FIGURE E: asymmetric-prior survived masses =====================
fig = plt.figure(figsize=(3.4, 1.9))
ax = fig.add_axes([0.12, 0.17, 0.86, 0.78])
labels = ["$+\\!+$", "$+\\!-$", "$-\\!+$", "$-\\!-$"]
vals = [float(m) for _, m in MASSES]
cols = [RED if m == Q(3, 10) else GREEN for _, m in MASSES]
ax.bar(range(4), vals, width=0.55, color=cols)
ax.axhline(0.7, color="#222", lw=0.8, ls="--")
ax.annotate(r"$V_2(b_0) = \frac{7}{10}$", (2.62, 0.72), fontsize=7)
ax.annotate(r"deficit $\frac{3}{10} =$ min mass", (1.85, 0.16), fontsize=6.4,
            color="#333")
ax.set_xticks(range(4)); ax.set_xticklabels(labels)
ax.set_xlabel(r"blind two-step sequence $u_1 u_2$ at $(z_0, T_{\mathrm{obs}}) "
              r"= (\frac{3}{2}, 2)$, $w = \frac{3}{10}$", labelpad=1)
ax.set_ylabel("survived mass", labelpad=1)
ax.set_ylim(0, 0.85)
for s_ in ("top", "right"):
    ax.spines[s_].set_visible(False)
fig.savefig(os.path.join(OUT, "fig_masses.pdf"))
plt.close(fig)


# ---------------- tex-ready table data -------------------------------------------
print("\n--- CAMPAIGN TABLE (16 rows x 12 columns, values 1/2 or 1) ---")
hdr = "z0   " + " ".join(f"T={T} k={k}" for T in TOS for k in (1, 2, 3, 4))
print(hdr)
for z in GRID:
    row = []
    for T in TOS:
        for k in (1, 2, 3, 4):
            v = V_closed(z, T, k)
            row.append("1" if v == 1 else "1/2")
    print(f"{float(z):.1f}  " + " ".join(f"{v:>6}" for v in row))
print("\n--- TYPE CENSUS ---")
for t, n in TYPE_CENSUS:
    print(t, n)
print("\n--- DEADLINES ---")
for t, th, K in DEADLINES:
    print(f"T_learn={t} thr={th} |K|={len(K)} K={[str(z) for z in K]}")
print(f"\nfigures: {sum(1 for _, o in PASS if o)}/{len(PASS)} checks pass")
raise SystemExit(0 if all(o for _, o in PASS) else 1)
