#!/usr/bin/env python3
"""F-calibration and cross-system placement (paper 5).

q is not directly calibratable (model effort units are bare); the calibratable
object is equilibrium fishing mortality F* = qE* (yr^-1, same units as
assessed F). This script places assessed-F distributions (42-stock screen
cohort from ram_target_stocks.csv; 454-stock broader pool from
v466_broader_cohort.csv) against the model's F* grid (S11.2: stable below
~0.002, marginal at baseline 0.00209, infeasible F* > r = 0.02).

GATES (before extension):
  G1: screen-cohort reproduction: stocks with >=20 valid SSB points == 42.
  G2: series->summary pipeline: reproduce fisheries_adh.csv F column
      (mean-F or last-F must match to rounding on intersection).
  G3: broader F quartiles reproduce broader_results.json F_q (overall +
      per-taxGroup medians).
EXTENSION:
  - per-stock F stats + placement class (fplacement_table.csv)
  - vintage check v444 vs v466 (paired, intersection)
  - TC/SSB exploitation cross-check vs F (Spearman)
  - exploratory: mean F vs band null-excess (tr_table.csv; Spearman)

Outputs: qcal_fplacement.log, fplacement_table.csv
"""
import csv, math, sys
import numpy as np
from scipy.stats import spearmanr

LOG = open('/home/user/_openitems/qcal_fplacement.log', 'w')
def log(*a):
    line = ' '.join(str(x) for x in a)
    print(line, flush=True); LOG.write(line + '\n')

def num(x):
    try: return float(x)
    except (TypeError, ValueError): return None

# ---------- load RAM target series ----------
series = {}
with open('/home/user/_openitems/ram_target_stocks.csv') as f:
    for row in csv.DictReader(f):
        sid = row['stockid'].strip('"')
        series.setdefault(sid, []).append((int(row['tsyear']), num(row['F']), num(row['TC']), num(row['SSB'])))
log(f'stocks in ram_target_stocks.csv: {len(series)}')

def valid_ssb(sid):
    return [(y, s) for y, f_, tc, s in series[sid] if s is not None and s == s]
cohort = sorted(s for s in series if len(valid_ssb(s)) >= 20)
log(f'G1: stocks with n>=20 valid SSB: {len(cohort)} (expect 42)')
assert len(cohort) == 42, 'G1 FAILED'
dropped = sorted(set(series) - set(cohort))
log(f'  below-threshold stocks: {dropped}')

def fstats(sid):
    fs = [(y, f_) for y, f_, tc, s in series[sid] if f_ is not None and f_ == f_]
    v = np.array([f_ for _, f_ in fs])
    if len(v) == 0:
        return dict(n=0, mean=None, med=None, mx=None, last=None)
    return dict(n=len(v), mean=float(np.mean(v)), med=float(np.median(v)),
                mx=float(np.max(v)), last=fs[-1][1] if fs else None)

# ---------- G2: reproduce fisheries_adh.csv F ----------
adh = {}
with open('/home/user/_openitems/xsys/fisheries_adh.csv') as f:
    for row in csv.DictReader(f):
        adh[row['stock']] = float(row['F'])
log(f'fisheries_adh rows: {len(adh)}')
m_mean = m_last = 0; worst = (None, 9e9)
for sid in sorted(set(adh) & set(series)):
    st = fstats(sid)
    if st['n'] == 0: continue
    dm = abs(st['mean']-adh[sid]); dl = abs((st['last'] or 9e9)-adh[sid])
    if dm < 5e-4: m_mean += 1
    if dl < 5e-4: m_last += 1
    worst = min(worst, (sid, min(dm, dl)), key=lambda t: -t[1] if False else 0)
log(f"G2: mean-F matches {m_mean}, last-F matches {m_last} (of {len(set(adh)&set(series))} intersected)")
# report worst mismatches for the record
bad = []
for sid in sorted(set(adh) & set(series)):
    st = fstats(sid)
    if st['n'] and min(abs(st['mean']-adh[sid]), abs((st['last'] or 9e9)-adh[sid])) >= 5e-4:
        bad.append((sid, round(adh[sid],4), round(st['mean'],4), st['last'], st['n']))
log(f'  non-matching stocks: {bad if bad else "none"}')
G2 = 'mean' if m_mean >= m_last else 'last'
log(f'  G2 verdict: fisheries_adh F = {G2}-F ({max(m_mean,m_last)} matches)')
assert max(m_mean, m_last) >= 40, 'G2 FAILED'

# ---------- broader pool ----------
broad = []
with open('/home/user/_openitems/xsys/v466_broader_cohort.csv') as f:
    for row in csv.DictReader(f):
        broad.append(row)
log(f'broader rows: {len(broad)} (expect 454)')
assert len(broad) == 454, 'broader n FAILED'
Fnow = np.array([float(r['F_now']) for r in broad])
groups = {}
for r in broad:
    groups.setdefault(r['taxGroup'], []).append(float(r['F_now']))
