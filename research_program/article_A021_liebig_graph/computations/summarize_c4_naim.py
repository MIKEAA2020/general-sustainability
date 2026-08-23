#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
from c4_cycle_naim import rhs

root=Path(__file__).parent
rows=[]
for tag in ['dt0p25','dt0p1','dt0p05']:
    j=json.loads((root/f'c4_floquet_{tag}.json').read_text())
    rows.append({k:j[k] for k in ['dt','dimension','period','phase_multiplier','phase_error','dominant_nontrivial_modulus','normal_exponent','count_modulus_ge_1']})
# tangent-speed bound from fine orbit over final cycle
z=np.load(root/'c4_tau4p5_fine.npz',allow_pickle=True);t=z['t'];x=z['x'];dt=float(z['dt']);tau=float(z['tau']);d=round(tau/dt)
N=x[:,0];ii=np.where((N[1:-1]>N[:-2])&(N[1:-1]>=N[2:]))[0]+1;s,e=ii[-2],ii[-1]
speeds=[]
for k in range(s-d,e+1):
    zd=x[k-d,2] if k>=d else x[0,2]
    speeds.append(np.linalg.norm(rhs(x[k],zd)))
speeds=np.asarray(speeds)
# history tangent sup norm at each phase
period=e-s
hs=[]
for i in range(s,e): hs.append(float(np.max(speeds[(i-s):(i-s)+d+1])))
mc=max(hs)/min(hs)
# finite-discrete leading projection conditioning
fm=np.load(root/'c4_floquet_dt0p05.npz');M=fm['M']; vals,vr=np.linalg.eig(M); idx=np.argmin(abs(vals-1)); lam=vals[idx]; v=vr[:,idx]
valsL,vl=np.linalg.eig(M.T); idxL=np.argmin(abs(valsL-lam)); w=vl[:,idxL]
scale=np.dot(w,v); proj_norm=float(np.linalg.norm(v)*np.linalg.norm(w)/abs(scale))
res={'selected_orbit':{'model':'gated Candidate-A C4','tau':tau,'phase':'N maximum','period':float(period*dt),'ranges':json.loads((root/'c4_tau4p5_fine.json').read_text())['ranges'],'floor_margin':json.loads((root/'c4_tau4p5_fine.json').read_text())['floor_margin']},'convergence':rows,'tangent_history_norm':{'min':float(min(hs)),'max':float(max(hs)),'M_c_ratio':float(mc)},'finite_discrete_phase_projection_norm':proj_norm,'warning':'Finite-dimensional RK4 history discretization; not a rigorous enclosure of the RFDE spectrum.'}
(root/'c4_naim_numerical_summary.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
