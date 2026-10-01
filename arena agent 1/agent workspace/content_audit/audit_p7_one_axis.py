#!/usr/bin/env python3
"""Recompute the correct worst ±1% sensitivity, without manuscript edits."""
import ast,csv,math
from pathlib import Path
import numpy as np
from numpy.linalg import eigvals
from scipy.linalg import expm
source=Path('/home/user/p7/sensitivity.py')
names={'np':np,'eigvals':eigvals,'expm':expm}
for node in ast.parse(source.read_text()).body:
    if isinstance(node,ast.FunctionDef) and node.name in ('build','exact_review','euler_review','rho','crossings'):
        exec(compile(ast.Module(body=[node],type_ignores=[]),str(source),'exec'),names)
B={'r':.02,'K':100.,'q':.001,'eta':.914,'Emax':30.,'dref':1.,'d0':.01,'tm':5.,'Zref':1.}
def get(**kw):
 m=names['build'](**kw);xs=names['crossings'](m,m['CE_m'],m['CZ_m'],True,n=4001)
 return xs[0][0] if xs else float('nan')
base=get();rows=[]
for key,val in B.items():
 v={f:get(**{key:val*f}) for f in (.98,.99,1.01,1.02)}
 correct=max(abs(v[.99]-base),abs(v[1.01]-base))/base*100
 old=max(abs(v[.98]-base),abs(v[1.02]-base))/base*100
 rows.append(dict(axis=key,minus2=v[.98],minus1=v[.99],baseline=base,plus1=v[1.01],plus2=v[1.02],worst_actual_1pct=correct,worst_actual_2pct=old))
for r in rows:
 print('%-5s  ±1%% %8.2f%%  ±2%% %8.2f%%  crossing -1%% %8.3f +1%% %8.3f' % (r['axis'],r['worst_actual_1pct'],r['worst_actual_2pct'],r['minus1'],r['plus1']))
with Path('/home/user/content_audit/p7_one_axis_recheck.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
