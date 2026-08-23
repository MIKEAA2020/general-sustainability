#!/usr/bin/env python3
"""Subdivided outward interval bound for C4 periodic linearization sup norm."""
import json
from pathlib import Path
import sympy as s,mpmath as mp
N,A,E,W=s.symbols('N A E W',real=True);r=s.Rational(2,100);K=s.Integer(100);q=s.Rational(1,1000);eta=s.Rational(914,1000);Emax=s.Integer(30);d0=s.Rational(1,100);A0=s.Integer(1);om=s.Rational(1,1000);kap=s.Rational(5,100)
R=r*N*(1-N/K)*A/(A+A0);B=R+kap*N*A/(A+A0);d=q*E*N-R
row0=[s.diff(R-q*E*N,x) for x in [N,A,E]]
row1=[s.diff(-B+om*(5050-A),x) for x in [N,A,E]]
dg=[s.diff(d,x) for x in [N,A,E]]
H=eta*E*(W-E/Emax)+d0*W/(1+W);g=(1-E/Emax)*H;row3=[s.diff(g,x) for x in [E,W]]
mods={};fs=[[s.lambdify((N,A,E),v,modules=[mods]) for v in row] for row in [row0,row1,dg]];fg=[s.lambdify((E,W),v,modules=[mods]) for v in row3]
def ab(v):
 try:return max(abs(float(v.a)),abs(float(v.b)))
 except:return abs(float(v))
def parts(lo,hi,n):return [(lo+(hi-lo)*i/n,lo+(hi-lo)*(i+1)/n) for i in range(n)]
Nr=parts(45.5,95.1,16);Ar=parts(834,944,12);Er=parts(.34,20.1,20);Wr=parts(.001,0.68,30)
maxrows=[0,0,0,0]
for nb in Nr:
 for abox in Ar:
  for eb in Er:
   iv=[mp.iv.mpf(nb),mp.iv.mpf(abox),mp.iv.mpf(eb)]
   maxrows[0]=max(maxrows[0],sum(ab(f(*iv)) for f in fs[0]))
   maxrows[1]=max(maxrows[1],sum(ab(f(*iv)) for f in fs[1]))
   # memory row: sp'<=1 and -Z/taum
   maxrows[2]=max(maxrows[2],.2+sum(ab(f(*iv)) for f in fs[2])/5)
for eb in Er:
 for wb in Wr:
  iv=[mp.iv.mpf(eb),mp.iv.mpf(wb)]
  maxrows[3]=max(maxrows[3],sum(ab(f(*iv)) for f in fg))
out={'box':{'N':[45.5,95.1],'A':[834,944],'E':[.34,20.1],'W':[.001,.68]},'subdivisions':{'N':16,'A':12,'E':20,'W':30},'Jacobian_row_sum_bounds':maxrows,'periodic_linearization_sup_bound':max(maxrows),'status':'outward interval subdivided pointwise Jacobian bound; sp-prime structural bound used'}
Path(__file__).with_name('c4_tight_jacobian_interval.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
