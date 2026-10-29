from pathlib import Path
import requests,json,re,hashlib,base64,collections
R=Path('/home/user');A=R/'workspace_archive_20261029';prefix='batch 9/agent 2/workspace_archive_20261029/'
token=re.search(r'github_pat_[A-Za-z0-9_]+',(R/'uploads/github_pat.txt').read_text()).group();s=requests.Session();s.headers.update({'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'});base='https://api.github.com/repos/MIKEAA2020/general-sustainability'
def api(method,path,**kw):
 r=s.request(method,base+path,timeout=90,**kw)
 if not r.ok:raise RuntimeError(f'{method} {path}: HTTP {r.status_code}')
 return r.json()
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
head=api('GET','/git/ref/heads/main')['object']['sha'];tree=api('GET','/git/commits/'+head)['tree']['sha'];remote=api('GET','/git/trees/'+tree,params={'recursive':'1'});assert not remote.get('truncated');old={x['path']:x for x in remote['tree']if x['type']=='blob'};byhash=collections.defaultdict(list)
for x in old.values():byhash[x['sha']].append(x['path'])
assert not any(p.startswith(prefix)for p in old),'Archive already exists; refuse overwrite'
files=[p for p in R.iterdir()if p.is_file()and not p.name.startswith('.')]
for d in R.iterdir():
 if d.is_dir()and not d.name.startswith('.')and d.name not in ['uploads',A.name]:files.extend(p for p in d.rglob('*')if p.is_file()and not any(q in ['__pycache__','node_modules','.git']for q in p.relative_to(d).parts))
for name in ['f07','f08']:
 files.extend(p for p in (R/'.cache'/name).rglob('*')if p.is_file()and p.suffix in ['.py','.log','.json','.png','.jpg','.txt'])
prune_dirs=['ecomod_audit','ecomod_c11_review','ecomod_c13_revision','ecomod_c14','ecomod_c15','ecomod_c16','ecomod_c17','ecomod_empirical_followup']+[f'ecomod_followup_F0{i}'for i in range(2,8)]
records=[];entries=[];pending={};created=0
for p in sorted(set(files)):
 rel=str(p.relative_to(R));b=p.read_bytes();assert token.encode()not in b,rel;h=blob(b);candidates=byhash.get(h,[])
 if candidates:
  path=max(candidates,key=lambda x:len(__import__('os').path.commonprefix([x[::-1],rel[::-1]])))
 else:
  path=prefix+'preserved/'+rel.lstrip('.').replace('/.cache/','/cache/')
  if h not in pending:
   actual=api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha'];assert actual==h;pending[h]=True;created+=1
  entries.append({'path':path,'mode':'100644','type':'blob','sha':h});byhash[h].append(path)
 records.append({'workspace_path':rel,'repository_path':path,'git_blob_sha1':h,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'planned_local_removal':rel.split('/')[0]in prune_dirs or rel.startswith('.cache/f07/')or rel.startswith('.cache/f08/')})
print('Inventoried',len(records),'files; already present or new preserved blobs:',created,'new',flush=True)
index={'date':'2026-10-29','repository':'MIKEAA2020/general-sustainability','verified_parent_commit':head,'archive_repository_prefix':prefix,'verification':'Every workspace record is matched to a repository Git blob SHA computed from its exact local bytes; new blobs uploaded before local deletion. Full prospective tree checked for preservation of every prior blob path/mode/hash.','retained':['ecomod_followup_F08','uploads including private credential','journal_revision_evaluation_20261029','revision_audit_20261029','review/assessment reports','this restoration index'],'planned_prune_directories':prune_dirs,'external_raw_cache_note':'Downloaded upstream XLSX/ZIP/range bytes and software/font caches are not author creations, are not redistributed and may be deleted; published source registries and audit code retain URLs, hashes and bounded re-fetch rules.','files':records}
(A/'RESTORE_INDEX.json').write_text(json.dumps(index,indent=2)+'\n');(A/'planned_prune.json').write_text(json.dumps({'directories':prune_dirs,'bytes_before_removal':sum(x['bytes']for x in records if x['planned_local_removal']),'candidate_files':sum(x['planned_local_removal']for x in records)},indent=2)+'\n')
for p in A.iterdir():
 if p.is_file():
  b=p.read_bytes();assert token.encode()not in b;h=blob(b);actual=api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha'];assert actual==h;entries.append({'path':prefix+p.name,'mode':'100644','type':'blob','sha':h})
newtree=api('POST','/git/trees',json={'base_tree':tree,'tree':entries})['sha'];check=api('GET','/git/trees/'+newtree,params={'recursive':'1'});assert not check.get('truncated');after={x['path']:x for x in check['tree']if x['type']=='blob'}
for path,x in old.items():assert after[path]['sha']==x['sha']and after[path]['mode']==x['mode'],path
for x in records:assert after[x['repository_path']]['sha']==x['git_blob_sha1']
commit=api('POST','/git/commits',json={'message':'Archive all remaining workspace creations and restoration index before verified local space cleanup; preserve all existing content','tree':newtree,'parents':[head]})['sha'];assert api('GET','/git/ref/heads/main')['object']['sha']==head;api('PATCH','/git/refs/heads/main',json={'sha':commit,'force':False});assert api('GET','/git/ref/heads/main')['object']['sha']==commit
# Re-read the published commit/tree, not only the prospective tree.
actualtree=api('GET','/git/commits/'+commit)['tree']['sha'];assert actualtree==newtree;published=api('GET','/git/trees/'+actualtree,params={'recursive':'1'});assert not published.get('truncated');published={x['path']:x for x in published['tree']if x['type']=='blob'}
for x in records:assert published[x['repository_path']]['sha']==x['git_blob_sha1']
# Download and verify the restore index itself.
e=published[prefix+'RESTORE_INDEX.json'];b=base64.b64decode(api('GET','/git/blobs/'+e['sha'])['content']);assert b==(A/'RESTORE_INDEX.json').read_bytes()
receipt={'published_commit':commit,'parent_commit':head,'verified_workspace_files':len(records),'new_preserved_content_blobs':created,'prior_repository_blob_paths_modes_hashes_preserved':len(old),'all_recorded_blobs_verified_in_published_tree':True,'restore_index_download_verified':True,'nothing_deleted_yet':True};(A/'publication_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2),flush=True)
