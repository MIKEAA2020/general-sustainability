#!/usr/bin/env python3
"""Reproduce F10 tests/build and optional guarded F05/F07 source derivations.
Always operate in excluded scratch storage; do not modify inherited_F10.
Protected F08/F09 comparison packages are restored from an immutable Git tree,
or copied from an explicitly supplied comparator root. Credentials are never logged.
"""
import argparse
import base64
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

ROOT=Path(__file__).resolve().parents[1]
API='https://api.github.com/repos/MIKEAA2020/general-sustainability'
PIN='37b520805cd94be875a6d045c2806c9463eae4d5'


def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def restore_comparators(scratch,token_file=None):
    token=os.environ.get('GITHUB_TOKEN','')
    if token_file:
        match=re.search(r'(github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9]+)',token_file.read_text())
        if not match:raise ValueError('No supported token found in token file')
        token=match.group()
    if not token:raise ValueError('Set GITHUB_TOKEN or pass --token-file for authenticated comparator restoration')
    session=requests.Session();session.headers.update({'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'})
    session.mount('https://',HTTPAdapter(max_retries=Retry(total=3,backoff_factor=.5,
        status_forcelist=[500,502,503,504],allowed_methods=['GET'])))
    def get(path,**kw):
        r=session.get(API+path,timeout=(20,120),**kw)
        if not r.ok:raise RuntimeError(f'GitHub HTTP {r.status_code}; no credential included')
        return r.json()
    commit=get('/git/commits/'+PIN)
    tree=get('/git/trees/'+commit['tree']['sha'],params={'recursive':'1'})
    if tree.get('truncated'):raise ValueError('Truncated immutable source tree')
    pending=[]
    for version in ('F08','F09'):
        prefix=f'batch 9/agent 2/ecomod_empirical_followup/{version}/'
        selected=[r for r in tree['tree']if r['type']=='blob'and r['path'].startswith(prefix)]
        if not selected:raise ValueError('Pinned comparison package absent')
        for r in selected:
            rel=Path(r['path'][len(prefix):])
            if rel.is_absolute()or '..'in rel.parts or r['size']>25000000:raise ValueError('Unsafe comparator path/size')
            pending.append((r,scratch/f'ecomod_followup_{version}'/rel))
    def fetch(pair):
        r,path=pair
        if path.exists():
            if gitsha(path.read_bytes())!=r['sha']:raise ValueError('Differing comparator; refuse overwrite')
            return
        payload=get('/git/blobs/'+r['sha']);b=base64.b64decode(payload['content'])
        if len(b)!=r['size']or gitsha(b)!=r['sha']:raise ValueError('Comparator blob identity mismatch')
        path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(b)
    with ThreadPoolExecutor(max_workers=5)as pool:list(pool.map(fetch,pending))
    return len(pending)


def command(args,cwd,log):
    with log.open('w')as out:
        p=subprocess.run(args,cwd=cwd,stdout=out,stderr=subprocess.STDOUT)
    if p.returncode:raise RuntimeError(f'Command failed; see {log.name}')


def run(args):
    scratch=ROOT/'.cache/legacy_reproduction_F11';scratch.mkdir(parents=True,exist_ok=True)
    if args.comparator_root:
        for version in ('F08','F09'):
            name=f'ecomod_followup_{version}';source=args.comparator_root/name
            if not source.is_dir():raise ValueError('Comparator root lacks '+name)
            shutil.copytree(source,scratch/name,dirs_exist_ok=True)
    else:
        restore_comparators(scratch,args.token_file)
    stage=scratch/'F10';shutil.copytree(ROOT/'inherited_F10',stage,dirs_exist_ok=True)
    ev=ROOT/'evidence';ev.mkdir(exist_ok=True)
    for optimized,label in [(False,'normal'),(True,'optimized')]:
        cmd=[sys.executable]+(['-O']if optimized else[])+['-m','unittest','discover','-s','tests','-v']
        log=ev/f'baseline_{label}_F11.log';command(cmd,stage,log)
        text=log.read_text()
        if 'Ran 134 tests'not in text or '\nOK\n'not in text or 'skipped'in text:
            raise ValueError('Full 134-test baseline without skips required')
    command(['bash','src/build_F10.sh'],stage,ev/'baseline_build_F11.log')
    if args.source_rerun:
        cache=ROOT/'.cache/source_reproduction_F11'
        command([sys.executable,'src/allocation_envelopes.py','--cache',str(cache)],stage,
                ev/'source_reproduction_F11.log')
        command([sys.executable,'src/brazil_support.py','--cache',str(cache/'ranges')],stage,
                ev/'cover_fraction_reproduction_F11.log')
        paths=['data/allocation/endpoint_envelopes_F07.csv','data/allocation/difference_envelopes_F07.csv',
               'data/allocation/full_cell_auxiliary_F07.csv','data/allocation/overlap_certificates_F07.npz',
               'metadata/allocation/computation_F07.json','data/brazil/BRA_F05_support_fractions.npz',
               'data/brazil/endpoint_support_areas.csv','data/brazil/source_class_areas.csv',
               'metadata/brazil/alignment_checks.json','metadata/brazil/range_provenance.json',
               'data/brazil/common_support_summary.json']
        records=[]
        for name in paths:
            a=(ROOT/'inherited_F10'/name).read_bytes();b=(stage/name).read_bytes()
            if a!=b:raise ValueError('Fresh derived bytes differ: '+name)
            records.append(dict(path=name,exact_bytes_match=True,
                inherited_sha256=hashlib.sha256(a).hexdigest(),fresh_sha256=hashlib.sha256(b).hexdigest()))
        payload=dict(scope='Fresh guarded BRA 2015/2023 native retrieval and MapBiomas range decoding; F05/F07 derivations rerun in scratch; not all reference/document acquisition',files=records)
        (ROOT/'metadata/source_reproduction_comparison_F11.json').write_text(json.dumps(payload,indent=2)+'\n')
    print('F10 134 tests passed without skips in each Python mode; main/SI rebuilt in scratch.')
    if args.source_rerun:print('All eleven newly derived F05/F07 outputs byte-identical to protected inputs.')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--token-file',type=Path)
    p.add_argument('--comparator-root',type=Path,help='Existing parent of ecomod_followup_F08 and F09')
    p.add_argument('--source-rerun',action='store_true')
    run(p.parse_args())
