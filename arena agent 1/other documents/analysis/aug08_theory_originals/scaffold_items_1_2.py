"""Items 1+2: for strong candidates, (1) classify each Hopf crossing direction
(dRe/dtau at the crossing: stabilizing vs destabilizing), and (2) map the stable windows
across tau to identify the cleanest manuscript-style structure
(stable at tau=0 -> unstable window -> stable again)."""
import numpy as np
from scipy.optimize import fsolve

rng = np.random.default_rng(21)
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
    g,P0,Nc,dA,dJ,alpha,A0,omegaA,Aeq,lamP,gammaU,zeta,deltaK,cE,K0,muE,eta,Emax,delta0,Dref,taum,q=(
        p['g'],p['P0'],p['Nc'],p['dA'],p['dJ'],p['alpha'],p['A0'],p['omegaA'],p['Aeq'],p['lamP'],
        p['gammaU'],p['zeta'],p['deltaK'],p['cE'],p['K0'],p['muE'],p['eta'],p['Emax'],p['delta0'],p['Dref'],p['taum'],p['q'])
    def F(x):
        XA,XJ,P_,U,A,KC,E=x
        gB=P0*XA*np.exp(-XA/Nc)*(A/(A+A0))-(1-psi)*q*E*XA; Q=q*E*XA
        return np.array([(1/g)*XJ-dA*XA-psi*q*E*XA, gB-(1/g)*XJ-dJ*XJ,
            (1-alpha)*psi*q*E*XA-lamP*P_, dA*XA+dJ*XJ+alpha*psi*q*E*XA+lamP*P_-gammaU*U,
            -gB+gammaU*U+omegaA*(Aeq-A), zeta*Q-KC*(deltaK+cE*E),
            (1-E/Emax)*(1-np.exp(-KC/K0))*(delta0-eta*E**2/Emax)-muE*E])
    E0=np.sqrt(delta0*Emax/eta)
    sol,info,ier,msg=fsolve(F,[min(90.,0.5*Nc),5.,1.,1.,Aeq*0.9,10.,E0],full_output=True,maxfev=20000)
    if ier!=1: return None
    XA,XJ,P_,U,A,KC,E=sol
    if XA<=0 or XJ<0 or U<0 or A<=0 or E<=0 or E>Emax or KC<0: return None
    return XA,XJ,P_,U,A,KC,E
def build(p,psi,state):
    XA,XJ,P_,U,A,KC,E=state
    g,P0,Nc,dA,dJ,alpha,A0,omegaA,Aeq,lamP,gammaU,zeta,deltaK,cE,K0,muE,eta,Emax,delta0,Dref,taum,q=(
        p['g'],p['P0'],p['Nc'],p['dA'],p['dJ'],p['alpha'],p['A0'],p['omegaA'],p['Aeq'],p['lamP'],
        p['gammaU'],p['zeta'],p['deltaK'],p['cE'],p['K0'],p['muE'],p['eta'],p['Emax'],p['delta0'],p['Dref'],p['taum'],p['q'])
    g0=1-np.exp(-KC/K0); h0=1-E/Emax
    if g0<=1e-9: return None
    betaA=P0*np.exp(-XA/Nc)*(1-XA/Nc)*(A/(A+A0))-(1-psi)*q*E
    betaa=P0*XA*np.exp(-XA/Nc)*(A0/(A+A0)**2)
    CE=-muE*E/(h0*Emax)-2*h0*g0*eta*E/Emax-muE; CK=muE*E/K0*(1-g0)/g0; CZ=h0*g0*eta*E/Dref
    J=np.array([[-(dA+psi*q*E),1/g,0,0,0,0],[betaA-(1-psi)*q*E,-(dJ+1/g),0,0,betaa,0],
        [(1-alpha)*psi*q*E,0,-lamP,0,0,0],[dA+alpha*psi*q*E,dJ,lamP,-gammaU,0,0],
        [-betaA,0,0,gammaU,-(betaa+omegaA),0],[zeta*q*E,0,0,0,0,-(deltaK+cE*E)]])
    bE=np.array([-psi*q*XA,-(1-psi)*q*XA,(1-alpha)*psi*q*XA,alpha*psi*q*XA,0,zeta*q*XA-cE*KC])
    return dict(g0=g0,h0=h0,CE=CE,CK=CK,CZ=CZ,J=J,bE=bE,taum=taum,E=E,XA=XA,KC=KC)
