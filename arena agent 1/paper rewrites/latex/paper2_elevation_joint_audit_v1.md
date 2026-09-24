# Joint Audit Record — Round 5: the Elevation and Duality Audits (`audits2.txt`)

**Inputs.** `uploads/audits2.txt`, four blocks: (1) gemini, "strategic masterplan" (five pillars: consolidation into two flagships; conic/SOS duality; Minimum Viable Monitoring synthesis; calibrated case studies; an open-source library; a six-month roadmap); (2) grok, elevation response (G1–G5, U1–U4, an integrity ledger, a sequencing table); (3) gemini, the "Universal Minimax Epistemic Duality Theorem" with five claimed corollaries, three design formulas, a continuous two-stock benchmark, and an insertion blueprint; (4) **a byte-identical duplicate of block 3 mislabeled as grok's** (verified: 21,784 characters, equal except the author label) — grok did not review the duality proposal, so block 3 is adjudicated once.

**Method.** As in every round: claims verified against artifacts before adjudication — all eight shipped paper2 PDFs probed; the duality theorem's steps re-derived and computed in exact rational arithmetic; the benchmark's arithmetic recomputed symbol-by-symbol; prior-round dispositions checked for staleness.

---

## Part I — Answer to the owner's first question: remaining audit points worth implementing

The residual ledger across rounds 1–5, with dispositions. (Items marked SHIP were implemented in this round; OWNER = owner decision, not ours; DONE = already shipped in a prior round.)

