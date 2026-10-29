#!/usr/bin/env python3
"""Render article tables and an original figure from computed F11 CSVs."""
import csv
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

def rows(name):
    with (ROOT/'data'/name).open() as f:
        return list(csv.DictReader(f))

def main():
    out=ROOT/'results';out.mkdir(exist_ok=True)
    scales=rows('resolution_frontier_F11.csv')
    cancellation=rows('cancellation_by_scale_F11.csv')
    sensitivity=rows('density_contrast_sensitivity_F11.csv')
    thresholds=rows('density_contrast_sign_boundaries_F11.csv')
    labels={'forest_formations':'Formations','formations_plus_savanna':'Formations + savanna'}
    basewidth=float(next(r for r in scales if r['block_side_native_cells']=='256')['width_Mg'])
    bygroup={g:[r for r in scales if r['group']==g] for g in labels}
    gains=float(cancellation[0]['gains_Mg']);losses=float(cancellation[0]['losses_Mg'])
    net=float(cancellation[0]['net_Mg']);k=float(cancellation[0]['cancellation'])
    macros={'MapNet':f'{net/1000:.2f}', 'MapGain':f'{gains/1000:.2f}',
            'MapLoss':f'{losses/1000:.2f}', 'MapCancellation':f'{100*k:.2f}',
            'WholeWidth':f'{basewidth/1000:.2f}'}
    for g,suffix in [('forest_formations','Form'),('formations_plus_savanna','Sav')]:
        native=bygroup[g][0];t=next(r for r in thresholds if r['group']==g)
        macros['Reduction'+suffix]=f"{100*(1-float(native['width_Mg'])/basewidth):.2f}"
        macros['Ratio'+suffix]=f"{float(t['positive_sign_boundary_ratio']):.4f}"
    (out/'numbers_F11.tex').write_text('\n'.join('\\newcommand{\\'+n+'}{'+v+'}' for n,v in macros.items())+'\n')
    table=[r'\begin{table}[htbp]',r'\centering\small',
           r'\caption{Same-footprint information comparison under the unrestricted allocation model. Widths are in $10^3$ Mg. Reduction compares native-cell mass observations with the one-window mass observation, retaining identical mapped domains and point maps. Neither information set identifies a group-change sign.}\label{tab:frontier}',
           r'\begin{tabular}{lrrr}',r'\toprule',
           r'Mapped domain & One-window width & Native-cell width & Reduction (\%)\\\midrule']
    for g in labels:
        width=float(bygroup[g][0]['width_Mg']);table.append(f"{labels[g]} & {basewidth/1000:.2f} & {width/1000:.2f} & {100*(1-width/basewidth):.2f}"+r'\\')
    table += [r'\bottomrule',r'\end{tabular}',r'\end{table}']
    (out/'frontier_table_F11.tex').write_text('\n'.join(table)+'\n')
    coverage=ROOT/'inherited_F10/data/support/native_probe_coverage.csv'
    # Exact inherited payload, additionally surfaced under an explicit F11 name.
    (ROOT/'data/native_probe_coverage_F11.csv').write_bytes(coverage.read_bytes())
    with coverage.open() as f: c=list(csv.DictReader(f))
    table=[r'\begin{table}[htbp]',r'\centering\small',
           r'\caption{Deterministic native access probes, not national or forest-coverage estimates. Every window contains 65,536 cells; joint valid denotes finite, in-range AGB and AGB-SD. Zeros are observed valid AGB values, not missing data or a forest-area classification.}\label{tab:nativecoverage}',
           r'\begin{tabular}{llrr}',r'\toprule',r'Country identifier & Year & Joint valid cells & AGB zero cells\\\midrule']
    for r in c:
        table.append(f"{r['ISO3']} & {r['year']} & {int(r['joint_agb_sd_valid_cells']):,} & {int(r['agb_zero_cells']):,}"+r'\\')
    table += [r'\bottomrule',r'\end{tabular}',r'\end{table}']
    (out/'coverage_table_F11.tex').write_text('\n'.join(table)+'\n')
    table=[r'\begin{longtable}{lrrr}',
           r'\caption{Conditional density-contrast sensitivity, in $10^3$ Mg. $R$ is assumed, not estimated or calibrated. $R=1$ is homogeneous allocation; $R=\infty$ is the primary unrestricted model.}\label{tab:contrast}\\',
           r'\toprule',r'Mapped domain & $R$ & Difference lower & Difference upper\\\midrule\endfirsthead',
           r'\toprule',r'Mapped domain & $R$ & Difference lower & Difference upper\\\midrule\endhead']
    for r in sensitivity:
        ratio=r'$\infty$' if r['max_density_ratio']=='inf' else f"{float(r['max_density_ratio']):g}"
        table.append(f"{labels[r['group']]} & {ratio} & {float(r['difference_lower_Mg'])/1000:.4f} & {float(r['difference_upper_Mg'])/1000:.4f}"+r'\\')
    table += [r'\bottomrule',r'\end{longtable}']
    (out/'contrast_table_F11.tex').write_text('\n'.join(table)+'\n')
    plt.rcParams.update({'font.size':8.5,'axes.spines.top':False,'axes.spines.right':False,
                         'svg.fonttype':'none','pdf.fonttype':42})
    fig=plt.figure(figsize=(6.3,5.2),layout='constrained')
    grid=fig.add_gridspec(2,2)
    ax=[fig.add_subplot(grid[0,0]),fig.add_subplot(grid[0,1]),fig.add_subplot(grid[1,:])]
    x=np.array([int(r['block_side_native_cells'])for r in cancellation])
    ax[0].plot(x,[float(r['gains_Mg'])/1000 for r in cancellation],'-o',ms=3,label='Positive local differences')
    ax[0].plot(x,[float(r['losses_Mg'])/1000 for r in cancellation],'-s',ms=3,label='Negative local differences')
    ax[0].axhline(net/1000,color='black',ls=':',lw=1,label='Net difference')
    ax[0].set(xscale='log',title='(a) Offsets in point-map differences',ylabel=r'$10^3$ Mg',xlabel='Block side (native cells)')
    ax[0].legend(fontsize=7.5,frameon=False,loc='upper right')
    colors=['#2166ac','#b35806']
    for color,g in zip(colors,labels):
        rr=bygroup[g]
        ax[1].plot(x,[float(r['width_Mg'])/1000 for r in rr],'-o',ms=3,color=color,label=labels[g])
        rr=[r for r in rows('density_contrast_curve_F11.csv') if r['group']==g]
        ax[2].plot([float(r['max_density_ratio'])for r in rr],
                   [float(r['difference_lower_Mg'])/1000 for r in rr],'-',color=color,label=labels[g])
        t=next(r for r in thresholds if r['group']==g)
        ax[2].plot(float(t['positive_sign_boundary_ratio']),0,marker='x',color=color,ms=6)
    ax[1].set(xscale='log',title='(b) Group-change set width',ylabel=r'$10^3$ Mg',xlabel='Block side (native cells)')
    ax[1].legend(fontsize=7.5,frameon=False,loc='lower right')
    ax[2].axhline(0,color='black',lw=.8)
    ax[2].set(xscale='log',title='(c) Assumed-contrast sensitivity',ylabel=r'Lower bound ($10^3$ Mg)',xlabel=r'Assumed density ratio bound $R$')
    ax[2].legend(fontsize=7.5,frameon=False,loc='lower left')
    for a in ax[:2]:
        a.set_xticks([1,4,16,64,256],labels=['1','4','16','64','256'])
    ax[2].set_xticks([1,2,5,10],labels=['1','2','5','10'])
    for a in ax:a.grid(alpha=.17)
    for ext in ('pdf','png','svg'):
        fig.savefig(out/f'identification_frontier_F11.{ext}',dpi=220)
    plt.close(fig)
    print('Rendered four tables/macros, surfaced coverage CSV, and original three-panel figure.')

if __name__=='__main__':main()
