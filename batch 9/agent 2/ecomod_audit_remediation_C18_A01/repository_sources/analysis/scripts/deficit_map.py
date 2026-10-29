import numpy as np
from mask_rk4 import run
def win(A,B,t,mindyrs=1.0):
    dA=np.diff(A); dB=np.diff(B); dt=t[1]-t[0]
    on=(dB>1e-9)&(dA<-1e-9); best=None; i=0
    while i<len(on):
        if on[i]:
            j=i
            while j<len(on) and on[j]: j+=1
            span=(j-i)*dt
            if span>=mindyrs:
                if best is None or span>best[0]:
                    best=(span,t[i],t[j],B[i],B[i:j+1].max(),B[i:j+1].max()-B[i],A[i],A[i:j+1].min(),A[i]-A[i:j+1].min())
            i=j
        i+=1
    return best

# FAVOURABLE mask config (early strong fast wave), vary E = deficit size
p=dict(rho=0.05,Amax=1.2,b0=0.5,bG=0.8,eta=0.05,alpha=0.03,kappa=0.2,tw=15,deltab=1.5,Aext=0.02,w=0.05)
A0=1.00; bA0=0.5*A0
print("A0=%.2f b0*A0=%.3f   (mask config: rho=0.05 bG=0.8 k=0.2 tw=15 db=1.5 eta=0.05 alpha=0.03, dt=0.05)^")
print("%-6s %-10s %-8s %-10s %-8s %-10s %-8s %-8s"%("E","deficit","B0","Bpeak","rise","Amin","fall","span"))
for E in [0.505,0.52,0.535,0.55,0.56,0.575,0.60,0.63,0.66,0.70,0.75,0.80,0.90,1.00]:
    r=run(p,T=250,dt=0.05,A0=A0,E=E); t,A,B=r['t'],r['A'],r['B']
    s=win(A,B,t)
    if s:
        print("%-6.3f %-10.4f %-8.3f %-10.3f %-8.3f %-10.3f %-8.3f %-8.1f"%(E,E-bA0,B[0],s[4],s[5],s[7],s[8],s[0]))
    else:
        # no mask; give Bmax and Amin
        print("%-6.3f %-10.4f %-8.3f %-10s %-8s %-10.3f %-8s %-8s"%(E,E-bA0,B[0],"---","---",A.min(),"---","---"))
