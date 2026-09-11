"""
fourstate_pipeline.py
=====================

Four-state core machinery for the donor-limited-equilibrium pipeline recompute.

Model (manuscript Eqs. fourstate-N / fourstate-A / Z-core / effort-core):
    Ndot  = R(N,A) - q*E*N
    Adot  = -B(N,A) + omega_A*(A_eq - A)
    Zdot  = (max(0, softplus_k(q*E*N - R(N,A)) - ln2/k + delta) - Z)/tau_m
    Edot  = eta*E*(Z(t-tau)/Dref - E/Emax) + delta0*Z(t-tau)/(Zref+Z(t-tau))   [UNGATED]
with
    R(N,A) = r*N*(1-N/K)*A/(A+A0)
    B(N,A) = R + kappa_A*N*A/(A+A0)          [donor-limited, corrected form]
    A_eq   = A_intr + kappa_A*K/omega_A      [D_ret = 0 for the four-state core]

Candidate A: r=0.02, K=100, q=0.001, eta=0.914, Emax=30, Dref=1.0, delta0=0.01,
Zref=1.0, tau_m=5, k=10, delta=ln2/10, kappa_A=0.05, omega_A=1e-3, A_intr=50,
A0=1.0, A_eq = 5050.

The PRE-correction (old) form used B = R + kappa_A*N (undivided turnover); the
post-correction (new) form uses B = R + kappa_A*N*A/(A+A0).  This module
implements both so the old numbers can be validated and the new pipeline
recomputed.
"""
import numpy as np
from numba import njit
from scipy.optimize import fsolve

# ---------------- parameters ----------------
def FOUR_PARAMS():
    return dict(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0, Dref=1.0,
                delta0=0.01, Zref=1.0, taum=5.0, k=10.0, delta=np.log(2.0)/10.0,
                kappa_A=0.05, omega_A=1e-3, A_intr=50.0, A0=1.0)

def four_arr(p=None):
    p = p or FOUR_PARAMS()
    Aeq = p['A_intr'] + p['kappa_A']*p['K']/p['omega_A']
    return np.array([p['r'], p['K'], p['q'], p['eta'], p['Emax'], p['taum'],
                     p['Dref'], p['k'], p['Zref'], p['delta0'], p['delta'],
                     p['kappa_A'], p['omega_A'], Aeq, p['A0']], dtype=np.float64)

@njit(fastmath=True)
def softplus_stable(u, k):
    if k*u > 30.0:
        return u
    if k*u < -30.0:
        return 0.0
    return np.log1p(np.exp(k*u))/k

@njit(fastmath=True)
def rhs_four(N, Z, E, A, Ztau, pa, donor):
    """donor=1: donor-limited turnover; donor=0: undivided turnover (old form)."""
    r_, K_, q_ = pa[0], pa[1], pa[2]
    eta_, Emax_, Dref_ = pa[3], pa[4], pa[6]
    delta0_, Zref_, k_, taum_ = pa[9], pa[8], pa[7], pa[5]
    delta_ = pa[10]; kA_ = pa[11]; omA_ = pa[12]; Aeq_ = pa[13]; A0_ = pa[14]
    R = r_*N*(1 - N/K_)*A/(A + A0_)
    if donor:
        B = R + kA_*N*A/(A + A0_)
    else:
        B = R + kA_*N
    Ndot = R - q_*E*N
    Adot = -B + omA_*(Aeq_ - A)
    u = q_*E*N - R
    sp = softplus_stable(u, k_)
    inner = sp - np.log(2.0)/k_ + delta_
    Zdot = ((inner if inner > 0.0 else 0.0) - Z)/taum_
    Edot = eta_*E*(Ztau/Dref_ - E/Emax_) + delta0_*Ztau/(Zref_ + Ztau)
    return Ndot, Zdot, Edot, Adot

def Estar(p=None):
    p = p or FOUR_PARAMS()
    Zs = p['delta']
    a = p['eta']/p['Emax']; b = p['eta']*Zs/p['Dref']; c = p['delta0']*Zs/(p['Zref']+Zs)
    return (b + np.sqrt(b*b + 4*a*c))/(2*a)

