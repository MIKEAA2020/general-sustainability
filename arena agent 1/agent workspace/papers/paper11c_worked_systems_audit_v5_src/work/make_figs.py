#!/usr/bin/env python3
"""Figures for paper11c v5, generated from the core and results.json."""
import json, os, sys, pathlib, collections
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ws_core import *
root = pathlib.Path(__file__).resolve().parent.parent
R = json.load(open(root / 'work' / 'results.json'))
FIG = root / 'figs'
FIG.mkdir(exist_ok=True)
plt.rcParams.update({'font.size': 9, 'axes.titlesize': 10, 'pdf.fonttype': 42})
BLUE, RED, GREY, GREEN, ORANGE = '#1f4e8c', '#b03a2e', '#8c8c8c', '#2e7d32', '#e67e22'

# ------------------------------------------------------------------ fig 1
fig, axes = plt.subplots(1, 3, figsize=(11, 3.6))
ax = axes[0]
for x in SAFE:
    col = GREY if x == CORNER else 'white'
    ax.add_patch(Rectangle((x[0] - 0.4, x[1] - 0.4), 0.8, 0.8, fc=col, ec='black', lw=0.8))
    ax.text(x[0], x[1], f"{x[0]}{x[1]}", ha='center', va='center', fontsize=9)
for x in CORNER_FREE:
    for u, ls, col, rad in ((1, '-', BLUE, 0.25), (2, '--', RED, 0.25)):
        y = step(x, u)
        if y in SAFESET:
            ax.annotate('', xy=y, xytext=x,
                        arrowprops=dict(arrowstyle='-|>', color=col, ls=ls, lw=1.0, shrinkA=14, shrinkB=14,
                                        connectionstyle=f'arc3,rad={rad}', mutation_scale=9))
ax.set_xlim(0.3, 3.7); ax.set_ylim(0.3, 3.7); ax.set_aspect('equal')
ax.set_xlabel('$z_1$   (the aggregate $z_1+z_2$ is constant on anti-diagonals)'); ax.set_ylabel('$z_2$')
ax.set_xticks([1, 2, 3]); ax.set_yticks([1, 2, 3])
ax.set_title('safe states and instruments 1 (solid), 2 (dashed)')
ax = axes[1]
pos = {(1, 2): (0, 1), (1, 3): (0, 0), (2, 1): (1.4, 1), (3, 1): (1.4, 0),
       (2, 2): (2.6, 1.1), (2, 3): (3.3, 1.1), (3, 2): (2.6, -0.1), (3, 3): (3.3, -0.1)}
for a, b in incompatibility_edges(CORNER_FREE):
    ax.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]], color='black', lw=1.0, zorder=1)
for x, (px, py) in pos.items():
    crit = x in {(1, 2), (1, 3), (2, 1), (3, 1)}
    ax.scatter([px], [py], s=420, c=[RED if crit else GREEN], edgecolors='black', zorder=2)
    ax.text(px, py, f"{x[0]}{x[1]}", ha='center', va='center', color='white', fontsize=8, zorder=3)
ax.text(0, 1.45, 'R={1}', ha='center', fontsize=7); ax.text(1.4, 1.45, 'R={2}', ha='center', fontsize=7)
ax.text(2.95, 1.55, 'R={1,2} (isolated)', ha='center', fontsize=7)
ax.set_xlim(-0.6, 3.9); ax.set_ylim(-0.6, 1.8); ax.axis('off')
ax.set_title('incompatibility graph $G^*$ ($K_{2,2}$ + 4 isolated)')
ax = axes[2]
for i, a in enumerate((1, 2)):
    S = [x for x in SAFE if alternation_safe(x, a)]
    for x in SAFE:
        col = (BLUE if a == 1 else RED) if x in S else 'white'
        ax.add_patch(Rectangle((x[0] - 0.4 + 4.2 * i, x[1] - 0.4), 0.8, 0.8, fc=col, ec='black', lw=0.6, alpha=0.85 if x in S else 1))
        ax.text(x[0] + 4.2 * i, x[1], f"{x[0]}{x[1]}", ha='center', va='center', fontsize=8,
                color='white' if x in S else 'black')
    ax.text(2 + 4.2 * i, 3.75, f'phase {a}', ha='center', fontsize=8)
ax.set_xlim(0.3, 8.0); ax.set_ylim(0.3, 4.1); ax.set_aspect('equal'); ax.axis('off')
ax.set_title('alternation-safe states $\\Phi_1$ (left), $\\Phi_2$ (right)')
fig.tight_layout()
fig.savefig(FIG / 'fig1_system.pdf'); plt.close(fig)