def RA_RK(w,B):
    M=np.linalg.inv(1j*w*np.eye(6)-B['J']); return (M@B['bE'])[0],(M@B['bE'])[5]
def char(iw,tau,B):
    RA,RK=RA_RK(iw.imag,B); D=iw-B['CE']-B['CK']*RK
    return (1+B['taum']*iw)*D+B['CZ']*np.exp(-iw*tau)*iw*RA
def gap_w(w,B):
    RA,RK=RA_RK(w,B)
    return abs(B['CZ']*1j*w*RA/(1+1j*w*B['taum']))-abs(1j*w-B['CE']-B['CK']*RK)

def tau0_rightmost(B, state):
    g_,P0_,Nc_,dA_,dJ_,alpha_,A0_,omegaA_,Aeq_,lamP_,gammaU_,zeta_,deltaK_,cE_,K0_,muE_,eta_,Emax_,delta0_,Dref_,taum_,q_=(
        B['p']['g'],B['p']['P0'],B['p']['Nc'],B['p']['dA'],B['p']['dJ'],B['p']['alpha'],B['p']['A0'],B['p']['omegaA'],
        B['p']['Aeq'],B['p']['lamP'],B['p']['gammaU'],B['p']['zeta'],B['p']['deltaK'],B['p']['cE'],B['p']['K0'],
        B['p']['muE'],B['p']['eta'],B['p']['Emax'],B['p']['delta0'],B['p']['Dref'],B['p']['taum'],B['p']['q'])
    XA,XJ,P_,U,A,KC,E=state
    def F8(y):
        XA_,XJ2,P2,U_,A_,KC_,Z_,E_=y
        gB=P0_*XA_*np.exp(-XA_/Nc_)*(A_/(A_+A0_))-0.0*q_*E_*XA_
        Q=q_*E_*XA_
        XAd=(1/g_)*XJ2-dA_*XA_-q_*E_*XA_
        return np.array([XAd, gB-(1/g_)*XJ2-dJ_*XJ2,
            (1-alpha_)*q_*E_*XA_-lamP_*P2,
            dA_*XA_+dJ_*XJ2+alpha_*q_*E_*XA_+lamP_*P2-gammaU_*U_,
            -gB+gammaU_*U_+omegaA_*(Aeq_-A_),
            zeta_*Q-KC_*(deltaK_+cE_*E_),
            (-XAd-Z_)/taum_,
            (1-E_/Emax_)*(1-np.exp(-KC_/K0_))*(eta_*E_*Z_/Dref_+delta0_-eta_*E_**2/Emax_)-muE_*E_])
    y0=np.array([XA,XJ,P_,U,A,KC,0.0,E]); h=1e-7
    J8=np.zeros((8,8))
    for j in range(8):
        sp=y0.copy(); sm=y0.copy(); sp[j]+=h; sm[j]-=h
        J8[:,j]=(F8(sp)-F8(sm))/(2*h)
    ev=np.linalg.eigvals(J8)
    return max(ev.real)

def find_hopf_crossings(B):
    """Return list of (tau*, omega*) genuine crossings (|char|<1e-6)."""
    ws=np.geomspace(1e-4,3.0,3000); gv=[gap_w(w,B) for w in ws]
    zeros=[]
    for i in range(len(ws)-1):
        if gv[i]*gv[i+1]<0:
            a,b=ws[i],ws[i+1]
            for _ in range(50):
                mid=(a+b)/2
                if gap_w(a,B)*gap_w(mid,B)<=0: b=mid
                else: a=mid
            zeros.append((a+b)/2)
    out=[]
    for wstar in zeros:
        RA,RK=RA_RK(wstar,B)
        D=1j*wstar-B['CE']-B['CK']*RK
        num=-(1+1j*wstar*B['taum'])*D; den=B['CZ']*1j*wstar*RA
        phi=np.angle(num)-np.angle(den)
        for n in range(0,60):
            tau=-(phi+2*np.pi*n)/wstar
            if tau<=0: continue
            if abs(char(1j*wstar,tau,B))<1e-6:
                out.append((tau,wstar)); break
    return out

