#!/usr/bin/env python3
"""Outward interval bounds for C4 smooth-branch derivatives on an orbit box.

Uses mpmath interval arithmetic for vector-field values, Jacobian, and Hessians.
These are rigorous for the stated rectangular box up to mpmath.iv semantics; they
are finite-vector-field bounds, not full Fourier radii-polynomial bounds.
"""
import json
from pathlib import Path
import sympy as s
import mpmath as mp
N,A,Z,E,W=s.symbols('N A Z E W', real=True);x=[N,A,Z,E,W]
r=s.Rational(2,100);K=s.Integer(100);q=s.Rational(1,1000);eta=s.Rational(914,1000);Emax=s.Integer(30);delta0=s.Rational(1,100);Dref=s.Integer(1);taum=s.Integer(5);kk=s.Integer(10);Zref=s.Integer(1);omega=s.Rational(1,1000);kap=s.Rational(5,100);A0=s.Integer(1);Aeq=s.Integer(5050)
R=r*N*(1-N/K)*A/(A+A0);B=R+kap*N*A/(A+A0);deficit=q*E*N-R;sp=s.log(1+s.exp(kk*deficit))/kk
F=s.Matrix([R-q*E*N,-B+omega*(Aeq-A),(sp-Z)/taum,(1-E/Emax)*(eta*E*(W/Dref-E/Emax)+delta0*W/(Zref+W))])
J=F.jacobian(x);Hs=[s.hessian(F[o],x) for o in range(4)]
mods={'exp':mp.iv.exp,'log':mp.iv.log}
ff=[s.lambdify(x,F[o],modules=[mods]) for o in range(4)];spf=s.lambdify(x,sp,modules=[mods]);jf=[[s.lambdify(x,J[o,j],modules=[mods]) for j in range(5)] for o in range(4)];hf=[[[s.lambdify(x,Hs[o][i,j],modules=[mods]) for j in range(5)] for i in range(5)] for o in range(4)]
box={'N':[45,96],'A':[830,950],'Z':[0,0.70],'E':[0.30,21],'W':[0,0.70]};iv=[mp.iv.mpf(box[k]) for k in ['N','A','Z','E','W']]
def ab(v):
 try:return max(abs(float(v.a)),abs(float(v.b)))
 except AttributeError:return abs(float(v))
Fabs=[ab(f(*iv)) for f in ff];Jabs=[[ab(jf[o][j](*iv)) for j in range(5)] for o in range(4)];Habs=[[[ab(hf[o][i][j](*iv)) for j in range(5)] for i in range(5)] for o in range(4)]
# Replace dependency-inflated softplus derivative intervals by structural bounds:
# 0<=sp'<=1 and 0<=sp''<=k/4.
dgrad=s.Matrix([deficit]).jacobian(x);dhess=s.hessian(deficit,x)
dgf=[s.lambdify(x,dgrad[j],modules=[mods]) for j in range(5)];dhf=[[s.lambdify(x,dhess[i,j],modules=[mods]) for j in range(5)] for i in range(5)]
dg=[ab(f(*iv)) for f in dgf];dh=[[ab(dhf[i][j](*iv)) for j in range(5)] for i in range(5)]
Jabs[2]=[dg[j]/float(taum) for j in range(5)];Jabs[2][2]+=1/float(taum)
soft_hess_sum=(float(kk)/4)*(sum(dg)**2)+sum(dh[i][j] for i in range(5) for j in range(5));Hrow2=soft_hess_sum/float(taum)
Hbounds=[sum(Habs[o][i][j] for i in range(5) for j in range(5)) for o in range(4)];Hbounds[2]=Hrow2
out={'box':box,'F_component_abs_bounds':Fabs,'F_inf_bound':max(Fabs),'Jacobian_abs_bounds':Jabs,'Jacobian_inf_operator_bound':max(sum(row) for row in Jabs),'deficit_gradient_abs_bounds':dg,'deficit_Hessian_abs_sum':sum(dh[i][j] for i in range(5) for j in range(5)),'Hessian_bilinear_inf_bounds_by_output':Hbounds,'Hessian_vector_bilinear_inf_bound':max(Hbounds),'floor_argument_lower_bound':float(spf(*iv).a),'status':'outward interval vector-field derivative bounds on stated box; Fourier tail and full collocation Hessian still pending'}
Path(__file__).with_name('c4_interval_derivative_box.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
