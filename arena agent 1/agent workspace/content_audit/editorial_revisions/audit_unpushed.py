#!/usr/bin/env python3
"""Read-only compare workspace blobs with remote tree at current branch tip.
Exclude credentials and generated toolchain; never print secret content.
"""
from pathlib import Path
import hashlib,subprocess,collections,os,json
R=Path('/home/user'); repo=Path('/tmp/editorial-push-repo')
assert (repo/'.git').exists()
commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
raw=subprocess.check_output(['git','-C',str(repo),'ls-tree','-r','-z','HEAD'])
tree={}
for x in raw.split(b'\0'):
 if x:
  a,p=x.split(b'\t',1);tree[p.decode()]=a.decode().split()[2]
prefix='arena agent 1/agent workspace/'
excluded=[]; items=[]; seen=[]
for d,ds,fs in os.walk(R):
 ds[:]=[v for v in ds if v not in {'.git','.cache','.local','__pycache__','node_modules','uploads','tools','.arena','.venv'}]
 for name in fs:
  p=Path(d)/name;rel=p.relative_to(R).as_posix()
  if p.is_symlink() or rel in {'.last_sha','p5/reps.pkl'} or name in {'tree.json','tree_main.json','repo_paths.json'} or name.endswith('.pyc'):
   excluded.append(rel);continue
  data=p.read_bytes();sha=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest();loc=prefix+rel
  if tree.get(loc)==sha:seen.append(rel)
  else:items.append(dict(path=rel,sha=sha,bytes=len(data),status='changed' if loc in tree else 'new',also_root=(tree.get(rel)==sha)))
print('tip',commit,'remote paths',len(tree),'workspace files already at mirrored path',len(seen),'push candidates',len(items),'bytes',sum(v['bytes'] for v in items),'exclusions',len(excluded))
print('by region:',dict(collections.Counter(x['path'].split('/')[0] for x in items)))
print('new version and audit records',sum('editorial_revisions' in x['path'] or '_v64.' in x['path'] for x in items))
for x in items:
 if x['bytes']>1000000: print('large',x['path'],x['bytes'])
(R/'content_audit/editorial_revisions/PUSH_INVENTORY_2026-10-02.json').write_text(json.dumps({'base':commit,'prefix':prefix,'already_at_mirror_count':len(seen),'candidates':items,'excluded':excluded},indent=2))
