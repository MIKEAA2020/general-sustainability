# Paper01 — v28 restoration audit (does anything from `paper rewrites/latex/paper2_obstruction_calculus_v28.tex` merit restoring into the current main/supplementary?)

**2026-10-03 · Task 140.** The owner asked whether anything from the paper-rewrites-era
`paper2_obstruction_calculus_v28.tex` (113,270 bytes, ~14.3k words, SVVA-submission shape)
merits restoring into the current line — main or supplementary — "either as is or after
adaptations or corrections." **The current line is v69** (article
`paper01_obstruction_calculus_v69.tex`, 175,620 bytes + supplement 84,183 bytes; committed
c4a204a0 on `e2-v3-source-year`, see Task 139); no v70 exists. This document records the
audit. **Verdict: nothing from v28 merits restoration — not as-is, and not after
adaptation.** Every content element of v28 survives in v69 main or supplement, almost all
of it in deliberately hardened or corrected form, and the only v28 material v69 does not
carry is material the four-gates compliance program removed on purpose. Restoring any of
it would regress the gates or reintroduce corrected errors. A v70, if one is ever cut,
should not be seeded from v28.

## 1. Method

1. **Environment census.** All `theorem/proposition/corollary/definition/example`
   environments in v28 listed (15) and located in v69 main + supplement.
2. **Sentence-level coverage audit.** All 304 long v28 sentences fuzzy-matched
   (difflib, math/citation-normalized) against the 967-sentence v69 main+supplement pool;
   the 108 below-ratio sentences were each traced by hand to their v69 disposition.
3. **Phrase-survival checks** on the signature passages the coverage audit flagged
   (threshold remark, comparison-function extension, barrier duality, diagnostic force,
   injective-observation consistency check, notation disambiguation, ladder rungs,
   quantifier-order note, "stock recovering or collapsing", harvest vector, Nagumo,
   Marchaud, tube-safe action set).
4. **Bibliography diff** (39 v28 entries vs 50 main + 29 supplement entries,
   author-year keyed) and **figure/table caption census** (6 figures + 1 table in v28 vs
   7 + 5 in v69 main, 4 + 1 in supplement).

## 2. What survives (everything of record)

- **All 15 v28 statement-level objects** survive: robust epistemic kernel (Def.),
  selector principle, finite-time exit certificate, epistemic emptiness by admissibility,
  common-action obstruction, uniform-margin tube obstruction, obstruction ladder,
  hidden-mode example, delayed-information obstruction, finite-horizon
  soundness/completeness, exact certifier, observation-fibre criterion,
  safety-crossing-fibres corollary, monotonicity of the epistemic kernel — each present
  in main (as `calc-*`) and/or supplement S1, with the finite-horizon proof carried in
  full in S1. v69 adds 13 further objects (LP instantiation, sparse/Helly witness,
  oracle-recourse, three-branch example, one-step completeness, static-observation
  reduction, two-phase decomposition, window-nogo, Open Problem 1, belief-state safety
  value, chance-constrained obstruction, deterministic-kernel limit, relaxation-gap
  example).
- **All six v28 figures and its summary table** survive (incompatible safe controls and
  delayed-information in main; ladder, one-step obstruction tree, fibre-crossing and
  certainty-equivalence trap in supplement; the certificate-summary table in main with a
  more carefully qualified caption). v69 adds the Lean-declaration table, two
  coverage-audit tables, the fibre table, and the belief-value figure.
- **All 39 v28 references** survive (author-year keyed) in the 50+29 v69 union.
- **Section-level:** v28 §1.2's five contributions + finite-horizon mechanism all appear
  in v69 §1.2 (plus two new ones); §2's notation disambiguation (H(ξ,v) vs harvest
  vector vs W-sets) stands at main ~516; §5's four clusters (a) Veliov, (b) estimation
  tube, (c) observer-and-buffer, (d) linear substitution stand verbatim-headed in
  supplement S2 plus the new two-phase block; §6's institutional-kernel (IRViab)
  material, quantifier-order/circularity note, and limitations stand; Appendix A.1/A.2
  stand verbatim in supplement S3 with a new A.3.

## 3. The v28 material v69 does *not* carry — and why it should stay out

