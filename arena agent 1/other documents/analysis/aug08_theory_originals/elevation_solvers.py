"""
From-scratch RK4-DDE solvers for the manuscript's core models (numba-jitted).

Models implemented directly from corrected_manuscript.tex equations:
  1. three-state corrected core  (eq:stock-core, eq:Z-core, eq:effort-core-corrected)
  2. three-state ungated core    (eq:effort-core)
  3. four-state core             (eq:fourstate-N, eq:fourstate-A, eq:Z-core, eq:effort-core ungated)

Candidate A: eta=0.914, Emax=30, delta0=0.01, Dref=1.0, taum=5, k=10,
             delta=ln(2)/k, r=0.02, K=100, q=0.001, Zref=1.0
Candidate B: eta=2.756, Emax=26, rest as above.
Four-state extras: kappa_A=0.05, omega_A=1e-3, A_intr=0.5*K=50,
             A0=0.01*K=1.0, A_eq=A_intr + kappa_A*K/omega_A = 5050.
"""
import numpy as np
from numba import njit

# ---------------- parameters ----------------
def PARAMS_A():
    return dict(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0, delta0=0.01,
                Dref=1.0, taum=5.0, k=10.0, Zref=1.0, delta=np.log(2.0)/10.0,
                kappa_A=0.05, omega_A=1e-3, A_intr=50.0, A0=1.0)

def PARAMS_B():
    p = PARAMS_A()
    p['eta'] = 2.756; p['Emax'] = 26.0
    return p

@njit(fastmath=True)
def softplus_shifted_floor(u, k, delta):
    """max(0, softplus_k(u) - ln2/k + delta)"""
    if k * u > 30.0:
        sp = u - np.log(2.0)/k          # softplus_k(u) ~ u for large k*u... note: softplus_k(u)=ln(1+e^{ku})/k ~ u as ku->inf
    else:
        sp = np.log1p(np.exp(k * u)) / k
    val = sp - np.log(2.0)/k + delta
    return val if val > 0.0 else 0.0

@njit(fastmath=True)
def softplus_k(u, k):
    if k * u > 30.0:
        return u
    if k * u < -30.0:
        return 0.0
    return np.log1p(np.exp(k * u)) / k

# ---------------- RHS ----------------
@njit(fastmath=True)
def rhs_three(N, Z, E, Ztau, p, gated):
    S = p[0]*N*(1 - N/p[1])
    C = p[2]*E*N
    Ndot = S - C
    Zdot = (softplus_shifted_floor(C - S, p[7], p[10]) - Z)/p[5]
    if gated:
        Edot = (1 - E/p[4])*(p[3]*E*(Ztau/p[6] - E/p[4]) + p[9]*Ztau/(p[8] + Ztau))
    else:
        Edot = p[3]*E*(Ztau/p[6] - E/p[4]) + p[9]*Ztau/(p[8] + Ztau)
    return Ndot, Zdot, Edot

@njit(fastmath=True)
def rhs_four(N, Z, E, A, Ztau, p):
    R = p[0]*N*(1 - N/p[1])*A/(A + p[14])
    Bflux = R + p[11]*N*A/(A + p[14])
    Ndot = R - p[2]*E*N
    Adot = -Bflux + p[12]*(p[13] - A)
    Zdot = (softplus_shifted_floor(p[2]*E*N - R, p[7], p[10]) - Z)/p[5]
    Edot = p[3]*E*(Ztau/p[6] - E/p[4]) + p[9]*Ztau/(p[8] + Ztau)   # ungated per registry
    return Ndot, Zdot, Edot, Adot

