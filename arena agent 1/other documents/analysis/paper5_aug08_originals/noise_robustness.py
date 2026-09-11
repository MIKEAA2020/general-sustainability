"""
Assessment-noise robustness of the sampled-governance windows (2026-08-08)
============================================================================
Multiplicative lognormal assessment error on the sampled signal:
    Z_obs(k T_r) = Z(k T_r) * exp(eps_k),  eps_k ~ N(0, sigma)
Questions: (1) does the anchovy-class window (T_r ~ 2-4 yr -> ~4-yr cycle)
survive 5-30% assessment error? (2) does noise induce false oscillation at
T_r=1 (annual), destroying the discrimination? (3) AR(1) colored noise.

Classification: oscillatory if tail peak-to-peak of detrended N > 3x the
T_r=1 reference (same sigma), i.e. the cycle is well above the noise floor.
Tight inline integrator; review boundaries precomputed as step indices.
"""
import numpy as np
from droop_test import softplus, K, qc, Emax, delta0, Dref, taum, Zref, delta, k

def run(r, g, eta_v, T_r, sigma, seed, T=2000.0, dt=0.05, pert=1e-3,
        ar1=False, rho=0.6):
    rng = np.random.default_rng(seed)
    from stage_r_window import stage_jacobians
    N0, E0, Z0 = stage_jacobians(r, g, eta_v)[0:3]
    nsteps = int(round(T / dt)); h = T / nsteps
    spr = max(int(round(T_r / h)), 1)          # steps per review
    nrev = nsteps // spr
    eps = rng.normal(0.0, sigma, nrev + 2)
    if ar1:
        for i in range(1, len(eps)):
            eps[i] = rho * eps[i - 1] + np.sqrt(1 - rho**2) * eps[i]
    Ng = int(round(g / h)); Ng = max(Ng, 1)    # delay in steps

    N_hist = np.full(nsteps + 1, N0)
    Z_hist = np.full(nsteps + 1, Z0)
    E_hist = np.full(nsteps + 1, E0)
    y = np.array([N0 * (1 + pert), Z0 * (1 + pert), E0 * (1 + pert)])

    for i in range(nsteps):
        # delayed N
        jd = i - Ng
        if jd <= 0:
            nd = N0
        else:
            fr = (i * h - g) / h - (jd - 1) if False else 0.0  # unused
            # linear interpolation between N_hist[jd] and N_hist[jd+1]
            tt = i * h - g
            j = int(tt / h)
            if j < 0:
                nd = N0
            elif j >= nsteps:
                nd = N_hist[nsteps]
            else:
                fr = tt / h - j
                nd = (1 - fr) * N_hist[j] + fr * N_hist[j + 1]
        # held signal: Z at review k = i // spr
        k = i // spr
        jz = k * spr
        zz = Z_hist[jz] if jz <= nsteps else Z0
        zs = zz * np.exp(eps[k]) if sigma > 0 else zz

        N, Z, E = y
        reg = r * nd * (1.0 - nd / K)
        qEN = qc * E * N
        src = max(0.0, softplus(qEN - reg) - np.log(2.0) / k + delta)
        fN = reg - qEN
        fZ = (src - Z) / taum
        gate = 1.0 - E / Emax
        fE = gate * (eta_v * E * (zs / Dref - E / Emax)
                     + delta0 * zs / (Zref + zs))
        k1 = np.array([fN, fZ, fE])

        # stage 2 (use same held signal; approximate mid-step delay via j2)
        tt = i * h + h / 2 - g
        j = int(tt / h)
        nd2 = N0 if j < 0 else (N_hist[nsteps] if j >= nsteps
                                else (1 - (tt / h - j)) * N_hist[j]
                                + (tt / h - j) * N_hist[j + 1])
        k2 = i + 0  # placeholder
        y2 = y + h / 2 * k1
        N, Z, E = y2
        reg = r * nd2 * (1.0 - nd2 / K)
        qEN = qc * E * N
        src = max(0.0, softplus(qEN - reg) - np.log(2.0) / k + delta)
        fN = reg - qEN; fZ = (src - Z) / taum
        gate = 1.0 - E / Emax
        fE = gate * (eta_v * E * (zs / Dref - E / Emax)
                     + delta0 * zs / (Zref + zs))
        k2 = np.array([fN, fZ, fE])

        y3 = y + h / 2 * k2
        N, Z, E = y3
        reg = r * nd2 * (1.0 - nd2 / K)
        qEN = qc * E * N
        src = max(0.0, softplus(qEN - reg) - np.log(2.0) / k + delta)
        fN = reg - qEN; fZ = (src - Z) / taum
        gate = 1.0 - E / Emax
        fE = gate * (eta_v * E * (zs / Dref - E / Emax)
                     + delta0 * zs / (Zref + zs))
        k3 = np.array([fN, fZ, fE])

        tt = i * h + h - g
        j = int(tt / h)
        nd4 = N0 if j < 0 else (N_hist[nsteps] if j >= nsteps
                                else (1 - (tt / h - j)) * N_hist[j]
                                + (tt / h - j) * N_hist[j + 1])
        y4 = y + h * k3
        N, Z, E = y4
        reg = r * nd4 * (1.0 - nd4 / K)
        qEN = qc * E * N
        src = max(0.0, softplus(qEN - reg) - np.log(2.0) / k + delta)
        fN = reg - qEN; fZ = (src - Z) / taum
        gate = 1.0 - E / Emax
        fE = gate * (eta_v * E * (zs / Dref - E / Emax)
                     + delta0 * zs / (Zref + zs))
        k4 = np.array([fN, fZ, fE])

        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y[0] = min(max(y[0], 0.0), 120.0)
        y[1] = max(y[1], 0.0)
        y[2] = min(max(y[2], 0.0), Emax)
        N_hist[i + 1] = y[0]; Z_hist[i + 1] = y[1]; E_hist[i + 1] = y[2]
    return N_hist, E_hist

