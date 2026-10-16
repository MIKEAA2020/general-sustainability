"""Verify v29's 'BH-adjusted zero count' from the recovered screen machinery.
Reuses ram_crosssection's exact functions (linear detrend, LS grid, AR(1) null,
seed 7, 200 sims); computes empirical p-values; applies BH-FDR over the
target-band family (42 stocks x bands A,B) at alpha=0.05."""
import numpy as np
from ram_crosssection import load, spectrum, band_power, BANDS, null_threshold
from scipy.signal import lombscargle

data = load()
rows = []
for sid in sorted(data):
    yr_s = data[sid]
    years = np.array([y for y, s in yr_s]); ssb = np.array([s for y, s in yr_s])
    if len(ssb) < 20: continue
    freq, P, phi = spectrum(years, ssb)
    # rebuild null sims with same seed to get empirical p-values
    t = years - years[0]; n = len(years)
    rng = np.random.default_rng(7)
    sims = np.zeros((200, 2))
    for s in range(200):
        e = rng.standard_normal(n); x = np.zeros(n); x[0] = e[0]
        for i in range(1, n): x[i] = phi * x[i-1] + e[i]
        x = x / np.std(x)
        b1, b0 = np.polyfit(t, x, 1); det = x - (b0 + b1*t)
        Ps = lombscargle(t, det, 2*np.pi*freq); Ps = Ps / Ps.sum()
        for bi, (_, lo, hi) in enumerate(BANDS[:2]):
            m = (freq > 1/hi) & (freq <= 1/lo)
            sims[s, bi] = Ps[m].sum()
    for bi, (bname, lo, hi) in enumerate(BANDS[:2]):
        bp = band_power(freq, P, lo, hi)
        p = float((np.sum(sims[:, bi] >= bp) + 1) / (200 + 1))
        rows.append((sid, bname, bp, p))

# BH-FDR, alpha=0.05, family = 42x2 = 84 tests
m = len(rows); alpha = 0.05
order = sorted(range(m), key=lambda i: rows[i][3])
bh_reject = set()
for rank, i in enumerate(order, start=1):
    if rows[i][3] <= rank / m * alpha: bh_reject.add(i)
# BH step-up: reject all up to largest passing rank
maxrank = 0
for rank, i in enumerate(order, start=1):
    if rows[i][3] <= rank / m * alpha: maxrank = rank
bh_set = set(order[:maxrank])
print(f'tests: {m}, alpha={alpha}')
print('smallest 5 p-values:')
for i in order[:5]:
    print(f'  {rows[i][0]:15s} {rows[i][1]:8s} bandpower={rows[i][2]:.3f} p={rows[i][3]:.4f}')
print(f'BH rejections: {len(bh_set)}')
for i in sorted(bh_set): print('  REJECT:', rows[i])
print('VERDICT:', 'ZERO COUNT CONFIRMED (BH-adjusted)' if not bh_set else 'NONZERO after BH')
