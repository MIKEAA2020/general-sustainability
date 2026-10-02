#!/usr/bin/env python3
"""Finite ensemble obstruction and held-out time-series conformal diagnostic.
No exchangeability, uniform-path coverage, or physical-model coverage is asserted.
"""
from pathlib import Path
import csv,math,json,sys
import numpy as np
R=Path('/home/user');OUT=R/'content_audit/revision_pair_cod_2026-10-02'
rows=list(csv.DictReader(open(R/'comp/wave_e_cod/src/results_ident_v3/e2_bootstrap_joint.csv')))
assert len(rows)==2000
lrp=884.6; lrp2=2*lrp
cases={}
for key,subset in [('all',rows),('K_ge_LRP',[z for z in rows if float(z['K'])>=lrp]),('K_ge_2LRP',[z for z in rows if float(z['K'])>=lrp2])]:
 vals=np.array([float(z['Cstar']) for z in subset])
 cases[key]={'n':len(vals),'min_Cstar':float(vals.min()),'nonpositive':int((vals<=0).sum()),'BAU_5kt_positive_budget_count':int((vals>=5).sum()),'worst_r_K_Cstar':{t:float(min(subset,key=lambda z:float(z['Cstar']))[t]) for t in ('r','K','Cstar')}}
assert cases['all']['nonpositive']==387 and cases['K_ge_2LRP']['nonpositive']==83
sys.path.insert(0,str(R/'comp/wave_e_edwards/src'))
import run_intervention as ed
p=ed.load_panel();f=ed.fit_affine(p)
yr=p['year'].to_numpy();head=p['H_mean'].to_numpy(float);recharge=p['R_total'].to_numpy(float);pump=p['P_wells'].to_numpy(float)
errors=head[1:]-(f['a']*head[:-1]+f['alpha']+f['beta']*recharge[1:]+f['gamma']*pump[1:])
cal=np.abs(errors[(yr[1:]>=1991)&(yr[1:]<=2010)])
test=np.abs(errors[(yr[1:]>=2011)&(yr[1:]<=2023)])
assert len(cal)==20 and len(test)==13 and f['n_train_transitions']==56
# Standard split-conformal order statistic: if rank > n, threshold is +infinity.
def threshold(scores,alpha):
 n=len(scores);rank=math.ceil((n+1)*(1-alpha)-1e-14)
 return {'rank':rank,'n':n,'q':float(np.sort(scores)[rank-1]) if rank<=n else 'infinity'}
q95=threshold(cal,.05);q_simultaneous3=threshold(cal,.05/3)
result={'cod_fixed_floor_joint_refit_finite_ensemble':cases,'cod_ensemble_scope':'2,000 finite joint bootstrap refits with registered q10 floor held fixed; not an uncertainty confidence region; failure of uniform positivity is an explicit counterexample','edwards':{'fit_years':'1934-1990','calibration_years':'1991-2010','evaluation_years':'2011-2023','calibration_n':len(cal),'evaluation_n':len(test),'calibration_max_ft':float(cal.max()),'evaluation_max_ft':float(test.max()),'q95_two_sided_split_conformal_ft':q95,'evaluation_exceedances_at_q95':int((test>q95['q']).sum()) if isinstance(q95['q'],float) else None,'bonferroni_three_step_95pct_per_step_threshold_ft':q_simultaneous3,'assumption':'Finite-sample marginal coverage requires exchangeable calibration/future absolute errors for a model fit without calibration leakage. It is not justified under arbitrary temporal shift; Bonferroni joint coverage additionally needs each marginal bound, and neither result is a sure pathwise bound.'}}
(OUT/'ROBUST_SCOPE_DIAGNOSTIC.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
