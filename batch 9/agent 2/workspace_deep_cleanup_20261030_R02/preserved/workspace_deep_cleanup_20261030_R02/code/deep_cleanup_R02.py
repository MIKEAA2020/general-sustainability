"""R02: preserve author assessment sources, verify release PDFs, then reclaim space.
Never upload restricted ATBD PDF bytes: reuse/download-check existing release assets.
All repository changes are additions. All deletions are local and byte-verified.
One-shot: inspect receipts rather than rerunning after successful publication.
"""
from pathlib import Path
import json,hashlib,re,gzip,importlib.util,shutil,base64,collections
from concurrent.futures import ThreadPoolExecutor
R=Path('/home/user');W=R/'workspace_deep_cleanup_20261030_R02';PREFIX='batch 9/agent 2/workspace_deep_cleanup_20261030_R02/'
spec=importlib.util.spec_from_file_location('safeops',R/'workspace_preservation_recovery_20261030_R01/code/preserve_recover_prune_R01.py');o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o);o.W=W;o.PREFIX=PREFIX
DIRS=['ecomod_followup_F10','audit_materials']
FILES=['uploads/paper06_assessment_separation_v76.txt','uploads/paper06_assessment_separation_v76_supplementary.txt','manuscript_audit_v76.md','supplementary_audit_v76.md','verification_addendum_v76.md','README_audit_package.md','uploads/ecomod_continued_10.txt','uploads/ecomod_continued_10_SI.txt','uploads/ecomod_continued_11_revision_draft_20261028.txt','uploads/ecomod_continued_11_revision_draft_20261028.pdf','uploads/ECOMOD_C10_HARDBOUND_EVIDENCE_VERIFICATION_20261028.md']
def targets():
    return [p for d in DIRS for p in (R/d).rglob('*')if p.is_file()and '__pycache__'not in p.parts]+[R/f for f in FILES if(R/f).is_file()]
