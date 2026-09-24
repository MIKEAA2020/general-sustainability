# Worked Systems, Edition 4 — Addendum

**Editions:** supersedes `paper2_worked_systems_v3` (v1–v3 retained in the archive). Same title, same author, same register; the audit frame and all v3 results are carried in full and unchanged.

**Content delta (v3 → v4), implementing the depth directive:**

- **The master table (Table 1, full width):** all 36 belief pairs × the five audited kernels (institutional, aggregate, full-information codex, full information, decentralized), every entry script-regenerated; the kernel counts become column sums.
- **The 16 sustaining law pairs (Table 2):** the decentralized sustainers of the audited pair shown to factor exactly as a 4 × 4 product (forced votes on the reachable coordinates, free votes on z ∈ {0, 3}).
- **The 48-cell timing grid (Table 3) + Figure 2:** the predicate column, the audited column, six viable cells, zero mismatches, the strict-form failure isolated at (2.0, 1).
- **The fifteen-partition census (Table 4) + Figure 3:** each partition with each fibre's exact common safe-action set; the failing-fibre reading at fibre level (adequate ⇔ no fibre merges (1,2) with (2,1) or (3,1)).
- **Benchmark (Table 5, Figure 4), drift (Table 6), static duality (Figure 5):** the cap arithmetic on six aggregates with the witness and the dual margin 3/50 (cap-sum shortfall 3/25 stated separately); the drift table s/5 + 1/100 with 1/20 increments; the duality figure with the constant Farkas mix.
- **Figure 1:** the four-class Boolean product with the meet/join reading.
- **Two sharpenings found while tabulating:** at kernel level the union of the two middle kernels falls exactly one pair (12|21) short of the full kernel — the alternation-forced pair, named and characterized; the census failing-fibre characterization above (v3's prose carried the (2,1)-only form).
- **Section cross-references now print true numbers** (the v1–v3 template left them unresolved on the page; recorded in roadmap v23 as a template fix applied going forward).

**Verification:** `paper2_worked_systems_v4_verification.py` 21/21 — chain 57/57 (seven lineage scripts), plus independent recomputation and full projection of every printed table (36×5 master marks, 16 timing rows, census, benchmark, drift, the 4 × 4 law product). `paper2_worked_systems_figures.py` regenerates the five figures from asserted exact data (6/6 data checks). Build: 6 pages, zero overfull.

**Process notes of record:** three defects caught by verification or page inspection before shipping — two arithmetic slips in drafted table cells (57/25; 3/25 vs the certificate margin 3/50) and one false census characterization in draft — each root-caused and fixed to the recomputed truth; matplotlib savefig-placement and layout defects caught by rendering inspection.
