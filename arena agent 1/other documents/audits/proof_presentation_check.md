# Proof-Presentation Check (Turn 50)

**Scope.** A statement-by-statement scan of the nine latest manuscript versions for displayed proofs: every numbered theorem/proposition/lemma/corollary must carry a proof, either displayed in full or replaced by a citation to the literature (the standing rule). The scan sweeps the statement-header/proof-marker pattern mechanically and then hand-inspects every flag. Findings are implemented where worth implementing, as-is or after correction (turn-33 standing instruction).

**Files scanned:** `paper1_assessment_separation_v6.md`, `paper2_obstruction_calculus_v3.md`, `paper3_material_ledgers_v6.md`, `paper4_delay_dynamics_v5.md`, `paper5_sampled_governance_v5.md`, `paperE1_cod_forecast_ladder_v5.md`, `paperE2_cod_intervention_v8.md`, `paperE3_edwards_forecast_ladder_v5.md`, `paperE4_edwards_intervention_v6.md`.

## Verdicts by paper

- **P1 (assessment separation, v6): clean.** All 8 numbered results carry displayed proofs. Theorem 7's proof is unlabelled but complete (datum/proof in one block); no action.
- **P2 (obstruction calculus, v3): clean.** All 6 theorems/corollaries carry proofs. Theorem 2 and Theorem 3 were inspected in full: constructive, no gaps. The line-172 flag is prose, not an unproved statement. No action.
- **P3 (material ledgers, v6): clean.** All 21 numbered results and the 3 unnumbered propositions/corollaries carry proofs. The orphan markers at lines 236, 329, 635, 641 belong to complete proof blocks for unnumbered statements. No action.
- **P4 (delay dynamics, v5): two gaps, fixed in v6.** Proposition 2 has a full conditional proof inline; Propositions 3, 4, 6 and Theorems 2–6 have proofs. **Corollary 3 and Proposition 5 carried their computations in the statement with no displayed proof.** These are the only genuine "could-expand" candidates in the corpus. Fixed in `paper4_delay_dynamics_v6.md`:
  1. *Corollary 3 (Section 5.4).* Appended a full proof of the existence step: the certificate map $F(\chi_m)$ (the supremum in (10)), the uniform $O(\omega^{-2})$ tail bound making the supremum a maximum over a compact frequency range, joint continuity giving continuity of $F$ (hypotheses (i)–(ii)), $F(0) = 0.080 < 1$ (hypothesis (iii) as its strict-margin form), and the conservative radius $\chi_m^*$. The final clause (sufficiently large mobilising weight; $\tau_p$ alone cannot produce a Hopf) is derived from the certificate's sufficient-condition status.
  2. *Proposition 5 (Section 6.3).* Appended a full proof of the computational step: modulus/phase separation of the characteristic function (5), invariance of the frequency equation under $C_Z \to -C_Z$, the odd-half-period phase shift, the two displayed delay formulas at the certified pair $(\tau_-, \tau_+) = (3.666149, 150.358477)$ with $(\omega_1, \omega_2) = (0.0251915, 0.0394366)$, and the simplicity/transversality evaluations ($-6.07\times10^{-6}$, $+1.83\times10^{-5}$) that keep both shifted crossings local Hopfs. All numbers are certified by the 21-gate registration campaign (`rerun_campaigns/campaign_p4_dr_registration.py`, gate log `rerun_campaigns/results/p4_dr_registration_gates.txt`; all gates pass).
  3. Both expansions are deposited as Supplementary S10; the delayed-recruitment registration records referenced by the proofs are Supplementary S9 (`paper4_supplementary_v2.md`).
- **P5 (sampled governance, v5): one gap, fixed in v6.** The phase-line proposition (line 120) and the forward-invariance proposition (line 134) carry full proofs. **The extra-loss threshold-shift lemma (line 124) carried only an informal paragraph** ("The argument is elementary..."). Fixed in `paper5_sampled_governance_v6.md`: the paragraph is replaced by a full proof — the derivative of the constitutive cubic production function, its unique interior maximum (the two displayed critical points $S_\pm$ with $0 < S_- < \mathfrak s < S_+ < K$), the two-interval (IVT + strict monotonicity) argument for both cases (i) constant loss and (ii) proportional mortality, coalescence at the production maximum and disappearance beyond it, and the case-(i)/case-(ii) distinction at $S = 0$ ($f_C(0) = -C < 0$ versus $f_M(0) = 0$). No statement or number of v5 changed.
- **E1–E4: no theorem constructs by design.** These are narrative/empirical papers with zero numbered results; there is nothing to attach proofs to. No action.

## Cross-cutting checks

- **No standard-result citation violations.** P4 cites Hale and Verduyn Lunel (1993, Ch. 11) for the stability-switch principle, Åström and Wittenmark (1997) for sampled-data design, Øksendal for stochastic integrals — all appropriate; no folklore result is used without either proof or citation.
- **The P4 v6 insertions are versioned, not overwrites.** v5 remains untouched in the repository; all changes live in `paper4_delay_dynamics_v6.md`, `paper5_sampled_governance_v6.md`, and `paper4_supplementary_v2.md`.

## Residual items

- P4 Proposition 2's proof is conditional on the unproved reduction conjecture — declared in the statement, consistent with the paper's own conventions; not a presentation defect.
- P1 Theorem 7's proof label is absent but the proof text is present; a cosmetic item, left as-is to avoid touching a clean version.
- No other "could-expand" candidates exist in the corpus as of the scanned versions.
