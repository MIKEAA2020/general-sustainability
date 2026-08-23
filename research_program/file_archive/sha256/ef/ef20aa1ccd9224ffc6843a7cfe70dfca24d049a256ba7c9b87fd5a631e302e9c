#!/usr/bin/env python3
"""Fourier decay, weight selection, and truncated-seed residual diagnostics."""
import json
from pathlib import Path
import numpy as np
from c4_cycle_naim import rhs,P
root=Path(__file__).parent;z=np.load(root/'c4_tau4p5_cap_seed.npz');period=float(z['period']);tau=float(z['tau']);modes=z['modes'].astype(int);coeff=z['coeff']
# decay fits on signal-dominated range
decay={}
for j,name in enumerate(['N','A','Z','E']):
 ks=np.arange(10,71);a=np.array([abs(coeff[modes==k,j][0]) for k in ks]);slope,inter=np.polyfit(ks,np.log(a),1)
 decay[name]={'slope':float(slope),'suggested_max_nu':float(np.exp(-slope)),'R2':float(np.corrcoef(ks,np.log(a))[0,1]**2)}
results=[];n=8192;freq=np.fft.fftfreq(n,d=1/n)
for K in [40,60,80,100]:
 C=np.zeros((n,4),complex)
 for mode,row in zip(modes,coeff):
  if abs(mode)<=K:C[mode%n]=row
 u=np.fft.ifft(C*n,axis=0).real
 du=np.fft.ifft((2j*np.pi*freq[:,None]/period)*(C*n),axis=0).real
 zd=np.fft.ifft((C[:,2]*n)*np.exp(-2j*np.pi*freq*tau/period)).real
 f=np.vstack([rhs(u[i],zd[i]) for i in range(n)]);res=du-f
 RC=np.fft.fft(res,axis=0)/n
 floor=[]
 for row in u:
  deficit=P['q']*row[3]*row[0]-P['r']*row[0]*(1-row[0]/P['K'])*row[1]/(row[1]+P['A0'])
  floor.append(np.log1p(np.exp(np.clip(P['k']*deficit,-700,700)))/P['k']-np.log(2)/P['k']+P['delta'])
 item={'K':K,'residual_inf':float(abs(res).max()),'residual_rms':float(np.sqrt(np.mean(res*res))),'floor_min':float(min(floor)),'weights':{}}
 for nu in [1.05,1.10,1.15]:
  seedmask=np.abs(freq)<=K;resmask=np.abs(freq)<=2*K
  ws=nu**np.abs(freq[seedmask]);wr=nu**np.abs(freq[resmask])
  item['weights'][str(nu)]={'seed_l1nu':[float(np.sum(np.abs(C[seedmask,j])*ws)) for j in range(4)],'residual_l1nu_truncated_2K':[float(np.sum(np.abs(RC[resmask,j])*wr)) for j in range(4)]}
 results.append(item)
out={'period':period,'decay_fit_k10_70':decay,'diagnostics':results,'recommendation':'Use finite seed K=80 and begin interval CAP tests with nu=1.05. Modes beyond about 80 approach numerical noise; no analytic tail is inferred from them. Weighted residual diagnostics are truncated to |k|<=2K and are not radii-polynomial Y bounds.'}
(root/'c4_fourier_weight_diagnostics.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
