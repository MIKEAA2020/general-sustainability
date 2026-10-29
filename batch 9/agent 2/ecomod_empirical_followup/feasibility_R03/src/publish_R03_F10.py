"""Authorized additive publication of R03 and F10; never overwrites old paths.
Uses a fresh main HEAD, compares every prior path/mode/blob, non-force updates,
and byte-verifies every new artifact. A second additive commit archives the first
commit's verification receipt without changing either package/manifest.
Credentials are read privately and never printed or saved in publication files.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse,base64,hashlib,json,re
import requests
BASE=Path(__file__).resolve().parents[2]
API='https://api.github.com/repos/MIKEAA2020/general-sustainability'
PARENT='batch 9/agent 2/ecomod_empirical_followup/'
PACKAGES=[('ecomod_followup_feasibility_R03','feasibility_R03','artifact_manifest_R03.json'),('ecomod_followup_F10','F10','artifact_manifest_F10.json')]
RECEIPT='PUBLICATION_RECEIPT_R03_F10.json'
def require(v,m):
    if not v:raise ValueError(m)
def publish(token_file):
    match=re.search(r'github_pat_[A-Za-z0-9_]+',token_file.read_text());require(match is not None,'Authorized credential not found');token=match.group()
    session=requests.Session();session.headers.update({'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'})
    def api(method,path,**kwargs):
        r=session.request(method,API+path,timeout=120,**kwargs)
        if not r.ok:raise RuntimeError('GitHub HTTP '+str(r.status_code))
        return r.json()
    def tree_at(head):
        sha=api('GET','/git/commits/'+head)['tree']['sha'];obj=api('GET','/git/trees/'+sha,params={'recursive':'1'});require(not obj.get('truncated'),'Truncated tree')
        return sha,{r['path']:r for r in obj['tree']if r['type']!='tree'}
    def preserved(old,after):
        for path,row in old.items():
            require(path in after and all(after[path][k]==row[k]for k in ['sha','mode','type']),'Prior content changed')
    local={}
    for folder,version,mname in PACKAGES:
        root=BASE/folder;manifest=json.loads((root/mname).read_text());actual={str(p.relative_to(root))for p in root.rglob('*')if p.is_file()and not any(x in {'.cache','__pycache__'}for x in p.relative_to(root).parts)}
        require(actual=={r['path']for r in manifest['files']}|{mname},'Manifest coverage')
        for row in manifest['files']:
            p=root/row['path'];require(p.stat().st_size==row['bytes']and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],'Artifact identity changed')
        for rel in actual:local[PARENT+version+'/'+rel]=root/rel
    head=api('GET','/git/ref/heads/main')['object']['sha'];tree,old=tree_at(head)
    for folder,version,mname in PACKAGES:require(not any(k.startswith(PARENT+version+'/')for k in old),'Version already exists; never rerun publisher unchanged')
    require(PARENT+RECEIPT not in old,'Receipt already exists')
    known={r['sha']for r in old.values()if r['type']=='blob'};entries=[]
    for path,p in sorted(local.items()):
        data=p.read_bytes();require(token.encode()not in data,'Credential found in artifact')
        blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        sha=blob if blob in known else api('POST','/git/blobs',json={'content':base64.b64encode(data).decode(),'encoding':'base64'})['sha']
        require(sha==blob,'Blob identity mismatch');known.add(sha);entries.append({'path':path,'mode':'100644','type':'blob','sha':sha})
    newtree=api('POST','/git/trees',json={'base_tree':tree,'tree':entries})['sha'];obj=api('GET','/git/trees/'+newtree,params={'recursive':'1'});require(not obj.get('truncated'),'Truncated new tree');after={r['path']:r for r in obj['tree']if r['type']!='tree'};preserved(old,after)
    require(set(after)-set(old)==set(local),'Unexpected path changes')
    require(api('GET','/git/ref/heads/main')['object']['sha']==head,'Branch advanced; stop')
    commit=api('POST','/git/commits',json={'message':'Add F10 and bounded R03 evidence: native SD-zero diagnostics, reference eligibility and implementation trace; preserve all prior results, author controls and eight holds','tree':newtree,'parents':[head]})['sha']
    require(api('GET','/git/ref/heads/main')['object']['sha']==head,'Branch advanced; stop')
    api('PATCH','/git/refs/heads/main',json={'sha':commit,'force':False});require(api('GET','/git/ref/heads/main')['object']['sha']==commit,'Publication head mismatch')
    print('Packages committed; verifying every published artifact',flush=True)
    def check(row):
        data=base64.b64decode(api('GET','/git/blobs/'+row['sha'])['content']);require(data==local[row['path']].read_bytes(),'Published byte mismatch');return True
    with ThreadPoolExecutor(max_workers=4)as pool:count=sum(pool.map(check,entries))
    receipt={'date':'2026-10-29','publication_commit':commit,'parent':head,'packages':{version:sum(p.startswith(PARENT+version+'/')for p in local)for folder,version,mname in PACKAGES},'all_new_files_byte_verified':count,'prior_paths_modes_hashes_preserved':len(old),'F08_F09_unchanged':True,'national_admissions_changed':False,'new_eligible_paired_change_reference':False,'calibrated_change_uncertainty_added':False,'receipt_archived_separately_additively':True}
    receipt_path=BASE/RECEIPT;require(not receipt_path.exists(),'Local receipt already exists');receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
    # Add only this new receipt, preserving the just-published packages too.
    data=receipt_path.read_bytes();sha=api('POST','/git/blobs',json={'content':base64.b64encode(data).decode(),'encoding':'base64'})['sha'];entry={'path':PARENT+RECEIPT,'mode':'100644','type':'blob','sha':sha}
    receipt_tree=api('POST','/git/trees',json={'base_tree':newtree,'tree':[entry]})['sha'];obj=api('GET','/git/trees/'+receipt_tree,params={'recursive':'1'});require(not obj.get('truncated'),'Receipt tree truncated');final={r['path']:r for r in obj['tree']if r['type']!='tree'};preserved(after,final);require(set(final)-set(after)=={entry['path']},'Unexpected receipt paths')
    require(api('GET','/git/ref/heads/main')['object']['sha']==commit,'Branch advanced before receipt')
    receipt_commit=api('POST','/git/commits',json={'message':'Archive verified F10/R03 publication receipt without changing prior content','tree':receipt_tree,'parents':[commit]})['sha']
    require(api('GET','/git/ref/heads/main')['object']['sha']==commit,'Branch advanced before receipt')
    api('PATCH','/git/refs/heads/main',json={'sha':receipt_commit,'force':False})
    require(api('GET','/git/ref/heads/main')['object']['sha']==receipt_commit,'Receipt publication head mismatch')
    require(base64.b64decode(api('GET','/git/blobs/'+sha)['content'])==data,'Receipt bytes differ')
    print(json.dumps({**receipt,'receipt_commit':receipt_commit,'receipt_byte_verified':True},indent=2),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--publish',action='store_true');p.add_argument('--token-file',type=Path,required=True);a=p.parse_args()
    if not a.publish:raise SystemExit('No publication requested; supply --publish explicitly')
    publish(a.token_file)
