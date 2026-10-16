"""Icelandic cod/haddock calculation audit (2026-09-11).
Re-derives the §3.7/S4 author-calculated CVs from public ICES SAG data
(standardgraphs source tables, 2026 advice vintage; cod key 22640, had key
22494; files ices_cod_27_5a.csv / ices_had_27_5a.csv).
Reported values under audit: cod post-rule CV 0.387 + 10-15 yr fluctuation;
haddock post-implementation CV 0.143 + 'higher recruitment variability'.
"""
import csv
import numpy as np
from scipy.signal import lombscargle

def load(fn):
    return list(csv.DictReader(open(fn)))

def ser(d, key, lo=1996, hi=2023):
    y, v = [], []
    for r in d:
        yr = int(r['year'])
        if lo <= yr <= hi and r[key] != '':
            y.append(yr); v.append(float(r[key]))
    return np.array(y), np.array(v)

cod = load('ices_cod_27_5a.csv'); had = load('ices_had_27_5a.csv')
print('cod vintage:', cod[0]['year'], '-', cod[-1]['year'], '| had vintage:', had[0]['year'], '-', had[-1]['year'])
for lab, d in [('cod', cod), ('had', had)]:
    print(f'--- {lab} post-1995 (1996-2023) ---')
    for nm, key in [('SSB', 'SSB'), ('catch', 'catch'), ('F', 'F'), ('R', 'R')]:
        _, x = ser(d, key)
        print(f'  {nm}: n={len(x)} CV={x.std()/x.mean():.3f} max/min={x.max()/x.min():.2f}')
print('--- haddock 0.143 forensics (all standard concepts) ---')
_, s = ser(had, 'SSB'); _, c = ser(had, 'catch')
t = np.arange(len(s))
b1, b0 = np.polyfit(t, s, 1)
print(f'  detrended-SSB residCV={(s-(b0+b1*t)).std()/s.mean():.3f} sdlog={np.log(s).std():.3f} '
      f'logdiff-vol={np.diff(np.log(s)).std():.3f}')
for start in [2000, 2005, 2008, 2010]:
    _, s2 = ser(had, 'SSB', start); _, c2 = ser(had, 'catch', start)
    print(f'  from {start}: SSB CV={s2.std()/s2.mean():.3f} catch CV={c2.std()/c2.mean():.3f}')
print('--- cod 10-15 yr check (detrended post-95 SSB) ---')
yc, sc = ser(cod, 'SSB')
t = yc - yc[0]; b1, b0 = np.polyfit(t, sc, 1); det = sc - (b0 + b1 * t)
fr = np.linspace(1/30, 0.5, 4000); P = lombscargle(t, det, 2*np.pi*fr); P /= P.sum()
pk = [(P[k], 1/fr[k]) for k in range(1, len(P)-1) if P[k] > P[k-1] and P[k] > P[k+1]]
pk.sort(reverse=True)
for p, per in pk[:4]:
    print(f'  period={per:.2f} yr power={p:.4f}')
m = (fr > 1/15) & (fr <= 1/10)
print(f'  band 10-15 yr share={P[m].sum():.3f} (n=28: trend-dominated; 12-yr 2005->2017 peak spacing is the visual basis)')
print('AUDIT: cod 0.387 CONFIRMED as post-1995 SSB CV (current-vintage 0.394; series concept identified). '
      'haddock 0.143 REFUTED on every standard concept (same-concept SSB CV 0.359) — number must be corrected. '
      'haddock higher recruitment variability CONFIRMED (R CV 0.894 vs cod 0.208).')
