#!/usr/bin/env python3
"""Numerical orbit-ball sensitivity of the sixth-derivative coefficient bound.

Random low-mode real perturbations are normalized in physical sup norm. This is a
precursor, not an interval Lipschitz proof.
"""
import json
from pathlib import Path
import numpy as np
from c4_floquet_discrete import jac
root=Path(__file__).parent;z=np.load(root/'c4_fourier_K120_operator.npz');u0=z['u'];P=float(z['period']);n0=len(u0);tau=4.5;n=2048;freq=np.fft.fftfreq(n,d=1/n)
# interpolate base to check grid
c0=np.fft.fft(u0,axis=0)/n0;k0=np.fft.fftfreq(n0,d=1/n0).astype(int);C0=np.zeros((n,4),complex)
for k,row in zip(k0,c0):C0[k%n]=row
base=np.fft.ifft(C0*n,axis=0).real

def L6(u):
 C=np.fft.fft(u,axis=0)/n;zd=np.fft.ifft(C[:,2]*n*np.exp(-2j*np.pi*freq*tau/P)).real;AA=np.zeros((n,4,4));DD=np.zeros((n,4,4))
 for i in range(n):AA[i],DD[i]=jac(u[i],zd[i])
 Ac=np.fft.fft(AA,axis=0)/n;Dc=np.fft.fft(DD,axis=0)/n;mask=abs(freq)<=500
 return float(sum((2*np.pi*abs(freq[i])/P)**6*(np.linalg.norm(Ac[i],np.inf)+np.linalg.norm(Dc[i],np.inf)) for i in np.where(mask)[0]))
baseval=L6(base);rng=np.random.default_rng(20260821);radius=2e-5;vals=[]
for q in range(80):
 Cp=np.zeros((n,4),complex);Kp=20
 for k in range(0,Kp+1):
  if k==0:Cp[0]=rng.normal(size=4)
  else:
   a=rng.normal(size=4)+1j*rng.normal(size=4);Cp[k]=a;Cp[-k]=a.conjugate()
 p=np.fft.ifft(Cp*n,axis=0).real;p/=np.max(abs(p));vals.append(L6(base+radius*p))
# coordinate constant shifts
for j in range(4):
 for sign in [-1,1]:
  p=np.zeros_like(base);p[:,j]=sign;vals.append(L6(base+radius*p))
out={'base_L6_coefficient_sum':baseval,'radius_sup':radius,'samples':len(vals),'min':float(min(vals)),'max':float(max(vals)),'max_absolute_change':float(max(abs(np.array(vals)-baseval))),'empirical_Lipschitz_per_sup_radius':float(max(abs(np.array(vals)-baseval))/radius),'factor_two_margin_remaining':float(2e-4-2*baseval),'status':'random/coordinate sensitivity precursor only; interval all-direction bound pending'}
(root/'c4_sixth_derivative_sensitivity.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
