"""Paired moving-block bootstrap of RMSE gaps (module minus persistence), as a
sensitivity to the registered layer, which resamples the two loss sequences
independently. Also band-level (period) margins. Seed 0, 20,000 replications."""
import numpy as np, pandas as pd, sys
NB=20000; SEED=0
import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
# repo root: set GS_REPO, or rely on the standard location  <repo>/arena agent 1/paper rewrites/latex/paperE1_cod_forecast_ladder_v69_src/work/
_REPO = _os.environ.get('GS_REPO', _os.path.abspath(_os.path.join(_HERE, '..', '..', '..', '..', '..')))
ROOT=_os.path.join(_HERE,'rerun')
MODELS=["M1_autonomous_Schaefer","M1b_autonomous_Allee","M2_stockflow_regimeC","M3_AR_residual","M4_delayed_info"]
def losses_for(spec):
    if spec=='A':
        df=pd.read_csv(_os.path.join(_REPO,'wave_e_cod','results','rolling_forecasts_regime.csv')); ser=pd.read_csv(f'{ROOT}/data/ncam_2016_table_a2.csv')
    else:
        df=pd.read_csv(f'{ROOT}/results/xte_rolling_forecasts.csv'); ser=pd.read_csv(f'{ROOT}/data/xtencam_table17_ssb.csv')
    S=dict(zip(ser.year,ser.ssb_kt)); out={}
    for h in (1,5):
        sub=df[df.horizon==h]; origins=sorted(sub.origin.unique())
        L={'persist':np.array([(S[o]-S[o+h])**2 for o in origins])}
        for m in MODELS:
            mm=sub[sub.model==m].sort_values('origin'); assert list(mm.origin)==origins
            L[m]=mm.sqerr.values
        out[h]=(np.array(origins),L)
    return out
def paired_mbb(LA,LB,block,nboot=NB,seed=SEED):
    rng=np.random.default_rng(seed); n=len(LA); nb=max(n//block,1); starts=np.arange(n-block+1)
    gaps=np.empty(nboot)
    for i in range(nboot):
        idx=rng.choice(starts,size=nb,replace=True)
        sel=np.concatenate([np.arange(j,j+block) for j in idx])
        gaps[i]=np.sqrt(LA[sel].mean())-np.sqrt(LB[sel].mean())
    lo,hi=np.percentile(gaps,[2.5,97.5]); p=2*min((gaps<=0).mean(),(gaps>=0).mean())
    return lo,hi,p
rows=[]
for spec in ('A','B'):
    data=losses_for(spec)
    for h in (1,5):
        origins,L=data[h]; blk=max(h,3)
        for m in MODELS:
            lo,hi,p=paired_mbb(L[m],L['persist'],blk)
            rows.append(dict(spec=spec,h=h,module=m.split('_')[0],n=len(origins),rmse_mod=np.sqrt(L[m].mean()),rmse_per=np.sqrt(L['persist'].mean()),gap=np.sqrt(L[m].mean())-np.sqrt(L['persist'].mean()),lo=lo,hi=hi,p=p))
R=pd.DataFrame(rows); pd.set_option('display.width',200)
print("=== PAIRED block bootstrap, H2 margins (pooled) ===")
print(R.round(3).to_string(index=False))
R.to_csv(_os.path.join(_HERE,'paired_bootstrap_pooled.csv'),index=False)
# band-level margins
bands={'A':[('1990-1995',1990,1995),('1996-2012',1996,2012),('2013-2014',2013,2014)],
       'B':[('1965-1990',1965,1990),('1991-1995',1991,1995),('1996-2012',1996,2012),('2013-2023',2013,2023)]}
rows=[]
for spec in ('A','B'):
    data=losses_for(spec)
    for h in (1,5):
        origins,L=data[h]
        for name,a,b in bands[spec]:
            sel=(origins>=a)&(origins<=b); n=int(sel.sum())
            if n<3: continue
            blk=min(max(h,3),n)
            for m in MODELS:
                LA=L[m][sel]; LB=L['persist'][sel]
                lo,hi,p=paired_mbb(LA,LB,blk)
                rows.append(dict(spec=spec,h=h,band=name,n=n,module=m.split('_')[0],rmse_mod=np.sqrt(LA.mean()),rmse_per=np.sqrt(LB.mean()),gap=np.sqrt(LA.mean())-np.sqrt(LB.mean()),rel=(np.sqrt(LA.mean())-np.sqrt(LB.mean()))/np.sqrt(LB.mean()),lo=lo,hi=hi,p=p))
B=pd.DataFrame(rows)
print("\n=== PAIRED block bootstrap, band margins ===")
print(B.round(3).to_string(index=False))
B.to_csv(_os.path.join(_HERE,'paired_bootstrap_bands.csv'),index=False)
