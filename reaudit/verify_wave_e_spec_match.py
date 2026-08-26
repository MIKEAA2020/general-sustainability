#!/usr/bin/env python3
"""Wave E Part III spec matching: freeze + match the scored-tree specifications.

For each scored tree (wave_e_edwards, wave_e_cod) this script:

1. reads the FROZEN specification (S, Omega, y_t, T, scoring rule) from the
   committed protocol / manuscript-spec records;
2. machine-matches the committed result artifacts against that specification:
   recomputes the primary scores from the per-observation forecast files (and,
   for the naive baselines, from the committed raw series) and checks them
   against the recorded summaries; checks the model-ladder set, the window
   definitions, the rolling-origin counts, the retention-rule application,
   and the frozen-protocol markers;
3. prints a per-check verdict and exits 0 iff every machine check passes.

Known artifact coverage limitation (recorded, not a failure): in the cod tree
the per-observation rolling artifact (`rolling_forecasts.csv`) stores the
annual-catch (Schijns) treatment; the regime-catch treatment is recorded at
summary level only. The regime rows are checked for presence and internal
consistency; their per-observation match is recorded as summary-level.

Status discipline: a pass of this script records SPEC-MATCHED at the artifact
level for the scored trees. It does NOT close any Wave E gate and does NOT
flip any Part III paper-support row (those concern paper claims, not the
trees). See batch 4/WAVE_E_SPEC_MATCH.md for the verdict record.
"""
from __future__ import annotations

import csv
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EDW = REPO / 'wave_e_edwards'
COD = REPO / 'wave_e_cod'

failures = []
passes = 0
notes = []


def check(name, ok, detail=''):
    global passes
    if ok:
        passes += 1
        print(f'  PASS  {name}' + (f' — {detail}' if detail else ''))
    else:
        failures.append(name)
        print(f'  FAIL  {name} — {detail}')


def read_csv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))


def close(a, b, tol=1e-8):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def recompute(rows, keys):
    groups = defaultdict(list)
    for r in rows:
        k = tuple(int(r[kk]) if kk == 'horizon' else r[kk] for kk in keys)
        groups[k].append(r)
    out = {}
    for k, g in groups.items():
        n = len(g)
        rmse = math.sqrt(sum(float(r['sqerr']) for r in g) / n)
        mae = sum(float(r['abserr']) for r in g) / n
        out[k] = (n, rmse, mae)
    return out


def series_map(path, ycol, vcol):
    return {int(r[ycol]): float(r[vcol]) for r in read_csv(path)}


def naive_rmse(series, origins, h):
    """last-value persistence RMSE over given origins at horizon h."""
    errs = [(series[o + h] - series[o]) ** 2 for o in origins]
    return math.sqrt(sum(errs) / len(errs))


def last_n_origins(series, h, n):
    """The n most recent origins o with both o and o+h in the series."""
    elig = [o for o in sorted(series) if o + h in series]
    return elig[-n:]


print('== Edwards (Omega_SA): frozen protocol.md ==')

# 0. frozen-protocol markers
proto = (EDW / 'protocol.md').read_text()
check('protocol lock marker',
      'Locked 2026-08-25' in proto
      and 'Retention is decided only after this file exists' in proto)
check('protocol_pass2 exists', (EDW / 'protocol_pass2.md').exists())

# 1. the object: J-17 (H_mean) years cover the frozen hindcast 1934-2023
panel = read_csv(EDW / 'data' / 'annual_panel.csv')
h_years = sorted(int(r['year']) for r in panel if r['H_mean'])
check('J-17 H_mean years cover 1934-2023 (90 years)',
      h_years[0] <= 1934 and h_years[-1] >= 2023
      and sum(1 for y in h_years if 1934 <= y <= 2023) == 90,
      f'{h_years[0]}-{h_years[-1]}')

