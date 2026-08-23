#!/usr/bin/env python3
"""Storage-hull interval certificate for the finite K=80 collocation system.

Encloses effects of exported one-ULP coefficient/period storage hulls and interval
vector-field evaluation. Does not include the infinite Fourier tail or true orbit ball.
"""
import csv,json
from pathlib import Path
import numpy as np
import mpmath as mp
root=Path(__file__).parent;rows=list(csv.DictReader(open(root/'c4_fourier_coefficients_K80.csv')));states=['N','A','Z','E'];K=80;n=161
modes=sorted(set(int(r['mode']) for r in rows));idx={k:i for i,k in enumerate(modes)};C=np.zeros((n,4),complex);rad=np.zeros((n,4));period=float(rows[0]['period']);plo=np.nextafter(period,-np.inf);phi=np.nextafter(period,np.inf);prad=max(period-plo,phi-period)
for r in rows:
 i=idx[int(r['mode'])];j=states.index(r['state']);re=float(r['real']);im=float(r['imag']);C[i,j]=re+1j*im;rr=max(abs(re-float(r['real_lo_1ulp'])),abs(float(r['real_hi_1ulp'])-re));ri=max(abs(im-float(r['imag_lo_1ulp'])),abs(float(r['imag_hi_1ulp'])-im));rad[i,j]=rr+ri
m=np.array(modes);theta=np.arange(n)/n;V=np.exp(2j*np.pi*np.outer(theta,m));u=(V@C).real;du=(V@((2j*np.pi*m[:,None]/period)*C)).real;phase=np.exp(-2j*np.pi*m*4.5/period);zd=(V@(C[:,2]*phase)).real
urad=rad.sum(0);durad=np.array([np.sum(2*np.pi*np.abs(m)/period*rad[:,j])+prad/period*np.sum(2*np.pi*np.abs(m)/period*np.abs(C[:,j])) for j in range(4)]);zdrad=np.sum(rad[:,2])+prad*np.sum(np.abs(C[:,2])*2*np.pi*np.abs(m)*4.5/period**2)
mp.iv.dps=40
def IV(x,r):return mp.iv.mpf([x-r,x+r])
def bounds(v):return float(v.a),float(v.b)
def Fiv(row,z):
 N,A,Z,E=[IV(row[j],urad[j]) for j in range(4)];W=IV(z,zdrad);r=mp.iv.mpf('0.02');q=mp.iv.mpf('0.001');R=r*N*(1-N/100)*A/(A+1);B=R+mp.iv.mpf('0.05')*N*A/(A+1);d=q*E*N-R;sp=mp.iv.log(1+mp.iv.exp(10*d))/10
 return [R-q*E*N,-B+mp.iv.mpf('0.001')*(5050-A),(sp-Z)/5,(1-E/30)*(mp.iv.mpf('0.914')*E*(W-E/30)+mp.iv.mpf('0.01')*W/(1+W))]
max_res_rad=0;max_res_abs=0
for i in range(n):
 fi=Fiv(u[i],zd[i])
 for j in range(4):
  ri=IV(du[i,j],durad[j])-fi[j];lo,hi=bounds(ri);cen=.5*(lo+hi);radx=.5*(hi-lo);max_res_abs=max(max_res_abs,abs(lo),abs(hi));max_res_rad=max(max_res_rad,radx)
z=np.load(root/'c4_fourier_K80_newton.npz');J=z['J'];R0=z['residual'];Ainv=np.linalg.inv(J);Bnorm=float(np.linalg.norm(Ainv,np.inf));Ycenter=float(np.linalg.norm(Ainv@R0,np.inf));normalized_residual_radius=period*max_res_rad+prad*13.30145;Ybound=Ycenter+Bnorm*normalized_residual_radius
# Jacobian uncertainty from storage hull: input map radius and period/shift variation
input_rad=max(max(urad),zdrad);H=1.9130731764705884;Jf=20.72045933333334;Snorm=1.483;SP=.0552;state_max=max(np.max(np.abs(u)),np.max(np.abs(zd)));deltaJ=period*H*(Snorm**2)*input_rad + prad*Jf*Snorm + period*Jf*(SP*prad)*state_max
Z0stored=2.436322919769105e-7+Bnorm*deltaJ
out={'K':K,'period':period,'period_radius_1ulp':prad,'coefficient_node_radii_by_state':urad.tolist(),'derivative_node_radii_by_state':durad.tolist(),'delayed_Z_radius':float(zdrad),'interval_residual_max_abs':max_res_abs,'interval_residual_max_radius':max_res_rad,'normalized_collocation_residual_radius':normalized_residual_radius,'finite_center_Y':Ycenter,'storage_interval_Y_bound':Ybound,'estimated_J_operator_uncertainty_from_storage_hulls':deltaJ,'storage_interval_Z0_bound':Z0stored,'scope':'one-ULP coefficient/period hull plus interval vector field; excludes infinite tail and orbit validation ball'}
(root/'c4_K80_storage_interval_certificate.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
