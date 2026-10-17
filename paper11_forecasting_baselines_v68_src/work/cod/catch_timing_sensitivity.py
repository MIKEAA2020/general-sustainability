"""Sensitivity of the rolling-origin scores to the catch-timing convention.
Registered runner: estimation pairs S_t -> S_{t+1} with C_t; forecasting applies C_{t+1}.
Here the forecast path uses C_t (consistent with estimation). M1/M1b are unaffected (constant catch)."""
import numpy as np, pandas as pd, sys
import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
# repo root: set GS_REPO, or rely on the standard location  <repo>/arena agent 1/paper rewrites/latex/paperE1_cod_forecast_ladder_v69_src/work/
_REPO = _os.environ.get('GS_REPO', _os.path.abspath(_os.path.join(_HERE, '..', '..', '..', '..', '..')))
sys.path.insert(0,_os.path.join(_HERE,'rerun','src')); import run_ladder as rl, run_xte as rx
def roll(years, ssb, C, min_train, consistent):
    rows=[]; n=len(years)
    for origin in range(min_train-1, n-1):
        tr=np.zeros(n,bool); tr[:origin+1]=True
        for spec in rl.SPECS:
            if spec.name.startswith('M1'): continue
            C_all=rl.catch_for_model(years, C, tr, spec.use_regime_C)
            p=rl.fit_params(ssb[tr], C_all[tr], allee=spec.allee)
            start=max(origin-spec.delay,0); S0=ssb[start]; i_tr=np.where(tr)[0]; last=0.0
            if spec.use_ar:
                fitted=np.array([rl.surplus(ssb[j],p['r'],p['K'],p['s_allee'])-C_all[j] for j in i_tr[:-1]]); last=(np.diff(ssb[i_tr])-fitted)[-1]
            for h in (1,5):
                if origin+h>=n: continue
                C_path = C_all[start:origin+h] if consistent else C_all[start+1:origin+h+1]
                yhat=float(rl.forecast_path(S0,C_path,p,spec.use_ar,last)[-1]); y=float(ssb[origin+h])
                rows.append(dict(origin=int(years[origin]),horizon=h,model=spec.name,pred=yhat,obs=y,sqerr=(yhat-y)**2))
    return pd.DataFrame(rows)
out=[]
years, ssb, c_reg, c_ann, idx, lrp = rl.load()
for tag,C,mt in (('A coarse',c_reg,8),('A annual',c_ann,8)):
    for cons in (False,True):
        d=roll(years,ssb,C,mt,cons)
        for (m,h),g in d.groupby(['model','horizon']):
            out.append(dict(spec=tag,convention='C_t (consistent)' if cons else 'C_{t+1} (registered)',model=m.split('_')[0],h=h,n=len(g),rmse=np.sqrt(g.sqerr.mean())))
yB, sB, CB = rx.load_xte()
for cons in (False,True):
    d=roll(yB,sB,CB,12,cons)
    for (m,h),g in d.groupby(['model','horizon']):
        out.append(dict(spec='B',convention='C_t (consistent)' if cons else 'C_{t+1} (registered)',model=m.split('_')[0],h=h,n=len(g),rmse=np.sqrt(g.sqerr.mean())))
R=pd.DataFrame(out); P=R.pivot_table(index=['spec','model','h'],columns='convention',values='rmse').round(1); print(P.to_string()); R.to_csv('catch_timing_sensitivity.csv',index=False)
