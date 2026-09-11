# Paper 5 audit-sweep verdict record (v42)

Date: 2026-09-12. Scope: every actionable item in the three audit files
(`audit of p5.txt`: deepseek sections 1-4 + qwen sections 1-5;
`author blocked.txt`: deepseek A3/A5/A6/A8-A11 + qwen A3/A5/A6/A10/A11;
`qwen p5 rewrite.txt`: journal-fit review, operative sections 1 + 3.1),
checked against the v41 manuscript + supplementary v17. Method: targeted
re-read of each audit body, then verbatim/regex verification in the v41
sources. Verdicts: DONE (implemented in v41 or earlier), V42 (fixed in
this version), HOLD (deliberately not implemented, rationale recorded).

## 1. audit of p5.txt — deepseek

| Item | Verdict | Evidence / rationale |
|---|---|---|
| 1.4 lineno + date + version | DONE | lineno package, `\date{September 12, 2026}`, version in filename + source comment |
| 1.5 figure file | DONE | 5 figure envs, all files in `figs_p5/` |
| 2.1 App-A opener vs 2.2 | DONE | opener lists 2.2, 2.4, 2.5, 3.3, 3.4 |
| 2.2 protective convention | DONE | 2.1 gives the quota-tracking law as equation and states it is the sign-reversed implementation |
| 2.3 three/four systems | DONE | "three groups illustrate" |
| 2.4 four-state period | DONE | 15-25x comparison dropped; four-state loop defined with centuries-scale timescales |
| 2.5 S(N) equation ref | DONE | "defined after equation (2)" |
| 2.6 crossing precision | DONE | precise values only (47.536, 79.143) |
| 3.1 C_E=0 case | DONE | limit branch stated with deviations defined |
| 3.2 eligibility criterion | DONE | 2.4: 58-stock panel + n>=20 filter, lengths 20-77 yr |
| 3.3 detrending rule | DONE | 2.4: linear trend (+ variants in S9.1) |
| 3.4 null calibration | DONE | 2.4 + S8 deposits + S9.1 battery |
| 3.5 section numbering | HOLD | non-standard but house convention across all versions; submission template conversion is author-side |
| 3.6 abstract env | DONE | well-formed |
| 3.7 "annual discrete form" | DONE | reworded |
| 3.8 rational term edges | DONE | sign-beyond + projection-does-not-repair + exact-contextual containment; Table 3 pins Zref=1 |
| 3.9 6.5 vs 6.501 | DONE | approximate in abstract, precise in body (standard) |
| 3.10 window-edges scope | DONE | scoped to the one-plant contrast |
| 3.11 lambda note | DONE | "derived eigenvalue, not a parameter" |
| 3.12 Box 1 row | DONE | old Box 1 moved to supp; new Box 1 = management-regimes box |
| 3.13-3.26 | DONE | all "Good" as audited; spot-verified present |
| must-fix 1-10 | DONE | title/author/preamble, 196-line References, declarations incl. AI declaration, App-A opener, protective convention, four-state characterisation, S(N) ref, three-groups, lineno+date, precision/C_E=0/annual-form |

## 2. audit of p5.txt — qwen critical (2.1-2.10)

| Item | Verdict | Evidence / rationale |
|---|---|---|
| 2.1 archived stage centrality | DONE | Option B executed: bands prespecified + provisional-carry disclosed in 2.4/3.5 + alt-band screens (S11.4); post-hoc redefinition rejected as HARKing (recorded) |
| 2.2 parameter vector | DONE | Table 3: full vector, k, fixed point + interiority, gains, crossing angle, lambda, closed-form/FD-step rows, solver + IEEE-754 + 50-digit certificate |
| 2.3 annual-instability strength | DONE | operator-scoped, numerically conditional verdict + margins paragraph |
| 2.4 Euler "artefact" | DONE | "dynamically real for an Euler-rule institution; artefacts only relative to the exact update" |
| 2.5 held vs interpolated | DONE | H4 + "main model takes E(t)=E_n; proposition stated for the hold-or-interpolate class" |
| 2.6 exact update spec | DONE | deviations defined, both C_E branches, end-of-period held assessment stated, "analytical, not a proposed institutional rule" |
| 2.7 screen detail (12 items) | DONE | 2.4 + deposits (IDs, code, periodograms) + S9.1/S11 (endpoint-trim in S11) |
| 2.8 power vagueness | DONE | formal P(reject\|signal) + Cohen + grid + deposits; full config S13.1 |
| 2.9 case inventory | DONE | `u5_case_table.csv` (per-system x c1-c4 + binding_fail + evidence) + S4 entries |
| 2.10 constrained-M | DONE | "listed as open problems... hypotheses, not results"; typo gone; quantities + requirements in S13.2 |

## 3. audit of p5.txt — qwen consistency (3.1-3.10)

All DONE: 3.1 one-plant contrast titled in 3.4; 3.2 "trajectory-classified only" status sentence;
3.3 multiplier types incl. 47.536 complex pair + NS signature; 3.4 Tr>=34 discrepancy explicitly
discussed (biomass-converged/weak, effort grows); 3.5 Tr=10 cell labelled disagreement, not used
inferentially; 3.6 fixed-plan "baseline rest point" verbatim; 3.7 protective equation + projection;
3.8 "not an empirical rejection" verbatim; 3.9 "The 3.7 yr catch periodicity is not a review
interval" verbatim; 3.10 q-row cites stage Plant paragraph + full vector listed.

