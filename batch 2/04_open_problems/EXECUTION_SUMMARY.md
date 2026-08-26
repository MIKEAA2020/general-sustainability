# A1→A3→B4→C-a Execution Summary

> **Post-transfer-audit addendum:** see `/TRANSFER_AUDIT_RESPONSE.md` for the repair of the three later audit findings (proof expansion, E5 scope, schema control). The corrected statuses in this summary remain in force; the theorem files it references now contain full reconstructed proofs.

> **STATUS CORRECTION:** The original summary used inflated statuses. The authoritative reclassification is in STATUS_CORRECTION.md. A1=COMPUTED_PARTIAL; A3=COMPUTED_PARTIAL (toy); B4=COMPUTED_PARTIAL (discrete); C-a=PROVEN at declared scope.

## Committed computational artifacts

| Computation | Result | File (committed) |
|---|---|---|
| A025 Hopf certificates | τ± reproduced (interval, dps=50) | `a025_fold/a025_interval_hopf.json` |
| C4 orbit Krawczyk | Unique orbit in 1e-8 box, margin 1186 | `a021_c4/c4_orbit_krawczyk_certificate.json` |
| C4 off-grid residual | INTERVAL-CERTIFIED: N≤6.6e-8, Z≤8.3e-7, E≤2.8e-6 | `a021_c4/c4_offgrid_residual_interval.json` |
| C4 monodromy (dt=0.25) | Phase simple+neutral; dominant 0.688+0.069<1 | `a021_c4/c4_monodromy_enclosure.json` |
| C4 monodromy (dt=0.1) | Second mesh level: dominant 0.6869+0.066<1, mesh-stable | `a021_c4/c4_monodromy_dt0p1_enclosure.json` |
| A025 fold (nominal, m=64/96/128) | tau_f = 5.5872361986… — all three inside the lost certificate interval | `a025_fold/a025_branch_continuation*.json` |
| E5 module admission | Five maps + interval-verified constants | `E5_NUMBERS.json` |

## Wave E candidate support (all NOT CONFIRMED)

| Need | Candidate | Status |
|---|---|---|
| Paper 4: certified computation | A1 (discrete K=80 PROVEN) | NOT CONFIRMED |
| Paper 4: NAIM capstone | B4 + A2 | NOT CONFIRMED |
| Paper 5: governance template | A3 | NOT CONFIRMED |
| Paper 5: computability | C-a | NOT CONFIRMED |

See PROOF_MANIFEST.md “Reproducibility status” (disclosure consolidation) for the full certification-level breakdown.
