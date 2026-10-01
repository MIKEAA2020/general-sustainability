#!/usr/bin/env python3
"""Retrieve user-specified family manuscripts plus adjacent source-year versions.

Read-only GitHub tree/blob SHA inventory. Paths under 'paper rewrites/latex'.
Original source files are stored verbatim; no manuscript is overwritten.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import urllib.request, urllib.parse, hashlib, json, re
BASE='https://api.github.com/repos/MIKEAA2020/general-sustainability'
BRANCH='e2-v3-source-year'
PREFIX='arena agent 1/paper rewrites/latex/'
ROOT=Path('/home/user/content_audit/family_depth')
PAT=Path('/home/user/uploads/github_pat.txt').read_text().strip()
H={'Authorization':'Bearer '+PAT,'Accept':'application/vnd.github+json','User-Agent':'family-depth-preservation'}
req=urllib.request.Request(BASE+'/git/trees/'+BRANCH+'?recursive=1',headers=H)
tree=json.load(urllib.request.urlopen(req,timeout=120));assert not tree['truncated']
items={x['path'][len(PREFIX):]:x for x in tree['tree'] if x['type']=='blob' and x['path'].startswith(PREFIX)}
series={
'obstr':('paper2_obstruction_calculus_v','_Automatica_routes.tex',[53,54,55,56]),
'comp':('paper2_computational_certification_v','.tex',[16,17,18,19,20]),
'ws':('paper2_worked_systems_v','.tex',[15,16,17]),
'minimax':('minimax_dual_certificates_v','.tex',[8,9,10,11,12]),
'ebc':('paper2_exact_belief_computation_v','.tex',[8,9,10,11,12,13]),
'psuff':('paper2_probabilistic_sufficiency_v','.tex',[10,11,12,13,14]),
'arv':('applied_regime_viability_v','.tex',[7,8,9]),
'e1':('paperE1_cod_forecast_ladder_v','.tex',[56,57,58,59,60]),
}
expected={}
for family,(pre,suf,vers) in series.items():
 for v in vers:expected[pre+str(v)+suf]=family
for v in [49,50,51]:
 expected[f'paper2_obstruction_calculus_v{v}_Automatica_routes_supplementary.tex']='obstr_supp'
for v in [4,5]:
 expected[f'paper2_computational_certification_v{v}_supplementary.tex']='comp_supp'
expected['paper2_computational_certification_supplementary_v6.tex']='comp_supp'
exact=[
 'paper2_obstruction_calculus_v55_Automatica_routes.pdf',
 'paper2_obstruction_calculus_v51_Automatica_routes_supplementary.pdf',
 'paper2_computational_certification_v17.pdf',
 'paper2_computational_certification_supplementary_v6.pdf',
 'paper2_worked_systems_v17.pdf',
 'minimax_dual_certificates_v9.pdf',
 'paper2_exact_belief_computation_v8.pdf',
 'paper2_probabilistic_sufficiency_v10.pdf',
 'applied_regime_viability_v8.pdf',
 'paperE1_cod_forecast_ladder_v58.pdf',
 'paper2_computational_certification_v17_verification.py',
 'paper2_worked_systems_v17_verification.py',
 'minimax_dual_certificates_v9_verify.py',
 'paper2_exact_belief_computation_v8_verification.py',
 'paper2_probabilistic_sufficiency_v10_verification.py',
 'applied_regime_viability_v8_verification.py',
 'paperE1_cod_forecast_ladder_v58_verification.py',
 # This separate 2016/2021 RAM vintage is needed by the named E1 verifier;
 # it is not part of the user-specified wave-e-cod calibration directory.
 'paperE1_calibration_data_v1_ram_timeseries.csv',
]
for n in exact:expected[n]='user_exact'
for n in items:
 if n.startswith('paperE1_calibration_data_v1_wave_e_cod/'):
  expected[n]='e1_data'
missing=sorted(set(expected)-set(items));assert not missing,missing

def get(name):
 x=items[name]
 local=ROOT/'source'/name;local.parent.mkdir(parents=True,exist_ok=True)
 if local.exists():b=local.read_bytes()
 else:
  url='https://raw.githubusercontent.com/MIKEAA2020/general-sustainability/'+BRANCH+'/'+urllib.parse.quote(PREFIX+name,safe='/')
  b=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'family-depth-preservation'}),timeout=120).read();local.write_bytes(b)
 assert len(b)==x['size'],(name,len(b),x['size'])
 assert hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()==x['sha'],name
 return dict(family=expected[name],name=name,remote_path=PREFIX+name,blob_sha=x['sha'],sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),local=str(local))
with ThreadPoolExecutor(max_workers=8) as pool:
 futures={pool.submit(get,name):name for name in expected};out=[]
 for f in as_completed(futures):
  d=f.result();out.append(d);print(d['family'],d['bytes'],d['name'],flush=True)
(ROOT/'source_manifest.json').write_text(json.dumps(sorted(out,key=lambda d:d['name']),indent=2)+'\n')
print('branch',BRANCH,'files verified',len(out),'total bytes',sum(d['bytes'] for d in out))
