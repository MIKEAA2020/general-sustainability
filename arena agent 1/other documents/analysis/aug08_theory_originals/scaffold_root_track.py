"""Definitive test: root-track the FULL characteristic quasi-polynomial across tau.
For each candidate, find the rightmost root Re(lambda) vs tau; a sign change = Hopf crossing.
"""
import numpy as np
from scipy.optimize import fsolve, brentq

rng = np.random.default_rng(7)

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
    if g0<=1e-12: return None
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
    return dict(g0=g0,h0=h0,CE=CE,CK=CK,CZ=CZ,J=J,bE=bE,taum=taum,E=E,XA=XA,KC=KC,p=p)

def char(lam, tau, B):
    M = np.linalg.inv(lam*np.eye(6) - B['J'])
    RA=(M@B['bE'])[0]; RK=(M@B['bE'])[5]
    D = lam - B['CE'] - B['CK']*RK
    return (1+B['taum']*lam)*D + B['CZ']*np.exp(-lam*tau)*lam*RA

def rightmost(tau, B):
    # find root of char with largest real part by scanning a region and polishing
    best=None
    # sample candidates from a grid of (re, im), polish each local min of |char|
    grid_re = np.linspace(-3.5, 0.6, 42)
    grid_im = np.linspace(-2.0, 2.0, 84)
    cands=[]
    for re in grid_re:
        for im in grid_im:
            v = abs(char(re+1j*im, tau, B))
            cands.append((v, re, im))
    cands.sort()
    # polish top 8 by Newton on Re/Im
    roots=[]
    for v0,re0,im0 in cands[:8]:
        def f(xy):
            l = xy[0]+1j*xy[1]
            return np.array([char(l, tau, B).real, char(l, tau, B).imag])
        try:
            sol,info,ier,msg=fsolve(f,[re0,im0],full_output=True)
            if ier==1:
                roots.append(sol[0]+1j*sol[1])
        except Exception: pass
    if roots:
        return max(roots, key=lambda r: r.real)
    return None

# --- find candidates with positive modulus gap, then root-track ---
cands=[]
for trial in range(30000):
    p = sample_params()
    state = solve_eq(p, 1.0)
    if state is None: continue
    B = build(p, 1.0, state)
    if B is None: continue
    # modulus gap
    best=-np.inf; bestw=None
    for w in np.geomspace(1e-3, 3.0, 100):
        try: M=np.linalg.inv(1j*w*np.eye(6)-B['J'])
        except: continue
        RA=(M@B['bE'])[0]; RK=(M@B['bE'])[5]
        L=abs(B['CZ']*1j*w*RA/(1+1j*w*B['taum'])); R=abs(1j*w-B['CE']-B['CK']*RK)
        if L-R>best: best,bestw=L-R,w
    if best>0.3:
        cands.append((best,p,state,B,bestw))
        cands.sort(key=lambda t:-t[0]); cands=cands[:6]
print(f"{len(cands)} strong candidates (gap>0.3)")

for gap,p,state,B,w0 in cands:
    # tau=0 rightmost
    r0 = rightmost(0.0, B)
    re0 = r0.real if r0 is not None else float('nan')
    # track rightmost vs tau
    taus = np.linspace(0.0, 30.0, 121)
    res = []
    prev = None
    for tau in taus:
        r = rightmost(tau, B)
        re = r.real if r is not None else float('nan')
        im = r.imag if r is not None else float('nan')
        res.append((tau, re, im))
    # sign changes
    crossings=[]
    for i in range(len(res)-1):
        a,b = res[i][1], res[i+1][1]
        if (a<0 and b>0) or (a>0 and b<0):
            crossings.append((res[i][0], res[i+1][0], a, b))
    print(f"\ncand gap={gap:.2f}: tau=0 rightmost Re={re0:.4f}; Re(tau) min={min(r[1] for r in res):.4f}; "
          f"crossings in tau∈[0,30]: {[(round(t1,2),round(t2,2)) for t1,t2,_,_ in crossings]}")
    if crossings:
        # refine first crossing: find tau* where Re=0, get omega
        t1,t2,_,_ = crossings[0]
        def re_at(tau): return rightmost(tau, B).real
        try:
            tstar = brentq(re_at, t1, t2, xtol=1e-8)
            rstar = rightmost(tstar, B)
            print(f"  HOPF at tau*={tstar:.4f}, lambda={rstar.real:.2e}{rstar.imag:+.2e}i, "
                  f"period={2*np.pi/abs(rstar.imag):.2f} time-units")
        except Exception as e:
            print("  refine failed:", e)
