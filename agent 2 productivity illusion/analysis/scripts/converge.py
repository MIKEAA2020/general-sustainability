import numpy as np
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;rg=0.02
Ms_A=Mmax*(1-gam*1.0*b0/(rho*ropt))
print(f"Scenario A exact equilibrium M*={Ms_A:.4f} P*={b0*Ms_A/ropt:.4f}")
def simA(e,dt,T=600.0):
    n=int(T/dt);Nhist=int(60/dt);idx0=Nhist
    Mv=np.full(idx0+n+1,1.0);Pv=np.full(idx0+n+1,0.1)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0;j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1));return a[j0]*(1-fr)+a[j1]*fr
    for k in range(n+1):
        t=k*dt;i=idx0+k
        if i==idx0: continue
        Mt=Mv[i-1];Pt=Pv[i-1];K=b0*Mt/ropt
        Etm=e*hist(Pv,t-dt,30) if 30>0 else e*Pt
        Pt_=hist(Pv,t-dt,25) if 25>0 else Pt
        dP=rg*Pt*(1-Pt_/K);dM=rho*Mt*(1-Mt/Mmax)-gam*Etm
        Mv[i]=max(0,Mt+dt*dM);Pv[i]=max(0,Pt+dt*dP)
    return Mv[-1],Pv[-1]
print("Scenario A with BOTH delays (30,25) - dt convergence of the equilibrium:")
for dt in [1.0,0.5,0.25,0.1,0.05]:
    M,P=simA(1.0,dt)
    print(f"  dt={dt}: Mfin={M:.5f} Pfin={P:.5f}")
