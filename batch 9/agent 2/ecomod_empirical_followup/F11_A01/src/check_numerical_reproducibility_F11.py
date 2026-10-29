#!/usr/bin/env python3
"""Compare normal/optimized numerical outputs, without asserting PDF byte identity."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]

def fingerprints():
    paths=sorted((ROOT/'data').glob('*.csv'))+[ROOT/'metadata/analysis_F11.json',ROOT/'metadata/joint_identification_F11.json']
    return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--offline',action='store_true');a=p.parse_args()
    before=fingerprints()
    for optimized in (False,True):
        for name in ('identification_F11.py','joint_identification_F11.py'):
            label=('optimized_'if optimized else'normal_')+name.replace('.py','.log')
            cmd=[sys.executable]+(['-O']if optimized else[])+['src/'+name]+(['--offline']if a.offline else[])
            with (ROOT/'evidence'/label).open('w')as log:subprocess.run(cmd,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,check=True)
        after=fingerprints()
        if after!=before:raise ValueError('Numerical CSV/metadata bytes changed across execution modes')
    payload=dict(normal_and_optimized_numeric_bytes_identical=True,
                 compared_files=len(before),files=before,
                 PDF_byte_identity_claimed=False,
                 scope='Determinism and optimized-mode guards, not ecological validation')
    (ROOT/'metadata/numerical_reproducibility_F11.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(f'Exact numerical bytes agree for {len(before)} files in normal and optimized execution.')
