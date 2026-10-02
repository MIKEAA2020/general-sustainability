#!/usr/bin/env python3
"""Scoped text/value crosswalk for independently rerun xte sensitivity.
Only tests explicitly listed claims; remaining paper claims are not inferred.
"""
from pathlib import Path
import csv,re,sys,os
B=Path(os.environ.get('PAPER09_AUDIT_DIR','/home/user/content_audit/paper09_rerun'))
P=Path(os.environ.get('PAPER09_MAIN_TEX','/home/user/content_audit/claim_alignment/drafts/paper09_cod_certification_v32.tex'))
t=P.read_text()
start=t.index('\\subsubsection{3.11 Second specification');end=t.index('\\subsubsection{3.12 Is the reference point',start);s=t[start:end]
base=list(csv.DictReader((B/'review_candidates/e2_xteNCAM_summary_stable.csv').open()))[0]
rows={(r['class_'],r['policy']):r for r in csv.DictReader((B/'review_candidates/e2_xteNCAM_row_stable.csv').open())}
import json
precision=json.loads((B/'review_candidates/xte_margin_precision.json').read_text())
assert round(float(precision['analytic_fit']['Cstar_kt']),2)==float(base['constructive_own_q10'])
assert round(float(precision['analytic_fit']['Cstar_kt']),4)==7.4898
items=[]
def check(name,calc,text,part=s):
 status='match' if text in part else 'mismatch' if text else 'not-produced'
 items.append((name,calc,text,status))
# Python-executed values (not the manuscript) drive the expected display.
assert len(rows)==12 and base['K']=='4813.06' and base['constructive_own_q10']=='7.49'
check('fit r',base['r'],r'\(r = 0.5023\)')
check('fit K kt',base['K'],r'\(K = 4813.1\)')
check('source-year floor q10',base['e_q10'],r'\(|e_{q10}| = 123.2\)')
check('constructive margin before display rounding',precision['analytic_fit']['Cstar_kt'],r'\(7.4898\) kt before display rounding')
check('constructive margin table precision',base['constructive_own_q10'],r'\(7.49\) kt in Table 7')
check('source-year floor worst',base['e_min'],r'\(> 395.9\) kt')
for pol in ('flat_0','BAU'):
 assert all(round(float(rows[('own_q10',pol)][h]),2)==276 for h in ('T1','T5','Tinf'))
check('q10 zero/BAU all horizons',','.join(rows[('own_q10','flat_0')][h] for h in ('T1','T5','Tinf')),'lower\nboundaries are \\(276\\) kt at all three horizons.')
for policy,t1,tinf in [('flat_25','312.45','397.60'),('flat_50','354.35','546.20')]:
 x=rows[('own_q10',policy)];assert round(float(x['T1']),2)==float(t1) and round(float(x['Tinf']),2)==float(tinf)
 check('q10 '+policy+' T1',x['T1'],r'\('+t1+r'\) kt')
 check('q10 '+policy+' Tinf',x['Tinf'],r'\('+tinf+r'\)')
for policy,t1 in [('flat_0','462.10'),('flat_50','548.05')]:
 x=rows[('own_min',policy)];assert round(float(x['T1']),2)==float(t1)
 check('worst '+policy+' T1',x['T1'],r'\('+t1+r'\) kt')
assert round(float(rows[('own_q05','flat_0')]['T1']),2)==345
check('q05 zero one-step',rows[('own_q05','flat_0')]['T1'],r'\(345.00\) kt')
check('Table 7 source-year row',';'.join([base['constructive_own_q10'],rows[('own_q10','flat_0')]['T1'],rows[('own_q10','flat_0')]['Tinf']]),r'xteNCAM (this row) & 0.5023 & 4813.1 & 1.4447 & 7.49 & 276.0 & 276.0 \\')
check('cod conclusion source-year margin',precision['analytic_fit']['Cstar_kt'],'is only \\(7.4898\\) kt (\\(7.49\\) kt to two decimals)',t)
with (B/'xte_claim_crosswalk.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['claim','computed','manuscript_snippet','status']);w.writerows(items)
from collections import Counter
print('XTE_SOURCEYEAR_CROSSWALK',dict(Counter(x[-1] for x in items)),len(items),'explicit checks')
if any(x[-1]!='match' for x in items):
 for x in items:
  if x[-1]!='match':print('UNMATCHED',x[0],x[-1],x[2])
 sys.exit(1)
