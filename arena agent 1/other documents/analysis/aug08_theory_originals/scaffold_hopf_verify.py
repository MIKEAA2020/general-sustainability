"""Verify a genuine Hopf for the top candidates: build the FULL characteristic quasi-polynomial
and find its imaginary roots (not just the modulus condition). Also check tau=0 stability.
"""
import numpy as np
from scipy.optimize import fsolve, brentq
import sys

rng = np.random.default_rng(42)

def sample_params():
    p = {}
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

def char_func(lam, tau, B):
    # characteristic: lam - CE - CK*RK(lam) + CZ e^{-lam tau} lam RA(lam)/(1+taum lam) = 0
    # equivalently (1+taum lam)[lam - CE - CK RK] + CZ e^{-lam tau} lam RA = 0
    M = np.linalg.inv(lam*np.eye(6) - B['J'])
    RA = (M@B['bE'])[0]; RK = (M@B['bE'])[5]
    D = lam - B['CE'] - B['CK']*RK
    return (1 + B['taum']*lam)*D + B['CZ']*np.exp(-lam*tau)*lam*RA

def check_candidate(p, psi, state):
    B = build(p, psi, state)
    # tau=0 eigenvalues: det(lam I - (J_eco + bE-based coupling?)) -- at tau=0 the E-equation couples
    # via C_E (already in E's own row) -- need full 7x7 at tau=0: states (X_A,X_J,P,U,A,K_C,E)
    g,P0,Nc,dA,dJ,alpha,A0,omegaA,Aeq,lamP,gammaU,zeta,deltaK,cE,K0,muE,eta,Emax,delta0,Dref,taum,q = (
        p['g'],p['P0'],p['Nc'],p['dA'],p['dJ'],p['alpha'],p['A0'],p['omegaA'],p['Aeq'],
        p['lamP'],p['gammaU'],p['zeta'],p['deltaK'],p['cE'],p['K0'],p['muE'],p['eta'],p['Emax'],p['delta0'],
        p['Dref'],p['taum'],p['q'])
    XA,XJ,P_,U,A,KC,E = state
    # 7x7 Jacobian at tau=0 (Z eliminated? No: Z is a state; at tau=0, z couples back). Full 8 states
    # (X_A,X_J,P,U,A,K_C,Z,E). But simpler: solve char_func(lam, 0) roots via polynomial approx?
    # Use the characteristic function: at tau=0, find rightmost root of char_func(lam,0)=0.
    # char_func(lam,0) = (1+tm lam)D + CZ lam RA. Its roots = eigenvalues of the linearised 6+2 system.
    # Scan Re(lam) by evaluating char_func on a grid? Instead: full 8x8 finite-difference Jacobian.
    def F8(y):
        XA_,XJ_,P2,U_,A_,KC_,Z_,E_ = y
        gB = P0*XA_*np.exp(-XA_/Nc)*(A_/(A_+A0)) - (1-psi)*q*E_*XA_
        Q = q*E_*XA_
        XAd = (1/g)*XJ_ - dA*XA_ - psi*q*E_*XA_
        U__ = dA*XA_ + dJ*XJ_ + alpha*psi*q*E_*XA_ + lamP*P2 - gammaU*U_
        Ad  = -gB + gammaU*U_ + omegaA*(Aeq-A_)
        ell = -XAd
        Ed  = (1-E_/Emax)*(1-np.exp(-KC_/K0))*(eta*E_*Z_/Dref + delta0 - eta*E_**2/Emax) - muE*E_
        return np.array([XAd,
                         gB-(1/g)*XJ_-dJ*XJ_,
                         (1-alpha)*psi*q*E_*XA_-lamP*P2,
                         U__,
                         Ad,
                         zeta*Q - KC_*(deltaK+cE*E_),
                         (ell - Z_)/taum,
                         Ed])
    y0 = np.array([XA,XJ,P_,U,A,KC,0.0,E])
    h=1e-7
    J8 = np.zeros((8,8))
    for j in range(8):
        sp=y0.copy(); sm=y0.copy(); sp[j]+=h; sm[j]-=h
        J8[:,j]=(F8(sp)-F8(sm))/(2*h)
    ev = np.linalg.eigvals(J8)
    return ev

