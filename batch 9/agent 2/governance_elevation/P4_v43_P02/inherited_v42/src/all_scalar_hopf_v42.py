"""Outward enclosures for both candidates and both gating variants.
Positive scalar roots are certified by endpoint signs and monotonic derivative.
B ungated additionally receives the explicit nonlinear cubic verification.
"""
from pathlib import Path
import json
from mpmath import mp,iv
from local_verification_v42 import coefficients,frequency_records
from interval_decimal_v42 import outward_bounds
from hopf_cubic_v42 import coefficient
ROOT=Path(__file__).resolve().parents[1]
def run():
    mp.dps=90;iv.dps=80;rows=[];bc=[]
    def lo(x):return mp.mpf(x._mpi_[0])
    def hi(x):return mp.mpf(x._mpi_[1])
    for candidate in ['A','B']:
      for gated in [True,False]:
        f=lambda s:iv.mpf(str(s));eta=f('.914'if candidate=='A'else'2.756');M=f(30 if candidate=='A'else 26);z=iv.log(f(2))/10;a=M*z;b=M*f('.01')*z/(eta*(1+z));E=(a+iv.sqrt(a*a+4*b))/2;N=100*(1-E/20);AN=-f('.02')*N/100;d=f('.2');BE=f('.001')*N/10;g=1-E/M if gated else f(1);CE=g*eta*(z-2*E/M);CZ=g*(eta*E+f('.01')/(1+z)**2)
        H=lambda x:(x+AN**2)*(x+d**2)*(x+CE**2)-(CZ*BE)**2*x
        Hp=lambda x:(x+d**2)*(x+CE**2)+(x+AN**2)*(x+CE**2)+(x+AN**2)*(x+d**2)-(CZ*BE)**2
        mid=lambda x:(lo(x)+hi(x))/2
        am,dm,em,zm,bm=map(mid,[AN,d,CE,CZ,BE]);hp=lambda x:(x+am**2)*(x+dm**2)*(x+em**2)-(zm*bm)**2*x
        variant=[]
        for rec in frequency_records(coefficients(candidate,gated)):
            x0=mp.mpf(str(rec['omega']))**2;root=mp.findroot(hp,(x0*mp.mpf('.999'),x0*mp.mpf('1.001')));left=root-mp.mpf('1e-34');right=root+mp.mpf('1e-34');X=iv.mpf([str(left),str(right)]);hlo,hhi=H(f(left)),H(f(right));der=Hp(X)
            if not((hi(hlo)<0<lo(hhi)or hi(hhi)<0<lo(hlo))and(lo(der)>0 or hi(der)<0)):raise ValueError('Scalar existence/uniqueness failed')
            w=iv.sqrt(X);s=iv.mpc(0,1)*w;ratio=(s-AN)*(s+d)*(s-CE)/(CZ*BE*s);angle=iv.atan2(iv.im(ratio),iv.re(ratio));branch=int(mp.ceil(mid(angle)/(2*mp.pi)));tau=(-angle+2*iv.pi*branch)/w
            row={'candidate':candidate,'gated':gated,'x_enclosure':outward_bounds(X),'omega_enclosure':outward_bounds(w),'tau_enclosure':outward_bounds(tau),'simple_scalar_root':True};rows.append(row);variant.append(row)
            if candidate=='B'and not gated:
                diagnostic=coefficient(iv,candidate,gated,w,tau,True);out={k:outward_bounds(v)for k,v in diagnostic.items()if k not in ['B_directional','C_directional']};out.update(row);bc.append(out)
        if candidate=='B'and not gated:
            recurrence=iv.mpf(variant[0]['tau_enclosure'])+2*iv.pi/iv.mpf(variant[0]['omega_enclosure'])
            if lo(recurrence)<=mp.mpf(variant[1]['tau_enclosure'][1]):raise ValueError('Resonance separation failed')
    for i,r in enumerate(bc):
        if not all(mp.mpf(r[k][0])>0 for k in ['Delta_prime_modulus_squared','zero_root_value','second_harmonic_resolvent_modulus_squared']):raise ValueError('Simple eigenpair or homological inverse failed')
        if not(mp.mpf(r['l1_physical_time'][1])<0 if i==0 else mp.mpf(r['l1_physical_time'][0])>0):raise ValueError('B cubic sign not verified')
        if not(mp.mpf(r['crossing_derivative_real'][1])<0 if i==0 else mp.mpf(r['crossing_derivative_real'][0])>0):raise ValueError('B crossing not transverse')
    (ROOT/'data/all_scalar_hopf_v42.json').write_text(json.dumps({'arithmetic':'mpmath.iv 80 digits, exact decimal parameter strings','scope':'scalar root and phase enclosures for all four candidate/gating combinations','records':rows},indent=2)+'\n')
    (ROOT/'data/hopf_cubic_B_interval_v42.json').write_text(json.dumps({'scope':'Classical nondegenerate RFDE Hopf hypotheses for ungated Candidate B; not a radii-polynomial branch box','other_family_separation_verified':True,'records':bc},indent=2)+'\n');print(json.dumps(rows,indent=2))
if __name__=='__main__':run()