def equilibrium(p=None, donor=1):
    """Solve N*, A* at fixed E* (closed form). Returns (N*, A*, E*, A_eq)."""
    p = p or FOUR_PARAMS()
    pa = four_arr(p)
    E1 = Estar(p)
    Aeq = pa[13]
    def sys(x):
        N, A = x
        R = pa[0]*N*(1-N/pa[1])*A/(A+pa[14])
        if donor:
            B = R + pa[11]*N*A/(A+pa[14])
        else:
            B = R + pa[11]*N
        return [R - pa[2]*E1*N, -B + pa[12]*(Aeq - A)]
    sol = fsolve(sys, [89.5, 400.0])
    return sol[0], sol[1], E1, Aeq

def jacobian_tau0(p=None, donor=1, state=None):
    """Full tau=0 Jacobian (delay coupling folded in: Z_tau = Z)."""
    p = p or FOUR_PARAMS()
    pa = four_arr(p)
    if state is None:
        N, A, E1, Aeq = equilibrium(p, donor)
        Z = p['delta']; E = E1
    else:
        N, Z, E, A = state
    h = 1e-6
    J = np.zeros((4,4))
    st = np.array([N, Z, E, A])
    for j in range(4):
        sp = st.copy(); sm = st.copy(); sp[j]+=h; sm[j]-=h
        fp = np.array(rhs_four(sp[0], sp[1], sp[2], sp[3], sp[1], pa, donor))  # Ztau=Z at tau=0
        fm = np.array(rhs_four(sm[0], sm[1], sm[2], sm[3], sm[1], pa, donor))
        J[:, j] = (fp - fm)/(2*h)
    return J, st

def char_eq_components(p=None, donor=1, state=None):
    """Return (J_local, B_delay, st): instantaneous Jacobian (no delay coupling),
    delay-coupling matrix B (only the E-row/Z-col entry), and equilibrium state."""
    p = p or FOUR_PARAMS()
    pa = four_arr(p)
    if state is None:
        N, A, E1, Aeq = equilibrium(p, donor)
        Z = p['delta']; E = E1
    else:
        N, Z, E, A = state
    h = 1e-6
    # J_local: freeze Z_tau at Z (constant), differentiate RHS wrt (N,Z,E,A) with Ztau fixed
    J = np.zeros((4,4))
    st = np.array([N, Z, E, A])
    for j in range(4):
        sp = st.copy(); sm = st.copy(); sp[j]+=h; sm[j]-=h
        fp = np.array(rhs_four(sp[0], sp[1], sp[2], sp[3], Z, pa, donor))
        fm = np.array(rhs_four(sm[0], sm[1], sm[2], sm[3], Z, pa, donor))
        J[:, j] = (fp - fm)/(2*h)
    # B_delay: dEdot/dZ_tau
    dEdZ = pa[3]*E/pa[6] + pa[9]*pa[8]/(pa[8]+Z)**2
    B = np.zeros((4,4)); B[2,1] = dEdZ
    # note: at tau=0 the system matrix is J + B (Z_tau = Z)
    return J, B, st

def det_char(l, tau, J, B):
    return np.linalg.det(l*np.eye(4) - J - B*np.exp(-l*tau))

