"""
Real power-analysis demo for the effort signal (replaces the report's
fabricated example values with computed ones).  Uses our sampled-governance
(sample-and-hold) model + Lomb-Scargle band detection vs AR(1) red-noise null
(the same methodology as ram_crosssection.py).

Targets the actual effort-signal regimes:
  sprat-class  r=0.8  g=2  T_r=7   (P ~ 8 yr, E amp ~ 236% of E*)
  anchovy-class r=1.6 g=1  T_r=3   (P ~ 4 yr, E amp ~ 81% of E*)
  stable cell  cod-class r=0.3 g=5 T_r=5  (P none, E stable) -> false positives
Also probes the report's two questionable example rows:
  r=0.01 T_r=5  (our scan: DRIFT, not a clean oscillation)
  r=0.05 T_r=30 (our scan: STABLE)
"""
import numpy as np
from scipy.signal import lombscargle

# ---------------- model (Candidate A) ----------------
K = 100.0; q = 0.001
eta, Emax = 0.914, 30.0
delta0, Dref, taum, Zref = 0.01, 1.0, 5.0, 1.0
k = 10.0
delta = np.log(2.0) / 10.0
LN2K = np.log(2.0) / k

def softplus(x):
    x = np.asarray(x, float); kx = k * x
    out = np.empty_like(kx)
    hi, lo = kx > 50, kx < -50
    out[hi] = x[hi]; out[lo] = 0.0
    mid = ~(hi | lo)
    out[mid] = np.log1p(np.exp(kx[mid])) / k
    return out

def eq_state(r, eta_v):
    Zs = delta
    a = -eta_v / Emax; b = eta_v * Zs / Dref; c = delta0 * Zs / (Zref + Zs)
    Es = (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)
    Ns = K * (1 - q * Es / r)
    return Ns, Zs, Es

def integrate_E(r, g, eta_v, T_r, T=120.0, dt=0.05, pert=1e-3):
    """Sample-and-hold model; return (years, annual E series after burn-in)."""
    N0, Z0, E0 = eq_state(r, eta_v)
    nsteps = int(round(T / dt)); h = T / nsteps
    y = np.array([N0 * (1 + pert), Z0 * (1 + pert), E0 * (1 + pert)])
    Nh = np.full(nsteps + 1, N0); Zh = np.full(nsteps + 1, Z0)
    Eh = np.full(nsteps + 1, E0)
    g_ = max(g, 4 * dt)
    spr = max(int(round(T_r / h)), 1)

    def dN(t):
        tt = t - g_
        if tt <= 0: return N0
        i = int(tt / h)
        if i >= nsteps: return Nh[nsteps]
        fr = tt / h - i
        return (1 - fr) * Nh[i] + fr * Nh[i + 1]

    def zsig(t):
        kk = int(np.floor(t / T_r)); tb = kk * T_r
        if tb <= 0: return Z0
        i = int(tb / h)
        if i >= nsteps: return Zh[nsteps]
        fr = tb / h - i
        return (1 - fr) * Zh[i] + fr * Zh[i + 1]

    def f(yy, nd, zs):
        N, Z, E = yy
        reg = r * nd * (1 - nd / K); qEN = q * E * N
        src = max(0.0, softplus(qEN - reg) - LN2K + delta)
        return np.array([reg - qEN, (src - Z) / taum,
                         (1 - E / Emax) * (eta_v * E * (zs / Dref - E / Emax)
                                           + delta0 * zs / (Zref + zs))])

    for i in range(nsteps):
        t = i * h
        nd = dN(t); zs = zsig(t)
        k1 = f(y, nd, zs)
        nd2 = dN(t + h / 2); zs2 = zsig(t + h / 2)
        k2 = f(y + h / 2 * k1, nd2, zs2)
        k3 = f(y + h / 2 * k2, nd2, zs2)
        nd4 = dN(t + h); zs4 = zsig(t + h)
        k4 = f(y + h * k3, nd4, zs4)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y[0] = min(max(y[0], 0.0), 120.0); y[1] = max(y[1], 0.0)
        y[2] = min(max(y[2], 0.0), Emax)
        Nh[i + 1], Zh[i + 1], Eh[i + 1] = y

    t_yr = np.arange(0, int(T), 1)
    idx = (t_yr / h).astype(int)
    E_ann = Eh[idx]
    burn = 20
    return t_yr[burn:], E_ann[burn:]

