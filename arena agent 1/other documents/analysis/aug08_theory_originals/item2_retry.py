"""Retry item 2: reproduce & classify the eta=10 unified-core-v2 intermittency.
Key manuscript facts to match:
  tau=18.45 (> tau_+=18.362), dt in {0.1,0.05,0.02,0.01} dt-convergent,
  ~6 escape events per 1e5 time units, alternation quiet(large-amplitude).
  eta=2.5 has richer multi-crossing (4 alternating bands) - not needed here.
Use: adaptive small dt, floor only (no upper clamp on E), several seeds.
"""
import numpy as np
from unified_v2_intermittency import equilibrium, dde_rhs, P, ETA

def integrate(y0, hist, T, tau, dt=0.01, floor=1e-10):
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
        y = y + h/6*(k1+2*k2+2*k3+k4)
        # floor only
        y[0]=max(y[0],floor); y[1]=max(y[1],floor)
        y[2]=max(y[2],floor); y[3]=max(y[3],floor)
        if not np.all(np.isfinite(y)):
            return ys[:i+1], True
        ys[i+1] = y
    return ys, False

if __name__ == "__main__":
    eq = equilibrium()
    Xstar, Estar = eq[0], eq[3]
    print(f"eq: X*={Xstar:.4f} E*={Estar:.4f}  (tau_-=17.568, tau_+=18.362)")
    tau = 18.45

    # Try several initial conditions, dt=0.01, T=1e5
    seeds = {
        "small-pert-eq": eq.copy(),
        "far-high-X": np.array([50.0, 1.0, 0.01, 0.01]),
        "far-low-X": np.array([2.0, 1.0, 0.01, 0.01]),
        "med": np.array([30.0, 0.5, 0.5, 0.5]),
    }
    seeds["small-pert-eq"][0] *= 1.001; seeds["small-pert-eq"][3] *= 1.01

    for name, y0 in seeds.items():
        print(f"\n=== seed: {name} (y0={np.round(y0,3)}) tau={tau} ===")
        hist = lambda t: y0
        ys, div = integrate(y0, hist, 1e5, tau, dt=0.01)
        X = ys[:,0]; t = np.arange(len(ys))*0.01
        if div:
            print("  DIVERGED")
            continue
        # large-amplitude excursions: X far from Xstar (X near 0 = collapse? or large?)
        # The 'large-amplitude attractor' in this model: X is small when collapsed.
        # Manuscript: 'quiet near equilibrium' vs 'large-amplitude excursion'.
        # Use |X - Xstar| and also X itself.
        print(f"  X range: {X.min():.3f}..{X.max():.3f} | final X={X[-1]:.4f}")
        # count excursions away from equilibrium: |X-X*| > threshold
        amp = np.abs(X - Xstar)
        for thr in [1.0, 3.0, 5.0, 8.0]:
            large = amp > thr
            trans = np.sum(np.diff(large.astype(int)) == 1)
            print(f"    |X-X*|>{thr}: frac={large.mean():.3f} escape_events={trans}")
        # sample the trajectory
        idx = [0, 100, 1000, 5000, 10000, 20000, 50000, 80000, 99999]
        print("    t:", end="")
        for i in idx:
            i = min(i, len(ys)-1)
            print(f" {i*0.01:.0f}:X={ys[i,0]:6.2f}", end="")
        print()
PYEOF