# ---------------- simulation core ----------------
@njit(fastmath=True)
def simulate_three(N0, Z0, E0, tau, T, dt, p, gated):
    """RK4-DDE for the three-state core. Returns (N, Z, E, Namp)."""
    n_delay = max(1, int(round(tau/dt)))
    N, Z, E = N0, Z0, E0
    buf = np.full(n_delay + 1, Z)
    idx = 0
    n_steps = int(T/dt)
    Nmin = N; Nmax = N
    for step in range(n_steps):
        Ztau = buf[idx]
        k1N,k1Z,k1E = rhs_three(N,Z,E,Ztau,p,gated)
        k2N,k2Z,k2E = rhs_three(N+dt/2*k1N,Z+dt/2*k1Z,E+dt/2*k1E,Ztau,p,gated)
        k3N,k3Z,k3E = rhs_three(N+dt/2*k2N,Z+dt/2*k2Z,E+dt/2*k2E,Ztau,p,gated)
        k4N,k4Z,k4E = rhs_three(N+dt*k3N,Z+dt*k3Z,E+dt*k3E,Ztau,p,gated)
        N = N + dt/6*(k1N+2*k2N+2*k3N+k4N)
        Z = Z + dt/6*(k1Z+2*k2Z+2*k3Z+k4Z)
        E = E + dt/6*(k1E+2*k2E+2*k3E+k4E)
        if N < 0.0: N = 0.0
        if E < 0.0: E = 0.0
        if N < Nmin: Nmin = N
        if N > Nmax: Nmax = N
        buf[idx] = Z
        idx = (idx + 1) % (n_delay + 1)
    return N, Z, E, Nmax - Nmin

@njit(fastmath=True)
def simulate_four(N0, Z0, E0, A0, tau, T, dt, p):
    """RK4-DDE for the four-state core. Returns (N, Z, E, A, Namp)."""
    n_delay = max(1, int(round(tau/dt)))
    N, Z, E, A = N0, Z0, E0, A0
    buf = np.full(n_delay + 1, Z)
    idx = 0
    n_steps = int(T/dt)
    Nmin = N; Nmax = N
    for step in range(n_steps):
        Ztau = buf[idx]
        k1N,k1Z,k1E,k1A = rhs_four(N,Z,E,A,Ztau,p)
        k2N,k2Z,k2E,k2A = rhs_four(N+dt/2*k1N,Z+dt/2*k1Z,E+dt/2*k1E,A+dt/2*k1A,Ztau,p)
        k3N,k3Z,k3E,k3A = rhs_four(N+dt/2*k2N,Z+dt/2*k2Z,E+dt/2*k2E,A+dt/2*k2A,Ztau,p)
        k4N,k4Z,k4E,k4A = rhs_four(N+dt*k3N,Z+dt*k3Z,E+dt*k3E,A+dt*k3A,Ztau,p)
        N = N + dt/6*(k1N+2*k2N+2*k3N+k4N)
        Z = Z + dt/6*(k1Z+2*k2Z+2*k3Z+k4Z)
        E = E + dt/6*(k1E+2*k2E+2*k3E+k4E)
        A = A + dt/6*(k1A+2*k2A+2*k3A+k4A)
        if N < 0.0: N = 0.0
        if E < 0.0: E = 0.0
        if N < Nmin: Nmin = N
        if N > Nmax: Nmax = N
        buf[idx] = Z
        idx = (idx + 1) % (n_delay + 1)
    return N, Z, E, A, Nmax - Nmin

# ---------------- equilibrium helpers ----------------
def equilibrium_three(p, gated=True):
    """Closed-form interior equilibrium (Z* = delta, E* quadratic, N* = K(1-qE*/r))."""
    Zs = p['delta']
    # eta E (Z/Dref - E/Emax) + delta0 Z/(Zref+Z) = 0  (gate factor nonzero for E<Emax)
    a = p['eta']/p['Emax']; b = p['eta']*Zs/p['Dref']; c = p['delta0']*Zs/(p['Zref']+Zs)
    # -a E^2 + b E + c = 0  ->  a E^2 - b E - c = 0
    E1 = (b + np.sqrt(b*b + 4*a*c))/(2*a)
    N1 = p['K']*(1 - p['q']*E1/p['r'])
    return N1, Zs, E1

