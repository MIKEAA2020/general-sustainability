#!/usr/bin/env python3
"""Finite-MOL slack semigroup sup-norm convergence at binding-period times."""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from c4_equilibrium_spectrum import generator
P=370.95
out=[]
for m in [25,50,100]:
 A=generator(10.,m).toarray();vals=[]
 for k in [1,2,5,10,15,20,25,30,35,40]:
  E=expm(A*(k*P));vals.append({'binding_periods':k,'time':k*P,'semigroup_inf_norm':float(np.linalg.norm(E,np.inf))})
 print(m,[(x['binding_periods'],round(x['semigroup_inf_norm'],6)) for x in vals])
 out.append({'history_intervals':m,'dimension':4*(m+1),'values':vals})
Path('c4_slack_semigroup_inf_convergence.json').write_text(json.dumps({'tau_y':10,'binding_period':P,'norm':'induced infinity norm of upwind MOL semigroup','levels':out,'status':'finite-dimensional numerical evidence, not continuum bound'},indent=2))
