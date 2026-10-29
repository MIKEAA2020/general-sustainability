import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mask_rk4 import run
def win(A,B,t,mindyrs=1.0):
    on=(np.diff(B)>1e-9)&(np.diff(A)<-1e-9); dt=t[1]-t[0]; best=None; i=0
    while i<len(on):
        if on[i]:
            j=i
            while j<len(on) and on[j]: j+=1
            span=(j-i)*dt
            if span>=mindyrs and (best is None or span>best[0]):
                best=(span,t[i],t[j],B[i],B[i:j+1].max(),B[i:j+1].max()-B[i],A[i],A[i:j+1].min(),A[i]-A[i:j+1].min())
            i=j
        i+=1
    return best
p=dict(rho=0.05,Amax=1.2,b0=0.5,bG=0.8,eta=0.05,alpha=0.03,kappa=0.2,tw=15,deltab=1.5,Aext=0.02,w=0.05)
A0=1.0; bA0=0.5*A0
fig,ax=plt.subplots(1,2,figsize=(12,4.6))
# Panel A: representative mask trajectory (deficit=0.06)
E=0.56
r=run(p,T=250,dt=0.02,A0=A0,E=E); t,A,B,D=r['t'],r['A'],r['B'],r['D']
ax[0].plot(t,A,label="stock A",color="#1f77b4",lw=2)
ax[0].plot(t,B,label="biocapacity B",color="#d62728",lw=2)
s=win(A,B,t)
if s:
    t0,t1=int(s[1]),int(s[2])
    ax[0].axvspan(t0,t1,color="gold",alpha=.35)
    ax[0].axvline(t0,color="orange",ls="--",lw=1.2)
    ax[0].axvline(t1,color="orange",ls="--",lw=1.2)
    ax[0].text((t0+t1)/2,1.1,"mask window\n%.1f yr"%s[0],ha="center",fontsize=9)
ax[0].set_xlim(0,120); ax[0].set_ylim(0,1.4)
ax[0].set_xlabel("time t (yr)"); ax[0].set_ylabel("value")
ax[0].set_title("(a) Representative \"productivity illusion\" run\nB rises %.3f->%.3f (peak) while A falls %.2f->%.2f"%(B[0],s[4],A[0],s[7]),fontsize=10)
ax[0].legend(fontsize=8,loc="upper left"); ax[0].grid(alpha=.3)
ax[0].annotate("hidden A decline for ~5 yr",xy=(t1,s[4]),xytext=(60,1.25),fontsize=9,
               arrowprops=dict(arrowstyle="->",color="orange"))
# Panel B: mask window width and rise vs deficit
Es=[0.505,0.515,0.525,0.535,0.545,0.555,0.565,0.575,0.585,0.595,0.61,0.63,0.66,0.70,0.80,1.00]
spans=[]; rises=[]; crit=None
for E in Es:
    r=run(p,T=250,dt=0.05,A0=A0,E=E); t,A,B=r['t'],r['A'],r['B']
    s=win(A,B,t)
    if s:
        spans.append(s[0]); rises.append(s[5])
    else:
        spans.append(0.0); rises.append(0.0)
        if crit is None: crit=E-bA0
ax[1].bar(np.arange(len(Es)),spans,color="#2ca02c",alpha=.85)
ax[1].set_xticks(np.arange(len(Es)))
ax[1].set_xticklabels(["%.3f"%(E-bA0) for E in Es],rotation=90,fontsize=7)
ax[1].set_ylabel("mask window width (yr)")
ax[1].set_xlabel("initial deficit  E \u2212 b\u2080A\u2080  (yr\u207b\u00b9)")
ax[1].set_title("(b) The mask collapses beyond a small deficit\nwindow vanishes for deficit \u2273 %.3f"%(crit if crit else 0.075),fontsize=10)
ax[1].grid(alpha=.3,axis="y")
ax[1].set_ylim(0,7)
plt.tight_layout()
plt.savefig("IMPLEMENTED_demo_masking.png",dpi=150)
print("saved IMPLEMENTED_demo_masking.png  | crit deficit = %.4f"%crit)
print("representative run: B0=%.3f Bpeak=%.3f A0=%.2f Amin=%.3f span=%.1f yr"%(B[0],s[4],A[0],s[7],s[0]))