# 2. ladder set in rolling summary
rs = read_csv(EDW / 'results' / 'rolling_summary.csv')
models = {r['model'] for r in rs}
frozen_ladder = {'naive_persist', 'naive_mean', 'M1', 'M2', 'M2m', 'M3',
                 'M4', 'M2_oracle'}
check('ladder = frozen protocol set', models == frozen_ladder,
      str(sorted(models)))

# 3. recompute rolling scores from per-observation forecasts
rf = read_csv(EDW / 'results' / 'rolling_forecasts.csv')
rec = recompute(rf, ('model', 'horizon'))
bad = []
for r in rs:
    k = (r['model'], int(r['horizon']))
    if k not in rec:
        bad.append(f'{k} missing from forecasts')
        continue
    n, rmse, mae = rec[k]
    if int(r['n']) != n or not close(float(r['rmse']), rmse) \
            or not close(float(r['mae']), mae):
        bad.append(f'{k}: summary ({r["n"]}, {float(r["rmse"]):.6f}) vs '
                   f'recomputed ({n}, {rmse:.6f})')
check('rolling scores recomputed from forecasts', not bad,
      f'{len(rs)} rows checked' + ('; ' + '; '.join(bad[:3]) if bad else ''))

# 4. rolling-origin counts: min 15 training years, panel 1934-2023
n_h1 = rec.get(('naive_persist', 1), (None,))[0]
n_h5 = rec.get(('naive_persist', 5), (None,))[0]
check('rolling counts h=1: 75 origins', n_h1 == 75, f'n={n_h1}')
check('rolling counts h=5: 71 origins', n_h5 == 71, f'n={n_h5}')

# 5. fixed windows: the four frozen windows with frozen train/test ranges
fw = read_csv(EDW / 'results' / 'fixed_window_scores.csv')
frozen_windows = {
    'dor_drawdown': ('1934-1950', '1951-1956', 6),
    'dor_recovery': ('1934-1956', '1957-1961', 5),
    'prepermit_wet': ('1980-1990', '1991-1995', 5),
    'cpm_era': ('1997-2014', '2015-2023', 9),
}
ok_w, det = True, []
for w, (tr, te, n) in frozen_windows.items():
    rows = [r for r in fw if r['window'] == w]
    if not rows:
        ok_w = False
        det.append(f'{w} missing')
        continue
    if any(r['train'] != tr or r['test'] != te or int(r['n']) != n
           for r in rows):
        ok_w = False
        det.append(f'{w}: {rows[0]["train"]}/{rows[0]["test"]}/{rows[0]["n"]}')
check('four frozen fixed windows with frozen ranges', ok_w,
      '; '.join(det) if det else 'all four windows match')

# 6. retention rule (point rule) application
by = {(r['model'], int(r['horizon'])): float(r['rmse']) for r in rs}
persist_h1 = by[('naive_persist', 1)]
m1_h1 = by[('M1', 1)]
m2_h1 = by[('M2', 1)]
m2m_h1 = by[('M2m', 1)]
m2m_h5 = by[('M2m', 5)]
persist_h5 = by[('naive_persist', 5)]
oracle_h1 = by[('M2_oracle', 1)]
check('persist h=1 = 13.23 (manuscript claim)', close(persist_h1, 13.23, 1e-3),
      f'{persist_h1:.4f}')
check('M1 h=1 = 12.84 (thin edge recorded)', close(m1_h1, 12.84, 1e-3),
      f'{m1_h1:.4f}')
check('M2 (causal stock-flow) h=1 worse than persist',
      m2_h1 > persist_h1, f'{m2_h1:.4f} > {persist_h1:.4f}')
check('M2m listed by point rule (beats persist at h=1 and h=5)',
      m2m_h1 < persist_h1 and m2m_h5 < persist_h5,
      f'{m2m_h1:.4f} < {persist_h1:.4f}; {m2m_h5:.4f} < {persist_h5:.4f}')
