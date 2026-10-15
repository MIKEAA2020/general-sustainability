"""Block-length sensitivity (2..8) of the paired MBB interval for the H2 margins, 5,000 reps."""
import numpy as np, pandas as pd, sys
sys.argv=['x']; exec(open('paired_bootstrap.py').read().split('rows=[]')[0])  # reuse losses_for, paired_mbb
rows=[]
for spec in ('A','B'):
    data=losses_for(spec)
    for h in (1,5):
        origins,L=data[h]
        for m in ("M1_autonomous_Schaefer","M3_AR_residual"):
            for blk in (2,3,4,5,6,8):
                lo,hi,p=paired_mbb(L[m],L['persist'],blk,nboot=5000)
                rows.append(dict(spec=spec,h=h,module=m.split('_')[0],block=blk,gap=np.sqrt(L[m].mean())-np.sqrt(L['persist'].mean()),lo=lo,hi=hi,p=p,excl0=(lo>0)|(hi<0)))
G=pd.DataFrame(rows); print(G.round(3).to_string(index=False)); G.to_csv('block_grid.csv',index=False)
