import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;r=0.02;alpha=0.2
dt=0.5;T=600.0;n=int(T/dt);Nhist=2000;idx0=Nhist
def run(e,tau_m,tau_p,alpha,db,twave,kappa):
    Mv=np.full(idx0+n+1,1.0);Pv=np.full(idx0+n+1,0.1);Dv=np.zeros(idx0+n+1)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0;j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1));return a[j0]*(1-fr)+a[j1]*fr
    rec=[]
    for k in range(n+1):
        t=k*dt;i=idx0+k
        if i==idx0: continue
        Dc=Dv[i-1];Tt=db/(1+np.exp(-kappa*(t-twave)))
        b=b0*np.exp(-alpha*max(0,Dc))+Tt
        B=b*Mv[i-1];K=B/ropt
        Etm=e*hist(Pv,t-dt,tau_m) if tau_m>0 else e*Pv[i-1]
        Pt_=hist(Pv,t-dt,tau_p) if tau_p>0 else Pv[i-1]
        dP=r*Pv[i-1]*(1-Pt_/K) if K>0 else 0.0
        dM=rho*Mv[i-1]*(1-Mv[i-1]/Mmax)-gam*Etm
        dD=max(e*Pv[i-1]-B,0.0)
        Mv[i]=max(0,Mv[i-1]+dt*dM);Pv[i]=max(0,Pv[i-1]+dt*dP);Dv[i]=max(0,Dv[i-1]+dt*dD)
        rec.append((t,Mv[i],Pv[i],Dv[i],b,B))
    return np.array(rec)
rec=run(1.15,30,25,0.2,0.8,100,0.05)
B0=rec[0,5]
print(f"IC M=1.0 P=0.1.  Result: Mfin={rec[-1,1]:.3f} Pfin={rec[-1,2]:.3f} Dfin={rec[-1,3]:.3f} Bfin={rec[-1,5]:.3f}")
print("Illusion window detection (B rising while M falling), with B above initial:")
B=rec[:,5];M=rec[:,1];t=rec[:,0]
dM=np.gradient(M,dt);dB=np.gradient(B,dt)
worstM=B0
for i in range(1,len(t)-1):
    if dB[i]>0 and dM[i]<0 and B[i]>B0*1.02 and M[i]<1.0:
        j=i
        while j<len(t)-1 and dB[j]>0 and dM[j]<0: j+=1
        print(f"  window t={t[i]:.0f}-{t[j]:.0f}: M {M[i]:.3f}->{M[j]:.3f}, B {B[i]:.3f}->{B[j]:.3f}. B now {B[i]/B0:.2f}x initial, M {M[i]:.2f} (below 1.0)")
# plot
fig,ax=plt.subplots(2,1,figsize=(7,6),sharex=True)
ax[0].plot(t,M,'b-',lw=2,label='Environmental stock M(t)')
ax[0].plot(t,B,'r-',lw=2,label='Biocapacity B(t)')
ax[0].axhline(1.0,color='gray',ls=':',lw=1)
ax[0].set_ylabel('gha');ax[0].legend();ax[0].set_title('Productivity illusion: B rises while M falls')
ax[1].plot(t,M,color='blue',lw=1)
ax[1].plot(t,B,color='red',lw=1)
ax[1].set_yscale('log');ax[1].set_xlabel('t (yr)');ax[1].set_ylabel('log scale')
ax[1].set_title('Same, log scale (late-time breakdown)')
plt.tight_layout();plt.savefig('/home/user/illusion_demo.png',dpi=110)
print("saved illusion_demo.png")
# choose index where M first dips below 1.0 and B still rising