check('oracle M2 = 7.55 diagnostic certificate',
      close(oracle_h1, 7.55, 1e-3), f'{oracle_h1:.4f}')

# 7. pass-2 retention bookkeeping: listed vs retained-as-structure split
p2m = json.loads((EDW / 'results' / 'pass2_meta.json').read_text())
ret = p2m['retention']
check('pass2 listed_by_point_rule nonempty, retained_as_structure empty',
      ret['listed_by_point_rule'] and not ret['retained_as_structure'],
      f'listed={ret["listed_by_point_rule"]}, '
      f'retained={ret["retained_as_structure"]}')
check('pass2 persist/M1 anchors match pass-1 summary',
      close(ret['persist_h1'], persist_h1) and close(ret['M1_h1'], m1_h1))

# 8. Brier-660 modern subsample exists (origins >= 2007 interpretation)
mod = read_csv(EDW / 'results' / 'rolling_modern_2007.csv')
check('rolling_modern_2007 (Brier interpretation subset) present',
      len(mod) > 0, f'{len(mod)} rows')

print('== Cod (Omega_2016 + Omega_xte): manuscript-declared specification ==')

# 0. freeze-discipline caveat: no pre-score protocol file in this tree
check('NO pre-score protocol file in cod tree (honest caveat recorded)',
      not (COD / 'protocol.md').exists())
notes.append('cod tree freeze discipline: manuscript-declared spec '
             '(manuscript section 2 + results/meta.json), no dated '
             'pre-score protocol file — weaker than the Edwards lock; '
             'recorded as a caveat, not a failure.')

# 1. series lock in meta.json
meta = json.loads((COD / 'results' / 'meta.json').read_text())
check('meta series lock: NCAM M-shift SSB 1983-2015',
      meta['year_min'] == 1983 and meta['year_max'] == 2015
      and meta['n_years'] == 33 and 'NCAM' in meta['series'],
      meta['series'])
check('meta LRP = 884.58 kt (1983-1989 mean)',
      close(meta['lrp_1980s_mean_kt'], 884.58, 1e-6),
      f'{meta["lrp_1980s_mean_kt"]:.2f}')

# 2. ladder set (manuscript set + recorded pass-2 extension M2_survey_start)
crs = read_csv(COD / 'results' / 'rolling_summary.csv')
cod_models = {r['model'] for r in crs}
frozen_cod = {'naive_persist', 'naive_train_mean', 'M1_autonomous_Schaefer',
              'M1b_autonomous_Allee', 'M2_stockflow_regimeC',
              'M3_AR_residual', 'M4_delayed_info', 'M2_survey_start'}
check('cod ladder = manuscript set + recorded pass-2 survey-start extension',
      cod_models == frozen_cod, str(sorted(cod_models)))

# 3. recompute rolling scores for the ANNUAL treatment from the
#    per-observation forecasts (the committed per-observation artifact);
#    M2_survey_start is stored in its own pass-2 artifact file
crf = read_csv(COD / 'results' / 'rolling_forecasts.csv')
rec_c = recompute(crf, ('model', 'horizon'))
bad = []
for r in crs:
    if r['catch'] != 'annual' or r['model'] == 'M2_survey_start':
        continue
    k = (r['model'], int(r['horizon']))
    if k not in rec_c:
        bad.append(f'{k} missing')
        continue
    n, rmse, mae = rec_c[k]
    if int(r['n']) != n or not close(float(r['rmse']), rmse) \
            or not close(float(r['mae']), mae):
        bad.append(f'{k}: ({r["n"]},{float(r["rmse"]):.4f}) vs '
                   f'({n},{rmse:.4f})')
check('cod rolling scores recomputed from forecasts (annual treatment)',
      not bad, f'{sum(1 for r in crs if r["catch"] == "annual" and r["model"] != "M2_survey_start")} rows'
      + ('; ' + '; '.join(bad[:3]) if bad else ''))
