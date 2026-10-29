"""Gate 6 (REAL DATA) — the genuine National Footprint & Biocapacity series, 1961-2022.

Data: `data/nfa/GFN_world_biocapacity_footprint_population_1961_2022.csv`
      (total world biocapacity gha; total world footprint gha; world population).
      Source: National Footprint and Biocapacity Accounts, 2025 edition, World data.

Decomposition (total world, per year):
    B   = total biocapacity (gha)     bc = B/P  per-capita biocapacity (gha/cap)
    F   = total footprint (gha)       fc = F/P  per-capita footprint (gha/cap)
    R_B = F/B = fc/bc  (the macro-ratio / biocapacity ratio)

Identity (exact, per year):  d ln B = d ln bc + d ln P.

IDENTIFIABILITY LIMIT — now demonstrated from the DATA ITSELF: this public World data
gives total biocapacity, total footprint and population ONLY.  It does NOT give the
land-type (book) split between provisioning land and ecological capital, nor a separate
yield factor vs area.  Hence it CANNOT, by construction, separate the model's
`A_f` (provisioning) / `A_c` (capital-land) composition, nor yield from area.  That is a
concrete, data-structure instance of the identifiability result, not an assertion.
"""
import csv
import numpy as np


def load(path="data/nfa/GFN_world_biocapacity_footprint_population_1961_2022.csv"):
    rows = []
    with open(path) as f:
        for row in csv.DictReader(f):
            rows.append((int(row["Year"]), float(row["Biocapacity_gha"]),
                         float(row["Footprint_gha"]), float(row["Population"])))
    rows.sort()
    Y = np.array([r[0] for r in rows], float)
    B = np.array([r[1] for r in rows], float)
    F = np.array([r[2] for r in rows], float)
    P = np.array([r[3] for r in rows], float)
    return Y, B, F, P


def analyze():
    Y, B, F, P = load()
    bc = B / P
    fc = F / P
    RB = F / B                      # biocapacity ratio (footprint/biocapacity)
    print("== NATIONAL FOOTPRINT & BIOCAPACITY ACCOUNTS (world), 1961-2022 ==")
    print(f"years: {int(Y[0])}-{int(Y[-1])}  (n={len(Y)})\n")

    # Aggregate biocapacity
    dB_tot = 100 * (B[-1] / B[0] - 1)
    dlnBC_tot = np.log(bc[-1] / bc[0])
    dlnP_tot = np.log(P[-1] / P[0])
    dlnB_tot = np.log(B[-1] / B[0])
    print(f"AGGREGATE biocapacity B : {B[0]:.3e} -> {B[-1]:.3e} gha   "
          f"({dB_tot:+.1f}%; {dB_tot/(Y[-1]-Y[0]):+.3f}%/yr; d ln B = {dlnB_tot:+.4f})")
    print(f"PER-CAPITA biocapacity  : {bc[0]:.3f} -> {bc[-1]:.3f} gha/cap   "
          f"({100*(bc[-1]/bc[0]-1):+.1f}%; {100*(bc[-1]/bc[0]-1)/(Y[-1]-Y[0]):+.3f}%/yr)")
    print(f"Per-capita footprint    : {fc[0]:.3f} -> {fc[-1]:.3f} gha/cap   "
          f"({100*(fc[-1]/fc[0]-1):+.1f}%; d ln fc = {np.log(fc[-1]/fc[0]):+.3f})")
    print(f"Biocapacity ratio R_B   : {RB[0]:.3f} -> {RB[-1]:.3f}   "
          f"(E/B; <1 = surplus, >1 = overshoot)\n")

    # Overshoot onset
    said_agg = said_cap = False
    for i in range(1, len(Y)):
        if not said_agg and F[i] > B[i] and F[i - 1] <= B[i - 1]:
            print(f"AGGREGATE overshoot (F>B) begins: {int(Y[i])}  (R_B crosses 1.0)")
            said_agg = True
        if not said_cap and fc[i] > bc[i] and fc[i - 1] <= bc[i - 1]:
            print(f"PER-CAPITA overshoot (fc>bc) begins: {int(Y[i])}")
            said_cap = True

    # Identity / contribution split
    print("\n== IDENTITY d ln B = d ln bc + d ln P (per-year) ==")
    gB = np.diff(np.log(B)); gbc = np.diff(np.log(bc)); gP = np.diff(np.log(P))
    print(f"mean d ln B/yr = {gB.mean():+.4f}  =  mean d ln bc/yr {gbc.mean():+.4f} "
          f"+ mean d ln P/yr {gP.mean():+.4f} = {gbc.mean()+gP.mean():+.4f}   "
          f"(exact match: {abs(gB.mean()-(gbc.mean()+gP.mean()))<1e-9})\n")

    print("== CONTRIBUTION SPLIT over the whole period ==")
    print(f"d ln B = {dlnB_tot:+.4f}  =  d ln bc {dlnBC_tot:+.4f} (per-capita) "
          f"+ d ln P {dlnP_tot:+.4f} (population)")
    print(f"  population term = {100*dlnP_tot/dlnB_tot:+.0f}% of d ln B "
          f"(>100% => more than the whole rise); per-capita term = {100*dlnBC_tot/dlnB_tot:+.0f}%\n")

    print("== INTERPRETATION (honest) ==")
    print("Aggregate biocapacity rose only because POPULATION rose (+%.0f%%). In per-capita "
          "terms biocapacity HALVED (-%.0f%%). The 'aggregate biocapacity rose' reading is a "
          "population-scale artefact: it masks a -%.0f%% per-person decline, and the"
          "(more than the whole rise) population term +%.0f%% is offset by the -%.0f%% "
          "per-capita term." % (
             100*(P[-1]/P[0]-1), 100*(bc[-1]/bc[0]-1), 100*(bc[-1]/bc[0]-1),
             100*dlnP_tot/dlnB_tot, 100*dlnBC_tot/dlnB_tot))
    print()
    print("== IDENTIFIABILITY LIMIT (from the data structure) ==")
    print("This public World file gives total B, total F, and population only. It does "
          "NOT give the provisioning/capital-land (book) split, nor yield vs area. So it "
          "cannot, by construction, separate the model's A_f/A_c composition or yield from "
          "area. The two-book composition is NOT identifiable from this product alone; it "
          "requires independent land-cover (A_c, A_f) and FAO yield (b_f) proxies.")
    return dict(Y=Y, B=B, F=F, P=P, bc=bc, fc=fc, RB=RB)


if __name__ == "__main__":
    analyze()
