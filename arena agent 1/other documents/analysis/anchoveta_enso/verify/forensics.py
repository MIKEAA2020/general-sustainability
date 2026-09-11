#!/usr/bin/env python3
"""Executable forensics record for the anchoveta-ENSO battery verification (2026-09-11).

Self-contained: run from /home/user/verify_battery/ with ./deposited (repo-committed
inputs+outputs of analysis/anchoveta_enso/) and ./frozen_inputs (NOAA PSL .data files
fetched 2026-09-11). Requires numpy/scipy/pandas/statsmodels (NOT pyEDM).

Proves, in order:
  1. NINO pipeline: frozen PSL fetch == deposited indices_annual.json on 1950-2019.
  2. SOI artifact: raw PSL soi.data (1950 = -99.99 missing flag, unfiltered by the
     author's parse_psl) reproduces ALL 90 committed v2 xcorr cells bit-exactly --
     i.e. the committed soi_ok.data input was raw PSL soi.data, missing flag included.
  3. Artifact-free SOI table (1950 dropped): all 18 SOI cells null.
  4. Crash-year exclusion decoded: T = {1972,1973,1983,1984,1998}, plain year-filter,
     cut-1985 halves -> supplementary entry reproduced exactly.
  5. Standalone files' provenance: xcorr_results.json == v1 r-extract;
     granger_results.json == RAM-series (v1-input) Granger via NINO1.
  6. Supplementary peaks + SOI splits reproduced (artifact included, as committed).
"""
import re, math, json
import numpy as np
import pandas as pd
from scipy import stats
from scipy.signal import lombscargle
from statsmodels.tsa.stattools import grangercausalitytests

import os
# Repo layout: run from analysis/anchoveta_enso/verify/ (inputs = parent dir).
# Workspace layout: run from verify_battery/ (inputs = deposited/ + frozen_inputs/).
DEP = 'deposited' if os.path.isdir('deposited') else '..'
FRZ = 'frozen_inputs' if os.path.isdir('frozen_inputs') else 'frozen_inputs'
fails = []
def check(name, cond, detail=''):
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {detail}")
    if not cond: fails.append(name)

def parse_psl(fn):
    rows = {}; cur_year = None
    for line in open(fn):
        line = line.strip()
        if not line: continue
        toks = line.split()
        if len(toks) == 2 and re.fullmatch(r"\d{4}", toks[0]) and re.fullmatch(r"\d{4}", toks[1]): continue
        if re.fullmatch(r"\d{4}", toks[0]) and len(toks) > 1:
            cur_year = int(toks[0]); toks = toks[1:]
        if cur_year is None: continue
        vals = [float(t) for t in toks if re.match(r"-?\d+(\.\d+)?$", t)]
        rows.setdefault(cur_year, []).extend(vals)
    return {y: sum(v)/len(v) for y, v in rows.items() if v}

def load_annual(fn, header=True):
    d = {}
    for line in open(fn):
        line = line.strip()
        if not line or (header and line.startswith('year')) or line.startswith('"'): continue
        p = line.split(','); d[int(p[0])] = float(p[1])
    return d

def xcell(catch, idx, lag):
    yrs = sorted(set(catch) & set(idx))
    x = np.array([math.log(catch[y]) for y in yrs]); x = x - x.mean()
    z = np.array([idx[y] for y in yrs]); z = z - z.mean()
    if lag >= 0: xa, za = x[lag:], z[:-lag] if lag else z
    else: xa, za = x[:lag], z[-lag:]
    r, p = stats.pearsonr(xa, za)
    return float(r), float(p), len(xa)

# ---------- inputs ----------
dep_idx = json.load(open(f'{DEP}/indices_annual.json'))
NINO = {n: {int(k): v for k, v in dep_idx[n].items()} for n in ('NINO1','NINO3','NINO34','NINO4')}
soi_raw = parse_psl(f'{FRZ}/soi.data')
soi_clean = {y: v for y, v in soi_raw.items() if v > -90}
peru = {y: v for y, v in load_annual(f'{DEP}/peru_sau_annual.csv').items() if 1950 <= y <= 2019}
chile = {y: v for y, v in load_annual(f'{DEP}/chile_sau_annual.csv').items() if 1950 <= y <= 2019}
ram_peru = load_annual(f'{DEP}/PANCHNCHSP_catch.csv'); ram_chile = load_annual(f'{DEP}/PANCHCCH_catch.csv')

# ---------- 1. NINO pipeline ----------
for n, f in (('NINO1','nina1'),('NINO3','nina3'),('NINO34','nina34'),('NINO4','nina4')):
    got = parse_psl(f'{FRZ}/{f}.anom.data')
    md = max(abs(got[y] - NINO[n][y]) for y in range(1950, 2020))
    check(f'NINO pipeline {n} (frozen fetch == deposited, 1950-2019)', md == 0.0, f'max|diff|={md:.1e}')

# ---------- 2. SOI artifact: 90/90 ----------
check('raw PSL parse keeps 1950 = -99.99 missing flag', soi_raw[1950] == -99.99)
IDX = dict(NINO); IDX['SOI'] = soi_raw
SER = {'Peru': peru, 'Chile': chile}
cells = json.load(open(f'{DEP}/battery_v2_results.json'))['xcorr']
miss = sum(1 for e in cells
           if (lambda r, p, n: abs(r-e['r']) > 2e-9 or abs(p-e['p']) > 1e-11 or n != e['n'])
           (*xcell(SER[e['series']], IDX[e['index']], e['lag'])))
