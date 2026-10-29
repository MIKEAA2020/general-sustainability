"""Build a source-traceable vector graphical abstract, not simulated data."""
from pathlib import Path
import json,hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch,Rectangle
from matplotlib.path import Path as MPath
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent/'governance_elevation_P4_v43_P02'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','pdf.fonttype':42})
NAVY='#183142';MUTED='#536675';TEAL='#17796C';RED='#A74436';LINE='#C5D0D5'
def run():
 sources={}
 for n in ['global_equilibrium_spectrum_v43.json','global_protective_basin_v43.json','field_response_test_v43.json']:
  p=BASE/'data'/n;sources[n]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'data':json.loads(p.read_text())}
 sp=next(r for r in sources['global_equilibrium_spectrum_v43.json']['data']['records']if r['candidate']=='A'and r['gated']);windows=[(float(r['left_Hopf_interval'][0]),float(r['right_Hopf_interval'][1]))for r in sp['all_positive_delay_stability_windows']];f=sources['field_response_test_v43.json']['data']['scenarios']['TBiomass']['protective'];gain=(1-f['RMSE_ratio_to_AR1'])*100
 fig=plt.figure(figsize=(7.2,4.64),facecolor='white');ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1800);ax.set_ylim(1160,0);ax.axis('off')
 def text(x,y,s,size=22,color=NAVY,weight='normal',ha='left',va='center',**kw):return ax.text(x,y,s,fontsize=size/2.5,color=color,weight=weight,ha=ha,va=va,**kw)
 def box(x,y,w,h,face='white',edge=LINE,rad=14,lw=.8):ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={rad}',facecolor=face,edgecolor=edge,lw=lw))
 def arrow(a,b,color=MUTED):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=8,linewidth=.9,color=color))
 text(90,63,'GOVERNANCE DELAY',18,MUTED,'bold')
 text(90,120,'Same stock. Different response laws.',42,NAVY,'bold')
 text(90,176,'Response law, deployment latency and review cadence are distinct design coordinates.',22)
 # Mechanism, not a measured institutional flowchart.
 for x,title,subtitle in [(100,'Stock N','renewal − harvest'),(700,'Memory Z','filtered decline'),(1300,'Effort E','deployed extraction')]:
  box(x,244,400,103,face='#F5F8F9');text(x+200,278,title,27,weight='bold',ha='center');text(x+200,319,subtitle,20,MUTED,ha='center')
 arrow((515,292),(685,292));text(600,265,'decline',19,MUTED,ha='center')
 arrow((1115,292),(1285,292));text(1200,265,'delay τ',19,MUTED,ha='center')
 path=MPath([(1500,353),(1500,411),(300,411),(300,353)],[MPath.MOVETO,MPath.LINETO,MPath.LINETO,MPath.LINETO]);ax.add_patch(FancyArrowPatch(path=path,arrowstyle='-|>',mutation_scale=8,lw=.9,color=MUTED));text(880,412,'harvest pressure',20,MUTED,ha='center',bbox={'facecolor':'white','edgecolor':'none','pad':2})
 text(1500,380,'review cadence Tᵣ',18,MUTED,ha='center',bbox={'facecolor':'white','edgecolor':'none','pad':1})
 # Two contrasting mathematical outcomes.
 box(90,465,795,370,face='#FDF8F6',edge='#E8D5CE');box(915,465,795,370,face='#F3F9F7',edge='#C7DED7')
 text(125,504,'MOBILISING',24,RED,'bold');text(125,544,'Effort escalates with decline',22)
 text(125,592,'Delay can stabilise — and destabilise.',24,weight='bold')
 text(125,633,'Complete equilibrium root count, all positive delays.',19)
 text(125,678,'A, gated · stable windows (years)',19,MUTED)
 x0,x1,y=145,830,723;scale=(x1-x0)/330
 ax.plot([x0,x1],[y,y],color=LINE,lw=4,solid_capstyle='butt')
 for lo,hi in windows:ax.plot([x0+scale*lo,x0+scale*hi],[y,y],color=TEAL,lw=6,solid_capstyle='butt')
 for tick in [0,150,300]:
  xx=x0+scale*tick;ax.plot([xx,xx],[y+11,y+21],color=MUTED,lw=.5);text(xx,y+37,str(tick),17,MUTED,ha='center')
 arrow((x1,y),(x1+23,y));text(x1+29,y,'τ',18,MUTED)
 for lo,hi in windows:text(x0+scale*(lo+hi)/2,800,f'{lo:.2f}–{hi:.2f}',18,TEAL,'bold',ha='center')
 text(950,504,'PROTECTIVE',24,TEAL,'bold');text(950,544,'Quota decreases as deficit memory rises',22)
 text(950,592,'Complete interior basin',25,weight='bold')
 text(950,630,'E₀ < M, qE₀ < r and Γ < 1',21)
 text(950,664,'Every fixed finite delay and positive fixed cadence',19)
 text(950,697,'Native signal-hold / exact nonlinear quota review',18,MUTED)
 text(950,742,'Γ < 0.475',30,TEAL,'bold');text(1375,742,'Γ < 0.687',30,TEAL,'bold')
 text(950,776,'common point',18,MUTED);text(1375,776,'declared parameter box',18,MUTED)
 text(950,812,'Excluded: zero-stock and saturated-effort faces.',18,MUTED)
 # The negative empirical result is part of the abstract, not a footnote.
 box(90,867,1620,172,face='#F2F5F7',edge='#D9E1E5')
 text(125,902,'FIELD CHECK · NORTH SEA HERRING',18,MUTED,'bold')
 text(125,949,f'Protective response: only {gain:.2f}% lower RMSE than AR(1).',25,weight='bold')
 text(125,992,'Stock forecasts fail baselines; joint DDE validation is not achieved.',23)
 text(90,1081,'Continuum folds: rigorous full-series residual bounds ≠ an existence certificate.',19,MUTED)
 text(90,1124,'Amin Abaee  ·  Governance manuscript v43',17,MUTED)
 metadata={'Title':'Graphical abstract: Governance delay and the stability of harvested stocks','Author':'Amin Abaee','Subject':'Source-traceable schematic accompanying governance v43; conditional theory and mixed field evidence'}
 fig.canvas.draw()
 renderer=fig.canvas.get_renderer();bounds=fig.bbox
 for item in ax.texts:
  b=item.get_window_extent(renderer)
  if b.x0<bounds.x0 or b.y0<bounds.y0 or b.x1>bounds.x1 or b.y1>bounds.y1:raise RuntimeError('Text outside canvas: '+item.get_text())
 fig.savefig(ROOT/'figures/graphical_abstract_governance_v43_GA01.pdf',metadata=metadata)
 fig.savefig(ROOT/'figures/graphical_abstract_governance_v43_GA01.svg',metadata={'Title':metadata['Title'],'Creator':'Amin Abaee; reproducible vector schematic'})
 fig.savefig(ROOT/'figures/graphical_abstract_governance_v43_GA01.png',dpi=500,metadata={'Title':metadata['Title'],'Author':'Amin Abaee'})
 plt.close(fig)
 claims={'scope':'Separate graphical-abstract asset for immutable governance v43/SIv10; no new theory, data or model fit','sources':{k:{'sha256':v['sha256'],'path':'../governance_elevation_P4_v43_P02/data/'+k}for k,v in sources.items()},'mobilising_axis':{'candidate':'A','gated':True,'all_stable_windows_years':windows,'endpoint_display':'approximately two decimals; schematic not uncertainty or calibration'},'protective':{'sufficient_condition':'Gamma<1 with E0<M and qE0<r','physical_basin':'N(0)>0, E(0)<M in the physical rectangle, with admissible bounded nonnegative memory history','point_gain_upper':sources['global_protective_basin_v43.json']['data']['global_gain'][1],'box_gain_upper':sources['global_protective_basin_v43.json']['data']['parameter_box_global_gain'][1],'implementations':'continuous delay, native signal-hold, exact nonlinear frozen-effort review; not Euler/mixed/mobilising'},'field':{'test_years':[2010,2024],'protective_RMSE_improvement_over_AR1_percent':gain,'non_confirmatory_retrospective_test':True,'common_support_correction_disclosed_in_main_SI':True,'joint_DDE_validation':False},'continuum_fold_existence_certified':False}
 (ROOT/'data/graphical_abstract_claims_v43_GA01.json').write_text(json.dumps(claims,indent=2)+'\n')
if __name__=='__main__':run()
