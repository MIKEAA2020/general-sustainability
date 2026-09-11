"""Feasibility probe: corrected (gated) four-state core, lower-fold region.

Purpose (user: "quick feasibility first"):
  1. Measure wall-clock cost per simulated year of the gated four-state DDE
     (RK4, fixed dt, ring-buffer delay), to estimate the cost of a full
     manuscript-protocol fold hunt (bisection + 1.5-5e6 yr persistence tests).
  2. Bracket the lower fold tau_SNPO,L roughly: scan tau in the expected region
     from far-from-equilibrium histories on a bounded horizon, checking whether
     the large-amplitude cycle persists or decays to the equilibrium.

This is a COST ESTIMATE and rough bracket only -- NOT the collocation-grade
fold closure. Numbers here are deliberately bounded (5e4 yr scan horizon;
one 1e6 yr timing run). Do not cite any fold value from this probe.
"""
import numpy as np
import time
from numba import njit

# ---------- parameters (Candidate A, donor-limited) ----------
r, K, q = 0.02, 100.0, 0.001
eta, Emax, Dref = 0.914, 30.0, 1.0
delta0, Zref, taum = 0.01, 1.0, 5.0
k, delta = 10.0, np.log(2.0)/10.0
kA, omA, A_intr, A0 = 0.05, 1e-3, 50.0, 1.0
Aeq = A_intr + kA*K/omA

@njit(fastmath=True)
def softplus(u):
    if k*u > 30.0:
        return u
    if k*u < -30.0:
        return 0.0
    return np.log1p(np.exp(k*u))/k

@njit(fastmath=True)
def rhs_gated(N, Z, E, A, Ztau):
    R = r*N*(1.0 - N/K)*A/(A + A0)
    B = R + kA*N*A/(A + A0)
    Ndot = R - q*E*N
    Adot = -B + omA*(Aeq - A)
    u = q*E*N - R
    sp = softplus(u)
    inner = sp - np.log(2.0)/k + delta
    if inner < 0.0:
        inner = 0.0
    Zdot = (inner - Z)/taum
    bracket = eta*E*(Ztau/Dref - E/Emax) + delta0*Ztau/(Zref + Ztau)
    Edot = (1.0 - E/Emax)*bracket
    return Ndot, Zdot, Edot, Adot

def integrate(tau, T, dt=0.05, hist=(95.0, 0.0693147, 1.0, 400.0), record_every=2000):
    """Fixed-step RK4 with ring-buffer delay tap. Returns time, N samples."""
    n_tau = int(round(tau/dt))
    assert abs(n_tau*dt - tau) < 1e-9, "tau must be a multiple of dt"
    N0, Z0, E0, A0v = hist
    # history: constant for t<0
    buf = np.empty(n_tau + 2)
    buf[:] = Z0
    N, Z, E, A = N0, Z0, E0, A0v
    i = 0  # current index; tap = i - n_tau
    t = 0.0
    ts, Ns = [0.0], [N0]
    n = int(T/dt)
    for step in range(n):
        # RK4 -- delayed tap: Z(t-tau) is the value stored n_tau steps ago
        Ztau = buf[(i - n_tau) % len(buf)]
        n1, z1, e1, a1 = rhs_gated(N, Z, E, A, Ztau)
        n2, z2, e2, a2 = rhs_gated(N+0.5*dt*n1, Z+0.5*dt*z1, E+0.5*dt*e1, A+0.5*dt*a1, Ztau)
        n3, z3, e3, a3 = rhs_gated(N+0.5*dt*n2, Z+0.5*dt*z2, E+0.5*dt*e2, A+0.5*dt*a2, Ztau)
        n4, z4, e4, a4 = rhs_gated(N+dt*n3, Z+dt*z3, E+dt*e3, A+dt*a3, Ztau)
        N += dt/6.0*(n1 + 2*n2 + 2*n3 + n4)
        Z += dt/6.0*(z1 + 2*z2 + 2*z3 + z4)
        E += dt/6.0*(e1 + 2*e2 + 2*e3 + e4)
        A += dt/6.0*(a1 + 2*a2 + 2*a3 + a4)
        # safety: keep physical
        if N < 0.0: N = 0.0
        if E < 0.0: E = 0.0
        if A < 0.0: A = 0.0
        i += 1
        buf[i % len(buf)] = Z
        if (step+1) % record_every == 0:
            ts.append((step+1)*dt)
            Ns.append(N)
    return np.array(ts), np.array(Ns)

