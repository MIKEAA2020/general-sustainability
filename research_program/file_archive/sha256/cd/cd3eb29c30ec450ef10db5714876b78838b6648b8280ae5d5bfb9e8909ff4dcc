#!/usr/bin/env python3
"""Prepare a compact Fourier seed and residual for validated C4 periodic-orbit work."""
import json
from pathlib import Path
import numpy as np
from c4_cycle_naim import rhs,P
root=Path(__file__).parent
z=np.load(root/'c4_tau4p5_fine.npz',allow_pickle=True);t=z['t'];x=z['x'];dt=float(z['dt']);tau=float(z['tau'])
from scipy.interpolate import CubicSpline
N=x[:,0];ii=np.where((N[1:-1]>N[:-2])&(N[1:-1]>=N[2:]))[0]+1;s,e=ii[-2],ii[-1]
def vertex_time(i):
    ym,y0,yp=N[i-1],N[i],N[i+1]; den=ym-2*y0+yp
    return t[i]+(0.5*(ym-yp)/den)*dt
start=vertex_time(s); stop=vertex_time(e); period=stop-start
n=int(round(period/dt)); grid=start+np.arange(n)*period/n
u=np.column_stack([CubicSpline(t[s-3:e+4],x[s-3:e+4,j])(grid) for j in range(4)])
end_state=np.array([CubicSpline(t[s-3:e+4],x[s-3:e+4,j])(stop) for j in range(4)])
# FFT convention u_j=sum_k c_k exp(2 pi i k j/n)
c=np.fft.fft(u,axis=0)/n;freq=np.fft.fftfreq(n,d=1/n)
# spectral derivative in physical time
du=np.fft.ifft((2j*np.pi*freq[:,None]/period)*np.fft.fft(u,axis=0),axis=0).real
# periodic delayed Z via exact Fourier phase
zd=np.fft.ifft(np.fft.fft(u[:,2])*np.exp(-2j*np.pi*freq*tau/period)).real
f=np.vstack([rhs(u[j],zd[j]) for j in range(n)])
r=du-f
# retain symmetric low modes |k|<=K
K=512;inds=np.r_[0:K+1,n-K:n]
np.savez_compressed(root/'c4_tau4p5_cap_seed.npz',period=period,tau=tau,coeff=c[inds],modes=freq[inds].astype(int),phase_state=u[0],ranges=np.c_[u.min(0),u.max(0)])
out={'period':period,'tau':tau,'samples':n,'retained_modes_each_side':K,'phase_state':[float(v) for v in u[0]],'endpoint_mismatch_inf':float(np.max(abs(end_state-u[0]))),'spectral_residual_inf':float(np.max(abs(r))),'spectral_residual_rms':float(np.sqrt(np.mean(r*r))),'state_residual_inf':[float(np.max(abs(r[:,j]))) for j in range(4)],'floor_argument_min':float(min(P['delta']-np.log(2)/P['k']+np.log1p(np.exp(np.clip(P['k']*(P['q']*row[3]*row[0]-P['r']*row[0]*(1-row[0]/P['K'])*row[1]/(row[1]+P['A0'])),-700,700)))/P['k'] for row in u))}
(root/'c4_tau4p5_cap_seed.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