def period_of(E):
    """Estimate dominant period of a series via crossings of the mean."""
    mn = E.mean()
    cr = [j for j in range(1, len(E)) if E[j - 1] < mn <= E[j]]
    if len(cr) < 3:
        return None
    return float(np.median(np.diff(cr)))

def detect(E, band, nf=800, nsim=120, seed=7):
    """Band power vs per-band 95% AR(1) red-noise null -> detected?"""
    t = np.arange(len(E))
    b1, b0 = np.polyfit(t, E, 1); det = E - (b0 + b1 * t)
    freq = np.linspace(1 / (2 * len(t)), 0.5, nf)
    P = lombscargle(t, det, 2 * np.pi * freq); P /= P.sum()
    m = (freq > 1 / band[1]) & (freq <= 1 / band[0])
    bp = P[m].sum()
    phi = np.corrcoef(det[:-1], det[1:])[0, 1] if len(det) > 4 else 0.0
    rng = np.random.default_rng(seed)
    sims = np.zeros(nsim)
    for s in range(nsim):
        e = rng.standard_normal(len(t)); x = np.zeros(len(t)); x[0] = e[0]
        for i in range(1, len(x)):
            x[i] = phi * x[i - 1] + e[i]
        x = x / np.std(x)
        b1, b0 = np.polyfit(t, x, 1); detx = x - (b0 + b1 * t)
        Px = lombscargle(t, detx, 2 * np.pi * freq); Px /= Px.sum()
        sims[s] = Px[m].sum()
    thr = np.percentile(sims, 95)
    return bool(bp > thr), bp, thr

def power_cell(r, g, T_r, band, noise_levels, n_real=60, label=""):
    t, E = integrate_E(r, g, 0.914, T_r)
    per = period_of(E)
    p2p = E.max() - E.min()
    print(f"[{label}] r={r} g={g} T_r={T_r}: period={per if per is None else round(per,1)} yr"
          f"  E p2p={p2p:.2f}  (E* scale)  -> {'OSCILLATORY' if per and per < 40 else 'NOT a clean cycle'}")
    for sig in noise_levels:
        dets = 0
        for k in range(n_real):
            eps = np.random.default_rng(k).normal(0, sig, len(E))
            d, bp, thr = detect(E * np.exp(eps), band)
            dets += d
        print(f"    noise sigma={sig}:  power = {dets/n_real:.2f}  ({dets}/{n_real})")
    print()

if __name__ == "__main__":
    print("=" * 70)
    print("REAL power-analysis demo (effort signal; Lomb-Scargle band vs AR(1) null)")
    print("=" * 70)
    # 1. actual effort-signal regimes (the report's grid MISSES these)
    power_cell(0.8, 2.0, 7.0, (5, 11), [0.1, 0.3], label="sprat-class")
    power_cell(1.6, 1.0, 3.0, (3, 5.5), [0.1, 0.3], label="anchovy-class")
    # 2. stable cell -> false-positive rate
    power_cell(0.3, 5.0, 5.0, (5, 11), [0.1, 0.3], label="cod-class (stable)")
    # 3. the report's example rows
    print("report's example rows:")
    power_cell(0.01, 0.0, 5.0, (5, 40), [0.1], label="report row r=0.01 T_r=5")
    power_cell(0.05, 0.0, 30.0, (5, 40), [0.1], label="report row r=0.05 T_r=30")
