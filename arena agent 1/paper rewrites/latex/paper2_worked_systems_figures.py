#!/usr/bin/env python3
"""
Worked-systems audit, edition 4 — figure and table-data generation.

Recomputes every plotted or tabulated quantity from the shared audit
system's primitives in exact integer/rational arithmetic (the same
primitives as paper2_worked_systems_v4_verification.py), asserts the
data, writes five vector figures to figs_ws4/, and prints the tex-ready
table data. Deterministic; matplotlib used only for rendering.

Run: python3 paper2_worked_systems_figures.py
"""
import os
from fractions import Fraction as Q
from itertools import product
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figs_ws4")
os.makedirs(OUT, exist_ok=True)
PASS = []
def check(name, cond, detail=""):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else " " + str(detail)))

plt.rcParams.update({"font.size": 7.5, "axes.linewidth": 0.6,
                     "mathtext.fontset": "cm"})
GREEN, RED, BLUE, GRAY = "#2a7f62", "#b04a3a", "#345f8a", "#8a8a8a"

# ---------------- shared audit system (ported primitives) ----------------------
CAP = 3
def step(x, u):
    z1, z2 = x
    if u == 0:
        return (max(0, z1 - 1), max(0, z2 - 1))
    return (max(0, min(CAP, z1 + 1 - (0 if u == 1 else 2))),
            max(0, min(CAP, z2 + 1 - (0 if u == 2 else 2))))
STATES = [(a, b) for a in range(4) for b in range(4)]
Vset = frozenset(x for x in STATES if x[0] >= 1 and x[1] >= 1)
pairs = sorted(frozenset({x, y}) for x in Vset for y in Vset if x < y)
H = 12
def parts_of(B, info):
    p = {}
    for x in B:
        p.setdefault(info(x), set()).add(x)
    return p
def win(B, info, h, last=None, alt=False):
    if h == 0:
        return B <= Vset
    cells = parts_of(B, info)
    acts = []
    for c in cells.values():
        cu = [u for u in (1, 2) if all(step(x, u) in Vset for x in c)]
        if not cu:
            return False
        if alt:
            cu = [u for u in cu if u != last]
            if not cu:
                return False
        acts.append(cu)
    for choice in product(*acts):
        choice_last = choice[0]
        succ = set()
        for c, u in zip(cells.values(), choice):
            succ |= {step(x, u) for x in c}
        ps = [frozenset(p) for p in parts_of(succ, info).values()]
        if all(win(p, info, h - 1, choice_last, alt) for p in ps):
            return True
    return False
def verd(B, info, alt=False):
    return win(B, info, H, None, alt) and win(B, info, H - 2, None, alt)

SH = {(1,1): "11", (1,2): "12", (1,3): "13", (2,1): "21", (2,2): "22",
      (2,3): "23", (3,1): "31", (3,2): "32", (3,3): "33"}
def pr(B):
    return "|".join(SH[x] for x in sorted(B))

agg, full = lambda x: x[0] + x[1], lambda x: x
K_inst = [B for B in pairs if verd(B, agg, alt=True)]
K_agg  = [B for B in pairs if verd(B, agg)]
K_cod  = [B for B in pairs if verd(B, full, alt=True)]
K_full = [B for B in pairs if verd(B, full)]
K_i, K_a, K_c, K_f = (frozenset(K_inst), frozenset(K_agg),
                      frozenset(K_cod), frozenset(K_full))
missing_join = K_f - (K_a | K_c)
check("kernels 24/26/25/28; meet of middles = inst setwise; kernel union "
      "is one pair short of full: exactly 12|21",
      (len(K_inst), len(K_agg), len(K_cod), len(K_full)) == (24, 26, 25, 28)
      and K_a & K_c == K_i
      and missing_join == {frozenset({(1, 2), (2, 1)})})

