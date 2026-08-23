#!/usr/bin/env python3
"""Dense Fourier-collocation Newton correction for the C4 periodic seed (K=80).

Produces a high-accuracy finite-dimensional solution and approximate inverse norms
for later interval/radii-polynomial execution. Not itself a validated proof.
"""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import lu_factor,lu_solve
from c4_cycle_naim import rhs
from c4_floquet_discrete import jac
root=Path(__file__).parent
K=80;n=2*K+1
seed=np.load(root/'c4_tau4p5_cap_seed.npz');P0=float(seed['period']);tau=float(seed['tau']);modes=seed['modes'];coeff=seed['coeff']
# reconstruct K-mode seed at theta_j=j/n
C=np.zeros((n,4),complex)
for m,row in zip(modes,coeff):
 if abs(m)<=K:C[m%n]=row
u0=np.fft.ifft(C*n,axis=0).real
freq=np.fft.fftfreq(n,d=1/n)
def mat_from_symbol(sym):
 E=np.eye(n);return np.fft.ifft(sym[:,None]*np.fft.fft(E,axis=0),axis=0).real
Dtheta=mat_from_symbol(2j*np.pi*freq)
ref=u0.copy();refd=Dtheta@ref;phasevec=(refd/n).reshape(-1)
def shift(P):
 sym=np.exp(-2j*np.pi*freq*tau/P);S=mat_from_symbol(sym)
 sp=sym*(2j*np.pi*freq*tau/P**2);SP=mat_from_symbol(sp)
 return S,SP

def residual_jac(w,needJ=True):
 u=w[:-1].reshape(n,4);P=w[-1];S,SP=shift(P);zd=S@u[:,2];zdp=SP@u[:,2]
 f=np.vstack([rhs(u[i],zd[i]) for i in range(n)])
 R=(Dtheta@u-P*f).reshape(-1);phase=float(np.sum((u-ref)*refd)/n)
 out=np.r_[R,phase]
 if not needJ:return out
 J=np.zeros((4*n+1,4*n+1))
 # derivative Dtheta kron I in time-major ordering
 J[:4*n,:4*n]=np.kron(Dtheta,np.eye(4))
 for i in range(n):
  A,B=jac(u[i],zd[i]);rr=slice(4*i,4*i+4);cc=slice(4*i,4*i+4)
  J[rr,cc]-=P*A
  # only delayed Z column contributes, but use full B safely
  for l in range(n):
   J[rr,4*l+2]-=P*B[:,2]*S[i,l]
  J[rr,-1]=-f[i]-P*B[:,2]*zdp[i]
 J[-1,:-1]=phasevec
 return out,J
w=np.r_[u0.reshape(-1),P0]
hist=[]
for it in range(10):
 R,J=residual_jac(w);rn=float(np.linalg.norm(R,np.inf));hist.append(rn);print(it,rn,w[-1])
 if rn<1e-12:break
 lu=lu_factor(J);dw=lu_solve(lu,-R);w+=dw
# final diagnostics
R,J=residual_jac(w);lu=lu_factor(J);inv=np.linalg.inv(J)
u=w[:-1].reshape(n,4);P=w[-1];S,_=shift(P);zd=S@u[:,2]
floor=[]
for i in range(n):
 N,A,Z,E=u[i];regen=0.02*N*(1-N/100)*A/(A+1);deficit=.001*E*N-regen
 floor.append(np.log1p(np.exp(np.clip(10*deficit,-700,700)))/10) # delta=ln2/k cancels shift
np.savez_compressed(root/'c4_fourier_K80_newton.npz',period=P,u=u,J=J,residual=R)
out={'K':K,'nodes':n,'period':float(P),'newton_residual_history':hist,'final_residual_inf':float(np.linalg.norm(R,np.inf)),'correction_from_seed_inf':float(np.max(abs(u-u0))),'period_correction':float(P-P0),'jacobian_inverse_inf_norm':float(np.linalg.norm(inv,np.inf)),'jacobian_condition_inf':float(np.linalg.cond(J,np.inf)),'floor_margin_nodes':float(min(floor)),'status':'high-accuracy finite Fourier collocation; not interval validated'}
(root/'c4_fourier_K80_newton.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
