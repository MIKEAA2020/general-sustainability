import numpy as np
# ORIGINAL constant-parameter subsystem (gross depletion, 2-D): dM/dt = rho M(1-M/Mmax) - gam*E
# dP/dt = r P (1 - P(tau_p)/K),  K = b0*M/r_opt,  E = e*P(tau_m)
rho=1.5; Mmax=1.2; gam=1.0; b0=0.5; ropt=1.0; r=0.02; e=1.15
Ms=Mmax*(1-gam*e*b0/(rho*ropt)); Ps=b0*Ms/ropt   # note: e used directly (=f*r_opt, r_opt=1)
def classify(M0,P0,tm,tp,dt=0.4,T=500.0):
    n=int(T/dt); Nhist=int(60/dt); idx0=Nhist
    Mv=np.full(idx0+n+1,M0); Pv=np.full(idx0+n+1,P0)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0; j=int(np.floor(xf)); fr=xf-j
        j0=max(0,min(len(a)-1,j)); j1=max(0,min(len(a)-1,j+1)); return a[j0]*(1-fr)+a[j1]*fr
    minM=1e9
    for k in range(n+1):
        i=idx0+k
        if i==idx0: continue
        Mt=Mv[i-1]; Pt=Pv[i-1]; K=b0*Mt/ropt
        Etm=e*hist(Pv,k*dt,tm) if tm>0 else e*Pt
        Pt_=hist(Pv,k*dt,tp) if tp>0 else Pt
        dP=r*Pt*(1-Pt_/K) if K>1e-9 else -r*Pt
        dM=rho*Mt*(1-Mt/Mmax)-gam*Etm
        Mv[i]=max(0,Mt+dt*dM); Pv[i]=max(0,Pt+dt*dP); minM=min(minM,Mv[i])
    if Mv[-1]<0.05: return 'C', minM
    if abs(Mv[-1]-Ms)<0.08 and abs(Pv[-1]-Ps)<0.08: return 'S', minM
    return 'O', minM
def stable_frac(gridM,gridP,tm,tp):
    tot=stab=0
    for M0 in gridM:
        for P0 in gridP:
            tot+=1
            if classify(M0,P0,tm,tp)[0]=='S': stab+=1
    return stab/tot
# fig_basin grid (the one the master's 0.506/0.042 presumably used)
gM_fb=np.arange(0.30,2.21,0.06); gP_fb=np.arange(0.02,0.82,0.04)
# basin.py grid (the other, coarser one)
gM_bp=np.arange(0.30,2.30,0.07); gP_bp=np.arange(0.02,0.85,0.05)
for name,gM,gP in [("fig_basin grid",gM_fb,gP_fb),("basin.py grid",gM_bp,gP_bp)]:
    for (tm,tp) in [(0,0),(30,25)]:
        f=stable_frac(gM,gP,tm,tp)
        c,minM=classify(1.0,0.1,tm,tp)
        print(f"[{name}] tau=({tm},{tp}): stable_frac={f:.3f}  stdIC(1.0,0.1)->{c}")
# (20,20) vs (30,25) trajectory min-M
for (tm,tp) in [(20,20),(30,25)]:
    c,minM=classify(1.0,0.1,tm,tp)
    print(f"tau=({tm},{tp}): stdIC (1.0,0.1) -> {c}, min M over run = {minM:.3f}")
print("equilibrium M*=%.3f P*=%.3f  (0.6 = Mmax/2 = %.3f;  note M* < 0.6 so it's NOT the threshold)"%(Ms,Ps,Mmax/2))
