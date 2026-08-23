#!/usr/bin/env python3
"""Candidate-A gated C4 DDE: orbit search and reproducible diagnostics.

This is a new local reproduction attempt for the A018-to-A021 crosswalk.
It does not replace the user-attested A018 computations and does not certify
an infinite-dimensional Floquet spectrum.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np

P = dict(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0,
         delta0=0.01, Dref=1.0, taum=5.0, k=10.0,
         delta=np.log(2)/10, Zref=1.0, omegaA=1e-3,
         kappaA=0.05, A0=1.0, Aeq_intrinsic=50.0)
P['AeqW'] = P['Aeq_intrinsic'] + P['kappaA']*P['K']/P['omegaA']
EQ = np.array([89.52562, 397.8665, np.log(2)/10, 2.08962])

def softplus(x, k):
    z=k*x
    if z>40: return x
    if z<-40: return np.exp(z)/k
    return np.log1p(np.exp(z))/k

def rhs(cur, zdel, p=P):
    N,A,Z,E=cur
    R=p['r']*N*(1-N/p['K'])*A/(A+p['A0'])
    B=R+p['kappaA']*N*A/(A+p['A0'])
    deficit=p['q']*E*N-R
    mem=max(0.0, softplus(deficit,p['k'])-np.log(2)/p['k']+p['delta'])
    return np.array([
      R-p['q']*E*N,
      -B+p['omegaA']*(p['AeqW']-A),
      (mem-Z)/p['taum'],
      (1-E/p['Emax'])*(p['eta']*E*(zdel/p['Dref']-E/p['Emax'])
       +p['delta0']*zdel/(p['Zref']+zdel))
    ])

def simulate(tau=4.5, dt=0.05, horizon=50000.0, x0=None):
    delay_steps=tau/dt
    if abs(delay_steps-round(delay_steps))>1e-10:
        raise ValueError('choose dt dividing tau')
    d=int(round(delay_steps)); n=int(round(horizon/dt))
    x0=np.array(x0 if x0 is not None else [25.,300.,0.5,10.],float)
    # ring plus full retained output at moderate stride
    hist=np.tile(x0,(d+1,1)); out_stride=1
    out_t=[]; out=[]
    cur=x0.copy()
    for i in range(n):
        idx=i%(d+1)
        # hist[(i-d) mod] is delayed state; intermediate delayed values linearly interpolated
        zd0=hist[(i-d)%(d+1),2]
        zdhalf=0.5*(hist[(i-d)%(d+1),2]+hist[(i-d+1)%(d+1),2])
        zd1=hist[(i-d+1)%(d+1),2]
        k1=rhs(cur,zd0)
        k2=rhs(cur+0.5*dt*k1,zdhalf)
        k3=rhs(cur+0.5*dt*k2,zdhalf)
        k4=rhs(cur+dt*k3,zd1)
        nxt=cur+dt*(k1+2*k2+2*k3+k4)/6
        hist[(i+1)%(d+1)]=nxt
        cur=nxt
        if (i+1)%out_stride==0:
            out_t.append((i+1)*dt);out.append(cur.copy())
        if not np.all(np.isfinite(cur)):
            raise RuntimeError(f'nonfinite at {i*dt}')
    return np.asarray(out_t),np.asarray(out)

def diagnostics(t,x,tail=10000.0):
    mask=t>=t[-1]-tail; tt=t[mask]; xx=x[mask]; N=xx[:,0]
    # maxima by three-point test
    ii=np.where((N[1:-1]>N[:-2])&(N[1:-1]>=N[2:]))[0]+1
    mt=tt[ii]; mv=N[ii]
    periods=np.diff(mt)
    return dict(
      tail_start=float(tt[0]), samples=int(len(tt)),
      ranges={name:[float(xx[:,j].min()),float(xx[:,j].max())]
              for j,name in enumerate(['N','A','Z','E'])},
      maxima_count=int(len(ii)),
      period_mean=float(periods[-20:].mean()) if len(periods)>=1 else None,
      period_sd=float(periods[-20:].std()) if len(periods)>=1 else None,
      maxima_last=[float(v) for v in mv[-10:]],
      floor_margin=float(np.min([softplus(P['q']*row[3]*row[0]-P['r']*row[0]*(1-row[0]/P['K'])*row[1]/(row[1]+P['A0']),P['k'])-np.log(2)/P['k']+P['delta'] for row in xx]))
    )

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--tau',type=float,default=4.5)
    ap.add_argument('--dt',type=float,default=.05);ap.add_argument('--horizon',type=float,default=50000)
    ap.add_argument('--tail',type=float,default=10000);ap.add_argument('--out',default='c4_tau4p5')
    a=ap.parse_args(); t,x=simulate(a.tau,a.dt,a.horizon)
    base=Path(a.out); np.savez_compressed(base.with_suffix('.npz'),t=t,x=x,params=P,tau=a.tau,dt=a.dt)
    d=diagnostics(t,x,a.tail); d.update(tau=a.tau,dt=a.dt,horizon=a.horizon,initial=[25.,300.,.5,10.])
    base.with_suffix('.json').write_text(json.dumps(d,indent=2)); print(json.dumps(d,indent=2))
if __name__=='__main__':main()
