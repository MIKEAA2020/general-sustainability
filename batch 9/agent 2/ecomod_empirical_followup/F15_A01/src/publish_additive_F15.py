#!/usr/bin/env python3
"""One-shot additive F15 publication. Never merge, delete, overwrite or force-push.
Requires explicit --publish and a private GITHUB_TOKEN or --token-file.
Do not rerun after a completed/partial publication: inspect the receipt and head.
"""
import argparse
import base64
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import re
import sys
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from verify_package_F15 import run as verify,files,gitsha,require,MANIFEST
API='https://api.github.com/repos/MIKEAA2020/general-sustainability'
PREFIX='batch 9/agent 2/ecomod_empirical_followup/F15_A01/'
RECEIPT='PUBLICATION_RECEIPT_F15_A01.json'


def main(args):
    require(args.publish,'Pass --publish to authorize the one-shot update')
    require(not(ROOT/RECEIPT).exists(),'Receipt exists; do not rerun')
    status=verify(False)
    token=os.environ.get('GITHUB_TOKEN','')
    if args.token_file:
        m=re.search(r'(github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9]+)',args.token_file.read_text())
        require(m is not None,'Supported token absent');token=m.group()
    require(bool(token),'Private GitHub token required')
    session=requests.Session();session.headers.update({'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'})
    session.mount('https://',HTTPAdapter(max_retries=Retry(total=3,backoff_factor=.5,
        status_forcelist=[500,502,503,504],allowed_methods=['GET'])))
    def api(method,path,**kw):
        r=session.request(method,API+path,timeout=(20,120),**kw)
        if not r.ok:raise RuntimeError(f'GitHub HTTP {r.status_code} on {path}; credentials not logged')
        return r.json()
    def tree(commit):
        t=api('GET','/git/commits/'+commit)['tree']['sha']
        data=api('GET','/git/trees/'+t,params={'recursive':'1'})
        require(not data.get('truncated'),'Truncated source tree')
        return t,{x['path']:x for x in data['tree']if x['type']!='tree'}
    def preserve(old,new):
        for name,row in old.items():
            require(name in new and all(row[k]==new[name][k]for k in ('sha','mode','type')),
                    'Prior remote leaf path changed: '+name)
    def commit_additions(parent,base,old,entries,message):
        require(api('GET','/git/ref/heads/main')['object']['sha']==parent,'Concurrent main update; stop')
        nt=api('POST','/git/trees',json={'base_tree':base,'tree':entries})['sha']
        data=api('GET','/git/trees/'+nt,params={'recursive':'1'})
        require(not data.get('truncated'),'Truncated proposed tree')
        new={x['path']:x for x in data['tree']if x['type']!='tree'};preserve(old,new)
        require(set(new)-set(old)=={x['path']for x in entries},'Unexpected path changes')
        c=api('POST','/git/commits',json={'message':message,'tree':nt,'parents':[parent]})['sha']
        require(api('GET','/git/ref/heads/main')['object']['sha']==parent,'Concurrent main update before ref')
        api('PATCH','/git/refs/heads/main',json={'sha':c,'force':False})
        require(api('GET','/git/ref/heads/main')['object']['sha']==c,'Unexpected main HEAD')
        actual_t,actual=tree(c);require(actual_t==nt,'Published tree mismatch');preserve(old,actual)
        return c,nt,actual
    head=api('GET','/git/ref/heads/main')['object']['sha'];base,old=tree(head)
    require(not any(p.startswith(PREFIX)for p in old),'Target prefix exists; refuse overwrite')
    candidates=files()+[ROOT/MANIFEST];payloads={}
    for p in candidates:
        b=p.read_bytes();require(token.encode()not in b,'Credential found in publication candidate')
        payloads[str(p.relative_to(ROOT))]=b
    existing={x['sha']for x in old.values()if x['type']=='blob'}
    unique={gitsha(b):b for b in payloads.values()}
    for h,b in unique.items():
        if h not in existing:
            obj=api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})
            require(obj['sha']==h,'Uploaded blob mismatch')
    entries=[dict(path=PREFIX+n,mode='100644',type='blob',sha=gitsha(b))for n,b in payloads.items()]
    package_commit,nt,new=commit_additions(head,base,old,entries,
        'Restore F15 omitted inherited results and method definitions: six main figures, two main tables, 25 linked SI tables; preserve all earlier files')
    receipt=dict(package_commit=package_commit,parent_commit=head,remote_prefix=PREFIX,
                 package_files=len(payloads),package_bytes=sum(map(len,payloads.values())),
                 one_integrated_publication=True,main_pages=status['main_pages'],SI_pages=status['SI_pages'],
                 workbook_sheets=status['workbook_sheets'],editorial_artifacts_reproduced=9,new_empirical_estimates=False,
                 main_figures=6,main_tables=2,SI_figures=2,SI_tables=25,all_SI_items_cited=True,
                 protected_F11_F12_F13_F14_local_files_verified=status['protected_F11_F12_F13_F14_files'],
                 Canadian_reported_total_change_interval_unresolved=True,
                 prior_remote_leaf_paths_preserved=len(old),original_primary_AGB_analyses_incomplete=8,secondary_inventory_volume_inferences=2,
                 verification_status='Package committed; byte-download verification pending')
    # A recovery point if the network fails after the commit; never claim completion early.
    (ROOT/RECEIPT).write_text(json.dumps(receipt,indent=2)+'\n')
    def check(pair):
        h,b=pair;obj=api('GET','/git/blobs/'+h);remote=base64.b64decode(obj['content'])
        require(gitsha(remote)==h and remote==b,'Downloaded package blob mismatch');return True
    with ThreadPoolExecutor(max_workers=5)as pool:require(all(pool.map(check,unique.items())),'Download verification failed')
    for name,b in payloads.items():require(new[PREFIX+name]['sha']==gitsha(b),'Published path mismatch')
    receipt.update(verification_status='Every package path and every unique package blob byte-verified',
                   unique_package_blobs_download_verified=len(unique),
                   prior_versions_unchanged=True,no_branch_merged=True,no_durable_local_or_remote_files_deleted=True,
                   tests_per_mode=status['tests_per_execution_mode'])
    (ROOT/RECEIPT).write_text(json.dumps(receipt,indent=2)+'\n')
    b=(ROOT/RECEIPT).read_bytes();h=gitsha(b)
    require(api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha']==h,'Receipt upload mismatch')
    final_commit,_,last=commit_additions(package_commit,nt,new,
        [dict(path=PREFIX+RECEIPT,mode='100644',type='blob',sha=h)],
        'Record F15 full package download verification and prior-history preservation')
    check((h,b));require(last[PREFIX+RECEIPT]['sha']==h,'Receipt path mismatch')
    print(json.dumps(dict(**receipt,receipt_commit=final_commit),indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--publish',action='store_true');p.add_argument('--token-file',type=Path)
    main(p.parse_args())