# ---------------- decentralized (ported from institutional_observation_v2) -----
def law_traj_ok(B, law1, law2, cap=512):
    cur, seen = frozenset(B), set()
    while True:
        if not (cur <= Vset):
            return False
        if cur in seen:
            return True
        seen.add(cur)
        if len(seen) > cap:
            return False
        nxt = set()
        for x in cur:
            u = law1[x[0]] if law1[x[0]] == law2[x[1]] else 0
            nxt.add(step(x, u))
        cur = frozenset(nxt)
LAW_PAIRS = [(l1, l2) for l1 in
             [dict(zip(range(4), t)) for t in product((1, 2), repeat=4)]
             for l2 in
             [dict(zip(range(4), t)) for t in product((1, 2), repeat=4)]]
assert len(LAW_PAIRS) == 256
def dec_viable(B):
    return any(law_traj_ok(B, l1, l2) for l1, l2 in LAW_PAIRS)
K_dec = [B for B in pairs if dec_viable(B)]
AUDITED = frozenset({(1, 2), (2, 1)})
DEC16 = sorted((tuple(l1.values()), tuple(l2.values()))
               for l1, l2 in LAW_PAIRS if law_traj_ok(AUDITED, l1, l2))
check("decentralized kernel 12 of 36; exactly 16 law pairs sustain "
      "the audited belief 12|21", len(K_dec) == 12 and len(DEC16) == 16)

# ---------------- timing grid ----------------------------------------------------------------
GRID = [Q(n, 10) for n in range(10, 26)]
TOS = [1, 2, 3]
import math
TIMING = [(float(z), int(math.floor(float(z) - 1)),
           tuple(int(z >= 1 + T) for T in TOS)) for z in GRID]
strict_bad = [(z, T) for z in GRID for T in TOS
              if ((z - 1) > T) != (z >= 1 + T)]
check("timing grid: boundary-inclusive zero mismatches; strict fails "
      "exactly at (2.0, 1)",
      all(((z - 1) >= T) == (z >= 1 + T) for z in GRID for T in TOS)
      and strict_bad == [(Q(2), 1)])

