# Force units from the manuscript's OWN equations (no assumptions).
# Eq (2):  B = b*M.  M in gha.  B is an annual flow (gha/yr, the paper says so).
#   => [b] = (gha/yr)/(gha) = 1/yr = yr^-1.  (b is a rate; T(t) in yr^-1 matches.)
# Eq (3):  K = B/r_opt = (gha/yr)/(gha/cap/yr) = cap.  OK.
# Eq (5):  E = P*e.  P in cap, e in gha/cap/yr => [E] = gha/yr.  (E is a FLOW.)
# Eq (1):  dM/dt = rho M (1 - M/Mmax) - gamma E.
#   [dM/dt] = gha/yr; [rho M (...)] = (1/yr)(gha) = gha/yr.
#   => [gamma E] = gha/yr.  [E] = gha/yr  =>  gamma is DIMENSIONLESS.  (matches footnote 1)
# Eq (6):  dD/dt = max(E - B, 0).
#   [dD/dt] = [E-B] = gha/yr.   (rate of change of D = a rate)
#   => [D] = (gha/yr) * yr = gha.      <-- NOT gha*yr.  The yrs cancel.
# Eq (7):  b = b0 exp(-alpha D) + T.   [b]=[T]=yr^-1.
#   => exp(-alpha D) dimensionless => [alpha D]=dimensionless.
#   => [alpha] = 1/[D] = 1/gha = gha^-1.   (matches the manuscript "alpha (gha^-1)")
print("CONCLUSION (verifying the reviewer's comment b):")
print("  Under the manuscript's OWN convention, E and B are FLOWS (gha/yr).")
print("  Deficit per year = E - B  = gha/yr.")
print("  D = integral of a (gha/yr) rate over years  =>  D in gha  (not gha*years).")
print("  alpha in gha^-1.  So the manuscript's 'D measured in gha' and 'alpha (gha^-1)'")
print("  are MUTUALLY CONSISTENT and CORRECT.")
print()
print("  The reviewer's 'accumulation should be gha*years' is WRONG for a differential")
print("  equation dD/dt = E-B, because [dD/dt]=gha/yr, so [D]=gha (yr cancels).")
print("  (Analogous: cumulative money deficit = dollars, NOT dollar-years.)")
print()
print("  The reviewer is RIGHT, however, that the manuscript never explicitly states")
print("  B and E are per-year FLOWS. That omission is what invites the confusion.")
