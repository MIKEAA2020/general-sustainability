"""Item 3: anchor the scaffold to real life-history classes (anchovy/sprat/cod)
x the manuscript's economic parameter ranges; test whether a delay-induced Hopf
exists in the anchored region. Uses life-history values consistent with the
manuscript's own stage-structure windows (r*g ~ 1.5-1.6 etc.)."""
import numpy as np
from scipy.optimize import fsolve

# ---- Life-history classes (anchored: age at maturity g, adult mortality M=dA,
#      juvenile mortality dJ ~ 2-4x M, Ricker productivity P0 ~ r + dA at low density,
#      Nc ~ stock at max recruitment on the K=100 scale) ----
classes = {
  'anchovy-class (g=1, r~1.6)':  dict(g=1.0, P0=8.0, Nc=40.0, dA=1.0, dJ=3.0),
  'sprat-class (g=2, r~0.8)':    dict(g=2.0, P0=4.0, Nc=50.0, dA=0.5, dJ=1.5),
  'cod-class (g=5, r~0.3)':      dict(g=5.0, P0=2.0, Nc=60.0, dA=0.2, dJ=0.6),
}
# ---- economic variants (manuscript Table: eta 0.5-3, Emax 15-50, delta0 0.005-0.05,
#      Dref 0.5-5, taum 2-15; scaffold thermodynamic: zeta, deltaK, cE, K0, muE) ----
econ = [
  dict(eta=0.914, Emax=30.0, delta0=0.010, Dref=1.0,  taum=5.0),
  dict(eta=1.5,   Emax=30.0, delta0=0.010, Dref=1.0,  taum=5.0),
  dict(eta=2.756, Emax=26.0, delta0=0.010, Dref=1.0,  taum=5.0),
  dict(eta=3.0,   Emax=50.0, delta0=0.010, Dref=1.0,  taum=5.0),
  dict(eta=0.914, Emax=30.0, delta0=0.020, Dref=1.0,  taum=2.0),
  dict(eta=0.914, Emax=30.0, delta0=0.010, Dref=2.0,  taum=10.0),
]
th = dict(zeta=0.25, deltaK=0.1, cE=0.5, K0=1.0, muE=1e-4,
          alpha=0.5, lamP=0.2, gammaU=0.2, A0=1.0, omegaA=1e-3, Aeq=5000.0, q=0.001)
psi = 1.0

def solve_eq(p):
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
def build(p,state):
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

print("=== ANCHORED SEARCH: life-history class x economic variant ===")
print(f"{'class':<22}{'eta':>5}{'Emax':>6}{'XA*':>8}{'E*':>7}{'g0':>6}{'maxgap':>9}  Hopf?")
hits=[]
for cname, bio in classes.items():
    for ec in econ:
        p = dict(bio); p.update(ec); p.update(th)
        state=solve_eq(p)
        if state is None:
            print(f"{cname:<22}{ec['eta']:>5}{ec['Emax']:>6}{'no eq':>8}"); continue
        B=build(p,state)
        if B is None:
            print(f"{cname:<22}{ec['eta']:>5}{ec['Emax']:>6}{'no B':>8}"); continue
        best=-np.inf; bestw=None
        for w in np.geomspace(1e-4,3.0,200):
            try:
                g=gap_w(w,B)
                if g>best: best,bestw=g,w
            except: pass
        hp = best>0
        print(f"{cname:<22}{ec['eta']:>5}{ec['Emax']:>6}{state[0]:>8.1f}{state[6]:>7.3f}"
              f"{B['g0']:>6.3f}{best:>9.2e}  {'YES' if hp else 'no'}")
        if hp:
            hits.append((cname,ec,B,state,best,bestw))
print()
if hits:
    print(f"{len(hits)} anchored parameter sets satisfy the modulus condition. Verifying full Hopf...")
    for cname,ec,B,state,best,bestw in hits:
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
        genuine=[]
        for wstar in zeros:
            RA,RK=RA_RK(wstar,B)
            D=1j*wstar-B['CE']-B['CK']*RK
            num=-(1+1j*wstar*B['taum'])*D; den=B['CZ']*1j*wstar*RA
            phi=np.angle(num)-np.angle(den)
            for n in range(0,80):
                tau=-(phi+2*np.pi*n)/wstar
                if tau<=0: continue
                if abs(char(1j*wstar,tau,B))<1e-6:
                    genuine.append((tau,wstar)); break
        if genuine:
            tau,w=genuine[0]
            print(f"  {cname} eta={ec['eta']}: GENUINE HOPF tau*={tau:.2f} w*={w:.5f} period={2*np.pi/w:.1f}")
        else:
            print(f"  {cname} eta={ec['eta']}: modulus gap>0 but no phase-consistent root (no genuine Hopf)")
else:
    print("\nNO anchored (life-history-plausible) parameter set satisfies the modulus condition.")
    print("=> The anchored region is delay-independently stable in the scaffold.")
