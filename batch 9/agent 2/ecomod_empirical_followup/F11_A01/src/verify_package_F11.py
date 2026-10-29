#!/usr/bin/env python3
"""Verify scientific guards and freeze/verify the additive F11 file manifest."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
MANIFEST='artifact_manifest_F11_A01.json'
POST_PUBLICATION={'PUBLICATION_RECEIPT_F11_A01.json'}
EXCLUDED={'.cache','__pycache__','.git'}

def sha(b):return hashlib.sha256(b).hexdigest()
def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def require(ok,message):
    if not ok:raise ValueError(message)
def load(name):return json.loads((ROOT/name).read_text())
def files():
    return sorted(p for p in ROOT.rglob('*')if p.is_file()
                  and not any(x in EXCLUDED for x in p.relative_to(ROOT).parts)
                  and p.name not in POST_PUBLICATION and p.name!=MANIFEST)

def scientific_guards():
    inherited=load('metadata/inherited_F10_identity_F11.json')['files']
    require(len(inherited)==218,'Incomplete inherited package')
    for r in inherited:require(sha((ROOT/'inherited_F10'/r['path']).read_bytes())==r['sha256'],'Inherited source changed: '+r['path'])
    for prefix,n in [('baseline',134),('tests',58)]:
        for mode in ('normal','optimized'):
            text=(ROOT/f'evidence/{prefix}_{mode}_F11.log').read_text()
            require(re.search(rf'Ran {n} tests in .*\n\nOK\s*$',text) is not None,'Incomplete test run')
            require('skipped'not in text,'Skipped tests are not a complete pass')
    for r in load('metadata/source_reproduction_comparison_F11.json')['files']:
        require(r['exact_bytes_match']and r['inherited_sha256']==r['fresh_sha256'],'Source reproduction mismatch')
    for r in load('metadata/document_QA_F11.json')['documents']:
        require(sha((ROOT/r['file']).read_bytes())==r['sha256'],'Stale PDF QA')
        require(not r['warning_lines']and not r['unresolved_reference_markers']and not r['text_outside_page_bounds'],'Failed PDF QA')
    numeric=load('metadata/numerical_reproducibility_F11.json')
    require(numeric['normal_and_optimized_numeric_bytes_identical'],'Numeric determinism failed')
    for name,expected in numeric['files'].items():require(sha((ROOT/name).read_bytes())==expected,'Stale numerical comparison: '+name)
    with (ROOT/'inherited_F10/data/support/physical_admission_F08.csv').open()as f:holds=list(csv.DictReader(f))
    require(len(holds)==8 and all(r['admission']=='hold_not_admitted'for r in holds),'National holds changed')
    require(load('metadata/joint_identification_F11.json')['all_four_strict_sign_quadrants_feasible'],'Joint sign result missing')
    require(load('metadata/prior_R02_remote_confirmation_F11.json')['all_previous_creations_already_published'],'Prior publication unverified')
    for name in ['README_F11_A01.md','AUDIT_RESOLUTION_AND_ELEVATION_F11_A01.md',
                 'REVISION_AND_DELETION_ACCOUNT_F11_A01.md','ANALYSIS_SPECIFICATION_F11_A01.md']:
        require((ROOT/name).is_file(),'Required scientific account absent')


def run(write=False):
    scientific_guards()
    records=[]
    for p in files():
        b=p.read_bytes();records.append(dict(path=str(p.relative_to(ROOT)),bytes=len(b),sha256=sha(b),git_blob_sha1=gitsha(b)))
    if write:
        payload=dict(version='F11_A01',kind='Additive scientific identification elevation, not ecological validation',
                     files=records,file_count=len(records),manifest_self_excluded=True,
                     post_publication_receipts_excluded=sorted(POST_PUBLICATION),
                     raw_provider_arrays_or_documents_added=False,
                     protected_F10_files_unchanged=218,all_eight_national_holds_retained=True)
        (ROOT/MANIFEST).write_text(json.dumps(payload,indent=2)+'\n')
    else:
        expected=load(MANIFEST)
        require(records==expected['files'],'Manifest mismatch or unlisted durable files')
    return dict(verified_files=len(records),bytes=sum(x['bytes']for x in records),
                inherited_F10_files=218,tests_per_execution_mode=192,
                national_holds=8,manifest_written=write)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--write-manifest',action='store_true')
    a=p.parse_args();print(json.dumps(run(a.write_manifest),indent=2))
