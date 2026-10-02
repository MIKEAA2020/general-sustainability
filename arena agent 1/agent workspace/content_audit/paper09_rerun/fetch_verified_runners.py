#!/usr/bin/env python3
"""Recover published comparison verifiers by authenticated Git blob and SHA-1.
No credential value appears in logs or saved sources; only byte-verified scripts persist.
"""
from pathlib import Path
import urllib.request,json,base64,hashlib,csv
R=Path('/home/user');O=R/'content_audit/paper09_rerun';O.mkdir(parents=True,exist_ok=True)
sha=(R/'content_audit/push_tip.txt').read_text().strip();token=(R/'uploads/github_pat.txt').read_text().strip();headers={'Authorization':'Bearer '+token,'User-Agent':'paper09-source-rerun'}
base='https://api.github.com/repos/MIKEAA2020/general-sustainability'
def j(uri):return json.load(urllib.request.urlopen(urllib.request.Request(base+uri,headers=headers),timeout=120))
tree=j('/git/trees/'+sha+'?recursive=1');assert not tree['truncated'];lookup={e['path']:e['sha'] for e in tree['tree'] if e['type']=='blob'}
names={'paperE2_cod_intervention_v29_verification.py':'arena agent 1/paper rewrites/latex/paperE2_cod_intervention_v29_verification.py','paperE4_edwards_intervention_v16_verification.py':'arena agent 1/paper rewrites/latex/paperE4_edwards_intervention_v16_verification.py','campaign_e4_elevation.py':'arena agent 1/other documents/rerun_campaigns/campaign_e4_elevation.py'}
with (O/'fetched_runner_manifest.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['remote_path','commit','git_blob_sha1','sha256','bytes','saved_path'])
 for local,path in names.items():
  blob=lookup[path];info=j('/git/blobs/'+blob);assert info['encoding']=='base64';data=base64.b64decode(info['content']);assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==blob
  out=O/'verified_runners'/local;out.parent.mkdir(exist_ok=True);out.write_bytes(data)
  w.writerow([path,sha,blob,hashlib.sha256(data).hexdigest(),len(data),str(out.relative_to(R))])
  print('VERIFIED',path,'bytes',len(data),'sha256',hashlib.sha256(data).hexdigest())
