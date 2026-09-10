import numpy as np
from scipy.optimize import root
rho=1.5; Mmax=1.2; gam=1.0; b0=0.5; ropt=1.0; r=0.02
eA=1.0
MstA=Mmax*(1-gam*eA*b0/(rho*ropt))
a11=rho*(1-2*MstA/Mmax); a21=r*b0/ropt; ge=gam*eA

def F(lam, tm, tp):
    return lam**2 - a11*lam + r*(lam-a11)*np.exp(-lam*tp) + ge*a21*np.exp(-lam*tm)

def dominant(tm, tp):
    seeds=[]
    for re in np.linspace(-0.35,0.35,15):
        for im in np.linspace(0,0.7,21):
            seeds.append((re,im)); seeds.append((re,-im))
    cand=[]
    for s in seeds:
        sol=root(lambda z:[F(complex(z[0],z[1]),tm,tp).real,F(complex(z[0],z[1]),tm,tp).imag],list(s))
        if sol.success:
            l=complex(sol.x[0],sol.x[1])
            if abs(F(l,tm,tp))<1e-7 and abs(l.imag)<0.8 and abs(l.real)<0.4:
                cand.append(l)
    uni=[]
    for l in cand:
        if not any(abs(l-u)<1e-4 for u in uni): uni.append(l)
    if not uni: return None
    return max(uni,key=lambda z:z.real)

points=[(0,0),(20,10),(30,25),(40,40),(50,30),(60,20),(70,10),(70,20),(60,30),(50,40),(40,50),(30,60),(20,70),(10,80),(80,0),(79,1),(78,2),(75,5),(74,6),(72,8),(60,20),(55,25),(50,30),(45,35)]
print("tau_m tau_p  sum   Re(lam)  Im(lam)")
for tm,tp in points:
    l=dominant(tm,tp)
    print(f"{tm:3d} {tp:3d}  {tm+tp:5d}  {l.real:+.4f}  {l.imag:+.4f}" if l else f"{tm:3d} {tp:3d}  {tm+tp:5d}  none")
