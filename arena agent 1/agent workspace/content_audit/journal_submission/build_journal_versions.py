#!/usr/bin/env python3
"""Compile new journal-facing heads with real local figures (no substitutions)."""
from pathlib import Path
from collections import defaultdict
import re,subprocess,shutil,json,hashlib
R=Path('/home/user');A=R/'content_audit/journal_submission';W=Path('/tmp/journal_compiles');W.mkdir(exist_ok=True)
files={
'papers':['paper01_obstruction_calculus_v65.tex','paper01_obstruction_calculus_v65_supplementary.tex','paper02_probabilistic_sufficiency_v14.tex','paper03_computational_certification_v18.tex','paper03_computational_certification_v18_supplementary.tex','paper04_minimax_dual_certificates_v18.tex','paper05_exact_belief_computation_v18.tex','paper06_assessment_separation_v69.tex','paper07_sampled_governance_v52.tex','paper08_governance_delay_v48.tex','paper09_cod_certification_v34.tex','paper09b_arv_certification_v4.tex','paper11_forecasting_baselines_v66.tex','paper11c_worked_systems_audit_v4.tex'],
'paper 2 family/01_obstruction':['paper01_obstruction_calculus_v65.tex','paper01_obstruction_calculus_v65_supplementary.tex'],
'paper 2 family/02_probabilistic_sufficiency':['paper02_probabilistic_sufficiency_v14.tex'],
'paper 2 family/03_computational_certification':['paper03_computational_certification_v18.tex','paper03_computational_certification_v18_supplementary.tex'],
'paper 2 family/04_minimax_dual_certificates':['paper04_minimax_dual_certificates_v18.tex'],
'paper 2 family/05_exact_belief_computation':['paper05_exact_belief_computation_v18.tex'],
'paper 2 family/09_cod_with_arv':['paper09_cod_certification_v34.tex','paper09b_arv_certification_v4.tex'],
'paper 2 family/11_forecasting_baselines':['paper11_forecasting_baselines_v66.tex'],
'paper 2 family/11c_worked_systems':['paper11c_worked_systems_audit_v4.tex']}
idx=defaultdict(list)
for p in R.rglob('*'):
 if p.is_file() and p.suffix.lower() in ('.png','.jpg','.jpeg','.pdf') and not any(q in p.parts for q in ['.git','node_modules']):idx[p.name].append(p)
results=[]
for directory,names in files.items():
 for name in names:
  src=R/directory/name;txt=src.read_text();key=directory.replace(' ','_').replace('/','__')+'__'+src.stem;work=W/key;work.mkdir(exist_ok=True)
  (work/name).write_text(txt)
  refs=set(re.findall(r'\\includegraphics\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}',txt));figs=[];missing=[]
  for rel in sorted(refs):
   base=Path(rel).name;choices=idx.get(base,[])
   # Priority: exact same directory; then staged/local producer assets. No generated placeholders.
   choices.sort(key=lambda p:(p.parent!=src.parent/Path(rel).parent,not str(p).startswith(str(R/'paper 2 family')),len(str(p))))
   if not choices:missing.append(rel);continue
   dest=work/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(choices[0],dest)
   figs.append({'ref':rel,'local_source':str(choices[0].relative_to(R)),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
  if missing:
   results.append({'path':str(src.relative_to(R)),'status':'MISSING_REAL_FIGURE','names':missing});print('FAIL',src.name,missing,flush=True);continue
  p=subprocess.run(['/tmp/tectonic','-X','compile',name,'--outdir','.'],cwd=work,capture_output=True,text=True,timeout=240)
  log=p.stdout+'\n'+p.stderr;(A/'compile_logs').mkdir(exist_ok=True);(A/'compile_logs'/(key+'.log')).write_text(log)
  pdf=work/src.with_suffix('.pdf').name;undefined=len(re.findall('undefined reference',log,re.I))
  status='COMPILED' if p.returncode==0 and pdf.exists() and not undefined else 'FAILED'
  if status=='COMPILED':shutil.copy2(pdf,src.with_suffix('.pdf'))
  results.append({'path':str(src.relative_to(R)),'status':status,'figures':figs,'undefined_reference_warnings':undefined,'tail':log[-700:]})
  print(status,src.relative_to(R),'figs',len(figs),'undefined',undefined,flush=True)
(A/'COMPILE_RESULTS.json').write_text(json.dumps(results,indent=2))
assert all(x['status']=='COMPILED' for x in results),[x['path'] for x in results if x['status']!='COMPILED']
