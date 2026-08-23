#!/usr/bin/env python3
"""Fourier coefficient norms of periodic C4 linearization along K120 orbit."""
import json
from pathlib import Path
import numpy as np
from c4_floquet_discrete import jac
root=Path(__file__).parent;z=np.load(root/'c4_fourier_K120_operator.npz');u0=z['u'];P=float(z['period']);n0=len(u0);tau=4.5;n=4096
c=np.fft.fft(u0,axis=0)/n0;k0=np.fft.fftfreq(n0,d=1/n0).astype(int);C=np.zeros((n,4),complex)
for k,row in zip(k0,c):C[k%n]=row
freq=np.fft.fftfreq(n,d=1/n);u=np.fft.ifft(C*n,axis=0).real;zd=np.fft.ifft(C[:,2]*n*np.exp(-2j*np.pi*freq*tau/P)).real
AA=np.zeros((n,4,4));DD=np.zeros((n,4,4))
for i in range(n):AA[i],DD[i]=jac(u[i],zd[i])
Ac=np.fft.fft(AA,axis=0)/n;Dc=np.fft.fft(DD,axis=0)/n
out={}
for nu in [1.0,1.001,1.005,1.01]:
 w=nu**abs(freq);An=sum(np.linalg.norm(Ac[i],np.inf)*w[i] for i in range(n));Dn=sum(np.linalg.norm(Dc[i],np.inf)*w[i] for i in range(n));L=float(An+Dn);Kcrit=int(np.ceil(P*L/(2*np.pi)-1));out[str(nu)]={'A_l1nu':float(An),'D_l1nu':float(Dn),'total_convolution_bound':L,'diagonal_tail_Kcrit':Kcrit}
# mode envelope and tail sums
mode=[]
for k in range(0,401):
 i=k%n;mode.append({'k':k,'A_inf':float(np.linalg.norm(Ac[i],np.inf)),'D_inf':float(np.linalg.norm(Dc[i],np.inf))})
(root/'c4_linearization_fourier_decay.json').write_text(json.dumps({'period':P,'weights':out,'positive_modes_0_400':mode,'status':'numerical Fourier coefficient bounds; not outward interval tail'},indent=2));print(json.dumps(out,indent=2))