## 4. audit of p5.txt — qwen math/logic (4.1-4.9) and empirical (5.1-5.8)

| Item | Verdict | Evidence / rationale |
|---|---|---|
| 4.1 S notation overload | HOLD | documented in 3 places (notation para, Table 4, 2.7 scoping); full rename = high churn/risk for a section-scoped, documented convention |
| 4.2 F_B positivity | DONE | restrictions + "well defined on the admissible state space" |
| 4.3 Phi_k shift delta | DONE | value + sign + interiority in Table 3; delta and tau_m rows in S11.1 battery |
| 4.4 rapid-review Re(lambda) | DONE | real-parts formulation |
| 4.5 "monodromy" term | DONE | defined once (Table 4 + 2.1), used consistently |
| 4.6 Prop 3.1 scope | DONE | "admissibility only" sentence (audit's either-or) |
| 4.7 a(E)=0 caution | DONE | limit branch used when \|a(E)\|<1e-12 |
| 4.8 Lemma C>0 | DONE | verbatim |
| 4.9 Schaefer limit | DONE | formal-limit wording |
| 5.1 band justification | DONE | S11.4 alt-band screens, all zero |
| 5.2 effort-band resolution | DONE | per-record accounting; unresolvable-on-all-42 stated in 3.5 + S11.4 |
| 5.3 AR(1) simplicity | DONE | 11-variant battery + 4.7(iv) clause |
| 5.4 criterion iii | DONE | comparative rule inline (outperform pre-registered alternatives) |
| 5.5 zero-count framing | V42 | body + 4.7(v) already carried the discipline; heading renamed to "Structured case search: no qualifying cases" |
| 5.6 Iceland precision | DONE | S4: windows, source, vintage comparison, no-detrend stated, CV + periodogram method |
| 5.7 anchoveta multiplicity | DONE | "The ninety index-lag cells are the BH family. The Granger tests are confirmatory and outside it." |
| 5.8 cod covariates | HOLD | single sentence with "descriptive inputs, not causal tests" disclaimer; relocation = churn without evidential gain |

## 5. author blocked.txt

| Item | Verdict | Evidence / rationale |
|---|---|---|
| A3 disclosure split | DONE | Table 3 = primitives + fixed point + interiority + gains + theta0 + lambda + solver; numerical/sensitivity detail in S-tables; positivity as main-text sentence |
| A5 archive role | DONE | supplement-kept; tau0 decomposition cited with numbers + generating scripts; bands verdict = Option B (recorded) |
| A6 registration materials | DONE | Path A executed: stock IDs, eligibility designations, detrending code, power spec + seeds, periodogram deposit, case inventory all deposited and cited |
| A8/A9 keep/leave | DONE | scope rules applied through the v41 demotion |
| A10 structure | DONE/HOLD | deepseek rule (cut non-load-bearing) executed in v41; qwen App-B drop HELD: App-B carries the venue-fit distributive content linked from 4.6, not an unlinked ornament |
| A11 AR(1) checks-or-clause | DONE | both: clause in 4.7(iv) + ARMA/bootstrap/regime checks in S9.1 |

## 6. qwen p5 rewrite.txt (journal fit)

NatSustain 3.1 items 1-7: DONE (decision-clock reframe + verbatim suggested title; broad
first paragraph; demotion of proofs/monodromy/Euler/stage/evidential-table to Methods-App/Supp;
Box 1 regimes + Box 2 design principles + TAC/HCR/multi-year/emergency real instruments;
nulls-as-falsification-discipline framing; 6.5 illustrative everywhere). Obstacles 1-5:
DONE (reframed nulls, moved guards, demoted bulk, conditional margins, perverse-pressure
justification with Sumaila/WTO). PNAS portable items: DONE except one-illustration (HELD:
integration is the thesis per standing structural decision). Other journals' sections:
venue-N/A (NatSustain chosen). Author-side residuals: presubmission inquiry, Zenodo DOI
at submission, companion paper.

## 7. Changes in v42 (+ supp v18)

1. Figure paths `../figs_p5/` -> `figs_p5/` (compile convention).
2. Spectral-margins + undelayed-limit paras: theta/lambda pointers updated to Table 3.
3. Section 3.7 heading rename (5.5).
4. Supplementary pointer: stale `paper5_supplementary_v12.md` filename -> version-free pointer.
5. Supp v18: S4 anchoveta working filenames -> deposited equivalents
   (`peru_anchoveta_catch_sau.csv`, `sau_taxa600004_reporting.json`).
No science changes; no new records.

## 8. Repo completeness ( checked 2026-09-12)

Mains v25-v41 tex + PDFs v25-v30; supps v2-v17; builders v27-v41/v6-v17;
figs_p5 7/7; originals 86 files covering every S8/App-A citation; nscircle in
originals; rwin/tau0 in rerun_outputs; anchoveta battery + inputs in
anchoveta_enso/. After this push: + v42 tex + v42 PDF + supp v18 + builders +
this record. No GitHub-Releases artifact workflow in this project; pushed = released.