# ---------------- DDE simulation (numba) ----------------
@njit(fastmath=True)
def sim_four(N0, Z0, E0, A0, tau, T, dt, pa, donor):
    """Fixed-step RK4-DDE, four-state. Returns (final N,Z,E,A, tail amplitude)."""
    n_delay = max(1, int(round(tau/dt)))
    N, Z, E, A = N0, Z0, E0, A0
    buf = np.full(n_delay+1, Z); idx = 0
    n_steps = int(T/dt)
    Nmin = N; Nmax = N
    for step in range(n_steps):
        Ztau = buf[idx]
        k1N,k1Z,k1E,k1A = rhs_four(N,Z,E,A,Ztau,pa,donor)
        k2N,k2Z,k2E,k2A = rhs_four(N+dt/2*k1N,Z+dt/2*k1Z,E+dt/2*k1E,A+dt/2*k1A,Ztau,pa,donor)
        k3N,k3Z,k3E,k3A = rhs_four(N+dt/2*k2N,Z+dt/2*k2Z,E+dt/2*k2E,A+dt/2*k2A,Ztau,pa,donor)
        k4N,k4Z,k4E,k4A = rhs_four(N+dt*k3N,Z+dt*k3Z,E+dt*k3E,A+dt*k3A,Ztau,pa,donor)
        N = N + dt/6.0*(k1N+2*k2N+2*k3N+k4N)
        Z = Z + dt/6.0*(k1Z+2*k2Z+2*k3Z+k4Z)
        E = E + dt/6.0*(k1E+2*k2E+2*k3E+k4E)
        A = A + dt/6.0*(k1A+2*k2A+2*k3A+k4A)
        if N < 0.0: N = 0.0
        if N < Nmin: Nmin = N
        if N > Nmax: Nmax = N
        buf[idx] = Z; idx = (idx+1) % (n_delay+1)
    return N, Z, E, A, Nmax - Nmin

@njit(fastmath=True)
def sim_four_series(N0, Z0, E0, A0, tau, T, dt, pa, donor, step_out):
    """Return (N,Z,E,A) sampled every step_out*dt years."""
    n_delay = max(1, int(round(tau/dt)))
    N, Z, E, A = N0, Z0, E0, A0
    buf = np.full(n_delay+1, Z); idx = 0
    n_steps = int(T/dt)
    out = np.zeros((int(n_steps/step_out), 4)); oi = 0
    for step in range(n_steps):
        Ztau = buf[idx]
        k1N,k1Z,k1E,k1A = rhs_four(N,Z,E,A,Ztau,pa,donor)
        k2N,k2Z,k2E,k2A = rhs_four(N+dt/2*k1N,Z+dt/2*k1Z,E+dt/2*k1E,A+dt/2*k1A,Ztau,pa,donor)
        k3N,k3Z,k3E,k3A = rhs_four(N+dt/2*k2N,Z+dt/2*k2Z,E+dt/2*k2E,A+dt/2*k2A,Ztau,pa,donor)
        k4N,k4Z,k4E,k4A = rhs_four(N+dt*k3N,Z+dt*k3Z,E+dt*k3E,A+dt*k3A,Ztau,pa,donor)
        N = N + dt/6.0*(k1N+2*k2N+2*k3N+k4N)
        Z = Z + dt/6.0*(k1Z+2*k2Z+2*k3Z+k4Z)
        E = E + dt/6.0*(k1E+2*k2E+2*k3E+k4E)
        A = A + dt/6.0*(k1A+2*k2A+2*k3A+k4A)
        if N < 0.0: N = 0.0
        buf[idx] = Z; idx = (idx+1) % (n_delay+1)
        if step % step_out == 0 and oi < out.shape[0]:
            out[oi,0]=N; out[oi,1]=Z; out[oi,2]=E; out[oi,3]=A; oi += 1
    return out[:oi]

# ---------------- kappa_A threshold ----------------
def kappaA_threshold(p=None, donor=1, lo=1e-5, hi=0.02):
    """Bisect the kappa_A value where the tau=0 Jacobian's rightmost eigenvalue
    crosses zero (linear stability flip at tau=0)."""
    from scipy.optimize import brentq
    def rightmost(kA):
        pp = dict(p or FOUR_PARAMS()); pp['kappa_A'] = kA
        J, st = jacobian_tau0(pp, donor)
        ev = np.linalg.eigvals(J)
        return max(ev.real)
    # bracket
    rlo, rhi = rightmost(lo), rightmost(hi)
    if rlo*rhi > 0:
        return None, rlo, rhi
    x = brentq(lambda kA: rightmost(kA), lo, hi, xtol=1e-9)
    return x, rightmost(x), None
