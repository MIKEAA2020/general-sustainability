# E1 wave-4 record — paperE1_cod_forecast_ladder_v11.md (Task 73, orchestrator)

Build: `apply_batch7_wave4_e1.py` (fail-loud; every edit anchor asserted to appear exactly once;
abstract word count and table-row count pinned; rebuild from v10 is byte-identical — MD5
`02bf161ad952f3e6b70cda9fff851a04`, verified by the orchestrator across consecutive runs). 424
lines (v10: 368). All dispositions below verified against the v11 file by grep/read.

## The cite-vs-drop and wording decisions (owner directive: "cite, don't drop; decide on
appropriate wording before implementing")

| Item | Decision | Wording chosen (and why) |
|---|---|---|
| R1 [both — consensus 7; the record-vs-file failure] companions uncited | **CITE** | The four in-text companion mentions were already present in v10 (L36 Edwards Aquifer forecast-evaluation; L85 governance; L348 Edwards Aquifer again, freeze-discipline; L350 interval-verified linear template) with zero reference entries — the joint evaluation's loud finding. Decision: cite, not drop — the cross-paper linkage is the audit's own ask. Each mention now carries "(Author et al., in review)" / "(Author et al., in preparation)"; three reference entries added in alphabetical position (Author, A. — the Edwards forecast-evaluation study with its real title; Author, B. — the governance study; Author, C. — the interval-verified linear template), fresh letters per the repo's E-paper pattern. |
| R2 [both — consensus 6] the abstract's freeze claim vs §4's no-dated-protocol disclosure | **WEAKEN-WITH-CITATION** (neither keep nor drop) | The claim "fixed in the analysis scripts before execution" overstated the freeze discipline against §4's own disclosure. Decision: keep the discipline claim, scope it honestly at all three sites (abstract L16, §1 L32, §4 lead L348) to **"coded before the first scoring pass and applied unchanged"**, with the later passes "declared, not preregistered" — wording matched to what the freeze-discipline paragraph already discloses, so abstract, §1, and §4 now state one consistent fact. The comparison against the Edwards companion's dated protocol files is retained and made the explicit caveat ("a freeze-discipline caveat, recorded so that the evidentiary asymmetry between the two studies is visible"). |
| R3 [both — audit item A8, the docket's one new computation] | **COMPUTE-AND-REGISTER (post-freeze-labelled, non-destructive)** | The DM/Künsch layer is the one item the owner authorised as a new computation. Wording decision: every mention labels it a **post-freeze layer** that "attaches uncertainty to margins the point rule has already ranked; it changes no frozen verdict, score, or table value" — the negative certificate stays a point-rule finding ("weaker than a statistical null") and the new layer cannot promote or demote it. E3's §5.3.1 uncertainty layer was the template (same DM + HAC(h−1) + Künsch block max(h,3) conventions; E1's runs on its own margins and per-origin files). |

## Per-item disposition

| Item | Status | Evidence (v11) |
|---|---|---|
| R1 companions [both, consensus 7] | IMPLEMENTED (cite-don't-drop) | 4 in-text citation sites (L36, L85, L348, L350) + 3 reference entries (L384, L386, L388) — the record's false "companions cited" status is now true for the file |
| R2 freeze claim [both, consensus 6] | IMPLEMENTED (weakened at all three sites) | Abstract L16 + §1 L32: "coded before the first scoring pass and applied unchanged"; §4 L348 freeze-discipline paragraph keeps the full disclosure incl. the no-dated-protocol fact and the companion asymmetry |
| R3 (A8) DM/bootstrap [both] | IMPLEMENTED (the one new computation) | Definition 2.4 completed: H3 = the frozen RMSE pair at h=1 & h=5; H1 comparators declared (M1-for-M2, M3-for-M4, M1b the reported alternative); 5% tie band declared with the completion disclosed as "recorded at this revision, after the scores of Section 3 were computed: no recorded verdict depends on them" (L129). New §3.5 (L285–289+) + Table 9 (32 rows: 8 per spec×horizon) + Diebold–Mariano 1995 / Künsch 1989 references + Data-availability registration of the script and CSV (L362) |
| R4 [grok] 1898-kt in abstract | IMPLEMENTED | Abstract L18: "on the extended 1954–2024 specification official landings drive the stock-flow module's collapse-window error to 1898 kt" |
| R5 [claude] log-score floor | IMPLEMENTED | Limitations L342: ε_log = 10⁻³ kt, the trajectory clip [ε_log, 10⁶] kt, "distinct from the process noise ε_t of Definition 2.1", per-origin floor-hit counts (15/25 M1 and 17/25 M1b at h=1; 19/21 at h=5; Specification B 22/59, 24/59, 36/55, 46/55; M2/M3/M4 between 0 and 11) |
| R6 [claude] "No module M2–M4 is retained" | IMPLEMENTED | "No structural model" (abstract L10/L18; Highlights; §3 sites) — the module-ladder reading and the model-family reading no longer conflate |
| R7 [claude] Def 4.2 → Methods; Funding; abstract's mixed range | IMPLEMENTED | Definition 2.5 (Negative certificate) at L131 in Methods with the machine layer defined; Funding section at L374 (submission placeholder, CRediT pattern); abstract L18 "across both catch treatments" (115–206 mixes Table 4/5 no longer implied) |
| A8 retention-rule completion (Def 2.4) [both] | IMPLEMENTED (part of R3 above) | L129: the two disclosures — the point-rule-not-a-test caveat and the completions-recorded-at-this-revision caveat with the 17% smallest-deficit check |
| Docket: methods/Def-4.2/funding items | IMPLEMENTED (as R7) | — |

## The R3 computation — registration and results

- Script: `batch 7 (audits of agent arena 1 paper rewrites)/campaign_e1_dm_uncertainty.py`
  (seed 0; 20,000 Künsch moving-block replications; DM with unweighted HAC truncation at lag
  h−1; block length max(h,3)). Deterministic: re-executed by the orchestrator; the output CSV
  regenerates byte-identically (MD5 `a29a878c75c7f40a182bdeb4a2d7d9b9`).
- Inputs: the archived per-origin forecast files (Specification B: the xteNCAM rolling file;
  Specification A: the annual-landings pass of §3.2 — the coarse-regime pass's per-origin rows
  are not archived, its summary is, and the verdicts coincide under both treatments). The
  persistence baseline is recomputed on the identical origin sets from the registered series and
  asserted against the recorded origin-matched values (98/265 kt on A; 84/300 kt on B) — the
  script fails loudly on mismatch.
- Results (Table 9, 32 rows): on **Specification A** every non-retention margin against
  persistence is within noise (bootstrap p = 0.19–0.93 at h=1; 0.27–0.76 at h=5) — the point-rule
  non-retention stands as a point ranking, not a statistically separated one, which §3.5 now
  states; on **Specification B** every margin against persistence separates (p = 0.032, 0.009,
  0.0001, 0.042, <0.001 at h=1; all ≤ 0.03 at h=5). Structural-vs-structural margins on B are
  mixed (M2 vs M1 p = 0.17; M4 vs M3 p < 0.001; M2 vs M1b p = 0.77).
- Wording in the paper: the layer "attaches uncertainty to margins the point rule has already
  ranked; it changes no frozen verdict, score, or table value" (§3.5 lead and the Definition-2.4
  disclosure), and the abstract's one-line reading ("all non-retention margins are within noise"
  on A, "every margin against persistence separates" on B) is carried in the version log and §6.

## Non-destructiveness

Tables 1–8 byte-identical (77 rows before; Table 9's 32 rows are new); no frozen verdict, score,
kernel, or spectral record changed; the abstract is exactly 300 words (pinned); Highlights
unchanged except R6's relabel; the reproducibility statement gains only the §3.5 registration
sentences. The build script enforces the abstract length and the table-row counts mechanically.

## Declines and notes

- None for E1's R1–R7 — every item is implemented. The two audit asks NOT taken in this wave
  remain the registered methodological items from the wave-2 docket that need new computations
  beyond the authorised R3 (they stay registered, with reasons, in WAVE2_IMPLEMENTATION.md's E1
  section): none of them was jointly endorsed as a one-line fix.
- Rose (2026) / the frozen 2026-09-01 plan date: not E1 items — resolved-by-clock, untouched
  (machine-checked by the wave-3 pass).
