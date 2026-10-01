#!/usr/bin/env python3
"""Read-only independent checks on source-matched E1 result archives and live/source text."""
import csv
from pathlib import Path
p=Path(__file__).resolve().parent
rows=lambda f:list(csv.DictReader((p/f).open(newline='',encoding='utf-8')))
A=rows('rolling_summary.csv');B=rows('xte_rolling_summary.csv')
for catch in ('regime','annual'):
 for h in (1,5):
  baseline=next(float(r['rmse']) for r in A if r['model']=='naive_persist' and int(r['horizon'])==h)
  structural=[float(r['rmse']) for r in A if r['catch']==catch and r['model'].startswith('M') and int(r['horizon'])==h]
  assert len(structural)>=5 and all(s>baseline for s in structural)
for h in (1,5):
 baseline=next(float(r['rmse']) for r in B if r['model']=='naive_persist' and int(r['horizon'])==h)
 structural=[float(r['rmse']) for r in B if r['model'].startswith('M') and int(r['horizon'])==h]
 assert len(structural)>=5 and all(s>baseline for s in structural)
print('archived cod result summaries: all scored structural M rows lose to persistence at h=1,5 on both unpooled specifications (but E1 v60 verifier does not independently recompute these files)')

R=rows('sim_retention_power.csv')
for dgp,truth,expect in [('D1_M1_collapse','M1_autonomous_Schaefer',(.965,.985)),('D3_M2_stockflow','M2_stockflow_regimeC',(.09,.11)),('D4_M1b_depens','M1b_autonomous_Allee',(.005,.015))]:
 for sigma,target in zip(('11.8','33.8'),expect):
  subset=[r for r in R if r['dgp']==dgp and r['module']==truth and r['sigma']==sigma]
  assert len(subset)==200 and sum(r['retained']=='True' for r in subset)/200==target
print('archived simulation rows: exact 200-replicate power cells D1=(.965,.985), D3=(.09,.11), D4=(.005,.015)')

live=Path('/home/user/papers/paper11_forecasting_baselines_v64.tex').read_text()
src=Path('/home/user/family/e1_v60.tex').read_text()
for text in ('the tie band\nand the comparator declarations are completions recorded after the\nscores', 'M1 on the observed'):
 assert text in live
assert 'Here nothing is selected from the scores at all' in live
assert 'Romano, J.P. and Wolf, M., 2005.' in live and 'Pella and\nRomano' in live
assert 'Pella and\nTomlinson, 1969)' in src
assert '12.84 \\textless{} 13.23' in live and '12.28 \\textless{} 13.23' in live
print('live merger contradictions: tie-band/comparators disclosed post-score vs fully pre-score; Pella-and-Tomlinson split by citation; aquifer M1 and M2m each beat persistence at h=1')
