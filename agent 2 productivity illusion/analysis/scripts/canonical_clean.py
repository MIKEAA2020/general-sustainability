import numpy as np
# CLEAN canonical integrator with properly-maintained B history (B = b*A, b from D).
rho=1.5; Amax=1.2; gamma=1.0; b0=0.5; ropt=1.0; r=0.02; alpha=0.5; kappa=0.1
dt=0.25; T=800.0; n=int(T/dt); Nhist=int(80.0/dt); idx=Nhist  # history padded
def run(e, tau_m, tau_p, theta, db=0.0, twave=150.0):
    size=idx+n+5
    A=np.full(size, 1.0); P=np.full(size, 0.1); D=np.zeros(size)
    Bhist=np.zeros(size); bhist=np.zeros(size)
    def h(a,t_arr,d):
        # t_arr is the raw array indexed by integer steps; t is absolute time
        xf=(t-d)/dt+idx; j=int(np.floor(xf)); fr=xf-j
        j0=max(0,min(len(a)-1,j)); j1=max(0,min(len(a)-1,j+1)); return a[j0]*(1-fr)+a[j1]*fr
    for k in range(n+1):
        t=k*dt; i=idx+k
        if i==idx:
            # init history on [-huge,0] at (A=1,P=0.1,D=0)
            # Bhist for past = b0*A = 0.5*1 = 0.5
            for j in range(idx): A[j]=1.0; P[j]=0.1; D[j]=0.0; Bhist[j]=b0*1.0
            continue
        Dc=D[i-1]; Tm=db/(1+np.exp(-kappa*(t-twave))) if db>0 else 0.0
        b=(b0+Tm)*np.exp(-alpha*max(0.0,Dc))
        bhist[i]=b; Bhist[i]=b*A[i-1]
        # lagged B at t-tau_m: use Bhist with interpolation
        def Blag(lag):
            return h(Bhist, t, lag)  # Bhist already = b*A
        Btm=Blag(tau_m) if tau_m>0 else Bhist[i]
        # E(t-tau_m) = e*P(t-tau_m)
        Etm=e*h(P,t,tau_m) if tau_m>0 else e*P[i-1]
        dA=rho*A[i-1]*(1-A[i-1]/Amax) - gamma*(Etm - theta*Btm)
        # carrying capacity at t-tau_p
        Ktm=(Blag(tau_p)/ropt) if tau_p>0 else Bhist[i]/ropt
        Ptm=h(P,t,tau_p) if tau_p>0 else P[i-1]
        dP=r*P[i-1]*(1-Ptm/Ktm) if Ktm>1e-9 else -r*P[i-1]
        dD=max(e*P[i-1]-Bhist[i],0.0)
        A[i]=max(0.0,A[i-1]+dt*dA); P[i]=max(0.0,P[i-1]+dt*dP); D[i]=max(0.0,D[i-1]+dt*dD)
    return A[i] if i<len(A) else A[-1], P[-1], D[-1]

for theta in [0.0,1.0]:
    for e,lab in [(1.0,'sustain e=r_opt'),(1.15,'overshoot e=1.15')]:
        Af,Pf,Df=run(e,30,25,theta)
        print(f"theta={theta:.0f} {lab:20s}: A_fin={Af:.4f}  P_fin={Pf:.4f}  D_fin={Df:.4f}")
print()
print("Interpretation: theta=1 (deficit-driven) should give A>0 (orchard intact) for e=r_opt.")
print("If it does, B2's 'take the fruit, keep the tree' is implemented by construction.")
