#!/usr/bin/env python3
"""Reproduce the 48-cell *discrete whole-window hold-class* coverage slice.

Run from any working directory: python3 content_audit/paper01_v70_author_batch_2026-10-03/coverage_v70.py
This is not the continuous adverse-path theorem and does not certify
nonviability for policies allowed to switch within the blind window.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
FIG = ROOT/'paper 2 family/01_obstruction/figs_p2/fig_p2_coverage_v70.png'
TAB = HERE/'coverage_v70.tsv'
LOG = HERE/'COVERAGE_RUN.md'
rows=[]
for T in (1,2,3):
    for k in range(10,26):
        z=F(k,10)
        # Both hidden modes evolve under the SAME one action, held for T steps.
        # A later reading reveals the mode, not a pre-window switching privilege.
        one_step=(z < 2)
        hold_viable=any(all(z+mode*u*T >= 1 for mode in (-1,1)) for u in (-1,1))
        assert hold_viable == (z >= 1+T)
        status='first-step' if one_step else ('viable' if hold_viable else 'later-blind-step')
        # A held action makes one mode decline monotonically. These labels
        # are about the DECLARED hold class and a finite integer deadline.
        rows.append((T,z,status,int(hold_viable),F(1,1) if hold_viable else F(1,2)))
counts=Counter(r[2] for r in rows)
assert counts=={'first-step':30,'later-blind-step':12,'viable':6},counts
assert len(rows)==48
HERE.mkdir(parents=True,exist_ok=True)
with TAB.open('w',newline='') as out:
    w=csv.writer(out,delimiter='\t');w.writerow(['T_obs','z0','classification','hold_viable','hold_value_full_horizon'])
    w.writerows((T,f'{float(z):.1f}',st,v,str(value)) for T,z,st,v,value in rows)
colors={'viable':'#2e7d32','first-step':'#c62828','later-blind-step':'#ef6c00'}
fig,ax=plt.subplots(figsize=(9.7,3.35))
for T,z,st,_,_ in rows:
    ax.scatter(float(z),T,s=120,color=colors[st],marker='s',edgecolor='white',linewidth=.55,zorder=3)
ax.plot([1,2.55],[0,1.55],'k--',linewidth=1.2,label=r'Hold boundary: $z_0=1+T_{\mathrm{obs}}$')
ax.axvline(2,color='#ae2525',linewidth=1.1,label=r'First-step boundary: $z_0=2$')
ax.set_xlim(.95,2.55);ax.set_ylim(.75,3.25);ax.set_yticks([1,2,3]);ax.set_xticks([1+i/4 for i in range(7)])
ax.set_xlabel(r'initial position $z_0$');ax.set_ylabel(r'blind window $T_{\mathrm{obs}}$ (steps)')
ax.set_title('Discrete whole-window hold-class coverage (48 cells)')
handles=[Patch(color=colors[k],label=label) for k,label in [('viable','Viable in hold class'),('first-step','Nonviable: first step'),('later-blind-step','Nonviable: later blind step')]]
lines=ax.get_lines();ax.legend(handles=handles+lines,loc='upper left',bbox_to_anchor=(1.015,1),borderaxespad=0,frameon=False,fontsize=8)
fig.subplots_adjust(left=.09,right=.69,bottom=.22,top=.84)
FIG.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(FIG,dpi=190,facecolor='white')
plt.close(fig)
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
LOG.write_text('# v70 discrete hold-class reproduction\n\n'
               'Run: `python3 content_audit/paper01_v70_author_batch_2026-10-03/coverage_v70.py` from any directory.\n'
               'This uses exact Fraction arithmetic for decisions and only matplotlib for the plot. It does not check the continuous drift theorem or per-step switching.\n\n'
               f'Counts: 48 cells, {counts["viable"]} viable, {counts["first-step"]} first-step failures, {counts["later-blind-step"]} later-blind-step failures.\n\n'
               f'`{TAB.relative_to(ROOT)}` SHA-256 `{sha(TAB)}`\n\n'
               f'`{FIG.relative_to(ROOT)}` SHA-256 `{sha(FIG)}`\n\n'
               f'Runner SHA-256 `{sha(Path(__file__))}`\n')
print('hold-class grid',dict(counts),'TABLE_SHA256',sha(TAB),'FIG_SHA256',sha(FIG))
