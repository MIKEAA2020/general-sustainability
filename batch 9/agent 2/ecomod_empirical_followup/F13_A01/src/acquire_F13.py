#!/usr/bin/env python3
"""Bounded source retrieval with first-discovery identities and drift rejection.
No credentials, source raster arrays or third-party PDF bodies are deposited.
"""
import argparse,hashlib,json
from pathlib import Path
import requests
ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT.parent/'.cache/F13/raw'
CAP=25000000

def retrieve(name,url,cap=CAP,offline=False):
 CACHE.mkdir(parents=True,exist_ok=True);path=CACHE/name;registry=ROOT/'metadata/source_registry_F13.json'
 old=json.loads(registry.read_text())if registry.exists()else{}
 if name in old and url!=old[name]['url']:raise ValueError('Source URL drift; explicit amendment required')
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
 registry=json.loads((ROOT/'metadata/source_registry_F13.json').read_text());SOURCES={k:v['url']for k,v in registry.items()}
 p=argparse.ArgumentParser();p.add_argument('names',nargs='+',choices=list(SOURCES));p.add_argument('--offline',action='store_true');a=p.parse_args()
 for name in a.names:
  _,receipt=retrieve(name,SOURCES[name],offline=a.offline);print(name,json.dumps(receipt))
