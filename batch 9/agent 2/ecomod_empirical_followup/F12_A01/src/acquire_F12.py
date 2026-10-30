#!/usr/bin/env python3
"""Bounded source retrieval with first-discovery identities and drift rejection.
No credentials, source raster arrays or third-party PDF bodies are deposited.
"""
import argparse,hashlib,json
from pathlib import Path
import requests
ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT.parent/'.cache/F12/raw'
SOURCES={
 'BRA_C11_biome_state.xlsx':'https://brasil.mapbiomas.org/wp-content/uploads/sites/3/2026/08/MAPBIOMAS_BRAZIL-COL.11-BIOME_STATE.xlsx',
 'IDN_C41.xlsx':'https://landy.mapbiomas.id/storage/files/statistics_lulc_indonesia_col4-1 (1) (1).xlsx',
 'BRA_C11_accuracy.pdf':'https://brasil.mapbiomas.org/wp-content/uploads/sites/3/2026/08/Accuracy-Assessment-Appendix-Collection-11-v1.pdf',
 'BRA_reference_v21.zip':'https://brasil.mapbiomas.org/wp-content/uploads/sites/4/2024/08/mapbiomas_85k_col2_1_points_w_edge_and_edited_v1.csv_-1.zip'}
SOURCES.update({
 'IDN_C3_coverage.xlsx':'https://landy.mapbiomas.id/storage/files/statistic_indonesia_coverage_col_3.xlsx',
 'IDN_C41_ATBD.pdf':'https://landy.mapbiomas.id/assets/files/ATBD Mapbiomas ID Col 4.1 EN.pdf',
 'FIN_NFI13_paper.pdf':'https://jukuri.luke.fi/server/api/core/bitstreams/eb3d5f26-f9f3-4aae-9288-0d3e67683b4f/content',
 'FIN_NFI12_tables.xlsx':'https://www.silvafennica.fi/supp_files/article10662/S2.xlsx',
 'FIN_NFI13_tables.xlsx':'https://www.silvafennica.fi/supp_files/article24045/S2.xlsx'})
CAP=25000000

def retrieve(name,url,cap=CAP,offline=False):
 CACHE.mkdir(parents=True,exist_ok=True);path=CACHE/name;registry=ROOT/'metadata/source_registry_F12.json'
 old=json.loads(registry.read_text())if registry.exists()else{}
 if path.exists():data=path.read_bytes();final=old.get(name,{}).get('final_url',url)
 else:
  if offline:raise ValueError('Missing offline cache: '+name)
  with requests.get(url,stream=True,timeout=(20,120))as r:
   r.raise_for_status();buf=bytearray();final=r.url
   if int(r.headers.get('Content-Length',0))>cap:raise ValueError('Declared response exceeds cap: '+name)
   for block in r.iter_content(65536):
    buf.extend(block)
    if len(buf)>cap:raise ValueError('Streaming source exceeds cap: '+name)
  data=bytes(buf);path.write_bytes(data)
 if len(data)>cap:raise ValueError('Cached source exceeds cap')
 sha=hashlib.sha256(data).hexdigest()
 if name in old and (sha!=old[name]['sha256']or len(data)!=old[name]['bytes']):raise ValueError('Source identity drift; explicit amendment required')
 old[name]=dict(url=url,final_url=final,bytes=len(data),sha256=sha,cap_bytes=cap,raw_redistributed=False)
 registry.write_text(json.dumps(old,indent=2)+'\n');return path,old[name]

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('names',nargs='+',choices=list(SOURCES));p.add_argument('--offline',action='store_true');a=p.parse_args()
 for name in a.names:
  _,receipt=retrieve(name,SOURCES[name],offline=a.offline);print(name,json.dumps(receipt))
