#!/usr/bin/env python3
"""High-precision argument-principle count for C4 equilibrium roots.

Combines an analytic exterior norm bound with mesh-converged high-precision
winding counts. This is strong numerical certification, not interval arithmetic.
"""
import json
from pathlib import Path
import numpy as np
import mpmath as mp
from c4_cycle_naim import EQ
from c4_floquet_discrete import jac

TAU=10.0
J,D=jac(EQ,EQ[2])
mp.mp.dps=70
JM=mp.matrix([[mp.mpf(str(v)) for v in row] for row in J])
DM=mp.matrix([[mp.mpf(str(v)) for v in row] for row in D])
I=mp.eye(4)

def det(z): return mp.det(z*I-JM-DM*mp.e**(-z*TAU))

def contour(a,R,n):
    # counterclockwise rectangle [a,R] x [-R,R]
    pts=[]
    def add(z0,z1):
        for k in range(n):pts.append(z0+(z1-z0)*mp.mpf(k)/n)
    add(a-1j*R,R-1j*R);add(R-1j*R,R+1j*R);add(R+1j*R,a+1j*R);add(a+1j*R,a-1j*R)
    pts.append(pts[0]);return pts

def count(a,R,n):
    vals=[det(z) for z in contour(mp.mpf(str(a)),mp.mpf(str(R)),n)]
    angles=[]; total=mp.mpf('0');maxinc=0
    for x,y in zip(vals[:-1],vals[1:]):
        inc=mp.arg(y/x);total+=inc;maxinc=max(maxinc,abs(float(inc)))
    return int(mp.nint(total/(2*mp.pi))),float(total/(2*mp.pi)),maxinc,float(min(abs(v) for v in vals))

def main():
    a_values=[0.0,-0.0005,-0.0006,-0.0007,-0.0010,-0.0011]
    # Exterior root exclusion for Re z>=a and |z| > ||J||+||D||exp(-a*tau)
    out=[]
    for a in a_values:
        bound=float(np.linalg.norm(J,2)+np.linalg.norm(D,2)*np.exp(-a*TAU));R=bound+0.15
        levels=[]
        for n in [2000,4000,8000,16000]:
            c,w,mi,md=count(a,R,n);levels.append({'edge_samples':n,'count':c,'winding':w,'max_phase_increment':mi,'min_sampled_det_modulus':md})
        out.append({'left_boundary':a,'analytic_exterior_radius':bound,'rectangle_radius':R,'levels':levels})
        print(a,bound,levels[-1])
    Path('c4_slack_tau10_argument_count.json').write_text(json.dumps({'tau':TAU,'norm_J':float(np.linalg.norm(J,2)),'norm_D':float(np.linalg.norm(D,2)),'method':'analytic exterior Neumann bound plus 70-digit mesh-converged argument principle; not interval arithmetic','counts':out},indent=2))
if __name__=='__main__':main()
