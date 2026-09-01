"""
DDE-BIFTOOL-style periodic-orbit continuation with Floquet-multiplier tracking
for the manuscript's three-state and four-state core models.

Method
------
* Fixed-step, method-of-lines DDE integration (explicit RK4) with linear
  history interpolation for the delayed term Z(t-tau).
* Single shooting: a periodic orbit is a fixed point of the stroboscopic map
  Phi_T(y0; history) = y0, where y0 = (N(0), Z(0), E(0)) and T is the period.
* Newton continuation in tau, with natural parameter continuation (the orbit at
  tau_n is used as the predictor for tau_{n+1}).
* Floquet multipliers: eigenvalues of the monodromy matrix D Phi_T / D y0,
  obtained by integrating the 3x3 (or 4x4) variational equation alongside
  the trajectory. One multiplier is always ~1 (phase mode); a *second*
  multiplier reaching +1 with non-tangent eigenvector is the defining
  signature of a saddle-node of periodic orbits (SNPO / fold of cycles).
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Callable, Tuple, List, Optional, Dict


# ---------------------------------------------------------------------------
# Model definitions
# ---------------------------------------------------------------------------

def softplus(x, k):
    """Numerically stable softplus."""
    # softplus_k(x) = (1/k) ln(1 + exp(k x))
    if np.isscalar(x):
        kx = k * x
        if kx > 50:
            return x
        if kx < -50:
            return 0.0
        return np.log1p(np.exp(kx)) / k
    kx = k * x
    out = np.empty_like(x)
    hi = kx > 50
    lo = kx < -50
    mid = ~(hi | lo)
    out[hi] = x[hi]
    out[lo] = 0.0
    out[mid] = np.log1p(np.exp(kx[mid])) / k
    return out


def softplus_deriv(x, k):
    """d/dx softplus_k(x) = sigmoid(k x).  At x=0 this is 1/2 for any k."""
    kx = k * x
    if np.isscalar(kx):
        if kx > 50:
            return 1.0
        if kx < -50:
            return 0.0
        return 1.0 / (1.0 + np.exp(-kx))
    out = np.empty_like(kx)
    hi = kx > 50
    lo = kx < -50
    mid = ~(hi | lo)
    out[hi] = 1.0
    out[lo] = 0.0
    out[mid] = 1.0 / (1.0 + np.exp(-kx[mid]))
    return out


@dataclass
class CoreParams:
    r: float = 0.02
    K: float = 100.0
    q: float = 0.001
    eta: float = 0.914
    Emax: float = 30.0
    delta0: float = 0.01
    Dref: float = 1.0
    tau_m: float = 5.0
    Zref: float = 1.0
    k: float = 10.0
    delta: float = np.log(2.0) / 10.0  # baseline-panic deficit
    gated: bool = False  # True = effort-saturation-corrected core (Eq 17)
    fourstate: bool = False
    kappaA: float = 0.05
    omegaA: float = 1e-3
    A0: float = 1.0  # 0.01 K
    Aeq_intrinsic: float = 50.0  # 0.5 K
    psi: float = 1.0  # liquidation channel (1 = pure stock culling)

    def Aeq(self):
        """Eq (12): A^{act,eq} = Aeq_intrinsic + (kappa_A K - Dret)/omega_A.
        Four-state core has no detritus, so Dret=0."""
        if self.fourstate:
            return self.Aeq_intrinsic + self.kappaA * self.K / self.omegaA
        return self.Aeq_intrinsic


def equilibrium(p: CoreParams):
    """Closed-form interior equilibrium of the three-state core
    (Section 'equilibrium-core', Eqs around E-star-quadratic).
    Z* = delta; E* solves the quadratic from dE/dt=0; N* = K(1-qE*/r).
    For the four-state core, (N*, A*) are found numerically, but E*, Z* are
    unchanged (manuscript, Section 'four-state-model').
    """
    Zs = p.delta
    # eta/Emax * E^2  -  eta*Zs/Dref * E  -  delta0*Zs/(Zref+Zs) = 0  with sign
    #  dE/dt = eta E (Zs/Dref - E/Emax) + delta0 Zs/(Zref+Zs) = 0
    #  => -(eta/Emax) E^2 + eta Zs/Dref E + delta0 Zs/(Zref+Zs) = 0
    a = -p.eta / p.Emax
    b = p.eta * Zs / p.Dref
    c = p.delta0 * Zs / (p.Zref + Zs)
    disc = b * b - 4 * a * c
    Es = (-b - np.sqrt(disc)) / (2 * a)  # positive root
    if not p.fourstate:
        Ns = p.K * (1.0 - p.q * Es / p.r)
        return np.array([Ns, Zs, Es])
    # four-state: solve N, A from dot N=0, dot A=0 at fixed E*, Z*=delta
    Ns, As = _fourstate_equilibrium(p, Es)
    return np.array([Ns, Zs, Es, As])


def _fourstate_equilibrium(p: CoreParams, Es: float):
    """Solve the coupled (N,A) equilibrium of the four-state core at fixed E*.

    dot N = r N (1-N/K) * A/(A+A0) - q E N = 0
    dot A = -B + omega_A (Aeq - A) = 0
    where B = R + kappa_A N * A/(A+A0), R = r N(1-N/K)*A/(A+A0).
    So dot A = -(R + kappa_A N A/(A+A0)) + omega_A(Aeq - A) = 0.
    From dot N=0: r(1-N/K) A/(A+A0) = q E => R = q E N.
    Thus dot A = -q E N - kappa_A N A/(A+A0) + omega_A(Aeq-A) = 0.
    Use Newton on (N,A).
    """
    Aeq = p.Aeq()
    # initial guess: frozen-A limit
    N = p.K * (1 - p.q * Es / p.r)
    A = Aeq
    for _ in range(200):
        fA = A / (A + p.A0)
        R = p.r * N * (1 - N / p.K) * fA
        B = R + p.kappaA * N * fA
        f1 = R - p.q * Es * N
        f2 = -B + p.omegaA * (Aeq - A)
        # Jacobian
        dR_dN = p.r * (1 - 2 * N / p.K) * fA
        dR_dA = p.r * N * (1 - N / p.K) * p.A0 / (A + p.A0) ** 2
        dB_dN = dR_dN + p.kappaA * fA
        dB_dA = dR_dA + p.kappaA * N * p.A0 / (A + p.A0) ** 2
        J = np.array([[dR_dN - p.q * Es, dR_dA],
                      [-dB_dN, -dB_dA - p.omegaA]])
        rhs = -np.array([f1, f2])
        step = np.linalg.solve(J, rhs)
        N += step[0]
        A += step[1]
        if np.max(np.abs(step)) < 1e-14:
            break
    return N, A


# ---------------------------------------------------------------------------
# DDE right-hand side and variational RHS
# ---------------------------------------------------------------------------

def _gating(p: CoreParams, E):
    if not p.gated:
        return 1.0
    return 1.0 - E / p.Emax


def rhs(state, delayed_state, p: CoreParams):
    """Evaluate the DDE right-hand side.

    Three-state core (Eq 14-16):
        dot N = S(N) - q E N
        dot Z = (1/tau_m)[ max(0, softplus_k(qEN-S(N)) - ln2/k + delta) - Z ]
        dot E = g(E) [ eta E (Z(t-tau)/Dref - E/Emax)
                        + delta0 Z(t-tau)/(Zref + Z(t-tau)) ]
    Four-state core adds:
        dot A = -B + omega_A (Aeq - A)
    """
    if p.fourstate:
        N, Z, E, A = state
        Nd, Zd, Ed = delayed_state[0], delayed_state[2], delayed_state[1]
        # Zd is actually delayed Z; note delayed_state layout = state at t-tau
        Ztau = delayed_state[1]
        fA = A / (A + p.A0)
        R = p.r * N * (1 - N / p.K) * fA
        S = R  # regeneration depends on A in four-state core
        B = R + p.kappaA * N * fA
        qEN = p.q * E * N
        dN = R - qEN
        src = max(0.0, softplus(qEN - S, p.k) - np.log(2.0) / p.k + p.delta)
        dZ = (src - Z) / p.tau_m
        gate = _gating(p, E)
        dE = gate * (p.eta * E * (Ztau / p.Dref - E / p.Emax)
                     + p.delta0 * Ztau / (p.Zref + Ztau))
        dA = -B + p.omegaA * (p.Aeq() - A)
        return np.array([dN, dZ, dE, dA])
    else:
        N, Z, E = state
        Ztau = delayed_state[1]
        S = p.r * N * (1 - N / p.K)
        qEN = p.q * E * N
        dN = S - qEN
        src = max(0.0, softplus(qEN - S, p.k) - np.log(2.0) / p.k + p.delta)
        dZ = (src - Z) / p.tau_m
        gate = _gating(p, E)
        dE = gate * (p.eta * E * (Ztau / p.Dref - E / p.Emax)
                     + p.delta0 * Ztau / (p.Zref + Ztau))
        return np.array([dN, dZ, dE])


def jacobians(state, delayed_state, p: CoreParams):
    """Return (J0, Jtau): derivatives of rhs w.r.t. current state and delayed
    state, used to integrate the variational equation.

    Variational eq: dot W = J0 W + Jtau W(t-tau), where W is n x n.
    """
    if p.fourstate:
        N, Z, E, A = state
        Ztau = delayed_state[1]
        fA = A / (A + p.A0)
        fA_A = p.A0 / (A + p.A0) ** 2
        R = p.r * N * (1 - N / p.K) * fA
        S = R
        qEN = p.q * E * N
        d = qEN - S
        sp = softplus(d, p.k)
        sp_d = softplus_deriv(d, p.k)
        src = sp - np.log(2.0) / p.k + p.delta
        floor_active = src < 0
        h = 0.0 if floor_active else sp_d  # d src / d d
        # dS/dN, dS/dA
        dS_dN = p.r * (1 - 2 * N / p.K) * fA
        dS_dA = p.r * N * (1 - N / p.K) * fA_A
        # d(qEN - S)/dN = qE - dS_dN ; d/dE = qN ; d/dA = -dS_dA
        dd_dN = p.q * E - dS_dN
        dd_dE = p.q * N
        dd_dA = -dS_dA
        # dot N
        dN_N = dS_dN - p.q * E
        dN_E = -p.q * N
        dN_A = dS_dA
        # dot Z = (1/tau_m)[max(0, src_raw) - Z]
        dZ_N = h * dd_dN / p.tau_m
        dZ_E = h * dd_dE / p.tau_m
        dZ_Z = -1.0 / p.tau_m
        dZ_A = h * dd_dA / p.tau_m
        # dot E
        gate = _gating(p, E)
        dgate_E = 0.0 if not p.gated else -1.0 / p.Emax
        fbracket = (p.eta * E * (Ztau / p.Dref - E / p.Emax)
                    + p.delta0 * Ztau / (p.Zref + Ztau))
        dE_E = (dgate_E * fbracket
                + gate * p.eta * (Ztau / p.Dref - 2 * E / p.Emax))
        dE_Ztau = gate * (p.eta * E / p.Dref
                          + p.delta0 * p.Zref / (p.Zref + Ztau) ** 2)
        # dot A
        B = R + p.kappaA * N * fA
        dB_dN = dS_dN + p.kappaA * fA
        dB_dA = dS_dA + p.kappaA * N * fA_A
        dA_N = -dB_dN
        dA_A = -dB_dA - p.omegaA
        J0 = np.array([[dN_N, 0, dN_E, dN_A],
                       [dZ_N, dZ_Z, dZ_E, dZ_A],
                       [0, 0, dE_E, 0],
                       [dA_N, 0, 0, dA_A]])
        Jtau = np.zeros((4, 4))
        Jtau[2, 1] = dE_Ztau
        return J0, Jtau
    else:
        N, Z, E = state
        Ztau = delayed_state[1]
        S = p.r * N * (1 - N / p.K)
        dS_dN = p.r * (1 - 2 * N / p.K)
        qEN = p.q * E * N
        d = qEN - S
        sp = softplus(d, p.k)
        sp_d = softplus_deriv(d, p.k)
        src = sp - np.log(2.0) / p.k + p.delta
        floor_active = src < 0
        h = 0.0 if floor_active else sp_d
        dd_dN = p.q * E - dS_dN
        dd_dE = p.q * N
        dN_N = dS_dN - p.q * E
        dN_E = -p.q * N
        dZ_N = h * dd_dN / p.tau_m
        dZ_E = h * dd_dE / p.tau_m
        dZ_Z = -1.0 / p.tau_m
        gate = _gating(p, E)
        dgate_E = 0.0 if not p.gated else -1.0 / p.Emax
        fbracket = (p.eta * E * (Ztau / p.Dref - E / p.Emax)
                    + p.delta0 * Ztau / (p.Zref + Ztau))
        dE_E = (dgate_E * fbracket
                + gate * p.eta * (Ztau / p.Dref - 2 * E / p.Emax))
        dE_Ztau = gate * (p.eta * E / p.Dref
                          + p.delta0 * p.Zref / (p.Zref + Ztau) ** 2)
        J0 = np.array([[dN_N, 0.0, dN_E],
                       [dZ_N, dZ_Z, dZ_E],
                       [0.0, 0.0, dE_E]])
        Jtau = np.zeros((3, 3))
        Jtau[2, 1] = dE_Ztau
        return J0, Jtau


# ---------------------------------------------------------------------------
# Fixed-step RK4 DDE integrator with linear history interpolation,
# simultaneously integrating the n x n variational matrix W.
# ---------------------------------------------------------------------------

def integrate_dde(y0, history_func, T, p: CoreParams, dt,
                  compute_monodromy=False, history_W=None):
    """Integrate from t=0 to t=T with RK4 using step h that divides T evenly
    (h = T/round(T/dt), so h is close to dt but T is hit exactly).  The
    delayed state is linearly interpolated from the on-grid trajectory; for
    t in [-tau,0] it uses history_func.

    Returns (yT, W(T), ts, ys).
    """
    n = len(y0)
    nsteps = max(int(round(T / dt)), 8)
    h = T / nsteps
    ts = np.linspace(0, T, nsteps + 1)
    ys = np.zeros((nsteps + 1, n))
    ys[0] = y0
    if compute_monodromy:
        W = np.eye(n) if history_W is None else history_W.copy()
        Ws = np.zeros((nsteps + 1, n, n))
        Ws[0] = W
    else:
        W = None
        Ws = None

    # On-grid delayed interpolation.  (t-tau) may lie in [-tau, T]; map to
    # a fractional index on [0,nsteps] for t>=0, else use history_func.
    def delayed_state(t):
        if t <= 0:
            return history_func(t)
        ti = t / h
        i = int(np.floor(ti))
        if i >= nsteps:
            return ys[nsteps]
        frac = ti - i
        return (1 - frac) * ys[i] + frac * ys[i + 1]

    def delayed_W(t):
        if t <= 0:
            return np.zeros((n, n))
        ti = t / h
        i = int(np.floor(ti))
        if i >= nsteps:
            return Ws[nsteps]
        frac = ti - i
        return (1 - frac) * Ws[i] + frac * Ws[i + 1]

    for i in range(nsteps):
        t = ts[i]
        y = ys[i]
        if compute_monodromy:
            W = Ws[i]
            yd1 = delayed_state(t - p.tau)
            J0_1, Jt_1 = jacobians(y, yd1, p)
            k1 = rhs(y, yd1, p)
            kW1 = J0_1 @ W + Jt_1 @ delayed_W(t - p.tau)
            ymid = y + h / 2 * k1
            yd2 = delayed_state(t + h / 2 - p.tau)
            J0_2, Jt_2 = jacobians(ymid, yd2, p)
            k2 = rhs(ymid, yd2, p)
            kW2 = J0_2 @ (W + h / 2 * kW1) + Jt_2 @ delayed_W(
                t + h / 2 - p.tau)
            ymid2 = y + h / 2 * k2
            J0_3, Jt_3 = jacobians(ymid2, yd2, p)
            k3 = rhs(ymid2, yd2, p)
            kW3 = J0_3 @ (W + h / 2 * kW2) + Jt_3 @ delayed_W(
                t + h / 2 - p.tau)
            yend = y + h * k3
            yd4 = delayed_state(t + h - p.tau)
            J0_4, Jt_4 = jacobians(yend, yd4, p)
            k4 = rhs(yend, yd4, p)
            kW4 = J0_4 @ (W + h * kW3) + Jt_4 @ delayed_W(t + h - p.tau)
            ys[i + 1] = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            Ws[i + 1] = W + h / 6 * (kW1 + 2 * kW2 + 2 * kW3 + kW4)
        else:
            yd1 = delayed_state(t - p.tau)
            k1 = rhs(y, yd1, p)
            yd2 = delayed_state(t + h / 2 - p.tau)
            k2 = rhs(y + h / 2 * k1, yd2, p)
            k3 = rhs(y + h / 2 * k2, yd2, p)
            yd4 = delayed_state(t + h - p.tau)
            k4 = rhs(y + h * k3, yd4, p)
            ys[i + 1] = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return ys[-1], (Ws[-1] if compute_monodromy else None), ts, ys


def _rhs_with_jac(y, yd, p, W, delayed_W, tdelay):
    f = rhs(y, yd, p)
    J0, Jtau = jacobians(y, yd, p)
    Wd = delayed_W(tdelay)
    dW = J0 @ W + Jtau @ Wd
    return f, dW


# ---------------------------------------------------------------------------
# Periodic orbit via single shooting + Newton, with phase condition.
# ---------------------------------------------------------------------------

@dataclass
class OrbitResult:
    y0: np.ndarray
    period: float
    tau: float
    converged: bool
    residual: float
    monodromy: Optional[np.ndarray] = None
    multipliers: Optional[np.ndarray] = None
    ts: Optional[np.ndarray] = None
    ys: Optional[np.ndarray] = None
    history: Optional[np.ndarray] = None
    nits: int = 0


def _periodic_history(ys, ts, T, tau):
    """Build a periodic history function and its grid samples from one
    converged period [0,T]. For t in [-tau,0], return y(T+t)."""
    dt = ts[1] - ts[0]

    n = ys.shape[1]
    def hfunc(t, n=n):
        # t <= 0
        return np.array([np.interp(t + T, ts, ys[:, j], period=T)
                         for j in range(n)])
    # also return a sampled array on [-tau, 0] for use as initial history
    nh = max(int(np.ceil(tau / dt)), 4)
    ht = np.linspace(-tau, 0, nh + 1)
    hvals = np.array([hfunc(tt) for tt in ht])
    return hfunc, ht, hvals


def shoot_orbit(y0_guess, T_guess, tau, p: CoreParams, dt,
                history_seed=None, maxit=60, tol=1e-9,
                free_period=True, phase_anchor_idx=0,
                phase_anchor_val=None, verbose=False,
                fp_iterations=8):
    """Find a periodic orbit of the DDE at delay tau by single shooting.

    The unknown is (y0, T).  We enforce Phi_T(y0) = y0 and a phase condition
    anchoring one component of y0.  Before Newton we run a few fixed-point
    (Picard) iterations on the period map with the history rebuilt from each
    successive orbit, which is robust to rough initial guesses.
    """
    p.tau = tau
    n = len(y0_guess)
    y0 = y0_guess.copy().astype(float)
    T = float(T_guess)
    if phase_anchor_val is None:
        phase_anchor_val = float(y0[phase_anchor_idx])
    anchor_target = phase_anchor_val

    eq = equilibrium(p)
    if history_seed is None:
        ht = np.linspace(-tau, 0, 32)
        hvals = np.tile(eq, (len(ht), 1))
        def hfunc(t):
            return eq
    else:
        ht, hvals = history_seed
        def hfunc(t, ht=ht, hvals=hvals, n=n):
            return np.array([np.interp(t, ht, hvals[:, j],
                                       period=tau + 1e-9) for j in range(n)])

    # --- Picard fixed-point iterations to refine seed, with phase anchor ---
    for _ in range(fp_iterations):
        yT, _, ts, ys = integrate_dde(y0, hfunc, T, p, dt,
                                      compute_monodromy=False)
        # measure period from the trajectory
        N = ys[:, 0]
        meanN = N.mean()
        cross = [j for j in range(1, len(N))
                 if N[j - 1] < meanN <= N[j]]
        if len(cross) >= 2:
            T = float(np.median(np.diff(cross))) * dt
        # re-segment so that y0 is at the point where the anchor component
        # crosses its target value upward (phase condition)
        anchor = ys[:, phase_anchor_idx]
        # find first index where anchor crosses target from below, near start
        shift = 0
        for j in range(1, len(anchor) - 1):
            if anchor[j - 1] < anchor_target <= anchor[j]:
                shift = j
                break
        if shift > 0:
            ys = np.roll(ys, -shift, axis=0)
            y0_new = ys[0].copy()
        else:
            y0_new = yT.copy()
        hfunc, ht, hvals = _periodic_history(ys, ts, T, tau)
        y0 = y0_new

    last_res = np.inf
    for it in range(maxit):
        yT, Wmono, ts, ys = integrate_dde(y0, hfunc, T, p, dt,
                                          compute_monodromy=True)
        res = yT - y0
        hfunc_new, ht_new, hvals_new = _periodic_history(ys, ts, T, tau)
        f_T = rhs(y0, hfunc_new(0 - tau), p)

        A = np.zeros((n + 1, n + 1))
        A[:n, :n] = Wmono - np.eye(n)
        A[:n, n] = f_T
        A[n, phase_anchor_idx] = 1.0
        rhs_vec = np.zeros(n + 1)
        rhs_vec[:n] = -res
        rhs_vec[n] = -(y0[phase_anchor_idx] - anchor_target)

        try:
            sol, *_ = np.linalg.lstsq(A, rhs_vec, rcond=None)
        except np.linalg.LinAlgError:
            if verbose:
                print(f"  singular Jacobian at it {it}")
            break
        dy = sol[:n]
        dT = sol[n]

        # line search: reduce residual norm
        cur_norm = np.linalg.norm(res)
        best_scale = 0.0
        best_norm = cur_norm
        best_state = (y0.copy(), T, (ht, hvals))
        for scale in [1.0, 0.5, 0.25, 0.1, 0.05, 0.02, 0.01, 0.005, 0.001]:
            y0n = y0 + scale * dy
            Tn = T + scale * dT
            if Tn < dt * 4:
                continue
            if y0n[0] <= 0 or y0n[2] < -0.1:
                continue
            try:
                yTn, _, _, _ = integrate_dde(y0n, hfunc_new, Tn, p, dt,
                                             compute_monodromy=False)
                rn = np.linalg.norm(yTn - y0n)
                if rn < best_norm:
                    best_norm = rn
                    best_scale = scale
                    best_state = (y0n, Tn, None)
            except (FloatingPointError, OverflowError, ValueError):
                continue
        if best_scale == 0.0:
            # accept a small step anyway if residual is already small
            if cur_norm < 1e-3:
                if verbose:
                    print(f"  accepting small-res state at it {it}, res={cur_norm:.2e}")
                break
            if verbose:
                print(f"  line search failed at it {it}, res={cur_norm:.2e}")
            break
        y0, T, _ = best_state
        hfunc = hfunc_new
        ht, hvals = ht_new, hvals_new
        r = best_norm
        if verbose and (it % 3 == 0 or r < tol * 100):
            print(f"  it {it}: res={r:.2e}, T={T:.4f}, scale={best_scale}")
        last_res = r
        if r < tol:
            # final monodromy with converged state
            yT, Wmono, ts, ys = integrate_dde(y0, hfunc, T, p, dt,
                                              compute_monodromy=True)
            return OrbitResult(y0=y0, period=T, tau=tau, converged=True,
                               residual=r, monodromy=Wmono,
                               multipliers=np.linalg.eigvals(Wmono),
                               ts=ts, ys=ys, history=(ht, hvals), nits=it)
    return OrbitResult(y0=y0, period=T, tau=tau, converged=False,
                       residual=last_res, monodromy=None,
                       multipliers=None, ts=None, ys=None,
                       history=(ht, hvals), nits=maxit)


def continue_branch(tau_start, tau_end, y0_start, T_start, p: CoreParams,
                    dt, nsteps=40, verbose=True,
                    history_seed=None, bidirectional=False):
    """Natural-parameter continuation of a periodic orbit in tau.

    Returns a list of OrbitResult (one per converged tau).
    """
    taus = np.linspace(tau_start, tau_end, nsteps)
    results = []
    y0 = y0_start.copy()
    T = T_start
    hseed = history_seed
    for i, tau in enumerate(taus):
        orb = shoot_orbit(y0, T, tau, p, dt, history_seed=hseed,
                          maxit=80, tol=1e-8, verbose=False)
        if orb.converged:
            results.append(orb)
            y0 = orb.y0
            T = orb.period
            hseed = orb.history
            if verbose:
                mults = orb.multipliers
                # sort by modulus descending, exclude phase ~1
                modsort = sorted(mults, key=lambda z: -abs(z))
                dom = modsort[1] if len(modsort) > 1 else modsort[0]
                print(f"tau={tau:8.4f}  T={T:9.3f}  "
                      f"amp(N)={orb.ys[:,0].max()-orb.ys[:,0].min():8.3f}  "
                      f"|mu_dom|={abs(dom):.5f}  "
                      f"mu_dom={dom:.4f}  res={orb.residual:.1e}")
        else:
            if verbose:
                print(f"tau={tau:8.4f}  ** did not converge (res={orb.residual:.2e})")
            # try smaller step
            break
    return results


# ---------------------------------------------------------------------------
# Long integration to find a stable limit cycle (to seed continuation)
# ---------------------------------------------------------------------------

def settle_to_cycle(tau, p: CoreParams, dt, yinit=None, T_warmup=400000.0,
                    history=None, n_periods_measure=4,
                    max_period_guess=500.0):
    """Integrate for a long time to land on a stable periodic orbit, then
    measure its period and return (y0, T, history_seed)."""
    p.tau = tau
    eq = equilibrium(p)
    n = len(eq)
    if yinit is None:
        yinit = eq.copy()
        yinit[0] *= 1.15
    if history is None:
        hfunc = lambda t: eq
        ht = np.linspace(-tau, 0, 64)
        hvals = np.tile(eq, (len(ht), 1))
    else:
        ht, hvals = history
        hfunc = lambda t: np.interp(t, ht, hvals)
    # long integration
    nwarm = int(np.round(T_warmup / dt))
    y = yinit.copy()
    ys_tail = []
    ts_tail = []
    t = 0.0
    # simple RK4 loop, saving tail
    # for memory, only keep last ~ max_period_guess*2
    tail_len_steps = int(np.round(max_period_guess * 2.5 / dt))
    ring = np.zeros((tail_len_steps, n))
    ring_t = np.zeros(tail_len_steps)
    idx = 0
    for i in range(nwarm):
        yd = hfunc(t - tau) if t - tau <= 0 else None
        # we'll just use the periodic history helper via a full integrate call
        break
    # Easier: use integrate_dde with constant history then restart with own tail
    yT, _, ts, ys = integrate_dde(yinit, hfunc, T_warmup, p, dt)
    # now find period from peaks of N in the latter portion
    tail = ys[-2 * tail_len_steps:] if len(ys) > 2 * tail_len_steps else ys
    N = tail[:, 0]
    # find upward crossings of mean
    meanN = N.mean()
    crossings = []
    for j in range(1, len(N)):
        if N[j - 1] < meanN <= N[j]:
            crossings.append(j)
    if len(crossings) < 3:
        # try peaks
        peaks = []
        for j in range(2, len(N) - 2):
            if N[j] > N[j - 1] and N[j] > N[j + 1] and N[j] > meanN:
                peaks.append(j)
        if len(peaks) < 3:
            return None
        periods = np.diff(peaks) * dt
    else:
        periods = np.diff(crossings) * dt
    T = float(np.median(periods[-n_periods_measure:]))
    # take the state at the last crossing as y0
    j0 = crossings[-1] if len(crossings) > 0 else peaks[-1]
    y0 = tail[j0].copy()
    # build history from the tail made periodic
    ts_tail = ts[-len(tail):]
    hfunc, ht, hvals = _periodic_history(tail, ts_tail - ts_tail[0], T, tau)
    return y0, T, (ht, hvals, tail, ts_tail - ts_tail[0])