ssf = read_csv(COD / 'results' / 'survey_start_forecasts.csv')
rec_ss = recompute(ssf, ('model', 'horizon'))
bad_ss = []
for r in crs:
    if r['model'] != 'M2_survey_start':
        continue
    k = (r['model'], int(r['horizon']))
    n, rmse, mae = rec_ss.get(k, (None, None, None))
    if n != int(r['n']) or not close(float(r['rmse']), rmse):
        bad_ss.append(f'{k}')
check('M2_survey_start recomputed from its own pass-2 artifact',
      not bad_ss and len(rec_ss) == 2,
      f'{len(ssf)} rows' + ('; ' + '; '.join(bad_ss) if bad_ss else ''))
notes.append('cod regime-catch treatment: summary-level rows present and '
             'range-consistent; per-observation artifact committed for the '
             'annual (Schijns) treatment only — recorded coverage '
             'limitation, summary-level match for the regime rows.')

# 3b. regime rows present with consistent n counts
regime_rows = [r for r in crs if r['catch'] == 'regime']
ok_r = all(
    (int(r['horizon']) == 1 and int(r['n']) == 25)
    or (int(r['horizon']) == 5 and int(r['n']) == 21)
    for r in regime_rows)
check('cod regime-treatment rows present (summary level), n=25/21',
      len(regime_rows) >= 10 and ok_r,
      f'{len(regime_rows)} rows')

# 3c. naive baselines recomputed from the raw committed series
#     (origins = the n most recent eligible, matching the summaries)
ncam = series_map(COD / 'data' / 'ncam_2016_table_a2.csv', 'year', 'ssb_kt')
np1 = naive_rmse(ncam, last_n_origins(ncam, 1, int(
    [r for r in crs if r['catch'] == 'na' and r['model'] == 'naive_persist'
     and r['horizon'] == '1'][0]['n'])), 1)
np5 = naive_rmse(ncam, last_n_origins(ncam, 5, int(
    [r for r in crs if r['catch'] == 'na' and r['model'] == 'naive_persist'
     and r['horizon'] == '5'][0]['n'])), 5)
cby = {(r['catch'], r['model'], int(r['horizon'])): float(r['rmse'])
       for r in crs}
check('naive_persist h=1 recomputed from raw NCAM series = summary',
      close(np1, cby[('na', 'naive_persist', 1)]),
      f'{np1:.4f} vs {cby[("na", "naive_persist", 1)]:.4f}')
check('naive_persist h=5 recomputed from raw NCAM series = summary',
      close(np5, cby[('na', 'naive_persist', 5)]),
      f'{np5:.4f} vs {cby[("na", "naive_persist", 5)]:.4f}')

# 4. headline retention claims (Omega_2016)
persist_1 = cby[('na', 'naive_persist', 1)]
persist_5 = cby[('na', 'naive_persist', 5)]
ladder_h1 = [v for k, v in cby.items()
             if k[0] in ('regime', 'annual') and k[2] == 1
             and k[1].startswith(('M1', 'M2', 'M3', 'M4'))]
check('persist h=1 = 98 kt (manuscript claim)',
      close(persist_1, 98.0, 1e-3), f'{persist_1:.2f}')
check('persist h=5 = 265 kt (manuscript claim)',
      close(persist_5, 265.0, 1e-2), f'{persist_5:.2f}')
check('no ladder model beats persist at h=1 (negative certificate)',
      all(v > persist_1 for v in ladder_h1),
      f'ladder min {min(ladder_h1):.1f} vs persist {persist_1:.1f}; '
      f'range {min(ladder_h1):.0f}-{max(ladder_h1):.0f} (manuscript: '
      f'115-206 kt)')

# 5. fixed windows (collapse / recovery) with frozen ranges
cfw = read_csv(COD / 'results' / 'fixed_window_scores.csv')
coll = [r for r in cfw if r['window'] == 'collapse'
        and r['catch'] == 'regime']
