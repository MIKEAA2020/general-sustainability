"""Exact tether equilibrium criterion plus an explicit interval-checked example.
All auxiliary parameters are illustrative model choices, not field estimates.
The old unparameterized 5.9 ratio is not used or fitted.
"""
from pathlib import Path
import json
from mpmath import mp,iv
from interval_decimal_v42 import outward_bounds
ROOT=Path(__file__).resolve().parents[1]

def functions(ctx,E):
    f=lambda s:ctx.mpf(str(s));r,K,q,eta,M,delta0,tm=f('.02'),f(100),f('.001'),f('.914'),f(30),f('.01'),f(5)
    z=ctx.log(f(2))/10;dk,cost,K0,mu=f('.1'),f('.01'),f('.1'),f('.02');N=K*(1-q*E/r);cap=q*E*N/(dk+cost*E);B=eta*E*(z-E/M)+delta0*z/(1+z);gate=1-E/M;s=1-ctx.exp(-cap/K0)
    G=gate*s*B/E
    capprime=(q*(N-q*K*E/r)*(dk+cost*E)-q*E*N*cost)/(dk+cost*E)**2
    Bprime=eta*(z-2*E/M)
    Gprime=-s*B/(M*E)+gate*ctx.exp(-cap/K0)*capprime*B/(K0*E)+gate*s*Bprime/E-gate*s*B/E**2
    an=-r*N/K;ae=-q*N
    J=ctx.matrix([[an,0,ae,0],[-an/(2*tm),-1/tm,-ae/(2*tm),0],[0,gate*s*(eta*E+delta0/(1+z)**2),-s*B/M+gate*s*Bprime-mu,gate*ctx.exp(-cap/K0)*B/K0],[q*E,0,q*N-cost*cap,-dk-cost*E]])
    return G-mu,Gprime,J,N,cap

def poly_coeff(ctx,J):
    I=ctx.eye(4);B=I;coeff=[]
    for k in range(1,5):
        product=J*B;c=-sum(product[i,i]for i in range(4))/k;coeff.append(c);B=product+c*I
    return coeff

def run():
    mp.dps=85;iv.dps=75;records=[]
    for bracket in [('.02','.04'),('1.3','1.5')]:
        root=mp.findroot(lambda E:functions(mp,E)[0],tuple(map(mp.mpf,bracket)));pad=mp.mpf('1e-30');lo,hi=root-pad,root+pad
        box=iv.mpf([str(lo),str(hi)]);fl=functions(iv,iv.mpf(str(lo)))[0];fh=functions(iv,iv.mpf(str(hi)))[0];ff,der,J,N,cap=functions(iv,box)
        def lower(x):return mp.mpf(x._mpi_[0])
        def upper(x):return mp.mpf(x._mpi_[1])
        if not((upper(fl)<0 and lower(fh)>0)or(lower(fl)>0 and upper(fh)<0)):raise ValueError('No interval endpoint sign change')
        if lower(der)<=0<=upper(der):raise ValueError('Scalar root simplicity failed')
        a1,a2,a3,a4=poly_coeff(iv,J);h2=a1*a2-a3;h3=a1*a2*a3-a3*a3-a1*a1*a4
        if lower(a4)>0:
            if not all(lower(x)>0 for x in [a1,a2,a3,a4,h2,h3]):raise ValueError('Upper equilibrium not interval Hurwitz')
            status='all four eigenvalues in the open left half-plane at tau=0'
        else:
            b=h2/a1;c=(b*a3-a1*a4)/b
            if not(lower(a1)>0 and lower(b)>0 and lower(c)>0 and upper(a4)<0):raise ValueError('Routh count not certified')
            status='exactly one eigenvalue in the open right half-plane at tau=0 (Routh count)'
        records.append({'E_enclosure':outward_bounds(box),'N_enclosure':outward_bounds(N),'capital_enclosure':outward_bounds(cap),'scalar_derivative':outward_bounds(der),'characteristic_coefficients':[outward_bounds(x)for x in [a1,a2,a3,a4]],'Hurwitz_second_minor':outward_bounds(h2),'Hurwitz_third_minor':outward_bounds(h3),'spectrum_statement':status})
    z=iv.log(iv.mpf(2))/10;alpha=iv.mpf('.001')*100*iv.mpf('.01')*z/(iv.mpf('.1')*iv.mpf('.1')*(1+z))
    # Independent high-precision Jacobian differentiation at the upper equilibrium.
    E=mp.mpf(records[-1]['E_enclosure'][0]);_,_,J,N,C=functions(mp,E);zz=mp.log(2)/10;x=mp.matrix([N,zz,E,C])
    def rhs(x):
        n,z,e,c=x;deficit=mp.mpf('.001')*e*n-mp.mpf('.02')*n*(1-n/100)
        return mp.matrix([-deficit,(mp.log(1+mp.exp(10*deficit))/10-z)/5,(1-e/30)*(1-mp.exp(-c/mp.mpf('.1')))*(mp.mpf('.914')*e*(z-e/30)+mp.mpf('.01')*z/(1+z))-mp.mpf('.02')*e,mp.mpf('.001')*e*n-c*(mp.mpf('.1')+mp.mpf('.01')*e)])
    Jad=mp.matrix(4);errors=[]
    for j in range(4):
        v=mp.matrix([int(i==j)for i in range(4)])
        for i in range(4):Jad[i,j]=mp.diff(lambda t:rhs(x+t*v)[i],0)
    error=max(abs(Jad[i,j]-J[i,j])for i in range(4)for j in range(4))
    if error>mp.mpf('1e-28'):raise ValueError('Analytic tether Jacobian failed')
    out={'status':'Illustrative full four-state bistability at tau=0, verified by scalar interval root signs and interval Routh-Hurwitz tests; no field calibration','auxiliary_parameters':{'delta_K':'.1','c_E':'.01','K0':'.1','mu_E':'.02'},'other_parameters':'Registered Candidate A stock/memory/mobilising bracket','alpha':outward_bounds(alpha),'zero_effort_equilibrium':'N=K,Z=delta,E=0,capital=0; stable for mu_E>alpha, independently of delay','extinction_point':'N=0,Z=delta,E=0,capital=0; eigenvalue +r, hence not an interior attractor','positive_equilibria':records,'independent_Jacobian_max_error':str(error),'not_claimed':['a global basin separator','the unparameterized 5.9 alpha ratio','a measured institutional Allee effect','unchanged Hopf or fold thresholds after adding the tether']}
    (ROOT/'data/tether_equilibria_v42.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));return out
if __name__=='__main__':run()
