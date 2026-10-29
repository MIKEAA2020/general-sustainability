from pathlib import Path
import json,hashlib,re,sys,subprocess,shutil,platform,importlib.metadata,csv,difflib
from pypdf import PdfReader
P=Path('/home/user/ecomod_followup_F08');old=Path('/home/user/ecomod_followup_F07');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
prior=[]
for name in ['ecomod_empirical_followup','ecomod_followup_F02','ecomod_followup_F03','ecomod_followup_F04','ecomod_followup_F05','ecomod_followup_F06','ecomod_followup_F07','ecomod_c13_revision','ecomod_c14','ecomod_c15','ecomod_c16','ecomod_c17']:
 d=P.parent/name;m=json.loads((d/'artifact_manifest.json').read_text());files=m['files']
 if isinstance(files,dict):files=[{'path':k,'sha256':v['sha256']if isinstance(v,dict)else v}for k,v in files.items()]
 for x in files:assert H(d/x['path'])==x['sha256'],(name,x['path'])
 prior.append({'package':name,'unchanged_manifest_listed_files':len(files),'manifest_sha256':H(d/'artifact_manifest.json')})
allowed={'README.md','REMAINING_EMPIRICAL_WORK.md','configs/study_design.json','metadata/SOURCE_USE.md','metadata/design_input_provenance.json','protocol/STUDY_PROTOCOL.md','src/build.sh','metadata/document_qa.json','metadata/computational_verification.json'}|{f'followup_F07_{n}.{e}'for n in ['main','SI']for e in ['tex','pdf']}
protected={}
for x in json.loads((old/'artifact_manifest.json').read_text())['files']:
 if x['path']not in allowed:assert H(P/x['path'])==x['sha256'],x['path'];protected[x['path']]=x['sha256']
assert (P/'protocol/archive/PROTOCOL_F07.md').read_bytes()==(old/'protocol/STUDY_PROTOCOL.md').read_bytes()
for name in ['document_qa','computational_verification']:assert(P/f'metadata/F07_{name}.json').read_bytes()==(old/f'metadata/{name}.json').read_bytes()
a=(old/'followup_F07_main.tex').read_text();b=(P/'followup_F08_main.tex').read_text();q=lambda t:re.search(r'\\begin\{enumerate\}(.*?)\\end\{enumerate\}',t,re.S).group(1);assert q(a)==q(b)
expected=r'\href{http://Arena.ai}{Arena.ai} Agent Mode was used to assist with computational methods and literature review.'
ai=lambda t:re.search(r'\\section\*\{Declaration of generative AI in scientific writing\}(.*?)\\begin\{thebibliography\}',t,re.S).group(1).strip();assert ai(b)==expected;assert ai(a)!=ai(b)
for n in ['main','SI']:
 x=(old/f'followup_F07_{n}.tex').read_text();y=(P/f'followup_F08_{n}.tex').read_text()
 for eq in re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}',x,re.S):assert eq in y
 for eq in re.findall(r'\\\[(.*?)\\\]',x,re.S):assert eq in y
 diff=''.join(difflib.unified_diff(x.splitlines(True),y.splitlines(True),fromfile=f'F07/{n}',tofile=f'F08/{n}'));assert(P/f'metadata/source_comparisons/F07_to_F08_{n}.diff').read_text()==diff
 assert r'\href{https://orcid.org/0000-0002-0019-1842}{0000-0002-0019-1842}'in y
for meta,items in [('metadata/reference/xlsx_retry_freeze_F08.json',[('protocol_sha256','protocol/XLSX_RETRY_F08.md'),('configuration_sha256','configs/xlsx_retry_F08.json')]),('metadata/allocation/freeze_F07.json',[('protocol_sha256','protocol/ALLOCATION_ENVELOPE_F07.md'),('configuration_sha256','configs/allocation_F07.json')])]:
 f=json.loads((P/meta).read_text())
 for k,name in items:assert H(P/name)==f[k]
assert H(P/'protocol/STUDY_PROTOCOL.md')==json.loads((P/'metadata/design_input_provenance.json').read_text())['active_protocol']['sha256']
logs={}
for label,args,count in [('all',[sys.executable,'-m','unittest','discover','-s',str(P/'tests'),'-v'],104),('optimized_F08',[sys.executable,'-O','-m','unittest','discover','-s',str(P/'tests'),'-p','test_xlsx_f08.py','-v'],20)]:
 r=subprocess.run(args,capture_output=True,text=True);text=r.stdout+r.stderr;assert r.returncode==0,text;assert int(re.search(r'Ran (\d+) tests',text).group(1))==count;(P/f'metadata/tests_F08_{label}.txt').write_text(text.replace(str(P),'.'));logs[label]=count
