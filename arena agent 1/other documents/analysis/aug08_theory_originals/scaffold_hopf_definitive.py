"""Definitive Hopf check: for candidates with modulus gap > 0, find omega* where |LHS|=|RHS|,
compute the phase-correct tau values, and evaluate |char(i omega*, tau)|. If ~0 => genuine Hopf.
"""
import numpy as np
from scipy.optimize import fsolve, brentq

rng = np.random.default_rng(11)

def sample_params():
    p={}
    p['g']=10**rng.uniform(-0.5,1.0); p['P0']=10**rng.uniform(-1.3,1.0); p['Nc']=10**rng.uniform(1.3,2.7)
    p['dA']=10**rng.uniform(-2.0,-0.3); p['dJ']=10**rng.uniform(-2.0,-0.3); p['alpha']=rng.uniform(0.1,0.9)
    p['A0']=10**rng.uniform(-1.0,1.0); p['omegaA']=10**rng.uniform(-4.0,-1.0); p['Aeq']=10**rng.uniform(2.0,4.0)
    p['lamP']=10**rng.uniform(-1.3,0.7); p['gammaU']=10**rng.uniform(-1.3,0.7); p['zeta']=rng.uniform(0.1,0.5)
    p['deltaK']=10**rng.uniform(-2.0,0.0); p['cE']=10**rng.uniform(-2.0,0.3); p['K0']=10**rng.uniform(-2.0,1.0)
    p['muE']=10**rng.uniform(-5.0,-2.0); p['eta']=10**rng.uniform(-1.0,1.0); p['Emax']=10**rng.uniform(1.0,2.0)
    p['delta0']=10**rng.uniform(-2.3,-1.0); p['Dref']=10**rng.uniform(-0.3,0.7); p['taum']=10**rng.uniform(0.0,1.3)
    p['q']=10**rng.uniform(-4.0,-2.0)
    return p

def solve_eq(p, psi):
    g,P0,Nc,dA,dJ,alpha,A0,omegaA,Aeq,lamP,gammaU,zeta,deltaK,cE,K0,muE,eta,Emax,delta0,Dref,taum,q = (
        p['g'],p['P0'],p['Nc'],p['dA'],p['dJ'],p['alpha'],p['A0'],p['omegaA'],p['Aeq'],
        p['lamP'],p['gammaU'],p['zeta'],p['deltaK'],p['cE'],p['K0'],p['muE'],p['eta'],p['Emax'],p['delta0'],
        p['Dref'],p['taum'],p['q'])
    def F(x):
        XA,XJ,P_,U,A,KC,E = x
        gB = P0*XA*np.exp(-XA/Nc)*(A/(A+A0)) - (1-psi)*q*E*XA
        Q  = q*E*XA
        return np.array([(1/g)*XJ-dA*XA-psi*q*E*XA,
                         gB-(1/g)*XJ-dJ*XJ,
                         (1-alpha)*psi*q*E*XA-lamP*P_,
                         dA*XA+dJ*XJ+alpha*psi*q*E*XA+lamP*P_-gammaU*U,
                         -gB+gammaU*U+omegaA*(Aeq-A),
                         zeta*Q-KC*(deltaK+cE*E),
                         (1-E/Emax)*(1-np.exp(-KC/K0))*(delta0-eta*E**2/Emax)-muE*E])
    E0=np.sqrt(delta0*Emax/eta)
    sol,info,ier,msg=fsolve(F,[min(90.,0.5*Nc),5.,1.,1.,Aeq*0.9,10.,E0],full_output=True,maxfev=20000)
    if ier!=1: return None
    XA,XJ,P_,U,A,KC,E=sol
    if XA<=0 or XJ<0 or U<0 or A<=0 or E<=0 or E>Emax or KC<0: return None
    return XA,XJ,P_,U,A,KC,E

