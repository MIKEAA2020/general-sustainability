#!/usr/bin/env python3
"""Freeze/verify the integrated additive package and protected dependencies.
Does not rebuild manuscripts or write into a frozen manifest during verification.
"""
import argparse,hashlib,json,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MANIFEST='artifact_manifest_F13_A01.json'
POST={'PUBLICATION_RECEIPT_F13_A01.json'}
def require(ok,msg):
 if not ok:raise ValueError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def load(name):return json.loads((ROOT/name).read_text())
def files():return sorted(p for p in ROOT.rglob('*')if p.is_file()and not any(v in {'.cache','__pycache__','.git'}for v in p.relative_to(ROOT).parts)and p.name not in POST|{MANIFEST})
def prior(name):
 p=ROOT.parent/name
 if not p.is_dir():p=ROOT.parent/('F11_A01'if'F11'in name else'F12_A01')
 require(p.is_dir(),'Protected dependency folder missing '+name);return p

def guards():
 n=load('metadata/numerical_reproducibility_F13.json')
 require(n['new_numerical_outputs']==13 and n['all_new_outputs_byte_identical_in_both_modes'],'Numerical reproduction incomplete')
 for name,digest in n['files'].items():require(sha((ROOT/name).read_bytes())==digest,'Changed numerical output '+name)
 for name,digest in n['source_scripts'].items():require(sha((ROOT/'src'/name).read_bytes())==digest,'Changed reproduced source '+name)
 for mode in ['normal','optimized']:
  t=(ROOT/f'evidence/tests_{mode}_F13.log').read_text();require(re.search(r'Ran 30 tests in .*\n\nOK\s*$',t)is not None and 'skipped'not in t,'Tests incomplete '+mode)
  require('ResourceWarning'not in t,'Resource warning unresolved '+mode)
 q=load('metadata/deliverable_QA_F13.json');require(q['visual_review_completed'],'Visual QA not confirmed')
 for kind in ['main','SI']:
  r=q[kind];require(not r['text_outside_page_bounds']and r['all_fonts_embedded']and r['ORCID_hyperlink'],'PDF QA failed '+kind)
  require(q['visual_review_pages'][kind]==list(range(1,r['pages']+1)),'Not every page visually reviewed')
  require(sha((ROOT/r['file']).read_bytes())==r['sha256'],'PDF changed after QA '+kind)
 require(q['main']['exact_AI_declaration'],'AI declaration changed')
 w=q['workbook'];require(w['sheets']==30 and w['inherited_sheets_compared']==19 and w['new_CSV_cells_independently_checked']>4000,'Workbook QA incomplete')
 require(sha((ROOT/w['file']).read_bytes())==w['sha256'],'Workbook changed after QA')
 s=load('data/source_analysis_summary_F13.json');require(s['original_primary_AGB_admissions']==0,'Original primary target changed')
 require(s['france_longest_cycle_delta_Mm3']==200 and s['france_longest_cycle_union90']==[104.,296.],'French source/rounding result drift')
 ca=load('data/CAN_NFI_scope_audit_F13.json');require(ca['uncertainty_tables_carry_matching_version_3_1_labels']and not ca['original_primary_AGB_admission'],'Canadian uncertainty/scope drift')
 fr=load('data/FRA_scope_and_bias_F13.json');require(fr['unknown_differential_method_bias_not_bounded']and fr['retrospective_cubage_and_rebut_harmonization_not_certified'],'French bias caveat omitted')
 co=load('data/COD_C1_interpretation_F13.json');require(co['subunits_not_certified_partition_of_country']and co['no_biomass_change_or_conversion_causality_inferred'],'Congo support/quantity drift')
 registry=load('metadata/source_registry_F13.json');require(all(not r['raw_redistributed']and r['bytes']<=r['cap_bytes']<=25000000 for r in registry.values()),'Source cap or redistribution guard failed')
 protected=0
 for package in load('metadata/protected_F11_F12_identity_F13.json')['packages']:
  path=prior(package['root_name'])
  for r in package['files']:require(sha((path/r['path']).read_bytes())==r['sha256'],'Protected dependency changed '+str(path/r['path']));protected+=1
 # Verify preserved F12 reproduction, test, QA and independent LP-certificate evidence.
 f12=prior('ecomod_empirical_closure_F12_A01')
 r=subprocess.run([sys.executable,str(f12/'src/verify_package_F12.py')],capture_output=True,text=True,check=True)
 inherited=json.loads(r.stdout);require(inherited['production_LPs_and_saved_primal_dual_witnesses']==634 and inherited['numeric_outputs_reproduced']==50,'Inherited F12 evidence not verified')
 for r in load('metadata/minimal_typesetting_dependencies_F13.json')['files']:
  require(sha((ROOT/r['vendored_relative_path']).read_bytes())==r['vendored_sha256'],'Vendored typesetting input changed')
 for name in ['README_F13_A01.md','COMPLETION_AND_REMAINING_WORK_F13_A01.md','REVISION_AND_DELETION_ACCOUNT_F13_A01.md','requirements_F13_A01.txt']:
  require((ROOT/name).is_file(),'Missing disclosure '+name)
 main=(ROOT/'integrated_F13_A01_main.tex').read_text();require(main.split('\\begin{enumerate}',1)[1].split('\\end{enumerate}',1)[0].count('\\item ')==5,'Five-question integration changed')
 require('All eight primary calibrated national' in main,'Primary holds absent from conclusion')
 require('independently supported account--asset divergence and conversion associations are not established' in main,'Unsupported association claim')
 for p in files():
  if p.suffix=='.pdf':require(p.name.startswith('integrated_')or 'paper_support'in p.parts,'Unexpected provider PDF in package')
  require(p.suffix not in {'.zip','.dbf','.shp','.tif','.nc','.nc4'},'Raw provider payload included')
 return protected

def run(write=False):
 protected=guards();records=[]
 for p in files():
  b=p.read_bytes();records.append(dict(path=str(p.relative_to(ROOT)),bytes=len(b),sha256=sha(b),git_blob_sha1=gitsha(b)))
 if write:
  (ROOT/MANIFEST).write_text(json.dumps(dict(version='F13_A01',kind='One integrated empirical main/SI, national source analyses, typed uncertainty and inherited identification results',
   files=records,file_count=len(records),manifest_self_excluded=True,post_publication_receipts_excluded=sorted(POST),
   protected_F11_F12_files_unchanged=protected,original_primary_AGB_admissions=0,
   secondary_conditional_volume_comparisons=2,Canadian_published_total_change_interval_unresolved=True,
   new_numerical_outputs_reproduced=13,tests_per_mode=30,no_new_provider_raw_payload_redistributed=True),indent=2)+'\n')
 else:require(records==load(MANIFEST)['files'],'Manifest mismatch or unlisted durable artifact')
 return dict(verified_files=len(records),bytes=sum(r['bytes']for r in records),protected_F11_F12_files=protected,
  tests_per_execution_mode=30,new_numeric_outputs_reproduced=13,preserved_F12_numeric_outputs=50,
  preserved_F12_LP_certificates=634,original_primary_AGB_holds=8,secondary_conditional_volume_comparisons=2,
  main_pages=load('metadata/deliverable_QA_F13.json')['main']['pages'],SI_pages=load('metadata/deliverable_QA_F13.json')['SI']['pages'],
  workbook_sheets=30,one_integrated_publication=True,manifest_written=write)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write-manifest',action='store_true');print(json.dumps(run(p.parse_args().write_manifest),indent=2))
