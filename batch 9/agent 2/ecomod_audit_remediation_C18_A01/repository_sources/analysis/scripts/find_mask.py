import numpy as np
from demo_unified import integrate
best=None; count=0
for bG in [0.3,0.8]:
  for P0 in [0.7,0.8,0.9,1.0]:
    for deltab in [0.5,0.8,1.0]:
      for tw in [70,90,110]:
        p=dict(rho=0.05,Amax=1.2,b0=0.5,bG=bG,e=0.7,r=0.02,eta=0.03,alpha=0.2,
               sig=1.0,deltab=deltab,kappa=0.04,tw=tw,tau_g=15,tau_p=25,Aext=0.02)
        res=integrate(p,T=400.0,dt=0.5,A0=1.0,P0=P0)
        t,A,P,D,B=res['t'],res['A'],res['P'],res['D'],res['B']
        B0=B[0];A0v=A[0]
        mask=np.array([(B[i]>B0 and A[i]<A0v*0.99) for i in range(len(t))])
        idx=np.where(mask)[0]
        if len(idx):
            j=idx[np.argmax(B[idx])]
            span=t[idx[-1]]-t[idx[0]]
            key=(span,B[idx].max(),A[idx].min())
            if best is None or key>best[0]:
                best=(key,p,A0v,B0,t[idx[0]],t[idx[-1]],t[j],A[j],B[idx].max(),A[idx].min(),D[idx].max())
        count+=1
print("runs=",count)
if best:
    print("BEST masking candidate:")
    print("  A0=%.3f B0=%.3f | window t=[%.0f,%.0f] span=%.0f yr | peak B=%.3f at t=%.0f while A=%.3f | A_min=%.3f D_max=%.3f"%(
        best[2],best[3],best[4],best[5],best[5]-best[4],best[8],best[6],best[7],best[9],best[10]))
    print("  params: bG=%.2f P0=%.2f deltab=%.2f tw=%.0f"%(
        best[1]['bG'],best[1]['P0'],best[1]['deltab'],best[1]['tw']))
    print("  => B rose to %.3f while A fell to %.3f (A0=%.3f): masking illusion, window %.0f yr"%(best[8],best[9],best[2],best[5]-best[4]))
    # refine with fine dt
    p=dict(best[1]); p['kappa']=0.04
    res=integrate(p,T=600.0,dt=0.1,A0=1.0,P0=p['P0'])
    t,A,P,D,B=res['t'],res['A'],res['P'],res['D'],res['B']
    B0=B[0];A0v=A[0];mask=np.array([(B[i]>B0 and A[i]<A0v*0.99) for i in range(len(t))]);idx=np.where(mask)[0]
    j=idx[np.argmax(B[idx])]
    print("  [fine] mask t=[%.0f,%.0f] span=%.0f yr | peak B=%.3f at t=%.0f A=%.3f | A_min=%.3f | final A=%.3f P=%.3f D=%.3f"%(
        t[idx[0]],t[idx[-1]],t[idx[-1]]-t[idx[0]],B[idx].max(),t[j],A[j],A[idx].min(),A[-1],P[-1],D[-1]))
    np.save('demo_mask.npy', np.array([t,A,B,P,D]))
else:
    print("No sustained masking window found")
