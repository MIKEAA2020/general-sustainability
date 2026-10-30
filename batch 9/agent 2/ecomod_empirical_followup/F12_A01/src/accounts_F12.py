#!/usr/bin/env python3
"""Actual primary 2015-2023, endpoint sensitivity and inherited 2010-2020 accounts."""
import argparse,csv,collections,hashlib,json,math
from pathlib import Path
from openpyxl import load_workbook
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'reference'
EXPECTED='26e4f5c78d9fe20cb5cd51c073815157566711b53278a1f9118d7726ab60ad1b'
CANDIDATES=('BRA','IDN','COD','CMR','CAN','FIN','FRA','AUS')
COMPONENTS=('crop','grazing','forest','fishing','built')

def require(ok,msg):
 if not ok:raise ValueError(msg)
def save(name,rows):
 p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w',newline='')as f:
  w=csv.DictWriter(f,list(rows[0]));w.writeheader();w.writerows(rows)
def delta_pct(a,b):return None if a==0 else 100*(b-a)/a
def sign(a,b,tolerance=1.):
 d=b-a;return 'increase'if d>tolerance else'decrease'if d< -tolerance else'unresolved_at_rounding_scale'
def domains(r):
 c={k:float(r['biocap_'+k+'_gha'])for k in COMPONENTS};total=float(r['biocap_total_gha'])
 return dict(total=total,terrestrial_excluding_fishing=total-c['fishing'],excluding_built=total-c['built'],terrestrial_excluding_built=total-c['fishing']-c['built'],forest_component=c['forest'])

