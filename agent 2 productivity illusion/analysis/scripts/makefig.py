import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from demo_unified import integrate
# Clean overshoot -> collapse scenario (well-posed: smooth ramp + A_ext floor + K floor)
p=dict(rho=0.08, Amax=1.2, b0=0.5, bG=0.6, e=0.55, r=0.02, eta=0.03, alpha=0.2,
       sig=1.0, deltab=0.5, kappa=0.04, tw=120, tau_g=15, tau_p=25, Aext=0.02)
res=integrate(p,T=900.0,dt=0.1,A0=1.0,P0=0.45)
t,A,P,D,B=res['t'],res['A'],res['P'],res['D'],res['B']
fig,ax=plt.subplots(2,1,figsize=(8,6),sharex=True)
ax[0].plot(t,A,label='Stock A (trees / area)',color='#1f77b4',lw=2)
ax[0].plot(t,B,label='Biocapacity B = bA + b_G·G(A)',color='#2ca02c',lw=2)
ax[0].plot(t,P,label='Population P',color='#d62728',lw=2)
ax[0].set_ylabel('A, B, P'); ax[0].legend(loc='upper left',fontsize=8); ax[0].grid(alpha=.3)
ax[0].axvline(210,color='gray',ls=':',lw=1)
ax[0].annotate('boom: B & P rise\n(weak-sustainability / overshoot)',xy=(120,1.3),fontsize=8,color='#333')
ax[0].annotate('masking window\n(B peak while A dips)',xy=(210,1.1),xytext=(260,1.4),fontsize=8,
               color='#1f77b4',arrowprops=dict(arrowstyle='->',color='#1f77b4'))
ax[1].plot(t,D,label='Ecological debt D',color='#9467bd',lw=2)
ax[1].set_xlabel('time (yr)'); ax[1].set_ylabel('D'); ax[1].legend(loc='upper right',fontsize=8); ax[1].grid(alpha=.3)
ax[1].annotate('overshoot→debt→collapse\n(A hits extinction floor, P→0)',xy=(250,0.37),xytext=(420,0.34),fontsize=8,
               color='#9467bd',arrowprops=dict(arrowstyle='->',color='#9467bd'))
fig.suptitle('Implemented unified stock–flow model: overshoot → collapse (Paper N′)',fontsize=11)
fig.tight_layout(); fig.savefig('IMPLEMENTED_demo.png',dpi=120)
print("saved IMPLEMENTED_demo.png")
print("A0=%.3f -> Amax(peak)=%.3f @t=%.0f ; collapse to A_ext=%.3f at t=%.0f ; D peak=%.3f"%(
    A[0],A.max(),t[np.argmax(A)],A[-1],t[np.argmax(np.where(A<=0.03,0,0))],D.max()))
j=np.argmax(B); print("B peak=%.3f at t=%.0f (A=%.3f); B0=%.3f"%(B[j],t[j],A[j],B[0]))
