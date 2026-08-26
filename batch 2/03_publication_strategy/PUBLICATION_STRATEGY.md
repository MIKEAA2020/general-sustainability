# Joint Publication-Strategy Assessment

**Objective:** as close to a general theory of sustainability as the mathematics supports; seamless retention of all valid/repairable content; optimal paper count, leaning toward fewer when in doubt.

## The recommended architecture

**Five journal papers, one monograph, one versioned compendium** — down from 5 + likely 6 + potentially 7 + domain papers.

| # | Paper | One-line question | Session additions |
|---|---|---|---|
| 1 | General Theory: Typed Architecture, Boundary, and Scope | What does the typed general theory claim, prove, and refuse? | + Stackelberg equilibrium existence (B10) in the institutional section; + the strategic-implementation docket as the acknowledged boundary |
| 2 | Theorem Atlas: Viability, Observation, Composition, Scale, Generation | Which theorem families are established, under which assumptions? | + Nonlinear assume–guarantee composition (A4); + sampled-data erosion theorem (B1); + stochastic viability layer — chance-kernel recursion, filter soundness, quantile erosion (B9); + decidability at fixed data (C-a); + quadratic-form moiety barriers (C-e); + RFDE-aggregate memory (C-f) |
| 3 | Conserved Ledgers, Componentwise Diagnostics, Conservation–Viability Coupling | What do conservation laws buy for safety? | + **E7 as the paper's bridge theorem**: the moiety-barrier sandwich computed from flux data alone; + E5's interval-verified numerical admission as the worked example — **method demonstration on the linear A001 §§6–10 module only; no transfer to either real system (the 2J3KL cod fishery or the Edwards J-17 aquifer system) or any other model without the R04 five-map certificate (not constructed)** |
| 4 | Delay-Driven Institutional Dynamics: Hopf, Validated Folds, Cycle Stability | How do delayed channels generate cycles with certified facts? | + committed interval-certified Hopf certificates (A025); + committed orbit Krawczyk (margin 1186); + committed interval-certified off-grid residual; + committed monodromy/Floquet (dt=0.25); fold pipeline script committed (computation incomplete) |
| 5 | Sampled Governance, Closed-Loop Certification, Empirical Falsification | How can the theory be tested? | + sampled-data erosion theorem (B1) closes R02.Cor6's bridge; + decidability theorem (C-a) guarantees computability at fixed data on the finite class (TCS-1.0 language); + the E5 admission template for case screening — **template only: the linear toy's numbers support no real-system claim (R04 forbids transfer)** |

## Proposed consolidations (editorial defaults — **proposals, not gates**)

> **Status correction (follow-up audit):** the folds below are the strategy's *editorial defaults*, not verified decisions and not Wave-0 gates. The Paper 6 fold is doubly contingent: the NAIM persistence capstone it would fold into is **NOT CONFIRMED** (PROOF_MANIFEST.md Part III), the A025 fold pipeline is **NOT REBUILT**, and the A1 continuum lift is COMPUTED_PARTIAL. Final fold decisions are made at Wave-0 close (independent rerun + spec match), not before.

- Paper 6 (A021 NAIM) folds into Paper 4's capstone **(proposed default — contingent on the capstone content becoming confirmed)**
- Paper 7 (stage/spatial) folds into Paper 4's supplement **(proposed default)**
- Domain papers fold into Paper 5's single closed empirical case (G1) **(proposed default)**
- E5's resource–sink admission serves Papers 3+5 — **as method demonstration / screening template on the linear module; the real-system tracks additionally require the R04 admission of the corresponding scored model or a Cor2 approximate admission, neither constructed (see TRANSFER_AUDIT_RESPONSE Finding 2 and the three-object table below)**

## Real-system referents — **three distinct objects (do not conflate)**

