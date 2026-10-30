#!/usr/bin/env python3
"""Scientific/output guards and additive F12 manifest verification."""
import argparse,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MANIFEST='artifact_manifest_F12_A01.json';POST={'PUBLICATION_RECEIPT_F12_A01.json'}

def require(ok,message):
 if not ok:raise ValueError(message)
def sha(b):return hashlib.sha256(b).hexdigest()
def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def load(name):return json.loads((ROOT/name).read_text())
def files():return sorted(p for p in ROOT.rglob('*')if p.is_file()and not any(x in {'.cache','__pycache__','.git'}for x in p.relative_to(ROOT).parts)and p.name not in POST|{MANIFEST})

def guards():
 n=load('metadata/numerical_reproducibility_F12.json');require(n['normal_and_optimized_bytes_identical']and n['outputs_checked']==50,'Incomplete numerical reproduction')
 for name,digest in n['files'].items():require(sha((ROOT/name).read_bytes())==digest,'Stale numeric artifact '+name)
 for name,digest in n['source_scripts'].items():require(sha((ROOT/'src'/name).read_bytes())==digest,'Numerical source changed after reproducibility '+name)
 for mode in ['normal','optimized']:
  t=(ROOT/f'evidence/tests_{mode}_F12.log').read_text();require(re.search(r'Ran 40 tests in .*\n\nOK\s*$',t)is not None and 'skipped'not in t,'Tests incomplete '+mode);require('ResourceWarning'not in t,'Unresolved resource warning')
 q=load('metadata/deliverable_QA_F12.json');require(q['visual_review_completed']and q['visual_review_pages']==list(range(1,q['pdf']['pages']+1)),'Visual review incomplete');require(not q['pdf']['text_outside_page_bounds']and q['pdf']['exact_AI_declaration']and q['pdf']['ORCID_hyperlink'],'PDF QA failure')
 for kind in ['pdf','workbook']:require(sha((ROOT/q[kind]['file']).read_bytes())==q[kind]['sha256'],'Stale deliverable QA '+kind)
 w=load('metadata/transition_witness_audit_F12.json');require(w['all_pass']and w['saved_primal_dual_witnesses_independently_checked']==634 and not w['solver_called'],'Saved witness audit incomplete')
 s=load('metadata/synthesis_F12.json');require(s['original_primary_national_AGB_admissions']==0 and s['secondary_inventory_volume_inferences']==1,'Primary/secondary scope drift');require(not s['conversion_association_or_causal_effect_estimated']and not s['reporting_accuracy_against_independent_physical_truth_estimated'],'Unsupported inference claim')
 old=load('metadata/protected_F11_identity_F12.json');prior=ROOT.parent/old['root_name']
 if not prior.is_dir():prior=ROOT.parent/'F11_A01'
 require(prior.is_dir(),'Protected F11 package required for publication verification')
 for r in old['files']:require(sha((prior/r['path']).read_bytes())==r['sha256'],'Protected F11 changed '+r['path'])
 for name in ['README_F12_A01.md','COMPLETION_AND_REMAINING_WORK_F12_A01.md','REVISION_AND_DELETION_ACCOUNT_F12_A01.md','metadata/WORK_DAG_F12.json']:require((ROOT/name).is_file(),'Missing disclosure '+name)
 for p in files():require(not p.name.startswith(('BRA_C11_accuracy','IDN_C41_ATBD','FIN_NFI13_paper'))or p.suffix!='.pdf','Provider PDF body in deposit')
 return len(old['files'])

def run(write=False):
 protected=guards();records=[]
 for p in files():
  b=p.read_bytes();records.append(dict(path=str(p.relative_to(ROOT)),bytes=len(b),sha256=sha(b),git_blob_sha1=gitsha(b)))
 if write:(ROOT/MANIFEST).write_text(json.dumps(dict(version='F12_A01',kind='National account, classification, inventory-cycle and conditional conversion empirical extension',files=records,file_count=len(records),manifest_self_excluded=True,post_publication_receipts_excluded=sorted(POST),protected_F11_files_unchanged=protected,original_primary_national_AGB_admissions=0,secondary_inventory_volume_inferences=1,raw_provider_workbooks_PDFs_and_raster_arrays_redistributed=False),indent=2)+'\n')
 else:require(records==load(MANIFEST)['files'],'Manifest mismatch or unlisted durable artifact')
 return dict(verified_files=len(records),bytes=sum(r['bytes']for r in records),protected_F11_files=protected,tests_per_execution_mode=40,numeric_outputs_reproduced=50,production_LPs_and_saved_primal_dual_witnesses=634,original_primary_AGB_holds=8,secondary_volume_inferences=1,manifest_written=write)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write-manifest',action='store_true');print(json.dumps(run(p.parse_args().write_manifest),indent=2))
