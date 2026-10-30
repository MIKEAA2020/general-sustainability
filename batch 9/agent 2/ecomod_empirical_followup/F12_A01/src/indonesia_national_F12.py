#!/usr/bin/env python3
"""Independent national MapBiomas Indonesia C4.1 classification analysis.
Published province/island partitions; no assumption of agreement with NFA land definitions.
"""
import argparse,collections,hashlib,json,math
from pathlib import Path
from openpyxl import load_workbook
from accounts_F12 import require,save,delta_pct
ROOT=Path(__file__).resolve().parents[1]
FOREST={3,5,76}
GROUPS={'mapped_forest':FOREST,'forest_formation':{3},'mangrove':{5},'peat_swamp_forest':{76},'oil_palm':{35},'pulpwood_plantation':{9},'rice_paddy':{40},'other_agriculture':{21},'other_natural_vegetation':{13},'water':{31,33},'unobserved':{0,27}}

def run(path):
 identity=json.loads((ROOT/'metadata/source_registry_F12.json').read_text())['IDN_C41.xlsx']
 require(hashlib.sha256(path.read_bytes()).hexdigest()==identity['sha256'],'IDN source identity drift')
 w=load_workbook(path,read_only=True,data_only=True);it=iter(w['COVERAGE'].values);h=next(it);idx={y:h.index(f'y{y}')for y in range(2015,2024)}
 coverage={};keys=set();agg=collections.defaultdict(float);codes=set();labels={}
 for row in it:
  if row[0]is None:continue
  nation,island,province,code=row[1],row[2],row[3],int(row[4]);key=(island,province,code)
  require(nation=='Indonesia'and key not in keys,'Duplicate/nonnational coverage row');keys.add(key);codes.add(code)
  require(code not in {1,10,18,22,26},'Hierarchy parents must not be summed')
  labels[code]=str(row[8])
  for y,j in idx.items():
   a=row[j];require(isinstance(a,(int,float))and math.isfinite(a)and a>=0,'Invalid coverage value');coverage[island,province,code,y]=a
   for level,unit in [('national','Indonesia'),('island',island),('province',province)]:
    agg[level,unit,'all_classes',y]+=a
    for group,cc in GROUPS.items():
     if code in cc:agg[level,unit,group,y]+=a
 save('data/IDN_C41_class_annual_by_province_F12.csv',[dict(island=i,province=p,class_code=c,year=y,area_ha=v)for(i,p,c,y),v in sorted(coverage.items())])
 units=sorted({(l,u)for l,u,g,y in agg});annual=[];changes=[]
 for level,unit in units:
  for group in ['all_classes']+list(GROUPS):
   for y in range(2015,2024):annual.append(dict(level=level,unit=unit,group=group,year=y,area_ha=agg[level,unit,group,y],classification_only=True))
   a,b=agg[level,unit,group,2015],agg[level,unit,group,2023];total=agg[level,unit,'all_classes',2015]
   changes.append(dict(level=level,unit=unit,group=group,start=2015,end=2023,area_start_ha=a,area_end_ha=b,difference_ha=b-a,percent_change=delta_pct(a,b),symmetric_endpoint_error_break_even_ha=abs(b-a)/2,symmetric_endpoint_error_break_even_pct_total=100*abs(b-a)/(2*total)if total else None,statistical_confidence_claimed=False))
 save('data/IDN_C41_extent_annual_F12.csv',annual);save('data/IDN_C41_extent_changes_F12.csv',changes)
 it=iter(w['TRANSITION'].values);th=next(it);pcols={y:th.index(f'p{y}_{y+1}')for y in range(2015,2023)}
 margins0=collections.defaultdict(float);margins1=collections.defaultdict(float);flows=collections.defaultdict(float);tkeys=set();rows=0
 for row in it:
  if row[0]is None:continue
  island,province,a,b=row[2],row[3],int(row[4]),int(row[5]);key=(island,province,a,b)
  require(row[1]=='Indonesia'and key not in tkeys,'Duplicate transition row');tkeys.add(key);rows+=1
  for y,j in pcols.items():
   v=row[j];require(isinstance(v,(int,float))and math.isfinite(v)and v>=0,'Invalid transition value')
   margins0[island,province,a,y]+=v;margins1[island,province,b,y+1]+=v
   event=None
   if a in FOREST and b not in FOREST:
    event='to_oil_palm'if b==35 else'to_pulpwood_plantation'if b==9 else'to_rice_paddy'if b==40 else'to_other_agriculture'if b==21 else'to_unobserved'if b in {0,27}else'to_other'
   elif a not in FOREST and b in FOREST:event='inflow_from_unobserved'if a in {0,27}else'inflow_from_other'
   elif a in FOREST and b in FOREST:event='forest_retained'
   if event:
    for level,unit in [('national','Indonesia'),('island',island),('province',province)]:flows[level,unit,event,y]+=v
 flowrows=[dict(level=l,unit=u,event=e,start=y,end=y+1,transition_event_area_ha=v,independent_validation=False)for(l,u,e,y),v in sorted(flows.items())]
 save('data/IDN_C41_annual_transition_events_F12.csv',flowrows)
 audits=[]
 for label,margin in [('from',margins0),('to',margins1)]:
  yy=range(2015,2023)if label=='from'else range(2016,2024);relevant={k for k in coverage if k[3]in yy};residual=[margin.get(k,0)-coverage.get(k,0)for k in sorted(set(margin)|relevant)]
  require(max(map(abs,residual))<.01,'Transition margins do not match coverage')
  audits.append(dict(margin=label,max_island_province_class_residual_ha=max(map(abs,residual)),sum_absolute_residual_ha=sum(map(abs,residual))))
 balances=[]
 for level,unit in units:
  for y in range(2015,2023):
   out=sum(v for(l,u,e,yy),v in flows.items()if(l,u,yy)==(level,unit,y)and e.startswith('to_'));inc=sum(v for(l,u,e,yy),v in flows.items()if(l,u,yy)==(level,unit,y)and e.startswith('inflow_'));net=agg[level,unit,'mapped_forest',y+1]-agg[level,unit,'mapped_forest',y]
   balances.append(dict(level=level,unit=unit,start=y,end=y+1,inflow_ha=inc,outflow_ha=out,transition_net_ha=inc-out,coverage_net_ha=net,residual_ha=inc-out-net))
 require(max(abs(r['residual_ha'])for r in balances)<.01,'Transition mass balance fails')
 save('data/IDN_C41_transition_balance_F12.csv',balances)
 summary=dict(source=identity,coverage_rows=len(keys),transition_rows=rows,islands=len({k[0]for k in keys}),provinces=len({k[1]for k in keys}),leaf_class_codes=sorted(codes),class_labels=labels,forest_classes=sorted(FOREST),national_area_by_year_ha={y:agg['national','Indonesia','all_classes',y]for y in range(2015,2024)},margin_audits=audits,max_group_balance_residual_ha=max(abs(r['residual_ha'])for r in balances),national_mapped_extents_available=True,calibrated_biomass_change_estimated=False,direct_2015_2023_transition_column_available='p2015_2023'in th,annual_event_sums_not_unique_multiyear_conversion=True,NFA_territory_equivalence_not_certified_by_matching_names=True)
 (ROOT/'metadata/IDN_C41_analysis_F12.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
 for r in changes:
  if r['level']=='national':print(r)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--workbook',type=Path,required=True);run(p.parse_args().workbook)
