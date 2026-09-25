# Round 17 — Proof Delegation, Envelope Correction, Open-Item Execution

**Date:** 2026-09-26. **Base:** `20bed07` (round 16 final). **Scope:** three directives — (D1) delegate lengthy technical proofs to supplements with brief sketches in main (P1 named); (D2) root-cause the elevation audit's rejected operator, correct the conjecture, fill the gaps; (D3) execute the three open items (recourse fold-in, E1 overfulls, venue package).

## D1 — Delegation (P1 v51 + supp v48)

Scan of main v50's 19 proof-bearing spans: the main text carried **sketch + extended discussion hybrids**, not lengthy proofs — the sketches were already brief; the bulk was discussion, worked instances, and one 48-cell table. Delegated to supp v48 as seven "Complete discussion of … (main text, Section N)" S1 blocks (verbatim bodies, refs adjusted to the supp's label set):
1. finite-horizon obstruction tree + one-step instance (Section 3);
2. common-action Farkas form (Section 3);
3. obstruction ladder itemization + strictness (Section 3);
4. delayed-information hypothesis + timing-bound discussion (Section 3);
5. minimal admissibility construction's mechanism isolation (Section 3);
6. fibre criterion's governance reading + fibre figure (Section 4);
7. degenerate limit's two worked instances + the audit-slice table (Section 10).

Main v51 keeps each statement + its brief sketch + a 1–2 sentence takeaway with an S1 pointer (~11.5k chars moved; main 156.5k → 145.1k chars, 19 → 18 pp). prop:monotone's span (3.2k ch) is mostly Section 6.5's limitations list — core content, not delegated. The intro roadmap sentence updated accordingly.

## D2 — The rejected operator: root cause, correction, gap-filling (minimax v2)

The elevation audit rejected the dynamic-envelope/Epistemic-HJBI proposal on three named grounds; `minimax_dual_certificates_v2.tex` now carries the full adjudication:

**Root causes.** (i) Category error: the proposed information-set operator is Bellman-type (nonlocal) dressed as a pointwise Hamiltonian — restricted-information games are information-state dynamic programs, not state PDEs; the nonlocality was never the defect, the differential clothing was. (ii) The measure *curve* t ↦ μ*_t carried no consistency (μ*_t need not be the marginal of one path measure) — no time consistency, so no recursion or comparison could even be posed; the correction replaces the curve with a single adversarial prior on disturbance paths. (iii) The selection gap was real only for value attainment: the certificate direction needs only the elementary bridge.

**Filled (complete proofs, exact verification).** Lemma (expectation-to-realization bridge): E[F] < 0 ⇒ positive-measure failing set, no selection theorem — 3-line proof. Definition (adversarial-prior envelope: essential supremum over nonanticipative policies of the conditional expected safety functional; per-policy martingale structure free). Theorem (finite well-posedness + comparison + exactness: the one-step operator Φ is order-preserving; backward induction computes Q(0) = Φ^N g exactly in rationals). Proposition (identification: the envelope's one-step evaluation IS the calculus's support-function recourse certificate Γ_h). Corollary (three-branch instance: Γ_h(τ) = 7/50 − τ, fires exactly for τ > 7/50, tight). Verifier: **24/24** (v1's 8-check static battery chained green; N1 bridge toy; N2 backward induction = brute force on a 2-step POMDP + full rational monotonicity scan; N3 the Γ_h identity at three τ's; N4 the pooling weights proven the blind-braking game's equalizer — Rλ = 0 and the row-sum identity (Rf)₂+(Rf)₃ = 18/25 − (48/25)f₁ ≤ 0 whenever (Rf)₁ ≥ 0, so the game value is 0 and hold-then-brake is optimal). Register leftovers in v1 ("programme" ×4) swept in v2. 4 pp, 0 overfull.

**Still conjectural (restated honestly).** The continuous-time residue: a consistent evolution law for the adversarial prior (martingale-transport flavor), the partition-refinement limit where a comparison principle would live, and general value attainment (selection). The static identification is exact and outside the conjecture.

## D3 — Open items executed

1. **Recourse fold-in (P1 v51).** The main-text proposition now states Γ_h with h_U the support function and firing condition Γ_h(λ) < 0; the sketch rewritten (variation-of-constants expansion → support-function bounds → strictly-negative weighted sum ⇒ facet violated); the example evaluates Γ_h(τ) = 7/50 − τ with Γ_h(1/5) = −3/50 < 0, threshold exact at 0.14. Supp v48's attainment remark rewritten edition-free (the φ_U-variant as the attainment-special case; the instance's critical delay shared).
2. **E1 overfulls (v52).** All 64 inherited boxes traced to ONE pandoc longtable (the Diebold–Mariano comparison, 11 columns). Fix: footnotesize + tabcolsep 3pt in a group + retuned column fractions. **0 overfull**, 35 pp, 47/47. (First attempt footnotesize-only got 64 → 44; the fraction retune cleared the rest.)
3. **Venue package.** `paper2_automatica_cover_note_v1.md` written: submission summary, proactive disclosure of the recourse correction (what changed and why), the proof architecture, replication pointers.

## Status table (this round's editions)

| Artifact | Edition | Checks | Pages | Overfull |
|---|---|---|---|---|
| P1 main | v51 | probe 8/8 | 18 | 0 |
| P1 supplementary | v48 | probe 7 blocks + ?? absent | 20 | 0 |
| minimax dual certificates | v2 | 24/24 (chained 8/8) | 4 | 0 |
| E1 cod forecast ladder | v52 | 47/47 | 35 | 0 |
| (unchanged) P3 v7, comp v11, ws v11, ebc v4, ARV v2 | round-16 editions | 30/30, 39/39, 46/46, 19/19, 61/61 | — | 0 |

## Alignment

Supp v48 ↔ P1 v51: the seven delegated blocks answer the main's pointers; the recourse block header corrected to "Section 3.7" (was mislabeled "Section 7" in v47); label hygiene verified by the no-"??" build checks. minimax v2's Γ_h and the three-branch numbers match P1 v51's folded statement exactly (both from the same exact script identities).
