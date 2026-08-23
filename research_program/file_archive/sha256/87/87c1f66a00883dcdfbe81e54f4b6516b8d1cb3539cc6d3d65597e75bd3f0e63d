#!/usr/bin/env python3
"""Numerical Newton-Kantorovich precursor for the K=80 collocation root.

Estimates Jacobian Lipschitz constants by directional finite differences. This is
not interval arithmetic and does not replace outward-rounded Hessian bounds.
"""
import json,importlib.util
from pathlib import Path
import numpy as np
root=Path(__file__).parent
spec=importlib.util.spec_from_file_location('newtonmod',root/'c4_fourier_newton.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
z=np.load(root/'c4_fourier_K80_newton.npz');u=z['u'];P=float(z['period']);w=np.r_[u.reshape(-1),P];R,J=mod.residual_jac(w);A=np.linalg.inv(J);Y=float(np.linalg.norm(A@R,np.inf));Z0=float(np.linalg.norm(np.eye(len(J))-A@J,np.inf));B=float(np.linalg.norm(A,np.inf))
rng=np.random.default_rng(20260820);eps=1e-6;ests=[]
# random infinity-normalized directions plus period and representative state coordinates
vecs=[]
for _ in range(80):
 v=rng.uniform(-1,1,len(w));v/=np.linalg.norm(v,np.inf);vecs.append(v)
# explicit coordinate directions: four states at 8 phases, and period
for i in np.linspace(0,mod.n-1,8,dtype=int):
 for j in range(4):
  v=np.zeros(len(w));v[4*i+j]=1;vecs.append(v)
v=np.zeros(len(w));v[-1]=1;vecs.append(v)
for v in vecs:
 _,Jp=mod.residual_jac(w+eps*v);_,Jm=mod.residual_jac(w-eps*v)
 ests.append(float(np.linalg.norm((Jp-Jm)/(2*eps),np.inf)))
L=max(ests);h=B*L*Y
out={'dimension':len(w),'inverse_inf_norm_B':B,'newton_residual_Y_equal_norm_A_F':Y,'inverse_defect_Z0':Z0,'directional_samples':len(ests),'epsilon':eps,'max_directional_J_lipschitz_inf':L,'median_directional_J_lipschitz_inf':float(np.median(ests)),'kantorovich_h_precursor_B_L_Y':h,'finite_root_condition_h_below_half':bool(h<.5),'status':'numerical directional precursor only; rigorous interval Hessian/tail bound pending'}
(root/'c4_fourier_K80_kantorovich_precursor.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
