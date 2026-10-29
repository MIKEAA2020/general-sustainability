import numpy as np
rho=1.5; Mmax=1.2; gam=1.0; b0=0.5; ropt=1.0; r=0.02; alpha=0.5
dt=0.25; T=600.0; n=int(T/dt); Nhist=4000; idx0=Nhist
def run(e,tau_m,tau_p,eta,alpha=0.5):
    Mv=np.full(idx0+n+1,1.0); Pv=np.full(idx0+n+1,0.1); Dv=np.zeros(idx0+n+1)
    def hist(arr,t,delay):
        xf=(t-delay)/dt+idx0
        j=int(np.floor(xf)); frac=xf-j
        j0=max(0,min(len(arr)-1,j)); j1=max(0,min(len(arr)-1,j+1))
        return arr[j0]*(1-frac)+arr[j1]*frac
    for k in range(n+1):
        t=k*dt; i=idx0+k
        if i==idx0: continue
        Dcur=Dv[i-1]
        b=b0*np.exp(-alpha*max(0.0,Dcur))
        B=b*Mv[i-1]; Em=e*Pv[i-1]
        K=B/ropt
        Etm=e*hist(Pv,t-dt,tau_m) if tau_m>0 else e*Pv[i-1]
        Pt_=hist(Pv,t-dt,tau_p) if tau_p>0 else Pv[i-1]
        dP=r*Pv[i-1]*(1-Pt_/K) if K>0 else 0.0
        dM=rho*Mv[i-1]*(1-Mv[i-1]/Mmax)-gam*Etm
        dD=max(Em-B,0.0)-eta*max(0.0,Dcur)
        Mv[i]=max(0,Mv[i-1]+dt*dM); Pv[i]=max(0,Pv[i-1]+dt*dP); Dv[i]=max(0.0,Dv[i-1]+dt*dD)
    return Mv,Pv,Dv
print("Full debt model, scenario D (tm=30,tp=25,e=1.15), varying eta:")
for eta in [0.0,0.02,0.5,2.0,10.0]:
    M,P,D=run(1.15,30,25,eta)
    print(f"  eta={eta:4}: Mfin={M[-1]:.4f} Pfin={P[-1]:.4f} Dfin={D[-1]:.4f} minM={M.min():.4f}")
