#!/usr/bin/env python3
"""Run source-year paper09 E2/E4 core runners in a fresh sparse Git checkout.
Execute only against SHA-verified archived inputs; never overwrite workspace
sources/figures. Separate output mismatch from a failed run. Not a full proof.
"""
from pathlib import Path
import csv,hashlib,json,platform,subprocess,sys
R=Path('/home/user');O=R/'content_audit/paper09_rerun';G=Path('/tmp/paper09-fresh-repo')
assert G.is_dir() and (G/'.git').exists()
HEAD=subprocess.check_output(['git','rev-parse','HEAD'],cwd=G,text=True).strip()
assert HEAD=='180b5aa082005701f127c62f19d3a8865067eabc',HEAD
assert not subprocess.check_output(['git','status','--porcelain'],cwd=G,text=True).strip()
import numpy,pandas,scipy,matplotlib
(O/'environment.json').write_text(json.dumps({'clone_commit':HEAD,'python':platform.python_version(),'numpy':numpy.__version__,'pandas':pandas.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__,'platform':platform.platform()},indent=2)+'\n')
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def repo_blob(f):
 data=f.read_bytes();d=subprocess.check_output(['git','hash-object','--stdin'],cwd=G,input=data).decode().strip();want=subprocess.check_output(['git','rev-parse','HEAD:'+str(f.relative_to(G))],cwd=G,text=True).strip();assert d==want,f
 return want
# This overincludes archived data files rather than relying on a brittle static list.
inputs=[]
for sub in ('wave_e_cod','wave_e_edwards'):
 for path in sorted((G/sub/'data').rglob('*')):
  if path.is_file():inputs.append((path,repo_blob(path)))
for relative in ('wave_e_cod/src/run_ladder.py','wave_e_cod/src/run_intervention_v3.py','wave_e_cod/src/campaign_e2_elevation_v3.py','wave_e_edwards/src/run_intervention_v2.py','wave_e_edwards/src/e4_audit_layer.py','wave_e_cod/results/intervention_results_v3.json','wave_e_cod/results/intervention_boundaries_v3.csv','wave_e_edwards/results/intervention_results_v2.json','wave_e_edwards/results/intervention_boundaries_v2.csv'):
 path=G/relative;inputs.append((path,repo_blob(path)))
with (O/'fresh_inputs.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['repo_path','git_blob_sha1','sha256','bytes']);
 for p,b in inputs:w.writerow([str(p.relative_to(G)),b,sha(p),p.stat().st_size])
print('VERIFIED_INPUTS',len(inputs),'Git blob SHA1 and SHA256',flush=True)
commands=[('cod_core','wave_e_cod/src/run_intervention_v3.py',['wave_e_cod/results/intervention_results_v3.json','wave_e_cod/results/intervention_boundaries_v3.csv'],300),('edwards_core','wave_e_edwards/src/run_intervention_v2.py',['wave_e_edwards/results/intervention_results_v2.json','wave_e_edwards/results/intervention_boundaries_v2.csv'],300),('edwards_audit','wave_e_edwards/src/e4_audit_layer.py',['wave_e_edwards/results/e4_audit_layer.json'],400),('cod_campaign','wave_e_cod/src/campaign_e2_elevation_v3.py',['wave_e_cod/src/results_srcyear_v3/'+n for n in ['e2_elevation_residuals.csv','e2_elevation_k_grid.csv','e2_elevation_stochastic.csv','e2_elevation_stochastic_constructive.csv','e2_elevation_finite_floors.csv','e2_elevation_bootstrap.csv']],800)]
results=[]
for key,script,outputs,timeout in commands:
 src=G/script;repo_blob(src)
 before={name:sha(G/name) if (G/name).exists() else None for name in outputs}
 try:
  done=subprocess.run([sys.executable,str(src)],cwd=G,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=timeout)
  log=done.stdout;rc=done.returncode
 except subprocess.TimeoutExpired as e:
  log=(e.stdout or b'').decode(errors='replace') if isinstance(e.stdout,bytes) else (e.stdout or '');rc=124
 (O/(key+'.log')).write_text(log)
 for name in outputs:
  path=G/name;after=sha(path) if path.exists() else None
  status='byte-match' if before[name]==after and after is not None else 'mismatch' if after else 'missing'
  results.append((key,script,name,rc,before[name],after,status))
  print(key,'rc',rc,name,status,flush=True)
 if rc!=0:print('runner error',key,log[-800:],flush=True)
with (O/'core_outputs.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['runner','source','output','exit_code','committed_sha256','rerun_sha256','comparison']);w.writerows(results)
print('CORE_SUMMARY',len(results),'output rows;',sum(x[-1]=='byte-match' for x in results),'exact matches;',sum(x[3]!=0 for x in results),'nonzero-output rows',flush=True)
