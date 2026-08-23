#!/usr/bin/env python3
"""Rightmost characteristic roots of Candidate-A C4 equilibrium by MOL convergence."""
import json
from pathlib import Path
import numpy as np
from scipy.sparse import lil_matrix,csc_matrix
from scipy.sparse.linalg import eigs
from c4_cycle_naim import EQ,P
from c4_floquet_discrete import jac

def generator(tau,m):
    h=tau/m;n=4*(m+1);A=lil_matrix((n,n),dtype=float)
    I=np.eye(4)
    for j in range(m):
        A[4*j:4*j+4,4*j:4*j+4]=-I/h
        A[4*j:4*j+4,4*(j+1):4*(j+1)+4]=I/h
    J,D=jac(EQ,EQ[2])
    A[4*m:4*m+4,4*m:4*m+4]=J
    A[4*m:4*m+4,0:4]=D
    return csc_matrix(A)

def main():
    out=[]
    for m in [50,100,200,400]:
        A=generator(4.5,m);v=eigs(A,k=16,which='LR',return_eigenvectors=False,tol=1e-10,maxiter=200000)
        v=v[np.argsort(-v.real)]
        out.append({'m':m,'dimension':4*(m+1),'rightmost_roots':[{'real':float(z.real),'imag':float(z.imag)} for z in v[:12]],'spectral_abscissa':float(v.real.max())})
        print(m,v[:6])
    Path('c4_equilibrium_tau4p5_spectrum.json').write_text(json.dumps({'tau':4.5,'method':'upwind method-of-lines generator; convergence evidence only','levels':out},indent=2))
if __name__=='__main__':main()