# ---------------- census ----------------------------------------------------------------------
R = lambda x: [u for u in (1, 2) if step(x, u) in Vset]
TARGET = [(1, 2), (2, 1), (2, 2), (3, 1)]
def partitions(S):
    if not S:
        yield []
        return
    first, rest = S[0], S[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield p + [[first]]
ALLP = sorted(tuple(tuple(sorted(F)) for F in P) for P in partitions(TARGET))
def inter_R(F):
    s = set(R(F[0]))
    for x in F[1:]:
        s &= set(R(x))
    return s
CENSUS = [(P, all(inter_R(F) for F in P)) for P in ALLP]
check("census: 15 partitions, 7 adequate, two adequate two-cell partitions",
      len(ALLP) == 15 and sum(a for _, a in CENSUS) == 7
      and sum(1 for P, a in CENSUS if a and len(P) == 2) == 2)

# ---------------- benchmark and drift ---------------------------------------------------------
def cap1(Y): return Q(3, 2) - (Y - 2) / 10
def cap2(Y): return Q(59, 50) - (Y - 2) / 10
Ssum = lambda Y: cap1(Y) + cap2(Y)
Ystar = Q(4) + (Ssum(Q(4)) - Q(2)) * 5
BENCH = [(Y, cap1(Y), cap2(Y), Ssum(Y)) for Y in
         (Q(4), Q(9, 2), Q(5), Q(11, 2), Q(27, 5), Q(6))]
g = lambda s: s * s
drift_u = lambda s: g(s + Q(1, 10)) - g(s)
DRIFT = [(s, drift_u(s), drift_u(s + Q(1, 10)) - drift_u(s)) for s in
         (Q(1), Q(5, 4), Q(3, 2), Q(7, 4), Q(2))]
check("benchmark Y* = 27/5, Y=6 sum 47/25; drift min 21/100 at s = 1",
      Ystar == Q(27, 5) and Ssum(Q(6)) == Q(47, 25)
      and DRIFT[0][1] == Q(21, 100)
      and all(d >= Q(21, 100) for _, d, _ in DRIFT))

# ---------------- static duality (ported from minimax_dual_certificates_v1) ----
U = [Q(n, 100) for n in range(0, 101)]
psi_obs = [lambda u: Q(2, 5) - u, lambda u: u - Q(3, 5)]
psi_fea = [lambda u: Q(2, 5) - u, lambda u: u - Q(1, 5)]
lhs = lambda psi: max(min(p(u) for p in psi) for u in U)
dualv = lambda psi: min(max(l * psi[0](u) + (1 - l) * psi[1](u) for u in U)
                        for l in [Q(n, 100) for n in range(0, 101)])
l = Q(1, 2)
E = [l * psi_obs[0](u) + (1 - l) * psi_obs[1](u) for u in U]
rows = [{Q(0): Q(-1), Q(1): Q(1)}, {Q(0): Q(1), Q(1): Q(-1)}]
lhs_c = max(min(r[u] for r in rows) for u in [Q(0), Q(1)])
rhs_c = min(max((1 - m) * rows[0][u] + m * rows[1][u] for u in [Q(0), Q(1)])
            for m in [Q(n, 100) for n in range(0, 101)])
check("static duality: obstructed -1/10 both sides, constant Farkas mix, "
      "contrast +1/10, nonconvex gap -1 vs 0",
      lhs(psi_obs) == Q(-1, 10) and dualv(psi_obs) == Q(-1, 10)
      and all(e == Q(-1, 10) for e in E) and lhs(psi_fea) == Q(1, 10)
      and lhs_c == Q(-1) and rhs_c == Q(0))

# ================= FIGURE 1: timing grid ========================================================
fig = plt.figure(figsize=(3.4, 1.75))
ax = fig.add_axes([0.10, 0.20, 0.88, 0.66])
for i, (z, sig, vs) in enumerate(TIMING):
    for j, T in enumerate(TOS):
        ax.add_patch(Rectangle((i - .5, j - .38), 1, .76,
                               facecolor=GREEN if vs[j] else "#e8e2dc",
                               edgecolor="white", lw=0.4))
ax.set_xlim(-0.6, 15.6); ax.set_ylim(-0.75, 2.85)
ax.set_yticks(range(3)); ax.set_yticklabels(["1", "2", "3"])
ax.set_xticks(range(0, 16, 3))
ax.set_xticklabels([f"{TIMING[i][0]:.1f}" for i in range(0, 16, 3)])
ax.set_xlabel(r"$z_0$", labelpad=1); ax.set_ylabel(r"$T_{\mathrm{obs}}$",
                                                 labelpad=1)
for s_ in ("top", "right"):
    ax.spines[s_].set_visible(False)
ax.add_patch(Rectangle((5.4, 2.52), 0.55, 0.30, facecolor=GREEN,
                       edgecolor="none", clip_on=False))
ax.annotate("viable at the deadline", (6.15, 2.67), fontsize=6,
            va="center")
ax.add_patch(Rectangle((12.4, 2.52), 0.55, 0.30, facecolor="#e8e2dc",
                       edgecolor="none", clip_on=False))
ax.annotate("not viable", (13.15, 2.67), fontsize=6, va="center")
i2b = GRID.index(Q(2))
ax.add_patch(Circle((i2b, 0), 0.60, fill=False, edgecolor=RED, lw=1.2))
ax.annotate("strict form fails here only", (i2b, -0.92), ha="center",
            color=RED, fontsize=5.8, va="top")
ax.set_ylim(-1.35, 2.85)
fig.savefig(os.path.join(OUT, "fig_timing.pdf"))
plt.close(fig)

# ================= FIGURE 2: kernel Boolean product =============================================
fig = plt.figure(figsize=(3.4, 2.35))
ax = fig.add_axes([0, 0, 1, 1]); ax.axis("off")
ax.set_xlim(0, 10); ax.set_ylim(-0.4, 10.1)
box = lambda cx, cy, lab: ax.annotate(lab, (cx, cy), ha="center",
                                      va="center", fontsize=7.4,
                                      bbox=dict(boxstyle="round,pad=0.5",
                                                fc="#f2f0ec", ec=GRAY,
                                                lw=0.7))
box(2.5, 7.4, "$\\mathcal{W}_{\\mathrm{full\\text{-}codex}}$, $|\\cdot| = 25$")
box(7.5, 7.4, "$\\mathcal{W}_{\\mathrm{full}}$, $|\\cdot| = 28$")
box(2.5, 3.0, "$\\mathcal{W}_{\\mathrm{inst}}$, $|\\cdot| = 24$")
box(7.5, 3.0, "$\\mathcal{W}_{\\mathrm{agg}}$, $|\\cdot| = 26$")
arr = lambda a, b: ax.add_patch(FancyArrowPatch(
    a, b, arrowstyle="-|>", mutation_scale=8, lw=0.8, color=GRAY,
    shrinkA=2, shrinkB=2))
arr((6.0, 7.4), (4.05, 7.4))
arr((7.5, 6.35), (7.5, 4.05))
arr((2.5, 6.35), (2.5, 4.05))
arr((6.0, 3.0), (4.05, 3.0))
ax.annotate("no-repeat protocol", (5.0, 8.15), ha="center", fontsize=6.2,
            color="#444")
ax.annotate("aggregation $c(x) = z_1 + z_2$", (9.5, 5.2), fontsize=6.0,
            color="#444", rotation=90, va="center", ha="center")
ax.annotate("join cell $=$ the full-information class;", (5.0, 9.65),
            ha="center", fontsize=6.2, color=BLUE)
ax.annotate("its kernel: the $C(8,2) = 28$ corner-free pairs", (5.0, 9.05),
            ha="center", fontsize=6.2, color=BLUE)
ax.annotate("meet of the middle cells", (5.0, 1.55), ha="center",
            fontsize=6.2, color=BLUE)
ax.annotate("$= \\mathcal{W}_{\\mathrm{inst}}$ setwise", (5.0, 0.85),
            ha="center", fontsize=6.2, color=BLUE)
fig.savefig(os.path.join(OUT, "fig_kernels.pdf"))
plt.close(fig)

# ================= FIGURE 3: the 15-partition census ============================================
fig, axes = plt.subplots(3, 5, figsize=(3.4, 2.35), constrained_layout=True)
SH4 = [SH[x] for x in TARGET]
for axp, (P, adm) in zip(axes.flat, CENSUS):
    axp.set_xlim(-0.6, 3.6); axp.set_ylim(-0.35, 2.3); axp.axis("off")
    for fi, F in enumerate(P):
        idx = sorted(TARGET.index(x) for x in F)
        y = 0.45 * (fi + 1)
        axp.plot([min(idx), max(idx)], [y, y], lw=2.4,
                 color=GREEN if adm else RED, solid_capstyle="round")
    for i, s in enumerate(SH4):
        axp.annotate(s, (i, -0.28), ha="center", fontsize=5.6, color="#333")
    axp.annotate("+" if adm else "$\\times$", (3.45, 2.1), ha="right",
                 fontsize=6.4, color=GREEN if adm else RED)
fig.savefig(os.path.join(OUT, "fig_census.pdf"))
plt.close(fig)

# ================= FIGURE 4: benchmark caps =====================================================
fig, ax = plt.subplots(figsize=(3.4, 2.4), constrained_layout=True)
Ys = [Q(n, 20) for n in range(70, 131)]
ax.plot([float(y) for y in Ys], [float(cap1(y)) for y in Ys], lw=1.0,
        color=BLUE, label=r"$\mathrm{cap}_1(Y)$")
ax.plot([float(y) for y in Ys], [float(cap2(y)) for y in Ys], lw=1.0,
        color="#7a5aa0", label=r"$\mathrm{cap}_2(Y)$")
ax.plot([float(y) for y in Ys], [float(Ssum(y)) for y in Ys], lw=1.5,
        color="#222", label=r"$\mathrm{cap}_1+\mathrm{cap}_2$")
ax.axhline(2, color=GREEN, lw=0.9, ls="--")
ax.axvline(float(Q(27, 5)), color=GREEN, lw=0.9, ls="--")
ax.plot([5], [float(Ssum(5))], "o", ms=4, color=GREEN)
ax.plot([6], [float(Ssum(6))], "o", ms=4, color=RED)
ax.annotate("$Y^{*} = 27/5$", (float(Q(27, 5)) + 0.06, 4.55), fontsize=7,
            color=GREEN, rotation=90, va="top")
ax.annotate("$Y{=}5$: $52/25$\nviable", (5.05, float(Ssum(5)) - 0.12),
            fontsize=6.4, color=GREEN, va="top")
ax.annotate("$Y{=}6$: $47/25 < 2$\nobstructed, margin $3/50$",
            (5.62, float(Ssum(6)) + 0.34), fontsize=6.4, color=RED)
ax.set_xlabel(r"$Y$"); ax.set_ylabel("cap sum")
ax.set_ylim(1.3, 5.2)
ax.legend(fontsize=6, loc="upper right", frameon=False)
fig.savefig(os.path.join(OUT, "fig_benchmark.pdf"))
plt.close(fig)

# ================= FIGURE 5: static duality =====================================================
fig, ax = plt.subplots(figsize=(3.4, 2.4), constrained_layout=True)
us = [Q(n, 100) for n in range(0, 101)]
ax.plot([float(u) for u in us], [float(psi_obs[0](u)) for u in us], lw=1.0,
        color=BLUE, label=r"$\psi_1(u) = 2/5 - u$")
ax.plot([float(u) for u in us], [float(psi_obs[1](u)) for u in us], lw=1.0,
        color="#7a5aa0", label=r"$\psi_2(u) = u - 3/5$")
ax.plot([float(u) for u in us],
        [float(min(psi_obs[0](u), psi_obs[1](u))) for u in us], lw=1.5,
        color="#222", label=r"$\min_u \psi$")
ax.axhline(0, color=GRAY, lw=0.6)
ax.plot([0.5], [-0.1], "o", ms=4, color=RED)
ax.axhline(-0.1, color=RED, lw=0.9, ls="--")
ax.annotate(r"$-\,\frac{1}{10}$: max--min $=$ min--max;"
            r" Farkas $(\frac{1}{2},\frac{1}{2})$ constant",
            (0.03, -0.16), fontsize=6.2, color=RED, va="top")
ax.set_xlabel(r"$u \in [0,1]$"); ax.set_ylabel("drift rows")
ax.legend(fontsize=6, loc="upper right", frameon=False)
fig.savefig(os.path.join(OUT, "fig_duality.pdf"))
plt.close(fig)

# ---------------- tex-ready table data ----------------------------------------------------------
print("\n--- MASTER TABLE (36 pairs x 5 kernels) ---")
for B in pairs:
    print(pr(B),
          "I" if B in K_inst else ".", "A" if B in K_agg else ".",
          "C" if B in K_cod else ".", "F" if B in K_full else ".",
          "D" if B in K_dec else ".")
print("\n--- DEC16 law pairs (l1; l2 votes on z=0,1,2,3) ---")
for l1, l2 in DEC16:
    print("".join(map(str, l1)) + "|" + "".join(map(str, l2)))
print("\n--- CENSUS rows ---")
for P, adm in CENSUS:
    print(" ; ".join("|".join(SH[x] for x in F) for F in P),
          "ADEQ" if adm else "no",
          "[" + " ".join("".join(str(u) for u in sorted(inter_R(F))) or "-" for F in P) + "]")
print(f"\nfigures: {sum(1 for _, o in PASS if o)}/{len(PASS)} checks pass")
raise SystemExit(0 if all(o for _, o in PASS) else 1)
