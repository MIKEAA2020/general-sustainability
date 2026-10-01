"""Committed power-analysis driver v2 (2026-09-11) — closes the driver gap behind
effort_signal_power_report.md section 2 / manuscript section 3.6.

v2 = v1 (same method, same defaults, same seeds) plus CLI knobs for the total
integration length T, burn-in, and trial/seed ranges, so the record's scope
("100--200 yr synthetic records", report section 2) can be tested against the
long-settled (T=4000) branch. v2 defaults reproduce the v1 table bit-exactly
(verified: see POWER_CLOSEOUT record); the v1 grid's 11 cells plus the two
record-scope cells v1 omitted (sprat_H200_s01, cod_H200_s01).

Method (unchanged from power_demo.py): sampled-governance operating model ->
annual effort series -> multiplicative observation error -> Lomb-Scargle band
power vs per-series AR(1) red-noise null (120 sims, 95%, seed 7) -> fraction of
50 trials detected (trial seeds 0..49).

Cells: sprat (r=0.8,g=2,Tr=7) band (30,120); anchovy (r=1.6,g=1,Tr=3) band
(8,20); cod false-positive cell (r=0.3,g=5,Tr=5) band (8,20).

Usage:
  python3 power_driver_v2.py [--tmode fixed --T 4000 | --tmode record]
      [--burn 20] [--trials 50] [--seed0 0] [--rho 0.6] [--noises white,ar1]
      [--out power_table_recomputed.json]
  --tmode record sets the per-cell integration length T = H + burn (the analyzed
  record is exactly the H-year window: "100--200 yr synthetic records").
Requires power_demo.py (integrate_E, detect) alongside.
"""
import argparse, json
import numpy as np
from power_demo import integrate_E, detect

NULL_SIMS = 120
NULL_SEED = 7
CACHE = {}

CELLS = [
    ('sprat',   0.8, 2.0, 7.0, (30,120), 100, 0.1),
    ('sprat',   0.8, 2.0, 7.0, (30,120), 100, 0.3),
    ('sprat',   0.8, 2.0, 7.0, (30,120), 200, 0.1),
    ('sprat',   0.8, 2.0, 7.0, (30,120), 200, 0.3),
    ('sprat',   0.8, 2.0, 7.0, (30,120), 400, 0.3),
    ('anchovy', 1.6, 1.0, 3.0, (8,20),   100, 0.1),
    ('anchovy', 1.6, 1.0, 3.0, (8,20),   100, 0.3),
    ('anchovy', 1.6, 1.0, 3.0, (8,20),   200, 0.1),
    ('anchovy', 1.6, 1.0, 3.0, (8,20),   200, 0.3),
    ('anchovy', 1.6, 1.0, 3.0, (8,20),   400, 0.1),
    ('anchovy', 1.6, 1.0, 3.0, (8,20),   400, 0.3),
    ('cod',     0.3, 5.0, 5.0, (8,20),   100, 0.1),
    ('cod',     0.3, 5.0, 5.0, (8,20),   100, 0.3),
    ('cod',     0.3, 5.0, 5.0, (8,20),   200, 0.1),
    ('cod',     0.3, 5.0, 5.0, (8,20),   200, 0.3),
    ('cod',     0.3, 5.0, 5.0, (8,20),   400, 0.1),
    ('cod',     0.3, 5.0, 5.0, (8,20),   400, 0.3),
]

def annual_E(r, g, Tr, T):
    key = (r, g, Tr, T)
    if key not in CACHE:
        CACHE[key] = integrate_E(r, g, 0.914, Tr, T=T)
    return CACHE[key]

def noise_white(n, sig, seed):
    return np.random.default_rng(seed).normal(0, sig, n)

def noise_ar1(n, sig, seed, rho):
    rng = np.random.default_rng(seed)
    eps = rng.normal(0, sig, n)
    for i in range(1, n):
        eps[i] = rho * eps[i-1] + np.sqrt(1 - rho**2) * eps[i]
    return eps

def power_cell(label, r, g, Tr, band, H, sig, T, burn, trials, seed0, noise_fn, noise_name):
    t, E = annual_E(r, g, Tr, T)
    Eh = E[burn:burn+H]
    assert len(Eh) == H, (label, H, len(Eh), T, burn)
    dets = 0
    for k in range(seed0, seed0 + trials):
        eps = noise_fn(len(Eh), sig, k)
        d, bp, thr = detect(Eh * np.exp(eps), band, nsim=NULL_SIMS, seed=NULL_SEED)
        dets += d
    pwr = dets / trials
    print(f'{label} band={band} H={H} sig={sig} T={T} burn={burn} noise={noise_name}: '
          f'power={pwr:.2f} ({dets}/{trials})', flush=True)
    return pwr

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tmode', default='fixed', choices=('fixed', 'record'))
    ap.add_argument('--T', type=float, default=4000.0)
    ap.add_argument('--burn', type=int, default=20)
    ap.add_argument('--trials', type=int, default=50)
    ap.add_argument('--seed0', type=int, default=0)
    ap.add_argument('--rho', type=float, default=0.6)
    ap.add_argument('--noises', default='white,ar1')
    ap.add_argument('--cells', default='',
                    help='comma-separated cell keys to run (default: all)')
    ap.add_argument('--out', default='power_table_recomputed.json')
    a = ap.parse_args()
    fns = {'white': noise_white, 'ar1': lambda n, s, k: noise_ar1(n, s, k, a.rho)}
    out = {'config': dict(tmode=a.tmode, T=a.T, burn=a.burn, trials=a.trials,
                           seed0=a.seed0, rho=a.rho, null_sims=NULL_SIMS,
                           null_seed=NULL_SEED)}
    want = set(a.cells.split(',')) if a.cells else None
    for name in a.noises.split(','):
        fn = fns[name]
        print(f'===== noise: {name} =====')
        tab = out[name] = {}
        for (label, r, g, Tr, band, H, sig) in CELLS:
            key = f"{label}_H{H}_s{('01' if sig == 0.1 else '03')}"
            if want is not None and key not in want:
                continue
            # +20: integrate_E burns 20 years internally before returning E.
            T = (H + a.burn + 20) if a.tmode == 'record' else a.T
            tab[key] = power_cell(label, r, g, Tr, band, H, sig, T, a.burn,
                                  a.trials, a.seed0, fn, name)
    json.dump(out, open(a.out, 'w'), indent=1)
    print(f"Saved {a.out}")

if __name__ == '__main__':
    main()
