#!/usr/bin/env python3
"""National/state/biome C11 extent and annual transition-event analysis.
Source tables, not extrapolation from the F11 window. No accuracy adjustment.
"""
import argparse,collections,csv,hashlib,json,math
from pathlib import Path
from openpyxl import load_workbook
from accounts_F12 import require,save,delta_pct
ROOT=Path(__file__).resolve().parents[1]
FORM={3,5,6,49};SAV={4,7};CROP={39,20,40,62,41,46,47,35,48}
GROUPS={'formations':FORM,'formations_plus_savanna':FORM|SAV,'plantation':{9},'cropland':CROP,'pasture':{15},'mosaic':{21},'unobserved':{0,27},'water':{31,33}}

def run(path):
 identity=json.loads((ROOT/'metadata/BRA_C11_source_F12.json').read_text());require(hashlib.sha256(path.read_bytes()).hexdigest()==identity['sha256'],'C11 source identity drift')
 w=load_workbook(path,read_only=True,data_only=True);it=iter(w['COVERAGE_11'].values);header=next(it);years=list(range(2015,2024));indices={y:header.index('y'+str(y))for y in years};keys=set();classes=set();coverage={};classrows=[]
 for row in it:
  if row[0]is None:continue
  r=dict(zip(header,row));code=int(r['class']);key=(r['state'],r['biome'],code)
  require(key not in keys,'Duplicate coverage geographic/class row');keys.add(key);classes.add(code)
  require(r['country']=='Brasil','Unexpected country scope')
  for y in years:
   value=row[indices[y]];require(isinstance(value,(float,int))and math.isfinite(value)and value>=0,'Missing/invalid national area')
   coverage[(r['state'],r['biome'],code,y)]=float(value)
   classrows.append(dict(state=r['state'],biome=r['biome'],class_code=code,year=y,area_ha=value))
 require(not(classes&{1,10,14,18,19,22,26,36}),'Hierarchy totals must not be summed as leaves')
 agg=collections.defaultdict(float)
 for (state,biome,code,year),value in coverage.items():
  for level,unit in [('national','Brazil'),('state',state),('biome',biome)]:
   agg[level,unit,'all_classes',year]+=value
   for name,codes in GROUPS.items():
    if code in codes:agg[level,unit,name,year]+=value
 units=sorted({(l,u)for l,u,g,y in agg});annual=[];changes=[]
 for level,unit in units:
  for group in ['all_classes']+list(GROUPS):
   for year in years:annual.append(dict(level=level,unit=unit,group=group,year=year,area_ha=agg[level,unit,group,year],classification_only=True))
   a,b=agg[level,unit,group,2015],agg[level,unit,group,2023];total=agg[level,unit,'all_classes',2015]
   changes.append(dict(level=level,unit=unit,group=group,start=2015,end=2023,area_start_ha=a,area_end_ha=b,difference_ha=b-a,percent_change=delta_pct(a,b),symmetric_endpoint_error_break_even_ha=abs(b-a)/2,symmetric_endpoint_error_break_even_pct_total=100*abs(b-a)/(2*total)if total else None,statistical_confidence_claimed=False))
 save('data/BRA_C11_class_annual_by_state_biome_F12.csv',classrows)
 save('data/BRA_C11_extent_annual_F12.csv',annual);save('data/BRA_C11_extent_changes_F12.csv',changes)
 # Stream annual transition rows, retaining group/class event areas and all margins.
 it=iter(w['TRANSITION_11'].values);th=next(it);pcols={y:th.index(f'p{y}_{y+1}')for y in range(2015,2023)}
 tf=th.index('class_from');tt=th.index('class_to');si=th.index('state');bi=th.index('biome')
 margins0=collections.defaultdict(float);margins1=collections.defaultdict(float);flows=collections.defaultdict(float);tkeys=set();trows=0
 for row in it:
  if row[0]is None:continue
  st,bio,a,b=row[si],row[bi],int(row[tf]),int(row[tt]);key=(st,bio,a,b)
  require(key not in tkeys,'Duplicate transition key');tkeys.add(key);trows+=1
  for year,index in pcols.items():
   value=row[index];require(isinstance(value,(int,float))and math.isfinite(value)and value>=0,'Missing transition value')
   margins0[st,bio,a,year]+=value;margins1[st,bio,b,year+1]+=value
   for group,codes in [('formations',FORM),('formations_plus_savanna',FORM|SAV)]:
    event=None
    if a in codes and b not in codes:
     event='to_cropland'if b in CROP else'to_pasture'if b==15 else'to_plantation'if b==9 else'to_mosaic'if b==21 else'to_unobserved'if b in {0,27}else'to_other'
    elif a not in codes and b in codes:event='inflow_from_unobserved'if a in {0,27}else'inflow_from_other'
    elif a in codes and b in codes:event='group_retained'
    if event:
     for level,unit in [('national','Brazil'),('state',st),('biome',bio)]:flows[level,unit,group,event,year]+=value
 flowrows=[dict(level=l,unit=u,group=g,event=e,start=y,end=y+1,transition_event_area_ha=v,independent_validation=False)for(l,u,g,e,y),v in sorted(flows.items())]
 save('data/BRA_C11_annual_transition_events_F12.csv',flowrows)
 # Do not silently accept mismatching transition/coverage operands.
 audits=[]
 for label,margin in [('from',margins0),('to',margins1)]:
  worst=0.;sumabs=0.;national=collections.defaultdict(float)
  for key in sorted(set(margin)|{k for k in coverage if k[3]in(range(2015,2023)if label=='from'else range(2016,2024))}):
   d=margin.get(key,0.)-coverage.get(key,0.);worst=max(worst,abs(d));sumabs+=abs(d);national[key[3]]+=d
  require(worst<.01,'Transition margins do not match coverage')
  audits.append(dict(margin=label,max_state_biome_class_residual_ha=worst,sum_absolute_residual_ha=sumabs,national_total_residual_by_year_ha=dict(national)))
 balances=[]
 for level,unit in units:
  for group in ('formations','formations_plus_savanna'):
   for y in range(2015,2023):
    out=sum(v for(l,u,g,e,yy),v in flows.items()if(l,u,g,yy)==(level,unit,group,y)and e.startswith('to_'))
    inflow=sum(v for(l,u,g,e,yy),v in flows.items()if(l,u,g,yy)==(level,unit,group,y)and e.startswith('inflow_'))
    net=agg[level,unit,group,y+1]-agg[level,unit,group,y]
    balances.append(dict(level=level,unit=unit,group=group,start=y,end=y+1,inflow_ha=inflow,outflow_ha=out,transition_net_ha=inflow-out,coverage_net_ha=net,residual_ha=inflow-out-net))
 require(max(abs(r['residual_ha'])for r in balances)<.01,'Transition mass balance fails')
 save('data/BRA_C11_transition_balance_F12.csv',balances)
 summary=dict(source=identity,coverage_rows=len(keys),transition_rows=trows,leaf_class_codes=sorted(classes),states=len({k[0]for k in keys}),biomes=len({k[1]for k in keys}),national_total_ha_by_year={str(y):agg['national','Brazil','all_classes',y]for y in years},margin_audits=audits,max_group_balance_residual_ha=max(abs(r['residual_ha'])for r in balances),annual_transition_sums_are_not_unique_multiyear_area=True,direct_2015_2023_transition_column_available='p2015_2023'in th,national_extent_estimated_as_mapped_classification=True,national_biomass_stock_or_accuracy_adjusted_extent_estimated=False,footprint_not_F11_local_window=True)
 (ROOT/'metadata/BRA_C11_analysis_F12.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps(summary,indent=2))
 for r in changes:
  if r['level']=='national':print(r)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--workbook',type=Path,required=True);run(p.parse_args().workbook)
