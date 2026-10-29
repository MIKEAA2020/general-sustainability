"""Independent RFDE cubic coefficient with explicit characteristic-matrix convention.
Analytic second/third derivatives; right eigenvector has unit Hermitian norm;
left row is normalised by p Delta'(i omega) v = 1. No provider-code imports.
"""
from pathlib import Path
import sys,json
from mpmath import mp,iv
from local_verification_v42 import coefficients,frequency_records
from interval_decimal_v42 import outward_bounds
ROOT=Path(__file__).resolve().parents[1]

def coefficient(ctx,candidate,gated,omega,tau,diagnostics=False):
    f=lambda s:ctx.mpf(str(s));j=ctx.mpc(0,1);eta=f('.914'if candidate=='A'else'2.756');em=f(30 if candidate=='A'else 26)
    r,K,q,k,tm,d0=f('.02'),f(100),f('.001'),f(10),f(5),f('.01');z=ctx.log(f(2))/10;a=em*z;b=em*d0*z/(eta*(1+z));E=(a+ctx.sqrt(a*a+4*b))/2;N=K*(1-q*E/r);AN=-r*N/K;AE=-q*N;BN=-AN/(2*tm);BE=-AE/(2*tm);d=1/tm;g=1-E/em if gated else f(1);CE=g*eta*(z-2*E/em);CZ=g*(eta*E+d0/(1+z)**2)
    w=omega;l=j*w
    D=[q*E-r+2*r*N/K,q*N];D2=[[2*r/K,q],[q,f(0)]]
    def B(u,v):
        out=[-2*r/K*u[0]*v[0]-q*(u[0]*v[2]+u[2]*v[0]),f(0),f(0)]
        for ii,i in enumerate([0,2]):
            for jj,jjindex in enumerate([0,2]):out[1]+=(D2[ii][jj]/2+k*D[ii]*D[jj]/4)/tm*u[i]*v[jjindex]
        bee=-2*eta*(1+z)/em+6*eta*E/em**2 if gated else -2*eta/em
        bez=eta-2*eta*E/em-d0/em/(1+z)**2 if gated else eta
        bzz=-2*d0*g/(1+z)**3
        out[2]=bee*u[2]*v[2]+bez*(u[2]*v[3]+u[3]*v[2])+bzz*u[3]*v[3];return out
    def C(u,v,s):
        out=[f(0),f(0),f(0)]
        for ii,i in enumerate([0,2]):
            for jj,jjindex in enumerate([0,2]):
                for kk,index in enumerate([0,2]):out[1]+=k/(4*tm)*(D2[ii][jj]*D[kk]+D2[ii][kk]*D[jj]+D2[jj][kk]*D[ii])*u[i]*v[jjindex]*s[index]
        eee=6*eta/em**2 if gated else f(0);eez=-2*eta/em if gated else f(0);ezz=2*d0/em/(1+z)**3 if gated else f(0);zzz=6*d0*g/(1+z)**4
        out[2]=eee*u[2]*v[2]*s[2]+eez*(u[2]*v[2]*s[3]+u[2]*v[3]*s[2]+u[3]*v[2]*s[2])+ezz*(u[2]*v[3]*s[3]+u[3]*v[2]*s[3]+u[3]*v[3]*s[2])+zzz*u[3]*v[3]*s[3];return out
    def inverse(s,b):
        e=ctx.exp(-s*tau);G=BE*s/((s-AN)*(s+d));base=b[1]/(s+d)+BN*b[0]/((s-AN)*(s+d));xe=(b[2]+CZ*e*base)/(s-CE-CZ*e*G)
        return [(b[0]+AE*xe)/(s-AN),base+G*xe,xe]
    v=[AE/(l-AN),BE*l/((l-AN)*(l+d)),f(1)];norm=ctx.sqrt(sum(ctx.re(x)**2+ctx.im(x)**2 for x in v));v=[x/norm for x in v]
    pz=CZ*ctx.exp(-l*tau)/(l+d);p=[BN*pz/(l-AN),pz,f(1)];dv=v.copy();dv[2]+=tau*CZ*ctx.exp(-l*tau)*v[1];den=sum(p[i]*dv[i]for i in range(3));p=[x/den for x in p]
    ext=lambda v,s:v+[ctx.exp(-s*tau)*v[1]]
    vc=ext(v,l);vb=[ctx.mpc(ctx.re(x),-ctx.im(x))for x in vc];h20=inverse(2*l,B(vc,vc));h11=inverse(f(0),B(vc,vb));b1=B(vb,ext(h20,2*l));b2=B(vc,ext(h11,f(0)));c3=C(vc,vc,vb);G=sum(p[i]*(c3[i]+b1[i]+2*b2[i])for i in range(3))
    if diagnostics:
        P=(l-AN)*(l+d)*(l-CE);Pp=(l+d)*(l-CE)+(l-AN)*(l-CE)+(l-AN)*(l+d)
        dp=Pp-CZ*BE*ctx.exp(-l*tau)*(1-l*tau);alpha=-CZ*BE*l*l*ctx.exp(-l*tau)/dp
        G2=BE*(2*l)/((2*l-AN)*(2*l+d));d2=2*l-CE-CZ*ctx.exp(-2*l*tau)*G2
        direction=list(map(f,['.3','-.1','.5','.2']))
        return {'l1_physical_time':ctx.re(G)/2,'Delta_prime_modulus_squared':ctx.re(dp)**2+ctx.im(dp)**2,'crossing_derivative_real':ctx.re(alpha),'zero_root_value':(-AN)*d*(-CE),'second_harmonic_resolvent_modulus_squared':ctx.re(d2)**2+ctx.im(d2)**2,'B_directional':B(direction,direction),'C_directional':C(direction,direction,direction)}
    return ctx.re(G)/(2*w)

