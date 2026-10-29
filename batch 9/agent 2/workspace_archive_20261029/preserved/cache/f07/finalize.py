from pathlib import Path
import json,hashlib,re,sys,subprocess,shutil,platform,importlib.metadata
from pypdf import PdfReader
P=Path('/home/user/ecomod_followup_F07');old=Path('/home/user/ecomod_followup_F06');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
prior=[]
for name in ['ecomod_empirical_followup','ecomod_followup_F02','ecomod_followup_F03','ecomod_followup_F04','ecomod_followup_F05','ecomod_followup_F06','ecomod_c13_revision','ecomod_c14','ecomod_c15','ecomod_c16','ecomod_c17']:
 d=Path('/home/user')/name;m=json.loads((d/'artifact_manifest.json').read_text());files=m['files']
 if isinstance(files,dict):files=[{'path':k,'sha256':v['sha256']if isinstance(v,dict)else v}for k,v in files.items()]
 for x in files:assert H(d/x['path'])==x['sha256'],(name,x['path'])
 prior.append({'package':name,'unchanged_manifest_listed_files':len(files),'manifest_sha256':H(d/'artifact_manifest.json')})
for x in ['src/estimands.py','data/derived/account_availability.csv','data/derived/country_availability.csv','results/account_coverage_F06.pdf','results/account_coverage_F06.png','results/brazil/BRA_F05_support_fractions.pdf','data/brazil/BRA_F05_support_fractions.npz','data/reference/reference_audit_F06.json']:
 assert (P/x).read_bytes()==(old/x).read_bytes(),x
assert (P/'protocol/archive/PROTOCOL_F06.md').read_bytes()==(old/'protocol/STUDY_PROTOCOL.md').read_bytes()
freeze=json.loads((P/'metadata/allocation/freeze_F07.json').read_text())
for k,x in [('protocol_sha256','protocol/ALLOCATION_ENVELOPE_F07.md'),('configuration_sha256','configs/allocation_F07.json')]:assert H(P/x)==freeze[k]
for x,sha in json.loads((P/'metadata/allocation/input_hashes_F07.json').read_text()).items():assert H(P/x)==sha
for name in ['protocol/BRAZIL_SUPPORT_F05.md','configs/brazil_support_F05.json','metadata/brazil/support_freeze_F05.json','protocol/REFERENCE_AUDIT_F06.md','metadata/reference/audit_freeze_F06.json']:
 assert (P/name).read_bytes()==(old/name).read_bytes()
a=(old/'followup_F06_main.tex').read_text();b=(P/'followup_F07_main.tex').read_text();q=lambda t:re.search(r'\\begin\{enumerate\}(.*?)\\end\{enumerate\}',t,re.S).group(1);assert q(a)==q(b)
ai=lambda t:re.search(r'\\section\*\{Declaration of generative AI in scientific writing\}(.*?)\\begin\{thebibliography\}',t,re.S).group(1);assert ai(a)==ai(b)
for n in ['main','SI']:
 x=(old/f'followup_F06_{n}.tex').read_text();y=(P/f'followup_F07_{n}.tex').read_text()
 for eq in re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}',x,re.S):assert eq in y
 for eq in re.findall(r'\\\[(.*?)\\\]',x,re.S):assert eq in y
r=subprocess.run([sys.executable,'-m','unittest','discover','-s',str(P/'tests'),'-v'],capture_output=True,text=True);assert r.returncode==0;rlog=r.stdout+r.stderr;count=int(re.search(r'Ran (\d+) tests',rlog).group(1));assert count==84;(P/'metadata/tests_F07.txt').write_text(rlog.replace(str(P),'.'))
checks=[]
for n in ['main','SI']:
 log=(P/f'.cache/tex/followup_F07_{n}.log').read_text();bad=[x for x in log.splitlines()if any(z in x for z in ['Overfull','Underfull','LaTeX Warning','Package natbib Warning','!'])];assert not bad,bad
 d=PdfReader(P/f'followup_F07_{n}.pdf');text='\n'.join(p.extract_text()for p in d.pages);assert all(len(p.extract_text())>100 for p in d.pages);assert '??'not in text
 checks.append({'file':f'followup_F07_{n}.pdf','pages':len(d.pages),'sha256':H(P/f'followup_F07_{n}.pdf'),'final_build_warnings':bad,'no_empty_pages_or_unresolved_references':True})
assert [x['pages']for x in checks]==[10,9]
rows=list(__import__('csv').DictReader((P/'data/support/physical_admission_F07.csv').open()));assert len(rows)==8 and all(x['admission']=='hold_not_admitted'and x['permanent_exclusion']=='False'for x in rows)
qa={'revision':'F07','date':'2026-10-29','documents':checks,'visual_review':'All-page contact sheets, detailed allocation table and S10 proof/topology pages; final table math signs and SI pp8–9 rechecked. Corrected Figure 1 unchanged and remains visibly separated. No clipping/overlap found in reviewed renders. Scoped technical/visual checks, not ecological validation.','research_questions_and_author_AI_declaration_unchanged':True,'inherited_math_retained':True,'Figure1_corrected_input_byte_identical_to_F06':True,'implementation_logs_outside_articles':True};(P/'metadata/document_qa.json').write_text(json.dumps(qa,indent=2)+'\n')
verification={'revision':'F07','date':'2026-10-29','unit_tests_passed':84,'new_allocation_tests':20,'new_allocation_tests_also_pass_with_python_optimization':True,'cached_reproduction':json.loads((P/'metadata/allocation/reproduction_F07.json').read_text()),'frozen_F05_F06_F07_rules_verified':True,'prior_packages':prior,'F06_protocol_archive_exact':True,'research_questions_AI_declaration_and_inherited_math_unchanged':True,'original_estimand_kernel_unchanged':True,'account_tables_and_corrected_Figure1_unchanged':True,'all_8_national_admissions_hold':True,'conditional_local_mass_sets_computed':True,'scientific_validation_or_uncertainty_calibration':False,'python':platform.python_version(),'tested_package_versions':{x:importlib.metadata.version(x)for x in ['numpy','scipy','tifffile','imagecodecs','requests','matplotlib','pypdf','netCDF4','shapely','pyproj','pyshp']}};(P/'metadata/computational_verification.json').write_text(json.dumps(verification,indent=2)+'\n')
for p in sorted(P.rglob('__pycache__'),reverse=True):shutil.rmtree(p)
shutil.rmtree(P/'.cache')
files=[{'path':str(p.relative_to(P)),'bytes':p.stat().st_size,'sha256':H(p)}for p in sorted(P.rglob('*'))if p.is_file()and p.name!='artifact_manifest.json']
assert all(not x['path'].endswith(('.bin','.ascii','.zip','.xlsx'))for x in files)
token=re.search(r'github_pat_[A-Za-z0-9_]+',Path('/home/user/uploads/github_pat.txt').read_text()).group().encode()
for x in files:assert token not in(P/x['path']).read_bytes()
(P/'artifact_manifest.json').write_text(json.dumps({'package':'ecomod_followup_F07','date':'2026-10-29','files':files},indent=2)+'\n');print('Finalized F07:',len(files)+1,'files; 84 tests; PDFs 10/9 pages; prior packages verified immutable.')
