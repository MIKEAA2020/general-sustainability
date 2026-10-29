import numpy as np
from scipy.optimize import root
rho=1.5; Mmax=1.2; gam=1.0; b0=0.5; ropt=1.0; r=0.02
a11=-0.5; a21=0.01; ge=1.0*1.0
def F(lam,tm,tp):
    return lam**2 - a11*lam + r*(lam-a11)*np.exp(-lam*tp) + ge*a21*np.exp(-lam*tm)
def dominant(tm,tp):
    seeds=[]
    for re in np.linspace(-0.3,0.3,13):
        for im in np.linspace(0,0.8,25):
            seeds.append((re,im))
    cand=[]
    for s in seeds:
        sol=root(lambda z:[F(complex(z[0],z[1]),tm,tp).real,F(complex(z[0],z[1]),tm,tp).imag],list(s))
        if sol.success:
            l=complex(sol.x[0],sol.x[1])
            if abs(F(l,tm,tp))<1e-8 and not any(abs(l-u)<1e-4 for u in cand):
                cand.append(l)
    if not cand: return None
    return max(cand,key=lambda z:z.real)
for (tm,tp) in [(40,40),(50,50),(60,60),(70,70),(80,80),(90,90),(100,100),(50,40),(60,50),(70,40),(80,30),(90,20),(40,80),(30,90),(20,100)]:
    l=dominant(tm,tp)
    print(f"tm={tm:3d} tp={tp:3d} sum={tm+tp:3d}  Re={l.real:+.4f} Im={l.imag:+.4f}" if l else f"tm={tm} tp={tp} none")
