#!/usr/bin/env python3
"""Alternative-band sensitivity + screen figures + cod periodogram (paper 5, S3.5/S3.8).

Reuses the committed per-stock machinery (ram_crosssection: load, spectrum,
band_power; null procedure identical to null_threshold) and validates BEFORE
extending:
  GATE 1: reproduce tr_table.csv band powers (A/B/C/D) from load+spectrum.
  GATE 2: p-value sim engine reproduces null_threshold() 95% cutoffs
          (same RNG stream: default_rng(7), AR(1), linear detrend, LS nf=1500).
Extension (exploratory, honestly labeled):
  - BH screens on baseline A/B, broad (2-10), cadence (1-3/3-8/8-20),
    effort-proxy (8-80) bands; resolution counts (span >= 3 x upper period).
  - Cod post-1995 SSB periodogram (peak period) + CV recompute.
  - Figures: screen q/excess panels; cod SSB+M windows from Table 2 + ICES.

Outputs: bands_sensitivity.log, bands_table.csv, fig_screen_v39.png,
         fig_cod_v39.png
"""
import csv, os, re, sys
import numpy as np
from scipy.signal import lombscargle
sys.path.insert(0, '/home/user/_openitems/release')
from ram_crosssection import load, spectrum, band_power, null_threshold, BANDS

LOG = open('/home/user/_openitems/bands_sensitivity.log', 'w')
def log(*a):
    line = ' '.join(str(x) for x in a)
    print(line, flush=True); LOG.write(line + '\n')

BASE_BANDS = [(b[0], b[1], b[2]) for b in BANDS]
log('committed BANDS:', BASE_BANDS)

def null_pvalues(years, phi, obs, bands, nsim=200, seed=7):
    """Empirical p-values under the committed AR(1) null (same stream as null_threshold)."""
    t = years - years[0]; n = len(years)
    rng = np.random.default_rng(seed)
    freq = np.linspace(1/(2*(years[-1]-years[0])), 0.5, 1500)
    sims = np.zeros((nsim, len(bands)))
    for s in range(nsim):
        e = rng.standard_normal(n)
        x = np.zeros(n); x[0] = e[0]
        for i in range(1, n):
            x[i] = phi*x[i-1] + e[i]
        x = x/np.std(x)
        b1, b0 = np.polyfit(t, x, 1)
        det = x - (b0 + b1*t)
        P = lombscargle(t, det, 2*np.pi*freq); P = P/P.sum()
        for bi, (_, lo, hi) in enumerate(bands):
            m = (freq > 1/hi) & (freq <= 1/lo)
            sims[s, bi] = P[m].sum() if m.any() else 0.0
    return np.array([(1+np.sum(sims[:, bi] >= obs[bi]))/(1+nsim) for bi in range(len(bands))]), sims

def bh(pvals, alpha=0.05):
    p = np.asarray(pvals); m = len(p)
    order = np.argsort(p)
    q = np.empty(m); q[order] = p[order]*m/np.arange(1, m+1)
    for i in range(m-2, -1, -1):
        if q[order[i]] > q[order[i+1]]: q[order[i]] = q[order[i+1]]
    return q, [bool(v) for v in (q < alpha)]

print('=== GATE 1: reproduce tr_table.csv ===', flush=True)
log('=== GATE 1: reproduce tr_table.csv ===')
data = load()
stocks = sorted(s for s in data if len(data[s]) >= 20)
log(f'stocks with n>=20: {len(stocks)}')
ref = {}
with open('/home/user/_openitems/tr_table.csv') as f:
    for row in csv.DictReader(f):
        ref[row['sid']] = row
g1 = True
for sid in stocks:
    ys = data[sid]
    years = np.array([y for y, s in ys]); ssb = np.array([s for y, s in ys])
    freq, P, phi = spectrum(years, ssb)
    bp = [band_power(freq, P, lo, hi) for _, lo, hi in BASE_BANDS]
    if sid in ref:
        for i, k in enumerate('ABCD'):
            if abs(float(ref[sid][k])-round(bp[i], 4)) > 2e-4:
                g1 = False; log(f'  MISMATCH {sid} band {k}')