rec_ = [r for r in cfw if r['window'] == 'recovery'
        and r['catch'] == 'regime']
check('collapse window 1983-1990 / 1991-1995',
      bool(coll) and all(r['train'] == '1983-1990'
                         and r['test'] == '1991-1995'
                         and int(r['n']) == 5 for r in coll))
check('recovery window 1995-2007 / 2008-2015',
      bool(rec_) and all(r['train'] == '1995-2007'
                         and r['test'] == '2008-2015'
                         and int(r['n']) == 8 for r in rec_))
coll_rmse = [float(r['rmse']) for r in coll]
check('collapse window missed by every model (694-819 kt)',
      all(690.0 < v < 820.0 for v in coll_rmse),
      f'{min(coll_rmse):.0f}-{max(coll_rmse):.0f}')

# 6. Omega_xte: second, unpooled specification
xrs = read_csv(COD / 'results' / 'xte_rolling_summary.csv')
xrf = read_csv(COD / 'results' / 'xte_rolling_forecasts.csv')
rec_x = recompute(xrf, ('model', 'horizon'))
bad = []
for r in xrs:
    if r['model'].startswith('naive'):
        continue
    k = (r['model'], int(r['horizon']))
    if k not in rec_x:
        bad.append(f'{k} missing')
        continue
    n, rmse, mae = rec_x[k]
    if int(r['n']) != n or not close(float(r['rmse']), rmse):
        bad.append(f'{k}')
check('xte rolling scores recomputed (ladder models)', not bad,
      f'{len(xrs)} rows' + ('; ' + '; '.join(bad[:3]) if bad else ''))
xby = {(r['model'], int(r['horizon'])): float(r['rmse']) for r in xrs}
xte_series = series_map(COD / 'data' / 'xtencam_table17_ssb.csv',
                        'year', 'ssb_kt')
xnp1 = naive_rmse(xte_series, last_n_origins(
    xte_series, 1, int([r for r in xrs if r['model'] == 'naive_persist'
                        and r['horizon'] == '1'][0]['n'])), 1)
check('xte naive_persist recomputed from raw xteNCAM series',
      close(xnp1, xby[('naive_persist', 1)]),
      f'{xnp1:.2f} vs {xby[("naive_persist", 1)]:.2f}')
check('xte persist h=1 = 88 kt vs M1 120 (manuscript claim)',
      close(xby[('naive_persist', 1)], 88.0, 1e-2)
      and close(xby[('M1_autonomous_Schaefer', 1)], 120.0, 1e-2),
      f'persist {xby[("naive_persist", 1)]:.1f} vs '
      f'M1 {xby[("M1_autonomous_Schaefer", 1)]:.1f}')

# 7. the two specifications are not pooled: distinct series over shared
#    calendar years — obs values differ on the same origin years
o1_obs = {int(r['origin']): float(r['obs']) for r in crf
          if int(r['horizon']) == 1}
ox_obs = {int(r['origin']): float(r['obs']) for r in xrf
          if int(r['horizon']) == 1}
shared = sorted(set(o1_obs) & set(ox_obs))
diff = [y for y in shared if not close(o1_obs[y], ox_obs[y], 1e-6)]
check('Omega_2016 and Omega_xte obs series distinct on shared origins '
      '(not pooled)', shared and len(diff) >= len(shared) - 1,
      f'{len(shared)} shared origins, {len(diff)} differing obs values')
check('xte obs match the committed xteNCAM series file',
      all(close(ox_obs[o], xte_series[o + 1], 1e-9) for o in ox_obs))

print()
print(f'TOTAL: {passes} passed, {len(failures)} failed')
for n in notes:
    print('NOTE:', n)
if failures:
    print('FAILURES:', failures)
    sys.exit(1)
print('WAVE E SPEC MATCH: all machine checks passed.')
