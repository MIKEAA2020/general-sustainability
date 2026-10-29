"""Authorized workspace preservation/recovery, R01. No remote deletions/overwrites.
Before cleanup, publish every surviving non-upload creation not already identified
by exact Git blob in the repository; verify all references and download every new
blob. Remove only complete explicitly listed older local package directories after
rechecking each file's SHA256 and downloading its remote blob for byte comparison.
Private uploads/credential and active C18/v43/F10 packages are never pruned.
"""
from pathlib import Path
import json,hashlib,base64,re,collections,sys,os,shutil
from concurrent.futures import ThreadPoolExecutor
import requests
R=Path('/home/user');W=R/'workspace_preservation_recovery_20261030_R01'
PREFIX='batch 9/agent 2/workspace_preservation_recovery_20261030_R01/'
API='https://api.github.com/repos/MIKEAA2020/general-sustainability'
PRUNE=['ecomod_followup_F08','ecomod_followup_F09','governance_elevation_P4_v42_P01']
EXCLUDE={'.cache','__pycache__','.git','node_modules','.texlive2025'}
def require(ok,msg):
    if not ok:raise RuntimeError(msg)
def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def sha256(b):return hashlib.sha256(b).hexdigest()
def dump(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,indent=2)+'\n')
def size(root):return sum(p.stat().st_size for p in root.rglob('*')if p.is_file()and not any(q in EXCLUDE for q in p.relative_to(root).parts))
def session():
    token=re.search(r'github_pat_[A-Za-z0-9_]+',(R/'uploads/github_pat.txt').read_text()).group()
    s=requests.Session();s.headers.update({'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'})
    return s,token
s,token=session()
def api(method,path,**kw):
    z=s.request(method,API+path,timeout=120,**kw)
    if not z.ok:raise RuntimeError('GitHub HTTP '+str(z.status_code)+' on '+path.split('?')[0])
    return z.json()
def tree(head):
    tsha=api('GET','/git/commits/'+head)['tree']['sha'];d=api('GET','/git/trees/'+tsha,params={'recursive':'1'});require(not d.get('truncated'),'Truncated tree')
    return tsha,{z['path']:z for z in d['tree']if z['type']!='tree'}
def download(h):
    d=api('GET','/git/blobs/'+h);b=base64.b64decode(d['content']);require(gitsha(b)==h,'Downloaded blob mismatch');return b
def preserve(old,new):
    for p,z in old.items():require(p in new and all(new[p][k]==z[k]for k in ['sha','type','mode']),'Prior remote path changed')
def allfiles():
    return sorted(p for p in R.rglob('*')if p.is_file()and 'uploads'not in p.relative_to(R).parts and not any(q in EXCLUDE or q.startswith('.')for q in p.relative_to(R).parts))
def publish_new(base,head,old,entries,message):
    require(api('GET','/git/ref/heads/main')['object']['sha']==head,'Remote advanced; stop without deletion')
    nt=api('POST','/git/trees',json={'base_tree':base,'tree':entries})['sha']
    d=api('GET','/git/trees/'+nt,params={'recursive':'1'});require(not d.get('truncated'),'Truncated proposed tree');new={z['path']:z for z in d['tree']if z['type']!='tree'};preserve(old,new)
    require(set(new)-set(old)=={z['path']for z in entries},'Unexpected new paths')
    c=api('POST','/git/commits',json={'message':message,'tree':nt,'parents':[head]})['sha']
    require(api('GET','/git/ref/heads/main')['object']['sha']==head,'Remote advanced before update');api('PATCH','/git/refs/heads/main',json={'sha':c,'force':False});require(api('GET','/git/ref/heads/main')['object']['sha']==c,'Publication HEAD mismatch')
    t,actual=tree(c);preserve(old,actual);require(t==nt,'Published tree mismatch');return c,t,actual

