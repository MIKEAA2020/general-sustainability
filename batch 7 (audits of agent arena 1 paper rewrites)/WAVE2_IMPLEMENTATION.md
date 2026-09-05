# Batch-7 Wave 2 — Remaining-Points Assessment and Implementation (Task 71)

**Date:** 2026-09-06 (this repo's clock). **Owner directive:** (1) fix the registered
leftover; (2) determine whether any points from the joint audits remain to be
implemented in any of the papers, and implement what applies; (3) commit and push.

Wave 1 (Tasks 69–70) dispositioned E2/E3/E4. This wave covers the six grok+claude
audits for P1–P5 and E1 that the owner uploaded to batch 7 (remote 3185653..c4346c3)
— the same audits the arena agent partially implemented on 2026-09-03/09-04
(P1 v17/v18, P2 v6/v7, P3 v24–v26, P4 v18–v25, P5 v19; E1 stayed at v9).

**Method.** Six parallel deep-read audit subagents (Task IDs 71-a…71-f) extracted
every point from both audit halves and classified it against the latest version
in the repo, with every load-bearing claim re-verified here (greps, diffs, and
fresh computation against `wave_e_cod/`). The registered leftover (E2 §3.6's
SSE/MSE mislabel) was fixed first as E2 v18 (build script
`apply_batch7_leftover_fix.py`; all four statistics re-verified: Schaefer MSE
12,772.2 = SSE 306,532.1/24; Allee MSE 7,690.1; declared-strength MSE 9,330.0).

---

## 1. The answer to "any points remaining?" — summary verdict per paper

| Paper | Latest (wave 1) | Wave-2 audit verdict | Wave-2 action |
|---|---|---|---|
| E1 | v9 | **The factual-recheck layer described as "v10" in the evaluation record never existed in the repo** (no file; every v10 number greps to zero; the referenced `/home/user/E1_FACTUAL_RECHECK.md` is absent). Several v9-claimed presentation fixes also absent. | **paperE1 v10 built** — all five verified fixes + the presentation fixes |
| E2 | v17 | Registered residual: §3.6 SSE→MSE one-word mislabels. | **paperE2 v18 built** (label fix) |
| E1's P-siblings: | | | |
| P1 | v18 | Thesis fork genuinely resolved (v17 hybrid: menu convexification + Proposition 9 + minimax framing). But the five "(D) still outstanding" items are untouched, and the hybrid introduced **dangling citations** (von Neumann 1928, Sion 1958, Ben-Tal et al. 2004 cited in §4.10, absent from References). | **paper1 v19 built** (reference fabric repair). Structural follow-ups registered. |
| P2 | v7 | **Essentially nothing implemented.** v6 = "conservative humanized rewrite" (no claims changed); v7 = abstract-only, responding to a *different* audit's checklist, re-asserting the flagged overclaim word-for-word and introducing two new flagged phrases. All 8 consensus items open. | **paper2 v8 built** (first safe tranche: a-fortiori direction, abstract scoping, companion reference, §6.4 cite). Theorem-level repairs registered as follow-ups. |
| P3 | v26 | ~2 full + ~10 partial of ~100 points (v24–v26 changed six line-pairs total). Consensus items 2 (notation), 3 (theorem inflation), 6 (five micro-errors), 7 (§11 re-argument) unimplemented; 1, 4, 5 partial. v26 introduced a **new internal contradiction** ("blank cell" vs the daggered Australia row). | **paper3 v27 built** (the verified micro-error cluster + both arithmetic facts + the contradiction). Structural items registered. |
| P4 | v25 | **The best case.** All 7 consensus items implemented (item 7 partial: abstract stripped, §1.2 not); the make-or-break fixes (§12 Euler revert, §9.4 four-state split, §7 GBN rebuild, §8 scheme-dependence) are real. A defined tail of small errors remains. | **paper4 v26 built** (τ_M pair, §5.1 pointer, regime (iii) arm range). Tail items registered. |
| P5 | v19 | One substantive ask implemented at two locations (the honest-tier correction); everything else byte-identical to the audited v18. v19 **introduced two regressions**: the abstract's non-transfer claim was broadened ("nothing transfers" — the opposite of the requested softening) and a new internal contradiction (§3.4/§4.1 still assert the archived windows as findings against the corrected §3.3 lead). | **paper5 v20 built** (both regressions repaired + archived-record attribution). Remaining items registered. |
| E3 | v12 | Dispositioned in Task 70 (comparator resolved, replication registered). No new audit. | none needed |
| E4 | v11 | Dispositioned in Task 69. No new audit. | none needed |

---

## 2. What wave 2 implemented (build script `apply_batch7_wave2.py`, fail-loud,
## asserted-once replacements; every number independently re-verified first)

### E1 v10 (from v9) — the never-landed layer, all numbers re-verified here
- **A7 (label swap + decimals):** rolling-origin decomposition recomputed:
  p0 = 98.05, control(S_tm1) = 184.43, M4 = 195.57 (h=1) → information delay
  86.4 / model's own cost 11.1; p0 = 264.72, control = 329.84, M4 = 488.27 (h=5)
  → 65.1 / 158.4. §4 relabelled (v9 had the component names swapped: "information
  loss 86 / the delay itself 12"), the lead-in dichotomy fixed, and the constructive
  finding stated (at h=1 the surplus model's own penalty is ~11 kt — the delay, not
  the structure, separates M4 from persistence; at h=5 Spec B the model dominates,
  694 of 713 kt).
- **A3 (documentation error):** §2.2's "K ∈ [500, 5000]" corrected to the code's
  actual box (K ∈ [max_train S + 10, 5000]; 500 is the multi-start initialiser) —
  verified against `run_ladder.py:fit_params` bounds. M1b's K = 105.9 kt declared
  an interior fit.
- **A5 (ranking caveat):** §3.2 addition — the fixed-K sweep recomputed on the
  coarse-regime recovery window (train 1995–2007, C̄ = 5.0): MSE 127.4 (K = 5000,
  r = 0.435) → 149.9 (K = 60, r = 0.773), training RMSE 11.29 → 12.24 kt; the
  (r, K) pair is not identified; valley-variant ordering not a robust ranking.
- **A1/A2 (obstruction restatement):** the collapse-window fit recomputed
  (r = 1.9350, K = 1032.7, C̄ = 240): two positive equilibria (repelling 144.1,
  attracting 888.6), the one-step map monotone below 783.2 (F′ = 0 there),
  damped approach (F′(attractor) ≈ −0.39). §1's "monotone parameter regime"
  sentence and Proposition 4.1's hypothesis/proof restated for this map; the
  obstruction verdict is unchanged.
- **A4:** one unifying sentence on the catch-dependence (rolling-insensitive vs
  fixed-window jump = the same flat valley).
- **Presentation fixes the v9 log claimed but the file lacked:** keyword
  ("recruitment forecasting" → "biomass forecasting; surplus production");
  origin-matched abstract numbers (84 vs 120 at h=1; 88 mixed-origin stated as
  such); §2.3 Brier near-degeneracy + Direction convention (persistence ΔS = 0 →
  0.00, excluded by declaration); "distinct from a statistical null" → "weaker
  than a statistical null" (two sites); Highlights all ≤ 85 characters; abstract
  298 words (≤ 300). Checked mechanically in the build.

### P1 v19 (from v18) — reference-fabric repair
- von Neumann (1928), Sion (1958), and Ben-Tal et al. (2004) — cited in §4.10's
  Remark since the v17 hybrid but never entered in the References — added in
  alphabetical position (Ben-Tal/Goryashko/Guslitzer/Nemirovski, *Math.
  Programming* 99(2):351–376; Sion, *Pac. J. Math.* 8(1):171–176; von Neumann,
  *Math. Annalen* 100:295–320). No other change.

### P5 v20 (from v19) — regression repair
- Abstract: "nothing transfers between them" → "stability does not transfer in
  general between them" (the requested softening; consistent with §3.2's
  hyperbolicity-conditioned transfer statement).
- §3.4: the stage-map sentences now attribute the 3–4/6–12 yr windows to the
  archived, unreproduced record (matching §3.3's corrected lead and the
  reconstruction-comparison table); the unsupported det(M − e^{iθ}I) = 0 gloss on
  the archived record dropped.
- §4.1: "exhibits an instability crossing near 3–4 yr" → "carries an archived,
  unreproduced instability record near 3–4 yr" with the §3.3/§3.4 status pointers.

### P3 v27 (from v26) — verified micro-error cluster
- Proposition 2's proof cites **Theorem 7** (the natural-block mass identity) for
  the mass-balance identity, not Theorem 3 (flux reconstruction) — verified
  against both theorems' statements.
- §3.3's displayed condition renamed the **barrier-safety (non-depletion)
  condition** (it is S_m(t) ≥ B_m(t), the negation of depletion).
- §2.2's list retitled "the four geo-interface and closure primitives"
  (γ_U U is U → A_act and does not involve the donor pool).
- §3.1 "separates the first three" → names the separated predicates (first,
  second, and fourth of the four; thermodynamic admissibility out of scope, per
  Proposition 2's layering).
- §5.4's double use of C disambiguated in prose (the composition matrix of
  Theorem 3 vs the coverage vector C(t)).
- §6.5.2's global-mean groundwater horizon corrected to **47.5 yr** (19/0.4).
- The MCS-2026 Australia sentence no longer claims the main-table cell is blank
  (the pre-2026 5,800,000 kt value is retained under the quarantine dagger).

### P4 v26 (from v25) — verified small-error cluster
- Corollary 6.1's proof: the delay pair is **(τ_M, τ_p)** (the deployment delays),
  not (τ_m, τ_p) — τ_m is the filter relaxation time, which by the paper's own
  notation rule never shares an equation with the deployment delays.
- §1.1: the phase-stabilised window is in **Section 5.1**, not Section 4.
- Five-regime topology, regime (iii): the second-fold unstable upper arm exists
  **above the second fold (regime (iv)'s 64.4 < τ < 150.4 yr)**, matching §9.3's
  registered record — not "through this window".

### P2 v8 (from v7) — first safe tranche
- **A-fortiori direction corrected:** the emptiness theorems are about ERViab
  (robust); they do not transfer to the weaker non-robust notion, which contains
  it. (v7 asserted the exact opposite.)
- **Abstract scoping:** "a set of finite, checkable certificates" → scoped to the
  polyhedral and finite-fibre cases with the timing bound a conditional template;
  "Five mechanisms are proved" → "established — four as finite objects, the
  timing bound as a closed-form template"; "The further four" named; "the
  disturbance moves after the control" made precise ("chosen along the realised
  control — with the policy's actions already fixed").
- **Companion reference:** the "companion assessment-separation analysis (under
  review)" now has a References entry (Author et al., in review).
- **§6.4:** the timing bound is computable from the drift certificate **(3)**
  (Theorem 4's), not (1).

### Non-destructiveness
Zero frozen verdicts, scores, kernels, spectral records, or table values changed
anywhere. E1's decomposition figures are relabelled and decimalised versions of
values already printed in v9's §4 (86/12/65/158 → 86.4/11.1/65.1/158.4); all
other edits are labels, citations, attributions, and the two arithmetic facts
(47.5; the blank-cell claim) that are corrections of printed errors.

---

## 3. What remains — the registered follow-up docket (deliberately not applied
## this wave, with reasons)

**P1 (largest structural remainder):** (1) the typed-endpoint operator E_end,typ
(grok A3 / claude §5.4-Fourth — the "photograph" claim remains unwitnessed);
(2) the §1.1 companion-prose strip (cycle-closure/hen-orchard/productivity-illusion
prose duplicated verbatim across P1/P3/P4 §1.1 — the cross-paper self-plagiarism
exposure all three auditors flagged); (3) the §2 13-slot tuple cut; (4) the
notation pass (FP₀/r/R/A/e/S collisions); (5) demotion of Prop 1/Lemma 2/Thm 3/
Thm 6 (only Theorem 4 → Proposition 4 was done in v18); (6) the title's doctrinal
sound; (7) the 25-check enumeration; (8) §6.1's unpublished-companion dependence.
*Reason:* each is a restructure-level edit on a sound paper; the thesis-level
fork (the audits' central issue) is resolved; these are presentation-layer
follow-ups best done as one coherent editing pass, not piecemeal.

**P2 (the deepest mathematical remainder):** Theorem 4's H2 circularity (restate
as an open-loop drift condition over [0, T_obs)); the Theorem 1/3 closed-loop
existence gap (D lsc/constant or convexification; the "exactly backwards"
convexity remark); Theorem 2 reframed as admissibility (not "hidden modes");
Definition 1/EViab deletion; Corollary 6's single-floor repair; Remark 1's Π_CE
class definition; the §5(b)–§6.3 contradiction; the C¹/Dini mismatch; the hitting-
time convention mismatch. *Reason:* these are theorem-level rewrites that change
what is claimed; doing them hastily would damage a paper whose every statement is
audited. They need a dedicated pass with mathematical verification of each
restated hypothesis.

**P3:** the notation pass (one letter one sort; the incomplete mid-§2.6 table);
theorem inflation (Thms 2/3/4/6/17/18/20, Lemma 16 — only supplement labels exist);
the R₀ split (R_ext/R_K/R_frozen); displaying the four-row and seven-compartment
incidence matrices; Theorem 14's missing E ≥ 0; §9's three inconsistent
field-difference values (4.47 / O(κ_A K) = O(5) / 4.652 vs −0.348); the
classification-matrix-vs-§6.5.4 Θ_F contradiction; the USGS single-vintage re-pin
(registered revision requirement, unchanged); the §11 weak/strong re-argument;
the three uncited companions; the length. *Reason:* as the auditors noted, these
are a monograph-scale restructuring; the top-priority mismatch (the §1.1
two-pool claim) was already defused at the claim level in v25, and this wave's
micro-errors were the verifiable remainder.

**P4:** the §9.2 lower-fold multiplier-record precision; the revision-history
changelog relocation to a supplement; §1.2's digit stripping; the M3-B family
list entry; the undefined "c > 0" Routh entry; the Halanay η collision; the
q*/p/S-for-stock notations; the uncited r-literature range; three uncited-but-
listed references (Zhang et al. 2013; Cloud–Moore–Kearfott 2009; Moore 1979);
§11.6's grant list; §8–§9 campaign tables. *Reason:* all are presentation-layer;
the paper's make-or-break items are closed.

**P5:** the claims-ledger box; the registration-vocabulary appendix; the logistic-
core parameter table; the λ/θ/margin reporting for ρ = 1.00035; the A1 undelayed-
stability reconciliation; the A9 slow-stock "agreement" reclassification; the
screen-band lineage acknowledgment; §4.6's relocation; the "42 vs several dozen"
count harmonisation; the companion citation. *Reason:* these were the audited
v18's open middle layer; v20 closed only the regressions v19 introduced (the
highest-severity items now standing). The remainder is a coherent next pass.

**E1:** the longer methodological asks (drift/damped-trend baseline; leave-one-
origin-out influence; the 900–1900 kt Table 6 forecast explanation; the M3/M4
609/586 deterioration explanation; the M4 decomposition as a results table; the
parameter table in a supplement; log-RMSE demotion). *Reason:* new computations/
analyses, not corrections; they need a scored campaign, not an edit.

**Cross-cutting (all papers):** the §1.1 shared-prose strip (P1/P3/P4) is the
single largest standing exposure. Rose (2026) and the frozen 2026-09-01 plan date
in P5 are no longer future-dated as of this repo's clock (2026-09), and are
recorded as resolved-by-clock, not edited.

---

## 4. Verification

- Every replacement asserted to occur exactly once (fail-loud build scripts:
  `apply_batch7_leftover_fix.py`, `apply_batch7_wave2.py`); re-runs are
  byte-stable.
- E1's new numbers computed fresh here (scripts inline in the task log):
  the A7 decomposition (98.05/184.43/195.57; 264.72/329.84/488.27), the A5 sweep
  (127.4/149.9; 0.435/0.773; 11.29/12.24), the A1/A2 collapse fit (1.9350/1032.7;
  144.1/888.6; 783.2; −0.39), and the A3 bounds against `run_ladder.py`.
- P3's arithmetic fact (19/0.4 = 47.5) and the Australia row (5,800,000 kt,
  daggered, not blank) verified directly.
- P4's τ notation rule verified against the paper's own §2.5/notation paragraph;
  the 64.4 < τ < 150.4 range against §9.3's registered record.
- All six diffs reviewed line-by-line; no unintended change.
