import numpy as np
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;r=0.02
Ms=Mmax*(1-gam*1.15*b0/(rho*ropt)); Ps=b0*Ms/ropt
print(f"equilibrium M*={Ms:.3f} P*={Ps:.3f} (for e=1.15, alpha=0)")
def classify(M0,P0,tau_m,tau_p,dt=0.4,T=500.0):
    n=int(T/dt);Nhist=2000;idx0=Nhist
    Mv=np.full(idx0+n+1,M0);Pv=np.full(idx0+n+1,P0)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0;j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1));return a[j0]*(1-fr)+a[j1]*fr
    for k in range(n+1):
        t=k*dt;i=idx0+k
        if i==idx0: continue
        Mt=Mv[i-1];Pt=Pv[i-1];K=b0*Mt/ropt
        Etm=1.15*hist(Pv,t-dt,tau_m) if tau_m>0 else 1.15*Pt
        Pt_=hist(Pv,t-dt,tau_p) if tau_p>0 else Pt
        if K>1e-9: dP=r*Pt*(1-Pt_/K)
        else: dP=-r*Pt*1.0  # overcapacity -> decline
        dM=rho*Mt*(1-Mt/Mmax)-gam*Etm
        Mv[i]=max(0,Mt+dt*dM);Pv[i]=max(0,Pt+dt*dP)
    # classify: stable if near equilibrium, collapse if M->0 significantly
    if Mv[-1]<0.05: return 'C'  # collapse
    if abs(Mv[-1]-Ms)<0.08 and abs(Pv[-1]-Ps)<0.08: return 'S'
    return 'O'  # other (osc/limit cycle)
for (tm,tp) in [(0,0),(10,10),(20,20),(15,15),(25,25),(30,25),(30,30),(40,40)]:
    gridM=np.arange(0.30,2.30,0.07); gridP=np.arange(0.02,0.85,0.05)
    tot=0;col=0;stab=0;other=0
    for M0 in gridM:
        for P0 in gridP:
            tot+=1
            c=classify(M0,P0,tm,tp)
            if c=='C': col+=1
            elif c=='S': stab+=1
            else: other+=1
    # is standard IC (1.0,0.1) inside?
    std=classify(1.0,0.1,tm,tp)
    print(f"tm={tm:3d} tp={tp:3d} (sum={tm+tp:3d}): stable frac={stab/tot:.3f} collapse frac={col/tot:.3f} other={other/tot:.3f}  std IC(1.0,0.1)-> {std}")
