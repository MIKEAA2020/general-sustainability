#!/usr/bin/env python3
"""Discrete-method-of-steps monodromy for the gated Candidate-A C4 cycle.

Computes the full spectrum of the finite-dimensional RK4 history discretization.
This is convergence evidence, not a rigorous enclosure of the RFDE spectrum.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np
from c4_cycle_naim import P, softplus


def jac(cur,zdel,p=P):
    N,A,Z,E=cur; fac=A/(A+p['A0'])
    RN=p['r']*(1-2*N/p['K'])*fac
    RA=p['r']*N*(1-N/p['K'])*p['A0']/(A+p['A0'])**2
    BN=RN+p['kappaA']*fac
    BA=RA+p['kappaA']*N*p['A0']/(A+p['A0'])**2
    deficit=p['q']*E*N-p['r']*N*(1-N/p['K'])*fac
    sig=1/(1+np.exp(-np.clip(p['k']*deficit,-700,700)))
    margin=softplus(deficit,p['k'])-np.log(2)/p['k']+p['delta']
    if margin<=0: raise RuntimeError('orbit touches nonsmooth floor')
    J=np.zeros((4,4)); D=np.zeros((4,4))
    J[0]=[RN-p['q']*E,RA,0,-p['q']*N]
    J[1]=[-BN,-BA-p['omegaA'],0,0]
    J[2]=[sig*(p['q']*E-RN)/p['taum'],-sig*RA/p['taum'],-1/p['taum'],sig*p['q']*N/p['taum']]
    H=p['eta']*E*(zdel/p['Dref']-E/p['Emax'])+p['delta0']*zdel/(p['Zref']+zdel)
    J[3,3]=-H/p['Emax']+(1-E/p['Emax'])*p['eta']*(zdel/p['Dref']-2*E/p['Emax'])
    D[3,2]=(1-E/p['Emax'])*(p['eta']*E/p['Dref']+p['delta0']*p['Zref']/(p['Zref']+zdel)**2)
    return J,D

def maxima_indices(x):
    N=x[:,0];return np.where((N[1:-1]>N[:-2])&(N[1:-1]>=N[2:]))[0]+1

def monodromy(npz):
    dat=np.load(npz,allow_pickle=True);t=dat['t'];x=dat['x'];dt=float(dat['dt']);tau=float(dat['tau'])
    d=int(round(tau/dt)); ii=maxima_indices(x); start,end=ii[-2],ii[-1]; nper=end-start
    if start<d:raise RuntimeError('not enough prehistory')
    base=x[start-d:end+1] # indices 0..d+nper
    dim=4*(d+1); V=np.zeros((d+nper+1,4,dim))
    V[:d+1]=np.eye(dim).reshape(d+1,4,dim)
    for i in range(nper):
        cur=base[d+i]; nxt=base[d+i+1]; half=.5*(cur+nxt)
        z0=base[i,2];z1=base[i+1,2];zh=.5*(z0+z1)
        v=V[d+i]; vd0=V[i];vd1=V[i+1];vdh=.5*(vd0+vd1)
        J1,D1=jac(cur,z0); k1=J1@v+D1@vd0
        J2,D2=jac(half,zh); k2=J2@(v+.5*dt*k1)+D2@vdh
        k3=J2@(v+.5*dt*k2)+D2@vdh
        J4,D4=jac(nxt,z1); k4=J4@(v+dt*k3)+D4@vd1
        V[d+i+1]=v+dt*(k1+2*k2+2*k3+k4)/6
    M=V[nper:nper+d+1].reshape(dim,dim)
    eig=np.linalg.eigvals(M); order=np.argsort(-np.abs(eig));eig=eig[order]
    # phase multiplier nearest 1
    phase=int(np.argmin(np.abs(eig-1)))
    non=np.delete(eig,phase); rho=float(np.max(np.abs(non)))
    result=dict(dt=float(dt),tau=float(tau),delay_steps=int(d),period_steps=int(nper),period=float(nper*dt),dimension=int(dim),
                phase_multiplier=[float(eig[phase].real),float(eig[phase].imag)],
                phase_error=float(abs(eig[phase]-1)),dominant_nontrivial_modulus=rho,
                normal_exponent=float(-np.log(rho)/(nper*dt)) if 0<rho<1 else None,
                count_modulus_ge_1=int(np.sum(np.abs(non)>=1)),
                top_multipliers=[dict(real=float(z.real),imag=float(z.imag),modulus=float(abs(z))) for z in eig[:20]])
    return M,eig,result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('npz');ap.add_argument('--out',default='c4_floquet')
    a=ap.parse_args();M,e,r=monodromy(a.npz);base=Path(a.out)
    np.savez_compressed(base.with_suffix('.npz'),M=M,eigenvalues=e)
    base.with_suffix('.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
if __name__=='__main__':main()
