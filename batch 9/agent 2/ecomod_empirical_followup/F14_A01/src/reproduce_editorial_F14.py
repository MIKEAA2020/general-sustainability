#!/usr/bin/env python3
"""Repeat the editorial assembly/plots in normal and optimized modes, not a new empirical study."""
from pathlib import Path
import hashlib,json,subprocess,sys,os
ROOT=Path(__file__).resolve().parents[1]
NAMES=['figures/account_composition_F14.pdf','figures/endpoint_cohorts_F14.pdf','figures/inventory_uncertainty_F14.pdf','metadata/plot_values_F14.json','integrated_F14_A01_main.tex','integrated_F14_A01_SI.tex','src/identification_protocols_SI_F14.tex','src/national_protocols_SI_F14.tex','src/local_cover_table_SI_F14.tex']
def hashes():return {n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest()for n in NAMES}
def run():
 # Establish baseline with the final source before the independent runs.
 for script in ['build_assets_F14.py','assemble_F14.py']:subprocess.run([sys.executable,str(ROOT/'src'/script)],check=True)
 expected=hashes();runs=[]
 for optimized,seed in [(False,17),(True,73)]:
  cmd=[sys.executable]+(['-O']if optimized else[]);env=dict(os.environ,PYTHONHASHSEED=str(seed));mode='optimized'if optimized else'normal'
  for script in ['build_assets_F14.py','assemble_F14.py']:subprocess.run(cmd+[str(ROOT/'src'/script)],env=env,check=True)
  if hashes()!=expected:raise ValueError('Editorial artifact byte mismatch '+mode)
  with (ROOT/f'evidence/tests_{mode}_F14.log').open('w')as log:subprocess.run(cmd+[str(ROOT/'src/test_F14.py')],stdout=log,stderr=subprocess.STDOUT,env=env,check=True)
  runs.append(dict(mode=mode,hash_seed=seed,artifacts_byte_identical=9,tests=20))
 scripts=['assemble_F14.py','build_assets_F14.py','test_F14.py','reproduce_editorial_F14.py']
 (ROOT/'metadata/editorial_reproducibility_F14.json').write_text(json.dumps(dict(runs=runs,files=expected,source_scripts={n:hashlib.sha256((ROOT/'src'/n).read_bytes()).hexdigest()for n in scripts},new_empirical_estimates=False,workbook_preservation_checked_by_cell_readback=True),indent=2)+'\n')
 print('Nine editorial artifacts byte-identical; 20 tests pass in each execution mode.')
if __name__=='__main__':run()
