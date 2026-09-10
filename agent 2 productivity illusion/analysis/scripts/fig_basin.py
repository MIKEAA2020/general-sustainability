import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;rg=0.02
Ms=Mmax*(1-gam*1.15*b0/(rho*ropt));Ps=b0*Ms/ropt
def classify(M0,P0,tm,tp,dt=0.4,T=500.0):
    n=int(T/dt);Nhist=int(60/dt);idx0=Nhist
    Mv=np.full(idx0+n+1,M0);Pv=np.full(idx0+n+1,P0)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0;j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1));return a[j0]*(1-fr)+a[j1]*fr
    for k in range(n+1):
        t=k*dt;i=idx0+k
        if i==idx0: continue
        Mt=Mv[i-1];Pt=Pv[i-1];K=b0*Mt/ropt
        Etm=1.15*hist(Pv,t-dt,tm);Pt_=hist(Pv,t-dt,tp)
        dP=rg*Pt*(1-Pt_/K) if K>1e-9 else -rg*Pt
        dM=rho*Mt*(1-Mt/Mmax)-gam*Etm
        Mv[i]=max(0,Mt+dt*dM);Pv[i]=max(0,Pt+dt*dP)
    if Mv[-1]<0.05: return 0
    if abs(Mv[-1]-Ms)<0.08 and abs(Pv[-1]-Ps)<0.08: return 1
    return 2
gridM=np.arange(0.30,2.21,0.06);gridP=np.arange(0.02,0.82,0.04)
Mats,Pats=np.meshgrid(gridM,gridP)
fig,axes=plt.subplots(1,2,figsize=(10,4.5),sharex=True,sharey=True)
for ax,(tm,tp) in zip(axes,[(0,0),(30,25)]):
    Z=np.zeros_like(Mats)
    for i in range(len(gridP)):
        for j in range(len(gridM)):
            Z[i,j]=classify(gridM[j],gridP[i],tm,tp)
    stable=(Z==1); collapse=(Z==0)
    ax.imshow(stable.astype(int),extent=[gridM[0],gridM[-1],gridP[0],gridP[-1]],
              origin='lower',aspect='auto',cmap='Blues',vmin=0,vmax=1)
    ax.scatter(Ms,Ps,c='k',marker='x',label='equil (0.74,0.37)')
    ax.scatter(1.0,0.1,c='r',marker='*',s=120,label='std IC (1.0,0.1)')
    ax.axhline(0.6,color='gray',ls=':')
    ax.set_title(f"$\\tau_M$={tm}  $\\tau_P$={tp}")
    ax.set_ylabel('$P_0$');ax.set_xlabel('$M_0$')
frac_st=lambda tm,tp: np.mean([classify(gm,gp,tm,tp)==1 for gm in gridM for gp in gridP])
axes[0].text(0.02,0.98,f"stable frac={frac_st(0,0):.3f}",transform=axes[0].transAxes,va='top')
axes[1].text(0.02,0.98,f"stable frac={frac_st(30,25):.3f}",transform=axes[1].transAxes,va='top')
axes[0].legend(loc='lower right',fontsize=7)
fig.suptitle("Basin of attraction of the overshoot steady state (e=1.15, alpha=0)\nblue=stable, white=collapse")
plt.tight_layout();plt.savefig('/home/user/basin_shrinkage.png',dpi=110)
print("saved basin_shrinkage.png")
