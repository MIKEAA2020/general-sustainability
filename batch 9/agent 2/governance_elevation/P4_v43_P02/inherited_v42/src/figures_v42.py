from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
r=json.loads((ROOT/'data/upper_arm_continuation_v42.json').read_text())['records'];f=json.loads((ROOT/'data/upper_arm_floquet_v42.json').read_text())['records']
t=np.array([x['tau']for x in r]);fig,ax=plt.subplots(2,2,figsize=(10,7.1),layout='constrained');blue='#176e88';orange='#b04e2b'
ax[0,0].plot(t,[x['N_max']for x in r],color=blue,label='Cycle maximum');ax[0,0].plot(t,[x['N_min']for x in r],color=blue,ls='--',label='Cycle minimum');ax[0,0].axhline(89.551883,color='#666',lw=1,label='Equilibrium');ax[0,0].set_ylabel('Stock N');ax[0,0].legend(fontsize=8)
ax[0,1].plot(t,[x['period']for x in r],color=blue);ax[0,1].set_ylabel('Period (years)')
ax[1,0].semilogy(t,[30-x['E_max']for x in r],color=orange);ax[1,0].set_ylabel('Distance from effort ceiling: 30 − max(E)')
ax[1,1].plot([x['tau']for x in f],[x['dominant_nontrivial_modulus']for x in f],color=blue);ax[1,1].axhline(1,color=orange,ls='--');ax[1,1].set_ylabel('Dominant nontrivial multiplier modulus');ax[1,1].set_ylim(.7,1.02)
for i,a in enumerate(ax.flat):
 a.axvspan(148.6,149.5,color='#e9b563',alpha=.3);a.axvline(150.3584773101414,color='#555',ls=':',lw=1);a.set_xlabel('Deployment delay (years)');a.grid(alpha=.18);a.text(.02,.96,'abcd'[i]+')',transform=a.transAxes,va='top',weight='bold')
fig.savefig(ROOT/'figures/fig2_upper_branch_v42.png',dpi=220);plt.close(fig)
# A waveform comparison uses the actual fresh H1 tail, not a fitted amplitude.
a=np.load(ROOT/'data/upper_arm_refined_orbits_v42.npz');w=a['149.5'];from periodic_orbits_v42 import physical
from scipy.signal import resample
Y=physical(resample(w[:-1].reshape(-1,3),4096,axis=0));T=w[-1];tail=np.load(ROOT/'data/nonlinear_tail_H1_tau149p5_dt0p02_v42.npz')['trajectory'];rec=json.loads((ROOT/'data/nonlinear_capture_check_v42.json').read_text())['records'][1];phase=rec['phase_shift_cycles']
phase_t=(tail[:,0]/T+phase)%1;sel=tail[:,0]>=tail[-1,0]-T
fig,axes=plt.subplots(3,1,figsize=(8.6,6.5),sharex=True,layout='constrained')
for j,a in enumerate(axes):
 a.plot(np.arange(len(Y))/len(Y),Y[:,j],color=blue,label='Continued orbit');a.scatter(phase_t[sel][::8],tail[sel,1+j][::8],s=8,color=orange,alpha=.65,label='Nonlinear H1 tail');a.set_ylabel(['N','Z','E'][j]);a.grid(alpha=.15)
axes[0].legend(ncol=2,fontsize=9);axes[-1].set_xlabel('Phase (cycles)');fig.savefig(ROOT/'figures/fig3_waveform_match_v42.png',dpi=200);plt.close(fig)
# Global topology: archived lower/turning records plus the new connected arm.
r=json.loads((ROOT/'data/upper_arm_continuation_v42.json').read_text())['records']
import pandas as pd
lower=pd.read_csv(ROOT/'inherited/p4_branch_archive_pinned_2efaa.csv');lower=lower[(lower.newton_ok==True)&(lower.floquet_ok==True)]
upper=pd.read_csv(ROOT/'inherited/second_fold_branch_pinned_2efaa.csv');upper=upper[(upper.newton_ok==True)&(upper.floquet_ok==True)]
fig,ax=plt.subplots(2,2,figsize=(11,7.5),layout='constrained');red='#bd3b3c'
for family,color,label in [('small_lower',red,'Unstable small arm'),('large_lower',blue,'Stable large arm')]:
 d=lower[lower.family==family];ax[0,0].plot(d.tau,d.N_ptp,color=color,label=label);ax[1,0].plot(d.tau,d.mu1_re,color=color,label=label)
ax[0,0].set_yscale('log');ax[0,0].set_ylabel('Stock peak-to-peak amplitude');ax[0,0].legend(fontsize=8)
for stable,color,label in [(False,red,'Upper unstable arm'),(True,blue,'Upper stable arm (archived turn)')]:
 d=upper[(upper.mu1_mod<1)==stable];ax[0,1].plot(d.tau,d.N_ptp,color=color,label=label)
ax[0,1].plot(t,[x['N_max']-x['N_min']for x in r],color=blue,lw=2,label='Connected stable arm');ax[0,1].axvspan(148.6,149.5,color='#e9b563',alpha=.35);ax[0,1].axvline(150.3584773,color='#555',ls=':',lw=1);ax[0,1].set_yscale('log');ax[0,1].set_ylabel('Stock peak-to-peak amplitude');ax[0,1].legend(fontsize=7.5,loc='lower left')
ax[1,0].axhline(1,color='#444',lw=1);ax[1,0].set_ylabel('Dominant real multiplier');ax[1,0].set_xlim(3.5,5.65)
colors={'captured':red,'settles':blue,'intermediate':'#d19b32'}
for file,marker,size in [('p4_basin_archive','o',18),('second_fold_basin','s',23)]:
 d=pd.read_csv(ROOT/f'inherited/{file}_pinned_2efaa.csv')
 for history,y in [('H1',0),('H2',1),('H3',2)]:
  for cls,color in colors.items():
   sub=d[(d.history==history)&(d.classification==cls)];ax[1,1].scatter(sub.tau,np.full(len(sub),y),s=size,marker=marker,color=color,edgecolor='white',lw=.25)
for cls,color in colors.items():ax[1,1].scatter([],[],color=color,s=22,label=cls)
ax[1,1].set_yticks([0,1,2],['H1','H2','H3']);ax[1,1].set_ylim(-.35,2.5);ax[1,1].legend(fontsize=7.5,ncol=3,loc='upper left');ax[1,1].set_xlim(0,160)
for i,a in enumerate(ax.flat):a.set_xlabel('Deployment delay (years)');a.grid(alpha=.16);a.set_title(['(a) Lower periodic family','(b) Full upper periodic family','(c) Lower-fold multiplier exchange','(d) Finite-history basin outcomes'][i],fontsize=10)
for a in [ax[0,0],ax[1,0]]:a.axvline(5.5872362,color='#666',ls='--',lw=1)
ax[0,0].axvline(3.666149,color='#666',ls=':',lw=1);ax[0,1].axvline(64.4023272,color='#666',ls='--',lw=1)
fig.savefig(ROOT/'figures/fig1_global_topology_v42.png',dpi=210);plt.close(fig)
