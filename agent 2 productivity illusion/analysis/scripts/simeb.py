import numpy as np
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;r=0.02;alpha=0.5
dt=0.5;T=600.0;n=int(T/dt);Nhist=2000;idx0=Nhist
def run(e,tau_m,tau_p,eta):
    Mv=np.full(idx0+n+1,1.0);Pv=np.full(idx0+n+1,0.1);Dv=np.zeros(idx0+n+1)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0
        j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1))
        return a[j0]*(1-fr)+a[j1]*fr
    for k in range(n+1):
        t=k*dt;i=idx0+k
        if i==idx0: continue
        Dc=Dv[i-1]; b=b0*np.exp(-alpha*max(0,Dc)); B=b*Mv[i-1]; Em=e*Pv[i-1]; K=B/ropt
        Etm=e*hist(Pv,t-dt,tau_m) if tau_m>0 else e*Pv[i-1]
        Pt_=hist(Pv,t-dt,tau_p) if tau_p>0 else Pv[i-1]
        dP=r*Pv[i-1]*(1-Pt_/K) if K>0 else 0.0
        dM=rho*Mv[i-1]*(1-Mv[i-1]/Mmax)-gam*Etm
        dD=max(Em-B,0.0)-eta*max(0,Dc)
        Mv[i]=max(0,Mv[i-1]+dt*dM);Pv[i]=max(0,Pv[i-1]+dt*dP);Dv[i]=max(0,Dv[i-1]+dt*dD)
    return Mv,Pv,Dv
# check for oscillation: count sign changes of (P - mean) in last 200 yr
import statistics
for eta in [0.0,0.005,0.02,0.05,0.1,0.2,1.0,5.0,10.0]:
    M,P,D=run(1.15,0,0,eta)
    tail=P[-400:]
    m=tail.mean()
    signs=np.sign(tail-m)
    crossings=int(np.sum(np.abs(np.diff(signs))>0))
    print(f"eta={eta:5}: Pfin={P[-1]:.4f} Mfin={M[-1]:.4f} Dfin={D[-1]:.4f} tail_crossings={crossings} tailrange={tail.max()-tail.min():.3f}")