def equilibrium_four(p):
    """Four-state equilibrium: solve R(N,A)=qEN and Adot=0 jointly."""
    from scipy.optimize import fsolve
    Aeq = p['A_intr'] + p['kappa_A']*p['K']/p['omega_A']
    Zs = p['delta']
    # E from same quadratic (Z=Zs, ungated same bracket)
    a = p['eta']/p['Emax']; b = p['eta']*Zs/p['Dref']; c = p['delta0']*Zs/(p['Zref']+Zs)
    E1 = (b + np.sqrt(b*b + 4*a*c))/(2*a)
    def sys(x):
        N, A = x
        R = p['r']*N*(1-N/p['K'])*A/(A+p['A0'])
        fN = R - p['q']*E1*N
        Bf = R + p['kappa_A']*N*A/(A+p['A0'])
        fA = -Bf + p['omega_A']*(Aeq - A)
        return [fN, fA]
    sol = fsolve(sys, [89.5, 400.0])
    return sol[0], Zs, E1, Aeq

def jacobian_four(p, state):
    """Numerical 4x4 Jacobian at tau=0 (N,Z,E,A)."""
    N0, Z0, E0, A0 = state
    h = 1e-6
    J = np.zeros((4,4))
    for j in range(4):
        sp = list(state); sm = list(state)
        sp[j] += h; sm[j] -= h
        f_plus = rhs_four(sp[0], sp[1], sp[2], sp[3], Z0, params_arr(p))
        f_minus = rhs_four(sm[0], sm[1], sm[2], sm[3], Z0, params_arr(p))
        for i in range(4):
            J[i, j] = (f_plus[i] - f_minus[i])/(2*h)
    return J

def params_arr(p):
    return np.array([p['r'], p['K'], p['q'], p['eta'], p['Emax'], p['taum'],
                     p['Dref'], p['k'], p['Zref'], p['delta0'], p['delta'],
                     p['kappa_A'], p['omega_A'], p['A_intr'] + p['kappa_A']*p['K']/p['omega_A'],
                     p['A0']], dtype=np.float64)

# ---------------- series capture (for period/amplitude diagnostics) ----------------
@njit(fastmath=True)
def simulate_three_series(N0, Z0, E0, tau, T, dt, p, gated, step_out):
    """Return (N,Z,E) sampled every step_out*dt years."""
    n_delay = max(1, int(round(tau/dt)))
    N, Z, E = N0, Z0, E0
    buf = np.full(n_delay + 1, Z); idx = 0
    n = int(T/dt); out = np.zeros((int(n/step_out), 3)); oi = 0
    for step in range(n):
        Ztau = buf[idx]
        k1N,k1Z,k1E = rhs_three(N,Z,E,Ztau,p,gated)
        k2N,k2Z,k2E = rhs_three(N+dt/2*k1N,Z+dt/2*k1Z,E+dt/2*k1E,Ztau,p,gated)
        k3N,k3Z,k3E = rhs_three(N+dt/2*k2N,Z+dt/2*k2Z,E+dt/2*k2E,Ztau,p,gated)
        k4N,k4Z,k4E = rhs_three(N+dt*k3N,Z+dt*k3Z,E+dt*k3E,Ztau,p,gated)
        N = N + dt/6*(k1N+2*k2N+2*k3N+k4N)
        Z = Z + dt/6*(k1Z+2*k2Z+2*k3Z+k4Z)
        E = E + dt/6*(k1E+2*k2E+2*k3E+k4E)
        if N < 0.0: N = 0.0
        if E < 0.0: E = 0.0
        buf[idx] = Z; idx = (idx + 1) % (n_delay + 1)
        if step % step_out == 0 and oi < out.shape[0]:
            out[oi] = (N, Z, E); oi += 1
    return out
