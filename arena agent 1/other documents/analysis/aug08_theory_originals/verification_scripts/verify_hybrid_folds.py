"""
verify_hybrid_folds.py
======================

Closes the Section (effort-saturation-fix) gap for the additive hybrid effort
law, Eq. (eq:effort-core-hybrid):

    Edot = (1 - E/Emax)*[ eta*E*(Z(t-tau)/Dref - E/Emax)
                          + delta0*Z(t-tau)/(Zref+Z(t-tau)) ] - mu_E*E

with Ndot = S(N) - qEN, Zdot = leaky integrator.  The manuscript verifies the
equilibrium (E*=2.086113 for Candidate A at mu_E=1e-4) and the lower Hopf
(tau_- ~ 3.60 yr), but explicitly states: "the full fold/SNPO analysis of
Section [hopf-verified] has not been repeated for it."  This script:

  [0] validates E* and tau_- (and locates tau_+),
  [1] locates the lower fold tau_SNPO,L (persistence-loss of the large cycle
      just above tau_-) and the upper fold tau_SNPO,R (just below tau_+),
  [2] reports the bistable-window structure and compares with the
      effort-saturation-corrected core (lower fold ~5.574, upper ~148.3).
"""
import numpy as np
from numba import njit
from scipy.optimize import fsolve, brentq

PARAMS_A = dict(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0, Dref=1.0,
                delta0=0.01, Zref=1.0, k=10.0, taum=5.0, mu_E=1e-4)
PARAMS_B = dict(r=0.02, K=100.0, q=0.001, eta=2.756, Emax=26.0, Dref=1.0,
                delta0=0.01, Zref=1.0, k=10.0, taum=5.0, mu_E=1e-4)

@njit(fastmath=True)
def softplus_stable(u, k):
    if k*u > 30.0: return u
    if k*u < -30.0: return 0.0
    return np.log1p(np.exp(k*u))/k

def delta_of(p):
    return np.log(2.0)/p['k']

def Estar_hybrid(p):
    """Solve the cubic (1-E/Emax)*bracket(E) - mu_E*E = 0 on (0, Emax)."""
    eta_, Emax_, Dref_ = p['eta'], p['Emax'], p['Dref']
    delta0_, Zref_ = p['delta0'], p['Zref']
    d = delta_of(p); mu = p['mu_E']
    Zs = d
    def f(E):
        br = eta_*E*(Zs/Dref_ - E/Emax_) + delta0_*Zs/(Zref_ + Zs)
        return (1 - E/Emax_)*br - mu*E
    Es = []
    for guess in np.linspace(0.5, 0.95*Emax_, 60):
        sol = fsolve(f, [guess])
        E = sol[0]
        if 0 < E < Emax_ and abs(f(E)) < 1e-9 and not any(abs(E - e) < 1e-8 for e in Es):
            Es.append(E)
    return Es[0] if Es else None

def equilibrium_hybrid(p):
    E = Estar_hybrid(p)
    r_, K_, q_ = p['r'], p['K'], p['q']
    N = K_*(1 - q_*E/r_)
    return N, delta_of(p), E

@njit(fastmath=True)
def rhs_hybrid(N, Z, Zd, E, pa):
    r_, K_, q_ = pa[0], pa[1], pa[2]
    eta_, Emax_, Dref_ = pa[3], pa[4], pa[5]
    delta0_, Zref_, k_, taum_ = pa[6], pa[7], pa[8], pa[9]
    delta_ = np.log(2.0)/k_; mu_ = pa[10]
    S = r_*N*(1 - N/K_)
    C = q_*E*N
    Ndot = S - C
    inner = softplus_stable(C - S, k_) - np.log(2.0)/k_ + delta_
    Zdot = (np.maximum(0.0, inner) - Z)/taum_
    bracket = eta_*E*(Zd/Dref_ - E/Emax_) + delta0_*Zd/(Zref_ + Zd)
    Edot = (1 - E/Emax_)*bracket - mu_*E
    return Ndot, Zdot, Edot

def pa_of(p):
    return np.array([p['r'], p['K'], p['q'], p['eta'], p['Emax'], p['Dref'],
                     p['delta0'], p['Zref'], p['k'], p['taum'], p['mu_E']])

def char_components(p, state=None):
    """Instantaneous Jacobian J and single delay-coupling B (E-row/Z-col)."""
    if state is None:
        N, Z, E = equilibrium_hybrid(p)
    else:
        N, Z, E = state
    pa = pa_of(p)
    h = 1e-6
    J = np.zeros((3,3))
    st = np.array([N, Z, E])
    for j in range(3):
        sp = st.copy(); sm = st.copy(); sp[j]+=h; sm[j]-=h
        fp = np.array(rhs_hybrid(sp[0], sp[1], st[1], sp[2], pa))  # Zd frozen at Z
        fm = np.array(rhs_hybrid(sm[0], sm[1], st[1], sm[2], pa))
        J[:, j] = (fp - fm)/(2*h)
    # B: dEdot/dZd
    dEdZ = (1 - E/p['Emax'])*(p['eta']*E/p['Dref'] + p['delta0']*p['Zref']/(p['Zref']+Z)**2)
    B = np.zeros((3,3)); B[2,1] = dEdZ
    return J, B, st