# ------------------------------------------------------------------ fig 2: lattice
K = R['kernels']
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8), gridspec_kw={'width_ratios': [1.25, 1]})
ax = axes[0]
nodes = {'full': (2, 2, f"full\n{K['audited']['full']['universe']}"),
         'codex': (3, 1, f"codex ($\\ell$)\n{K['audited']['codex']['universe']}"),
         'agg': (1, 1, f"aggregate\n{K['audited']['agg']['universe']}"),
         'inst': (2, 0, f"institutional ($\\ell$) = blind\n{K['audited']['inst']['universe']}")}
for a, b in [('inst', 'agg'), ('inst', 'codex'), ('agg', 'full'), ('codex', 'full')]:
    ax.annotate('', xy=nodes[b][:2], xytext=nodes[a][:2], arrowprops=dict(arrowstyle='-|>', color='black', lw=1, shrinkA=22, shrinkB=22))
for k, (x, y, t) in nodes.items():
    ax.text(x, y, t, ha='center', va='center', fontsize=8.5, bbox=dict(boxstyle='round,pad=0.4', fc='#eef3fa', ec=BLUE))
ax.text(1.5, 1.5, '$\\supsetneq$ strict', fontsize=7, color=GREY, rotation=45, ha='center')
ax.text(2.1, 1.0, 'incomparable', fontsize=7, color=RED, ha='center')
ax.set_xlim(0.3, 3.8); ax.set_ylim(-0.5, 2.5); ax.axis('off')
ax.set_title('shared ledger: the four classes (viable beliefs of 255)')
ax = axes[1]
nodes2 = {'full': (2, 2.2, f"full\n255"),
          'codexp': (3.2, 1.3, f"codex ($\\pi$)\n{K['branch']['codex']['universe']}"),
          'aggp': (0.8, 1.3, f"aggregate = institutional ($\\pi$)\n{K['branch']['agg']['universe']}"),
          'codexl': (3.2, 0.2, f"codex ($\\ell$)\n{K['audited']['codex']['universe']}"),
          'instl': (0.8, 0.2, f"institutional ($\\ell$)\n{K['audited']['inst']['universe']}")}
for a, b in [('aggp', 'full'), ('codexp', 'full'), ('instl', 'aggp'), ('codexl', 'full'), ('instl', 'codexl')]:
    ax.annotate('', xy=nodes2[b][:2], xytext=nodes2[a][:2], arrowprops=dict(arrowstyle='-|>', color='black', lw=1, shrinkA=22, shrinkB=22))
for k, (x, y, t) in nodes2.items():
    ax.text(x, y, t, ha='center', va='center', fontsize=8.5, bbox=dict(boxstyle='round,pad=0.4', fc='#fbeeea' if '$\\ell$' in t else '#eef7ee', ec=RED if '$\\ell$' in t else GREEN))
ax.text(3.95, 0.75, 'incomparable:\n13|31 vs 12|21', fontsize=7, color=RED, ha='center', va='center')
ax.set_xlim(0.0, 4.5); ax.set_ylim(-0.3, 2.7); ax.axis('off')
ax.set_title('private register ($\\pi$) against shared ledger ($\\ell$)')
fig.tight_layout()
fig.savefig(FIG / 'fig2_lattice.pdf'); plt.close(fig)

# ------------------------------------------------------------------ fig 3: census
D = R['design']
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
ax = axes[0]
ks = sorted(int(k) for k in D['by_cells'])
tot = [D['by_cells'][str(k)]['partitions'] for k in ks]
ad = [D['by_cells'][str(k)]['adequate'] for k in ks]
ax.bar(ks, ad, color=GREEN, label='dynamically adequate (kernel 255)')
ax.bar(ks, [t - a for t, a in zip(tot, ad)], bottom=ad, color=GREY, label='not adequate')
for k, t, a in zip(ks, tot, ad):
    ax.text(k, t + 25, f"{a}/{t}", ha='center', fontsize=7)
ax.set_xlabel('number of cells'); ax.set_ylabel('partitions'); ax.legend(frameon=False, fontsize=8)
ax.set_title('4,140 partitions of the eight viable states')
ax = axes[1]
sizes = sorted(int(k) for k in D['kernel_sizes'])
cnt = [D['kernel_sizes'][str(s)] for s in sizes]
cols = [GREEN if s == 255 else (RED if s == 111 else (ORANGE if s == 143 else BLUE)) for s in sizes]
ax.bar(range(len(sizes)), cnt, color=cols)
ax.set_xticks(range(len(sizes))); ax.set_xticklabels(sizes, rotation=90, fontsize=7)
ax.set_xlabel('kernel size (viable beliefs)'); ax.set_ylabel('partitions')
ax.set_yscale('log'); ax.set_ylim(5, 6000)
ax.text(0, cnt[0] * 1.3, 'blind', ha='center', fontsize=7, color=RED)
ax.text(sizes.index(143), D['kernel_sizes']['143'] * 1.3, 'aggregate', ha='center', fontsize=7, color=ORANGE)
ax.text(len(sizes) - 1, cnt[-1] * 1.3, 'adequate', ha='center', fontsize=7, color=GREEN)
ax.set_title(f"kernel sizes: {len(sizes)} values, {D['distinct_kernels']} distinct kernels")
fig.tight_layout()
fig.savefig(FIG / 'fig3_census.pdf'); plt.close(fig)

