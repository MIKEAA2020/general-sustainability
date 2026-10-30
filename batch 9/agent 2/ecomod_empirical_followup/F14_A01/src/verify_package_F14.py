#!/usr/bin/env python3
"""Freeze/verify only the additive F14 deposit; no rebuild during verification."""
import argparse,hashlib,json,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MANIFEST='artifact_manifest_F14_A01.json';POST={'PUBLICATION_RECEIPT_F14_A01.json'}
def require(ok,msg):
 if not ok:raise ValueError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def load(n):return json.loads((ROOT/n).read_text())
def files():return sorted(p for p in ROOT.rglob('*')if p.is_file()and not any(v in {'.git','.cache','__pycache__'}for v in p.relative_to(ROOT).parts)and p.name not in POST|{MANIFEST})
def prior(folder):
 p=ROOT.parent/folder
 if not p.exists():p=ROOT.parent/re.search(r'F\d+_A01',folder)[0]
 require(p.is_dir(),'Prior package missing '+folder);return p

def guards():
 n=load('metadata/editorial_reproducibility_F14.json');require(len(n['files'])==9 and n['new_empirical_estimates']is False,'Editorial reproduction scope')
 for name,h in n['files'].items():require(sha((ROOT/name).read_bytes())==h,'Changed reproduced artifact '+name)
 for name,h in n['source_scripts'].items():require(sha((ROOT/'src'/name).read_bytes())==h,'Reproduced source changed '+name)
 for mode in ['normal','optimized']:
  text=(ROOT/f'evidence/tests_{mode}_F14.log').read_text();require(re.search(r'Ran 20 tests in .*\n\nOK\s*$',text)is not None and 'skipped'not in text,'Incomplete tests '+mode)
 q=load('metadata/deliverable_QA_F14.json');require(q['visual_review_completed'],'Visual review incomplete')
 require((q['main_figures'],q['main_tables'],q['main_result_sections'],q['SI_figures'],q['SI_tables'])==(6,2,5,2,17),'Editorial allocation drift')
 for kind in ['main','SI']:
  r=q[kind];require(sha((ROOT/r['file']).read_bytes())==r['sha256'],'PDF changed after QA');require(not r['text_outside_page_bounds']and r['all_fonts_embedded']and r['ORCID_hyperlink'],'PDF QA failed');require(q['visual_review_pages'][kind]==list(range(1,r['pages']+1)),'Not every page reviewed')
 require(q['main']['AI_declaration']and q['keywords']==7 and q['abstract_whitespace_words']<=250,'Declaration/keywords/abstract')
 w=q['workbook'];require(w['sheets']==31 and w['inherited_sheets_unchanged']==30 and w['inherited_cells_checked']==60314,'Workbook inheritance QA')
 require(sha((ROOT/w['file']).read_bytes())==w['sha256'],'Workbook changed after QA')
 links=load('metadata/SI_linkage_F14.json');require(len(links['labels'])==19 and set(links['labels'])==set(links['main_citations'])and not links['uncited_SI_items']and not links['unknown_main_references'],'Unlinked SI')
 protected=0
 for pkg in load('metadata/protected_prior_identity_F14.json'):
  p=prior(pkg['folder'])
  for r in pkg['files']:require(sha((p/r['path']).read_bytes())==r['sha256'],'Protected file changed '+r['path']);protected+=1
 require(protected==537,'Protected count drift')
 for r in load('metadata/input_lineage_F14.json'):require(sha((ROOT/r['vendored_path']).read_bytes())==r['sha256']and r['byte_identical'],'Copied input changed')
 f13=prior('ecomod_empirical_integration_F13_A01');status=subprocess.run([sys.executable,str(f13/'src/verify_package_F13.py')],check=True,capture_output=True,text=True)
 inherited=json.loads(status.stdout);require(inherited['new_numeric_outputs_reproduced']==13 and inherited['preserved_F12_LP_certificates']==634,'Prior numerical evidence not preserved')
 main=(ROOT/'integrated_F14_A01_main.tex').read_text()
 require('Completion is distinct from sign resolution'in main and 'None of the eight calibrated national 2015--2023 forest-AGB analyses is complete'in main,'Primary scope changed')
 for name in ['README_F14_A01.md','REVISION_AND_MIGRATION_ACCOUNT_F14_A01.md','requirements_F14_A01.txt']:require((ROOT/name).is_file(),'Disclosure missing '+name)
 for p in files():require(p.suffix not in {'.zip','.dbf','.shp','.tif','.nc','.nc4'},'Raw provider payload included')
 return protected

def run(write=False):
 protected=guards();rows=[]
 for p in files():
  b=p.read_bytes();rows.append(dict(path=str(p.relative_to(ROOT)),bytes=len(b),sha256=sha(b),git_blob_sha1=gitsha(b)))
 if write:(ROOT/MANIFEST).write_text(json.dumps(dict(version='F14_A01',kind='Content-based main/SI editorial integration; no new empirical estimates',files=rows,file_count=len(rows),manifest_self_excluded=True,post_publication_receipts_excluded=sorted(POST),protected_F11_F12_F13_files_unchanged=protected,original_primary_AGB_analyses_incomplete=8),indent=2)+'\n')
 else:require(rows==load(MANIFEST)['files'],'Manifest mismatch/unlisted durable file')
 return dict(verified_files=len(rows),bytes=sum(r['bytes']for r in rows),protected_F11_F12_F13_files=protected,tests_per_execution_mode=20,editorial_artifacts_reproduced=9,new_empirical_estimates=False,original_primary_AGB_analyses_incomplete=8,main_pages=15,SI_pages=22,main_figures=6,main_tables=2,SI_figures=2,SI_tables=17,all_SI_items_cited=True,workbook_sheets=31,one_integrated_publication=True,manifest_written=write)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write-manifest',action='store_true');print(json.dumps(run(p.parse_args().write_manifest),indent=2))
