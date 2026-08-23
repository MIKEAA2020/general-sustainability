#!/usr/bin/env python3
"""Finite-history phase projection and stable-complement sup-norm powers."""
import json
from pathlib import Path
import numpy as np
root=Path(__file__).parent
out=[]
for tag in ['dt0p25','dt0p1','dt0p05']:
 z=np.load(root/f'c4_floquet_{tag}.npz');M=z['M'];vals,vr=np.linalg.eig(M)
 i=int(np.argmin(abs(vals-1)));lam=vals[i];v=vr[:,i]
 valsL,vl=np.linalg.eig(M.T);j=int(np.argmin(abs(valsL-lam)));w=vl[:,j];w=w/(w@v)
 P=np.outer(v,w);S=M-lam*P
 levels=[];A=np.eye(M.shape[0])
 for n in range(1,81):
  A=A@S
  if n in [1,2,3,5,10,15,20,25,30,35,40,50,60,70,80]:
   levels.append({'periods':n,'stable_power_inf_norm':float(np.linalg.norm(A,np.inf))})
 out.append({'tag':tag,'dimension':int(M.shape[0]),'phase_multiplier':[float(lam.real),float(lam.imag)],'phase_projection_inf_norm':float(np.linalg.norm(P,np.inf)),'stable_powers':levels})
 print(tag,out[-1]['phase_projection_inf_norm'],[(x['periods'],round(x['stable_power_inf_norm'],6)) for x in levels])
(root/'c4_discrete_prefactor_convergence.json').write_text(json.dumps({'norm':'matrix induced infinity norm on discretized history samples','levels':out,'status':'finite-history numerical evidence, not continuum operator bound'},indent=2))