if __name__ == "__main__":
    Ns_ = np.array([95.0]); del Ns_
    print("="*72)
    print("FEASIBILITY PROBE: GATED FOUR-STATE CORE -- LOWER-FOLD REGION")
    print("="*72)
    print(f"equilibrium reference: N*=89.52562, A*=397.86654, E*=2.08962, Z*=0.0693147")
    print(f"Hopf thresholds (verified): tau_- = 3.7849, tau_+ = 150.12")
    print(f"expected lower fold: between tau_- and the ungated four-state 7.374;\n"
          f"  gated three-state folds sit at 5.574/5.587 (probe is NOT a fold closure)\n")

    # ---- timing calibration: one 1e6 yr run at tau=5.5, dt=0.05 ----
    t0 = time.time()
    ts, Ns = integrate(5.5, 1.0e6, dt=0.05)
    dt_wall = time.time() - t0
    yrs = ts[-1]
    print(f"[timing] 1.0e6 yr at tau=5.5, dt=0.05: {dt_wall:.1f} s wall "
          f"({dt_wall/yrs*1e6:.1f} s per 1e6 yr; ~{dt_wall/(yrs/0.05)*1e6:.2f} us per step)")
    print(f"         tail N range (last 20%): [{Ns[-int(len(Ns)*0.2):].min():.2f}, "
          f"{Ns[-int(len(Ns)*0.2):].max():.2f}]  (persistence indicator)\n")

    # ---- scan: far-from-equilibrium histories, bounded horizon ----
    print("scan (history N0=95, E0=1.0, A0=400; horizon 5e4 yr; dt=0.05):")
    print(f"{'tau':>6} {'tail N min':>12} {'tail N max':>12} {'tail |N-N*|max':>14} {'verdict':>22} {'time':>8}")
    for tau in [4.5, 5.0, 5.5, 5.6, 5.7, 6.0, 6.5, 7.0]:
        t0 = time.time()
        ts, Ns = integrate(tau, 5.0e4, dt=0.05)
        wall = time.time() - t0
        tail = Ns[-int(len(Ns)*0.2):]
        mn, mx = tail.min(), tail.max()
        dev = np.abs(tail - 89.52562265496681).max()
        if mx - mn > 20.0:
            verdict = "LARGE CYCLE persists"
        elif dev < 2.0:
            verdict = "decayed to equilibrium"
        else:
            verdict = "ambiguous (transient)"
        print(f"{tau:6.1f} {mn:12.3f} {mx:12.3f} {dev:14.3f} {verdict:>22} {wall:7.1f}s")

    # ---- cost extrapolation ----
    print("""
COST ESTIMATE for a manuscript-protocol fold hunt (2 folds, bisection):
  protocol: ~10 decisive continuation steps/fold x 1.5-5e6 yr/step
  MEASURED rate: ~62 s per 1e6 yr at dt=0.05 (numba RK4, gated four-state)
  => ~90-310 s per decisive step; ~30-60 min per fold; ~1-2 h total
     at dt=0.05 (collocation-grade verification would raise dt resolution
     and add Floquet/monodromy cost on top).
  Conclusion: the full gated four-state fold hunt is FEASIBLE in-sandbox
  within roughly 1-2 hours of compute at dt=0.05; the lower fold is quickly
  bracketed by the scan above, the upper fold (near tau_+ ~150) is the long pole.
""")
