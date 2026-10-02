#!/usr/bin/env python3
"""Edwards retrospective ACI, block-bootstrap OOB EnbPI-style diagnostic and eps kernels.
No guarantees of joint pathwise coverage or of forecasted future recharge/pumping inputs.
"""
from pathlib import Path
import json,math,sys,contextlib,io
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path('/home/user');O=R/'content_audit/revision_pair_cod_2026-10-02';sys.path.insert(0,str(R/'comp/wave_e_edwards/src'))
import run_intervention as ed
p=ed.load_panel();f=ed.fit_affine(p);pol=ed.make_policies(float(p[p['year']<=ed.TRAIN_END]['P_wells'].mean()))
yr=p['year'].to_numpy(int);H=p['H_mean'].to_numpy(float);rr=p['R_total'].to_numpy(float);P=p['P_wells'].to_numpy(float)
X=np.column_stack([np.ones(len(H)-1),rr[1:],P[1:],H[:-1]]);target=H[1:]
tr=(yr[1:]<=1990);oos=~tr;trainX=X[tr];trainY=target[tr];testX=X[oos];testY=target[oos];test_years=yr[1:][oos]
coef=np.linalg.lstsq(trainX,trainY,rcond=None)[0];assert len(trainY)==56 and len(testY)==33 and abs(coef[3]-f['a'])<1e-9
trscore=np.abs(trainY-trainX@coef);e=np.abs(testY-testX@coef)
assert abs(trscore.max()-f['train_residual_max'])<1e-8

def qconf(scores,alpha):
 n=len(scores)
 if alpha<=0:return math.inf
 if alpha>=1:return 0.
 k=math.ceil((n+1)*(1-alpha)-1e-12)
 return float(np.sort(scores)[k-1]) if k<=n else math.inf

def metrics(y,q,yr):
 misses=y>q; finite=np.isfinite(q)
 return {'n':int(len(y)),'covered':int((~misses).sum()),'coverage':float((~misses).mean()),'finite_widths':int(finite.sum()),'infinite_widths':int((~finite).sum()),'median_finite_radius_ft':float(np.median(q[finite])) if finite.any() else None,'max_finite_radius_ft':float(np.max(q[finite])) if finite.any() else None,'miss_years':yr[misses].tolist(),'joint_3yr_all_covered_windows':int(sum(not np.any(misses[i:i+3]) for i in range(len(misses)-2))),'joint_3yr_windows_total':int(len(misses)-2)}
# ACI uses a rolling historical score pool; gamma fixed before seeing OOS outcomes.
aci={};aci_curves={}
for gam in (.005,.01,.05,.1):
 pool=list(trscore);alpha=.05;qs=[];alphas=[]
 for score in e:
  alphap=alpha;radius=qconf(pool[-56:],alphap);qs.append(radius);alphas.append(alphap)
  alpha=alpha+gam*(.05-float(score>radius))
  pool.append(score)
 qa=np.asarray(qs);key=str(gam);aci[key]={'full':metrics(e,qa,test_years),'late_2011_2023':metrics(e[test_years>=2011],qa[test_years>=2011],test_years[test_years>=2011]),'alpha_range':[float(min(alphas)),float(max(alphas))]};aci_curves[key]=[None if not np.isfinite(q) else float(q) for q in qa]
# EnbPI-style: block-bootstrap OOB score construction, full ensemble predictions,
# then online sliding residual window. Finite-sample validity theorem requires
# additional weak-dependence/stability conditions and ex-ante predictor covariates.
B=300;block=5;n=len(trainY);rng=np.random.default_rng(20261002);predOOB=np.zeros(n);cnt=np.zeros(n);testpred=np.zeros(len(testY))
for _ in range(B):
 idx=np.concatenate([np.arange(st,st+block)%n for st in rng.integers(0,n,size=math.ceil(n/block))])[:n]
 co=np.linalg.lstsq(trainX[idx],trainY[idx],rcond=None)[0]
 testpred+=testX@co/B
 unused=np.setdiff1d(np.arange(n),np.unique(idx))
 predOOB[unused]+=trainX[unused]@co;cnt[unused]+=1