# ------------------------------------------------------------------ fig 4: timing
tg = timing_grid()
fig, axes = plt.subplots(1, 2, figsize=(10, 3.4))
import numpy as np
zs = [float(z) for z in tg['grid']]
for ax, idx, title, nv in ((axes[0], 0, 'free switching, unit damage', tg['viable_free']),
                           (axes[1], 1, 'alternation, damages (1, 1/2)', tg['viable_alt'])):
    M = np.array([[1 if row[j][idx] else 0 for (z, s, row) in tg['rows']] for j in range(3)])
    ax.imshow(M, aspect='auto', cmap=matplotlib.colors.ListedColormap(['#f2f2f2', BLUE]), origin='lower',
              extent=(zs[0] - 0.05, zs[-1] + 0.05, 0.5, 3.5))
    ax.set_yticks([1, 2, 3]); ax.set_ylabel('review period $T$'); ax.set_xlabel('initial level $z_0$')
    ax.set_title(f"{title}: {nv} viable cells")
    if idx == 0:
        for (z, T) in [(2, 1), (3, 2), (4, 3)]:
            ax.scatter([z], [T], marker='x', color=RED, s=40, zorder=3)
        ax.text(1.05, 3.2, 'x: strict form $z_0-1>T$ fails at (2,1), (3,2), (4,3)', color=RED, fontsize=7)
fig.tight_layout()
fig.savefig(FIG / 'fig4_timing.pdf'); plt.close(fig)

# ------------------------------------------------------------------ fig 5: continuous
fig, axes = plt.subplots(1, 2, figsize=(10, 3.9))
ax = axes[0]
Ys = np.linspace(3, 7.5, 200)
cs = [float(cap1(Q(y).limit_denominator(1000)) + cap2(Q(y).limit_denominator(1000))) for y in Ys]
ax.plot(Ys, cs, color=BLUE, label='$c_1(Y)+c_2(Y)$')
ax.axhline(2, color='black', lw=0.8, label='demand 2')
ax.axvline(27 / 5, color=RED, ls='--', lw=0.8)
ax.text(27 / 5 + 0.05, 2.25, '$Y^* = 27/5$', color=RED, fontsize=8)
Ym = np.linspace(27 / 5, 7.5, 50)
ax.fill_between(Ym, 2, [float(cap1(Q(y).limit_denominator(1000)) + cap2(Q(y).limit_denominator(1000))) for y in Ym], color=RED, alpha=0.15)
ax.text(6.55, 2.04, 'deficiency $2\\mu(Y)$', color=RED, fontsize=8)
ax.scatter([6], [47 / 25], color=RED, s=20); ax.text(4.9, 1.72, 'Y=6: cap sum 47/25, margin 3/50', fontsize=7)
ax.set_xlabel('pressure $Y$'); ax.set_ylabel('cap sum'); ax.legend(frameon=False, fontsize=8, loc='lower left')
ax.set_title('benchmark fibre: crossover and margin law')
ax = axes[1]
us = np.linspace(0, 1, 200)
r1 = 2 / 5 - us; r2 = us - 3 / 5; r2f = us - 1 / 5
ax.plot(us, r1, color=BLUE, label='$r_1 = 2/5 - u$'); ax.plot(us, r2, color=RED, label='$r_2 = u - 3/5$')
ax.plot(us, np.minimum(r1, r2), color='black', lw=2, label='$\\min_j r_j$')
ax.plot(us, r2f, color=RED, ls=':', label='feasible contrast $u - 1/5$')
ax.scatter([0.5], [-0.1], color='black', zorder=3); ax.text(0.52, -0.08, 'saddle: value $-1/10$', fontsize=8)
ax.scatter([0.3], [0.1], color=GREY, zorder=3); ax.text(0.32, 0.13, 'value $+1/10$', fontsize=8, color=GREY)
ax.axhline(0, color=GREY, lw=0.5)
ax.set_xlabel('$u$'); ax.set_ylabel('floor slack'); ax.set_ylim(-0.7, 0.5); ax.legend(frameon=False, fontsize=7, loc='upper center', bbox_to_anchor=(0.5, -0.22), ncol=2)
ax.set_title('static duality on the two-floor instance')
fig.tight_layout()
fig.savefig(FIG / 'fig5_continuous.pdf'); plt.close(fig)
print('figures written')