checks=[];words=json.loads((P/'configs/study_design.json').read_text())['keywords']
for n in ['main','SI']:
 log=(P/f'.cache/tex/followup_F08_{n}.log').read_text();bad=[x for x in log.splitlines()if any(z in x for z in ['Overfull','Underfull','LaTeX Warning','Package hyperref Warning','Package natbib Warning','!'])];assert not bad,bad
 d=PdfReader(P/f'followup_F08_{n}.pdf');text='\n'.join(p.extract_text()for p in d.pages);assert all(len(p.extract_text())>100 for p in d.pages);assert '??'not in text;assert d.metadata['/Keywords']=='; '.join(words);assert d.metadata['/Title'];assert d.metadata['/Author']=='Amin Abaee'
 uris=[str(a.get_object().get('/A',{}).get('/URI',''))for page in d.pages for a in page.get('/Annots',[])];assert 'https://orcid.org/0000-0002-0019-1842'in uris
 if n=='main':assert 'http://Arena.ai'in uris;assert 'Arena.ai Agent Mode was used to assist with computational methods and literature review.'in ' '.join(text.split());assert all(w in ' '.join(text.split())for w in words)
 checks.append({'file':f'followup_F08_{n}.pdf','pages':len(d.pages),'sha256':H(P/f'followup_F08_{n}.pdf'),'final_build_warnings':bad,'no_empty_pages_or_unresolved_references':True,'ORCID_clickable_URI_verified':True,'seven_PDF_keywords_verified':True,'PDF_title_and_author_metadata_verified':True})
assert[x['pages']for x in checks]==[10,9]
rows=list(csv.DictReader((P/'data/support/physical_admission_F08.csv').open()));assert len(rows)==8 and all(x['admission']=='hold_not_admitted'and x['permanent_exclusion']=='False'for x in rows);assert rows==list(csv.DictReader((old/'data/support/physical_admission_F07.csv').open()))
reproduction=json.loads((P/'metadata/reference/xlsx_reproduction_F08.json').read_text());assert reproduction['network_disabled']and reproduction['audit_and_member_hashes_byte_identical']
for name,sha in reproduction['files'].items():assert H(P/name)==sha
qa={'revision':'F08','date':'2026-10-29','documents':checks,'visual_review':'Reviewed all 19 pages in contact sheets plus detailed main first page, declaration page and SI reference table/results page. No clipping/overlap found in reviewed renders; the corrected Figure 1 remains unchanged. Scoped document checks, not scientific validation.','research_questions_and_inherited_math_unchanged':True,'AI_declaration_author_approved_replacement':True,'AI_declaration_exact_sentence_and_URI_verified':True,'ECOMOD_C17_unchanged':True,'Figure1_corrected_input_byte_identical_to_F07':True,'implementation_logs_outside_articles':True};(P/'metadata/document_qa.json').write_text(json.dumps(qa,indent=2)+'\n')
verification={'revision':'F08','date':'2026-10-29','unit_tests_passed':104,'new_F08_tests':20,'new_F08_tests_also_pass_with_python_optimization':True,'complete_XLSX_cached_reproduction':reproduction,'F07_scientific_outputs_hash_verified_unchanged':protected,'frozen_F05_F06_F07_rules_unchanged':True,'frozen_F08_workbook_only_exception_verified':True,'prior_packages':prior,'F07_protocol_and_QA_archives_exact':True,'research_questions_and_inherited_math_unchanged':True,'author_approved_AI_declaration_replacement':True,'ORCID_copied_from_unchanged_C17':True,'original_estimand_kernel_unchanged':True,'account_tables_and_corrected_Figure1_unchanged':True,'all_8_national_admissions_hold':True,'XLSX_is_not_independent_validation':True,'scientific_validation_or_uncertainty_calibration':False,'python':platform.python_version(),'tested_package_versions':{x:importlib.metadata.version(x)for x in ['numpy','scipy','tifffile','imagecodecs','requests','matplotlib','pypdf','netCDF4','shapely','pyproj','pyshp','openpyxl']}};(P/'metadata/computational_verification.json').write_text(json.dumps(verification,indent=2)+'\n')
for p in sorted(P.rglob('__pycache__'),reverse=True):shutil.rmtree(p)
shutil.rmtree(P/'.cache')
files=[{'path':str(p.relative_to(P)),'bytes':p.stat().st_size,'sha256':H(p)}for p in sorted(P.rglob('*'))if p.is_file()and p.name!='artifact_manifest.json']
assert all(not x['path'].endswith(('.bin','.ascii','.zip','.xlsx'))for x in files)
token=re.search(r'github_pat_[A-Za-z0-9_]+',Path('/home/user/uploads/github_pat.txt').read_text()).group().encode()
for x in files:assert token not in(P/x['path']).read_bytes()
(P/'artifact_manifest.json').write_text(json.dumps({'package':'ecomod_followup_F08','date':'2026-10-29','files':files},indent=2)+'\n');print('Finalized F08:',len(files)+1,'files; 104 tests + 20 optimized; PDFs 10/9 pages; 12 prior packages immutable; complete workbook offline reparse byte-identical.',flush=True)