def tail_p2p(N_hist, frac=0.6):
    tail = N_hist[int(len(N_hist) * frac):]
    t = np.arange(len(tail))
    b1, b0 = np.polyfit(t, tail, 1)
    det = tail - (b0 + b1 * t)
    return det.max() - det.min()

if __name__ == "__main__":
    print("=" * 92)
    print("Noise robustness scan (tight integrator, T=2000, 3 seeds)")
    print("=" * 92)

    def table(band_label, r, g, Trs, sigmas, seeds=3):
        refs = {s: np.median([tail_p2p(run(r, g, 0.914, 1.0, s, sd)[0])
                              for sd in range(seeds)])
                for s in sigmas}
        print(f"\n--- {band_label} ---")
        print("T_r   sigma   oscillatory fraction   median p2p(N)   ref(T_r=1)")
        for T_r in Trs:
            for sigma in sigmas:
                p2ps = np.array([tail_p2p(run(r, g, 0.914, T_r, sigma, sd)[0])
                                 for sd in range(seeds)])
                med_ref = refs[sigma]
                frac = float(np.mean(p2ps > 3 * med_ref)) if med_ref > 0 else 0.0
                print(f"{T_r:4.1f}  {sigma:5.2f}   {frac:.2f}"
                      f"                    {np.median(p2ps):6.2f}   {med_ref:6.2f}")

    table("ANCHOVY band (r=1.6, g=1): ~4-yr cycle at T_r in (1.5-2,5+)",
          1.6, 1.0, [1.0, 2.0, 3.0, 4.0], [0.05, 0.30])
    table("SPRAT band (r=0.8, g=2): ~8-yr cycle at T_r in (6,12+)",
          0.8, 2.0, [1.0, 7.0], [0.05, 0.30])

    print("\n--- False-positive check at T_r=1 (annual), sigma=0.30 ---")
    for (label, r, g) in [("anchovy", 1.6, 1.0), ("sprat", 0.8, 2.0)]:
        p2ps = np.array([tail_p2p(run(r, g, 0.914, 1.0, 0.30, sd)[0])
                         for sd in range(6)])
        print(f"  {label}: median p2p = {np.median(p2ps):.3f}")

    print("\n--- AR(1) colored noise, anchovy T_r=3, sigma=0.15 ---")
    p2ps = np.array([tail_p2p(run(1.6, 1.0, 0.914, 3.0, 0.15, sd, ar1=True)[0])
                     for sd in range(6)])
    print(f"  median p2p = {np.median(p2ps):.2f}")
