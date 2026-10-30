#!/usr/bin/env python3
"""Acquire official Finnish inventory and forest-account tables with actual time domains.
Never relabel a 2014-2018 inventory as an independently observed 2015 endpoint.
"""
import argparse,hashlib,itertools,json,math
from pathlib import Path
import requests
from accounts_F12 import require,save
ROOT=Path(__file__).resolve().parents[1]
INV='https://statdb.luke.fi/PxWeb/api/v1/en/LUKE/met/zzz_lak/06%20Metsavarat/'
ACCOUNT='https://statdb.luke.fi/PxWeb/api/v1/en/LUKE/met/mettil/'


def decode(j):
 ids=j['id'];sizes=j['size'];values=j['value'];require(math.prod(sizes)==len(values),'Unexpected sparse JSON-stat response')
 axes=[]
 for name,size in zip(ids,sizes):
  c=j['dimension'][name]['category'];index=c['index'];ordered=sorted(index,key=index.get)if isinstance(index,dict)else index
  require(len(ordered)==size,'JSON-stat dimension mismatch');axes.append([(x,c['label'][x])for x in ordered])
 for i,labels in enumerate(itertools.product(*axes)):
  yield {**{k:v[0]for k,v in zip(ids,labels)},**{k+'_label':v[1]for k,v in zip(ids,labels)},'value':values[i]}


def fetch(tag,url,select,offline=False):
 meta=ROOT/'metadata'/f'{tag}_schema_F12.json';response=ROOT/'data'/f'{tag}_response_F12.json';querypath=ROOT/'metadata'/f'{tag}_query_F12.json'
 if offline:
  return json.loads(response.read_text())
 r=requests.get(url,timeout=(20,90));r.raise_for_status();m=r.json();query=[]
 for v in m['variables']:
  values=select.get(v['code'],v['values'])
  require(set(values)<=set(v['values']),'Query includes nonexistent source code')
  query.append(dict(code=v['code'],selection=dict(filter='item',values=values)))
 payload=dict(query=query,response=dict(format='json-stat2'));r=requests.post(url,json=payload,timeout=(20,90));r.raise_for_status();j=r.json();require(len(r.content)<1000000,'Oversized statistical response')
 meta.write_text(json.dumps(m,indent=2)+'\n');querypath.write_text(json.dumps(dict(url=url,query=payload,response_sha256=hashlib.sha256(r.content).hexdigest()),indent=2)+'\n')
 if response.exists():
  require(json.loads(response.read_text())==j,'Official table changed: amendment required')
 response.write_text(json.dumps(j,indent=2)+'\n');return j


def run(offline=False):
 region=['1','1.1.21'];cycles=['11','12','13','14']
 biomass=fetch('FIN_inventory_biomass',INV+'1.29_Puuston_biomassa_metsa_ja_kitumaalla.px',{'inventointi':cycles,'maakunta':region,'puulaji':['Yhteensä']},offline)
 volume=fetch('FIN_inventory_volume',INV+'1.16_Puuston_tilavuus_metsa_ja_kitumaalla_pu.px',{'inventointi':cycles,'maakunta':region,'puulaji':['Koko puusto']},offline)
 area=fetch('FIN_inventory_area',INV+'1.01_Metsatalousmaa.px',{'inventointi':cycles,'maakunta':region},offline)
 forest_account=fetch('FIN_forest_account_volume',ACCOUNT+'0200_mettil.px',{'INFO':['M3_PUU'],'A':['2022','2023'],'MLK':['FOR']},offline)
 bio_rows=[];bg={}
 for r in decode(biomass):
  row=dict(inventory=r['inventointi_label'],inventory_code=r['inventointi'],region=r['maakunta_label'],component=r['puun osa_label'],biomass_million_tonnes=r['value'],standard_error_supplied=False,exact_2015_2023_endpoint=False)
  bio_rows.append(row);bg.setdefault((r['inventointi'],r['maakunta']),{})[r['puun osa_label']]=r['value']
 save('data/FIN_inventory_biomass_components_F12.csv',bio_rows)
 summary_rows=[]
 for (cycle,reg),components in bg.items():
  values=[components[k]for k in ['Stems','Branches and foliage','Stumps and roots','Biomass of trees, total']]
  if not all(isinstance(x,(int,float))for x in values):continue
  stems,branches,below,total=values;require(abs(stems+branches+below-total)<=2,'Component rounding discrepancy too large')
  summary_rows.append(dict(inventory_code=cycle,inventory=biomass['dimension']['inventointi']['category']['label'][cycle],region=biomass['dimension']['maakunta']['category']['label'][reg],total_living_biomass_Mt=total,stems_plus_branches_foliage_Mt=stems+branches,stumps_roots_Mt=below,component_sum_minus_total_Mt=stems+branches+below-total,CCI_AGB_equivalence_established=False,exact_2015_2023_endpoint=False))
 save('data/FIN_inventory_biomass_operational_summaries_F12.csv',summary_rows)
 vr=[dict(inventory=r['inventointi_label'],region=r['maakunta_label'],volume_million_m3=r['value'],standard_error_supplied=False)for r in decode(volume)];save('data/FIN_inventory_volume_F12.csv',vr)
 ar=[dict(inventory=r['inventointi_label'],region=r['maakunta_label'],land_class=r['maaluokka_label'],area_thousand_ha=r['value'])for r in decode(area)];save('data/FIN_inventory_area_F12.csv',ar)
 fr=[dict(year=int(r['A']),land_class=r['MLK_label'],item=r['PMPA_label'],volume_thousand_m3=r['value'],unit=r['INFO_label'],independent_of_NFI=False,AGB_mass=False)for r in decode(forest_account)];save('data/FIN_forest_account_volume_2022_2023_F12.csv',fr)
 m12=next(r for r in summary_rows if r['inventory_code']=='12'and r['region']=='WHOLE COUNTRY');m13=next(r for r in summary_rows if r['inventory_code']=='13'and r['region']=='WHOLE COUNTRY')
 summary=dict(source='Official Luke archived inventory API and forest accounts API',archived_source_recovered_via_zzz_lak=True,national_cycle_total_biomass_difference_Mt=m13['total_living_biomass_Mt']-m12['total_living_biomass_Mt'],operational_stems_branches_foliage_difference_Mt=m13['stems_plus_branches_foliage_Mt']-m12['stems_plus_branches_foliage_Mt'],inventories=['2014-2018','2019-2023'],Aland_explicitly_in_source=True,cycle_notes=biomass['dimension']['inventointi']['category'].get('note',{}),marginal_biomass_variance_supplied=False,primary_2015_2023_biomass_comparison_admitted=False,reason='Cycle windows are not exact 2015/2023 endpoint observations; total biomass includes stumps/roots; table supplies no biomass variance or cross-cycle covariance. Forest-account volume is a different quantity and partly derives from NFI.',new_quantitative_physical_inventory_evidence_acquired=True)
 (ROOT/'metadata/FIN_inventory_assessment_F12.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2));print('Forest account volume rows',fr)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--offline',action='store_true');run(p.parse_args().offline)
