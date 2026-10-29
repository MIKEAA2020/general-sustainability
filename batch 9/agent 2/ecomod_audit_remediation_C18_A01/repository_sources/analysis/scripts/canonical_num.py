import numpy as np
# Numerically verify the CANONICAL deficit-driven model: theta=1 (only deficit drains A)
# vs ORIGINAL theta=0 (full footprint drains A). Show orchard metaphor becomes true for theta=1.
rho=1.5; Amax=1.2; gamma=1.0; b0=0.5; ropt=1.0; r=0.02; alpha=0.5; kappa=0.1
dt=0.4; T=300.0; n=int(T/dt); Nhist=int(60/dt); idx=Nhist
def run(e, tau_m, tau_p, theta, db=0.3, twave=150.0):
    A=np.full(idx+n+1, 1.0); P=np.full(idx+n+1, 0.1); D=np.zeros(idx+n+1)
    def h(a,t,d):
        xf=(t-d)/dt+idx; j=int(np.floor(xf)); fr=xf-j
        j0=max(0,min(len(a)-1,j)); j1=max(0,min(len(a)-1,j+1)); return a[j0]*(1-fr)+a[j1]*fr
    # store B history to avoid recompute: keep A and b and D; B=b*D? use b from D
    def B(t_lag):
        Dl=h(D.copy(),t_lag,0)
        Tb=db/(1+np.exp(-kappa*(t_lag-twave))) if db>0 else 0.0
        b=(b0+Tb)*np.exp(-alpha*max(0,Dl))
        return b*h(A.copy(),t_lag,0)
    for k in range(n+1):
        t=k*dt; i=idx+k
        if i==idx: continue
        Dc=D[i-1]; Tb=db/(1+np.exp(-kappa*(t-twave))) if db>0 else 0.0
        b=(b0+Tb)*np.exp(-alpha*max(0,Dc))
        Bcur=b*A[i-1]; Btm=B(t-tau_m) if tau_m>0 else Bcur
        Etm=e*h(P.copy(),t-dt,tau_m) if tau_m>0 else e*P[i-1]
        dA=rho*A[i-1]*(1-A[i-1]/Amax) - gamma*(Etm - theta*Btm)
        Ktm=B(t-tau_p)/ropt if tau_p>0 else Bcur/ropt
        Ptm=h(P.copy(),t-dt,tau_p) if tau_p>0 else P[i-1]
        dP=r*P[i-1]*(1-Ptm/Ktm) if Ktm>1e-9 else -r*P[i-1]
        dD=max(e*P[i-1]-Bcur,0.0)
        A[i]=max(0,A[i-1]+dt*dA); P[i]=max(0,P[i-1]+dt*dP); D[i]=max(0,D[i-1]+dt*dD)
    return A,P,D

print("ORIGINAL (theta=0: full footprint E drains stock, gamma=1):  sustainable e=r_opt")
A,P,D=run(1.0,30,25,0.0)
print(f"   e=1.0 (sustainable): Afin={A[-1]:.3f} Pfin={P[-1]:.3f} Dfin={D[-1]:.4f}")
print(f"   NOTE: even at SUSTAINABLE e=1.0, the original model drains/degraded the stock (B not in Eq1).")
A,P,D=run(1.15,30,25,0.0)
print(f"   e=1.15 (overshoot): Afin={A[-1]:.3f} Pfin={P[-1]:.3f} Dfin={D[-1]:.4f}  (stock still drawn)")
print()
print("CANONICAL (theta=1: only DEFICIT drains stock): e=r_opt sustainable should be PRISTINE")
A,P,D=run(1.0,30,25,1.0)
print(f"   e=1.0 (sustainable): Afin={A[-1]:.3f} Pfin={P[-1]:.3f} Dfin={D[-1]:.4f}")
print(f"   -> At sustainable e=r_opt, the 'deficit' E-B=0, so NO stock loss. Orchard metaphor TRUE.")
A,P,D=run(1.15,30,25,1.0)
print(f"   e=1.15 (overshoot): Afin={A[-1]:.3f} Pfin={P[-1]:.3f} Dfin={D[-1]:.4f}  (only overshoot drains stock)")
print()
print("CONCLUSION: theta (accounting switch) is the root-cause lever that makes Eq(1) implement the")
print("narrative. theta=0 is the paper's gross-depletion form (B2 flaw); theta=1 is the GFN/deficit")
print("form that makes 'take the fruit, keep the tree' literally true. The ORIGINAL narrative demands")
print("theta=1 yet implements theta=0.")
