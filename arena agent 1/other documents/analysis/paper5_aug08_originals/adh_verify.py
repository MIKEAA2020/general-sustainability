#!/usr/bin/env python3
"""ADH cross-system analysis: verify + independently re-execute (paper 5).

ADH (reverse-engineered from the deposited tables, verified below) is
buffer-years: ADH = max(0, ln(SSB/B_lim)/F) — log stock-status over fishing
mortality. Prior work (broader_results.json) compared the archived-43 cohort
against broader RAM pools. This script:
  GATE 1: recompute ADH from (SSB, F, B_lim) for fisheries_adh.csv (43) and
          v466_broader_cohort.csv (454) — must match deposited ADH columns.
  GATE 2: reproduce broader_results.json descriptives (overall + per-group
          n/zeros/medians/max/quartiles; archived43; zero fractions;
          vintage counterfactual on the 33-stock overlap).
  EXTENSION (independent re-execution): random-draw medians (m=43) from the
          broad-454 and forage-64 pools with a NEW seed — compare
          pct-below-archived-median against the record (2.12 / 0.29).

Outputs: adh_verify.log
"""
import csv, json, math, sys
import numpy as np

LOG = open('/home/user/_openitems/adh_verify.log', 'w')
def log(*a):
    line = ' '.join(str(x) for x in a)
    print(line, flush=True); LOG.write(line + '\n')

def adh(ssb, f, blim):
    if f is None or f <= 0 or ssb is None or blim is None or ssb <= 0 or blim <= 0:
        return None
    return max(0.0, math.log(ssb/blim)/f)

arch = list(csv.DictReader(open('/home/user/_openitems/xsys/fisheries_adh.csv')))
v466 = list(csv.DictReader(open('/home/user/_openitems/xsys/v466_broader_cohort.csv')))
v444 = {r['stockid']: r for r in csv.DictReader(open('/home/user/_openitems/xsys/v444_adh_cohort.csv'))}
br = json.load(open('/home/user/_openitems/xsys/broader_results.json'))
ov = json.load(open('/home/user/_openitems/xsys/overlap.json'))
log(f"rows: arch={len(arch)} v466={len(v466)} v444={len(v444)} overlap33={ov['n_in_both']}")

print('=== GATE 1: ADH formula ===', flush=True)
log('=== GATE 1: ADH formula ===')
d1 = max(abs(adh(float(r['SSB']), float(r['F']), float(r['B_lim'])) - float(r['ADH_yr'])) for r in arch)
d2 = max(abs(adh(float(r['SSB_now']), float(r['F_now']), float(r['B_lim'])) - float(r['ADH'])) for r in v466)
log(f'max |recomputed - deposited| ADH: arch43={d1:.2e}, v466={d2:.2e} (tol 1e-3; inputs rounded)')
assert d1 < 1e-3 and d2 < 1e-3, 'GATE 1 FAILED'
log('GATE 1 PASSED: ADH = max(0, ln(SSB/B_lim)/F).')

print('=== GATE 2: descriptives ===', flush=True)
log('=== GATE 2: descriptives ===')
def desc(v):
    v = np.array(v)
    pos = v[v > 0]
    return dict(n=len(v), zeros=int(np.sum(v == 0)), median_incl=float(np.median(v)),
                median_pos=float(np.median(pos)), max=float(np.max(v)),
                q25=float(np.percentile(v, 25)), q75=float(np.percentile(v, 75)))
A = [float(r['ADH_yr']) for r in arch]
B = [float(r['ADH']) for r in v466]
ok = True
for nm, v, rec in (('v466_overall', B, br['v466_overall']), ('archived43', A, br['archived43'])):
    mine = desc(v)
    bad = [k for k in mine if abs(mine[k]-rec[k]) > max(1e-3, 1e-6*abs(rec[k]))]
    ok &= not bad
    log(f"  {nm}: {'OK' if not bad else 'DIFF '+str(bad)} (median_incl mine={mine['median_incl']:.4f} record={rec['median_incl']})")
groups = {}
for r in v466:
    groups.setdefault(r['taxGroup'], []).append(float(r['ADH']))
for g, v in sorted(groups.items()):
    mine = desc(v); rec = br[f'v466_{g}']
    bad = [k for k in mine if abs(mine[k]-rec[k]) > max(1e-3, 1e-6*abs(rec[k]))]
    ok &= not bad
    if bad: log(f'  group {g}: DIFF {bad}')
log(f'  groups: all match' if ok else '  groups: MISMATCH')
zf = {'archived43': sum(1 for v in A if v == 0)/len(A),
      'v466_broad': sum(1 for v in B if v == 0)/len(B),
      'v466_forage': sum(1 for v in groups['forage fish'] if v == 0)/len(groups['forage fish'])}
for k, v in zf.items():
    match = abs(v-br['zero_fractions'][k]) < 1e-3
    ok &= match
    log(f'  zero_fraction {k}: mine={v:.4f} record={br["zero_fractions"][k]} {"OK" if match else "DIFF"}')
both = ov['in_both']
v466map = {r['stockid']: float(r['ADH']) for r in v466}
av = [float([r for r in arch if r['stock'] == s][0]['ADH_yr']) for s in both]
cv = [v466map[s] for s in both]  # 'current' side is v466 (verified against record)
vc = br['vintage_counterfactual_33']
chk = (abs(np.median(av)-vc['archived_median_33']) < 1e-3 and abs(np.median(cv)-vc['current_median_33']) < 1e-3
       and sum(1 for v in av if v == 0) == vc['archived_zeros_33'] and sum(1 for v in cv if v == 0) == vc['current_zeros_33'])
ok &= chk
log(f"  vintage33: arch_med mine={np.median(av):.4f} record={vc['archived_median_33']}; v466_med mine={np.median(cv):.4f} record={vc['current_median_33']}; zeros match={chk}")
pair = sorted(set(v444) & set(v466map))
rev = np.array([abs(float(v444[s]['ADH'])-v466map[s]) for s in pair])
log(f'  EXTRA vintage drift v444->v466: {len(pair)} paired stocks, median |dADH|={np.median(rev):.4f}')
assert ok, 'GATE 2 FAILED'
log('GATE 2 PASSED: all descriptives reproduced.')

print('=== EXTENSION: independent random-draw re-execution (new seed) ===', flush=True)
log('=== EXTENSION: independent random-draw re-execution (new seed) ===')
rng = np.random.default_rng(11)
arch_med = float(np.median(A))
for nm, pool in (('broad454', B), ('forage64', groups['forage fish'])):
    pool = np.array(pool)
    meds = np.array([np.median(rng.choice(pool, size=43, replace=False)) for _ in range(20000)])
    rec = br['random_draw'][nm]
    pct = 100*np.mean(meds < arch_med)
    log(f'{nm}: pool={len(pool)} draws=20000 seed=11: draw_median_mean={meds.mean():.4f} (record {rec["draw_median_mean"]}); '
        f'p2.5/p50/p97.5={np.percentile(meds,2.5):.4f}/{np.percentile(meds,50):.4f}/{np.percentile(meds,97.5):.4f} '
        f'(record {rec["p2_5"]}/{rec["p50"]}/{rec["p97_5"]}); pct_below_archmed={pct:.2f} (record {rec["pct_draws_below_1.7902"]})')
log('DONE')
LOG.close()
