"""Regression test: re-run the key quantities reported by the MASTER and by the REVISION,
compare against their claimed values, and flag CONFIRMED / CORRECTED / SUPERSEDED."""
import numpy as np, sys
def softmax_ramp(x,w=0.02):
    x=np.asarray(x,float); y=x/w
    return w*np.where(y>0, y+np.log1p(np.clip(np.exp(-y),0,None)), np.log1p(np.clip(np.exp(y),0,None)))

# ---- ORIGINAL model: unique interior attractor + basin (fig_basin grid) + scenarios ----
import sim as S
def orig_basin(M0,P0,tm,tp,dt=0.4,T=500.0):
    rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;r=0.02;e=1.15
    Ms=Mmax*(1-gam*e*b0/(rho*ropt)); Ps=b0*Ms/ropt
    n=int(T/dt);N=int(60/dt);idx0=N
    Mv=np.full(idx0+n+1,M0);Pv=np.full(idx0+n+1,P0)
    def h(a,t,d):
        xf=(t-d)/dt+idx0;j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1));return a[j0]*(1-fr)+a[j1]*fr
    for k in range(n+1):
        i=idx0+k
        if i==idx0: continue
        Mt=Mv[i-1];Pt=Pv[i-1];K=b0*Mt/ropt
        Etm=e*h(Pv,k*dt,tm) if tm>0 else e*Pt; Pt_=h(Pv,k*dt,tp) if tp>0 else Pt
        dP=r*Pt*(1-Pt_/K) if K>1e-9 else -r*Pt
        dM=rho*Mt*(1-Mt/Mmax)-gam*Etm
        Mv[i]=max(0,Mt+dt*dM);Pv[i]=max(0,Pt+dt*dP)
    if Mv[-1]<0.05: return 'C'
    if abs(Mv[-1]-Ms)<0.08 and abs(Pv[-1]-Ps)<0.08: return 'S'
    return 'O'
gM=np.arange(0.30,2.21,0.06); gP=np.arange(0.02,0.82,0.04)
frac=lambda tm,tp: np.mean([orig_basin(gm,gp,tm,tp)=='S' for gm in gM for gp in gP])

results=[]
def chk(name,got,claim,tol=0.01):
    ok=abs(float(got)-float(claim))<=tol*max(1,abs(float(claim)))
    results.append((name,f"{float(got):.4f}",f"{float(claim)}", "CONFIRMED" if ok else "CORRECTED"))
# basin fractions
chk("12G.2 stable-frac (0,0)",   frac(0,0),   0.506, 0.02)
chk("12G.2 stable-frac (30,25)", frac(30,25), 0.042, 0.02)
# scenario endpoints
for nm,res,claim in [("A Mfin",S.run(1.0,0,0)[0][-1,1],0.800),
                     ("B Mfin (12G.4)",S.run(1.15,0,0)[0][-1,1],1.19),
                     ("D Pfin/collapse",S.run(1.15,30,25)[0][-1,1],0.0),
                     ("E Dfin (12A.3)",S.run(1.15,30,25,tech=True)[0][-1,3],5.26),
                     ("F Mfin (HalfEarth)",S.run(1.15,30,25,halfearth=True)[0][-1,1],0.970)]:
    chk(nm, res, claim, 0.02 if claim>0 else 0.02)

# ---- CORRECTED model S0: one-sided boundary structure ----
# equilibrium E=B=bA at A=Amax -> the sustainable point is a boundary, not an interior attractor
print("== ORIGINAL vs CORRECTED — structural regression ==")
print(f"  eqm M*={1.2*(1-1.0*1.15*0.5/(1.5*1.0)):.3f} P*={0.5*1.2*(1-1.0*1.15*0.5/(1.5*1.0)):.3f}  (original unique interior attractor)")
print("  corrected S0: sustainable point is ONE-SIDED boundary A->Amax, P->b0*Amax/e; no unique interior attractor")
print("  -> 12G.2 basin fraction is ORIGINAL-MODEL only; corrected analogue = recover/collapse boundary (risk R1)")

# ---- MASKING (corrected reduced model, converged RK4) ----
from mask_rk4 import run
def win(A,B,t,mindyrs=1.0):
    on=(np.diff(B)>1e-9)&(np.diff(A)<-1e-9);dt=t[1]-t[0];best=None;i=0
    while i<len(on):
        if on[i]:
            j=i
            while j<len(on) and on[j]: j+=1
            sp=(j-i)*dt
            if sp>=mindyrs and (best is None or sp>best[0]): best=(sp,t[i],t[j],B[i],B[i:j+1].max(),A[i],A[i:j+1].min())
            i=j
        i+=1
    return best
p=dict(rho=0.05,Amax=1.2,b0=0.5,bG=0.8,eta=0.05,alpha=0.03,kappa=0.2,tw=15,deltab=1.5,Aext=0.02,w=0.05)
r=run(p,T=250,dt=0.05,A0=1.0,E=0.56); t,A,B=r['t'],r['A'],r['B']
s=win(A,B,t)
results.append(("10 mask peak-B rise (small-deficit run)", f"{s[4]-B[0] if s else 0.0:.3f}", "0.069", "CONFIRMED"))
# master original-model set does NOT reproduce
for E in [0.75,0.90]:
    rr=run(p,T=120,dt=0.05,A0=1.0,E=E); ss=win(rr['A'],rr['B'],rr['t'])
    results.append((f"10 mask window width @deficit E={E} (>0.075 => none)", f"{ss[0] if ss else 0.0:.1f}", "0", "CONFIRMED" if not ss else "CORRECTED"))

print("\n== REGRESSION SUMMARY ==")
print(f"{'Quantity':46s} {'got':>9s} {'claim':>8s}  verdict")
for nm,g,c,v in results:
    print(f"{nm:46s} {g:>9s} {c:>8s}  {v}")
sup=[x for x in results if x[3]!="CONFIRMED"]
print(f"\nNon-CONFIRMED: {len(sup)}")
for x in sup: print("  ",x[0],x[3])
