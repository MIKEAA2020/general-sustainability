"""One-shot additive publication of the authorized governance audit only.
Rejects existing versioned paths; preserves prior modes/hashes; non-force push;
byte-verifies package and a separately archived receipt. No manuscript edits.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse,base64,hashlib,json,re
import requests
BASE=Path(__file__).resolve().parents[2]
ROOT=BASE/'governance_audit_P4_v41_R01'
API='https://api.github.com/repos/MIKEAA2020/general-sustainability'
PARENT='batch 9/agent 2/ecomod_audit/'
PREFIX=PARENT+'governance_p4_v41_R01/'
RECEIPT='PUBLICATION_RECEIPT_GOVERNANCE_P4_V41_R01.json'
MANIFEST='artifact_manifest_R01.json'
def require(ok,message):
    if not ok:raise ValueError(message)
def publish(token_file):
    match=re.search(r'github_pat_[A-Za-z0-9_]+',token_file.read_text());require(match is not None,'Authorized credential not found');token=match.group()
    session=requests.Session();session.headers.update({'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'})
    def api(method,path,**kwargs):
        response=session.request(method,API+path,timeout=120,**kwargs)
        if not response.ok:raise RuntimeError('GitHub HTTP '+str(response.status_code))
        return response.json()
    def tree_at(head):
        sha=api('GET','/git/commits/'+head)['tree']['sha'];obj=api('GET','/git/trees/'+sha,params={'recursive':'1'});require(not obj.get('truncated'),'Truncated tree')
        return sha,{r['path']:r for r in obj['tree']if r['type']!='tree'}
    def preserved(old,new):
        for path,row in old.items():require(path in new and all(new[path][k]==row[k]for k in ['sha','mode','type']),'Prior content changed')
    manifest=json.loads((ROOT/MANIFEST).read_text());actual={str(p.relative_to(ROOT))for p in ROOT.rglob('*')if p.is_file()and '__pycache__'not in p.parts}
    require(actual=={row['path']for row in manifest['files']}|{MANIFEST},'Manifest coverage mismatch')
    for row in manifest['files']:
        p=ROOT/row['path'];data=p.read_bytes();require(len(data)==row['bytes']and hashlib.sha256(data).hexdigest()==row['sha256'],'Manifest identity mismatch')
    local={PREFIX+rel:ROOT/rel for rel in actual};head=api('GET','/git/ref/heads/main')['object']['sha'];base,old=tree_at(head)
    require(not any(path.startswith(PREFIX)for path in old),'Version already published; do not rerun')
    require(PARENT+RECEIPT not in old and not(BASE/RECEIPT).exists(),'Receipt already exists')
    known={row['sha']for row in old.values()if row['type']=='blob'};entries=[]
    for path,p in sorted(local.items()):
        data=p.read_bytes();require(token.encode()not in data,'Credential found in artifact');sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if sha not in known:
            returned=api('POST','/git/blobs',json={'content':base64.b64encode(data).decode(),'encoding':'base64'})['sha'];require(returned==sha,'Blob identity mismatch');known.add(sha)
        entries.append({'path':path,'mode':'100644','type':'blob','sha':sha})
    newtree=api('POST','/git/trees',json={'base_tree':base,'tree':entries})['sha'];obj=api('GET','/git/trees/'+newtree,params={'recursive':'1'});require(not obj.get('truncated'),'Truncated proposed tree');after={r['path']:r for r in obj['tree']if r['type']!='tree'}
    preserved(old,after);require(set(after)-set(old)==set(local),'Unexpected paths');require(api('GET','/git/ref/heads/main')['object']['sha']==head,'Branch advanced; stop')
    commit=api('POST','/git/commits',json={'message':'Add bounded audit of C17-cited governance v41: independent spectra, interval mixed-delay witness, sampled-map and citation checks; no manuscript changes','tree':newtree,'parents':[head]})['sha']
    require(api('GET','/git/ref/heads/main')['object']['sha']==head,'Branch advanced; stop');api('PATCH','/git/refs/heads/main',json={'sha':commit,'force':False});require(api('GET','/git/ref/heads/main')['object']['sha']==commit,'Published HEAD mismatch')
    print('Audit committed; byte-verifying all new files',flush=True)
    def verify(entry):
        data=base64.b64decode(api('GET','/git/blobs/'+entry['sha'])['content']);require(data==local[entry['path']].read_bytes(),'Remote artifact bytes differ');return True
    with ThreadPoolExecutor(max_workers=4)as pool:verified=sum(pool.map(verify,entries))
    receipt={'date':'2026-10-29','publication_commit':commit,'parent':head,'package_path':PREFIX,'new_files_byte_verified':verified,'prior_non_tree_paths_modes_hashes_preserved':len(old),'governance_and_C17_manuscripts_unchanged':True,'declarations_bibliographies_deposits_unchanged':True,'empirical_validation_added':False,'global_DDE_campaign_rerun':False,'tests_normal':26,'tests_optimized':26,'receipt_archived_separately':True}
    receipt_path=BASE/RECEIPT;receipt_path.write_text(json.dumps(receipt,indent=2)+'\n');data=receipt_path.read_bytes()
    sha=api('POST','/git/blobs',json={'content':base64.b64encode(data).decode(),'encoding':'base64'})['sha'];entry={'path':PARENT+RECEIPT,'mode':'100644','type':'blob','sha':sha}
    rt=api('POST','/git/trees',json={'base_tree':newtree,'tree':[entry]})['sha'];obj=api('GET','/git/trees/'+rt,params={'recursive':'1'});require(not obj.get('truncated'),'Receipt tree truncated');final={r['path']:r for r in obj['tree']if r['type']!='tree'};preserved(after,final);require(set(final)-set(after)=={entry['path']},'Unexpected receipt paths')
    require(api('GET','/git/ref/heads/main')['object']['sha']==commit,'Branch advanced before receipt');rc=api('POST','/git/commits',json={'message':'Archive verified governance v41 audit publication receipt additively','tree':rt,'parents':[commit]})['sha']
    require(api('GET','/git/ref/heads/main')['object']['sha']==commit,'Branch advanced before receipt');api('PATCH','/git/refs/heads/main',json={'sha':rc,'force':False});require(api('GET','/git/ref/heads/main')['object']['sha']==rc,'Receipt HEAD mismatch');require(base64.b64decode(api('GET','/git/blobs/'+sha)['content'])==data,'Receipt bytes differ')
    print(json.dumps({**receipt,'receipt_commit':rc,'receipt_byte_verified':True},indent=2),flush=True)
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--publish',action='store_true');parser.add_argument('--token-file',type=Path,required=True);args=parser.parse_args()
    if not args.publish:raise SystemExit('Supply --publish to request authorized one-shot publication')
    publish(args.token_file)
