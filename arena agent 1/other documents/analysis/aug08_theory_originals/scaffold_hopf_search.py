"""Biological-parameter search for a Hopf bifurcation in the 9-state Grand-Unified-Core scaffold.

Question: does ANY parameter set allow the delay-induced Hopf (modulus condition satisfiable)?
If yes, find it and compute tau_-, tau_+. If no (over the searched range), report the best gap.

Method: Latin-hypercube-ish random sampling (log-uniform), solve the coupled 7-D equilibrium,
build the corrected 6x6 J_eco + b_E (psi-factors fixed), sweep omega for max(|LHS|-|RHS|).
"""
import numpy as np
from scipy.optimize import fsolve

rng = np.random.default_rng(42)

def sample_params():
    p = {}
    p['g']    = 10**rng.uniform(-0.5, 1.0)      # 0.3-10
    p['P0']   = 10**rng.uniform(-1.3, 1.0)      # 0.05-10
    p['Nc']   = 10**rng.uniform(1.3, 2.7)       # 20-500
    p['dA']   = 10**rng.uniform(-2.0, -0.3)     # 0.01-0.5
    p['dJ']   = 10**rng.uniform(-2.0, -0.3)
    p['alpha']= rng.uniform(0.1, 0.9)
    p['A0']   = 10**rng.uniform(-1.0, 1.0)      # 0.1-10
    p['omegaA']=10**rng.uniform(-4.0, -1.0)     # 1e-4-0.1
    p['Aeq']  = 10**rng.uniform(2.0, 4.0)       # 100-10000
    p['lamP'] = 10**rng.uniform(-1.3, 0.7)      # 0.05-5
    p['gammaU']=10**rng.uniform(-1.3, 0.7)
    p['zeta'] = rng.uniform(0.1, 0.5)
    p['deltaK']=10**rng.uniform(-2.0, 0.0)      # 0.01-1
    p['cE']   = 10**rng.uniform(-2.0, 0.3)      # 0.01-2
    p['K0']   = 10**rng.uniform(-2.0, 1.0)      # 0.01-10
    p['muE']  = 10**rng.uniform(-5.0, -2.0)     # 1e-5-1e-2
    p['eta']  = 10**rng.uniform(-1.0, 1.0)      # 0.1-10
    p['Emax'] = 10**rng.uniform(1.0, 2.0)       # 10-100
    p['delta0']=10**rng.uniform(-2.3, -1.0)     # 0.005-0.1
    p['Dref'] = 10**rng.uniform(-0.3, 0.7)      # 0.5-5
    p['taum'] = 10**rng.uniform(0.0, 1.3)       # 1-20
    p['q']    = 10**rng.uniform(-4.0, -2.0)     # 1e-4-1e-2
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
        return np.array([
            (1/g)*XJ - dA*XA - psi*q*E*XA,
            gB - (1/g)*XJ - dJ*XJ,
            (1-alpha)*psi*q*E*XA - lamP*P_,
            dA*XA + dJ*XJ + alpha*psi*q*E*XA + lamP*P_ - gammaU*U,
            -gB + gammaU*U + omegaA*(Aeq-A),
            zeta*Q - KC*(deltaK + cE*E),
            (1-E/Emax)*(1-np.exp(-KC/K0))*(delta0 - eta*E**2/Emax) - muE*E,
        ])
    E0 = np.sqrt(delta0*Emax/eta)
    guess = [min(90.0, 0.5*Nc), 5.0, 1.0, 1.0, Aeq*0.9, 10.0, E0]
    sol,info,ier,msg = fsolve(F, guess, full_output=True, maxfev=20000)
    if ier != 1: return None
    XA,XJ,P_,U,A,KC,E = sol
    if XA <= 0 or XJ < 0 or U < 0 or A <= 0 or E <= 0 or E > Emax or KC < 0:
        return None
    return XA,XJ,P_,U,A,KC,E

def hopf_analysis(p, psi, state, wgrid):
    XA,XJ,P_,U,A,KC,E = state
    g,P0,Nc,dA,dJ,alpha,A0,omegaA,Aeq,lamP,gammaU,zeta,deltaK,cE,K0,muE,eta,Emax,delta0,Dref,taum,q = (
        p['g'],p['P0'],p['Nc'],p['dA'],p['dJ'],p['alpha'],p['A0'],p['omegaA'],p['Aeq'],
        p['lamP'],p['gammaU'],p['zeta'],p['deltaK'],p['cE'],p['K0'],p['muE'],p['eta'],p['Emax'],p['delta0'],
        p['Dref'],p['taum'],p['q'])
    g0 = 1-np.exp(-KC/K0); h0 = 1-E/Emax
    if g0 <= 0 or h0 <= 0: return None
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
    best = -np.inf; bestw = None; best_L = 0; best_R = 0
    for w in wgrid:
        try:
            M = np.linalg.inv(1j*w*np.eye(6)-J)
        except np.linalg.LinAlgError:
            continue
        RA = (M@bE)[0]; RK = (M@bE)[5]
        LHS = abs(CZ*1j*w*RA/(1+1j*w*taum))
        RHS = abs(1j*w - CE - CK*RK)
        gap = LHS - RHS
        if gap > best: best, bestw, best_L, best_R = gap, w, LHS, RHS
    return dict(g0=g0, h0=h0, E=E, XA=XA, KC=KC, best=best, bestw=bestw, L=best_L, R=best_R)

wgrid = np.geomspace(1e-3, 3.0, 150)

# ---- BROAD SEARCH ----
N = 3000
results = []
for i in range(N):
    p = sample_params()
    state = solve_eq(p, 1.0)  # psi=1 first
    if state is None: continue
    r = hopf_analysis(p, 1.0, state, wgrid)
    if r is None: continue
    r['p'] = p
    results.append(r)

print(f"Broad search: {N} samples, {len(results)} valid equilibria")
pos = [r for r in results if r['best'] > 0]
print(f"Samples with max(LHS-RHS) > 0 (modulus satisfiable): {len(pos)}")
results.sort(key=lambda r: -r['best'])
print("\nTop 10 by max gap:")
for r in results[:10]:
    print(f"  gap={r['best']:+.4e} @w={r['bestw']:.4f}  g0={r['g0']:.3f} XA={r['XA']:7.2f} E={r['E']:.4f}")
print("\nBest overall:", results[0]['best'] if results else "N/A")
