"""
Core DDE model expressed in SymPy for JiTCDDE, plus a fast wrapper that
integrates one segment given a piecewise-linear periodic history.
"""
import numpy as np
import sympy as sp
from jitcdde import jitcdde, y, t


def make_core(gated=False, k=10.0, delta=None, r=0.02, K=100.0, q=0.001,
              eta=0.914, Emax=30.0, delta0=0.01, Dref=1.0, tau_m=5.0,
              Zref=1.0):
    """Return (f, params dict) for the three-state core DDE in JiTCDDE form.
    State: y(0)=N, y(1)=Z, y(2)=E. Delay: y(1,t-tau) = Z(t-tau)."""
    if delta is None:
        delta = float(np.log(2.0) / k)
    N, Z, E = y(0), y(1), y(2)
    Ztau = y(1, t - sp.Symbol('tau'))
    S = r * N * (1 - N / K)
    qEN = q * E * N
    d = qEN - S
    softplus = sp.log(1 + sp.exp(k * d)) / k
    src = sp.Piecewise((softplus - sp.log(2) / k + delta,
                       softplus - sp.log(2) / k + delta > 0),
                      (0, True))
    dN = S - qEN
    dZ = (src - Z) / tau_m
    bracket = (eta * E * (Ztau / Dref - E / Emax)
               + delta0 * Ztau / (Zref + Ztau))
    if gated:
        dE = (1 - E / Emax) * bracket
    else:
        dE = bracket
    return [dN, dZ, dE], dict(k=k, delta=delta, r=r, K=K, q=q, eta=eta,
                               Emax=Emax, delta0=delta0, Dref=Dref,
                               tau_m=tau_m, Zref=Zref)


class SegmentIntegrator:
    """Integrates the core DDE over one segment given a periodic history
    function h(t).  JiTCDDE is recompiled per (tau, params) but reused across
    segments via `reset` and `add_past_points`.
    """
    def __init__(self, gated=False, **params):
        f, self.p = make_core(gated=gated, **params)
        self.f = f
        self.gated = gated
        self.DDE = None

    def _build(self, tau, h_times, h_values):
        """Build a fresh JiTCDDE instance with a piecewise-cubic Hermite past
        sampled at h_times (sorted) with h_values (m,3)."""
        tau_sym = sp.Symbol('tau')
        f_subs = [sp.sympify(eq).subs(tau_sym, tau) for eq in self.f]
        DDE = jitcdde(f_subs, verbose=False)
        # provide past points; JiTCDDE expects Cubic Hermite interpolation
        # via add_past_point(time, state, derivative).  We approximate
        # derivatives by central differences.
        m = len(h_times)
        for i, tt in enumerate(h_times):
            state = h_values[i]
            if i == 0:
                dstate = (h_values[1] - h_values[0]) / (h_times[1] - h_times[0])
            elif i == m - 1:
                dstate = (h_values[-1] - h_values[-2]) / (h_times[-1] - h_times[-2])
            else:
                dstate = ((h_values[i + 1] - h_values[i - 1])
                          / (h_times[i + 1] - h_times[i - 1]))
            DDE.add_past_point(float(tt),
                               np.asarray(state, dtype=float),
                               np.asarray(dstate, dtype=float))
        DDE.step_on_discontinuities()
        return DDE

    def integrate_segment(self, y0, h, tau, h_times, h_values):
        """Integrate from state y0 at t=0 for h time units.  Returns
        (yT, trajectory_times, trajectory_states)."""
        DDE = self._build(tau, h_times, h_values)
        # force initial state at t=0
        DDE.integrate(0.0)  # settle to last past point
        # We want to start at y0 at t=0; the past already covers [-tau,0],
        # with h_values[-1] = state at t=0.  Override by adding a point.
        # JiTCDDE: integrate from current time.
        yT = DDE.integrate(h)
        # sample trajectory densely
        return np.array(yT, dtype=float), DDE