log('GATE 1:', 'PASSED' if g1 else 'FAILED')
if not g1: sys.exit(1)

print('=== GATE 2: p-engine reproduces null_threshold ===', flush=True)
log('=== GATE 2: p-engine reproduces null_threshold ===')
g2 = True
for sid in stocks[:6]:
    ys = data[sid]
    years = np.array([y for y, s in ys]); ssb = np.array([s for y, s in ys])
    freq, P, phi = spectrum(years, ssb)
    obs = [band_power(freq, P, lo, hi) for _, lo, hi in BASE_BANDS]
    _, sims = null_pvalues(years, phi, obs, BASE_BANDS)
    mine = np.percentile(sims, 95, axis=0)
    ref95 = null_threshold(years, phi)
    if np.max(np.abs(mine-ref95)) > 1e-12:
        g2 = False; log(f'  STREAM MISMATCH {sid}')
log('GATE 2:', 'PASSED (identical RNG stream)' if g2 else 'FAILED')
if not g2: sys.exit(1)

print('=== SCREENS: baseline + alternative bands ===', flush=True)
log('=== SCREENS: baseline + alternative bands ===')
CONFIGS = {
  'baseline A/B': [('A', 2.5, 5), ('B', 5, 9)],
  'broad 2-10': [('W', 2, 10)],
  'cadence 1-3/3-8/8-20': [('C1', 1, 3), ('C2', 3, 8), ('C3', 8, 20)],
  'effort-proxy 8-80': [('E', 8, 80)],
}
table = [['config', 'band', 'n_eligible', 'n_resolvable', 'BH_signif', 'min_q']]
fig_base = None
for cfg, bands in CONFIGS.items():
    P_, cells, excess, eligible, resolvable = [], [], [], 0, 0
    for sid in stocks:
        ys = data[sid]
        years = np.array([y for y, s in ys]); ssb = np.array([s for y, s in ys])
        span = years[-1]-years[0]
        freq, Pw, phi = spectrum(years, ssb)
        obs = [band_power(freq, Pw, lo, hi) for _, lo, hi in bands]
        pvs, sims = null_pvalues(years, phi, obs, bands)
        thr = np.percentile(sims, 95, axis=0)
        for bi, (nm, lo, hi) in enumerate(bands):
            res_ok = span >= 3*hi
            if res_ok: resolvable += 1
            eligible += 1
            P_.append(pvs[bi]); cells.append((sid, nm))
            excess.append(obs[bi]/thr[bi] if thr[bi] > 0 else np.nan)
    q, sig = bh(P_)
    n_sig = sum(sig)
    log(f'{cfg}: cells={len(P_)} eligible={eligible} resolvable(3x)={resolvable} BH-signif={n_sig} min-q={min(q):.4f}')
    if n_sig:
        for (sid, nm), s, qq in zip(cells, sig, q):
            if s: log(f'   SIGNIF {sid} {nm} q={qq:.4f}')
    for bi, (nm, lo, hi) in enumerate(bands):
        idx = [i for i, c in enumerate(cells) if c[1] == nm]
        table.append([cfg, f'{nm}({lo}-{hi})', str(len(idx)),
                      str(sum(1 for i in idx for sid2 in [cells[i][0]]
                              if (data[sid2][-1][0]-data[sid2][0][0]) >= 3*hi)),
                      str(sum(1 for i in idx if sig[i])), f'{min(q[i] for i in idx):.4f}'])
    if cfg == 'baseline A/B':
        fig_base = (np.array(q), np.array(P_), np.array(excess), cells)
with open('/home/user/_openitems/bands_table.csv', 'w', newline='') as f:
    csv.writer(f).writerows(table)

print('=== COD PERIODOGRAM (post-1995 SSB) ===', flush=True)
log('=== COD PERIODOGRAM (post-1995 SSB) ===')
with open('/home/user/_openitems/ices_cod_27_5a.csv') as f:
    rdr = csv.DictReader(f)
    cols = rdr.fieldnames
    log('cod csv cols:', cols)
    yc = [c for c in cols if 'year' in c.lower()][0]
    sc = [c for c in cols if 'ssb' in c.lower() or 'biomass' in c.lower() or 'stock' in c.lower()][0]
    rows = [(int(float(r[yc])), float(r[sc])) for r in rdr]
