# P3 Edition 5 — Round-13 Addendum (bundle: companion pointers, bridge remark, Section-10 note)

**Base:** `paper2_probabilistic_sufficiency_v4.tex` (frozen at `2ac7adc`). **Scope:** the
three-edit bundle executed on the round-12 audit's findings. Verify chain **28/28**
(26 v4 checks carried + 2 new); 9 pp, overfull 0. Companion edition shipped in the
same push: `paper2_exact_belief_computation_v2` (see its addendum).

## 1. The three edits

1. **Companion back-pointer (§methods).** The methods paragraph now names the P2
   lineage's scaling record (exact belief computation, editions 1–2: point-based
   evaluation, antichain compression, the four-parameter cube's Hamming
   classification) as built on P3's class-restricted rational alpha-vectors
   (`prop:pl`), with the scripts chaining this paper's seeds. This closes the
   back-pointer asymmetry found in the round-12 audit (the scaling paper cited P3;
   P3 cited nothing back).
2. **Noiseless-limit remark (`rem:eps0`).** New remark after the probe-count
   bound: the exact split of `prop:learn` (branch separation 2) is the
   ε → 0 degeneration of the probe-count law — sep = 1/2 − ε → 1/2,
   p_wrong(1) = ε → 0, so one probe achieves δ = 0 in the limit; for ε > 0 the
   law prices what the exact split gets for free, plus the 1/10 floor margin per
   probe step. Check 28 verifies the identities exactly (p_wrong(1) = ε at
   ε ∈ {1/10, 1/100, 1/1000}; strictness of (4ε(1−ε))^{1/2} > ε; sep(0) = 1/2).
3. **Calculus Section-10 cross-note (stochastic layer).** The sensor
   counterexample (deficit 1/20 against min-mass 1/2) now explicitly delimits the
   deterministic-limit reach of the calculus's probabilistic development (its
   Section 10): the min-mass bound there is adversarial-degeneration-scoped, not
   a law of the noisy layer. Conversely, the calculus's delayed-hidden-regime
   instance is identified as the deadline law at d₀ = 1, e_p = 0 (viability
   boundary z₀ ≥ 1 + T_obs; cell-by-cell tabulated agreement). P1 itself is
   untouched (frozen pending the owner venue decision); the note lives here and
   in the roadmap's cross-effect map.

## 2. Verification and build

- Chain: seeds 16+21/15/6 + 28 own checks, exit 0. New check 27 = eleven
  cross-reference needles; check 28 = the noiseless-limit identities above.
- Build: tectonic 0.15.0, `--keep-logs`; 9 pp, overfull 0; render probes green
  (remark title, back-pointer, cross-note strings, "with six results", no `??`).
- Code pointer updated to `paper2_probabilistic_sufficiency_v5_verification.py`
  (exactly once).

## 3. Process note

The first edit pass issued three parallel edits to the same file; the last write
won and edit 1 was silently lost — caught by the verifier's own needle check
(the missing back-pointer needles), re-applied serially. Standing rule reaffirmed:
**never issue parallel edits to one file.**
