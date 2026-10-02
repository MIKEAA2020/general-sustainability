#!/usr/bin/env python3
"""Compile versioned sources in isolated scratch with real local figures; record failures and caveats."""
from pathlib import Path
from collections import defaultdict
import re, json, shutil, subprocess, hashlib
R=Path('/home/user');P=R/'papers';A=R/'content_audit/editorial_revisions';W=Path('/tmp/editorial_version_compile');W.mkdir(exist_ok=True)
files=['paper01_obstruction_calculus_v64.tex','paper01_obstruction_calculus_v64_supplementary.tex','paper02_probabilistic_sufficiency_v13.tex','paper03_computational_certification_v17.tex','paper03_computational_certification_v17_supplementary.tex','paper04_minimax_dual_certificates_v17.tex','paper05_exact_belief_computation_v17.tex','paper06_assessment_separation_v68.tex','paper07_sampled_governance_v51.tex','paper08_governance_delay_v47.tex','paper09_cod_certification_v33.tex','paper09b_arv_certification_v3.tex','paper11_forecasting_baselines_v65.tex','paper11c_worked_systems_audit_v3.tex']
# Indexed local producer images. Never write fake figures into a successful compiled manuscript.
idx=defaultdict(list)
for p in R.rglob('*'):
 if p.is_file() and p.suffix.lower() in ('.png','.jpg','.jpeg','.pdf','.eps') and not any(q in p.parts for q in ['.git','node_modules','Unselected files']):idx[p.name].append(p)
results=[]
for f in files:
 src=P/f;t=src.read_text();work=W/f.removesuffix('.tex');work.mkdir(exist_ok=True)
 (work/f).write_text(t)
 refs=set(re.findall(r'\\includegraphics\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}',t));missing=[];figs=[]
 for rel in refs:
  name=Path(rel).name;matches=idx.get(name,[])
  # prefer corresponding staged package image if available
  matches.sort(key=lambda p:(not str(p).startswith(str(R/'paper 2 family')),len(str(p))))
  if not matches:missing.append(rel);continue
  dest=work/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(matches[0],dest)
  figs.append((rel,str(matches[0].relative_to(R)),hashlib.sha256(dest.read_bytes()).hexdigest()))
 if missing:
  results.append({'file':f,'status':'missing real figures','missing':missing,'real_figures':figs});print(f,'MISSING',missing,flush=True);continue
 try:
  p=subprocess.run(['/tmp/tectonic','-X','compile',f,'--outdir','.'],cwd=work,text=True,capture_output=True,timeout=300)
  log=p.stdout+'\n'+p.stderr;(A/(f+'.compile.log')).write_text(log)
  pdf=work/f.replace('.tex','.pdf')
  status='compiled' if p.returncode==0 and pdf.exists() else 'failed'
  result={'file':f,'status':status,'returncode':p.returncode,'real_figures':figs,'undefined_references':len(re.findall('undefined reference',log,re.I)),'warnings':len(re.findall(r'^warning:',log,re.M)),'tail':log[-1000:]}
  if status=='compiled':
   # New version-specific PDF, not a modified old version. Included figures are unmodified real local files.
   shutil.copy2(pdf,src.with_suffix('.pdf'))
  results.append(result)
  print(f,status,'figs',len(figs),'undefined',result['undefined_references'],flush=True)
 except subprocess.TimeoutExpired:
  results.append({'file':f,'status':'timeout','real_figures':figs});print(f,'TIMEOUT',flush=True)
(A/'COMPILE_RESULTS.json').write_text(json.dumps(results,indent=2))
