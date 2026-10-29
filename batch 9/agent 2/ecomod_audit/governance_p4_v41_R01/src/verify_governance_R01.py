"""Independent bounded equation-level audit of P4 v41. No provider-code imports.
Floating-point spectra are not interval certificates of hybrid bifurcations.
The separate interval routine checks two scalar frequency roots and phase images,
not nonlinear Hopf, global folds, basins, or ecological validation.
"""
from pathlib import Path
import json, math, platform
import numpy as np
import scipy
from scipy.linalg import expm
from scipy.optimize import brentq, minimize_scalar
from mpmath import mp, iv
from interval_decimal_R01 import outward_bounds
ROOT=Path(__file__).resolve().parents[1]

def coefficients(candidate='A',gated=True):
    r,K,q,eta,emax=.02,100.,.001,(.914 if candidate=='A' else 2.756),(30. if candidate=='A' else 26.)
    delta=math.log(2)/10;d0=.01;tm=5.;a=emax*delta;b=emax*d0*delta/(eta*(1+delta))
    E=(a+math.sqrt(a*a+4*b))/2;N=K*(1-q*E/r);gate=1-E/emax if gated else 1.
    AN=-r*N/K;AE=-q*N;BN=-AN/(2*tm);BE=-AE/(2*tm)
    return dict(N=N,Z=delta,E=E,AN=AN,AE=AE,BN=BN,BE=BE,d=1/tm,
                CE=gate*eta*(delta-2*E/emax),CZ=gate*(eta*E+d0/(1+delta)**2))

def protective():
    c=coefficients();eta=.914;gate=1-c['E']/30
    c['CE']=-gate*eta;c['CZ']=c['CE']*c['E']/(1+c['Z']);return c

def cubic(c):
    p=np.polymul(np.polymul([1,c['AN']**2],[1,c['d']**2]),[1,c['CE']**2])
    p[-2]-=(c['CZ']*c['BE'])**2
    return p

def characteristic(lam,tau,c):
    return (lam-c['AN'])*(lam+c['d'])*(lam-c['CE'])-c['CZ']*c['BE']*lam*np.exp(-lam*tau)

def frequency_records(c):
    roots=np.roots(cubic(c));records=[]
    for x in sorted(z.real for z in roots if abs(z.imag)<1e-10 and z.real>0):
        w=math.sqrt(x);l=1j*w;P=(l-c['AN'])*(l+c['d'])*(l-c['CE'])
        tau=(-np.angle(P/(c['CZ']*c['BE']*l)))%(2*np.pi)/w
        Pp=(l+c['d'])*(l-c['CE'])+(l-c['AN'])*(l-c['CE'])+(l-c['AN'])*(l+c['d'])
        derivative=-l*P/(Pp-P/l+tau*P)
        records.append(dict(omega=w,tau=float(tau),dRe_dtau=float(derivative.real),characteristic_residual=float(abs(characteristic(l,tau,c)))))
    return records

def hold_matrix(c):
    return np.array([[c['AN'],0,c['AE']],[c['BN'],-c['d'],c['BE']],[0,0,0.]],dtype=float)

def monodromy(T,c,scheme='exact'):
    A=hold_matrix(c);ce,cz=c['CE'],c['CZ']
    if scheme in ['exact','euler']:
        h=np.expm1(ce*T)/ce if scheme=='exact' else T
        R=np.eye(3);R[2,1]=h*cz;R[2,2]=np.exp(ce*T)if scheme=='exact'else 1+ce*T
        return R@expm(A*T)
    if scheme=='native':
        Z=A.copy();Z[2,2]=ce
        # Augmented exponential gives the forcing integral without Z^{-1}.
        U=np.zeros((4,4));U[:3,:3]=Z;U[:3,3]=[0,0,cz];Q=expm(U*T)
        return Q[:3,:3]+np.outer(Q[:3,3],[0,1,0])
    raise ValueError('Unknown scheme')

def radius(T,c,scheme):return float(max(abs(np.linalg.eigvals(monodromy(T,c,scheme)))))

def gain_max(c):
    def gain(w):return abs(c['CZ']*c['BE']*1j*w/((1j*w-c['AN'])*(1j*w+c['d'])*(1j*w-c['CE'])))
    opt=minimize_scalar(lambda z:-gain(math.exp(z)),bounds=(-15,3),method='bounded')
    return {'maximum_numerically_located':float(-opt.fun),'omega':math.exp(opt.x),'certified_global_maximum':False}

