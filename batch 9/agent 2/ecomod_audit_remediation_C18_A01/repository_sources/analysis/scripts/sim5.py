import numpy as np
rho=1.5; Mmax=1.2; gam=1.0; b0=0.5; ropt=1.0; r=0.02
def run(e,tau_m,tau_p,dt=0.25,T=600.0,IC=(1.0,0.1)):
    n=int(T/dt); Nhist=4000; idx0=Nhist
    Mv=np.full(idx0+n+1,IC[0]); Pv=np.full(idx0+n+1,IC[1])
    def hist(arr,t,delay):
        xf=(t-delay)/dt+idx0
        j=int(np.floor(xf)); frac=xf-j
        j0=max(0,min(len(arr)-1,j)); j1=max(0,min(len(arr)-1,j+1))
        return arr[j0]*(1-frac)+arr[j1]*frac
    for k in range(n+1):
        t=k*dt; i=idx0+k
        if i==idx0: continue
        Mt=Mv[i-1]; Pt=Pv[i-1]
        K=b0*Mt/ropt
        Etm=e*hist(Pv,t-dt,tau_m) if tau_m>0 else e*Pt
        Pt_=hist(Pv,t-dt,tau_p) if tau_p>0 else Pt
        dP=r*Pt*(1-Pt_/K) if K>0 else 0.0
        dM=rho*Mt*(1-Mt/Mmax)-gam*Etm
        Mv[i]=max(0,Mt+dt*dM); Pv[i]=max(0,Pt+dt*dP)
    return Mv,Pv
for name,(tm,tp) in [('B no lag',(0,0)),('C env only',(30,0)),('D both',(30,25)),('Dbp both',(25,25)),('D both 20',(20,20)),('D both 10',(10,10))]:
    M,P=run(1.15,tm,tp)
    print(f"{name:12s} tm={tm} tp={tp}: Mfin={M[-1]:.4f} Pfin={P[-1]:.4f} minM={M.min():.4f}")
