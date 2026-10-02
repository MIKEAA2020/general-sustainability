#!/usr/bin/env python3
"""Prune ONLY files whose exact Git blob is present at the verified remote branch tip.
Dry-run by default; --apply verifies the full plan before removing anything.
"""
from pathlib import Path
import hashlib,subprocess,sys,re,json
R=Path('/home/user');C=Path('/tmp/cleanup-verification');PIN='e31cdedfee541b89f53e1f3f886296ed3153cd15';PREFIX='arena agent 1/agent workspace/'
assert (C/'.git').is_dir()
def git(*args):return subprocess.check_output(['git','-C',str(C),*args],text=True).strip()
assert git('rev-parse','HEAD')==PIN
assert git('ls-remote','origin','refs/heads/e2-v3-source-year').split()[0]==PIN,'remote tip moved: stop and reverify'
raw=subprocess.check_output(['git','-C',str(C),'ls-tree','-r','-z','HEAD']);tree={}
for ent in raw.split(b'\0'):
 if ent:
  meta,path=ent.split(b'\t',1);tree[path.decode()]=meta.decode().split()[2]
latest={
 'paper01_obstruction_calculus':64,'paper02_probabilistic_sufficiency':13,
 'paper03_computational_certification':17,'paper04_minimax_dual_certificates':17,
 'paper05_exact_belief_computation':17,'paper06_assessment_separation':68,
 'paper07_sampled_governance':51,'paper08_governance_delay':47,
 'paper09_cod_certification':33,'paper09b_arv_certification':3,
 'paper10_depletion_ledgers':53,'paper10b_edwards_aquifer':1,
 'paper11_forecasting_baselines':65,'paper11b_edwards_forecast':2,
 'paper11c_worked_systems_audit':3,
}
reclonable_dirs=['lean_repro','latest/lean','content_audit/claim_alignment/compile',
'content_audit/compile05','content_audit/compile06','content_audit/compile07',
'content_audit/compile11c','content_audit/family_depth/source']
collect={}
for folder in reclonable_dirs:
 d=R/folder
 if d.exists():
  for p in d.rglob('*'):
   if p.is_file():collect[p]=folder
archive=R/'tools/tectonic-0.15.0-x86_64-static.tar.gz'
if archive.exists():collect[archive]='archived compiler (restore instructions retained)'
# Newer versions stay available in exactly the same directory; remove only earlier heads.
rx=re.compile(r'^(paper\d+[a-z]?_[\w]+)_v(\d+)(?:_supplementary(?:_[a-z]+)?)?\.(?:tex|pdf|md)$')
for d in [R/'papers',*(x for x in (R/'paper 2 family').iterdir() if x.is_dir())]:
 for p in d.iterdir():
  if not p.is_file():continue
  m=rx.fullmatch(p.name)
  if not m:continue
  name,v=m.group(1),int(m.group(2)); newest=latest.get(name)
  if newest is None or v>=newest:continue
  newer=list(d.glob(f'{name}_v{newest}.*'))
  if not newer:continue
  collect[p]='earlier paper version (current head retained in same folder)'

verified=[];bad=[]
for p,reason in sorted(collect.items()):
 rel=p.relative_to(R).as_posix();data=p.read_bytes()
 sha=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
 if tree.get(PREFIX+rel)!=sha:bad.append((rel,reason,sha,tree.get(PREFIX+rel)))
 else:verified.append((p,reason,len(data),sha))
from collections import Counter
print('remote tip',PIN,'exact-matched deletion candidates',len(verified),'bytes',sum(x[2] for x in verified))
print('categories',dict(Counter(x[1] for x in verified)))
print('UNMATCHED WILL NEVER DELETE:',len(bad))
for x in bad[:30]:print('UNMATCHED',x[0],x[1])
assert not bad,'refuse partial cleanup: fix mismatch before applying'
manifest=R/'content_audit/editorial_revisions/CLEANUP_CANDIDATES.json'
# Keep a compact manifest outside deletion targets; can be pushed for future recovery.
if '--apply' not in sys.argv:
 manifest.write_text(json.dumps({'remote_tip':PIN,'branch':'e2-v3-source-year','prefix':PREFIX,'files':[{'path':p.relative_to(R).as_posix(),'bytes':n,'git_blob':sha,'category':reason} for p,reason,n,sha in verified]},indent=2))
 print('DRY RUN; manifest',manifest)
else:
 # Insist an unchanged, pre-recorded full plan; additions cannot be deleted by surprise.
 recorded=json.loads(manifest.read_text())
 assert recorded['remote_tip']==PIN
 assert {x['path']:x['git_blob'] for x in recorded['files']}=={p.relative_to(R).as_posix():sha for p,_,_,sha in verified}
 for p,_,_,_ in verified:p.unlink()
 for folder in sorted(reclonable_dirs,key=len,reverse=True):
  d=R/folder
  if d.exists():
   for child in sorted((x for x in d.rglob('*') if x.is_dir()),key=lambda x:len(x.parts),reverse=True):
    if not any(child.iterdir()):child.rmdir()
   if not any(d.iterdir()):d.rmdir()
 print('REMOVED',len(verified),'verified blobs; retained current heads, checklist, provenance, manifest and restore instructions')
