import numpy as np
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;rg=0.02;alpha=0.5
dt=0.5;T=600.0;n=int(T/dt);Nhist=2000;idx0=Nhist
def run(e,tau_m,tau_p,cap_frac,cap_on='footprint'):
    Mv=np.full(idx0+n+1,1.0);Pv=np.full(idx0+n+1,0.1);Dv=np.zeros(idx0+n+1)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0;j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1));return a[j0]*(1-fr)+a[j1]*fr
    rec=[]
    for k in range(n+1):
        t=k*dt;i=idx0+k
        if i==idx0: continue
        Dc=Dv[i-1];b=b0*np.exp(-alpha*max(0,Dc));B=b*Mv[i-1]
        if cap_on=='footprint':
            K=cap_frac*B/e
        else:
            K=cap_frac*B/ropt
        Etm=e*hist(Pv,t-dt,tau_m) if tau_m>0 else e*Pv[i-1]
        Pt_=hist(Pv,t-dt,tau_p) if tau_p>0 else Pv[i-1]
        dP=rg*Pv[i-1]*(1-Pt_/K) if K>0 else 0.0
        dM=rho*Mv[i-1]*(1-Mv[i-1]/Mmax)-gam*Etm
        dD=max(e*Pv[i-1]-B,0.0)
        Mv[i]=max(0,Mv[i-1]+dt*dM);Pv[i]=max(0,Pv[i-1]+dt*dP);Dv[i]=max(0,Dv[i-1]+dt*dD)
        bt=b0*np.exp(-alpha*Dv[i]);Bt=bt*Mv[i]
        rec.append((t,Mv[i],Pv[i],Dv[i],Bt,e*Pv[i]/Bt if Bt>1e-9 else np.nan))
    return np.array(rec)
print("Corrected 'Half-Earth' = cap on FOOTPRINT: K = cap*B/e  => Omega -> cap")
for cap in [0.5,0.6]:
    res=run(1.15,30,25,cap,'footprint')
    print(f"  cap={cap}: Mfin={res[-1,1]:.3f} Pfin={res[-1,2]:.3f} Dfin={res[-1,3]:.3f} Omega_final={res[-1,5]:.3f} minM={res[:,1].min():.3f}")
print("Original (population) K=0.5*B/r_opt => Omega=0.575 as in paper:")
res=run(1.15,30,25,0.5,'population')
print(f"  Mfin={res[-1,1]:.3f} Pfin={res[-1,2]:.3f} Dfin={res[-1,3]:.3f} Omega_final={res[-1,5]:.3f} minM={res[:,1].min():.3f}")
