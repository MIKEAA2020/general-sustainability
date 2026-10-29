import numpy as np
rho=1.5; Mmax=1.2; gam=1.0; b0=0.5; ropt=1.0; r=0.02; alpha=0.5
dt=0.5; T=600.0; n=int(T/dt); Nhist=2000; idx0=Nhist
def run(e,tau_m,tau_p,db,twave,kappa,alpha=0.5):
    Mv=np.full(idx0+n+1,1.0); Pv=np.full(idx0+n+1,0.1); Dv=np.zeros(idx0+n+1)
    def hist(arr,t,delay):
        xf=(t-delay)/dt+idx0
        j=int(np.floor(xf)); frac=xf-j
        j0=max(0,min(len(arr)-1,j)); j1=max(0,min(len(arr)-1,j+1))
        return arr[j0]*(1-frac)+arr[j1]*frac
    maxom=0.0; bmax=0.0; Mmin=1.0
    rec=[]
    for k in range(n+1):
        t=k*dt; i=idx0+k
        if i==idx0: Mv[i]=1.0;Pv[i]=0.1;Dv[i]=0.0; continue
        Dcur=Dv[i-1]
        Tt=db/(1+np.exp(-kappa*(t-twave)))
        b=b0*np.exp(-alpha*Dcur)+Tt
        B=b*Mv[i-1]
        Em=e*Pv[i-1]
        Etm=e*hist(Pv,t-dt,tau_m) if tau_m>0 else e*Pv[i-1]
        K=B/ropt
        Pt_=hist(Pv,t-dt,tau_p) if tau_p>0 else Pv[i-1]
        if K<=0: dPdt=0.0
        else: dPdt=r*Pv[i-1]*(1-Pt_/K)
        dMdt=rho*Mv[i-1]*(1-Mv[i-1]/Mmax)-gam*Etm
        dDdt=max(Em-B,0.0)
        Mv[i]=max(0,Mv[i-1]+dt*dMdt); Pv[i]=max(0,Pv[i-1]+dt*dPdt); Dv[i]=Dv[i-1]+dt*dDdt
        bt=b0*np.exp(-alpha*Dv[i])+Tt
        Bt=bt*Mv[i]; Et=e*Pv[i]
        if Bt>1e-9: maxom=max(maxom,Et/Bt)
        bmax=max(bmax,bt); Mmin=min(Mmin,Mv[i])
        rec.append((t,Mv[i],Pv[i],Bt,Dv[i]))
    return np.array(rec),maxom,bmax,Mmin

# Try to find productivity illusion: rising B while M declines, without collapse
for (db,tw) in [(0.3,150),(2.0,50),(2.0,20),(3.0,10),(2.0,100)]:
    rec,om,bmax,Mmin=run(1.15,30,25,db,tw,0.1)
    # find where B rises above initial B(=0.5) while M has declined
    B0=0.5*1.0
    rising = rec[:,3].max()
    # index of max B
    imax=np.argmax(rec[:,3])
    M_at_peakB=rec[imax,1]
    print(f"db={db} tw={tw}: maxB={rising:.3f} (init {B0:.3f}) M_at_maxB={M_at_peakB:.3f} Mfin={rec[-1,1]:.3f} Pfin={rec[-1,2]:.3f} bmax={bmax:.3f}")
