from pathlib import Path
import json,time
import numpy as np
from periodic_orbits_v42 import Collocation,resize
from floquet_v42 import spectrum
ROOT=Path(__file__).resolve().parents[1]

def run():
    a=np.load(ROOT/'data/upper_arm_orbits_v42.npz');keys=a.files;results=[];fine={}
    for target in [64.43828538552961,80.,100.,120.,149.5,155.]:
        key=min(keys,key=lambda k:abs(float(k)-target));w=a[key];tau=target;rows=[]
        for n in [257,513,1025]:
            c=Collocation(n);w,ok,err,it=c.newton(resize(w,n),tau,tol=3e-10,maxit=25)
            if not ok:raise RuntimeError('Mesh refinement failed')
            q=c.offgrid(w,tau,count=4097);row={'nodes':n,'ok':ok,'collocation_residual':err,**q};rows.append(row);print('mesh',tau,json.dumps(row),flush=True)
        fine[str(target)]=w
        fl=[spectrum(w,tau,dt=h)for h in [.04,.02,.01]]
        result={'tau':tau,'meshes':rows,'floquet_steps':fl};results.append(result);print('floquet',tau,json.dumps(fl),flush=True)
        (ROOT/'data/upper_arm_refinement_v42.json').write_text(json.dumps({'certification':'Numerical mesh and timestep convergence, not continuum proof','records':results},indent=2)+'\n');np.savez_compressed(ROOT/'data/upper_arm_refined_orbits_v42.npz',**fine)
if __name__=='__main__':run()
