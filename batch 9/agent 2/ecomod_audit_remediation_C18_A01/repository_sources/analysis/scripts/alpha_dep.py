import numpy as np
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;rg=0.02
dt=0.5;T=600.0;n=int(T/dt);Nhist=2000;idx0=Nhist
def run(e,tau_m,tau_p,alpha,db,twave,kappa):
    Mv=np.full(idx0+n+1,1.0);Pv=np.full(idx0+n+1,0.1);Dv=np.zeros(idx0+n+1)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0;j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1));return a[j0]*(1-fr)+a[j1]*fr
    for k in range(n+1):
        t=k*dt;i=idx0+k
        if i==idx0: continue
        Dc=Dv[i-1];Tt=db/(1+np.exp(-kappa*(t-twave)))
        b=b0*np.exp(-alpha*max(0,Dc))+Tt; B=b*Mv[i-1];K=B/ropt
        Etm=e*hist(Pv,t-dt,tau_m); Pt_=hist(Pv,t-dt,tau_p)
        dP=rg*Pv[i-1]*(1-Pt_/K) if K>1e-12 else -rg*Pv[i-1]
        dM=rho*Mv[i-1]*(1-Mv[i-1]/Mmax)-gam*Etm
        dD=max(e*Pv[i-1]-B,0.0)
        Mv[i]=max(0,Mv[i-1]+dt*dM);Pv[i]=max(0,Pv[i-1]+dt*dP);Dv[i]=max(0,Dv[i-1]+dt*dD)
    return Mv,Pv,Dv
# Detect illusion (B rising while M falling, B>init)
def has_illusion(e,alpha,db,tw,kappa):
    M,P,D=run(e,30,25,alpha,db,tw,kappa)
    # reconstruct B
    B=np.zeros(len(M)); 
    Dc=np.zeros(len(M))
    # approximate B via stored: recompute (cheap) - rerun recording B
    return None
# simpler: rerun recording B
def runB(e,tau_m,tau_p,alpha,db,twave,kappa):
    Mv=np.full(idx0+n+1,1.0);Pv=np.full(idx0+n+1,0.1);Dv=np.zeros(idx0+n+1);Bv=np.zeros(idx0+n+1)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0;j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1));return a[j0]*(1-fr)+a[j1]*fr
    for k in range(n+1):
        t=k*dt;i=idx0+k
        if i==idx0: continue
        Dc=Dv[i-1];Tt=db/(1+np.exp(-kappa*(t-twave)))
        b=b0*np.exp(-alpha*max(0,Dc))+Tt; Bv[i]=b*Mv[i-1];K=Bv[i]/ropt
        Etm=e*hist(Pv,t-dt,tau_m); Pt_=hist(Pv,t-dt,tau_p)
        dP=rg*Pv[i-1]*(1-Pt_/K) if K>1e-12 else -rg*Pv[i-1]
        dM=rho*Mv[i-1]*(1-Mv[i-1]/Mmax)-gam*Etm
        dD=max(e*Pv[i-1]-Bv[i],0.0)
        Mv[i]=max(0,Mv[i-1]+dt*dM);Pv[i]=max(0,Pv[i-1]+dt*dP);Dv[i]=max(0,Dv[i-1]+dt*dD)
    return Mv,Bv,Dv
for alpha in [0.2,0.5]:
    for db in [0.8,2.0]:
        M,B,D=runB(1.15,30,25,alpha,db,100,0.05)
        # find any window B rising while M falling
        dM=np.gradient(M,dt);dB=np.gradient(B,dt)
        ok=any((dB[i]>0 and dM[i]<0 and B[i]>0.51) for i in range(1,len(M)-1))
        print(f"  alpha={alpha} db={db}: Bmax={B.max():.3f} (init 0.5) Bfin={B[-1]:.3f} Mfin={M[-1]:.3f} Dfin={D[-1]:.3f} illusion_window={ok}")