def F_lambda(l, tau, J, B):
    return np.linalg.det(l*np.eye(3) - J - B*np.exp(-l*tau))

def PQ(l, J, B):
    n = J.shape[0]
    M = l*np.eye(n) - J
    P = np.linalg.det(M)
    i, j = np.nonzero(np.abs(B) > 1e-300)
    i, j = int(i[0]), int(j[0])
    b = B[i, j]
    minor = np.delete(np.delete(M, i, axis=0), j, axis=1)
    C = ((-1)**(i+j))*np.linalg.det(minor)
    return P, -b*C

def hopf_thresholds(J, B, w_lo=0.001, w_hi=2.0, nw=5000, nmax=8):
    ws = np.linspace(w_lo, w_hi, nw)
    vals = np.array([abs(PQ(1j*w, J, B)[0]) - abs(PQ(1j*w, J, B)[1]) for w in ws])
    taus = []
    for k in range(len(ws)-1):
        if vals[k]*vals[k+1] < 0:
            a, b = ws[k], ws[k+1]; fa, fb = vals[k], vals[k+1]
            for _ in range(60):
                mid = 0.5*(a+b)
                fm = abs(PQ(1j*mid, J, B)[0]) - abs(PQ(1j*mid, J, B)[1])
                if fa*fm <= 0: b, fb = mid, fm
                else: a, fa = mid, fm
            wstar = 0.5*(a+b)
            P, Q = PQ(1j*wstar, J, B)
            phi = np.angle(P/Q)
            for n in range(nmax):
                tau = (-phi - np.pi + 2*np.pi*n)/wstar
                if tau > 0: taus.append((tau, wstar))
    taus.sort()
    out = []
    for tau, w in taus:
        if not out or abs(tau - out[-1][0]) > 0.5:
            out.append((tau, w))
    return out

@njit(fastmath=True)
def sim_hybrid_tail(N0, Z0, E0, tau, T, dt, pa):
    """RK4-DDE; returns final state and the tail amplitude of N (max-min over
    the last 20% of the run) plus the max-min over the whole run."""
    n_delay = max(1, int(round(tau/dt)))
    N, Z, E = N0, Z0, E0
    buf = np.full(n_delay+1, Z); idx = 0
    n_steps = int(T/dt)
    Nmin_all, Nmax_all = N, N
    tail0 = int(0.8*n_steps)
    Nmin_t, Nmax_t = None, None
    for step in range(n_steps):
        Zd = buf[idx]
        k1 = rhs_hybrid(N, Z, Zd, E, pa)
        k2 = rhs_hybrid(N+dt/2*k1[0], Z+dt/2*k1[1], Zd, E+dt/2*k1[2], pa)
        k3 = rhs_hybrid(N+dt/2*k2[0], Z+dt/2*k2[1], Zd, E+dt/2*k2[2], pa)
        k4 = rhs_hybrid(N+dt*k3[0], Z+dt*k3[1], Zd, E+dt*k3[2], pa)
        N = N + dt/6.0*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
        Z = Z + dt/6.0*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        E = E + dt/6.0*(k1[2]+2*k2[2]+2*k3[2]+k4[2])
        if N < 0.0: N = 0.0
        if N < Nmin_all: Nmin_all = N
        if N > Nmax_all: Nmax_all = N
        if step == tail0:
            Nmin_t, Nmax_t = N, N
        elif step > tail0:
            if N < Nmin_t: Nmin_t = N
            if N > Nmax_t: Nmax_t = N
        buf[idx] = Z; idx = (idx+1) % (n_delay+1)
    return N, Z, E, Nmax_all - Nmin_all, Nmax_t - Nmin_t

def cycle_persists(p, tau, T=1e6, dt=0.05, seed='far', tail_frac=0.2):
    """Does a far-from-equilibrium history settle onto a large-amplitude cycle?
    Persistence = tail amplitude (last tail_frac of the run) > 15; this
    separates a true cycle from a long-lived ghost transient (the manuscript's
    critical-slowing-down caution requires >= ~1e6 yr horizons near folds)."""
    Ns, Zs, Es = equilibrium_hybrid(p)
    if seed == 'far':
        N0, Z0, E0 = 1.5*Ns, Zs, 0.4*Es
    else:
        N0, Z0, E0 = Ns*1.02, Zs, Es*1.02
    pa = pa_of(p)
    Nf, Zf, Ef, amp_all, amp_tail = sim_hybrid_tail(N0, Z0, E0, tau, T, dt, pa)
    return amp_tail > 15.0, amp_tail

