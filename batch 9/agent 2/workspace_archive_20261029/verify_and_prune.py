"""User-authorized local cleanup; remote backup and exact local identity required first."""
from pathlib import Path
import json,hashlib,shutil,requests,re
R=Path('/home/user');A=Path(__file__).resolve().parent
index=json.loads((A/'RESTORE_INDEX.json').read_text());receipt=json.loads((A/'publication_receipt.json').read_text());assert receipt['all_recorded_blobs_verified_in_published_tree']and receipt['restore_index_download_verified']
token=re.search(r'github_pat_[A-Za-z0-9_]+',(R/'uploads/github_pat.txt').read_text()).group();s=requests.Session();s.headers.update({'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'});base='https://api.github.com/repos/'+index['repository']
def get(path):
 r=s.get(base+path,timeout=90);assert r.ok,('GitHub request failed',r.status_code);return r.json()
commit=receipt['published_commit'];tree=get('/git/commits/'+commit)['tree']['sha'];obj=get('/git/trees/'+tree+'?recursive=1');assert not obj.get('truncated');remote={x['path']:x for x in obj['tree']if x['type']=='blob'}
records={x['workspace_path']:x for x in index['files']};dirs=index['planned_prune_directories'];expected=['ecomod_audit','ecomod_c11_review','ecomod_c13_revision','ecomod_c14','ecomod_c15','ecomod_c16','ecomod_c17','ecomod_empirical_followup']+[f'ecomod_followup_F0{i}'for i in range(2,8)];assert dirs==expected
for x in records.values():assert remote[x['repository_path']]['sha']==x['git_blob_sha1']
# Refuse deletion of any unindexed or locally changed file in a package.
package_files=[]
for name in dirs:
 d=R/name;assert d.is_dir()and not d.is_symlink()
 for p in d.rglob('*'):
  assert not p.is_symlink(),str(p)
  if p.is_file():
   rel=str(p.relative_to(R));assert rel in records,('Unindexed file',rel);x=records[rel];assert hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'],('Changed file',rel);assert x['planned_local_removal'];package_files.append(x)
# Own operational creations in these caches must also have an exact archived record.
for name in ['f07','f08']:
 for p in (R/'.cache'/name).rglob('*'):
  if p.is_file()and p.suffix in ['.py','.log','.json','.png','.jpg','.txt']:
   rel=str(p.relative_to(R));assert rel in records;assert hashlib.sha256(p.read_bytes()).hexdigest()==records[rel]['sha256']
# Hash the retained current package, assessments and credential before/after cleanup.
retained={}
for name in ['ecomod_followup_F08','uploads','journal_revision_evaluation_20261029','revision_audit_20261029']:
 for p in (R/name).rglob('*'):
  if p.is_file():retained[str(p.relative_to(R))]=hashlib.sha256(p.read_bytes()).hexdigest()
def treebytes(p):return sum(q.stat().st_size for q in p.rglob('*')if q.is_file())if p.exists()else 0
before_visible=sum(treebytes(d)if d.is_dir()else d.stat().st_size for d in R.iterdir()if not d.name.startswith('.'));cache_before=treebytes(R/'.cache');removed_bytes=sum(x['bytes']for x in package_files)
for name in dirs:shutil.rmtree(R/name)
for name in ['f07','f08','restore_test','matplotlib','pip']:
 p=R/'.cache'/name
 if p.exists():shutil.rmtree(p)
for rel,h in retained.items():assert hashlib.sha256((R/rel).read_bytes()).hexdigest()==h,rel
for name in dirs:assert not(R/name).exists()
after_visible=sum(treebytes(d)if d.is_dir()else d.stat().st_size for d in R.iterdir()if not d.name.startswith('.'));cache_after=treebytes(R/'.cache')
report={'date':'2026-10-29','backup_commit':commit,'backup_verified_before_deletion':True,'restoration_test':'ECOMOD C17 main .tex and .pdf downloaded from the pinned public commit and SHA-256 verified before deletion','all_prior_repository_content_preserved':True,'local_package_directories_removed':dirs,'local_package_files_removed':len(package_files),'local_package_bytes_removed':removed_bytes,'visible_workspace_bytes_before':before_visible,'visible_workspace_bytes_after':after_visible,'replaceable_cache_bytes_before':cache_before,'replaceable_cache_bytes_after':cache_after,'retained_current_F08_uploads_private_credential_and_governing_assessments_hash_verified':True,'credential_contents_not_logged_or_published':True,'retained_file_count_hash_verified':len(retained),'raw_upstream_caches_not_redistributed':True,'restore_index':'RESTORE_INDEX.json','restoration_script':'restore_files.py'}
(A/'CLEANUP_REPORT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True)
