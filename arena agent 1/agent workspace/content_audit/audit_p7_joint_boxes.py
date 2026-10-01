#!/usr/bin/env python3
"""Independent re-execution of P7 six-axis joint-box claims (audit only).

Imports ONLY definitions, not the top-level report, from archived
p7/sensitivity.py. Uses the source's formulae and rho; all 64 corners,
4001-point [0.2,200] scan plus 80 bisection steps as in source.
The original report and manuscript do not specify the six-axis names; this
reconstruction assumes r,K,q,Emax,eta,dref based on the one-at-a-time table.
It is a sensitivity check, not an independent proof of model correctness.
"""
import ast, csv, hashlib, itertools, json
from pathlib import Path
src = Path('/home/user/p7/sensitivity.py')
text = src.read_text()
import numpy as np
from numpy.linalg import eigvals
from scipy.linalg import expm
names = {'np':np, 'eigvals':eigvals, 'expm':expm}
for node in ast.parse(text).body:
    if isinstance(node, ast.FunctionDef) and node.name in ('build','exact_review','euler_review','rho','crossings'):
        exec(compile(ast.Module(body=[node], type_ignores=[]), str(src), 'exec'), names)
build, rho, crossings = (names[n] for n in ('build','rho','crossings'))
base = dict(r=0.02,K=100.0,q=0.001,eta=0.914,Emax=30.0,dref=1.0)
axes = tuple(base)
rows=[];summary=[]
for pct in (.005,.01):
    for signs in itertools.product((-1,1), repeat=len(axes)):
        params={n:base[n]*(1+pct*sign) for n,sign in zip(axes,signs)}
        m=build(**params)
        xs=crossings(m,m['CE_m'],m['CZ_m'],True,n=4001)
        annual=rho(1.,m,m['CE_m'],m['CZ_m'],True)
        row={'pct':pct,'signs':','.join(f'{n}:{s:+d}' for n,s in zip(axes,signs)),
             'annual_rho':annual,'n_crossings':len(xs),
             'crossings':';'.join(f'{t:.8f}:{direction}' for t,direction in xs)}
        rows.append(row)
    matched=[x for x in rows if x['pct']==pct]
    cs=[float(t.split(':')[0]) for x in matched for t in x['crossings'].split(';') if t]
    no=[x for x in matched if x['n_crossings']==0]
    result={'pct':pct,'crossing_corners':64-len(no),'no_crossing_corners':len(no),
            'range':(min(cs),max(cs)) if cs else None,
            'no_crossing_annual_rho_range':(min(x['annual_rho'] for x in no),max(x['annual_rho'] for x in no)) if no else None,
            'multiple_crossing_corners':sum(x['n_crossings']>1 for x in matched)}
    summary.append(result)
    print(json.dumps(result,sort_keys=True))
out=Path('/home/user/content_audit')
with (out/'p7_joint_box_recheck.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
(out/'p7_joint_box_recheck.json').write_text(json.dumps({'source':str(src),'source_sha256':hashlib.sha256(text.encode()).hexdigest(),'assumed_axes':axes,'grid':4001,'range_T':[.2,200.], 'summary':summary},indent=2)+'\n')
