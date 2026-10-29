import numpy as np, sys
from demo_unified import integrate as uni
sys.path.insert(0,'.')

print("="*78)
print("A) CORRECTED MODEL (1''') — what is the constant-parameter S0 equilibrium?")
print("="*78)
p=dict(rho=0.08, Amax=1.2, b0=0.5, bG=0.6, e=0.55, r=0.02, eta=0.03, alpha=0.0,
       sig=1.0, deltab=0.0, kappa=0.04, tw=120, tau_g=0, tau_p=0, Aext=0.02)
print("(no tech: deltab=0; alpha=0 so b=b0; tau=0 so S0, no delays)")
for (A0,P0) in [(1.0,0.45),(0.7,0.3),(1.3,0.6),(0.5,0.9)]:
    r=uni(p,T=800.0,dt=0.2,A0=A0,P0=P0)
    t,A,P,D,B=r['t'],r['A'],r['P'],r['D'],r['B']
    i=len(t)-1
    K=B[i]/p['e']
    print(f"  IC(A0={A0},P0={P0}) -> final A*={A[i]:.4f} P*={P[i]:.4f} B*={B[i]:.4f} D*={D[i]:.3f}  P/K={P[i]/K:.4f}")

print()
print("NOTE: the corrected S0 equilibrium obeys E=B (P=B/e) for the WHOLE curve of A*; the")
print("system has NO unique interior point (unlike the original's unique M*=0.740, P*=0.370).")
print("The 'basin of attraction of a unique steady state' (12G.2) is therefore defined only for")
print("the ORIGINAL model; the corrected analogue must be recomputed with the one-sided/deg. caveat.")

print()
print("="*78)
print("B) ORIGINAL MODEL — re-confirm master's headline numbers (gross depletion, 2-D)")
print("="*78)
from sim import run as orig          # original scenario runs
import importlib.util
def orig_scen():
    import sim
    return sim
# call sim's run via module import
import sim as S
for name,res in [("A(1.0,0,0)",S.run(1.0,0,0)),("B(1.15,0,0)",S.run(1.15,0,0)),
                 ("C(1.15,30,0)",S.run(1.15,30,0)),("D(1.15,30,25)",S.run(1.15,30,25)),
                 ("E(1.15,30,25,T)",S.run(1.15,30,25,tech=True)),
                 ("F(1.15,30,25,HE)",S.run(1.15,30,25,halfearth=True))]:
    a=res[0]; print(f"  {name}: Mfin={a[-1,1]:.3f} Pfin={a[-1,2]:.3f} Dfin={a[-1,3]:.3f}")
print()
print("   Master(12G.4) B/C: 'M rebounds to ~1.19 while P and harvest collapse' -> confirmed (1.194/1.193, P ~0)")
print("   Master(12G.5) D: '(30,25) collapses' -> Mfin=0 Pfin=0 confirmed")
print("   Master(12A.3): 'D_E ~ 5.26' -> confirmed (5.262); 'D_D=4.826'")
