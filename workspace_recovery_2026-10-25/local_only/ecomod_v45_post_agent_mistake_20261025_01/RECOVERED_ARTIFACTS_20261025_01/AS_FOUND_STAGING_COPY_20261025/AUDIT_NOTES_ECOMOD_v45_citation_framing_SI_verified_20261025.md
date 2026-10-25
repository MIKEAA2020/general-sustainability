# Audit notes — v45 citation/framing and SI follow-up

**Checked against the final local build on 2026-10-25.** These notes distinguish direct companion support, manuscript scope, and sampled numerical checks; they are not a public release certification.

## Companion citations and claim scope

- **Key mapping preserved:** `Abaee2026a` = Paper4 governance; `Abaee2026b` = Paper06 assessment; `Abaee2026c` = Paper3 ledger. The later audit package's swapped mapping was not used.
- **Paper06 v71, Theorem 4(iii):** Read and checked against the companion's own witness-defined diagonal-gap region. It supplies exact intervals of diagonal-gap states falsely certified as safe for each positive elasticity. It does **not** entail the manuscript's former unqualified, general “no positive-elasticity aggregator is uniformly safe” claim. The revised main and SI prose explicitly localize the statement to the companion's witness-defined diagonal-gap region. Theorem 2 is separately cited for the finite-plan claim that no single available plan meets every component floor.
- **Paper3 metadata:** The reference pins the PDF path to public repository commit `2efaa62083f2007dec3446c15c475af88f0925f3`. The manuscript footnote states: `The labels conflict: PDF v50, README/checksum v49, and TeX header v48.` The commit-pinned URL, rather than the inconsistent version label alone, identifies the artifact.
- The Paper4 entry retains its governance title and v41 locator; the Paper06 entry retains its assessment title and v71 locator. Rendered main references show all three entries and the Paper3 commit URL; SI references show the correct `a`/`b` mapping.

## Framing and titles

- Main and SI agree on: **“Aggregate biocapacity does not identify its composition: a two-land model of ecological-capital drawdown.”** This is the result-style title requested in the review; no documented readability-pass decision justified switching to the mechanism-style alternative.
- Weak/strong sustainability framing is cited to Paper3 Sections 1.2 and 10.1 (not §1.1). It is described as an analogy about compensability, not an identity between ECOMOD's annual account total and the companion's material-flow ledger.
- The model's reservation is an **annual human-available-flow** reservation. Half-Earth is described as a **spatial conservation target**; the prose explicitly says the model neither maps protected areas nor evaluates that proposal.
- No broad boom–bust claim is made. The SI's delayed-logistic threshold statement is limited to the reported baseline `r τ_p = 0.5 < π/2`, rather than generalized to the coupled model.
- The removed “no Allee threshold other than the floor” statement was not restored. SI §S4.4 gives the correctness/trap rationale: the near-floor equilibrium has `A_c ≈ 0.0513`, `B = E`, and both restoration gates inactive.

## Numerical and cross-reference checks

- **Table S4:** Both `si_drawdown_depth.csv` and `si_drawdown_depth_current_quality.csv` contain `minAc = 0.050000000006867766 ha` at `A_c0 = 0.4 ha`, `P0 = 3.5 cap`; `0.050 ha` is the correct reported rounding. No `0.060` pattern-based replacement was made.
- **Monotonicity assessment:** On the deposited 0.1-cap grid (124 rows, four `A_c0` values, 31 `P0` levels), both minimum-area columns (`χ_r = 0.10` and `χ_r = 0`) are non-increasing with `P0` and non-decreasing with `A_c0` in each of the delayed- and current-quality CSVs; zero grid violations were found. The claim is supported on the tested grid (with plateaus at the typed floor). A discrete grid verifies sampled monotonicity; it is not, by itself, a proof of mathematical continuity between grid points.
- **Anchor:** `φ_0 = 0.12864722023747` is the cropland-biocapacity / total-biocapacity anchor; main text rounds to `0.128647` (about 12.86%).
- **Main Table 2(a):** Rendered on main p. 17. The `E_{ceil}` heading and baseline value `1.138 gha` are visible and legible.
- **SI links/layout:** Fixed-point reference is Eq. (18); §S4.2 explicitly points to SI Table S2 in §S3. Table S6 and its interpretation are together on SI p. 8. The final threshold-comparison sentence begins SI p. 7; SI p. 6 ends after the preceding complete sentence. Table S4 remains on p. 7.
- `\phi_0`, title, footnote, table captions, and page breaks were checked in the rendered PDFs. Earlier readability snapshots remain historical context and were not dismissed as stale evidence.

## Rendered QA and build

- Main PDF: 35 US Letter pages. SI PDF: 20 A4 pages. Tectonic 0.17.0, `--reruns 2`; packaged assembled TeX sources were independently compiled from the package directory with the included figures.
- Extracted final PDFs contain zero unresolved `??` markers. The TeX logs have no fatal build failure or undefined-reference diagnostics. Non-fatal warnings include one 2.608 pt overfull box during main-page output and underfull boxes; visual checks found no clipping or material disruption.
- Visually reviewed: main pp. 1, 3, 17, 21, 25, 27, 30–31, 35; SI pp. 1, 4, 6–8, 14, 20. Specific checks included the Paper3 disclosure footnote fitting on one line; the main title and SI title match; Table 2(a) and `E_{ceil}`; anchor; Theorem 4(iii) scope; Half-Earth distinction; Table S4's `0.050`; Table S6 layout; and the companion reference locators/links.
- Alleged `b_{c,c}` typo was not present in the inspected source/render. Table S1 uses `b_{G,c}`; Table S10 uses `Y_c = Υ_c(q) A_c`. No unsupported corrections were introduced.
- The latest SI source change (`\par\pagebreak` before the restoration-threshold comparison) was rebuilt and visually verified. The current package PDFs include that edit; the earlier output folder's generic intermediate PDFs were not retained in this named follow-up package.

## Release boundary

This is a local working follow-up only. It was not committed, pushed, or published. Public `main` and historical comparison packages were not changed. Packaging, checksum generation, or this local audit does not authorize any remote action.