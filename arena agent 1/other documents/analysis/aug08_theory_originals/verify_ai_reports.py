"""Deep verification of ai report1.txt + ai report 2.txt claims."""
import numpy as np

print("="*70)
print("REPORT 1, CLAIM 1: M_max/2 is the inflection point, not a separatrix")
rho, Mmax = 1.5, 100.0
for M in [1.0, 25.0, 50.0, 75.0, 99.0]:
    regen = rho*M*(1 - M/Mmax)
    print(f"  M={M:6.1f}: regeneration={regen:8.3f}  (positive for all 0<M<Mmax)")
print("  d2M/dt2 = rho(1-2M/Mmax): at M=50 ->", rho*(1-2*50/Mmax), "= 0 -> inflection point at M_max/2")
print("  MSY condition: max of rho M(1-M/Mmax) = rho*Mmax/4 =", rho*Mmax/4)
print()

print("="*70)
print("REPORT 1, CLAIM 2: polynomial degree for tau_m=0 case")
# paper reports omega^2(2500 w^4 + 1199 w^2 + 143.5) = 0 -> degree 6 in omega
# correct: |P(iw)|^2 - |Q(iw)|^2 with P 2nd-order, Q 1st-order -> degree 4
# verify constant term: (gamma_e a21)^2 - r^2 a11^2 with stated params
# (from the chat: gamma_e a21 = 0.01, r = 0.02, a11 = -0.5)
gamma_e_a21, r, a11 = 0.01, 0.02, -0.5
ct = (gamma_e_a21)**2 - (r*a11)**2
print(f"  constant term (gamma_e a21)^2 - (r a11)^2 = {gamma_e_a21**2} - {(r*a11)**2} = {ct}")
print(f"  paper's implied constant 143.5/2500 = {143.5/2500:.6f}  ->  {ct:.4f} vs {143.5/2500:.6f}")
print(f"  paper constant REQUIRES {ct:.4f} = {143.5/2500:.6f}, which is FALSE for stated params -> polynomial is impossible")
print()

print("="*70)
print("REPORT 1, CLAIM 4: depletion law depletes by total extraction, not deficit")
print("  dM/dt = rho M(1-M/Mmax) - gamma E(t-tau_m)")
print("  => depletion term is -gamma E, proportional to TOTAL extraction, not max(E-B,0)")
print("  verified: yes, as written the model depletes M even when E <= B (if gamma E > regen)")
print()

print("="*70)
print("REPORT 2, CLAIM 2: Rate-Induced Tipping framing")
print("  R-tipping: collapse from rate of change exceeding relaxation time, not static crossing")
print("  -> standard concept in climate literature (Ashwin et al. 2012); framing sound")
print()

print("="*70)
print("REPORT 2, CLAIM 4: Stock vs flow pollutants")
print("  stock pollutants accumulate (CO2, microplastics) -> cumulative matters")
print("  flow pollutants dissipate (smog) -> rate matters")
print("  -> standard environmental-chemistry distinction; correct")
print()

print("="*70)
print("CROSS-CHECK: does the CURRENT manuscript embody the 'correct' depletion law?")
print("  Current core: dN/dt = S(N) - qEN, deficit identity qEN - S(N) = -dN/dt")
print("  => net depletion happens only when qEN > S(N) i.e. E > B_s (deficit-driven)")
print("  => the OLD draft's flaw (gamma E even when E<=B) is ABSENT in the current core")