check('v2 90-cell sweep reproduced with raw-PSL SOI (artifact included)', miss == 0, f'{90-miss}/90 exact')

# ---------- 3. artifact-free SOI ----------
print('--- artifact-free SOI xcorr (1950 dropped) ---')
allnull = True
for s in ('Peru', 'Chile'):
    for lag in range(-4, 5):
        r, p, n = xcell(SER[s], soi_clean, lag)
        allnull &= (p > 0.05)
        print(f'  {s:5s} lag={lag:+d} r={r:+.4f} p={p:.4f} n={n}')
check('all 18 artifact-free SOI cells null at 0.05 (uncorrected)', allnull)

# ---------- 4. crash-year exclusion ----------
T = {1972, 1973, 1983, 1984, 1998}
re_, pe, ne = xcell({y: v for y, v in peru.items() if 1950 <= y <= 1984 and y not in T}, soi_raw, 1)
rl, pl, nl = xcell({y: v for y, v in peru.items() if 1985 <= y <= 2019 and y not in T}, soi_raw, 1)
want = json.load(open(f'{DEP}/supplementary_results.json'))['peru_excl_crash_years_lag1']
check('crash exclusion T={1972,73,83,84,98} early', (round(re_,3),round(pe,4),ne)==(want['early'][0],want['early'][1],30), f'({re_:.3f},{pe:.4f},{ne})')
check('crash exclusion T={1972,73,83,84,98} late', (round(rl,3),round(pl,3),nl)==(want['late'][0],want['late'][1],33), f'({rl:.3f},{pl:.4f},{nl})')

# ---------- 5. standalone provenance ----------
xc = json.load(open(f'{DEP}/xcorr_results.json'))
c1 = json.load(open(f'{DEP}/battery_results.json'))['xcorr']
ok = all(abs(xc[e['series']][e['index']][str(e['lag'])] - e['r']) == 0.0 for e in c1)
check('xcorr_results.json == v1 xcorr r-extract (180 values)', ok)
def gr(s, i):
    yrs = sorted(set(s) & set(i))
    df = pd.DataFrame({"catch": [math.log(s[y]) for y in yrs], "enso": [i[y] for y in yrs]})
    o = {}
    for d, cols in [("E->c", ["catch","enso"]), ("c->E", ["enso","catch"])]:
        g = grangercausalitytests(df[cols], maxlag=3)
        o[d] = {str(l): round(float(v[0]["ssr_ftest"][1]), 4) for l, v in g.items()}
    return o
sg = json.load(open(f'{DEP}/granger_results.json'))
gp, gc = gr(ram_peru, NINO['NINO1']), gr(ram_chile, NINO['NINO1'])
ok = (gp['E->c']==sg['Peru_ENSO->catch'] and gp['c->E']==sg['Peru_catch->ENSO']
      and gc['E->c']==sg['Chile_ENSO->catch'] and gc['c->E']==sg['Chile_catch->ENSO'])
check('granger_results.json == RAM-series NINO1 Granger (12 values)', ok)

# ---------- 6. supp peaks + SOI splits ----------
def top2(s):
    yrs = sorted(s); x = np.array(yrs)
    y = np.log(np.array([s[yy] for yy in yrs])); y = y - y.mean()
    f = np.linspace(1/10, 1/1.5, 4000); pg = lombscargle(x, y, 2*np.pi*f, normalize=True)
    i1 = int(np.argmax(pg)); pg2 = pg.copy(); pg2[max(0,i1-400):i1+400] = -1; i2 = int(np.argmax(pg2))
    return [(round(float(1/f[i1]),2),round(float(pg[i1]),3)),(round(float(1/f[i2]),2),round(float(pg[i2]),3))]
sup = json.load(open(f'{DEP}/supplementary_results.json'))
p1 = top2({y: v for y, v in load_annual(f'{DEP}/peru_sau_annual.csv').items() if 1950 <= y <= 2019})
p2 = top2({y: v for y, v in load_annual(f'{DEP}/peru_sau_annual.csv').items() if 1960 <= y <= 2019})
check('supp Peru peaks 1950-2019 (7.96/0.029, 3.70/0.027)', p1==[(7.96,0.029),(3.7,0.027)], str(p1))
check('supp Peru peaks 1960-2019 (6.17/0.052, 3.63/0.049)', p2==[(6.17,0.052),(3.63,0.049)], str(p2))
nsp = 0; nst = 0
for sname, S in (('peru', peru), ('chile', chile)):
    for lag in (0, 1, 2):
        for half, lo, hi in (('early',1950,1984),('late',1985,2019)):
            w = sup.get(f'split_half_{sname}_soi', {}).get(f'lag{lag}', {}).get(half)
            if w is None: continue
            nst += 1
            r, p, _ = xcell({y: v for y, v in S.items() if lo <= y <= hi}, soi_raw, lag)
            nsp += (round(r,3) == w[0] and round(p,4) == w[1])
check('supp SOI splits (artifact included, as committed)', nsp == nst, f'{nsp}/{nst}')

print(f"\nFORENSICS: {'ALL PASS' if not fails else 'FAILURES: '+str(fails)}")
raise SystemExit(1 if fails else 0)