def root_at(tau, wguess, B):
    """Polish root of char near (0, wguess) for this tau."""
    def f(xy):
        l=xy[0]+1j*xy[1]
        c=char(l,tau,B); return np.array([c.real,c.imag])
    sol,info,ier,msg=fsolve(f,[0.0,wguess],full_output=True)
    if ier!=1: return None
    return sol[0]+1j*sol[1]

def rightmost_re(tau,B,re_lo=-4.0,re_hi=0.8):
    """rightmost root real part via grid+polish."""
    cands=[]
    for re in np.linspace(re_lo,re_hi,30):
        for im in np.linspace(-2.0,2.0,40):
            cands.append((abs(char(re+1j*im,tau,B)),re,im))
    cands.sort()
    roots=[]
    for v0,re0,im0 in cands[:6]:
        def f(xy):
            l=xy[0]+1j*xy[1]; c=char(l,tau,B); return np.array([c.real,c.imag])
        try:
            sol,info,ier,msg=fsolve(f,[re0,im0],full_output=True)
            if ier==1 and abs(char(sol[0]+1j*sol[1],tau,B))<1e-4:
                roots.append(sol[0]+1j*sol[1])
        except: pass
    return max((r.real for r in roots), default=float('nan'))

# ---- find candidates, then classify ----
cands=[]
for trial in range(40000):
    p=sample_params(); state=solve_eq(p,1.0)
    if state is None: continue
    B=build(p,1.0,state)
    if B is None: continue
    B['p']=p
    best=-np.inf
    for w in np.geomspace(1e-3,3.0,100):
        try: best=max(best,gap_w(w,B))
        except: pass
    if best>0.8:
        cands.append((best,p,state,B))
        cands.sort(key=lambda t:-t[0]); cands=cands[:6]
print(f"{len(cands)} candidates (gap>0.8)\n")

for gap,p,state,B in cands:
    crossings=find_hopf_crossings(B)
    re0=tau0_rightmost(B,state)
    print("="*72)
    print(f"candidate gap={gap:.2f}, XA={state[0]:.1f}, E={state[6]:.3f}, g0={B['g0']:.3f}")
    print(f"  tau=0 rightmost Re = {re0:+.5f}  ({'stable' if re0<0 else 'UNSTABLE'})")
    print(f"  {len(crossings)} Hopf crossings:")
    for tau,w in crossings:
        # crossing direction: Re at tau*(1±0.02)
        d=0.02*tau
        r_lo=root_at(tau-d,w,B); r_hi=root_at(tau+d,w,B)
        if r_lo is None or r_hi is None:
            dr='?'; continue
        dr=(r_hi.real-r_lo.real)/(2*d)
        direc = 'destabilizing (Re: - -> + as tau increases)' if dr>0 else 'stabilizing (Re: + -> -)'
        print(f"    tau*={tau:8.2f}  omega*={w:.5f}  period={2*np.pi/w:9.1f}  "
              f"dRe/dtau={dr:+.3e}  -> {direc}")
    # stable windows: track rightmost Re on a coarse grid up to 1.2*max tau
    tmax=1.2*max((t for t,w in crossings), default=1.0)
    taus=np.linspace(0.0,tmax,240)
    res=[(t, rightmost_re(t,B)) for t in taus]
    stable=[ (taus[i],taus[i+1]) for i in range(len(res)-1) if res[i][1]<0 and res[i+1][1]<0 ]
    # merge adjacent
    merged=[]
    for s,e in stable:
        if merged and s-merged[-1][1]<tmax/240*1.5: merged[-1]=(merged[-1][0],e)
        else: merged.append((s,e))
    print(f"  stable windows in tau∈[0,{tmax:.0f}]: {[(round(a,1),round(b,1)) for a,b in merged]}")
    # classify the structure
    if re0<0 and len(merged)>=2 and merged[0][0]<=1e-6:
        print("  STRUCTURE: stable at tau=0, then unstable window(s), then stable again  <-- manuscript-style")
    elif re0<0:
        print("  STRUCTURE: stable at tau=0, loses stability later (no re-stabilization within range)")
    else:
        print("  STRUCTURE: unstable at tau=0 (Hopf adds crossings; no clean manuscript-style window)")
