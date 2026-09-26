# Round 19 — General Finite-Sequence Envelope, Package Hygiene, Venue Fits

**Date:** 2026-09-26. **Base:** `4fbe6b4` (round 18 final). **Scope:** four directives — (D1) lift the coupling identities to a general finite-sequence statement; (D2) cover-note enclosure line update; (D3) P1 case-study table cleanup; (D4) top-venue fits.

## D1 — The general theorem (minimax v4)

`minimax_dual_certificates_v4.{tex,pdf,_verify.py}`: new section "The general finite-sequence envelope" states and **proves in full** the lift of the review-sequence identities (the K = 2 instance was the template):

- **Setup.** K windows, finite disturbance sets, Ω = ∏D_k finite; consistent adversarial prior μ* = ⊗μ*_k (consistency = exactly the requirement the original proposal lacked); review filtration as an increasing sequence of partitions 𝒫₁ ⪯ … ⪯ 𝒫_K (singletons at K; 𝒫₁ may be trivial — blind first window); nonanticipative policies = cell-constant action rules (the filtration carries the full observation history, so cell-constancy IS adaptedness); bounded rational safety functional G.
- **Theorem (i) tower + martingale:** for every policy, E[G^π] equals the iterated-conditional evaluation over the filtration; M^π_k = E[G^π | 𝒫_k] is a μ*-martingale. *Proof:* finiteness + the defining property of conditional expectation.
- **Theorem (ii) dynamic programming:** the review-tree node recursion (max over the window's actions, μ*-weighted child averages) computes the envelope value exactly: Q₀ = sup_π E[G^π] = prior-weighted N₁; the supremum is **attained** by a policy pasted from the node-wise maximizers. *Proof:* backward induction on stages; the step conditions on the 𝒫₁-cell (exogeneity of disturbances keeps the child weights at the prior ratios), decomposes policies as (action, continuation), and invokes the induction hypothesis on the conditioned sub-instances; the tower identity does the splitting.
- **Theorem (iii) refinement monotonicity:** stage-wise refinement never decreases Q₀ (every coarse-adapted policy is fine-adapted; supima ordered).
- **Theorem (iv) exactness + obstruction:** all node values rational; Q₀ < 0 ⇒ for EVERY policy the defeating set {G^π < 0} carries positive μ*-measure (via the corrected formulation's bridge lemma).
- **Remark (three consequences).** (1) The recourse certificate is the depth-one case — the node recursion collapses to Γ_h (the corrected formulation's identification). (2) **Coupling selection is a real problem**: one-step priors do not determine μ* — two consistent couplings with identical marginals give different values (0 vs +1 certified); the residue conjecture's "evolution law for the adversarial prior" is precisely a coupling-selection problem, the finite shadow of its martingale-transport flavour. (3) Refinement monotonicity grounds the partition-limit clause; the continuous-time residue is exactly which couplings and which refinement limits survive continuous disturbance sets.

**Verification:** 24/24 (chained v3 20/20 → v2 24/24 → v1 8/8), all checks substantive: the tower identity on **all 8192 policies** of a K = 3 adaptive-filtration instance; the level-by-level martingale equalities as explicit intermediate recomputations; the DP = tree-supremum equality on a second instance (K = 2, blind first window, 3 actions — 19 683 policies tower-checked); refinement monotone with a genuine enumeration of the measurability inclusion; the bridge direction with certified positive defeating measure; the coupling-selection example. (Two vacuous check drafts were caught and replaced before shipping — the shipped battery is honest.) 5 pp, 0 overfull, build exit-0/halt-0 verified.

## D2 — Cover note updated in place

`paper2_automatica_cover_note_v1.md`: enclosure line now **main v52 + supp v50** (18 pp + 20 pp); the companion-work paragraph now cites **minimax v4** with the general theorem and the grounded residue. Diff verified to contain exactly the two intended edits.

## D3 — P1 tables (v52 main + supp v50)

Check first: P1's tables carry **no pandoc minipage wrappers** (0 occurrences — hand-written booktabs; the E1 cleanup target does not exist here). The genuine equivalent defect found: three tables broke the package's pure-booktabs style with vertical rules — the coverage grid (`l|cccc…`), the two-patch table (`l|c|l|l`, inside \resizebox), and the supp's belief-state slice (`cc|ccc|c|l`). Removed in **P1 v52** and **supp v50** (one-line preamble changes each; a first supp attempt miscounted the 7-column preamble and was caught by the build gate — exit/halt/?? all checked). Both: 0 overfull, no "??", 18 pp / 20 pp.

## D4 — Top venue fits

Verified anchors: Automatica — regular papers nominally 12 pp in its two-column format (flexible in practice), brief papers 8 pp, technical communiqués 5 pp [1](https://www.sciencedirect.com/journal/automatica/publish/guide-for-authors); SICON — research articles on the mathematics and applications of control theory and the parts of optimization concerned with dynamics, requiring significance at both the mathematical and applied levels [2](https://www.scimagojr.com/journalsearch.php?q=26405&tip=sid&clean=0).

| Manuscript | Primary fit | Why | Backups |
|---|---|---|---|
| Obstruction calculus (P1 v52 + supp v50) | **Automatica** (established) | certificate-based systems flavour, control-semantics match, regular-paper length now comfortable with the delegation architecture | IEEE TAC (paper style: compact full proofs in main); SICON (more mathematical depth tolerated, supp culture accepted) |
| Probabilistic sufficiency (P3 v7) | **IEEE TAC** (or Stochastic Systems) | POMDP belief-state values, exact rational value functions — TAC's brevity culture fits the closed-form battery | SIAM J. Control Optim.; Ann. Appl. Probab. (if the stochastic layer is foregrounded) |
| Computational certification (comp v11) | **Automatica (brief)** or **SIAM J. Optimization** | LP duality, moment approximations, certified bounds — SIOPT loves certificates + finite programs | Math. Programming (if the LP theory is foregrounded); Systems & Control Letters |
| Worked systems (ws v11) | **Systems & Control Letters** | worked/counterexample genre is the journal's core; 9 pp fits | Automatica (technical communiqué for the strongest three systems) |
| Exact belief computation (ebc v4) | **Stochastic Systems** or **Automatica (brief)** | PBVI-style exact recursion + antichain compression | IEEE TAC; Machine Learning (if the compression algorithm is foregrounded) |
| Minimax dual certificates (v4) | **Mathematics of Operations Research** | measure duals, minimax equality + convexity boundary, coupling selection, martingale-transport-flavoured residue — MoOR's exact genre | Operations Research; SICON (control-dressed); Journal of Convex Analysis |
| Applied pair (ARV v2 + E1 v53) | **Canadian Journal of Fisheries and Aquatic Sciences** | NAFO 2J3KL is CJFAS's home stock; LRP governance angle | ICES J. Marine Science (reconstruction cross-check angle); Fisheries Research (forecast-ladder scoring); PNAS-style only if the monitoring-not-catch theorem is framed general |
| Forecast ladder methodology alone | **International J. of Forecasting** | competing-ladder scoring + review-timing identity as forecast evaluation | — |

Strategic note: the calculus (Automatica) and the dual-certificates paper (MoOR) are cleanly separated venues; submitting comp v11 to SIOPT and ws v11 to SCL keeps all submissions simultaneous without overlap. The applied pair's governance theorem is the one piece a general-audience venue could take — decide whether to keep it with the package orlet it stand alone.

## Status table (round-19 editions)

| Artifact | Edition | Checks | Pages | Overfull | Build |
|---|---|---|---|---|---|
| minimax dual certificates | v4 | 24/24 (chained 20/24/8) | 5 | 0 | exit 0, halt 0 |
| P1 main | v52 | probe: tables normalized, ?? absent | 18 | 0 | exit 0, halt 0 |
| P1 supplementary | v50 | ?? absent | 20 | 0 | exit 0, halt 0 |
| cover note | v1 (updated in place, as directed) | — | — | — | — |
| (unchanged) P3 v7, comp v11, ws v11, ebc v4, ARV v2, E1 v53 | prior editions | 30/30, 39/39, 46/46, 19/19, 61/61, 47/47 | — | 0 | — |

### Correction appendix (September 26, 2026, post round 26 + review III)

The strategic note above (line 41) is obsolete on three counts, established by the shipped record:

1. **The "governance theorem" no longer exists in the package.** The referent was ARV v2's `prop:capelin`, "the covariate alarm **leads** the mortality crossing" ("the monitoring instrument moved before the mortality regime did") — the early-warning reading behind the PNAS-style option. The current edition certifies the weaker, correct claim: v6's `prop:capelin` is "the covariate crossing **is contemporaneous with** the mortality crossing" — at annual data resolution the crossings coincide; the lead is not certifiable as a predictive claim and was withdrawn in the verification lineage (lineage audit, `programme_lineage_content_loss_audit_v1.md`). The one piece a general-audience venue could take dissolved under exact certification; the decision this note posed ("keep with the package or let it stand alone") resolved itself — there is nothing to extract, and ARV v6 stays CJFAS-scoped on the realized record.
2. **The branding was loose even for v2.** ARV v2 contains zero occurrences of "governance"; the proposition is a monitoring/early-warning result about one stock's indicators. Theorem-grade governance content in this programme lives in `paper5_sampled_governance` ("The decision clock", blinded NatSustain edition v47) — which already stands alone, so the note's either/or has been executed on the correct object by other means.
3. **Editions are stale.** comp v11 / ws v11 / ARV v2 / E1 v53 are now v15 / v15 / v6 / v56 (check counts in the map's current-editions table).

The venue-strategy substance that survives: the separation of the Automatica and MoOR submissions, and the comp-to-SIOPT / ws-to-SCL simultaneity point. The applied pair's correct general-audience posture remains the one review III recorded: no extractable theorem; companion-by-construction split (ARV prices what could have been kept safe, E1 prices what could be predicted); governance-adjacent material delegated by citation (ARV → E1 §3.10; E1 → the sampled-governance deposit, 22554297).

**Timeline note (same day).** The venue table above is the round-19 snapshot, frozen as written: obstruction calculus P1 v52 + supp v50, comp v11, ws v11, ebc v4, ARV v2, E1 v53, minimax v4, P3 v7. Current editions (map v11, round 26): obstruction calculus **v53 + supp v51**, comp v15, ws v15, ebc v6, ARV v6, E1 v56, minimax v7, P3 v8. The v52 mention is historical, not a current-state claim.