The earlier shorthand "2J3KL/J-17-class systems" collapsed three different objects and is **retired**. The transfer prohibition (R04.Thm1's converse) applies to each of them separately:

| Object | What it is | Programme locus | Kind | R04 five-map | Cor2 | Independent rerun |
|---|---|---|---|---|---|---|
| **NAFO 2J3KL** | Northern cod SSB. Scored \(\Omega_{2016}\), \(\Omega_{\mathrm{xte}}\) | [`wave_e_cod/`](../../wave_e_cod/) | Real system — fisheries | A001 admitted; A014 at corrected status. E5 toy does **not** transfer | not constructed for the surplus ladder | **NONE** |
| **Edwards well J-17** | San Antonio Pool index well (TWDB 6837203). Scored \(\Omega_{\mathrm{SA}}\) | [`wave_e_edwards/`](../../wave_e_edwards/) | Real system — groundwater | two-pool **not** constructed | H0 forecast-map `APPROXIMATION` in `wave_e_edwards/admission/R04_Cor2_edwards_H0.md` — **not** a kernel certificate | **NONE** |
| **A021 C4 J-series** | Docket J01–J25 (J17 = BLZ citation item). Not a basin | `research_program/external_reviews/A021_joint_decision_docket.csv` | Audit docket + programme DDE | not constructed from the E5 toy | not constructed | **NONE** (artifacts committed) |

There is **no** manuscript in this repository that rejects Edwards on a “confound gate.” That phrase is withdrawn. Scored RMSE is not a transferred judgment.

Reproduce: `wave_e_cod/` — `python3 src/run_ladder.py`. `wave_e_edwards/` — `python3 src/run_ladder.py && python3 src/run_recharge.py` (uses the committed `data/annual_panel.csv`, which already carries all derived columns — the reproduction path verified end-to-end in `batch 4/WAVE_E_RERUN.md`). **Do not** run `build_panel.py` first: it silently overwrites the committed 20-column panel with a 15-column version (dropping the climate columns) and `build_climate.py` then exits 1 without the uncommitted nClimDiv raw file (URL in `wave_e_edwards/data/SOURCES.md`) — the rebuild path is recorded separately in `PROOF_MANIFEST.md` Part VI (WAVE_E_RERUN findings F4/C2).

## Gap-filling agenda (G1–G6, updated statuses)

| Item | Original status | Updated status |
|---|---|---|
| G1: one closed empirical instantiation | Top priority | E5 method template committed (toy numbers). Scored forecast \(\Omega\) are in `wave_e_cod/` and `wave_e_edwards/` (persist / thin M1). Kernel transfer still gated. Independent rerun **NONE**. A021 J-series is a docket, not a system |
| G2: A021 coupling class | Open (author decision) | **DECLARED** (LIEBIG-SANCTIONED-COUPLING-v1; discrete-level hypothesis verification; conditional on A1) |
| G3: continuum lift | Open | **COMPUTED_PARTIAL** (piecewise-Chebyshev route specified, NOT EXECUTED) |
| G4: selector regularity | Open | **Half-proved** (measurable selection PROVED; continuous selection conditional on Michael class) |
| G5: external novelty audit | Open | Matrix exists (E6); **execution NOT DONE** |
| G6: TCS-1.1 freeze | Open | **FROZEN (diff only — NOT controlling)**: TCS-1.0 controls every existing record; the migration is an open Wave-0 obligation; no record is TCS-1.1-compatible |

## Release waves

| Wave | Content | Prerequisites |
|---|---|---|
| 0 | Closure: G6 diff frozen (migration **not** done — TCS-1.0 still controls), G5 (external audit), artifact manifests, **independent rerun of all committed computations**, **R04 admission certificate for the real-system tracks (G1 gating; see the three-object table)** | The independent rerun is the single gating item (see HONEST_DISCLOSURE.md); the G1 real-system transfer is the empirical gating item |
| 1 | Papers 1+2 (the theory dyad) | Wave 0 complete |
| 2 | Papers 4, 3, 5 (in readiness order) | Wave 1 complete; Paper 5 additionally gated on G1 |
| 3 | The monograph | Papers 1–2 through external scrutiny |

## Critical rule

**No gate is treated as closed for Wave E without spec matching and independent verification.** Every Wave E support row is NOT CONFIRMED until the frozen specification (S, Ω, y_t, T, scoring rule) is matched against the computation artifacts. See HONEST_DISCLOSURE.md and PROOF_MANIFEST.md Part III.
