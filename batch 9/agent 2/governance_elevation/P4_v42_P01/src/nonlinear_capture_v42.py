"""Fresh nonlinear method-of-steps runs from the registered depleted history.
Log stock/logit effort; no boundary clipping. Compare tail waveform with the
continued periodic orbit, allowing one phase shift only (no amplitude fitting).
"""
from pathlib import Path
import json,math,time
import numpy as np
from numba import njit
from scipy.signal import resample
from scipy.optimize import minimize_scalar
from periodic_orbits_v42 import physical
ROOT=Path(__file__).resolve().parents[1]

@njit(cache=True)
def f(u,z,v,zd):
    N=math.exp(u);s=1/(1+math.exp(-v));E=30*s;deficit=N*(.001*E-.02+.0002*N);x=10*deficit
    mem=deficit if x>40 else(math.exp(x)/10 if x< -40 else math.log1p(math.exp(x))/10)
    return .02*(1-N/100)-.001*E,(mem-z)/5,.914*(zd-E/30)+.01*zd/(E*(1+zd))

@njit(cache=True)
def trajectory(tau,dt,horizon=40000.,tail=1000.,output_dt=.1,history=2):
    steps=int(round(horizon/dt));lag=tau/dt;L=int(math.ceil(lag))+2;buf=np.full(L,math.log(2)/10)
    u=math.log(5. if history==2 else 90.);z=math.log(2)/10;effort=15. if history==2 else 1.044811698868834;v=math.log(effort/(30-effort));skip=int(round(output_dt/dt));first=steps-int(round(tail/dt));out=np.empty((int(round(tail/dt))//skip,4));ct=0
    for j in range(steps):
        t=j-lag;i=int(math.floor(t));ff=t-i;zd0=(1-ff)*buf[i%L]+ff*buf[(i+1)%L]
        t=j+.5-lag;i=int(math.floor(t));ff=t-i;zd1=(1-ff)*buf[i%L]+ff*buf[(i+1)%L]
        t=j+1-lag;i=int(math.floor(t));ff=t-i;zd2=(1-ff)*buf[i%L]+ff*buf[(i+1)%L]
        a=f(u,z,v,zd0);b=f(u+dt*a[0]/2,z+dt*a[1]/2,v+dt*a[2]/2,zd1);c=f(u+dt*b[0]/2,z+dt*b[1]/2,v+dt*b[2]/2,zd1);d=f(u+dt*c[0],z+dt*c[1],v+dt*c[2],zd2)
        u+=dt*(a[0]+2*b[0]+2*c[0]+d[0])/6;z+=dt*(a[1]+2*b[1]+2*c[1]+d[1])/6;v+=dt*(a[2]+2*b[2]+2*c[2]+d[2])/6;buf[(j+1)%L]=z
        if j>=first and(j-first+1)%skip==0:
            out[ct,0]=(j+1)*dt;out[ct,1]=math.exp(u);out[ct,2]=z;out[ct,3]=30/(1+math.exp(-v));ct+=1
    return out[:ct]

def compare(tail,w):
    table=physical(resample(w[:-1].reshape(-1,3),65536,axis=0));T=w[-1];grid=np.arange(len(table)+1)/len(table);table=np.vstack([table,table[0]]);obs=tail[:,1:];scale=np.maximum(np.ptp(table,axis=0),1e-4)
    def pred(phase):
        tt=(tail[:,0]/T+phase)%1;return np.column_stack([np.interp(tt,grid,table[:,j])for j in range(3)])
    def loss(phase):return float(np.mean(((obs-pred(phase))/scale)**2))
    phases=np.arange(256)/256;best=phases[np.argmin([loss(t)for t in phases])];opt=minimize_scalar(loss,bounds=(best-1/256,best+1/256),method='bounded',options={'xatol':1e-13});dif=obs-pred(opt.x)
    return {'period_from_continuation':float(T),'phase_shift_cycles':float(opt.x%1),'normalised_waveform_rms':float(np.sqrt(opt.fun)),'rms_N_Z_E':np.sqrt(np.mean(dif*dif,axis=0)).tolist(),'max_abs_N_Z_E':np.max(np.abs(dif),axis=0).tolist(),'tail_N_min_max':[float(obs[:,0].min()),float(obs[:,0].max())],'tail_E_min_max':[float(obs[:,2].min()),float(obs[:,2].max())]}
if __name__=='__main__':
    a=np.load(ROOT/'data/upper_arm_refined_orbits_v42.npz');records=[]
    for tau,history,horizon in [(149.5,1,100000.),(149.5,2,40000.),(155.,2,40000.)]:
        for dt in [.04,.02]:
            t=time.time();tail=trajectory(tau,dt,horizon=horizon,output_dt=.2,history=history);w=a[str(tau)];q=compare(tail,w);r={'tau':tau,'dt':dt,'history':('H2: N=5,Z=log(2)/10,E=15 constant'if history==2 else'H1: N=90,Z=log(2)/10,E=E_star/2 constant'),'horizon_years':horizon,'tail_years':1000,'boundary_clipping':False,'waveform_fit':'one phase shift only; fixed collocation period and amplitudes','wall_seconds':time.time()-t,'capture_waveform_supported':q['normalised_waveform_rms']<1e-4,**q};records.append(r)
            np.savez_compressed(ROOT/f'data/nonlinear_tail_H{history}_tau{str(tau).replace(".","p")}_dt{str(dt).replace(".","p")}_v42.npz',trajectory=tail);print(json.dumps(r),flush=True);(ROOT/'data/nonlinear_capture_check_v42.json').write_text(json.dumps({'certification':'Independent floating-point long-horizon integration; not basin completeness or validated orbit existence','records':records},indent=2)+'\n')
