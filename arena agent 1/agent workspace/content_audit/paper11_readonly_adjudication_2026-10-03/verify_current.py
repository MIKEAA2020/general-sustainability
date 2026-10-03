#!/usr/bin/env python3
"""Read-only spot checks on current Paper 11/11c against deposited output rows.
This does NOT refit models, replay simulations, prove a theorem, or provide an external review.
Run from any cwd: python3 content_audit/paper11_readonly_adjudication_2026-10-03/verify_current.py
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
from collections import defaultdict
import csv, hashlib, math, re
ROOT = Path(__file__).resolve().parents[2]
main = ROOT/'paper 2 family/11_forecasting_baselines/paper11_forecasting_baselines_v66.tex'
worked = ROOT/'paper 2 family/11c_worked_systems/paper11c_worked_systems_audit_v4.tex'
for f in (main,worked,ROOT/'paper 2 family/11_forecasting_baselines/paper11_forecasting_baselines_v66.pdf',ROOT/'paper 2 family/11c_worked_systems/paper11c_worked_systems_audit_v4.pdf',ROOT/'paper 2 family/11_forecasting_baselines/paper11_forecasting_baselines_v66_SI.md'):
    print('SHA256', f.relative_to(ROOT), hashlib.sha256(f.read_bytes()).hexdigest())
text=main.read_text(); wtext=worked.read_text()
prior=(ROOT/'content_audit/scientific_validity/ws/paper2_worked_systems_v17.tex').read_text()
def tabular_after_label(s,label):
    anchor=s.find('\\label{'+label+'}')
    assert anchor>=0
    start=s.find('\\begin{tabular}',anchor)
    end=s.find('\\end{tabular}',start)+len('\\end{tabular}')
    assert start>=0 and end>start
    return re.sub(r'\s+','',s[start:end])
for label in ('tab:master','tab:laws','tab:timing','tab:census','tab:bench','tab:drift'):
    assert tabular_after_label(wtext,label)==tabular_after_label(prior,label)
    print('WS_CURRENT_TABLE_IDENTICAL_TO_TESTED_V17',label)
# Re-score stored predictions, not model fitting or independent field validation.
rows=list(csv.DictReader((ROOT/'comp/wave_e_edwards/results/rolling_forecasts.csv').open()))
scores=defaultdict(list)
for r in rows:
    h=int(r['horizon']); model=r['model']; pred=float(r['pred']); obs=float(r['obs']); loss=float(r['sqerr'])
    assert math.isclose(loss,(pred-obs)**2,rel_tol=1e-10,abs_tol=1e-8)
    scores[model,h].append(loss)
summary={(r['model'],int(r['horizon'])):(int(r['n']),float(r['rmse'])) for r in csv.DictReader((ROOT/'comp/wave_e_edwards/results/rolling_summary.csv').open())}
for model,h in [('naive_persist',1),('M1',1),('M2',1),('M2m',1),('naive_mean',5),('naive_persist',5),('M2m',5)]:
    loss=scores[model,h]; n,rmse=summary[model,h]; check=math.sqrt(sum(loss)/len(loss))
    assert n==len(loss) and math.isclose(check,rmse,rel_tol=1e-12)
    print('EDWARDS_ARCHIVED_ROWS',model,h,n,'RMSE',round(check,5))
assert summary['M2m',1][1]<summary['M1',1][1]<summary['naive_persist',1][1]<summary['M2',1][1]
assert summary['naive_mean',5][1]<summary['naive_persist',5][1]
assert '12.28 ft but is declined by its protocol class clause' in text
assert 'M2m satisfies (H1) and (H2) at h = 1' in text
assert 'pre-registered simulation' in text and 'completed after scores' in text
# The historical cod archive has summaries, not original refit replay in this spot check.
for file in ('rolling_summary.csv','xte_rolling_summary.csv'):
    R=list(csv.DictReader((ROOT/'content_audit/scientific_validity/e1'/file).open()))
    for h in (1,5):
        baseline=next(float(r['rmse']) for r in R if r['model']=='naive_persist' and int(r['horizon'])==h)
        structural=[float(r['rmse']) for r in R if r['model'].startswith('M') and int(r['horizon'])==h]
        assert structural and min(structural)>baseline
        print('COD_ARCHIVED_SUMMARY',file,h,'persistence',round(baseline,4),'min_structural',round(min(structural),4))
R=list(csv.DictReader((ROOT/'content_audit/scientific_validity/e1/sim_retention_power.csv').open()))
for name,model in [('D1_M1_collapse','M1_autonomous_Schaefer'),('D3_M2_stockflow','M2_stockflow_regimeC'),('D4_M1b_depens','M1b_autonomous_Allee')]:
    for sigma in ('11.8','33.8'):
        S=[r for r in R if r['dgp']==name and r['module']==model and r['sigma']==sigma]
        assert len(S)==200
        print('COD_ARCHIVED_POWER',name,sigma,sum(r['retained']=='True' for r in S),len(S))
# Arithmetic reconstructed independently from current 11c definitions.
cap1=lambda y:Q(3,2)-(Q(y)-2)/10
cap2=lambda y:Q(59,50)-(Q(y)-2)/10
assert (cap1(Q(27,5)),cap2(Q(27,5)))==(Q(29,25),Q(21,25))
assert cap1(6)+cap2(6)==Q(47,25)
assert (2-cap1(6)-cap2(6))/2==Q(3,50)
assert Q(6,5)<=cap1(5) and Q(4,5)<=cap2(5)
print('WS_INDEPENDENT_BENCHMARK','critical 27/5 feasible','Y6 margin 3/50','Y5 witness 6/5+4/5')
viable=real_strict_loss=floor_strict_loss=0
for i,T in product(range(10,41),(1,2,3)):
    tau=Q(i,10)-1; sigma=tau.numerator//tau.denominator
    ok=T<=tau
    viable+=ok; real_strict_loss+=ok and not T<tau; floor_strict_loss+=ok and not T<sigma
assert (viable,real_strict_loss,floor_strict_loss)==(33,3,21)
assert '21 of the 33 viable cells' in wtext
print('WS_INDEPENDENT_TIMING',93,viable,real_strict_loss,floor_strict_loss)
print('OK: limited, scoped checks only')
