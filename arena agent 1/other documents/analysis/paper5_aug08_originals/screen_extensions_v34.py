"""Screen extensions v34: endpoint-trim check + periodogram deposit dump.

(a) Endpoint trims (README_verification gap 4 residue): fixed 42-stock cohort,
    drop-first-5 / drop-last-5 / drop-3+3 years; rerun the published machinery
    (linear detrend, Lomb-Scargle nf=1500 grid, seed-7 AR(1) null, 200 sims,
    empirical p=(k+1)/201, BH-FDR over the 84 A/B target-band cells).
    Pass criterion: verdict stability of the BH-adjusted zero count.
(b) Periodogram dump: normalized Lomb-Scargle periodograms (nf=1500) for the
    42 eligible stocks -> screen_periodograms_v34.csv (long format).
"""
import csv
import hashlib
import numpy as np
from scipy.signal import lombscargle

CSV = '/home/user/_a6work/battery/ram_target_stocks.csv'
BANDS_AB = [('A 2.5-5', 2.5, 5), ('B 5-9', 5, 9)]
NF, NSIM, SEED, ALPHA = 1500, 200, 7, 0.05


def load():
    rows = {}
    with open(CSV) as f:
        for d in csv.DictReader(f):
            if d['SSB'] in ('', 'NA'):
                continue
            rows.setdefault(d['stockid'], []).append(
                (int(d['tsyear']), float(d['SSB'])))
    return {k: sorted(v) for k, v in rows.items()}


def spectrum_of(years, ssb):
    t = years - years[0]
    b1, b0 = np.polyfit(t, ssb, 1)
    det = ssb - (b0 + b1 * t)
    freq = np.linspace(1 / (2 * (years[-1] - years[0])), 0.5, NF)
    P = lombscargle(t, det, 2 * np.pi * freq)
    P = P / P.sum()
    phi = float(np.corrcoef(det[:-1], det[1:])[0, 1]) if len(det) >= 4 else 0.0
    return freq, P, phi, det, t


def band_power(freq, P, lo, hi):
    m = (freq > 1 / hi) & (freq <= 1 / lo)
    return float(P[m].sum()) if m.any() else 0.0


def run_trim(data, name, drop_first, drop_last):
    prow = []
    for sid in sorted(data):
        pts = data[sid]
        if len(pts) < 20:
            continue
        cut = pts[drop_first: len(pts) - drop_last if drop_last else len(pts)]
        years = np.array([y for y, s in cut])
        ssb = np.array([s for y, s in cut])
        freq, P, phi, det, t = spectrum_of(years, ssb)
        n = len(years)
        rng = np.random.default_rng(SEED)
        sims = np.zeros((NSIM, 2))
        for s in range(NSIM):
            e = rng.standard_normal(n)
            x = np.zeros(n)
            x[0] = e[0]
            for i in range(1, n):
                x[i] = phi * x[i - 1] + e[i]
            x = x / np.std(x)
            b1, b0 = np.polyfit(t, x, 1)
            dx = x - (b0 + b1 * t)
            Px = lombscargle(t, dx, 2 * np.pi * freq)
            Px = Px / Px.sum()
            for bi, (_, lo, hi) in enumerate(BANDS_AB):
                m = (freq > 1 / hi) & (freq <= 1 / lo)
                sims[s, bi] = Px[m].sum()
        for bi, (bname, lo, hi) in enumerate(BANDS_AB):
            bp = band_power(freq, P, lo, hi)
            p = float((np.sum(sims[:, bi] >= bp) + 1) / (NSIM + 1))
            prow.append((sid, bname, len(years), bp, p))
    m = len(prow)
    order = sorted(range(m), key=lambda i: prow[i][4])
    maxrank = 0
    for rank, i in enumerate(order, start=1):
        if prow[i][4] <= rank / m * ALPHA:
            maxrank = rank
    rej = set(order[:maxrank])
    ns = sorted({r[2] for r in prow})
    print(f'=== {name} (drop_first={drop_first}, drop_last={drop_last}): '
          f'tests={m} BH rejections={len(rej)} '
          f'[{"STABLE-ZERO" if not rej else "NONZERO"}] trimmed-n range '
          f'{min(ns)}-{max(ns)}')
    for i in order[:5]:
        print(f'    {prow[i][0]:15s} {prow[i][1]:8s} n={prow[i][2]:3d} '
              f'bp={prow[i][3]:.3f} p={prow[i][4]:.4f}')
    return prow, rej


def main():
    data = load()
    n_elig = sum(1 for v in data.values() if len(v) >= 20)
    print(f'stocks with n>=20: {n_elig}')
    results = {}
    results['trim_first5'] = run_trim(data, 'trim-first-5yr', 5, 0)
    results['trim_last5'] = run_trim(data, 'trim-last-5yr', 0, 5)
    results['trim_ends3'] = run_trim(data, 'trim-ends-3+3yr', 3, 3)
    print()
    print('TRIM      BHrej  VERDICT')
    for k, (prow, rej) in results.items():
        print(f'{k:10s} {len(rej):5d}  '
              f'{"STABLE-ZERO" if not rej else "NONZERO"}')
    # (b) periodogram dump (untrimmed, published machinery)
    outp = '/home/user/_v34work/screen_periodograms_v34.csv'
    nrows = 0
    with open(outp, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['stockid', 'n', 'freq_cyc_per_yr', 'power_norm'])
        for sid in sorted(data):
            pts = data[sid]
            if len(pts) < 20:
                continue
            years = np.array([y for y, s in pts])
            ssb = np.array([s for y, s in pts])
            freq, P, phi, det, t = spectrum_of(years, ssb)
            for fr, pw in zip(freq, P):
                w.writerow([sid, len(years), f'{fr:.8f}', f'{pw:.10f}'])
                nrows += 1
    h = hashlib.sha256(open(outp, 'rb').read()).hexdigest()
    print()
    print(f'periodogram dump: {nrows} rows, sha256={h}')


if __name__ == '__main__':
    main()
