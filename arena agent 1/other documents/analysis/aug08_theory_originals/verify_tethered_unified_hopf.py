"""Verify audit #7's claim: does the thermodynamically-tethered unified core
(5-state: X,U,Z,B_x,E) preserve the delay-induced Hopf of the untethered
unified core v2 (X,U,Z,E)?

Untethered unified v2 (from manuscript/on-disk machinery):
  Xdot = g(X,A) - m(X) - q E X ;  A = M - X - U
  Udot = m(X) - gamma_U U
  Zdot = (ell - Z)/tau_m, ell = -Xdot
  Edot = (1-E/Emax)[ eta E Z(t-tau)/Dref + delta0 - eta E^2/Emax ]
  g = mu*X*A/(KA+A); m = d*X + c*X^2
Known (D-series): at eta=10, Hopf pair tau_-~17.568, tau_+~18.362 yr.

Tethered (audit #7):
  Bxdot = eps*(q E X) - Bx*(delta_B + c_E E)
  Edot  = (1-E/Emax)(1-e^{-Bx/B0})[ eta E Z(t-tau)/Dref + delta0 - eta E^2/Emax ] - mu_E E
"""
import numpy as np, sys
sys.path.insert(0, 'verification_scripts')
from verify_kappaA_sweep import hopf_thresholds

P = dict(M=100.0, mu=0.340, KA=24.5, d=0.072, c=0.00995, gamma_U=0.388,
         q=0.0384, Emax=35.8, Dref=2.29, tau_m=5.13, delta0=0.0118)
ETA = 10.0

def gX(X,A): return P['mu']*X*A/(P['KA']+A)
def mX(X):   return P['d']*X + P['c']*X**2

def equilibrium(tether, eta=ETA):
    # solve X,U,E with Z*=0; U = m(X)/gamma_U
    import scipy.optimize as so
    if not tether:
        E = np.sqrt(P['delta0']*P['Emax']/eta)
        def sys(x):
            X, U = x
            A = P['M']-X-U
            return [gX(X,A)-mX(X)-P['q']*E*X, mX(X)-P['gamma_U']*U]
        sol = so.fsolve(sys, [16., 10.]); X,U = sol
        return np.array([X,U,0.,E])
    eps_, dB_, cE_, B0_, muE_ = tether
    def sys(x):
        X, U, E = x
        A = P['M']-X-U
        g = gX(X,A); m = mX(X)
        Bx = eps_*P['q']*E*X/(dB_ + cE_*E)
        gate = 1.0 - np.exp(-Bx/B0_)
        return [g - m - P['q']*E*X,
                m - P['gamma_U']*U,
                (1-E/P['Emax'])*gate*(P['delta0'] - eta*E**2/P['Emax']) - muE_*E]
    sol, info, ier, msg = so.fsolve(sys, [16., 10., 0.5], full_output=True)
    if ier != 1: return None
    X,U,E = sol
    A = P['M']-X-U
    Bx = tether[0]*P['q']*E*X/(tether[1] + tether[2]*E)
    return np.array([X,U,0.,Bx,E])

def jac_and_delay(eq, tether, eta=ETA):
    def rhs(y, Ztau):
        X,U,Z,E = y[:4]
        A = P['M']-X-U
        g = gX(X,A); m = mX(X)
        Xdot = g - m - P['q']*E*X
        Udot = m - P['gamma_U']*U
        ell = -Xdot
        Zdot = (ell - Z)/P['tau_m']
        if not tether:
            Edot = (1-E/P['Emax'])*(eta*E*Ztau/P['Dref'] + P['delta0'] - eta*E**2/P['Emax'])
            return np.array([Xdot,Udot,Zdot,Edot])
        eps_,dB_,cE_,B0_,muE_ = tether
        Bx = y[3]
        Bxdot = eps_*P['q']*E*X - Bx*(dB_ + cE_*E)
        gate = 1.0 - np.exp(-Bx/B0_)
        Edot = (1-E/P['Emax'])*gate*(eta*E*Ztau/P['Dref'] + P['delta0'] - eta*E**2/P['Emax']) - muE_*E
        return np.array([Xdot,Udot,Zdot,Bxdot,Edot])
    n = len(eq); h = 1e-6
    J = np.zeros((n,n))
    for j in range(n):
        sp = eq.copy(); sm = eq.copy(); sp[j]+=h; sm[j]-=h
        Z = eq[2]
        fp = rhs(sp, Z); fm = rhs(sm, Z)
        J[:,j] = (fp-fm)/(2*h)
    Bd = np.zeros((n,n))
    # delay coupling: dEdot/dZ(t-tau) ; E is last index, Z is index 2
    e_idx = n-1; z_idx = 2
    sp = eq.copy(); sp[z_idx] += h
    fp = rhs(sp, eq[2]+h); fm = rhs(eq, eq[2])
    Bd[e_idx, z_idx] = (fp[e_idx]-fm[e_idx])/h
    return J, Bd

print("="*72)
print("UN-TETHERED unified v2 at eta=10 (expect tau_-~17.57, tau_+~18.36)")
eq0 = equilibrium(None)
print("eq (X,U,Z,E):", np.round(eq0,6))
J0, B0 = jac_and_delay(eq0, None)
ev0 = np.linalg.eigvals(J0 + B0)
print("tau=0 eigen:", np.round(ev0,5))
th0 = hopf_thresholds(J0, B0, w_lo=1e-3, w_hi=3.0, nw=12000, nmax=4)
print("Hopf:", [(round(t,3), round(w,4)) for t,w in th0])

print()
print("="*72)
print("TETHERED unified v2 (audit #7) — sweep tether parameters")
tether_sets = [
    ("B0=10 (well-fueled), muE=0.01", (0.5, 0.1, 0.01, 10.0, 0.01)),
    ("B0=1  (marginally fueled), muE=0.01", (0.5, 0.1, 0.01, 1.0, 0.01)),
    ("B0=10, muE=0.1 (strong decay)", (0.5, 0.1, 0.01, 10.0, 0.1)),
    ("B0=0.1 (fuel-limited), muE=0.01", (0.5, 0.1, 0.01, 0.1, 0.01)),
    ("muE=0 (no entropy decay)", (0.5, 0.1, 0.01, 10.0, 0.0)),
]
for name, tt in tether_sets:
    eq = equilibrium(tt)
    if eq is None:
        print(f"{name}: NO EQUILIBRIUM"); continue
    X,U,Z,Bx,E = eq
    print(f"\n{name}")
    print(f"  eq (X,U,Bx,E): {X:.4f},{U:.4f},{Bx:.4f},{E:.4f}   Bx/B0={Bx/tt[3]:.3f}  gate={1-np.exp(-Bx/tt[3]):.4f}")
    J, B = jac_and_delay(eq, tt)
    ev = np.linalg.eigvals(J + B)
    print(f"  tau=0 eigen: {np.round(ev,5)}")
    th = hopf_thresholds(J, B, w_lo=1e-3, w_hi=3.0, nw=12000, nmax=4)
    print(f"  Hopf: {[(round(t,3), round(w,4)) for t,w in th] if th else 'NONE'}")
