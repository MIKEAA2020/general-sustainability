"""Interval constants for the nonlinear global-basin theorem.
The proof is an asymptotic-gain argument, not a parameter/cadence scan.
"""
from pathlib import Path
import json,sys
from mpmath import mp,iv
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'inherited_v42/src'))
from interval_decimal_v42 import outward_bounds

def run():
    mp.dps=90;iv.dps=80;f=lambda x:iv.mpf(str(x));delta=iv.log(f(2))/10;M=f(30);eta=f('.914');aa=M*delta;bb=M*f('.01')*delta/(eta*(1+delta));E=(aa+iv.sqrt(aa*aa+4*bb))/2;E0=E*(1+delta)
    s=f('.001')*E0/f('.02');nb=100*(1-s);gain=f('.001')*100*E0*(1+100/nb)
    r=iv.mpf(['.018','.022']);K=iv.mpf(['90','110']);q=iv.mpf(['.0009','.0011']);es=iv.mpf(['1.8','2.4']);z=iv.mpf(['.06','.08']);e0=es*(1+z);fraction=1-q*e0/r;boxgain=q*K*e0*(1+1/fraction)
    def upper(x):return mp.mpf(x._mpi_[1])
    def lower(x):return mp.mpf(x._mpi_[0])
    if not(lower(fraction)>0 and upper(gain)<1 and upper(boxgain)<1):raise ValueError('Global gain certificate failed')
    out={'theorem':'Complete protective equilibrium basin relative to physical nonnegative bounded-history state space','assumptions':['nonnegative globally 1-Lipschitz memory source Phi, Phi(0)=delta','C(Z)=E0 Zref/(Zref+Z), E0<Emax','q E0<r','Gamma=q K (E0/Zref) [1+1/(1-q E0/r)]<1','eta_p>0, tau_m>0; every fixed finite latency and positive fixed cadence'],'basin':'N(0)>0 and E(0)<Emax, with physical nonnegative bounded Z history; E(0)=0 and N(0)=K are allowed','excluded_boundary_faces':['N(0)=0: stock remains zero','E(0)=Emax: effort remains Emax for continuous/native/exact nonlinear quota relaxation'],'operators':['continuous protective deployment delay','native sampled/held signal with finite additional latency','exact nonlinear frozen-effort quota review'],'not_transferred':['mobilising law','mixed channels','explicit-Euler command map','arbitrary asymptotically unbounded latency/cadence'],'E0':outward_bounds(E0),'N_b':outward_bounds(nb),'global_gain':outward_bounds(gain),'parameter_box_global_gain':outward_bounds(boxgain),'parameter_box_positive_stock_fraction':outward_bounds(fraction),'parameter_box':{'r':[.018,.022],'K':[90,110],'q':[.0009,.0011],'E_star':[1.8,2.4],'delta':[.06,.08],'Emax':[26,34],'Zref':1,'eta_p':'any >0','tau_m':'any >0','memory':'e.g. softplus with kappa=log(2)/delta'},'consequences':['global convergence to the unique positive protective equilibrium for every history in the stated basin','no nonconstant periodic or other non-equilibrium omega-limit set in that basin','no global uniform convergence rate as initial effort approaches Emax or latency/cadence tend to infinity'],'certification':'analytical theorem with outward interval verification of constants; not a mobilising periodic-orbit Floquet certificate'}
    (ROOT/'data/global_protective_basin_v43.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));return out
if __name__=='__main__':run()