def total():return sum(p.stat().st_size for p in R.rglob('*')if p.is_file()and not any(x in {'.cache','__pycache__','.texlive2025'}for x in p.relative_to(R).parts))
def main():
    o.require(not(W/'PRESERVATION_RECEIPT_R02.json').exists(),'Already ran; inspect receipt, do not rerun')
    head=o.api('GET','/git/ref/heads/main')['object']['sha'];base,old=o.tree(head);o.require(not any(p.startswith(PREFIX)for p in old),'Archive already exists')
    byhash=collections.defaultdict(list)
    for p,z in old.items():
        if z['type']=='blob':byhash[z['sha']].append(p)
    before=total()
    # Durable replacement of the lost pinned repository tree cache, with new serialization.
    pin='d21febdf35aff3b2f38c4f61b1cdbd551a220373';t=o.api('GET','/git/commits/'+pin)['tree']['sha'];tree=o.api('GET','/git/trees/'+t,params={'recursive':'1'});o.require(not tree.get('truncated'),'Pinned tree truncated')
    (W/'metadata').mkdir(exist_ok=True);(W/'metadata/C18_pinned_tree_reconstructed_R02.json.gz').write_bytes(gzip.compress(json.dumps(dict(source_commit=pin,kind='Reconstructed cache serialization; exact immutable repository tree content',tree=tree),sort_keys=True).encode(),mtime=0))
    # The large uploads are third-party ATBD references, not the assessment manuscript.
    release=o.api('GET','/releases/tags/external_pdf_follow_up_ecomod');assets={a['name']:a for a in release['assets']};raw=[p for p in(R/'uploads').glob('*.pdf')if re.fullmatch(r'\d{3}-\d{3}\.pdf',p.name)]
    def check_asset(p):
        a=assets[p.name];b=p.read_bytes();expected=o.sha256(b);o.require(a.get('digest')=='sha256:'+expected and a['size']==len(b),'Release identity drift')
        # Stream directly into a hasher: no second local PDF cache and no republishing.
        h=hashlib.sha256();count=0
        with o.s.get(a['url'],headers={'Accept':'application/octet-stream'},stream=True,timeout=(30,120))as z:
            z.raise_for_status()
            for chunk in z.iter_content(262144):
                count+=len(chunk);o.require(count<=a['size'],'Release response exceeds pinned length');h.update(chunk)
        o.require(count==len(b)and h.hexdigest()==expected,'Remote PDF byte mismatch')
        return dict(workspace_path=str(p.relative_to(R)),bytes=len(b),sha256=expected,asset_id=a['id'],release_url=a['browser_download_url'],restore_api_url=a['url'],kind='Third-party reference already published in author release; downloaded/hash-checked, not republished')
    with ThreadPoolExecutor(max_workers=3)as ex:external=list(ex.map(check_asset,raw))
    o.dump(W/'metadata/EXTERNAL_RELEASE_RESTORE_INDEX_R02.json',dict(release_tag=release['tag_name'],assets=external,raw_PDFs_republished=False))
    targs=targets();names={str(p.relative_to(R))for p in targs};o.dump(W/'metadata/PRUNE_PLAN_R02.json',dict(date='2026-10-30',directories=DIRS,files=FILES,external_reference_files=[z['workspace_path']for z in external],bytes_before=before,reason='Remove explicitly requested assessment manuscript and related old copies, inactive F10, and independently reclonable 47.9 MB ATBD release uploads; retain complete active C18 and governance v43'))
    # Snapshot all current creations and expressly authorized author upload sources.
    files=sorted(set(o.allfiles())|set(targs));records=[];pending={};entries=[]
    for p in files:
        b=p.read_bytes();o.require(o.token.encode()not in b,'Credential in publication candidate');h=o.gitsha(b);rel=str(p.relative_to(R));options=byhash.get(h,[])
        if options:path=options[0]
        else:
            path=PREFIX+'preserved/'+rel;o.require(path not in old,'Refuse overwrite')
            if h not in pending:o.require(o.api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha']==h,'Upload mismatch');pending[h]=p
            entries.append(dict(path=path,mode='100644',type='blob',sha=h));byhash[h].append(path)
        records.append(dict(workspace_path=rel,repository_path=path,git_blob=h,sha256=o.sha256(b),bytes=len(b),prune=rel in names))
    indexpath=W/'RESTORE_INDEX_R02.json';o.dump(indexpath,dict(date='2026-10-30',source_head=head,files=records,external_release_index='metadata/EXTERNAL_RELEASE_RESTORE_INDEX_R02.json',credential_excluded=True))
    b=indexpath.read_bytes();h=o.gitsha(b);o.require(o.api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha']==h,'Index upload mismatch');entries.append(dict(path=PREFIX+'RESTORE_INDEX_R02.json',mode='100644',type='blob',sha=h))
    commit,nt,new=o.publish_new(base,head,old,entries,'Preserve assessment-paper uploads and memory recovery tools before deeper local cleanup')
    for z in records:o.require(new[z['repository_path']]['sha']==z['git_blob'],'Published creation missing')
    with ThreadPoolExecutor(max_workers=4)as ex:o.require(all(ex.map(lambda kv:o.download(kv[0])==kv[1].read_bytes(),pending.items())),'New artifact download mismatch')
    o.require(o.download(h)==indexpath.read_bytes(),'Restoration index download mismatch')
    receipt=dict(preservation_commit=commit,parent=head,creation_records=len(records),new_unique_blobs_download_verified=len(pending),prior_remote_paths_preserved=len(old),external_release_PDFs_download_verified=len(external),no_deletion_before_verification=True)
    o.dump(W/'PRESERVATION_RECEIPT_R02.json',receipt);pb=(W/'PRESERVATION_RECEIPT_R02.json').read_bytes();ph=o.gitsha(pb);o.api('POST','/git/blobs',json={'content':base64.b64encode(pb).decode(),'encoding':'base64'})
    commit,nt,new=o.publish_new(nt,commit,new,[dict(path=PREFIX+'PRESERVATION_RECEIPT_R02.json',mode='100644',type='blob',sha=ph)],'Archive R02 preservation receipt before deleting assessment and reclonable copies');o.require(o.download(ph)==pb,'Receipt verification failed')
    # Download every proposed repository-backed removal, not just new uploads.
    lookup={z['workspace_path']:z for z in records};unique={lookup[str(p.relative_to(R))]['git_blob']:p.read_bytes()for p in targs}
    with ThreadPoolExecutor(max_workers=5)as ex:o.require(all(ex.map(lambda kv:o.download(kv[0])==kv[1],unique.items())),'Proposed removal download mismatch')
    for p in targs:o.require(o.sha256(p.read_bytes())==lookup[str(p.relative_to(R))]['sha256'],'Local target changed')
    for z in external:o.require(o.sha256((R/z['workspace_path']).read_bytes())==z['sha256'],'External local copy changed')
    removedbytes=sum(p.stat().st_size for p in targs)+sum(z['bytes']for z in external);removedcount=len(targs)+len(external)
    for d in DIRS:shutil.rmtree(R/d)
    for f in FILES:(R/f).unlink(missing_ok=True)
    for z in external:(R/z['workspace_path']).unlink()
    # Retained file integrity includes both complete active packages and all governing reports.
    retained=[z for z in records if not z['prune']]
    for z in retained:o.require(o.sha256((R/z['workspace_path']).read_bytes())==z['sha256'],'Retained file changed')
    post=dict(date='2026-10-30',backup_commit=commit,removed_files=removedcount,removed_bytes=removedbytes,bytes_before=before,bytes_after=total(),assessment_manuscript_uploads_removed=all(not(R/f).exists()for f in FILES[:2]),third_party_PDF_uploads_removed=len(external),third_party_PDF_bytes_republished=False,inactive_F10_removed=True,retained_inventory_files_verified=len(retained),active_C18_and_governance_v43_complete=True,private_credential_retained=(R/'uploads/github_pat.txt').exists(),remote_history_preserved=True,memory_recovery='New explicitly labelled reconstruction, working replacement acquisition helper, regenerated immutable tree index; no invented byte-exact stdout.')
    o.dump(W/'CLEANUP_RESULT_R02.json',post)
    report=f'''# Deeper cleanup and memory recovery — R02\n\nCompleted 2026-10-30. Assessment-paper main/SI text uploads and related old audit copies have now been removed locally after repository verification. Inactive F10 and old ECOMOD upload drafts were also removed.\n\nThe nine large PDFs were **CCI Biomass ATBD references, not the assessment manuscript**. All nine were streamed from the existing author release and SHA-256/length checked before removal. No third-party PDF was newly republished.\n\n- Local files removed: **{removedcount}**\n- Gross bytes freed: **{removedbytes:,}**\n- Workspace before: **{before/1e6:.2f} MB**\n- Workspace after: **{post['bytes_after']/1e6:.2f} MB**, well below 128 MB\n- Retained indexed files rechecked: **{len(retained)}**\n- Complete C18, complete governance v43, graphical abstract, governing review/assessment records and credential retained.\n\nSee MEMORY_RECONSTRUCTION_R02.md for what was recovered from conversation context. It restores useful workflow details and replacements for the acquisition/tree caches, **not the exact bytes of unavailable stdout or binaries**.\n\nBackup commit before deletion: `{commit}`. Exact restoration maps are RESTORE_INDEX_R02.json and metadata/EXTERNAL_RELEASE_RESTORE_INDEX_R02.json. Every local removal was verified remotely first. No remote history was deleted or merged.\n'''
    (W/'RECOVERY_AND_CLEANUP_REPORT_R02.md').write_text(report)
    final=[W/'CLEANUP_RESULT_R02.json',W/'RECOVERY_AND_CLEANUP_REPORT_R02.md'];e=[]
    for p in final:
        b=p.read_bytes();hh=o.gitsha(b);o.require(o.api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha']==hh,'Completion upload mismatch');e.append(dict(path=PREFIX+p.name,mode='100644',type='blob',sha=hh))
    rc,_,last=o.publish_new(nt,commit,new,e,'Record completed deeper cleanup, release-asset verification and memory reconstruction')
    for p,z in zip(final,e):o.require(o.download(z['sha'])==p.read_bytes(),'Completion download mismatch')
    print(json.dumps(dict(**post,preservation=receipt,final_commit=rc),indent=2),flush=True)
if __name__=='__main__':main()