def build(p, psi, state):
    XA,XJ,P_,U,A,KC,E = state
    g,P0,Nc,dA,dJ,alpha,A0,omegaA,Aeq,lamP,gammaU,zeta,deltaK,cE,K0,muE,eta,Emax,delta0,Dref,taum,q = (
        p['g'],p['P0'],p['Nc'],p['dA'],p['dJ'],p['alpha'],p['A0'],p['omegaA'],p['Aeq'],
        p['lamP'],p['gammaU'],p['zeta'],p['deltaK'],p['cE'],p['K0'],p['muE'],p['eta'],p['Emax'],p['delta0'],
        p['Dref'],p['taum'],p['q'])
    g0=1-np.exp(-KC/K0); h0=1-E/Emax
    if g0<=1e-9: return None
    betaA = P0*np.exp(-XA/Nc)*(1-XA/Nc)*(A/(A+A0)) - (1-psi)*q*E
    betaa = P0*XA*np.exp(-XA/Nc)*(A0/(A+A0)**2)
    CE = -muE*E/(h0*Emax) - 2*h0*g0*eta*E/Emax - muE
    CK = muE*E/K0*(1-g0)/g0
    CZ = h0*g0*eta*E/Dref
    J = np.array([
     [-(dA+psi*q*E), 1/g,0,0,0,0],
     [betaA-(1-psi)*q*E, -(dJ+1/g),0,0,betaa,0],
     [(1-alpha)*psi*q*E, 0, -lamP,0,0,0],
     [dA+alpha*psi*q*E, dJ, lamP, -gammaU,0,0],
     [-betaA,0,0,gammaU,-(betaa+omegaA),0],
     [zeta*q*E, 0,0,0,0,-(deltaK+cE*E)]])
    bE = np.array([-psi*q*XA, -(1-psi)*q*XA, (1-alpha)*psi*q*XA, alpha*psi*q*XA, 0, zeta*q*XA - cE*KC])
    return dict(g0=g0,h0=h0,CE=CE,CK=CK,CZ=CZ,J=J,bE=bE,taum=taum,E=E,XA=XA,KC=KC)

def RA_RK(w, B):
    M = np.linalg.inv(1j*w*np.eye(6) - B['J'])
    return (M@B['bE'])[0], (M@B['bE'])[5]

def char(iw, tau, B):
    RA,RK = RA_RK(iw.imag if np.iscomplexobj(iw) else iw, B)
    D = iw - B['CE'] - B['CK']*RK
    return (1+B['taum']*iw)*D + B['CZ']*np.exp(-iw*tau)*iw*RA

def gap_w(w, B):
    RA,RK = RA_RK(w, B)
    L = abs(B['CZ']*1j*w*RA/(1+1j*w*B['taum']))
    R = abs(1j*w - B['CE'] - B['CK']*RK)
    return L-R

# find strong candidates
cands=[]
for trial in range(40000):
    p = sample_params()
    state = solve_eq(p, 1.0)
    if state is None: continue
    B = build(p, 1.0, state)
    if B is None: continue
    best=-np.inf; bestw=None
    for w in np.geomspace(1e-3, 3.0, 120):
        try: g=gap_w(w,B)
        except: continue
        if g>best: best,bestw=g,w
    if best>0.5:
        cands.append((best,p,state,B,bestw))
        cands.sort(key=lambda t:-t[0]); cands=cands[:8]
print(f"{len(cands)} candidates with gap>0.5")
for gap,p,state,B,w0 in cands:
    # find omega* where gap=0 near bestw (root of gap_w)
    # first locate sign change around bestw
    ws=np.geomspace(1e-4,3.0,4000)
    gv=[gap_w(w,B) for w in ws]
    zeros=[]
    for i in range(len(ws)-1):
        if gv[i]*gv[i+1]<0:
            a,b=ws[i],ws[i+1]
            for _ in range(60):
                mid=(a+b)/2
                if gap_w(a,B)*gap_w(mid,B)<=0: b=mid
                else: a=mid
            zeros.append((a+b)/2)
    # for each omega*, phase -> tau (CORRECT sign), check char
    found=False
    for wstar in zeros:
        RA,RK=RA_RK(wstar,B)
        S = 1j*wstar*RA/(1+1j*wstar*B['taum'])
        D = 1j*wstar - B['CE'] - B['CK']*RK
        num = -(1+1j*wstar*B['taum'])*D   # char: e^{-iw tau} = num/den
        den = B['CZ']*1j*wstar*RA
        phi = np.angle(num) - np.angle(den)
        # e^{-iw tau} = |num/den| e^{i phi}  => -w tau = phi + 2 pi n => tau = -(phi+2pi n)/w
        for n in range(0,30):
            tau = -(phi + 2*np.pi*n)/wstar
            if tau <= 0: continue
            val = char(1j*wstar, tau, B)
            if abs(val) < 1e-6:
                found=True
                print(f"  GENUINE HOPF: w*={wstar:.5f}, tau={tau:.4f}, |char|={abs(val):.2e}, "
                      f"period={2*np.pi/wstar:.2f}")
    if not found:
        print(f"  cand gap={gap:.2f}, XA={state[0]:.1f}, E={state[6]:.3f}, g0={B['g0']:.3f}: "
              f"{len(zeros)} modulus zeros but NO phase-consistent root (|char|>1e-6 at all)")
