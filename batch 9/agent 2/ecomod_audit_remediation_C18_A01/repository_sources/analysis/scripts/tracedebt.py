import numpy as np
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;r=0.02;alpha=0.5
dt=0.5;T=600.0;n=int(T/dt);Nhist=2000;idx0=Nhist
def run(e,tau_m,tau_p,eta,db,twave,kappa):
    Mv=np.full(idx0+n+1,1.0);Pv=np.full(idx0+n+1,0.1);Dv=np.zeros(idx0+n+1)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0
        j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1))
        return a[j0]*(1-fr)+a[j1]*fr
    rec=[]
    for k in range(n+1):
        t=k*dt;i=idx0+k
        if i==idx0: continue
        Dc=Dv[i-1]; Tt=db/(1+np.exp(-kappa*(t-twave))) if db>0 else 0.0
        b=b0*np.exp(-alpha*max(0,Dc))+Tt
        B=b*Mv[i-1]; Em=e*Pv[i-1]; K=B/ropt
        Etm=e*hist(Pv,t-dt,tau_m) if tau_m>0 else e*Pv[i-1]
        Pt_=hist(Pv,t-dt,tau_p) if tau_p>0 else Pv[i-1]
        dP=r*Pv[i-1]*(1-Pt_/K) if K>0 else 0.0
        dM=rho*Mv[i-1]*(1-Mv[i-1]/Mmax)-gam*Etm
        dD=max(Em-B,0.0)-eta*max(0,Dc)
        Mv[i]=max(0,Mv[i-1]+dt*dM);Pv[i]=max(0,Pv[i-1]+dt*dP);Dv[i]=max(0,Dv[i-1]+dt*dD)
        rec.append((t,Mv[i],Pv[i],B,Em,dD*dt,Dv[i]))
    return np.array(rec)
# D (no tech) vs E (tech)
D_=run(1.15,30,25,0.0,0.0,150.0,0.1)
E_=run(1.15,30,25,0.0,0.3,150.0,0.1)
print("Final: D_D=%.3f  D_E=%.3f"%(D_[-1,6],E_[-1,6]))
# compare B, E, and (E-B)*dt integrand at select times
for t in [110,120,130,140,150,160,170,180,200,250,300]:
    i=int(t//dt)
    # find nearest
    j=int(np.argmin(np.abs(D_[:,0]-t)))
    t2=D_[j,0]
    print(f" t={t2:5.1f} | D: M={D_[j,1]:.3f} P={D_[j,2]:.3f} B={D_[j,3]:.3f} E={D_[j,4]:.3f} dD={D_[j,5]:.4f} D={D_[j,6]:.3f} | E: M={E_[j,1]:.3f} P={E_[j,2]:.3f} B={E_[j,3]:.3f} E={E_[j,4]:.3f} dD={E_[j,5]:.4f} D={E_[j,6]:.3f}")
