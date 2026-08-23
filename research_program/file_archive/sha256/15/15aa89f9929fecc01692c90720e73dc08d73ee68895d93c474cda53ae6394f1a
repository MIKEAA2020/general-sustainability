#!/usr/bin/env python3
"""K-refinement of phase-fixed Fourier collocation roots and inverse norms."""
import argparse,json
from pathlib import Path
import numpy as np
from scipy.linalg import lu_factor,lu_solve
from c4_cycle_naim import rhs
from c4_floquet_discrete import jac
root=Path(__file__).parent;seed=np.load(root/'c4_tau4p5_cap_seed.npz');Pseed=float(seed['period']);tau=float(seed['tau']);modes=seed['modes'].astype(int);coeff=seed['coeff']
def solve(K,compute_inverse=True):
 n=2*K+1;freq=np.fft.fftfreq(n,d=1/n);EYE=np.eye(n)
 def mat(sym):return np.fft.ifft(sym[:,None]*np.fft.fft(EYE,axis=0),axis=0).real
 Dth=mat(2j*np.pi*freq);C=np.zeros((n,4),complex)
 for m,row in zip(modes,coeff):
  if abs(m)<=K:C[m%n]=row
 u0=np.fft.ifft(C*n,axis=0).real;ref=u0.copy();refd=Dth@ref;phase=(refd/n).reshape(-1)
 def shift(P):
  sy=np.exp(-2j*np.pi*freq*tau/P);return mat(sy),mat(sy*(2j*np.pi*freq*tau/P**2))
 def RJ(w):
  u=w[:-1].reshape(n,4);P=w[-1];S,SP=shift(P);zd=S@u[:,2];zdp=SP@u[:,2];f=np.vstack([rhs(u[i],zd[i]) for i in range(n)]);R=np.r_[(Dth@u-P*f).reshape(-1),np.sum((u-ref)*refd)/n];J=np.zeros((4*n+1,4*n+1));J[:4*n,:4*n]=np.kron(Dth,np.eye(4))
  for i in range(n):
   A,B=jac(u[i],zd[i]);rr=slice(4*i,4*i+4);J[rr,rr]-=P*A
   J[rr,2:4*n:4]-=P*B[:,2,None]*S[i,None,:]
   J[rr,-1]=-f[i]-P*B[:,2]*zdp[i]
  J[-1,:-1]=phase;return R,J
 w=np.r_[u0.reshape(-1),Pseed];hist=[]
 for it in range(5):
  R,J=RJ(w);hist.append(float(np.linalg.norm(R,np.inf)))
  if hist[-1]<5e-10:break
  w+=lu_solve(lu_factor(J),-R)
 R,J=RJ(w);u=w[:-1].reshape(n,4);P=w[-1]
 if compute_inverse:
  inv=np.linalg.inv(J);invnorm=float(np.linalg.norm(inv,np.inf));cond=float(np.linalg.cond(J,np.inf))
 else:
  invnorm=None;cond=None
 # off-grid residual
 ng=4096;fg=np.fft.fftfreq(ng,d=1/ng);Cc=np.zeros((ng,4),complex);cc=np.fft.fft(u,axis=0)/n
 for k,row in zip(freq.astype(int),cc):Cc[k%ng]=row
 U=np.fft.ifft(Cc*ng,axis=0).real;dU=np.fft.ifft(2j*np.pi*fg[:,None]/P*Cc*ng,axis=0).real;zd=np.fft.ifft(Cc[:,2]*ng*np.exp(-2j*np.pi*fg*tau/P)).real;F=np.vstack([rhs(U[i],zd[i]) for i in range(ng)]);off=float(np.max(abs(dU-F)))
 np.savez_compressed(root/f'c4_fourier_K{K}_operator.npz',u=u,period=P,J=J,residual=R)
 return {'K':K,'dimension':4*n+1,'period':float(P),'newton_history':hist,'node_residual_inf':float(np.linalg.norm(R,np.inf)),'offgrid_residual_inf':off,'inverse_inf_norm':invnorm,'condition_inf':cond,'correction_from_seed_inf':float(np.max(abs(u-u0)))}
ap=argparse.ArgumentParser();ap.add_argument('--K',type=int,nargs='*',default=[40,60,80,100]);ap.add_argument('--skip-inverse',action='store_true');a=ap.parse_args()
out=[solve(K,not a.skip_inverse) for K in a.K]
(root/'c4_fourier_newton_K_convergence_latest.json').write_text(json.dumps({'levels':out,'status':'finite collocation convergence; not continuum inverse enclosure'},indent=2));print(json.dumps(out,indent=2))
