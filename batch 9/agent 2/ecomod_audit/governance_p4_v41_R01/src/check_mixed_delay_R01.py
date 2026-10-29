"""Independent mixed-channel check of Eq. (9), including interval Krawczyk
inclusions for one characteristic root at each of two protective delays.
This does not certify an entire infinite characteristic spectrum.
"""
from pathlib import Path
import json
import numpy as np
from mpmath import mp, iv
from interval_decimal_R01 import outward_bounds
from verify_governance_R01 import coefficients, protective
ROOT=Path(__file__).resolve().parents[1]

def exact_coeffs(ctx):
    c=lambda s:ctx.mpf(str(s))
    r,K,q,eta,emax,d0,tm=map(c,['.02','100','.001','.914','30','.01','5'])
    z=ctx.log(c(2))/10;a=emax*z;b=emax*d0*z/(eta*(1+z));E=(a+ctx.sqrt(a*a+4*b))/2;N=K*(1-q*E/r);g=1-E/emax
    return -r*N/K,1/tm,q*N/(2*tm),g*eta*(z-2*E/emax),-g*eta,g*(eta*E+d0/(1+z)**2),-g*eta*E/(1+z)

def run():
    mp.dps=90;iv.dps=80
    def model(ctx,tp):
        AN,d,BE,ceM,ceP,czM,czP=exact_coeffs(ctx);chi=ctx.mpf('.9988');ce=chi*ceM+(1-chi)*ceP;cm=chi*czM;cp=(1-chi)*czP;tm=ctx.mpf('0');tp=ctx.mpf(str(tp))
        def f(l):return (l-AN)*(l+d)*(l-ce)-BE*l*(cm*ctx.exp(-l*tm)+cp*ctx.exp(-l*tp))
        def df(l):return (l+d)*(l-ce)+(l-AN)*(l-ce)+(l-AN)*(l+d)-BE*(cm*ctx.exp(-l*tm)*(1-l*tm)+cp*ctx.exp(-l*tp)*(1-l*tp))
        return f,df
    def lo(x):return mp.mpf(x._mpi_[0])
    def hi(x):return mp.mpf(x._mpi_[1])
    records=[]
    for tp in [0,110]:
        f,df=model(mp,tp);fi,dfi=model(iv,tp);z=mp.findroot(f,mp.mpc('-0.000057'if tp==0 else'.000006','.0279'))
        vals=[mp.re(z),mp.im(z)];eps=mp.mpf('1e-18');X=[iv.mpf([str(v-eps),str(v+eps)])for v in vals];cent=[iv.mpf(str(v))for v in vals];zc=iv.mpc(*cent);zx=iv.mpc(*X)
        f0=fi(zc);D=dfi(zx);der=df(z);aa,bb=mp.re(der),mp.im(der);den=aa*aa+bb*bb
        C=[[iv.mpf(str(aa/den)),iv.mpf(str(bb/den))],[iv.mpf(str(-bb/den)),iv.mpf(str(aa/den))]]
        J=[[iv.re(D),-iv.im(D)],[iv.im(D),iv.re(D)]];F=[iv.re(f0),iv.im(f0)]
        B=[[int(i==j)-sum(C[i][k]*J[k][j]for k in range(2))for j in range(2)]for i in range(2)]
        K=[cent[i]-sum(C[i][j]*F[j]for j in range(2))+sum(B[i][j]*(X[j]-cent[j])for j in range(2))for i in range(2)]
        inclusion=all(lo(K[i])>lo(X[i])and hi(K[i])<hi(X[i])for i in range(2))
        contraction_bound=max(sum(max(abs(lo(B[i][j])),abs(hi(B[i][j])))for j in range(2))for i in range(2))
        if not(inclusion and contraction_bound<1):raise ValueError('Mixed-delay root Krawczyk inclusion/contraction failed')
        def bounds(v):return outward_bounds(v)
        records.append({'protective_delay_years':tp,'point_root':[mp.nstr(v,55)for v in vals],'test_box_Re':bounds(X[0]),'test_box_Im':bounds(X[1]),'krawczyk_Re':bounds(K[0]),'krawczyk_Im':bounds(K[1]),'strict_krawczyk_inclusion':bool(inclusion),'contraction_norm_upper_bound':outward_bounds(iv.mpf(str(contraction_bound)))[1],'root_certified_in_right_half_plane':bool(lo(X[0])>0),'root_certified_in_left_half_plane':bool(hi(X[0])<0)})
    c=coefficients();p=protective();chi=.9988;ce=chi*c['CE']+(1-chi)*p['CE'];cm=chi*c['CZ'];cp=(1-chi)*p['CZ'];BE=c['BE'];AN=c['AN'];d=c['d'];P=np.poly1d(np.poly([AN,-d,ce]));a2,a1,a0=P.c[1:];q1=a1-cm*BE
    H=[1,a2*a2-2*q1,q1*q1-2*a0*a2-(cp*BE)**2,a0*a0];crossings=[]
    for x in sorted(z.real for z in np.roots(H)if abs(z.imag)<1e-11 and z.real>0):
        w=np.sqrt(x);l=1j*w;Q=P(l)-cm*BE*l;t=(-np.angle(Q/(cp*BE*l)))%(2*np.pi)/w
        Qprime=np.polyder(P)(l)-cm*BE;derivative=-l*Q/(Qprime-Q/l+t*Q)
        crossings.append({'omega':w,'tau_p_fundamental':float(t),'dRe_dtau_p':float(derivative.real),'next_same_family':float(t+2*np.pi/w)})
    ANi,di,BEi,ceMi,cePi,czMi,czPi=exact_coeffs(iv);ch=iv.mpf('.9988');cei=ch*ceMi+(1-ch)*cePi;cmi=ch*czMi;cpi=(1-ch)*czPi
    a2i=di-ANi-cei;a1i=ANi*cei-di*(ANi+cei)-BEi*(cmi+cpi);a0i=ANi*di*cei
    margins=[a2i,a1i,a0i,a2i*a1i-a0i];hurwitz=all(lo(v)>0 for v in margins)
    if not hurwitz:raise ValueError('Undelayed mixed cubic is not certified Hurwitz')
    def peak(t):
        from scipy.optimize import brentq
        ce=t*c['CE']+(1-t)*p['CE'];G=t*c['CZ']-(1-t)*p['CZ'];s1=AN*AN+d*d+ce*ce;s3=AN*AN*d*d*ce*ce
        x=brentq(lambda x:2*x**3+s1*x*x-s3,1e-12,10,xtol=1e-18)
        return G*BE*np.sqrt(x)/np.sqrt((x+AN*AN)*(x+d*d)*(x+ce*ce))
    from scipy.optimize import brentq
    def routh_margin(t):
        ce=t*c['CE']+(1-t)*p['CE'];g=t*c['CZ']+(1-t)*p['CZ'];v=np.poly([AN,-d,ce]);v[-2]-=g*BE;return v[1]*v[2]-v[3]
    result={'chi_m_exact_decimal':'.9988','chi_p_exact_decimal':'.0012','tau_M_exact_decimal_years':'0','eta_p_exact_decimal':'.914','scope':'Counterexample to the extra claim of protective-delay independence OUTSIDE the weighted-small-gain certificate. The valid certificate itself is not contradicted.','roots':records,'tau_M_tau_p_zero':{'hurwitz_interval_certified':bool(hurwitz),'routh_margins_a2_a1_a0_a2a1_minus_a0':[outward_bounds(v)for v in margins],'undelayed_roots_float':[[float(z.real),float(z.imag)]for z in np.roots(P-np.poly1d([(cm+cp)*BE,0]))]},'single_delay_tau_M_0':{'positive_frequency_crossings_float':crossings,'note':'The floating-point crossing calculation additionally places destabilisation near tau_p=86.0259 and restabilisation near 132.0765 years; the next recurrent crossing is later. These crossing locations are not interval-enclosed here.'},'weighted_small_gain':{'F_at_witness':float(peak(.9988)),'F_equals_1_weight_float':float(brentq(lambda t:peak(t)-1,0,1,xtol=1e-15)),'undelayed_routh_boundary_weight_float':float(brentq(routh_margin,0,1,xtol=1e-15)),'maximisation_identity':'For fixed chi, x=omega^2 maximises x/[(x+a^2)(x+d^2)(x+CE^2)] at the unique positive root 2x^3+(a^2+d^2+CE^2)x^2-a^2*d^2*CE^2=0. The numerical chi boundaries are not interval certificates.'},'arithmetic':'mpmath.iv 80 decimal digits; exact registered decimal parameters; independent 2x2 real Krawczyk calculation and cubic Routh margins','important_limit':'At tau_p=0 the finite undelayed Jacobian is certified Hurwitz; at tau_p=110 an actual RHP characteristic root is interval-enclosed. This establishes a mixed-channel local stability contrast, not a certified nonlinear Hopf bifurcation.'}
    (ROOT/'data/mixed_delay_check_R01.json').write_text(json.dumps(result,indent=2)+'\n');return result

if __name__=='__main__':print(json.dumps(run(),indent=2))