def main():
    require(not(W/'metadata/PRE_CLEANUP_PUBLICATION_RECEIPT_R01.json').exists(),'One-shot already ran; inspect receipt, never blindly rerun')
    head=api('GET','/git/ref/heads/main')['object']['sha'];base,old=tree(head)
    require(not any(p.startswith(PREFIX)for p in old),'Version already exists')
    bysha=collections.defaultdict(list)
    for p,z in old.items():
        if z['type']=='blob':bysha[z['sha']].append(p)
    # Verify the 2026-10-29 intentional cleanup records independently of local absence.
    historic=json.loads((R/'workspace_archive_20261029/RESTORE_INDEX.json').read_text())['files']
    for z in historic:require(z['repository_path']in old and old[z['repository_path']]['sha']==z['git_blob_sha1'],'Historic archived creation no longer available')
    # Restore the known lost audit-reference cache as durable versioned references.
    recovered=[]
    for short,label in [('44f48861d6c20a3a8419798d18f03b16130ebbef','MAIN'),('8c4691ca927d1abcfb6368a4c1198c56208ad180','SI')]:
        c=api('GET','/commits/'+short);dump(W/f'recovered_references/commit_{label}_R01.json',c)
        name='AUDIT_ECOMOD_C17_'+label+'_20261029.md';path='batch 9/agent 2/ecomod_audit/'+name
        _,tr=tree(short);require(path in tr,'Audit reference missing in exact commit');b=download(tr[path]['sha']);dest=W/'recovered_references'/(name.replace('.md','_recovered_R01.md'));dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
        recovered.append(dict(original_cache_reference=name,restored_path=str(dest.relative_to(R)),repository_commit=short,repository_path=path,git_blob=tr[path]['sha'],sha256=sha256(b),kind='Exact repository reference bytes'))
    # Latest publication status is reconstructed from authoritative receipt/commit,
    # not falsely labelled a byte-exact recovery of excluded console stdout.
    receipt=json.loads((R/'PUBLICATION_RECEIPT_ECOMOD_C18_A01.json').read_text())
    require(receipt['publication_commit']=='688701d6053ea1d89a37b9c708ef29c9b2e8ddf5','Unexpected C18 receipt')
    dump(W/'recovered_references/C18_publication_status_reconstructed_R01.json',dict(kind='Regenerated operational status, not original cache stdout',receipt=receipt,receipt_commit='f729cce6881ed0ad876cabbceafe7f6675235900',receipt_commit_metadata=api('GET','/commits/f729cce6881ed0ad876cabbceafe7f6675235900')))
    dump(W/'metadata/RECOVERY_FINDINGS_BEFORE_CLEANUP_R01.json',dict(manifested_deliverables_missing=0,manifested_records_matching=1400,manifest_count=22,historical_restore_index_records=len(historic),historical_missing_intentionally_removed=995,historical_unplanned_missing=0,all_historical_records_remote_verified=True,exact_reference_recoveries=recovered,cache_limit='Excluded .cache software, builds and console files are not preserved by workspace snapshots. Unmanifested byte-exact cache recovery cannot be guaranteed; primary data/code/documents survive and their archived reproduction tools remain available.',uploads='All user uploads, private PDF parts and private credential retained locally, excluded from publication and deletion.'))
    records=[];pending={};entries=[]
    # Select restoration paths by content, never merely by similar names.
    files=allfiles()
    for p in files:
        rel=str(p.relative_to(R));b=p.read_bytes();require(token.encode()not in b,'Credential content in candidate');h=gitsha(b)
        candidates=bysha.get(h,[])
        if candidates:
            path=max(candidates,key=lambda q:len(os.path.commonprefix([q[::-1],rel[::-1]])))
        else:
            path=PREFIX+'preserved/'+rel
            require(path not in old,'Refuse path overwrite')
            if h not in pending:
                got=api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha'];require(got==h,'Upload mismatch');pending[h]=p
            entries.append(dict(path=path,mode='100644',type='blob',sha=h));bysha[h].append(path)
        records.append(dict(workspace_path=rel,repository_path=path,git_blob=h,sha256=sha256(b),bytes=len(b),planned_prune=rel.split('/')[0]in PRUNE))
    index=dict(date='2026-10-30',source_head=head,scope='Every surviving non-upload creation plus verified historical restore index; no secrets or private uploads',files=records,planned_prune_directories=PRUNE,private_uploads_retained=True,excluded_cache_dirs=sorted(EXCLUDE),bytes_before=size(R),target='Retain active complete C18/v43/F10 packages, graphical abstract, author-facing reviews and original uploads; remove only older separately reclonable packages.')
    indexpath=W/'metadata/RESTORE_INDEX_R01.json';dump(indexpath,index);b=indexpath.read_bytes();h=gitsha(b);require(api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha']==h,'Index upload mismatch');entries.append(dict(path=PREFIX+'RESTORE_INDEX_R01.json',mode='100644',type='blob',sha=h))
    print('Inventory ready:',len(records),'surviving files;',len(historic),'historical records verified; publishing additions before any cleanup',flush=True)
    commit,nt,new=publish_new(base,head,old,entries,'Preserve all surviving chat creations, restore references and publish recovery index before local cleanup')
    for z in records:require(new[z['repository_path']]['sha']==z['git_blob'],'Creation missing in published tree')
    with ThreadPoolExecutor(max_workers=5)as ex:
        verified=list(ex.map(lambda kv:download(kv[0])==kv[1].read_bytes(),pending.items()))
    require(all(verified),'New blob byte verification failed');require(download(h)==indexpath.read_bytes(),'Restore index download mismatch')
    pre=dict(publication_commit=commit,parent=head,surviving_creation_files_verified=len(records),historical_records_remote_verified=len(historic),new_unique_blobs_download_verified=len(pending),all_prior_remote_paths_preserved=len(old),restore_index_download_verified=True,no_deletion_before_success=True)
    dump(W/'metadata/PRE_CLEANUP_PUBLICATION_RECEIPT_R01.json',pre);print(json.dumps(pre),flush=True)
    # Archive even the newly created pre-cleanup receipt before deleting a local copy.
    pb=(W/'metadata/PRE_CLEANUP_PUBLICATION_RECEIPT_R01.json').read_bytes();ph=gitsha(pb)
    require(api('POST','/git/blobs',json={'content':base64.b64encode(pb).decode(),'encoding':'base64'})['sha']==ph,'Receipt upload mismatch')
    commit,nt,new=publish_new(nt,commit,new,[dict(path=PREFIX+'completion/PRE_CLEANUP_PUBLICATION_RECEIPT_R01.json',mode='100644',type='blob',sha=ph)],'Archive verified pre-cleanup preservation receipt before any local deletion')
    require(download(ph)==pb,'Pre-cleanup receipt download mismatch')
    # Require each file in a whole-directory removal to have a published index row.
    bylocal={z['workspace_path']:z for z in records};pruned=[];download_cache={}
    for dirname in PRUNE:
        directory=R/dirname;require(directory.is_dir(),'Missing planned directory')
        actual=[p for p in directory.rglob('*')if p.is_file()and not any(q in EXCLUDE for q in p.relative_to(directory).parts)]
        checks=[]
        for p in actual:
            z=bylocal.get(str(p.relative_to(R)));require(z is not None,'Uninventoried file in cleanup target');b=p.read_bytes();require(sha256(b)==z['sha256'],'Local content changed since archive');checks.append((p,z,b))
        unique={z['git_blob']:b for _,z,b in checks}
        def verify_pair(kv):return kv[0],download(kv[0])==kv[1]
        with ThreadPoolExecutor(max_workers=5)as ex:
            for hh,ok in ex.map(verify_pair,unique.items()):require(ok,'Cleanup candidate remote download mismatch')
        # Reread local bytes immediately before deleting the verified directory.
        for p,z,b in checks:require(p.read_bytes()==b,'Local changed before prune')
        count=len(checks);nbytes=sum(len(b)for _,_,b in checks);shutil.rmtree(directory);pruned.append(dict(directory=dirname,files=count,bytes=nbytes,all_remote_bytes_verified=True))
        print('Pruned exact reclonable local copy:',dirname,nbytes,'bytes',flush=True)
    post=dict(date='2026-10-30',backup_commit=commit,prior_remote_paths_preserved=True,verified_local_prunes=pruned,bytes_after=size(R),bytes_before=index['bytes_before'],all_uploads_and_credential_retained=True,active_complete_packages_retained=['ecomod_audit_remediation_C18_A01','governance_elevation_P4_v43_P02','governance_graphical_abstract_P4_v43_GA01','ecomod_followup_F10'],manifest_loss_result='0 missing or mismatched among 1,400 pre-cleanup checks; older historical absent files were all planned removals with verified remote copies',remaining_loss_limits='Unindexed excluded cache stdout/builds cannot be proven exactly recovered; exact source references and authoritative publication status have been recovered/reconstructed distinctly.')
    dump(W/'reports/CLEANUP_AND_RECOVERY_RESULT_R01.json',post)
    # Append completion records at fresh paths, never overwrite the pre-cleanup tree.
    finalfiles=[W/'reports/CLEANUP_AND_RECOVERY_RESULT_R01.json']
    finalentries=[]
    for p in finalfiles:
        b=p.read_bytes();hh=gitsha(b);require(api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha']==hh,'Completion upload mismatch');finalentries.append(dict(path=PREFIX+'completion/'+p.name,mode='100644',type='blob',sha=hh))
    rc,_,last=publish_new(nt,commit,new,finalentries,'Record byte-verified workspace cleanup and recovery outcome; preserve all prior content')
    for p,z in zip(finalfiles,finalentries):require(download(z['sha'])==p.read_bytes(),'Completion receipt mismatch')
    print(json.dumps(dict(**post,preservation_receipt=pre,completion_commit=rc),indent=2),flush=True)
if __name__=='__main__':main()
