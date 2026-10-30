#!/usr/bin/env python3
"""Prior-collection AND reported-support sensitivity; not a pure version-effect estimate."""
import collections,csv,hashlib,json,math
from pathlib import Path
from openpyxl import load_workbook
from accounts_F12 import require,save
ROOT=Path(__file__).resolve().parents[1]
ISLANDS={'Sumatera','Kalimantan','Sulawesi','Jawa','Bali & Nusa Tenggara','Maluku','Papua'}

def run():
 p=ROOT.parent/'.cache/F12/raw/IDN_C3_coverage.xlsx';identity=json.loads((ROOT/'metadata/source_registry_F12.json').read_text())[p.name];require(hashlib.sha256(p.read_bytes()).hexdigest()==identity['sha256'],'Collection 3 source drift')
 w=load_workbook(p,read_only=True,data_only=True);it=iter(w['dbase'].values);h=next(it);ix={k:h.index(k)for k in ['area','class_code','territory_code','year','class_level_1_en','class_level_2_en','provinsi','pulau']};totals=collections.defaultdict(float);forest=collections.defaultdict(float);geo=collections.defaultdict(float);labels={};keys=set();n=0;excluded=collections.Counter();islands=collections.Counter()
 for row in it:
  if not row or row[0]is None:continue
  y=int(row[ix['year']])
  if y not in {2015,2023}:continue
  island=str(row[ix['pulau']]);a=float(row[ix['area']]);code=int(row[ix['class_code']]);key=(row[ix['territory_code']],code,y)
  require(key not in keys and math.isfinite(a)and a>=0,'Duplicate or invalid source value');keys.add(key)
  labels[code]=str(row[ix['class_level_2_en']])
  if island not in ISLANDS:excluded[island]+=1;continue
  n+=1;islands[island]+=1;totals[y]+=a;geo[island,y]+=a
  level=str(row[ix['class_level_1_en']]).strip()
  # Forest is the source's own level-one class, excluding plantations in Agriculture.
  if level=='1. Forest':forest[y]+=a
 require(set(excluded)<={'Island buffered 20 km'}and set(islands)==ISLANDS,'Unexpected country partition token')
 rows=[dict(collection='3',year=y,all_class_area_ha=totals[y],forest_area_ha=forest[y],source_forest_definition='Source level-one Forest, plantations excluded',same_boundary_as_collection_41_certified=False)for y in [2015,2023]];save('data/IDN_C3_national_extent_sensitivity_F12.csv',rows)
 c41=next(r for r in csv.DictReader((ROOT/'data/IDN_C41_extent_changes_F12.csv').open())if r['level']=='national'and r['group']=='mapped_forest')
 summary=dict(source=identity,endpoint_rows_included=n,island_groups=dict(islands),excluded_nonstandard_island_tokens=dict(excluded),class_labels=labels,C3_all_class_area_ha=dict(totals),C3_forest_difference_ha=forest[2023]-forest[2015],C3_forest_percent_change=100*(forest[2023]-forest[2015])/forest[2015],C41_forest_difference_ha=float(c41['difference_ha']),C41_forest_percent_change=float(c41['percent_change']),C3_minus_C41_total_support_area_2015_ha=totals[2015]-189044390.24458277,pure_version_effect_estimated=False,statistical_uncertainty_interval=False,reason='Provider tables use different reported geographic subdivisions/support; source-version and support effects are not separated.')
 (ROOT/'metadata/IDN_collection_sensitivity_F12.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))

if __name__=='__main__':run()
