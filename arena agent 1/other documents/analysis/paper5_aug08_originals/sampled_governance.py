"""
Sampled-governance stage model v2 — sample-and-hold of the deficit signal
==========================================================================
Correct bridge to the continuous model.  Institutions do NOT jump effort to
a target at each review; they HOLD their observation of the deficit between
reviews and adjust effort continuously against the held signal:

    dN/dt = r N(t-g)(1 - N(t-g)/K) - q E N
    dZ/dt = (max(0, softplus(qEN - regen) - ln2/k + delta) - Z)/tau_m
    dE/dt = (1 - E/Emax)[ eta E (Z_sig/Dref - E/Emax)
                          + delta0 Z_sig/(Zref + Z_sig) ]
    Z_sig(t) = Z(k*T_r)   for t in [k*T_r, (k+1)*T_r)   (sample-and-hold)

As T_r -> 0, Z_sig -> Z(t), recovering the tau=0 continuous system (stable
below the window) -- a correct bridge.  The hold introduces an effective
delay of up to T_r between the true deficit and the signal driving effort.

Question: at which review intervals T_r does the sampled system oscillate?
Prediction to test: T_r = 1 yr (annual TAC) stable (matches observation);
some window at larger T_r where the mechanism becomes field-testable on real
multi-year-review systems (NZ QMS data-limited, SA OMP reviews, GFCM
transitional multi-year catch limits).

Deterministic first cut; assessment error / noise / partial-revision bias
flagged as open.
"""
import numpy as np
from droop_test import softplus, K, qc, Emax, delta0, Dref, taum, Zref, delta, k
from stage_r_window import stage_jacobians

def sampled_governance(r, g, eta_v, T_r, T=8000.0, dt=0.02, pert=1e-3,
                       clamp=(0.0, 120.0)):
    res = stage_jacobians(r, g, eta_v)
    N0, E0, Z0 = res[0], res[1], res[2]
    nsteps = int(round(T / dt)); h = T / nsteps
    y = np.array([N0 * (1 + pert), Z0 * (1 + pert), E0 * (1 + pert)])
    N_hist = np.zeros(nsteps + 1); Z_hist = np.zeros(nsteps + 1)
    E_hist = np.zeros(nsteps + 1)
    N_hist[0], Z_hist[0], E_hist[0] = y
    preN, preZ, preE = N0, Z0, E0

    def delayed_N(t):
        tt = t - g
        if tt <= 0: return preN
        ti = tt / h; i = int(np.floor(ti))
        if i >= nsteps: return N_hist[nsteps]
        fr = ti - i
        return (1 - fr) * N_hist[i] + fr * N_hist[i + 1]

    def z_sig(t):
        # Z at the most recent review boundary k*T_r <= t
        kk = int(np.floor(t / T_r))
        tb = kk * T_r
        if tb <= 0: return preZ
        ti = tb / h; i = int(np.floor(ti))
        if i >= nsteps: return Z_hist[nsteps]
        fr = ti - i
        return (1 - fr) * Z_hist[i] + fr * Z_hist[i + 1]

    def f(yy, nd, zs):
        N, Z, E = yy
        reg = r * nd * (1.0 - nd / K)
        qEN = qc * E * N
        src = max(0.0, softplus(qEN - reg) - np.log(2.0) / k + delta)
        dN = reg - qEN
        dZ = (src - Z) / taum
        gate = 1.0 - E / Emax
        dE = gate * (eta_v * E * (zs / Dref - E / Emax)
                     + delta0 * zs / (Zref + zs))
        return np.array([dN, dZ, dE])

    for i in range(nsteps):
        t = i * h
        nd = delayed_N(t); zs = z_sig(t)
        k1 = f(y, nd, zs)
        zs2 = z_sig(t + h / 2)
        nd2 = delayed_N(t + h / 2)
        k2 = f(y + h / 2 * k1, nd2, zs2)
        k3 = f(y + h / 2 * k2, nd2, zs2)
        nd4 = delayed_N(t + h); zs4 = z_sig(t + h)
        k4 = f(y + h * k3, nd4, zs4)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y[0] = min(max(y[0], clamp[0]), clamp[1])
        y[1] = max(y[1], 0.0)
        y[2] = min(max(y[2], 0.0), Emax)
        N_hist[i + 1], Z_hist[i + 1], E_hist[i + 1] = y

    tail_n = N_hist[int(len(N_hist) * 0.6):]
    mn = tail_n.mean()
    cr = [j for j in range(1, len(tail_n)) if tail_n[j - 1] < mn <= tail_n[j]]
    per = np.median(np.diff(cr)) * dt if len(cr) >= 3 else None
    amp = tail_n.max() - tail_n.min()
    Ne = tail_n[-1]
    if per is not None and amp > 0.5:
        cls = 'oscillatory'
    elif abs(Ne - N0) < 0.5:
        cls = 'stable'
    else:
        cls = 'drift'
    return cls, per, amp, Ne

if __name__ == "__main__":
    from stage_r_window import stage_crossings
    print("=" * 96)
    print("Sampled-governance v2 (sample-and-hold of deficit signal)")
    print("=" * 96)
    cases = [
        ("sprat band  r=0.8 g=2   (cont. tau-window (2.6,7.7)/(3.1,7.8))",
         0.8, 2.0, [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0, 12.0]),
        ("cod band    r=0.3 g=5   (cont. tau-window (9.9,20.3))",
         0.3, 5.0, [1.0, 2.0, 3.0, 5.0, 8.0, 10.0, 12.0, 15.0, 20.0]),
        ("anchovy band r=1.6 g=1  (cont. tau-window (1.1,3.9) eta3)",
         1.6, 1.0, [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]),
    ]
    for eta_v in (0.914, 3.0):
        print(f"\n=== eta = {eta_v} ===")
        for name, r, g, Trs in cases:
            cr = stage_crossings(r, g, eta_v=eta_v, nw=3000)
            ref = f"({min(t0 for w,t0,P in cr):.1f},{max(t0 for w,t0,P in cr):.1f})" if cr else "none"
            print(f"  {name}   [cont. tau-window {ref}]")
            row = []
            for Tr in Trs:
                cls, per, amp, Ne = sampled_governance(r, g, eta_v, Tr)
                tag = f"Tr={Tr:4.1f}:{cls[0]}" + (f"({per:.0f})" if per else "")
                row.append(tag)
            print("    " + "  ".join(row))
