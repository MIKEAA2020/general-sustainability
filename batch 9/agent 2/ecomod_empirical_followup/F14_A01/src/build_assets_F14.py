#!/usr/bin/env python3
"""Replot source-pinned results; no new empirical estimates or confidence claims."""
from pathlib import Path
import csv,json,hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook
from openpyxl.styles import Font,PatternFill,Alignment
ROOT=Path(__file__).resolve().parents[1]
def require(ok,msg):
 if not ok:raise ValueError(msg)
def read(name):
 with (ROOT/'data'/name).open(newline='')as f:return list(csv.DictReader(f))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(fig,name):
 fig.savefig(ROOT/'figures'/name,bbox_inches='tight',metadata={'CreationDate':None,'ModDate':None});plt.close(fig)
def run():
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'pdf.fonttype':42,'axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'bold'})
 codes=['BRA','IDN','COD','CMR','CAN','FIN','FRA','AUS'];names=['Brazil','Indonesia','DR Congo','Cameroon','Canada','Finland','France','Australia']
 a=read('accounts_candidate_changes_F12.csv');lookup={(r['ISO3'],r['domain']):float(r['percent_change'])for r in a if r['start']=='2015'and r['end']=='2023'}
 fig,ax=plt.subplots(figsize=(9,4.5));y=np.arange(8)
 ax.barh(y-.17,[lookup[c,'total']for c in codes],height=.30,color='#167f7b',label='Total biocapacity account')
 ax.barh(y+.17,[lookup[c,'forest_component']for c in codes],height=.30,color='#203e53',label='Forest account component')
 ax.set(yticks=y,yticklabels=names,xlabel='Published account change, 2015–2023 (%)',xlim=(-8.8,14.8));ax.invert_yaxis();ax.axvline(0,color='#687b83',lw=.8);ax.grid(axis='x',alpha=.12);ax.set_axisbelow(True)
 ax.legend(loc='lower left',bbox_to_anchor=(0,1.01),ncol=2,frameon=False,fontsize=11)
 fig.tight_layout();save(fig,'account_composition_F14.pdf')
 rows=[r for r in read('endpoint_conversion_path_bounds_F12.csv')if r['constraint_level']=='finest_reported_geography']
 fig,axes=plt.subplots(1,2,figsize=(10,4.1),gridspec_kw={'width_ratios':[1.1,1]})
 exported=[]
 for ax,code,title in zip(axes,['BRA','IDN'],['Brazil','Indonesia']):
  rr=[r for r in rows if r['country']==code]
  for j,r in enumerate(rr):
   lo=float(r['lower_unique_endpoint_area_ha'])/1e6;hi=float(r['upper_unique_endpoint_area_ha'])/1e6
   initial={'formations':'F','formations_plus_savanna':'F+S','forest':'F','mapped_forest':'F'}[r['initial_group']]
   label=initial+' → '+r['final_target'].replace('_',' ')
   ax.plot([lo,hi],[j,j],lw=5,color='#24485c'if code=='BRA'else'#167f7b',solid_capstyle='butt');ax.plot([lo,hi],[j,j],'|',color='#142d3b',ms=11)
   ax.text((lo+hi)/2,j-.15,f'{lo:.3f}–{hi:.3f}',ha='center',va='bottom',fontsize=10.5)
   exported.append(dict(country=code,group=r['initial_group'],target=r['final_target'],lower_Mha=lo,upper_Mha=hi))
  ax.set(yticks=range(len(rr)),yticklabels=[{'formations':'F','formations_plus_savanna':'F+S','forest':'F','mapped_forest':'F'}[r['initial_group']]+' → '+r['final_target'].replace('_',' ')for r in rr],xlabel='Unique endpoint cohort (million ha)',title=title,ylim=(len(rr)-.5,-.65));ax.axvline(0,color='#999999',lw=.7);ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
  ax.set_xlim((-1,38)if code=='BRA'else(-.12,4.9))
 fig.tight_layout(w_pad=2);save(fig,'endpoint_cohorts_F14.pdf')
 fi=json.loads((ROOT/'data/FIN_cycle_volume_inference_F12.json').read_text())
 fr=read('FRA_volume_change_bounds_F13.csv');fr=[r for r in fr if r['initial_cycle']=='2013-2017'and r['endpoint_family']=='2']
 ca=next(r for r in read('CAN_NFI_biomass_intervals_F13.csv')if r['kind']=='annual_change'and r['forest_type']=='Subtotal')
 fig,axes=plt.subplots(3,1,figsize=(9.7,7.4));intervals=[]
 def panel(ax,entries,point,title,unit):
  for j,(label,lo,hi,color)in enumerate(entries):
   ax.plot([lo,hi],[j,j],lw=7,color=color,solid_capstyle='butt');ax.plot(point,j,'o',color='#163544',ms=6);intervals.append(dict(panel=title,label=label,point=point,lower=lo,upper=hi,unit=unit))
  ax.set(yticks=range(len(entries)),yticklabels=[r[0]for r in entries],title=title,xlabel=unit,ylim=(len(entries)-.5,-.5));ax.axvline(0,color='#b44f3b',lw=1);ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
 panel(axes[0],[('Approx. 95% marginal-normal',*fi['approx_95pct_simultaneous_endpoint_difference_interval_Mm3'],'#167f7b'),('95% second-moment sensitivity',*fi['moment_only_95pct_two_sided_sensitivity_interval_Mm3'],'#6d818e')],fi['point_difference_Mm3'],'(a) Finland: NFI13 (2019–2023) minus NFI12 (2014–2018)','Volume difference (million m³)')
 panel(axes[1],[(('At least 90% marginal coverage'if r['mode']=='union90'else'Approx. 95% marginal-normal'),float(r['lower_Mm3']),float(r['upper_Mm3']),'#6d818e'if r['mode']=='union90'else'#167f7b')for r in fr],200.,'(b) France: 2021–2025 minus 2013–2017 campaigns','Volume difference (million m³)')
 panel(axes[2],[('Provider interval; level uncertified',float(ca['provider_interval_lower']),float(ca['provider_interval_upper']),'#6d818e')],float(ca['estimate']),'(c) Canada: remeasured 2007–2017 / projected 2006–2017','Annualized AGB change (Mt/year)')
 fig.tight_layout(h_pad=2.5);save(fig,'inventory_uncertainty_F14.pdf')
 (ROOT/'metadata/plot_values_F14.json').write_text(json.dumps(dict(account_values=lookup_to_rows(lookup),endpoint_cohorts=exported,inventory_intervals=intervals,all_intervals_typed_not_pooled=True,no_new_empirical_estimates=True),indent=2)+'\n')
 # Preserve every original workbook value; add only an editorial navigation sheet.
 source=ROOT.parent/'ecomod_empirical_integration_F13_A01/national_results_F13_A01.xlsx'
 if not source.exists():source=ROOT.parent/'F13_A01/national_results_F13_A01.xlsx'
 w=load_workbook(source);guide=w.create_sheet('F14 reader guide',0)
 guide.append(['F14 manuscript navigation','Main is self-contained; SI supplies protocols and exact supporting tables.'])
 for row in [('Main Figure 1','Eight-country account composition'),('Main Figures 2–4','Local support, coherent joint sign ambiguity and information increments'),('Main Figure 5','All seven unique mapped endpoint-cohort ranges'),('Main Figure 6','Separate Finnish, French and Canadian inventory panels'),('Main Table 1','All eight national cases and typed physical evidence'),('Main Table 2','Local conditional allocation bounds'),('SI','Full account sensitivities, Indonesia source sensitivity, exact conversions, source/uncertainty protocols'),('Inheritance','All 30 F13 sheets retained unchanged in value; F13 notes identify the numerical vintage.'),('Inference','No new calibrated national AGB comparison or reporting-accuracy evaluation is claimed.'),('AI assistance','Arena.ai Agent Mode was used to assist with computational methods and literature review.')]:guide.append(row)
 guide.freeze_panes='A2';guide.column_dimensions['A'].width=28;guide.column_dimensions['B'].width=110
 for c in guide[1]:c.font=Font(bold=True,color='FFFFFF');c.fill=PatternFill('solid',fgColor='173E52')
 for row in guide:
  for c in row:c.alignment=Alignment(vertical='top',wrap_text=True)
  guide.row_dimensions[row[0].row].height=32
 path=ROOT/'national_results_F14_A01.xlsx';w.save(path);w.close()
 old=load_workbook(source,read_only=True,data_only=False);new=load_workbook(path,read_only=True,data_only=False);checked=0
 try:
  require(len(new.sheetnames)==31,'Workbook sheet count')
  for name in old.sheetnames:
   x=old[name];y=new[name];require(x.max_row==y.max_row and x.max_column==y.max_column,'Inherited workbook dimensions')
   for row0,row1 in zip(x.values,y.values):
    for v0,v1 in zip(row0,row1):require(v0==v1,'Inherited workbook cell changed '+name);checked+=1
 finally:old.close();new.close()
 (ROOT/'metadata/workbook_QA_F14.json').write_text(json.dumps(dict(file=path.name,sha256=sha(path),sheets=31,inherited_sheets_unchanged=30,inherited_cells_checked=checked),indent=2)+'\n')
 print('Three source-based vector figures; 30 workbook sheets verified unchanged plus one reader guide.')
def lookup_to_rows(d):return [dict(country=k[0],domain=k[1],percent_change=v)for k,v in d.items()]
if __name__=='__main__':run()