# --- re-run the best samples, keep top 5, verify full Hopf ---
best_list = []
for trial in range(20000):
    p = sample_params()
    state = solve_eq(p, 1.0)
    if state is None: continue
    B = build(p, 1.0, state)
    wgrid = np.geomspace(1e-3, 3.0, 120)
    best=-np.inf; bestw=None
    for w in wgrid:
        try: M = np.linalg.inv(1j*w*np.eye(6)-B['J'])
        except np.linalg.LinAlgError: continue
        RA=(M@B['bE'])[0]; RK=(M@B['bE'])[5]
        L=abs(B['CZ']*1j*w*RA/(1+1j*w*B['taum'])); R=abs(1j*w-B['CE']-B['CK']*RK)
        gap=L-R
        if gap>best: best,bestw=gap,w
    if best>0.5:
        best_list.append((best,p,state))
        best_list.sort(key=lambda t:-t[0]); best_list=best_list[:5]
print("Top 5 candidates with gap>0.5:")
for gap,p,state in best_list:
    XA,XJ,P_,U,A,KC,E = state
    print(f"  gap={gap:.3f} XA={XA:.1f} E={E:.3f} KC={KC:.3f} g0={1-np.exp(-KC/p['K0']):.3f}")

# verify the single best: full characteristic roots + tau=0 stability
if best_list:
    gap,p,state = best_list[0]
    B = build(p, 1.0, state)
    print("\n=== VERIFYING BEST CANDIDATE ===")
    print("params:", {k: round(v,4) for k,v in p.items()})
    # tau=0 eigenvalues
    ev0 = check_candidate(p, 1.0, state)
    print("tau=0 eigenvalues (8x8):", np.round(ev0,4))
    print("tau=0 stable?", all(ev0.real<0), " rightmost:", round(max(ev0.real),5))
    # find imaginary roots of char_func across omega, and matching tau from phase
    def gap_w(w):
        M=np.linalg.inv(1j*w*np.eye(6)-B['J'])
        RA=(M@B['bE'])[0]; RK=(M@B['bE'])[5]
        return abs(B['CZ']*1j*w*RA/(1+1j*w*B['taum'])) - abs(1j*w-B['CE']-B['CK']*RK)
    # find sign changes of gap_w
    ws = np.geomspace(5e-4, 3.0, 2000)
    gv = [gap_w(w) for w in ws]
    roots_w=[]
    for i in range(len(ws)-1):
        if gv[i]*gv[i+1]<0:
            a,b=ws[i],ws[i+1]
            for _ in range(60):
                mid=(a+b)/2
                if gap_w(a)*gap_w(mid)<=0: b=mid
                else: a=mid
            roots_w.append((a+b)/2)
    print("w where |LHS|=|RHS|:", [round(w,5) for w in roots_w])
    # phase: tau = [arg(D)-arg(S)+(2n+1)pi]/w ; find smallest positive tau for each w
    for w in roots_w[:4]:
        M=np.linalg.inv(1j*w*np.eye(6)-B['J'])
        RA=(M@B['bE'])[0]; RK=(M@B['bE'])[5]
        S = 1j*w*RA/(1+1j*w*B['taum']); D = 1j*w-B['CE']-B['CK']*RK
        # char eq: (1+tm l)D + CZ e^{-lt} l RA = 0 => e^{-i w tau} = -(1+i w tm) D/(CZ i w RA)
        # so tau_n = [arg(-(1+iw tm)D) - arg(CZ iw RA) + 2 pi n]/w
        num = -(1+1j*w*B['taum'])*D
        den = B['CZ']*1j*w*RA
        phi = np.angle(num) - np.angle(den)
        taus = [(phi+2*np.pi*n)/w for n in range(0,20)]
        taus = [t for t in taus if t>0]
        # verify actual root
        realroots=[]
        for t in taus[:4]:
            val = char_func(1j*w, t, B)
            realroots.append((t, abs(val)))
        print(f"w={w:.5f}: candidate tau (smallest): {[round(t,3) for t in taus[:3]]}, |char|={[f'{v:.1e}' for _,v in realroots]}")
