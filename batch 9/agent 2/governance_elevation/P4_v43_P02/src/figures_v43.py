from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'legend.frameon':False})
a=pd.read_csv(ROOT/'data/field_test_predictions_v43.csv');s=pd.read_csv(ROOT/'data/field_stock_predictions_v43.csv');r=pd.read_csv(ROOT/'data/field_recursive_predictions_v43.csv');fig,ax=plt.subplots(2,2,figsize=(10.2,7.6),sharex=True);col={'mobilising':'#af4439','protective':'#197d73','logistic':'#af4439','recruitment_lag1':'#197d73'}
x=s[s.model=='logistic'];ax[0,0].plot(x.target_year,x.observed_N,'ko-',lw=1,ms=3,label='assessment');ax[0,0].plot(x.target_year,x.AR1,':',color='#6d6d6d',label='AR(1)')
for label,g in s.groupby('model'):ax[0,0].plot(g.target_year,g.predicted_N,color=col[label],label='logistic'if label=='logistic'else'with recruitment')
x=a[(a.scenario=='TBiomass')&(a.law=='protective')];ax[0,1].plot(x.target_year,x.observed_target_proxy,'ko-',lw=1,ms=3,label='assessment proxy');ax[0,1].plot(x.target_year,x.AR1_prediction,':',color='#6d6d6d',label='AR(1)')
for label,g in a[a.scenario=='TBiomass'].groupby('law'):ax[0,1].plot(g.target_year,g.prediction,color=col[label],label=label)
x=r[r.law=='protective']
for j,var in enumerate(['N','U']):
 ax[1,j].plot(x.year,x['observed_'+var],'ko-',lw=1,ms=3,label='assessment'+(' proxy'if j else''));ax[1,j].plot(x.year,x['VAR1_'+var],':',color='#6d6d6d',label='VAR(1)');ax[1,j].plot(x.year,x['constant_'+var],'--',lw=.8,color='#999',label='2009 constant')
 for label,g in r.groupby('law'):ax[1,j].plot(g.year,g['predicted_'+var],color=col[label],label=label)
for x,title,y in zip(ax.flat,['(a) Stock: observed-input one-step test','(b) Catch intensity: response-component test','(c) Stock: recursive annual surrogate','(d) Catch intensity: recursive annual surrogate'],['Normalised total biomass N','Dimensionless catch intensity U','Normalised total biomass N','Dimensionless catch intensity U']):
 x.set_title(title,loc='left',fontsize=10);x.set_ylabel(y);x.grid(alpha=.16);x.legend(fontsize=7.4,ncol=2,loc='best');x.set_xlim(2009.5,2024.5)
for x in ax[1]:x.set_xlabel('Target year')
fig.tight_layout(pad=1.4);fig.savefig(ROOT/'figures/fig4_field_tests_v43.png',dpi=240);fig.savefig(ROOT/'figures/fig4_field_tests_v43.pdf');plt.close(fig)
