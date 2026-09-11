"""Summary: characterize the best candidate's Hopf structure (stabilizing vs destabilizing)
and confirm the delay-amplified-instability mechanism exists in the 9-state scaffold.
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

# find ONE strong candidate, then characterize its tau-window
best=None
for trial in range(60000):
    p=sample_params(); state=solve_eq(p,1.0)
    if state is None: continue
    B=build(p,1.0,state)
    if B is None: continue
    g=-np.inf
    for w in np.geomspace(1e-3,3.0,100):
        try: g=max(g,gap_w(w,B))
        except: pass
    if g>1.0:
        best=(g,p,state,B); break
if best is None:
    print("no candidate"); raise SystemExit
g,p,state,B=best
print("BEST CANDIDATE")
print("params:", {k:round(v,4) for k,v in p.items()})
print(f"state: XA={state[0]:.2f} XJ={state[1]:.3f} P={state[2]:.4f} U={state[3]:.3f} A={state[4]:.1f} KC={state[5]:.3f} E={state[6]:.4f}")
print(f"g0={B['g0']:.4f} h0={B['h0']:.4f} CE={B['CE']:.4f} CK={B['CK']:.4f} CZ={B['CZ']:.4f}")
# find all omega* and tau for which char(iw,tau)=0
ws=np.geomspace(1e-4,3.0,5000); gv=[gap_w(w,B) for w in ws]
zeros=[]
for i in range(len(ws)-1):
    if gv[i]*gv[i+1]<0:
        a,b=ws[i],ws[i+1]
        for _ in range(60):
            mid=(a+b)/2
            if gap_w(a,B)*gap_w(mid,B)<=0: b=mid
            else: a=mid
        zeros.append((a+b)/2)
print("modulus zeros w*:", [round(w,5) for w in zeros])
hopf_pairs=[]
for wstar in zeros:
    RA,RK=RA_RK(wstar,B)
    D=1j*wstar-B['CE']-B['CK']*RK
    num=-(1+1j*wstar*B['taum'])*D; den=B['CZ']*1j*wstar*RA
    phi=np.angle(num)-np.angle(den)
    for n in range(0,40):
        tau=-(phi+2*np.pi*n)/wstar
        if tau<=0: continue
        if abs(char(1j*wstar,tau,B))<1e-6:
            hopf_pairs.append((tau,wstar))
print("Hopf crossings (tau, omega, period):")
for tau,w in hopf_pairs:
    print(f"  tau={tau:.3f}  omega={w:.5f}  period={2*np.pi/w:.1f}")
# tau=0 stability (8x8 finite-diff)
g_=p['g'];P0_=p['P0'];Nc_=p['Nc'];dA_=p['dA'];dJ_=p['dJ'];alpha_=p['alpha'];A0_=p['A0'];omegaA_=p['omegaA']
Aeq_=p['Aeq'];lamP_=p['lamP'];gammaU_=p['gammaU'];zeta_=p['zeta'];deltaK_=p['deltaK'];cE_=p['cE'];K0_=p['K0']
muE_=p['muE'];eta_=p['eta'];Emax_=p['Emax'];delta0_=p['delta0'];Dref_=p['Dref'];taum_=p['taum'];q_=p['q']
XA,XJ,P_,U,A,KC,E=state
def F8(y):
    XA_,XJ2,P2,U_,A_,KC_,Z_,E_=y
    gB=P0_*XA_*np.exp(-XA_/Nc_)*(A_/(A_+A0_))-(1-1.0)*q_*E_*XA_
    Q=q_*E_*XA_
    XAd=(1/g_)*XJ2-dA_*XA_-1.0*q_*E_*XA_
    return np.array([XAd, gB-(1/g_)*XJ2-dJ_*XJ2,
        (1-alpha_)*1.0*q_*E_*XA_-lamP_*P2,
        dA_*XA_+dJ_*XJ2+alpha_*1.0*q_*E_*XA_+lamP_*P2-gammaU_*U_,
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
print("tau=0 eigenvalues:", np.round(ev,4))
print("tau=0 stable?", all(ev.real<0), "| rightmost:", round(max(ev.real),5))
