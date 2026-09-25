# Round 16 — Meta-Register Purge, Self-Containment, Applied Expansion, Proof Completion

**Date:** 2026-09-25/26. **Base:** `5f0c9ec` (round 15 final). **Scope:** five directives — (D1) formal-register purge, (D2) self-containment + citation format, (D3) ARV data completeness, (D4) P1/P2 identity + proof-bar meaning, (D5) delegation/alignment.

## D1+D2 — Register and self-containment (scan then sweep)

Scan (round-16 entry 85) quantified meta-markers across the 8 current files. Dispositions:
- **Technical usages kept (content, not process):** estimation-tube programme, barrier programme (literature), coverage audit / asymmetric audit / learning-deadline audit / protection audit (device names), "value campaign" (computational), "worked-systems audit" (P4 title).
- **Process usages removed:** "the edition's script" → "the verification script"; "the audit" (process sense) → "the verification record"; "audited X" → "certified X" (P3 only); "chained" → "executes"; "the programme's concordance (companion)" → "the supplementary material" / "companion monitoring paper"; "P2 lineage (editions 1–2)" → "computational companion papers"; "This edition carries/asks/pushes" → "This paper …"; "Edition 1 of this series" (abstracts) → removed entirely; "flagship board / charter / owner / memo" → gone; "same repository" in references → "Preprint".
- **P3 v7:** the methods parity sentence ("Every theorem, proposition, lemma, and corollary carries a proof; standard results are cited rather than restated …") **deleted** — the bar itself stands and is enforced by verifier check 16 (18 envs / 18 proofs, exact parity).
- **Abstracts made fully self-contained:** ws v11 (dropped the in-abstract "(Abaee, 2026b)" citation); ebc v4 (dropped the "Edition 1 of this series" opening — abstract now leads with the paper's own contribution); ARV v2 (rewritten from scratch: no programme/edition/L4 shorthand, no internal shorthand; prose data description only). P3/comp abstracts were already clean.
- **L4-sentence class (ARV):** "the viability machinery … has been developed and validated on deliberately small exact instances" retained as the only lineage sentence, in the introduction, in formal register; the abstract carries no lineage at all.

Editions shipped (all NEW files; nothing overwritten): P1 **v50** main, supp **v47**; comp **v11**; P3 **v7**; ws **v11**; ebc **v4**; E1 **v51**; ARV **v2**.

## D3 — ARV v2 data expansion

v1 (3 pp) judged short. v2 (4 pp) adds three certified datasets + a summary table, all exact-rational verified (61/61 checks):
- **Schijns catch reconstruction** (Table 1): removals 1994 = 1,314 t, 1995 = 413 t; 2015 = 4,436 t cross-checked equal to the official removals row (cross-file consistency proposition); 1983–1989 rows all > 130,000 t (scale contrast).
- **RV fall survey index** (Table 3, model-independent): 1989 = 2,127,417 → 1994 = 21,797 (factor 21797/2127417); 1992 factor 239740/1117670. Duplicate 1983–85 rows in the archived file are **byte-identical** — the verifier asserts row-consistency (no contradiction), so no dedup decision was needed.
- **RAM per-year extension** (2021 vintage): SSB 2016–2021 = 340, 433, 394, 419, 440, 411 kt — re-crosses 276 kt by 2016, max 440 = 49.7% of the 884.6 kt reference point (never near it), recovery under a 4,436 t fishery (bidirectional moratorium reading).
- v2 also adds the decade-ratio table against the LRP (min 4180/4423 at 1986, max 94075/88460 at 1987) and Table 1 (summary of all windows/instruments).

## D4 — Answers

- **P1 (obstruction calculus v49/v50 + supp) IS the main Automatica-target paper** — the "paper 2" lineage. The venue was established earlier; no change.
- **"Build the six proofs" = completing condensed proofs in the supplementary.** Round 15 reported six missing; the recount found that three were already complete (lp-instant, decomposition, window-nogo as detached "Complete proof of…" blocks; emptiness by "Proof (by construction)") — the proof-pairing scan had undercounted. True gaps: **selector, oracle-recourse, sparse-witness (helly)**.

## Proof completion (supp v47, new in S1)

1. **Selector principle** — complete proof: admissibility, safety (reach inclusion under sampled-hold semantics), recursive viability (continuation witnesses the successor belief), induction on the review index, contrapositive to the certificate; finite converse = backward induction (cited), continuous converse = Section 6.5 completion (cited, not re-derived).
2. **Sparse common-action witness (prop:helly)** — complete proof: closedness (compactness of D(x) + continuity), boundedness (U compact), **convexity (needs the q_j convex — hypothesis now explicit**, the standing barrier-literature assumption; the remark records that without it the Helly route applies only to the convexified sets, consistent with the Section 3.4 nonconvex example), then finite-intersection property + Helly's theorem in R^m (contrapositive: empty intersection ⇒ ≤ m+1 members empty).
3. **Oracle-recourse certificate** — **the main text's φ_U-display has a genuine soundness gap**: its chaining step ("weighted safety implies the bracket is nonnegative") requires the policy's realized pairings to *attain* the pointwise minima, which an arbitrary admissible signal need not do. Supp v47 ships the **corrected, airtight support-function certificate** Γ_h(λ) = inf_d{Σλβ + ∫₀^τ h_U(Σλk) + Σ∫_τ^T h_U(λk)} with firing condition Γ_h(λ) < 0, proved in full (support-function bound + strictly-negative weighted sum ⇒ some facet violated; window-signal arbitrariness handled). The remark proves the attainment condition HOLDS on the pooled window term of the three-branch instance (Σλk ≡ 0 ⇒ φ_U(0) = h_U(0) = 0 for every signal), so the instance's exact critical delay τ* = 7/50 is unchanged; the φ_U-form is retained as the attainment-special case. **The main text's display is left as-is in v50** (the instance's post-τ arithmetic under the h-form would need the branch dynamics re-read; folded into the venue-revision package, recorded here and in the roadmap).

## Verifier and build status (all re-run green this round)

| Paper | Edition | Checks | Pages | Overfull |
|---|---|---|---|---|
| P1 obstruction calculus (main) | v50 | probe 9/9 | 19 | 0 |
| P1 supplementary | v47 | probe 5/5 | 17 | 0 |
| P3 probabilistic sufficiency | v7 | 30/30 | 10 | 0 |
| comp computational certification | v11 | 39/39 | 10 | 0 |
| ws worked systems | v11 | 46/46 | 9 | 0 |
| ebc exact belief computation | v4 | 19/19 | 4 | 0 |
| E1 cod forecast ladder | v51 | 47/47 | 35 | 64 (v50-inherited, pandoc lineage; byte-diff vs v50 = the 4 edited hunks only) |
| ARV applied regime viability | v2 | 61/61 | 4 | 0 |

Needle-rot rule applied throughout: when an edition deliberately replaces wording, that edition's verifier needles are updated in the same pass (comp "present framework" needle; ebc "executes the series' first verification script"; P3 v7 removed the parity-sentence needles and extended FORBIDDEN with the retired markers).

## D5 — Delegation/alignment

Alignment: every verifier re-run green against its own edition; supp v47 ↔ P1 v50 consistent (the three complete proofs answer the main text's three unproved statements; the attainment remark dovetails with the main text's pooling discussion). Delegation: nothing further moved main→supp this round — the only new main-text material (ARV v2's three datasets) is applied results the paper must carry itself; the recourse correction lives in the supp by design (main carries the sketch, supp the complete material), and the venue-revision package will fold the corrected display into the main statement after the instance arithmetic is re-derived from the branch dynamics.
