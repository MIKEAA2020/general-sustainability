"""Close item 2: classify the eta=10 unified-core-v2 intermittency at tau~18.45.
Build the unified-v2 DDE integrator (X,U,Z,E), simulate long, then diagnose:
  (a) time series of the large-amplitude excursions (periods, quiet durations)
  (b) return map of excursion peak amplitudes -> 1-D map? (homoclinic/relaxation)
  (c) power spectrum of switching times -> incommensurate freqs (torus)?
  (d) equilibrium linearisation -> saddle? (homoclinic signature)
Model (unified core v2, Eq unified-core-v2):
  Xdot = g(X,A) - m(X) - q E X
  Udot = m(X) - gamma_U U
  Zdot = (ell - Z)/tau_m,  ell = -Xdot
  Edot = (1-E/Emax)[ eta E Z(t-tau)/Dref + delta0 - eta E^2/Emax ]
  A = M - X - U
"""
import numpy as np
from scipy.optimize import fsolve

P = dict(M=100.0, mu=0.340, KA=24.5, d=0.072, c=0.00995, gamma_U=0.388,
         q=0.0384, Emax=35.8, Dref=2.29, tau_m=5.13, delta0=0.0118)
ETA = 10.0

def equilibrium(eta=ETA):
    E = np.sqrt(P['delta0']*P['Emax']/eta)
    def sys(x):
        X, U = x
        A = P['M'] - X - U
        g = P['mu']*X*A/(P['KA']+A)
        m = P['d']*X + P['c']*X**2
        return [g - m - P['q']*E*X, m - P['gamma_U']*U]
    sol, info, ier, msg = fsolve(sys, [16.0, 10.0], full_output=True)
    if ier != 1: return None
    X, U = sol
    return np.array([X, U, P['M']-X-U, E])

def dde_rhs(y, ytau, eta=ETA):
    X, U, Z, E = y
    Ztau = ytau[2]   # delayed Z
    A = P['M'] - X - U
    g = P['mu']*X*A/(P['KA']+A)
    m = P['d']*X + P['c']*X**2
    Xdot = g - m - P['q']*E*X
    Udot = m - P['gamma_U']*U
    ell = -Xdot
    Zdot = (ell - Z)/P['tau_m']
    Edot = (1 - E/P['Emax'])*(eta*E*Ztau/P['Dref'] + P['delta0']
                              - eta*E**2/P['Emax'])
    return np.array([Xdot, Udot, Zdot, Edot])

def integrate(y0, hist, T, tau, dt=0.02):
    n = len(y0)
    nsteps = int(round(T/dt)); h = T/nsteps
    ys = np.zeros((nsteps+1, n)); ys[0] = y0
    def delayed(t):
        if t <= 0: return hist(t)
        ti = t/h; i = int(np.floor(ti))
        if i >= nsteps: return ys[nsteps]
        fr = ti - i
        return (1-fr)*ys[i] + fr*ys[i+1]
    for i in range(nsteps):
        t = i*h; y = ys[i]
        k1 = dde_rhs(y, delayed(t-tau))
        k2 = dde_rhs(y + h/2*k1, delayed(t+h/2-tau))
        k3 = dde_rhs(y + h/2*k2, delayed(t+h/2-tau))
        k4 = dde_rhs(y + h*k3, delayed(t+h-tau))
        ys[i+1] = y + h/6*(k1+2*k2+2*k3+k4)
    return ys

if __name__ == "__main__":
    eq = equilibrium()
    print("equilibrium (X,U,A,E):", np.round(eq, 6))
    # linearisation at equilibrium -> saddle?
    J = np.zeros((4,4))
    X, U, Z, E = eq
    h = 1e-6
    for j in range(4):
        sp = eq.copy(); sm = eq.copy(); sp[j]+=h; sm[j]-=h
        yt = eq.copy()
        fp = dde_rhs(sp, yt); fm = dde_rhs(sm, yt)
        J[:,j] = (fp-fm)/(2*h)
    lam = np.linalg.eigvals(J)
    print("tau=0 eigenvalues (at eta=10):", np.round(lam, 5))
    print("  real parts:", np.round(np.real(lam), 5))
