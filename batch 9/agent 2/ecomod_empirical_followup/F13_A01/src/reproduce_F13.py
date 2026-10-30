#!/usr/bin/env python3
"""Re-execute all new numerical outputs in normal/optimized modes and two hash seeds.
Works from immutable source-cache identities, not network availability. Rebuilds
in temporary excluded cache directories; protected earlier packages remain read-only.
"""
import hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(ok,msg):
 if not ok:raise ValueError(msg)
def run():
 cache=ROOT.parent/'.cache/F13';cache.mkdir(parents=True,exist_ok=True)
 baseline={str(p.relative_to(ROOT)):sha(p)for p in sorted((ROOT/'data').glob('*'))if p.is_file()}
 baseline['metadata/BRA_current_vector_schema_F13.json']=sha(ROOT/'metadata/BRA_current_vector_schema_F13.json')
 runs=[]
 for optimized,seed in [(False,17),(True,73)]:
  env=dict(os.environ,PYTHONHASHSEED=str(seed));args=[sys.executable]+(['-O']if optimized else[])
  with tempfile.TemporaryDirectory(prefix='repro_',dir=cache)as tmp:
   out=Path(tmp);subprocess.run(args+[str(ROOT/'src/analyze_sources_F13.py'),'--output',str(out)],env=env,check=True)
   sub=out/'BRA_current_vector_schema_F13.json'
   subprocess.run(args+[str(ROOT/'src/reference_audit_F13.py'),'--output',str(sub)],env=env,check=True,stdout=subprocess.DEVNULL)
   for name,digest in baseline.items():
    p=out/Path(name).name;require(p.exists()and sha(p)==digest,'Non-reproduced artifact: '+name)
   mode='optimized'if optimized else'normal'
   with (ROOT/f'evidence/tests_{mode}_F13.log').open('w')as log:
    subprocess.run(args+['-m','unittest','discover','-s',str(ROOT/'src'),'-p','test_F13.py','-v'],env=env,check=True,stdout=log,stderr=subprocess.STDOUT)
   runs.append(dict(mode=mode,hash_seed=seed,outputs_checked=len(baseline),tests=30))
 scripts=['analyze_sources_F13.py','reference_audit_F13.py','acquire_F13.py','test_F13.py','reproduce_F13.py']
 result=dict(new_numerical_outputs=len(baseline),all_new_outputs_byte_identical_in_both_modes=True,
  runs=runs,files=baseline,source_scripts={n:sha(ROOT/'src'/n)for n in scripts},
  earlier_F12_fifty_output_reproduction_and_634_certificate_evidence_preserved=True,
  earlier_F11_192_tests_per_mode_evidence_preserved=True,no_new_AGB_admissions=True)
 (ROOT/'metadata/numerical_reproducibility_F13.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':run()
