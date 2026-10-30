#!/usr/bin/env python3
"""Stream old public reference archive; audit compatibility, not map accuracy.
Only aggregate diagnostics are deposited; no 98 MB decompression is written.
"""
import collections,csv,hashlib,io,json,zipfile
from pathlib import Path
from accounts_F12 import require,save
ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT.parent/'.cache/F12/raw'


def nonblank(x):return x.strip().lower()not in {'','nan','na','null','none'}

def run():
 registry=json.loads((ROOT/'metadata/source_registry_F12.json').read_text());p=CACHE/'BRA_reference_v21.zip';require(hashlib.sha256(p.read_bytes()).hexdigest()==registry[p.name]['sha256'],'Reference source drift')
 z=zipfile.ZipFile(p);require(len(z.infolist())==1 and z.infolist()[0].file_size<125000000,'Unexpected archive expansion');counts=collections.defaultdict(collections.Counter);tokens=collections.defaultdict(collections.Counter);ids=set()
 with z.open(z.namelist()[0])as raw:
  reader=csv.DictReader(io.TextIOWrapper(raw,encoding='utf-8-sig'));fields=reader.fieldnames
  for r in reader:
   require(r['TARGETID']not in ids,'Duplicate reference ID');ids.add(r['TARGETID']);bio=r['BIOMA_250K']
   a,b=nonblank(r['CLASS_2015']),nonblank(r['CLASS_2023'])
   observed=a and b and all('OBSERVADO'not in r[k].upper()for k in ['CLASS_2015','CLASS_2023']);nontraining=r['AMOSTRA_AM']=='0';clear=r['BORDA_2015']=='0'and r['BORDA_2023']=='0'
   for unit in ['all',bio]:
    counts[unit]['points']+=1;counts[unit]['2015_nonblank']+=a;counts[unit]['2023_nonblank']+=b;counts[unit]['paired_nonblank']+=a and b;counts[unit]['paired_observed_nontraining']+=observed and nontraining;counts[unit]['paired_observed_nontraining_nonedge_both']+=observed and nontraining and clear
   for k in ['CLASS_2023','AMOSTRAS','AMOSTRA_AM','BORDA_2015','BORDA_2023']:tokens[k][r[k]]+=1
 rows=[dict(unit=u,**c)for u,c in sorted(counts.items())];save('data/BRA_reference_v21_label_completeness_F12.csv',rows)
 status=dict(source=registry[p.name],uncompressed_bytes=z.infolist()[0].file_size,point_count=len(ids),diagnostics=dict(counts['all']),token_counts={k:dict(v)for k,v in tokens.items()},weight_fields_present=[x for x in fields if any(w in x.upper()for w in ['PESO','PROB'])],reference_collection_current_C11='3',archive_reference_collection='2.1',current_C11_reference_temporal_extent=[1985,2024],reference_collection_compatible=False,paired_nonblank_fraction=counts['all']['paired_nonblank']/len(ids),spatial_representativeness_of_nonblank_2023_not_established=True,accuracy_or_area_estimate_computed=False,pooled_accuracy_not_transferred_to_change_bounds=True)
 (ROOT/'metadata/BRA_reference_compatibility_F12.json').write_text(json.dumps(status,indent=2)+'\n');print(json.dumps(status,indent=2))

if __name__=='__main__':run()
