#!/usr/bin/env python3
"""Actions-portable paper09 source-year core/xte replay.
Reruns eleven archived core output files and the independently repaired
xte second-specification row; asserts source/inputs and staged text match.
The slower supplemental campaigns are documented in RERUN_REPORT, not
implicitly claimed by this shorter hosted job.
"""
from pathlib import Path
import csv,hashlib,json,os,platform,subprocess,sys,tempfile
B=Path(__file__).resolve().parent
WORK=Path(os.environ.get('PAPER09_WORKSPACE',B.parents[1]))
G=Path(os.environ.get('PAPER09_REPO',WORK.parents[1]))
assert WORK.name=='agent workspace' or 'PAPER09_WORKSPACE' in os.environ,WORK
assert (G/'.git').exists(),G
OUT=B/'ci_out';OUT.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=G,text=True).strip()
print('SOURCE_COMMIT',head,flush=True)
for item in csv.DictReader((B/'fresh_inputs.tsv').open(),delimiter='\t'):
 p=G/item['repo_path'];assert p.is_file() and sha(p)==item['sha256'],('input SHA mismatch',p)
 print('INPUT_OK',item['repo_path'],item['sha256'],flush=True)
for mod in ('numpy','pandas','scipy','matplotlib'):
 x=__import__(mod);print('ENV',mod,x.__version__,flush=True)
print('ENV Python',platform.python_version(),flush=True)
arch=list(csv.DictReader((B/'core_outputs.tsv').open(),delimiter='\t'))
by={r['output']:r['committed_sha256'] for r in arch};assert len(by)==11
jobs=[('cod_core','wave_e_cod/src/run_intervention_v3.py',300),('edwards_core','wave_e_edwards/src/run_intervention_v2.py',300),('edwards_audit','wave_e_edwards/src/e4_audit_layer.py',400),('cod_campaign','wave_e_cod/src/campaign_e2_elevation_v3.py',800)]
for name,source,timeout in jobs:
 selected=[r for r in arch if r['runner']==name];assert selected
 for r in selected:assert sha(G/r['output'])==r['committed_sha256'],('checkout drift',r['output'])
 proc=subprocess.run([sys.executable,str(G/source)],cwd=G,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=timeout)
 (OUT/(name+'.log')).write_text(proc.stdout)
 assert proc.returncode==0,(name,proc.returncode,proc.stdout[-500:])
 for r in selected:
  actual=sha(G/r['output']);assert actual==r['committed_sha256'],(name,r['output'],actual,r['committed_sha256'])
  print('OUTPUT_MATCH',r['output'],actual,flush=True)
# Run reviewed one-line correction in isolated temporary path, never replace
# the historical tracked xte script or its old result files.
src=(B/'review_candidates/campaign_e2_xteNCAM_row_sourceyear.py').read_text()
old='REPO = Path("/home/user/repo")';assert src.count(old)==1
with tempfile.TemporaryDirectory(prefix='xte-sourceyear-ci-') as d:
 p=Path(d)/'campaign_e2_xteNCAM_row.py';p.write_text(src.replace(old,'REPO = Path('+repr(str(G))+')'))
 proc=subprocess.run([sys.executable,str(p)],cwd=G,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=600)
 (OUT/'xte_sourceyear.log').write_text(proc.stdout)
 assert proc.returncode==0,(proc.returncode,proc.stdout[-500:])
 for n in ('e2_xteNCAM_summary.csv','e2_xteNCAM_row.csv'):
  generated=Path(d)/'results'/n;expected=B/'review_candidates'/n
  assert generated.is_file() and sha(generated)==sha(expected),(n,'source-year candidate output drift')
  print('XTE_OUTPUT_MATCH',n,sha(generated),flush=True)
# The checker reads the packaged source too, so a later manuscript edit cannot
# silently invalidate the numeric conclusion while the archived output stays.
cmd=[sys.executable,str(B/'check_xte_sourceyear.py')]
env=dict(os.environ,PAPER09_AUDIT_DIR=str(B),PAPER09_MAIN_TEX=str(WORK/'paper 2 family/09_cod_with_arv/paper09_cod_certification_v32.tex'))
proc=subprocess.run(cmd,cwd=G,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=30)
(OUT/'xte_claim_crosswalk.log').write_text(proc.stdout)
assert proc.returncode==0,(proc.returncode,proc.stdout)
print(proc.stdout.strip(),flush=True)
(OUT/'summary.json').write_text(json.dumps({'source_commit':head,'core_output_matches':11,'xte_output_matches':2,'xte_claim_checks':15,'scope':'core source-year and repaired xte only; see full local campaign report'},indent=2)+'\n')
print('CI_PAPER09_CORE_XTE_PASS 11 archived core outputs, 2 source-year xte candidate outputs, 15 scoped manuscript comparisons',flush=True)
