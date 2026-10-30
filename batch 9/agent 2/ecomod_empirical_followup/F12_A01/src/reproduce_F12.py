#!/usr/bin/env python3
"""Execute the dependency-ordered numerical programme in normal and optimized Python.
Raw provider workbooks/PDF bodies remain in the excluded cache, not in the deposit.
"""
import argparse,hashlib,json,os,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];CACHE=ROOT.parent/'.cache/F12/raw'


def run(account,download=False):
 if download:
  sys.path.insert(0,str(ROOT/'src'));from acquire_F12 import retrieve
  for name,r in json.loads((ROOT/'metadata/source_registry_F12.json').read_text()).items():retrieve(name,r['url'])
 commands=[('accounts_F12.py',['--workbook',str(account)]),('brazil_national_F12.py',['--workbook',str(CACHE/'BRA_C11_biome_state.xlsx')]),('indonesia_national_F12.py',['--workbook',str(CACHE/'IDN_C41.xlsx')]),('finland_inventory_F12.py',['--offline']),('finland_change_bounds_F12.py',['--nfi12',str(CACHE/'FIN_NFI12_tables.xlsx'),'--nfi13',str(CACHE/'FIN_NFI13_tables.xlsx')]),('reference_audit_F12.py',[]),('indonesia_collection_sensitivity_F12.py',[]),('transition_path_bounds_F12.py',['--brazil',str(CACHE/'BRA_C11_biome_state.xlsx'),'--indonesia',str(CACHE/'IDN_C41.xlsx')]),('audit_transition_witnesses_F12.py',[]),('summarize_F12.py',[])]
 snapshots={};env=dict(os.environ,PYTHONHASHSEED='17',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1')
 metadata=['accounts_analysis_F12.json','BRA_C11_analysis_F12.json','IDN_C41_analysis_F12.json','FIN_inventory_assessment_F12.json','FIN_cycle_volume_inference_F12.json','BRA_reference_compatibility_F12.json','IDN_collection_sensitivity_F12.json','transition_path_inference_F12.json','transition_witness_audit_F12.json','synthesis_F12.json']
 for mode in ['normal','optimized']:
  env['PYTHONHASHSEED']='17'if mode=='normal'else'73'
  for script,args in commands:
   print(mode,script,flush=True)
   with (ROOT/'evidence'/f'{script[:-3]}_{mode}_F12.log').open('w')as f:subprocess.run([sys.executable]+(['-O']if mode=='optimized'else[])+[str(ROOT/'src'/script)]+args,cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
  files=sorted((ROOT/'data').glob('*'))+[ROOT/'metadata'/n for n in metadata]
  snapshots[mode]={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in files if p.is_file()}
 if snapshots['normal']!=snapshots['optimized']:raise ValueError('Numerical output differs by optimization/hash seed')
 result=dict(source_scripts={script:hashlib.sha256((ROOT/'src'/script).read_bytes()).hexdigest()for script in [x[0]for x in commands]+['reproduce_F12.py']},normal_and_optimized_bytes_identical=True,hash_seeds=[17,73],LP_solver_thread_environment=1,files=snapshots['normal'],outputs_checked=len(snapshots['normal']),national_raw_sources_downloaded_if_requested=download,physical_validation_not_implied=True)
 (ROOT/'metadata/numerical_reproducibility_F12.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(outputs_checked=result['outputs_checked'],normal_and_optimized_bytes_identical=True),indent=2),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--account-workbook',type=Path,required=True);p.add_argument('--download',action='store_true');a=p.parse_args();run(a.account_workbook.resolve(),a.download)
