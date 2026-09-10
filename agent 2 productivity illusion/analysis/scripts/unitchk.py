# Dimensional audit of the model as the manuscript defines it.
# From the manuscript text:
#  M : gha (stock), dM/dt : gha yr^-1
#  E : gha yr^-1  ("gha per year")  -> footnote 1
#  B : gha yr^-1   (annual regenerative flow)
#  e : gha cap^-1 yr^-1
#  r_opt : gha cap^-1 yr^-1
#  rho, r : yr^-1
#  b = B/M : (gha yr^-1)/(gha) = yr^-1           (Eq 2)
#  K = B/r_opt : (gha yr^-1)/(gha cap^-1 yr^-1) = cap   (Eq 3)
#  E = P*e : cap * gha cap^-1 yr^-1 = gha yr^-1    (Eq 5)
#  Eq 6:  dD/dt = max(E - B, 0)
#         so [dD/dt] = gha yr^-1
#         so [D] = gha yr^-1 * yr = gha yr   (gha-years)  <-- KEY
print("D = integral(E - B) dt")
print("  [E]=[B]= gha yr^-1; dt = yr  => [D] = gha*yr  ('gha-years')")
print()
print("Eq 7: b = b0 exp(-alpha D) + T ; [b] = yr^-1")
print("  exponent alpha*D must be dimensionless")
print("  [alpha] = 1/[D] = (gha yr)^-1 = gha^-1 yr^-1")
print("Manuscript says: D 'measured in gha',  alpha '(gha^-1)'  -> INCONSISTENT")
print()
print("Sanity check alternative: if E,B were pure gha (not yr^-1),")
print("  dD/dt=max(E-B,0) would have units gha, but it's written *dD/dt*,")
print("  so a time derivative => D would be gha*yr. Same conclusion.")