import json
br = json.load(open('/home/user/_openitems/xsys/broader_results.json'))
q = [float(np.percentile(Fnow, p)) for p in (25, 50, 75)]
log(f"G3: broader F quartiles mine {[round(v,4) for v in q]} vs record {br['v466_overall']['F_q']}")
assert all(abs(a-b) < 5e-4 for a, b in zip(q, br['v466_overall']['F_q'])), 'G3 overall FAILED'
gmiss = 0
for g, vs in sorted(groups.items()):
    rec = br.get(f'v466_{g}', {}).get('F_q')
    mine = [round(float(np.percentile(vs, p)), 4) for p in (25, 50, 75)]
    ok = rec is not None and all(abs(a-b) < 5e-3 for a, b in zip(mine, rec))
    gmiss += (not ok)
    log(f"  group {g}: n={len(vs)} mine={mine} record={rec} {'OK' if ok else 'DIFF'}")
log(f'G3 verdict: {len(groups)-gmiss}/{len(groups)} group quartile triples match')
assert gmiss == 0, 'G3 groups FAILED'
log('ALL GATES PASSED.')

# ---------- placement ----------
def pclass(f):
    if f < 0.001: return 'below-stable'
    if f <= 0.004: return 'marginal'
    if f <= 0.02: return 'unstable-range'
    return 'beyond-feasible'
noF = sorted(s for s in cohort if fstats(s)['n'] == 0)
log(f'stocks with valid SSB but no F series (excluded from F summaries): {noF}')
cohortF = [s for s in cohort if fstats(s)['n'] > 0]
log(f'=== COHORT F (mean-F per stock, n={len(cohortF)}) ===')
fm = np.array([fstats(s)['mean'] for s in cohortF])
log(f'median={np.median(fm):.4f} IQR=[{np.percentile(fm,25):.4f},{np.percentile(fm,75):.4f}] range=[{fm.min():.4f},{fm.max():.4f}]')
log(f'scale factor vs baseline F*=0.00209: median {np.median(fm)/0.00209:.0f}x')
from collections import Counter
cc = Counter(pclass(v) for v in fm)
log(f'placement classes (mean-F): {dict(cc)}')
rows = [['stockid','n_SSB','n_F','F_mean','F_med','F_max','placement']]
for s in cohort:
    st = fstats(s)
    if st['n'] == 0:
        rows.append([s, str(len(valid_ssb(s))), '0', '-', '-', '-', 'no-F'])
    else:
        rows.append([s, str(len(valid_ssb(s))), str(st['n']), f"{st['mean']:.4f}",
                     f"{st['med']:.4f}", f"{st['mx']:.4f}", pclass(st['mean'])])
with open('/home/user/_openitems/fplacement_table.csv', 'w', newline='') as f:
    csv.writer(f).writerows(rows)
log('wrote fplacement_table.csv')
log('=== BROADER F_now (n=454) ===')
log(f'median={np.median(Fnow):.4f} IQR=[{np.percentile(Fnow,25):.4f},{np.percentile(Fnow,75):.4f}]')
log(f'scale factor vs baseline: median {np.median(Fnow)/0.00209:.0f}x')
cb = Counter(pclass(v) for v in Fnow)
log(f'placement classes (F_now): {dict(cb)}')

# ---------- vintage check ----------
v444 = {}
with open('/home/user/_openitems/xsys/v444_adh_cohort.csv') as f:
    for row in csv.DictReader(f):
        v444[row['stockid']] = float(row['F_now'])
v466map = {r['stockid']: float(r['F_now']) for r in broad}
inter = sorted(set(v444) & set(v466map))
rev = np.array([abs(v444[s]-v466map[s]) for s in inter])
log(f'=== VINTAGE v444 vs v466: {len(inter)} paired stocks ===')
log(f'median |dF|={np.median(rev):.4f}, median F_now v444={np.median([v444[s] for s in inter]):.4f} v466={np.median([v466map[s] for s in inter]):.4f}')

# ---------- TC cross-check ----------
pairs = []
for sid in cohort:
    for y, f_, tc, s in series[sid]:
        if f_ is not None and tc is not None and s is not None and s > 0 and f_ == f_ and tc == tc:
            pairs.append((f_, tc/s))
pairs = np.array(pairs)
rho, p = spearmanr(pairs[:,0], pairs[:,1])
log(f'=== TC/SSB vs F: n={len(pairs)} Spearman rho={rho:.4f} p={p:.2e} ===')

# ---------- exploratory: mean F vs band null-excess ----------
tr = {}
with open('/home/user/_openitems/tr_table.csv') as f:
    for row in csv.DictReader(f):
        tr[row['sid']] = row
xs, eA, eB = [], [], []
for s in cohortF:
    if s in tr:
        xs.append(fstats(s)['mean'])
        eA.append(float(tr[s]['A'])/float(tr[s]['A95']))
        eB.append(float(tr[s]['B'])/float(tr[s]['B95']))
for nm, e in (('A', eA), ('B', eB)):
    rho, p = spearmanr(xs, e)
    log(f'F-mean vs band-{nm} excess: n={len(xs)} Spearman rho={rho:.4f} p={p:.4f} (prediction under dormancy: ~0)')
import sys as _sys; _sys.path.insert(0, '/home/user/_openitems/release')
from ram_crosssection import regime as _regime
keep = [i for i, sd in enumerate([sd for sd in cohortF if sd in tr]) if _regime(sd) != 'Peru/Chile annual+in-season']
xs2 = [xs[i] for i in keep]
for nm, e in (('A', eA), ('B', eB)):
    e2 = [e[i] for i in keep]
    rho, p = spearmanr(xs2, e2)
    log(f'F-mean vs band-{nm} excess, Peru/Chile OUT: n={len(xs2)} Spearman rho={rho:.4f} p={p:.4f}')
log('DONE')
LOG.close()