1. **The LSC / measurable-selection adverse-path derivations.** v28's proofs of the
   exit, common-action, and delayed-information theorems derived the adverse realization
   from lower semicontinuity of `D` via measurable-selection arguments (its (H1.2)/(H3.3)
   realization clauses). The v67–v69 hardening replaced these derivations with explicit
   original-system path hypotheses (H2.3, H3.2, H5.2) — the owner's gate 1. v69 is on
   record against the old route: "No lower semicontinuity inheritance for a thresholded
   disturbance correspondence, measurable feedback d(x), or convexified-to-original
   transfer is presumed" (main ~654) and "No use is made of a thresholded-correspondence
   LSC inheritance or an unproved closed-loop selection" (supplement exit proof).
   Restoring the v28 derivations as-is would claim what the gates withdrew; restoring
   them as an optional sufficiency remark ("under LSC of D on the strip the (H5.2) pair
   exists by measurable selection") is possible in principle but re-opens a settled gate
   decision to purchase a remark the paper explicitly declines to lean on. Not merited.
2. **v28's unconditional greatest-fixed-point thesis** ("the epistemic kernel is the
   greatest recursively viable collection of information states in the sense of the
   estimation-space reduction") — corrected in v69 to "Under exact rectangular belief
   dynamics and a strategy class admitting nonanticipative concatenation … Without those
   hypotheses, this is an organizational description rather than an exact
   greatest-fixed-point theorem" (main ~445). Restoring would regress gate 1.
3. **v28's CQSP-2007 "no loss of value / equality of value functions" attribution** —
   the exact claim verified as unverifiable in Task 139 and re-scoped at four sites in
   v69 (§1.1, §5(b), §6.3, S2(b)), with the estimation-space semantics carried by
   Kurzhanski–Vályi (1997) and all value-coincidence statements made conditional.
   Restoring would regress gate 4.

## 4. v28 passages superseded by corrected v69 versions (restoring would reintroduce errors)

- **State-dependent-decline extension** (v28: exit-time bound "sharpens" whenever the
  comparison integral is finite; otherwise "weakens to asymptotic approach") → v69's
  comparison-function remark (main ~1044) corrects this: a finite integral bounds only
  *first boundary contact* (its `\dot q = -\sqrt q` counterexample reaches zero and can
  stay there); strict exit requires a compatible continuation with negative drift at or
  through contact. v28's version was loose; v69's is exact.
- **Emptiness construction's singleton-prior claim** (v28: singleton beliefs "are not
  admissible initial states of this observation structure") → v69 explicitly admits
  singleton priors and restricts the empty-kernel statement to full-fibre starting
  beliefs (supplement prop:emptiness). v28's version was an overclaim.
- **Injective-observation consistency check** (v28: "the epistemic and robust kernels
  agree") → v69 adds the missing caveat that equality with a state-feedback robust
  kernel "requires an additional policy-class reduction; under such a reduction …"
  (main ~494). Hardened, not lost.
- **Barrier "diagnostic force" passage** (v28 §6.2 prose: "outside converse settings, the
  absence of a found barrier has no diagnostic force") → survives in stronger, worked
  form in S2's one-system comparison ("The unsuccessful search for a barrier is
  inconclusive on emptiness"; "No general nonexistence of a state-dependent barrier is
  inferred solely from a fibre-constancy argument"). The v28-era fibre-constancy claim
  itself was corrected in later rounds.
- **Threshold remark** (v28 rem:sigma) → survives *improved* as `calc-rem:sigma`
  (main ~825) and `rem:sigma` (supplement ~981): class-specific `σ*_Π`, the strictness
  caveat ("the threshold itself may be strictly smaller, in which case nonviability holds
  even when (3) fails"), and a new finite-checkability paragraph v28 lacked.
- **"Two readings" remark / Isaacs reading / exit-below-ladder / rungs-strict** → the
  Isaacs reading stands (main ~65, ~1050 region with the `d*` sufficiency discussion);
  rungs-strict and exit-below-ladder stand in S1's "Complete discussion of the
  obstruction ladder" block with Figure S1; the clairvoyant/intermediate-region phrasings
  are gone but their substance (unsafety complement of the converse; constructive;
  defeats all controls) is in §6.2's condensed text.

## 5. Verification status and disposition

- No changes were made to any TeX source; v69 (article + supplement) remains the shipped
  line of record, and v68 stays byte-frozen. This audit record is the only artifact.
- The audit was performed at source level (the .tex files), as with the prior rounds; the
  supplement's own standing note that article-to-supplement concordance "requires
  checking against compiled paginated proofs" is unaffected.
- **Recommendation:** if a v70 is cut for other reasons, seed it from v69 alone. The one
  conceivable v28-derived addition — an explicitly non-load-bearing LSC-sufficiency
  remark for (H5.2) — is available if the owner ever wants it, but on this audit's
  evidence it is not merited: it buys nothing the gates need and re-opens text that was
  deliberately hardened.