def bracket_fold(p, a, b, persists_a, T=1e6, dt=0.05, tol=0.02):
    """Bisect the persistence flip on [a,b] (monotone in between)."""
    pa_, _ = cycle_persists(p, a, T, dt)
    pb_, _ = cycle_persists(p, b, T, dt)
    assert pa_ == persists_a and pb_ != persists_a, (a, b, pa_, pb_)
    while b - a > tol:
        mid = 0.5*(a+b)
        pm, _ = cycle_persists(p, mid, T, dt)
        if pm == persists_a: a = mid
        else: b = mid
    return 0.5*(a+b), a, b

if __name__ == "__main__":
    print("="*76)
    print("HYBRID EFFORT LAW (Eq. effort-core-hybrid): fold/Hopf gap closure")
    print("="*76)
    for name, p in [("Candidate A", PARAMS_A), ("Candidate B", PARAMS_B)]:
        print(f"\n--- {name} ---")
        Ns, Zs, Es = equilibrium_hybrid(p)
        print(f"  equilibrium: N*={Ns:.6f}, Z*={Zs:.6f}, E*={Es:.6f}"
              f"  (manuscript: E*=2.086113 for A, 1.804558 for B)")
        J, B, st = char_components(p)
        thr = hopf_thresholds(J, B)
        pos = [t for t, w in thr if t < 5000]
        print(f"  Hopf crossings: {[round(t,4) for t in pos[:4]]}")
        if len(pos) >= 2:
            print(f"    -> tau_- = {pos[0]:.4f}  (manuscript: ~3.60 for A, ~5.51 for B)")
            print(f"       tau_+ = {pos[1]:.4f}")
            tm, tp = pos[0], pos[1]
            # stability check: near-equilibrium sim at a safe interior tau
            mid_tau = 0.5*(tm + tp)
            Ns_, Zs_, Es_ = equilibrium_hybrid(p)
            pa_ = pa_of(p)
            Nf, Zf, Ef, _, _ = sim_hybrid_tail(Ns_*1.02, Zs_, Es_*1.02, mid_tau, 5e5, 0.05, pa_)
            dev = abs(Nf - Ns_)
            print(f"    near-equilibrium at tau={mid_tau:.2f}: |N-N*| after 5e5 yr = {dev:.3e}"
                  + ("  (stable)" if dev < 1.0 else "  (** deviates **)"))
            if name == "Candidate A":
                # locate folds: cycle persists in (tau_-, SNPO,L) and (SNPO,R, tau_+),
                # absent in the wide middle.  Tail amplitude measured over the last
                # 20% of a 1e6-yr run (ghost transients excluded).
                mid_m = 0.5*(tm + tp)
                _, amp_mid = cycle_persists(p, mid_m, T=1e6)
                print(f"    middle tau={mid_m:.1f}: tail amp={amp_mid:.1f} -> "
                      + ("cycle persists (bad)" if amp_mid > 15 else "quiet (expected)"))
                # lower fold: flip between 5.0 (cycle) and 5.6 (quiet)
                t_lo, a_lo, b_lo = bracket_fold(p, 5.0, 5.6, True, T=1e6, tol=0.005)
                print(f"    lower fold tau_SNPO,L in [{a_lo:.4f},{b_lo:.4f}] (midpoint {t_lo:.4f})")
                # upper fold, manuscript-convention history (95,0.01,0.5)
                def tail_ms(tau):
                    return sim_hybrid_tail(95.0, 0.01, 0.5, tau, 1e6, 0.05, pa_of(p))[4]
                a, b = 140.0, 145.0
                for _ in range(45):
                    m = 0.5*(a+b)
                    if tail_ms(m) > 15.0: b = m
                    else: a = m
                t_hi = 0.5*(a+b)
                print(f"    upper fold tau_SNPO,R in [{a:.4f},{b:.4f}] (midpoint {t_hi:.4f})")
                print(f"    bistable windows: ({tm:.3f},{t_lo:.3f}) and ({t_hi:.3f},{tp:.3f})")
                print(f"    wide safe range:  ({t_lo:.3f},{t_hi:.3f})")
                print(f"    (corrected core reference: SNPO,L~5.574, SNPO,R~148.3)")
                print(f"    caveat: near the upper fold the large cycle's basin bleeds into")
                print(f"    the safe range for histories with Z0~=delta or N0>K (verified for")
                print(f"    the corrected core too); the upper fold is seed-dependent within")
                print(f"    [140, 143.5].")
    print("\n  (folds for Candidate B: manuscript located none under the corrected law;")
    print("   only Candidate A's fold structure is checked here, as in the paper)")
