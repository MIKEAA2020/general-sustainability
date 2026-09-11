"""
Shared definitions for the CORRECTED core DDE:
    Ndot = S(N) - q*E*N
    Zdot = (1/taum)*( max(0, softplus_k(qEN-S(N)) - ln2/k + delta) - Z )
    Edot = (1 - E/Emax) * [ eta*E*(Z(t-tau)/Dref - E/Emax) + delta0*Z(t-tau)/(Zref+Z(t-tau)) ]

This is Eq. (eq:effort-core-corrected) in the manuscript: the entire RHS of the
effort equation multiplied by (1-E/Emax), guaranteeing E cannot exceed Emax.

Candidate A parameters (manuscript Table, Section sec:hopf-verified /
sec:effort-saturation-fix):
    r=0.02, K=100, q=0.001, eta=0.914, Emax=30, Dref=1.0,
    delta0=0.01, Zref=1.0, k=10.0, taum=5.0, delta=(ln2/k, baseline)
Relocated Hopf points for Candidate A (corrected equation):
    tau_minus ~ 3.666,  tau_plus ~ 150.359
"""
import numpy as np

PARAMS_A = dict(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0, Dref=1.0,
                 delta0=0.01, Zref=1.0, k=10.0, taum=5.0)
PARAMS_B = dict(r=0.02, K=100.0, q=0.001, eta=2.756, Emax=26.0, Dref=1.0,
                 delta0=0.01, Zref=1.0, k=10.0, taum=5.0)

def softplus(x, k):
    # numerically stable
    return np.logaddexp(0.0, k*x)/k

def equilibrium(params):
    """Closed-form equilibrium (unchanged by the (1-E/Emax) correction, since the
    bracket vanishes at equilibrium regardless of the outer factor)."""
    r_, K_, q_ = params['r'], params['K'], params['q']
    eta_, Emax_, Dref_ = params['eta'], params['Emax'], params['Dref']
    delta0_, Zref_ = params['delta0'], params['Zref']
    delta = np.log(2)/params['k']  # baseline delta chosen = ln2/k as in scratch scripts (Zstar = delta)
    Zstar = delta
    # quadratic: -(eta/Emax) E^2 + eta*(Zstar/Dref) E + delta0*Zstar/(Zref+Zstar) = 0
    a = -eta_/Emax_
    b = eta_*Zstar/Dref_
    c = delta0_*Zstar/(Zref_+Zstar)
    disc = b*b - 4*a*c
    Estar1 = (-b + np.sqrt(disc))/(2*a)
    Estar2 = (-b - np.sqrt(disc))/(2*a)
    Estar = max(Estar1, Estar2) if max(Estar1,Estar2) > 0 else min(Estar1,Estar2)
    # pick the positive one
    cands = [x for x in (Estar1,Estar2) if x > 0]
    Estar = cands[0] if len(cands)==1 else max(cands)
    Nstar = K_*(1 - q_*Estar/r_)
    return Nstar, Zstar, Estar

def rhs_corrected(N, Z, Zd, E, params):
    r_, K_, q_ = params['r'], params['K'], params['q']
    eta_, Emax_, Dref_ = params['eta'], params['Emax'], params['Dref']
    delta0_, Zref_, k_, taum_ = params['delta0'], params['Zref'], params['k'], params['taum']
    delta = np.log(2)/k_
    S = r_*N*(1-N/K_)
    C = q_*E*N
    fN = S - C
    inner = softplus(C - S, k_) - np.log(2)/k_ + delta
    fZ = (1.0/taum_)*(np.maximum(0.0, inner) - Z)
    bracket = eta_*E*(Zd/Dref_ - E/Emax_) + delta0_*Zd/(Zref_ + Zd)
    fE = (1.0 - E/Emax_) * bracket
    return fN, fZ, fE

def simulate(params, tau, T_end, dt, N0, Z0, E0, report_every=1):
    """Fixed-step RK4 DDE integration with a circular buffer for the single delay tau.
    Returns times, N, Z, E arrays (subsampled by report_every)."""
    n_delay = max(1, int(round(tau/dt)))
    n_steps = int(round(T_end/dt))
    # circular buffer of Z history, length n_delay+1 (store Z at each step)
    Zbuf = np.full(n_delay+1, Z0)
    N = N0; Z = Z0; E = E0
    ts = np.empty(n_steps//report_every + 1)
    Ns = np.empty_like(ts); Zs = np.empty_like(ts); Es = np.empty_like(ts)
    idx = 0
    ts[0]=0.0; Ns[0]=N; Zs[0]=Z; Es[0]=E
    buf_ptr = 0
    out_i = 1
    for step in range(1, n_steps+1):
        Zd = Zbuf[(buf_ptr - n_delay) % (n_delay+1)]
        # RK4 (freeze Zd across the substep -- standard approx for smooth delay term)
        k1N, k1Z, k1E = rhs_corrected(N, Z, Zd, E, params)
        k2N, k2Z, k2E = rhs_corrected(N+0.5*dt*k1N, Z+0.5*dt*k1Z, Zd, E+0.5*dt*k1E, params)
        k3N, k3Z, k3E = rhs_corrected(N+0.5*dt*k2N, Z+0.5*dt*k2Z, Zd, E+0.5*dt*k2E, params)
        k4N, k4Z, k4E = rhs_corrected(N+dt*k3N, Z+dt*k3Z, Zd, E+dt*k3E, params)
        N = N + (dt/6.0)*(k1N+2*k2N+2*k3N+k4N)
        Z = Z + (dt/6.0)*(k1Z+2*k2Z+2*k3Z+k4Z)
        E = E + (dt/6.0)*(k1E+2*k2E+2*k3E+k4E)
        N = max(N, 0.0)
        E = max(0.0, min(E, params['Emax']))  # corrected eq should already enforce this to within numerical tol
        buf_ptr = (buf_ptr+1) % (n_delay+1)
        Zbuf[buf_ptr] = Z
        if step % report_every == 0:
            ts[out_i]=step*dt; Ns[out_i]=N; Zs[out_i]=Z; Es[out_i]=E
            out_i += 1
    return ts[:out_i], Ns[:out_i], Zs[:out_i], Es[:out_i]
