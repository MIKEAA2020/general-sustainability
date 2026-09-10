import numpy as np
rho=1.5; Mmax=1.2; gam=1.0; b0=0.5; ropt=1.0; r=0.02
# constant-parameter subsystem: alpha=0 (b=b0 constant), e=1.15 overshoot, both delays
# This is what "forcing D->0" gives.
def run(e,tau_m,tau_p,dt=0.5,T=600.0,IC=(1.0,0.1)):
    n=int(T/dt); Nhist=2000; idx0=Nhist
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
        if K<=0: dP=0.0
        else: dP=r*Pt*(1-Pt_/K)
        dM=rho*Mt*(1-Mt/Mmax)-gam*Etm
        Mv[i]=max(0,Mt+dt*dM); Pv[i]=max(0,Pt+dt*dP)
    return Mv,Pv
for dt in [0.5,0.25,0.1]:
    M,P=run(1.15,30,25,dt=dt)
    print(f"const-sub dt={dt}: Mfin={M[-1]:.4f} Pfin={P[-1]:.4f} minM={M.min():.4f} minP={P.min():.4f}")
# also from near-equilibrium IC to confirm stability
M,P=run(1.15,30,25,IC=(0.740,0.37))
print("near-eq IC: Mfin=%.4f Pfin=%.4f minM=%.4f"%(M[-1],P[-1],M.min()))