def scalar_interval_check():
    mp.dps=90;iv.dps=80
    def lo(x):return mp.mpf(x._mpi_[0])
    def hi(x):return mp.mpf(x._mpi_[1])
    def point(t):return iv.mpf(str(t))
    r,K,q,eta,emax,d0,tm=[point(t)for t in ['.02','100','.001','.914','30','.01','5']]
    z=iv.log(point(2))/10;a=emax*z;b=emax*d0*z/(eta*(1+z));E=(a+iv.sqrt(a*a+4*b))/2;N=K*(1-q*E/r)
    AN=-r*N/K;BE=q*N/(2*tm);d=1/tm;gate=1-E/emax;CE=gate*eta*(z-2*E/emax);CZ=gate*(eta*E+d0/(1+z)**2)
    def H(x):return (x+AN**2)*(x+d**2)*(x+CE**2)-(CZ*BE)**2*x
    def Hp(x):return (x+d**2)*(x+CE**2)+(x+AN**2)*(x+CE**2)+(x+AN**2)*(x+d**2)-(CZ*BE)**2
    # High-precision point roots only seed rigorous sign/derivative tests.
    def mid(x):return (lo(x)+hi(x))/2
    am,dm,em,zm,bm=map(mid,[AN,d,CE,CZ,BE])
    f=lambda x:(x+am**2)*(x+dm**2)*(x+em**2)-(zm*bm)**2*x
    records=[]
    for rec in frequency_records(coefficients()):
        x0=mp.mpf(str(rec['omega']))**2;root=mp.findroot(f,(x0*mp.mpf('.9999'),x0*mp.mpf('1.0001')))
        left,right=root-mp.mpf('1e-35'),root+mp.mpf('1e-35');X=iv.mpf([str(left),str(right)])
        fl,fr=H(point(left)),H(point(right));opposite=(hi(fl)<0 and lo(fr)>0)or(lo(fl)>0 and hi(fr)<0)
        deriv=Hp(X);simple=lo(deriv)>0 or hi(deriv)<0
        if not(opposite and simple):raise ValueError('Scalar root existence/uniqueness test failed')
        w=iv.sqrt(X);l=iv.mpc(0,1)*w;P=(l-AN)*(l+d)*(l-CE);ratio=P/(CZ*BE*l)
        angle=iv.atan2(iv.im(ratio),iv.re(ratio));branch=0 if rec['tau']<10 else 1;tau=(-angle+2*iv.pi*branch)/w
        printed=(mp.mpf('3.6661490142739'),mp.mpf('3.6661490142743'))if branch==0 else(mp.mpf('150.3584773101408'),mp.mpf('150.3584773101421'))
        contained=printed[0]<=lo(tau)and hi(tau)<=printed[1]
        if not contained:raise ValueError('Published delay enclosure inconsistent')
        records.append({'x_enclosure':outward_bounds(X),'endpoint_sign_change_proved':bool(opposite),'derivative_excludes_zero':bool(simple),'tau_enclosure':outward_bounds(tau),'inside_published_delay_enclosure':bool(contained)})
    return {'arithmetic':'mpmath.iv, 80 decimal digits; exact decimal parameters and interval log(2)','scope':'Two scalar frequency roots and interval phase images, not a nonlinear RFDE Hopf theorem','roots':records}

def run():
    core={}
    for candidate in ['A','B']:
        for gated in [True,False]:
            c=coefficients(candidate,gated);core[candidate+('_gated'if gated else'_ungated')]={'coefficients':c,'frequencies':frequency_records(c)}
    c=coefficients();p=protective();sample=[]
    for channel,cc in [('mobilising',c),('protective',p)]:
        for scheme in ['euler','exact','native']:
            brackets=([(40,55),(75,85)]if scheme=='euler'else[(6,7)])if channel=='mobilising'else([(2,3)]if scheme=='euler'else[])
            crossings=[float(brentq(lambda t:radius(t,cc,scheme)-1,*br))for br in brackets]
            grid=np.linspace(.2,300,1501);radii=[radius(float(t),cc,scheme)for t in grid]
            sample.append({'channel':channel,'scheme':scheme,'rho_at_1_year':radius(1,cc,scheme),'located_crossings_from_declared_brackets':crossings,'grid_min_Tr':.2,'grid_max_Tr':300,'grid_count':len(grid),'maximum_grid_rho':max(radii),'grid_max_rho_at_Tr':float(grid[int(np.argmax(radii))]),'rho_47p536':radius(47.536,cc,scheme),'rho_79p143':radius(79.143,cc,scheme),'global_crossing_completeness_certified':False})
    J=hold_matrix(c);J[2,1]=c['CZ'];J[2,2]=c['CE'];Jp=hold_matrix(p);Jp[2,1]=p['CZ'];Jp[2,2]=p['CE']
    flipped=dict(c);flipped['CZ']=-flipped['CZ']
    return {'source':'P4 v41, equations (1), (3), (5)-(8), (11)-(13), native-ZOH formula','core':core,'undelayed_mobilising_eigenvalues':[[float(z.real),float(z.imag)]for z in np.linalg.eigvals(J)],'undelayed_protective_eigenvalues':[[float(z.real),float(z.imag)]for z in np.linalg.eigvals(Jp)],'protective_modulus_cubic_coefficients':cubic(p).tolist(),'protective_gain':gain_max(p),'mobilising_gain':gain_max(c),'sign_flipped_frequencies':frequency_records(flipped),'sampled':sample,'scalar_interval_checks':scalar_interval_check(),'not_rerun':['global DDE trajectories and basins','periodic-orbit continuation','Moore-Spence/Krawczyk fold pipelines','Lyapunov coefficient calculations','maturation-delay model campaign'],'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'ecological_or_institutional_calibration_established':False}

if __name__=='__main__':
    result=run();(ROOT/'data').mkdir(exist_ok=True);(ROOT/'data/verification_results_R01.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'local_crossings_A':[x['tau']for x in result['core']['A_gated']['frequencies']],'sampled':result['sampled'],'scalar_interval_checks':result['scalar_interval_checks']},indent=2))