| # | Residual point (source round) | Disposition |
|---|---|---|
| R1 | "Fix all uncompiled LaTeX `\ref`s" (this round, gemini Month-2) | **DONE/stale.** Fixed in rounds 1 and 3; re-probed now across all eight shipped PDFs: zero malformed reference forms in every one. |
| R2 | "Unshown scripts / informal path" (grok, rounds 4–5) | **Stale.** The scripts are public in the repository and ship in the source zips; the path is disclosed in every paper's code-availability statement by owner convention. |
| R3 | "Declarations pasted into the body" (grok, round 5) | **Refuted in round 3** — a PDF text-extraction artifact (hyphenated page break + interleaved folio); the sources are clean. |
| R4 | Delay-rule inequality, "28 → 36 reversed", reversed CE labels (grok integrity ledger, round 5) | **DONE** — all three repaired in rounds 3–4 (monitoring v2's identity form; vector-floor v2's corrected sentence; the canonical-uncorrected convention across the five v2 editions and the selector v3). |
| R5 | State-level vs epistemic failure as a core axiom (gemini Pillar 2) | **ADOPTED — SHIP.** Implemented in this round's new paper as the three-class obstruction taxonomy (physical / epistemic / institutional) instantiated on the audited grid (check V7), with the exact sentence "a dead state is never an information failure". |
| R6 | Minimum Viable Monitoring (gemini Pillar 3; grok U3's four rules) | **PARTIALLY DONE; PART ADOPTED.** The design side exists as the monitoring note's coarsest-monitoring enumeration and the applications note's rules; this round adds the verified synthesis instances (closed-form critical aggregate; fibre-width formula). The general min-cost program remains a successor item. |
| R7 | Fibre Danger Index (gemini Pillar 3) | **ADOPTED AFTER CORRECTION — SHIP.** Implemented as the exact fibre-width formula Δx₁(Y) = Y − 4 on the benchmark (V8); the audit's "provably incapable" threshold is a buffer reading of the fibre criterion, stated as such. |
| R8 | Open-source library (`pyViabCert`, gemini Pillar 5; grok U1; applications note L5) | **ACCEPTED — SCHEDULED (owner roadmap).** The highest-leverage remaining item by both reviewers. The exact-arithmetic verify scripts shipped across rounds 1–5 (five d4–d13 scripts, three selector scripts, the pointer checker, and this round's minimax verifier with reusable certificate checks) are its seed module set. Not built in this round; recorded as the top successor item. |
| R9 | Second, non-toy worked system (grok "no second example"; gemini Pillar 4) | **PARTIALLY SHIP.** The corrected two-stock continuous model (this round's new paper) is a second, fully specified system with closed-form results. Real-data calibration (fisheries/SEIR) is OWNER-side (applications note L4); the venue for such an applied paper is an owner decision. |
| R10 | Insert the duality theorem into the calculus paper as §3.0; retire/withdraw the catalogue notes; consolidate into 2–3 flagships (all four strategy blocks, mutually contradictory) | **OWNER — not adopted.** The reviewers disagree with each other on the target architecture (two flagships vs three; which notes die), and the standing constraints keep lineages standalone and renames owner-decided. Recorded with the contradictions mapped in Part III. |
| R11 | SOS/barrier duality, HJB elevation of the timing bound (gemini Pillar 2) | **RECORDED, not adopted.** Plausible successor-programme directions beyond the verified static core; no audit-verifiable content was supplied to ship. |
| R12 | Applied calibration case studies with published data (gemini Pillar 4; grok U2) | **OWNER-side** (requires domain data and venue choice; matches applications-note limitation L4). |
| R13 | Errata/concordance of "which integer is which kernel on which system" (grok integrity) | **PARTIALLY DONE.** The addenda and audit records now carry the counts with provenance; a standalone concordance document remains a small owner-side item. |
| R14 | Comparison table vs neighbouring tools (barrier certificates, POMDP solvers, MSE) (grok U4) | **RECORDED — owner/successor.** Not adoptable without a literature verification pass; flagged for the successor paper's related-work section. |

**Net: three items shipped this round (R5, R6-partial, R7 + the duality core itself), one scheduled (R8), the rest are owner decisions or already done — nothing verified-and-actionable remains unimplemented on our side.**

## Part II — The duality proposal: step-by-step adjudication

| Claim (block 3) | Verdict after verification | Where it lands |
|---|---|---|
| Minimax equality (Sion core) | **Correct** under the hypotheses (compact convex U, control-affine f, compact active bundle); exact on the polyhedral instance (−1/10 = −1/10, both directions; feasible contrast +1/10) | Theorem 1, check V1 |
| Emptiness iff adversarial measure with margin | **Correct given convexity** (attainment by compactness) | Theorem 1 |
| Sparsity "at most k+1 atoms" | **Result correct; proposed proof garbled** (Carathéodory gives k+2; the Helly step is asserted, not executed) | Proposition 2: repaired route (finite reduction → LP duality → basic-solution support), tightness certified (V4) |
| Corollary: Farkas recovery | **Correct and verified** — λ = (1/2,1/2) makes the expected drift constant −1/10, exactly the calculus paper's §3.4 normalized pair | Proposition 3(i), check V2 |
| Corollary: Isaacs singleton | **Correct with a caveat the proposal missed**: the dual is an adversarial distribution over disturbances; the single-worst-disturbance reading is not the dual (1 ≠ 0 on the exact instance) | Proposition 3(ii), check V6 |
| Corollary: fibre classification from the dual measure | **Rejected — not proven.** The fibre criterion is a labeling result; no measure argument for it is supplied | Not claimed |
| Corollary: stochastic selector bridge (μ* = worst-case prior) | **Rejected as claimed — conjecture** (unverified against the stochastic lineage's masked-backup mechanics) | Conjectures section |
| "Resolves Open Problem 1" (dynamic envelope / Epistemic HJBI) | **Rejected.** The proposed operator is nonlocal in the state and is not a well-posed PDE; no viscosity well-posedness, comparison argument, or nonanticipative-selection proof; an expectation envelope crossing zero is not a trajectory violation without a selection theorem. Open Problem 1 remains open | Conjectures section, gaps named |
| Design formula 1 (safe interval as a dual ratio) | **Conjecture** (plausible scaling, unproven) | Conjectures section |
| Design formula 2 (Lipschitz quantization bound) | **Conjecture** (instance-supported only) | Conjectures section |
| Design formula 3 (aggregation width) | **Adopted after correction** — the exact fibre-width formula Δx₁(Y) = Y − 4 on the benchmark; the "provably incapable" threshold restated as the fibre criterion's buffer reading | Theorem 4's section, check V8 |
| Benchmark: "viable at Y = 5, obstructed at Y = 4.1" | **Rejected — the evaluation switches control sets** (capacity at Y = 5; a demand floor that contradicts the capacity at Y = 4.1; under both constraints simultaneously the control set is empty). Caps arithmetic itself verified correct (1.2/0.88 and 1.29/0.97) | Replaced: one fixed control set (demand floor 2), closed form |
| Benchmark: "margin ε = 0.14 with weights (1/2,1/2)" | **Normalization error.** (1/2,1/2) on the active-floor atoms yields ε = 0.07 under the demand floor; 0.14 is the row-side Farkas slack with weights (1,1,1) including the demand row — two different objects | Paper uses the corrected dual: ε = 3/50 at Y = 6 with λ = (1/2,1/2) (check V5) |
| Insertion blueprint (§3.0 of the calculus paper; retire five notes; repurpose Track B) | **OWNER** — recorded with the inter-reviewer contradictions (Part III) | Not enacted |

## Part III — The consolidation blueprints: mapped and recorded (owner decision)

Gemini (block 1): two flagships; fold the selectors into Paper 1; fold D4/D7/D8 into a computational Paper 2; **drop D11/D13**. Gemini (block 3): one theorem subsumes everything; insert into the calculus paper; retire five notes. Grok (block 2): original calculus as the theory paper; Track B as the only computational companion; belief-state theory as a proper paper; **fold the catalogue facts into a supplement**; library + one applied paper first. The three disagree on the target architecture, on which notes survive, and on sequencing. All three share two factual premises that do not survive verification as of this round: "undefined working system / unpublished grid" (the system is defined in the calculus paper's Section 8 and every count is machine-verified in public scripts) and "unshown scripts" (public, in-repo, shipped in zips). All three also predate or ignore the round-3/4 repairs (the integrity ledger's items are shipped-fixed). The defensible residue on which they AGREE — and which the owner should decide on: (a) a library MVP, (b) one real calibrated application, (c) whether the catalogue notes should eventually be folded into a supplement. None of these is enacted by an audit round.

## Verification summary (this round's new paper)

`minimax_dual_certificates_v1_verify.py`, 8/8 exact checks: V1 polyhedral iff both directions; V2 normalized-Farkas recovery; V3 the non-convex minimax gap; V4 Helly-tight k+1 sparsity; V5 the corrected benchmark (Y* = 27/5; witness (6/5,4/5); two-point certificate, ε = 3/50); V6 the singleton reduction with the load-bearing distribution; V7 the three-class taxonomy by full enumeration (physical corner / epistemic B* / institutional 12→0); V8 the fibre-width formula. Build: 3 pages, zero Overfull, zero malformed references.
