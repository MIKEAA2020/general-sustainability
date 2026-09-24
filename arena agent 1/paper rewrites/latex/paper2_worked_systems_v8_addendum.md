# Worked systems — edition 8 addendum

**Edition:** `paper2_worked_systems_v8` (tex/pdf/verify), replacing v7 per the new-editions-only protocol. **Trigger:** rigor-elevation directive. **Verification:** `paper2_worked_systems_v8_verification.py` — 32/32 checks (57/57 chained); build 0 overfull.

## Content (v7 → v8)

Seven propositions with proofs added (full table in `paper2_rigor_elevation_v1.md`): the **general review-timing law** (all \(z_0 \ge 1\), all integer deadlines — the 48-cell grid is its restriction), the **exact benchmark crossover** (\(Y \le 27/5\) iff input-feasible) with the **general margin law** \((Y - 27/5)/10\), **branchwise full-information decomposition** (kernel = the 28 corner-free pairs, via an explicit memoryless singleton policy), the **class lattice**, **register-semantics invariance**, the **authority-restriction zero lemma** (hand proof of the 0 side), the **two-floor saddle with uniqueness**, and **Helly sparse-witness** status. No claim was softened; no number changed; the verify script gains checks P1–P6 (dense-grid timing identity, benchmark crossover + margin identity, singleton verdicts + 24-step policy safety, unique saddle attainment, Helly pair points, authority zero).
