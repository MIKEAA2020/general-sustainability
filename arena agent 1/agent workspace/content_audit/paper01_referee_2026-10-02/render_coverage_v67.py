#!/usr/bin/env python3
"""Render the previously verified 48-cell discrete hold-class grid with an external legend.
The plot is not a proof of the continuous-time timing theorem.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from shutil import copyfile

R=Path('/home/user')
output=R/'paper 2 family/01_obstruction/figs_p2/fig_p2_coverage_v67.png'
output.parent.mkdir(parents=True,exist_ok=True)
colors={'viable':'#2e7d32','one-step':'#c62828','hold-only':'#ef6c00'}
rows=[]
for T in (1,2,3):
 for j in range(16):
  z=(10+j)/10
  viable=z>=1+T
  cell='viable' if viable else ('one-step' if z<2 else 'hold-only')
  rows.append((T,z,cell))
assert len(rows)==48
assert [sum(cell==k for _,_,cell in rows) for k in ('viable','one-step','hold-only')]==[6,30,12]
fig=plt.figure(figsize=(9.5,3.4),facecolor='white')
# Leave 29% of image width as blank right-side legend area.
ax=fig.add_axes([.075,.20,.62,.67])
for T,z,cell in rows:
 ax.scatter(z,T,s=245,color=colors[cell],marker='s',edgecolor='white',linewidth=.6,zorder=3)
ax.plot([.99,1.90,2.5],[.9,.9,1.5],color='black',lw=1.4,ls='--',zorder=4)
ax.plot([2,2],[.82,3.18],color=colors['one-step'],lw=1.4,zorder=4)
ax.set_xlim(.95,2.55);ax.set_ylim(.80,3.20)
ax.set_xticks([1,1.25,1.5,1.75,2,2.25,2.5])
ax.set_yticks([1,2,3])
ax.set_xlabel(r'initial position $z_0$',fontsize=10)
ax.set_ylabel(r'blind window $T_{\mathrm{obs}}$ (steps)',fontsize=10)
ax.set_title('Discrete hold-class coverage (48 cells)',fontsize=11,pad=8)
handles=[Patch(facecolor=colors['viable'],label='Viable in hold class'),
 Patch(facecolor=colors['one-step'],label='Nonviable: first step'),
 Patch(facecolor=colors['hold-only'],label='Nonviable: later blind step'),
 Line2D([0],[0],color='black',lw=1.4,ls='--',label=r'Hold boundary $z_0=1+T_{\mathrm{obs}}$'),
 Line2D([0],[0],color=colors['one-step'],lw=1.4,label=r'First-step boundary $z_0=2$')]
legend=fig.legend(handles=handles,loc='upper left',bbox_to_anchor=(.72,.78),
                  frameon=False,fontsize=8.3,borderaxespad=0,labelspacing=.85,
                  handlelength=2.0)
# Disallow future edits from making the legend intrude on the plotted axes.
fig.canvas.draw()
renderer=fig.canvas.get_renderer()
axbox=ax.get_window_extent(renderer)
legendbox=legend.get_window_extent(renderer)
assert legendbox.x0>axbox.x1+10,(legendbox,axbox)
fig.savefig(output,dpi=230,facecolor='white')
mirror=R/'b01/figs_p2/fig_p2_coverage_v67.png';copyfile(output,mirror)
print('RENDERED',output,'mirror',mirror,'grid_counts',6,30,12,'legend_right_of_axes_px',round(legendbox.x0-axbox.x1,1))
