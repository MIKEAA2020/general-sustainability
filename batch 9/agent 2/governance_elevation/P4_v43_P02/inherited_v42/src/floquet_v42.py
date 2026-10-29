"""Independent method-of-steps variational monodromy in log/logit coordinates.
History state stores delayed Z only plus current u,v. RK4 with piecewise-linear
history interpolation; timestep convergence and phase multiplier are reported.
Floating-point spectral evidence, not a validated RFDE Floquet certificate.
"""
from pathlib import Path
import json,time,sys
import numpy as np
from numba import njit
from scipy.signal import resample
from scipy.sparse.linalg import LinearOperator,eigs
from periodic_orbits_v42 import field
ROOT=Path(__file__).resolve().parents[1]

@njit(cache=True)
def advance(vec,steps,h,lag,L,C):
    z=np.empty(L+steps+1);z[:L+1]=vec[:L+1];u=vec[L+1];v=vec[L+2]
    for j in range(steps):
        t=L+j-lag;i=int(np.floor(t));frac=t-i;zd0=(1-frac)*z[i]+frac*z[i+1]
        t=L+j+.5-lag;i=int(np.floor(t));frac=t-i;zd1=(1-frac)*z[i]+frac*z[i+1]
        t=L+j+1-lag;i=int(np.floor(t));frac=t-i;zd2=(1-frac)*z[i]+frac*z[i+1]
        z0=z[L+j];c=C[2*j];k1u=c[0]*u+c[1]*v;k1z=c[2]*u+c[3]*z0+c[4]*v;k1v=c[5]*v+c[6]*zd0
        uu=u+h*k1u/2;zz=z0+h*k1z/2;vv=v+h*k1v/2;c=C[2*j+1]
        k2u=c[0]*uu+c[1]*vv;k2z=c[2]*uu+c[3]*zz+c[4]*vv;k2v=c[5]*vv+c[6]*zd1
        uu=u+h*k2u/2;zz=z0+h*k2z/2;vv=v+h*k2v/2
        k3u=c[0]*uu+c[1]*vv;k3z=c[2]*uu+c[3]*zz+c[4]*vv;k3v=c[5]*vv+c[6]*zd1
        uu=u+h*k3u;zz=z0+h*k3z;vv=v+h*k3v;c=C[2*j+2]
        k4u=c[0]*uu+c[1]*vv;k4z=c[2]*uu+c[3]*zz+c[4]*vv;k4v=c[5]*vv+c[6]*zd2
        u+=h*(k1u+2*k2u+2*k3u+k4u)/6;v+=h*(k1v+2*k2v+2*k3v+k4v)/6;z[L+j+1]=z0+h*(k1z+2*k2z+2*k3z+k4z)/6
    out=np.empty(L+3);out[:L+1]=z[steps:steps+L+1];out[L+1]=u;out[L+2]=v;return out

def spectrum(w,tau,dt=.04,k=8):
    X=w[:-1].reshape(-1,3);n=len(X);T=w[-1];steps=int(np.ceil(T/dt));h=T/steps;lag=tau/h;L=int(np.ceil(lag));freq=np.fft.fftfreq(n,d=1/n)
    fine=resample(X,2*steps,axis=0);co=np.fft.fft(X[:,1]);shift=np.fft.ifft(co*np.exp(-2j*np.pi*freq*tau/T)).real;zd=resample(shift,2*steps)
    fine=np.vstack([fine,fine[0]]);zd=np.r_[zd,zd[0]];f,A,B=field(fine,zd,True)
    C=np.column_stack([A[:,0,0],A[:,0,2],A[:,1,0],A[:,1,1],A[:,1,2],A[:,2,2],B[:,2]])
    def mv(x):return advance(np.asarray(x,dtype=float),steps,h,lag,L,C)
    op=LinearOperator((L+3,L+3),matvec=mv,dtype=float);start=np.random.default_rng(20261029).normal(size=L+3);t0=time.time()
    vals,vecs=eigs(op,k=k,which='LM',tol=2e-10,maxiter=500,v0=start,ncv=max(32,2*k+2))
    idx=int(np.argmin(np.abs(vals-1)));neutral=vals[idx];others=np.delete(vals,idx);order=np.argsort(-np.abs(others));others=others[order]
    deriv=np.fft.ifft((2j*np.pi*freq/T)[:,None]*np.fft.fft(X,axis=0),axis=0).real;dfine=resample(deriv,2*steps,axis=0)
    tangent=np.r_[dfine[(-2*np.arange(L, -1,-1))%(2*steps),1],dfine[0,0],dfine[0,2]]
    align=float(abs(np.vdot(tangent,vecs[:,idx]))/(np.linalg.norm(tangent)*np.linalg.norm(vecs[:,idx])))
    vec=vecs[:,idx];defect=np.linalg.norm(mv(vec.real)+1j*mv(vec.imag)-neutral*vec)/np.linalg.norm(vec)
    return {'tau':float(tau),'dt_target':dt,'dt_actual':h,'steps':steps,'segment_dimension':L+3,'neutral_multiplier':[float(neutral.real),float(neutral.imag)],'neutral_alignment':align,'neutral_eigen_residual':float(defect),'nontrivial_multipliers':[[float(z.real),float(z.imag)]for z in others],'dominant_nontrivial_modulus':float(max(abs(others))),'wall_seconds':time.time()-t0}

if __name__=='__main__':
    archive=np.load(ROOT/'data/upper_arm_orbits_v42.npz');keys=archive.files
    if len(sys.argv)>1 and sys.argv[1]=='selected':keys=[keys[i]for i in [0,20,50,80,110,len(keys)-1]]
    results=[]
    for key in keys:
        r=spectrum(archive[key],float(key));results.append(r);print(json.dumps(r),flush=True)
        (ROOT/'data/upper_arm_floquet_v42.json').write_text(json.dumps({'method':'RK4 method-of-steps plus Arnoldi; no neutral deflation; phase alignment checked','certification':'floating-point, not validated full-spectrum enclosures','records':results},indent=2)+'\n')
