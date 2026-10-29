"""One-shot additive publication of the authorized governance v43/SIv10 package.
Never invokes either older publisher. Refuses an existing version path.
Requires --publish and an external credential file; no credential is stored.
"""
from pathlib import Path
import argparse,base64,hashlib,json,re
from concurrent.futures import ThreadPoolExecutor
import requests
from make_manifest_v43 import ROOT,NAME,artifacts
REPO='MIKEAA2020/general-sustainability';API='https://api.github.com/repos/'+REPO
PREFIX='batch 9/agent 2/governance_elevation/P4_v43_P02/'
PARENT='batch 9/agent 2/governance_elevation/'
RECEIPT='PUBLICATION_RECEIPT_GOVERNANCE_P4_V43_P02.json'
def require(condition,message):
    if not condition:raise RuntimeError(message)
def publish(token_file):
    match=re.search(r'github_pat_[A-Za-z0-9_]+',token_file.read_text());require(match is not None,'Authorized credential not found');token=match.group()
    session=requests.Session();session.headers.update({'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'})
    def api(method,path,**kwargs):
        response=session.request(method,API+path,timeout=120,**kwargs)
        if not response.ok:raise RuntimeError('GitHub HTTP '+str(response.status_code))
        return response.json()
    def tree_at(head):
        tree=api('GET','/git/commits/'+head)['tree']['sha'];obj=api('GET','/git/trees/'+tree,params={'recursive':'1'});require(not obj.get('truncated'),'Truncated tree');return tree,{r['path']:r for r in obj['tree']if r['type']!='tree'}
    def check_tree(tree):
        obj=api('GET','/git/trees/'+tree,params={'recursive':'1'});require(not obj.get('truncated'),'Truncated proposed tree');return {r['path']:r for r in obj['tree']if r['type']!='tree'}
    def preserved(old,new):
        for path,row in old.items():require(path in new and all(new[path][k]==row[k]for k in ['sha','mode','type']),'Prior path/hash/mode changed')
    manifest=json.loads((ROOT/NAME).read_text());actual={str(p.relative_to(ROOT)):p for p in artifacts()};require(set(actual)=={r['path']for r in manifest['files']}|{NAME},'Manifest coverage mismatch')
    for row in manifest['files']:
        b=actual[row['path']].read_bytes();require(len(b)==row['bytes']and hashlib.sha256(b).hexdigest()==row['sha256'],'Manifest identity mismatch')
    for label in ['normal','optimized']:
        log=(ROOT/f'data/tests_{label}_v43.txt').read_text();require('Ran 49 tests'in log and '\nOK'in log,'New test suite not passed')
        inherited=(ROOT/f'data/inherited_tests_{label}_v43.txt').read_text();require('Ran 64 tests'in inherited and '\nOK'in inherited,'Inherited test suite not passed')
    head=api('GET','/git/ref/heads/main')['object']['sha'];base,old=tree_at(head)
    require(not any(path.startswith(PREFIX)for path in old),'Version already exists; do not rerun')
    receipt_path=ROOT.parent/RECEIPT;require(PARENT+RECEIPT not in old and not receipt_path.exists(),'Receipt already exists')
    known={r['sha']for r in old.values()if r['type']=='blob'};local={PREFIX+k:v for k,v in actual.items()};entries=[]
    print('Fresh HEAD verified; preparing additive package',flush=True)
    for path,p in sorted(local.items()):
        b=p.read_bytes();require(token.encode()not in b,'Credential found in artifact');sha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        if sha not in known:
            got=api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha'];require(got==sha,'Blob identity mismatch');known.add(sha)
        entries.append({'path':path,'mode':'100644','type':'blob','sha':sha})
    tree=api('POST','/git/trees',json={'base_tree':base,'tree':entries})['sha'];after=check_tree(tree);preserved(old,after);require(set(after)-set(old)==set(local),'Unexpected new paths')
    require(api('GET','/git/ref/heads/main')['object']['sha']==head,'Branch advanced; stop safely')
    commit=api('POST','/git/commits',json={'message':'Add governance v43 and SIv10: complete protective basin, all-delay equilibrium spectra, rigorous infinite-Fourier residuals and dynamic field tests; preserve C17','tree':tree,'parents':[head]})['sha']
    require(api('GET','/git/ref/heads/main')['object']['sha']==head,'Branch advanced before update');api('PATCH','/git/refs/heads/main',json={'sha':commit,'force':False});require(api('GET','/git/ref/heads/main')['object']['sha']==commit,'Published HEAD mismatch')
    print('Package committed; byte-verifying every new artifact',flush=True)
    def verify(row):
        b=base64.b64decode(api('GET','/git/blobs/'+row['sha'])['content']);require(b==local[row['path']].read_bytes(),'Remote bytes differ');return True
    with ThreadPoolExecutor(max_workers=4)as pool:verified=sum(pool.map(verify,entries))
    receipt={'date':'2026-10-29','publication_commit':commit,'parent':head,'package_path':PREFIX,'new_files_byte_verified':verified,'prior_non_tree_paths_modes_hashes_preserved':len(old),'ECOMOD_C17_unchanged':True,'earlier_governance_revisions_unchanged':True,'deposits_and_C17_version_specific_citations_unchanged':True,'main_revision':'v43','supplement_revision':'v10','main_pages':54,'supplement_pages':20,'tests_normal':113,'tests_optimized':113,'classical_nonlinear_Hopf_hypotheses_verified':True,'protective_all_cadences_theorem_retained':True,'nonlinear_protective_stock_floor_theorem_retained':True,'floating_upper_branch_connection_retained':True,'herring_event_evidence_retained':True,'quantitative_dynamic_field_tests_executed':True,'joint_dynamic_field_validation_achieved':False,'field_common_support_amendment_disclosed':True,'complete_protective_basin_under_sufficient_gain':True,'complete_equilibrium_all_positive_delay_root_count':True,'full_infinite_Fourier_fold_residual_bounds':True,'full_periodic_Floquet_certificate_achieved':False,'mobilising_complete_basins_achieved':False,'continuum_fold_lift_achieved':False,'odd_65_129_257_augmented_fold_solves_executed':True,'manifest_sha256':hashlib.sha256((ROOT/NAME).read_bytes()).hexdigest(),'receipt_archived_separately':True}
    receipt_path.write_text(json.dumps(receipt,indent=2)+'\n');b=receipt_path.read_bytes();sha=api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha'];rt=api('POST','/git/trees',json={'base_tree':tree,'tree':[{'path':PARENT+RECEIPT,'mode':'100644','type':'blob','sha':sha}]})['sha'];final=check_tree(rt);preserved(after,final);require(set(final)-set(after)=={PARENT+RECEIPT},'Unexpected receipt paths')
    require(api('GET','/git/ref/heads/main')['object']['sha']==commit,'Branch advanced before receipt; package remains published')
    rc=api('POST','/git/commits',json={'message':'Archive verified additive governance v43/SIv10 publication receipt','tree':rt,'parents':[commit]})['sha'];require(api('GET','/git/ref/heads/main')['object']['sha']==commit,'Branch advanced before receipt update');api('PATCH','/git/refs/heads/main',json={'sha':rc,'force':False});require(api('GET','/git/ref/heads/main')['object']['sha']==rc,'Receipt HEAD mismatch');require(base64.b64decode(api('GET','/git/blobs/'+sha)['content'])==b,'Receipt bytes differ')
    print(json.dumps({**receipt,'receipt_commit':rc,'receipt_byte_verified':True},indent=2),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--publish',action='store_true');p.add_argument('--token-file',type=Path,required=True);a=p.parse_args()
    if not a.publish:raise SystemExit('Supply --publish only for an authorized one-shot publication')
    publish(a.token_file)
