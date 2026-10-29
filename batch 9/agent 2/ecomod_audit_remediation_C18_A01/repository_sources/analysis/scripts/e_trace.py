import numpy as np
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;rg=0.02
dt=0.5;T=600.0;n=int(T/dt);Nhist=2000;idx0=Nhist
def runB(e,tau_m,tau_p,alpha,db,twave,kappa):
    Mv=np.full(idx0+n+1,1.0);Pv=np.full(idx0+n+1,0.1);Dv=np.zeros(idx0+n+1);Bv=np.zeros(idx0+n+1)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0;j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1));return a[j0]*(1-fr)+a[j1]*fr
    rec=[]
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
        rec.append((t,Mv[i],Pv[i],b,Bv[i],Tt,Dv[i]))
    return np.array(rec)
print("PAPER's scenario E (db=0.3, t_wave=150, kappa=0.1, alpha=0.5):")
r=runB(1.15,30,25,0.5,0.3,150,0.1)
for t in [0,50,100,120,140,160,180,200,300,600]:
    j=int(np.argmin(np.abs(r[:,0]-t)))
    print(f"  t={r[j,0]:5.1f}  M={r[j,1]:.4f}  b={r[j,3]:.4f}  B={r[j,4]:.4f}  T={r[j,5]:.4f}  D={r[j,6]:.3f}")
print("  Bmax over run = %.4f (init B=0.5)"%r[:,4].max())
print()
print("SAME but t_wave=100 (earlier):")
r2=runB(1.15,30,25,0.5,0.3,100,0.1)
print("  Bmax=%.4f  M_at_Bmax=%.4f  Dfin=%.3f"%(r2[:,4].max(), r2[np.argmax(r2[:,4]),1], r2[-1,6]))
# check: does B rise while M falls?
M=r2[:,1];B=r2[:,4]
dM=np.gradient(M,dt);dB=np.gradient(B,dt)
w=[(r2[i,0],M[i],B[i]) for i in range(1,len(M)-1) if dB[i]>0 and dM[i]<0 and B[i]>0.51 and M[i]<1.0]
if w:
    i0=1
    # find longest sustained window
    print("  illusion present (B rising & M falling & B>0.51): sample", w[0])
    print("  e.g. B peaks at %.3f while M=%.3f"%(B.max(), M[np.argmax(B)]))
