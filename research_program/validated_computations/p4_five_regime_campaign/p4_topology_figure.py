#!/usr/bin/env python3
"""P4 five-regime topology figure — drawn ONLY from the campaign's
committed records (p4_branch_*.csv, p4_basin_archive.csv,
p4_campaign_results.json), per the pre-registration's figure-ungating
rule (section 6): every displayed feature is traceable to a committed
record; no legacy number is drawn.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).parent


def load_branch():
    rows = list(csv.DictReader(open(HERE / 'p4_branch_archive.csv')))
    out = []
    for r in rows:
        try:
            out.append(dict(
                family=r['family'], method=r['method'],
                tau=float(r['tau']), T=float(r['T']),
                ptp=float(r['N_ptp']),
                mu1=float(r['mu1_mod']) if r['mu1_mod'] else None,
                mu1re=float(r['mu1_re']) if r['mu1_re'] else None,
                ok=(r['newton_ok'] == 'True')))
        except (ValueError, TypeError):
            continue
    return [r for r in out if r['ok'] or r['method'].startswith('basin')]


def load_basin():
    rows = list(csv.DictReader(open(HERE / 'p4_basin_archive.csv')))
    return [r for r in rows if abs(float(r['dt']) - 0.02) < 1e-12]


def stability(r):
    if r['mu1re'] is None:
        return 'none'
    if abs(r['mu1re'] - 1.0) < 2e-3:
        return 'edge'
    return 'stable' if r['mu1re'] < 1.0 else 'unstable'


def main():
    branch = load_branch()
    basin = load_basin()
    res = json.loads((HERE / 'p4_campaign_results.json').read_text())
    bt = res['boundary_table']

    COL = dict(stable='#7a2010', unstable='#3b3b3b', edge='#c0762c',
               none='#9a9a9a')
    fig, axes = plt.subplots(2, 2, figsize=(11.5, 8.2))

    # ---- (a) lower bifurcation diagram -------------------------------
    ax = axes[0, 0]
    for fam, label in (('small_lower', 'small branch (from $\\tau_-$)'),
                       ('large_lower', 'large-amplitude arm')):
        pts = [r for r in branch if r['family'] == fam and r['ok']]
        for st in ('stable', 'unstable', 'edge'):
            sel = [(r['tau'], r['ptp']) for r in pts
                   if stability(r) == st]
            if sel:
                xs, ys = zip(*sel)
                ax.plot(xs, ys, 'o', ms=3.2, color=COL[st],
                        label=f'{label}, $\\mu_1${"<1" if st=="stable" else ">1" if st=="unstable" else "\\approx 1"}')
    tau_h = bt['tau_hopf_lower']['bracket']
    ax.axvline(tau_h[0], color='#555555', lw=0.8, ls=':')
    ax.text(tau_h[0], 63, ' $\\tau_-$ (certified Hopf)', fontsize=8,
            color='#555555', va='top', rotation=90)
    fold = bt['small_branch_fold']['bracket']
    ax.axvline(fold[0], color='#7a2010', lw=0.9, ls='--')
    ax.text(fold[0], 63, ' SNPO fold 5.5872362\n (three-order MS,\n Krawczyk-certified)',
            fontsize=7.5, color='#7a2010', va='top', ha='right')
    # equilibrium amplitude marker
    eqN = json.loads((HERE / 'p4_environment.json').read_text())[
        'equilibrium'][0]
    ax.axhline(0.0, color='#28623f', lw=1.1)
    ax.text(1.05, 1.4, 'equilibrium (stable on $(\\tau_-,\\tau_+)$; '
            'root-scan + basin archive)', fontsize=7.5, color='#28623f')
    ax.set_xlim(1.0, 6.6)
    ax.set_ylim(-3, 66)
    ax.set_xlabel('$\\tau$ (yr)')
    ax.set_ylabel('N peak-to-peak amplitude')
    ax.set_title('(a) Lower region: one S-shaped branch\n'
                 '(small arm and large arm meet at the single fold)')
    ax.legend(fontsize=7, loc='upper right', framealpha=0.9)

    # ---- (b) upper bifurcation diagram --------------------------------
    ax = axes[0, 1]
    pts = [r for r in branch if r['family'] == 'small_upper' and r['ok']]
    for st in ('stable', 'unstable', 'edge'):
        sel = [(r['tau'], r['ptp']) for r in pts if stability(r) == st]
        if sel:
            xs, ys = zip(*sel)
            ax.plot(xs, ys, 'o', ms=3.2, color=COL[st],
                    label=f'small branch, $\\mu_1$'
                          f'{"<1" if st=="stable" else ">1" if st=="unstable" else "\\approx 1"}')
    tau_h = bt['tau_hopf_upper']['bracket']
    ax.axvline(tau_h[0], color='#555555', lw=0.8, ls=':')
    ax.text(tau_h[0] - 0.4, 2.0, ' $\\tau_+$ (certified Hopf)', fontsize=8,
            color='#555555', va='top', rotation=90)
    ax.axhline(0.0, color='#28623f', lw=1.1)
    # basin capture strip (from the basin archive)
    grid = {}
    for r in basin:
        grid.setdefault(float(r['tau']), {})[r['history']] = \
            r['classification']
    taus = sorted(grid)
    for t in taus:
        if t < 125:
            continue
        cls = grid[t].get('H1')
        if cls == 'captured':
            ax.plot([t], [-0.55], marker='v', color='#7a2010', ms=5)
    ax.text(126.5, -1.05, 'basin archive: H1 captured '
            '(E~$E_{\\max}$ face cycle, amp~44, not Fourier-collocatable)',
            fontsize=7, color='#7a2010', va='top')
    ub = res['comparison']['upper_boundary'].get('campaign_bracket')
    if ub:
        ax.axvspan(ub[0], ub[1], color='#c0762c', alpha=0.18)
        ax.text(ub[1] + 0.3, 1.9, 'H1 capture onset\n[%0.1f, %0.1f]'
                % tuple(ub), fontsize=7.5, color='#8a5416')
    ax.set_xlim(125, 161)
    ax.set_ylim(-1.4, 2.4)
    ax.set_xlabel('$\\tau$ (yr)')
    ax.set_ylabel('N peak-to-peak amplitude')
    ax.set_title('(b) Upper region: the Hopf small branch\n'
                 '+ the captured E-face family (basin record)')
    ax.legend(fontsize=7, loc='upper left', framealpha=0.9)

    # ---- (c) multiplier tracks ----------------------------------------
    ax = axes[1, 0]
    for fam, label in (('large_lower', 'large arm (lower)'),
                       ('small_lower', 'small arm (lower)'),
                       ('small_upper', 'small branch (upper)')):
        pts = [r for r in branch if r['family'] == fam
               and r['mu1re'] is not None and r['ok']]
        pts.sort(key=lambda r: r['tau'])
        ax.plot([r['tau'] for r in pts], [r['mu1re'] for r in pts],
                'o-', ms=2.6, lw=0.9, label=label)
    ax.axhline(1.0, color='#555555', lw=1.0, ls='--')
    ax.text(6.42, 1.012, '+1 (fold)', fontsize=8, color='#555555')
    ax.set_xlim(1.2, 6.6)
    ax.set_ylim(0.0, 1.14)
    ax.set_xlabel('$\\tau$ (yr)')
    ax.set_ylabel('dominant nontrivial multiplier $\\mu_1$ (real)')
    ax.set_title('(c) Variational Floquet tracks along the branches\n'
                 '(real at every record; $\\mu_1\\to 1$ at the fold)')
    ax.legend(fontsize=8, loc='upper left')
    # inset: the upper track
    axin = ax.inset_axes([0.63, 0.12, 0.35, 0.38])
    pts = [r for r in branch if r['family'] == 'small_upper'
           and r['mu1re'] is not None]
    pts.sort(key=lambda r: r['tau'])
    axin.plot([r['tau'] for r in pts], [r['mu1re'] for r in pts],
              'o-', ms=2, lw=0.8, color='#3b3b3b')
    axin.axhline(1.0, color='#555555', lw=0.8, ls='--')
    axin.set_xlim(129, 151)
    axin.set_title('small branch (upper)', fontsize=7)

    # ---- (d) basin grid ------------------------------------------------
    ax = axes[1, 1]
    hist_order = ['H1', 'H2', 'H3']
    cmap = dict(captured='#7a2010', settles='#d8cdbd',
                intermediate='#c0762c')
    for i, t in enumerate(taus):
        for j, h in enumerate(hist_order):
            cls = grid[t].get(h)
            ax.add_patch(plt.Rectangle((i - 0.5, j - 0.5), 1, 1,
                                       color=cmap[cls]))
    ax.set_xlim(-0.5, len(taus) - 0.5)
    ax.set_ylim(-0.5, 2.5)
    ax.set_xticks(range(len(taus)))
    ax.set_xticklabels([f'{t:g}' for t in taus], rotation=70,
                       fontsize=6.5)
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(['H1 (large stock,\nlow effort)',
                        'H2 (depleted)',
                        'H3 (near-eq,\n+1%)'], fontsize=7)
    for i, t in enumerate(taus):
        for j, h in enumerate(hist_order):
            cls = grid[t].get(h)
            ax.text(i, j, cls[0].upper(), ha='center', va='center',
                    fontsize=6.5,
                    color='white' if cls == 'captured' else '#3b3b3b')
    ax.set_title('(d) History/basin archive (87 runs, dt=0.02,\n'
                 'horizon $4\\times10^4$ yr, tail 1800 yr)\n'
                 'C=captured, S=settles, I=intermediate', fontsize=9)
    import matplotlib.patches as mpatches
    handles = [mpatches.Patch(color=cmap['captured'], label='captured'),
               mpatches.Patch(color=cmap['settles'], label='settles'),
               mpatches.Patch(color=cmap['intermediate'],
                              label='intermediate')]
    ax.legend(handles=handles, fontsize=7, loc='upper right')

    fig.suptitle('P4 five-regime topology — pre-registered campaign '
                 '2026-09-03 (first committed five-regime record; the '
                 'inherited A018 numbers keep their exploratory status)',
                 fontsize=9.5, y=0.995)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    out = HERE / 'p4_topology_figure.png'
    fig.savefig(out, dpi=170)
    print('written', out)


if __name__ == '__main__':
    main()
