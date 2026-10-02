# Compute the EXISTING committed v15's reactive families (A: C=phi*g(S); B: graded)
# under the same source-year machinery, to verify its claimed numbers.
from __future__ import annotations
import run_intervention_srcyear as base
import numpy as np
K_STAR=base.K_STAR; H=base.HORIZONS
FIT=base.fit_surplus(); R,K=FIT["r"],FIT["K"]
def g(S): return base.surplus(S,R,K)
GRID=[]
s=1.0
while s<1400: GRID.append(s); s+=25
s=1400
while s<base.S_HI: GRID.append(s); s+=200
GRID.append(base.S_HI); GRID=sorted(set(GRID))
UC={"UC_min":FIT["train_residual_min"],"UC_q05":FIT["train_residual_q05"],"UC_q10":FIT["train_residual_q10"]}
def mk(fn): return {"fn":fn,"thresholds":list(GRID),"label":""}
policies={}
for ph in (0.25,0.50,0.75):
    policies[f"A_phi{ph}"]=mk(lambda S,ph=ph: ph*g(S) if S>=K_STAR else 0.0)
def graded2(S):
    return 0.0 if S<K_STAR else (60.0 if S<1.25*K_STAR else 90.0)
def graded3(S):
    if S<K_STAR: return 0.0
    if S<1.15*K_STAR: return 30.0
    if S<1.35*K_STAR: return 60.0
    return 90.0
policies["B_graded2"]=mk(graded2)
policies["B_graded3"]=mk(graded3)

# BAU reference under source-year for comparison (from base)
bau=base.make_policies()["BAU"]
def b(pid,uc,T):
    pol=policies[pid]
    return base.boundary(base.kernel_inf_stable(pol,FIT,UC[uc],K_STAR) if T=="inf" else base.kernel(pol,FIT,UC[uc],K_STAR,T))
print("Existing-v15 Family A/B under source-year:")
print(f"{'policy':12s} {'q10T1':>8s} {'q10Tinf':>8s} {'q05T1':>8s} {'q05Tinf':>8s} {'minT1':>8s} {'minTinf':>7s} {'meanC':>7s}")
for pid in policies:
    s=base.supply_replay(FIT,policies[pid])
    print(f"{pid:12s} {str(b(pid,'UC_q10',1)):>8s} {str(b(pid,'UC_q10','inf')):>8s} {str(b(pid,'UC_q05',1)):>8s} {str(b(pid,'UC_q05','inf')):>8s} {str(b(pid,'UC_min',1)):>8s} {str(b(pid,'UC_min','inf')):>7s} {s['train_mean_C']:7.2f}")
# also report raw kernel lower boundaries at T=1 for q10 to compare
print("\nsupply:", {p:round(base.supply_replay(FIT,policies[p])['train_mean_C'],2) for p in policies})
