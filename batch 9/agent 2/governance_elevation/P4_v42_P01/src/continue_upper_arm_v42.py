"""Bounded continuation of upper stable arm with odd grids and log/logit states.
Run with OPENBLAS_NUM_THREADS=1. Seed is extracted from the pinned archive.
Refinement and off-grid defects are recorded; Floquet checks are separate.
"""
from pathlib import Path
import sys,json,time
import numpy as np
from periodic_orbits_v42 import Collocation,from_physical,resize
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/'data';DATA.mkdir(exist_ok=True)

def run(seed_file,target=155.):
    archive=np.load(seed_file);w0=archive['64.438285386'];tau=64.43828538552961
    w=np.r_[from_physical(w0[:-1].reshape(64,3)).ravel(),w0[-1]];n=129;c=Collocation(n);w,ok,err,it=c.newton(resize(w,n),tau)
    if not ok:raise RuntimeError('Seed correction failed')
    records=[];orbits={};dtau=.05;prev=None;attempts=0;t0=time.time()
    while tau<target and attempts<900:
        attempts+=1
        quality=c.offgrid(w,tau,count=2*n+3)
        if max(quality['offgrid_abs_residual_N_Z_E'])>1e-6 and n<513:
            n=2*n-1;c=Collocation(n);w,ok,err,it=c.newton(resize(w,n),tau)
            print('refine',n,tau,ok,err,flush=True)
            if not ok:raise RuntimeError('Refinement failed')
            quality=c.offgrid(w,tau,count=2*n+3)
        row=dict(tau=tau,nodes=n,collocation_residual=err,**quality)
        if not records or abs(records[-1]['tau']-tau)>1e-10:
            records.append(row);orbits[f'{tau:.12f}']=w.copy();print(json.dumps(row),flush=True)
            (DATA/'upper_arm_continuation_v42.json').write_text(json.dumps({'status':'running','target':target,'records':records},indent=2)+'\n');np.savez_compressed(DATA/'upper_arm_orbits_v42.npz',**orbits)
        newtau=min(target,tau+dtau);predict=w.copy()
        if prev is not None and len(prev[1])==len(w):predict=w+(w-prev[1])*((newtau-tau)/(tau-prev[0]))
        wn,ok,en,its=c.newton(predict,newtau)
        if ok and np.ptp(wn[:-1].reshape(n,3)[:,0])>.001:
            prev=(tau,w.copy());tau=newtau;w=wn;err=en;dtau=min(.75,dtau*1.25)
        else:
            dtau*=.5;print('retry',tau,newtau,dtau,en,flush=True)
            if dtau<.0001:break
    quality=c.offgrid(w,tau,count=max(2049,2*n+3));records.append(dict(tau=tau,nodes=n,collocation_residual=err,**quality));orbits[f'{tau:.12f}']=w
    result={'status':'target_reached'if tau>=target else'stalled','target':target,'last_tau':tau,'wall_seconds':time.time()-t0,'attempts':attempts,'method':'Odd Fourier collocation; log N and effort logit; natural-parameter predictor/corrector; no clipping','certification':'floating-point continuation and off-grid defects, not continuum proof or Floquet stability certificate','records':records}
    (DATA/'upper_arm_continuation_v42.json').write_text(json.dumps(result,indent=2)+'\n');np.savez_compressed(DATA/'upper_arm_orbits_v42.npz',**orbits);print('FINAL',json.dumps({k:v for k,v in result.items()if k!='records'}),flush=True)
if __name__=='__main__':run(sys.argv[1],float(sys.argv[2])if len(sys.argv)>2 else 155.)
