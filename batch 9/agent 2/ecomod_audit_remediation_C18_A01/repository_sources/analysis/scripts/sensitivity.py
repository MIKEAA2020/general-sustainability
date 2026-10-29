import numpy as np
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;rg=0.02;alpha=0.5
dt=0.5;T=600.0;n=int(T/dt);Nhist=2000;idx0=Nhist
def run(e,tau_m,tau_p,db,twave,kappa,handle):
    Mv=np.full(idx0+n+1,1.0);Pv=np.full(idx0+n+1,0.1);Dv=np.zeros(idx0+n+1)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0;j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1));return a[j0]*(1-fr)+a[j1]*fr
    for k in range(n+1):
        t=k*dt;i=idx0+k
        if i==idx0: continue
        Dc=Dv[i-1];Tt=db/(1+np.exp(-kappa*(t-twave))) if db>0 else 0.0
        b=b0*np.exp(-alpha*max(0,Dc))+Tt; B=b*Mv[i-1];K=B/ropt
        Etm=e*hist(Pv,t-dt,tau_m); Pt_=hist(Pv,t-dt,tau_p)
        if handle=='freeze':   # K<=0 -> no growth, P held (sim.py v1)
            dP=rg*Pv[i-1]*(1-Pt_/K) if K>1e-15 else 0.0
        else:                  # 'decline': K<=0 -> rapid crash
            dP=rg*Pv[i-1]*(1-Pt_/K) if K>1e-12 else -rg*Pv[i-1]
        dM=rho*Mv[i-1]*(1-Mv[i-1]/Mmax)-gam*Etm
        dD=max(e*Pv[i-1]-B,0.0)
        Mv[i]=max(0,Mv[i-1]+dt*dM);Pv[i]=max(0,Pv[i-1]+dt*dP);Dv[i]=max(0,Dv[i-1]+dt*dD)
    return Mv,Pv,Dv
print("Sensitivity of reported D to the ad-hoc treatment of the singular K->0 endpoint:")
for handle in ['freeze','decline']:
    for label,(db,tw) in [('D (no tech)',(0.0,150)),('E (tech .3)',(0.3,150))]:
        M,P,D=run(1.15,30,25,db,tw,0.1,handle)
        print(f"  handle={handle:8s} {label:12s}: Dfin={D[-1]:.3f}  (paper: D=4.826, E=5.240)")
