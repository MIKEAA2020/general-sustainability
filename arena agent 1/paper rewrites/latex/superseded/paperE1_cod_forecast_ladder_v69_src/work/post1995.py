import numpy as np, pandas as pd
exec(open('paired_bootstrap.py').read().split('rows=[]')[0])  # reuse loaders/functions
rows=[]
for spec in ('A','B'):
    data=losses_for(spec)
    for h in (1,5):
        origins,L=data[h]; sel=origins>=1996; n=int(sel.sum()); blk=max(h,3)
        for m in MODELS:
            LA=L[m][sel]; LB=L['persist'][sel]; lo,hi,p=paired_mbb(LA,LB,blk)
            rows.append(dict(spec=spec,h=h,n=n,module=m.split('_')[0],rmse_mod=np.sqrt(LA.mean()),rmse_per=np.sqrt(LB.mean()),rel=(np.sqrt(LA.mean())-np.sqrt(LB.mean()))/np.sqrt(LB.mean()),lo=lo,hi=hi,p=p))
        # collapse-band-only (origins <=1995) for completeness
        sel2=origins<=1995; n2=int(sel2.sum())
        for m in MODELS:
            LA=L[m][sel2]; LB=L['persist'][sel2]
            rows.append(dict(spec=spec,h=h,n=n2,module=m.split('_')[0]+'(<=1995)',rmse_mod=np.sqrt(LA.mean()),rmse_per=np.sqrt(LB.mean()),rel=(np.sqrt(LA.mean())-np.sqrt(LB.mean()))/np.sqrt(LB.mean()),lo=np.nan,hi=np.nan,p=np.nan))
R=pd.DataFrame(rows); pd.set_option('display.width',200); print(R.round(3).to_string(index=False)); R.to_csv('post1995_margins.csv',index=False)