if __name__=='__main__':
    mp.dps=80;iv.dps=70;records=[]
    for candidate,gated in [('A',True),('B',False)]:
        c=coefficients(candidate,gated)
        for h in frequency_records(c):
            # Refine the scalar cubic and phase with exact decimal parameters.
            eta=mp.mpf('.914'if candidate=='A'else'2.756');em=mp.mpf(30 if candidate=='A'else 26);z=mp.log(2)/10;a=em*z;b=em*mp.mpf('.01')*z/(eta*(1+z));E=(a+mp.sqrt(a*a+4*b))/2;N=100*(1-mp.mpf('.001')*E/mp.mpf('.02'));AN=-mp.mpf('.02')*N/100;d=mp.mpf('.2');BE=mp.mpf('.001')*N/10;gate=1-E/em if gated else 1;CE=gate*eta*(z-2*E/em);CZ=gate*(eta*E+mp.mpf('.01')/(1+z)**2)
            H=lambda x:(x+AN**2)*(x+d**2)*(x+CE**2)-CZ**2*BE**2*x
            x=mp.findroot(H,(h['omega']**2*.999,h['omega']**2*1.001));w=mp.sqrt(x);l=1j*w;angle=mp.arg((l-AN)*(l+d)*(l-CE)/(CZ*BE*l));tau=(-angle+2*mp.pi*(0 if h['tau']<20 else 1))/w
            val=coefficient(mp,candidate,gated,w,tau);records.append({'candidate':candidate,'gated':gated,'omega':str(w),'tau':str(tau),'l1_convention_ReG21_over_2omega':str(val),'l1_physical_time_ReG21_over_2':str(val*w)});print(records[-1],flush=True)
    (ROOT/'data/hopf_cubic_crosscheck_v42.json').write_text(json.dumps({'status':'Independent high-precision normal-form calculation; interval certification not asserted for these point evaluations','normalisation':'unit Hermitian right eigenvector; left row p Delta_prime v=1; l1=Re(G21)/(2 omega)','records':records},indent=2)+'\n')

    base=json.loads((ROOT/'data/local_results_v42.json').read_text())['scalar_interval_checks']['roots'];bounds=[]
    for source in base:
        w=iv.sqrt(iv.mpf(source['x_enclosure']));tau=iv.mpf(source['tau_enclosure']);info=coefficient(iv,'A',True,w,tau,True)
        row={key:outward_bounds(value)for key,value in info.items()if key not in ['B_directional','C_directional']};row.update(tau=source['tau_enclosure'],omega=outward_bounds(w));bounds.append(row)
    for i,row in enumerate(bounds):
        for name in ['l1_physical_time','Delta_prime_modulus_squared','zero_root_value','second_harmonic_resolvent_modulus_squared']:
            if mp.mpf(row[name][0])<=0:raise ValueError('Nondegenerate Hopf hypothesis failed: '+name)
        slope=row['crossing_derivative_real']
        if not(mp.mpf(slope[1])<0 if i==0 else mp.mpf(slope[0])>0):raise ValueError('Crossing is not transverse')
    low_next=iv.mpf(bounds[0]['tau'])+2*iv.pi/iv.mpf(bounds[0]['omega']);upper=iv.mpf(bounds[1]['tau'])
    if not(mp.mpf(low_next._mpi_[0])>mp.mpf(upper._mpi_[1])):raise ValueError('Other frequency family might be resonant')
    (ROOT/'data/hopf_cubic_interval_v42.json').write_text(json.dumps({'status':'Interval checks of classical RFDE Hopf hypotheses: scalar frequencies plus simple/transverse eigenpair plus nonzero physical-time cubic; not a radii-polynomial construction of a branch neighbourhood','arithmetic':'mpmath.iv 70 decimal digits; exact registered decimals; outward serialized endpoints','first_recurrence_lower_family':outward_bounds(low_next),'other_family_separation_verified':True,'records':bounds},indent=2)+'\n')
    # An independent differentiation of the original nonlinear expressions checks B,C.
    c=coefficients();N=mp.mpf(str(c['N']));E=mp.mpf(str(c['E']));z=mp.log(2)/10;v=list(map(mp.mpf,['.3','-.1','.5','.2']))
    # Match the exact-rest parameters used internally, rather than rounded floating output.
    eta=mp.mpf('.914');em=mp.mpf(30);aa=em*z;bb=em*mp.mpf('.01')*z/(eta*(1+z));E=(aa+mp.sqrt(aa*aa+4*bb))/2;N=100*(1-E/20)
    info=coefficient(mp,'A',True,mp.mpf(records[0]['omega']),mp.mpf(records[0]['tau']),True)
    def rhs(t):
        nn=N+t*v[0];zz=z+t*v[1];ee=E+t*v[2];zd=z+t*v[3];renew=mp.mpf('.02')*nn*(1-nn/100);deficit=mp.mpf('.001')*ee*nn-renew
        return [renew-mp.mpf('.001')*ee*nn,(mp.log(1+mp.exp(10*deficit))/10-zz)/5,(1-ee/30)*(eta*ee*(zd-ee/30)+mp.mpf('.01')*zd/(1+zd))]
    checks=[]
    for order,name in [(2,'B_directional'),(3,'C_directional')]:
        errors=[abs(mp.diff(lambda t:rhs(t)[i],0,order)-info[name][i])for i in range(3)];checks.append({'order':order,'max_error':str(max(errors))})
        if max(errors)>mp.mpf('1e-45'):raise ValueError('Derivative formula check failed')
    (ROOT/'data/hopf_derivative_checks_v42.json').write_text(json.dumps({'method':'mpmath high-precision automatic directional differentiation of the original nonlinear expressions, compared with hand-derived B,C','checks':checks},indent=2)+'\n')