rows = [(y, v) for y, v in rows if v == v]
post = [(y, v) for y, v in rows if y >= 1995]
ys = np.array([y for y, v in post]); vv = np.array([v for y, v in post])
cv = float(np.std(vv, ddof=1)/np.mean(vv))
t = ys-ys[0]; b1, b0 = np.polyfit(t, vv, 1); det = vv-(b0+b1*t)
freq = np.linspace(1/(2*(ys[-1]-ys[0])), 0.5, 3000)
Pxx = lombscargle(t, det, 2*np.pi*freq); Pxx = Pxx/Pxx.sum()
per = 1/freq
m = (per >= 5) & (per <= 30)
peak_per = float(per[m][np.argmax(Pxx[m])])
log(f'window {ys[0]}-{ys[-1]} n={len(ys)} CV={cv:.4f} (record 0.387/0.394)')
log(f'detrended LS peak in 5-30 yr: period={peak_per:.2f} yr, peak power frac={float(np.max(Pxx[m])):.4f}')

print('=== FIGURES ===', flush=True)
log('=== FIGURES ===')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
q, p, exc, cells = fig_base
fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
ax[0].hist(q, bins=21, range=(0, 1), color='0.6', edgecolor='k')
ax[0].axvline(0.05, color='k', ls='--', lw=1)
ax[0].set_xlabel('BH q-value (84 cells)'); ax[0].set_ylabel('cells')
ax[0].set_title('baseline A/B screen: q distribution')
eA = [e for e, c in zip(exc, cells) if c[1] == 'A']
eB = [e for e, c in zip(exc, cells) if c[1] == 'B']
ax[1].scatter(range(len(eA)), eA, s=12, label='A (2.5-5)')
ax[1].scatter(range(len(eB)), eB, s=12, label='B (5-9)')
ax[1].axhline(1.0, color='k', lw=0.8)
ax[1].set_xlabel('stock index'); ax[1].set_ylabel('power / 95% null threshold')
ax[1].set_title('null-excess per stock'); ax[1].legend(fontsize=8)
fig.tight_layout(); fig.savefig('/home/user/_openitems/fig_screen_v39.png', dpi=150)
log('wrote fig_screen_v39.png')

tex = open('/home/user/paper5_v38/paper5_sampled_governance_v38.tex', encoding='utf-8').read()
i = tex.find('Year & SSB (kt)')
j = tex.find('\\end{longtable}', i)
rows2 = re.findall(r'(\d{4})\s*&\s*([\d.]+)\s*&\s*\$?\\?\(?M\$?\\?\)?\s*\(yr\$\^\{-1\}\$\)\s*&\s*\$?\\exp\(-M\)\$?', tex[i:j])
t2 = re.findall(r'(\d{4})\s*&\s*([\d.]+)\s*&\s*([\d.]+)\s*&\s*([\d.]+)', tex[i:j])
log(f'parsed Table 2 rows: {len(t2)} ({t2[0][0]}-{t2[-1][0]})' if t2 else 'TABLE 2 PARSE FAILED')
if t2:
    T2y = np.array([int(r[0]) for r in t2]); T2s = np.array([float(r[1]) for r in t2]); T2m = np.array([float(r[2]) for r in t2])
    fig, ax1 = plt.subplots(figsize=(7.2, 4.2))
    ax1.plot(T2y, T2s, 'k.-', ms=3, label='SSB (kt, Table 2)')
    ax1.axvspan(1991, 1995, color='0.85', label='crash window')
    ax1.axvspan(1995, T2y[-1], color='0.92', label='non-recovery window')
    ax1.set_xlabel('year'); ax1.set_ylabel('SSB (kt)')
    ax2 = ax1.twinx()
    ax2.step(T2y, T2m, 'r-', where='mid', label='M (yr-1)')
    ax2.set_ylabel('M (yr-1)', color='r')
    ax1.set_title('Northern cod: Table-2 SSB and natural mortality by window')
    fig.tight_layout(); fig.savefig('/home/user/_openitems/fig_cod_v39.png', dpi=150)
    log('wrote fig_cod_v39.png')
log('DONE')
LOG.close()