def run(workbook):
 b=workbook.read_bytes();require(hashlib.sha256(b).hexdigest()==EXPECTED,'Account source identity drift')
 with (BASE/'account_availability_F11.csv').open()as f:availability=list(csv.DictReader(f))
 eligible={r['ISO3']for r in availability if r['account_available']=='True'}
 require(len(eligible)==183,'Inherited availability changed')
 w=load_workbook(workbook,read_only=True,data_only=True);it=iter(w['national_data'].values);head=next(it);groups=collections.defaultdict(dict);count=0
 for row in it:
  if row[0]is None:continue
  r=dict(zip(head,row));iso=r['country_ISO3'];year=int(r['year']);require(year not in groups[iso],'Duplicate country-year');groups[iso][year]=r;count+=1
 require(count==13652 and len(groups)==236,'Wrong national source dimensions')
 annual=[];comparisons=[];contributions=[];decomposition=[];secondary_exclusions=[]
 allowed={'+++','++','+'}
 for iso in sorted(eligible):
  for year in range(2015,2024):
   r=groups[iso][year];require(r['flag']in allowed,'Disallowed annual account flag');out=dict(ISO3=iso,country=r['country_name'],year=year,candidate=iso in CANDIDATES,flag=r['flag'])
   for k in COMPONENTS:out['biocap_'+k+'_gha']=r['biocap_'+k+'_gha']
   out.update(biocap_total_gha=r['biocap_total_gha'],population_persons=1000*r['pop_1000_persons'],biocap_total_per_person_gha=r['biocap_total_gha']/(1000*r['pop_1000_persons']),account_forest_area_ha=r['area_forest_ha'],account_crop_area_ha=r['area_crop_ha'],component_sum_minus_total_gha=sum(r['biocap_'+k+'_gha']for k in COMPONENTS)-r['biocap_total_gha'])
   annual.append(out)
  for start,end in ((2015,2023),(2015,2022),(2010,2020)):
   if any(y not in groups[iso]or groups[iso][y]['flag']not in allowed for y in (start,end)):
    require(start==2010,'Primary account endpoint unexpectedly unavailable');secondary_exclusions.append(dict(ISO3=iso,start=start,end=end,reason='Endpoint missing or disallowed flag'));continue
   r0,r1=groups[iso][start],groups[iso][end];t0,t1=float(r0['biocap_total_gha']),float(r1['biocap_total_gha']);d0,d1=domains(r0),domains(r1)
   for domain in d0:
    # Differences of n rounded components have a conservative n-gha endpoint-difference budget.
    tolerance={'total':1.,'terrestrial_excluding_fishing':2.,'excluding_built':2.,'terrestrial_excluding_built':3.,'forest_component':1.}[domain]
    comparisons.append(dict(ISO3=iso,country=r0['country_name'],candidate=iso in CANDIDATES,start=start,end=end,domain=domain,value_start_gha=d0[domain],value_end_gha=d1[domain],difference_gha=d1[domain]-d0[domain],percent_change=delta_pct(d0[domain],d1[domain]),direction=sign(d0[domain],d1[domain],tolerance),rounding_difference_budget_gha=tolerance,physical_asset_outcome=False))
   pop0,pop1=1000*r0['pop_1000_persons'],1000*r1['pop_1000_persons']
   comparisons.append(dict(ISO3=iso,country=r0['country_name'],candidate=iso in CANDIDATES,start=start,end=end,domain='per_person_total',value_start_gha=t0/pop0,value_end_gha=t1/pop1,difference_gha=t1/pop1-t0/pop0,percent_change=delta_pct(t0/pop0,t1/pop1),direction=sign(t0/pop0,t1/pop1,0.),rounding_difference_budget_gha=None,physical_asset_outcome=False))
   compdiff=0.
   for k in COMPONENTS:
    a,b=float(r0['biocap_'+k+'_gha']),float(r1['biocap_'+k+'_gha']);compdiff+=b-a
    contributions.append(dict(ISO3=iso,start=start,end=end,component=k,value_start_gha=a,value_end_gha=b,difference_gha=b-a,contribution_percentage_points_of_initial_total=100*(b-a)/t0 if t0 else None))
   require(abs(compdiff-(t1-t0))<=6.000001,'Component difference exceeds rounding budget')
   a0,a1=float(r0['area_forest_ha']),float(r1['area_forest_ha']);bf0,bf1=float(r0['biocap_forest_gha']),float(r1['biocap_forest_gha'])
   if a0>0 and a1>0:
    f0,f1=bf0/a0,bf1/a1;area=(a1-a0)*(f0+f1)/2;factor=(f1-f0)*(a0+a1)/2
    require(abs(area+factor-(bf1-bf0))<max(1e-6,abs(bf1-bf0)*1e-12),'Account decomposition identity failed')
    decomposition.append(dict(ISO3=iso,start=start,end=end,forest_account_difference_gha=bf1-bf0,area_contribution_gha=area,factor_contribution_gha=factor,factor_start_gha_per_ha=f0,factor_end_gha_per_ha=f1,physical_yield_or_biomass_inferred=False))
 save('data/accounts_annual_183_F12.csv',annual);save('data/accounts_changes_183_F12.csv',comparisons);save('data/accounts_component_contributions_F12.csv',contributions);save('data/accounts_forest_component_decomposition_F12.csv',decomposition)
 save('data/accounts_candidate_changes_F12.csv',[r for r in comparisons if r['candidate']])
 summary=dict(account_workbook_sha256=EXPECTED,national_rows=count,identifiers=236,eligible_identifiers=183,annual_rows=len(annual),all_eight_candidates_retained=True,primary_window=[2015,2023],sensitivity_window=[2015,2022],inherited_secondary_window=[2010,2020],secondary_comparable_identifiers=len([r for r in comparisons if r['start']==2010 and r['domain']=='total']),secondary_exclusions=secondary_exclusions,primary_total_directions=dict(collections.Counter(r['direction']for r in comparisons if r['end']==2023 and r['domain']=='total')),national_physical_changes_estimated=False,component_change_not_equal_physical_asset_change=True)
 (ROOT/'metadata/accounts_analysis_F12.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps(summary,indent=2))
 for iso in CANDIDATES:
  print(iso,[(r['domain'],round(r['percent_change'],4),r['direction'])for r in comparisons if r['ISO3']==iso and r['end']==2023])

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--workbook',type=Path,required=True);run(p.parse_args().workbook)
