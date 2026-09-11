"""Refine the anchored search: for each life-history class, scan the economic
parameters that the manuscript itself varies (eta, savings zeta, fuel efficiency
1/K0, catchability q) to see whether the anchored region can reach a Hopf."""
import numpy as np
from scipy.optimize import fsolve
classes = {
  'anchovy': dict(g=1.0, P0=8.0, Nc=40.0, dA=1.0, dJ=3.0),
  'sprat':   dict(g=2.0, P0=4.0, Nc=50.0, dA=0.5, dJ=1.5),
  'cod':     dict(g=5.0, P0=2.0, Nc=60.0, dA=0.2, dJ=0.6),
}
th = dict(eta=0.914, Emax=30.0, delta0=0.010, Dref=1.0, taum=5.0,
          zeta=0.25, deltaK=0.1, cE=0.5, K0=1.0, muE=1e-4,
          alpha=0.5, lamP=0.2, gammaU=0.2, A0=1.0, omegaA=1e-3, Aeq=5000.0, q=0.001)
psi=1.0
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
def maxgap(B):
    best=-np.inf
    for w in np.geomspace(1e-4,3.0,200):
        try: best=max(best,gap_w(w,B))
        except: pass
    return best

print("=== REFINED: anchored class x economic scan (eta, zeta, K0, q) ===")
print("columns: eta, zeta, K0, q -> maxgap (positive = Hopf possible)")
best_any = -np.inf; best_desc=None
for cname,bio in classes.items():
    local_best=-np.inf; local=None
    for eta in [0.914, 2.0, 3.0, 5.0]:
        for zeta in [0.25, 0.5, 0.8]:
            for K0 in [1.0, 0.3, 0.1, 0.03]:
                for q in [0.001, 0.003, 0.01]:
                    p=dict(bio); p.update(th); p.update(eta=eta, zeta=zeta, K0=K0, q=q)
                    st=solve_eq(p)
                    if st is None: continue
                    B=build(p,st)
                    if B is None: continue
                    g=maxgap(B)
                    if g>local_best: local_best,local=g,(eta,zeta,K0,q,g,st,B)
                    if g>best_any: best_any,best_desc=g,(cname,eta,zeta,K0,q,g)
    print(f"\n{cname}: best maxgap = {local_best:+.3e} at (eta,zeta,K0,q)={local[:4] if local else '-'}")
    if local and local_best>0:
        _,_,_,_,g,st,B=local
        # verify genuine Hopf
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
            RA,RK=RA_RK(wstar,B); D=1j*wstar-B['CE']-B['CK']*RK
            num=-(1+1j*wstar*B['taum'])*D; den=B['CZ']*1j*wstar*RA
            phi=np.angle(num)-np.angle(den)
            for n in range(0,80):
                tau=-(phi+2*np.pi*n)/wstar
                if tau<=0: continue
                if abs(char(1j*wstar,tau,B))<1e-6: genuine.append((tau,wstar)); break
        if genuine:
            tau,w=genuine[0]
            print(f"  -> GENUINE HOPF: tau*={tau:.2f} period={2*np.pi/w:.1f} (E={st[6]:.3f}, XA={st[0]:.1f}, g0={B['g0']:.3f})")
        else:
            print(f"  -> modulus>0 but no phase root (no genuine Hopf)")
print(f"\nOverall best anchored maxgap: {best_any:+.3e} at {best_desc}")