assert np.all(cnt>=20),cnt.min()
predOOB/=cnt;pool=list(np.abs(trainY-predOOB));enbscore=np.abs(testY-testpred);rad=[]
for score in enbscore:
 rad.append(qconf(pool[-n:],.05));pool.append(score)
rad=np.asarray(rad)
enbpi={'method':'symmetric, fixed-block bootstrap OOB model ensemble + online rolling score pool (EnbPI-style; not externally validated full EnbPI guarantee)','block':block,'B':B,'min_OOB_models':int(cnt.min()),'full':metrics(enbscore,rad,test_years),'late_2011_2023':metrics(enbscore[test_years>=2011],rad[test_years>=2011],test_years[test_years>=2011]),'note':'Retrospective annual R_total and P_wells enter the predictor; not available when issuing a prospective decision without independent forecasts. OOB residuals are not independent of serial data.'}
# Direct interval recursion from prior audited code: imported run reproduces existing
# results without changing the paper or reading uncalibrated coverage into eps.
sys.path.insert(0,str(O))
with contextlib.redirect_stdout(io.StringIO()):
 import audit09 as a
floor=float(p[p['year']<=ed.TRAIN_END]['R_total'].min())
# At K=618, UC-min, find largest eps with nonempty set at horizon T; binary search
# values are floating-point sensitivity outputs, not interval arithmetic.
def bound(eps,name,T):return a.bnd(a.robust(pol[name],floor,618.,eps,T))
names=['BAU','flat_90','S1','cpm'];hor=[1,2,3,4,5];thresholds={};curve=[]
for name in names:
 thresholds[name]={}
 for T in hor:
  if bound(0.,name,T) is None:critical=0.
  elif bound(30.,name,T) is not None:critical=None
  else:
   lo,hi=0.,30.
   for _ in range(50):
    mid=(lo+hi)/2
    if bound(mid,name,T) is not None:lo=mid
    else:hi=mid
   critical=lo
  thresholds[name][str(T)]=critical
 for eps in np.arange(0,30.0001,.5):curve.append({'policy':name,'horizon':3,'eps_ft':float(eps),'boundary_ft':bound(float(eps),name,3)})
for name in names:
 xs=[z['eps_ft'] for z in curve if z['policy']==name];ys=[z['boundary_ft'] if z['boundary_ft'] is not None else float('nan') for z in curve if z['policy']==name]
 plt.plot(xs,ys,label=name)
plt.xlabel('Assumed uniform additive defect $\\epsilon$ (ft)');plt.ylabel('3-year robust kernel lower edge (ft)');plt.title('Fitted Edwards map, UC-min recharge, safe head 618–710 ft');plt.ylim(615,712);plt.legend();plt.tight_layout();plt.savefig(O/'EDW_EPSILON_CURVE.png',dpi=180);plt.close()
import csv
with (O/'EDW_EPSILON_CURVE.csv').open('w',newline='') as ff:
 w=csv.DictWriter(ff,fieldnames=curve[0].keys());w.writeheader();w.writerows(curve)
result={'training':'1934-1990 fixed affine fit, 56 transitions','evaluation':'1991-2023 33 transitions, covariates realized (not prospective)','ACI':aci,'EnbPI_style':enbpi,'eps_recursion':{'assumptions':'fixed affine fit, registered policies, UC-min recharge and imposed bounded additive defect; eps is an assumed sure bound, not an ACI radius or a future guarantee','K_ft':618,'T3_critical_epsilon_ft':{k:v['3'] for k,v in thresholds.items()},'critical_epsilon_by_policy_horizon':thresholds},'limitations':'ACI long-run realized coverage is distinct from a finite-horizon simultaneous probability and from a uniform all-outcomes bound. EnbPI-style empirical results depend on block bootstrap, score stability and available covariates; no method establishes the future defect assumption.'}
(O/'EDW_ADAPTIVE_AND_EPSILON.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
