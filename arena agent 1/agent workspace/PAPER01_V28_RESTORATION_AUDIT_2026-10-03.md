# Paper01 — v28 restoration audit (does anything from `paper rewrites/latex/paper2_obstruction_calculus_v28.tex` merit restoring into the current main/supplementary?)

**2026-10-03 · Task 140.** The owner asked whether anything from the paper-rewrites-era
`paper2_obstruction_calculus_v28.tex` (113,270 bytes, ~14.3k words, SVVA-submission shape)
merits restoring into the current line — main or supplementary — "either as is or after
adaptations or corrections." **Verdict: no. Nothing from v28 merits restoration into the
current line — not as-is, and not after adaptation.** Every content element of v28 that
should survive does survive, almost all of it in deliberately hardened or corrected form;
the only v28 material the current line does not carry is material the four-gates program
removed on purpose or that a later adjudication retired with cause. Restoring any of it
would regress the gates, reintroduce corrected errors, or undo a fresh deliberate
decision.

**Line-of-record note.** The audit began against v69 (the then-tip, Task 139, commit
c4a204a0). During the audit the remote line advanced four commits — including
`2038cd2f` "**Paper01 v70: scoped B edits, demote A4, preserve held review gates**" —
so the audit was re-targeted at **v70** (`paper01_obstruction_calculus_v70.tex` +
`paper01_obstruction_calculus_v70_supplementary.tex`, builds green per their committed
logs). The v69→v70 delta is small and scoped: main +44/−57 lines, supp +13/−21; the only
v28-lineage deletion in it is the demotion of the uniform-margin proposition (§3 below);
everything else v70 touches is post-v28 hardening of v69 text (HJ paragraph re-scope,
notation-table fixes, ζ-display for the robust inequality, timing-figure caption,
Lean-provenance paragraph rewrite, §5(d) matrix data, summary-table resize, §6.4/§6.5
prose). The findings below are stated against v70.

## 1. Method

1. **Environment census.** All `theorem/proposition/corollary/definition/example`
   environments in v28 listed (15) and located in v70 main + supplement; v69→v70 diff
   re-checked line-by-line for v28-lineage deletions.
2. **Sentence-level coverage audit.** All 304 long v28 sentences fuzzy-matched
   (math/citation-normalized difflib) against the 967-sentence v69 main+supplement pool;
   the 108 below-threshold sentences were each hand-traced to their disposition; the v70
   delta was then overlaid.
3. **Phrase-survival checks** on the flagged signature passages (threshold remark,
   comparison-function extension, barrier duality, diagnostic force, injective-observation
   consistency check, notation disambiguation, ladder rungs, quantifier-order note,
   "stock recovering or collapsing", harvest vector, Nagumo, Marchaud, tube-safe action
   set, σ*, √q comparison).
4. **Bibliography diff** (39 v28 entries vs 50 main + 29 supplement) and
   **figure/table caption census** (6 figures + 1 table in v28 vs the current inventory).

## 2. What survives (everything of record)

- **14 of the 15 v28 statement-level objects survive as numbered environments in v70**
  (main `calc-*` and/or supplement S1): robust epistemic kernel (Def.), selector
  principle, finite-time exit certificate, epistemic emptiness by admissibility,
  common-action obstruction, obstruction ladder, hidden-mode example, delayed-information
  obstruction, finite-horizon soundness/completeness, exact certifier, observation-fibre
  criterion, safety-crossing-fibres corollary, monotonicity of the epistemic kernel,
  plus the comparison-function and threshold remarks. The finite-horizon proof is carried
  in full in S1. The 15th object is the uniform-margin proposition — demoted in v70 by a
  deliberate adjudication, not lost; see §3.1. v70 adds 13 further objects (LP
  instantiation, sparse/Helly witness, oracle-recourse, three-branch example, one-step
  completeness, static-observation reduction, two-phase decomposition, window-nogo, Open
  Problem 1, belief-state safety value, chance-constrained obstruction,
  deterministic-kernel limit, relaxation-gap example).
- **All six v28 figures and its summary table** survive (incompatible safe controls and
  delayed-information in main; ladder, one-step obstruction tree, fibre-crossing and
  certainty-equivalence trap in supplement; the certificate-summary table in main — now
  resizeboxed, with the uniform-margin row re-pointed to the held-action consequence).
- **All 39 v28 references** survive in the current main+supplement union.
- **Section-level:** v28 §1.2's five contributions + finite-horizon mechanism all appear
  in v70 §1.2 (plus two new); §2's notation disambiguation (H(ξ,v) vs harvest vector vs
  W-sets) stands; §5's four clusters (a) Veliov, (b) estimation tube, (c)
  observer-and-buffer, (d) linear substitution stand verbatim-headed in supplement S2
  (with §5(d) now carrying explicit matrix data); §6's institutional-kernel (IRViab)
  material, quantifier-order/circularity note, and limitations stand; Appendix A.1/A.2
  stand verbatim in supplement S3 with the newer A.3. The "stock recovering or collapsing"
  analogy, "rungs are strict", "quantifier order is essential", "unsuccessful search for
  a barrier", and "unsafety complement" passages all verified present in v70.

## 3. The v28 material the current line does *not* carry — and why it should stay out

### 3.1 The uniform-margin proposition (the one genuine post-v70 gap candidate — declined)

v28's `prop:uniform-margin` ("uniform margin gives a tube obstruction at every review
length": ∃η>0 such that each candidate a has a boundary state, active constraint and
disturbance with ∇q_j(x_a)·f(x_a,a,d_a) ≤ −η ⇒ A_tube(B,Δ)=∅ ∀Δ) survived v28→v69 as a
numbered proposition (already carrying the added (H2.3) path assumption), and **v70
demoted it to an unnumbered paragraph** in both main §3.2 ("Immediate consequence of the
held-action adverse-path premise") and supplement S1 — explicitly retiring the
uniform-η packaging: "no uniform η or uniform exit time is supplied … This is not a
numbered proposition or a claim against unrestricted within-review switching."

Restoration is **not** merited, for three reasons:
1. **The demotion is logically conservative.** v70 derives the same conclusion (tube
   emptiness at every review length, for the declared hold class) from strictly weaker
   assumptions — it drops the uniform η and the uniform exit interval entirely. v28's
   η-margin layer was already redundant in v69, since the (H2.3) exiting-path premise was
   assumed alongside it; restoring the numbered η-form would add a redundant hypothesis
   layer, not strength.
2. **The checkable part survives.** The genuinely useful v28 content — the finite
   gradient test as a *trigger* — remains in v70 at three sites: (H2.2)'s
   boundary-inequality form in the common-action theorem, the ladder's "original-system
   exiting paths (H2.3) whenever an active-gradient test fails", and the tube paragraph's
   "Instantaneous gradient tests imply this tube obstruction only under the
   original-system path premise (H2.3)."
3. **The demotion was a fresh, deliberate adjudication** by the parallel line ("demote
   A4, preserve held review gates"), consistent with the four-gates program; re-elevating
   it from v28 would undo a considered decision recorded in commit 2038cd2f.

### 3.2 The LSC / measurable-selection adverse-path derivations

v28's proofs of the exit, common-action, and delayed-information theorems derived the
adverse realization from lower semicontinuity of D via measurable-selection arguments
(its (H1.2)/(H3.3) realization clauses). The v67–v70 hardening replaced these derivations
with explicit original-system path hypotheses (H2.3, H3.2, H5.2) — the owner's gate 1.
The current line is on record against the old route: "No lower semicontinuity
inheritance for a thresholded disturbance correspondence, measurable feedback d(x), or
convexified-to-original transfer is presumed" and "No use is made of a
thresholded-correspondence LSC inheritance or an unproved closed-loop selection."
Restoring as-is would claim what the gates withdrew; restoring as an optional
sufficiency remark ("under LSC of D on the strip the (H5.2) pair exists by measurable
selection") is possible in principle but re-opens a settled gate decision to purchase a
remark the paper explicitly declines to lean on. Not merited.

### 3.3 The unconditional greatest-fixed-point thesis and the CQSP no-loss attribution

v28's "the epistemic kernel is the greatest recursively viable collection … in the sense
of the estimation-space reduction" is corrected in the current line to a form conditional
on exact rectangular belief dynamics and nonanticipative concatenation ("Without those
hypotheses, this is an organizational description rather than an exact
greatest-fixed-point theorem"). v28's CQSP-2007 "no loss of value / equality of value
functions" attribution is the exact claim verified as unverifiable in Task 139 and
re-scoped at four sites in v69 (estimation-space semantics carried by Kurzhanski–Vályi
1997; all value-coincidence statements conditional on matching policy/admissibility
hypotheses); v70 leaves those fixes intact. Restoring either would regress gates 1 and 4.

## 4. v28 passages superseded by corrected current versions (restoring would reintroduce errors)

- **State-dependent-decline extension** → the comparison-function remark corrects it: a
  finite comparison integral bounds only *first boundary contact* (the `\dot q=-\sqrt q`
  counterexample reaches zero and can stay there); strict exit requires a compatible
  continuation with negative drift at or through contact. v70's timing-figure caption now
  carries the same correction ("The bound need not equal the first contact time").
- **Emptiness construction's singleton-prior claim** (v28 overclaim) → current line
  admits singleton priors and restricts the empty-kernel statement to full-fibre
  starting beliefs.
- **Injective-observation consistency check** → current line adds the missing caveat
  that equality with a state-feedback robust kernel "requires an additional
  policy-class reduction."
- **Barrier "diagnostic force" passage** → survives in stronger, worked form in S2's
  one-system comparison ("The unsuccessful search for a barrier is inconclusive on
  emptiness"; "No general nonexistence of a state-dependent barrier is inferred solely
  from a fibre-constancy argument"). The v28-era fibre-constancy claim itself was
  corrected in later rounds.
- **§1.3 HJ-reachability contrast** → v28/v69's "the value function would have to live
  on an infinite-dimensional space of measures; level-set and physics-informed solvers …
  do not carry over" was re-scoped by v70 ("no claim that every Section 3 certificate is
  a finite algebraic object or that every partial-observation method requires an
  infinite-dimensional probability-measure grid is intended"; belief-state safety has
  its own information-state formulations). Restoring v28's phrasing would reintroduce
  the over-claim v70 just retired.
- **Threshold remark** → survives improved (`σ*_Π` class-specific form, strictness
  caveat, finite-checkability paragraph — none in v28).
- **"Two readings" remark / Isaacs reading / exit-below-ladder / rungs-strict** → the
  Isaacs reading stands with the d\* sufficiency discussion; rungs-strict and
  exit-below-ladder stand in S1's "Complete discussion of the obstruction ladder" block
  with Figure S1; the clairvoyant/intermediate-region phrasings are gone but their
  substance (unsafety complement of the converse; constructive; defeats all controls) is
  in §6.2's condensed text.

## 5. Verification status and disposition

- **No changes were made to any TeX source.** v70 (article + supplement) is the shipped
  line of record (remote tip fb03e538 at audit time); v68 and v69 remain byte-frozen as
  committed. This audit record is the only artifact.
- The audit was performed at source level (the .tex files), as with prior rounds; the
  supplement's standing note that article-to-supplement concordance "requires checking
  against compiled paginated proofs" is unaffected.
- **Recommendation:** any future version should continue to seed from the current line
  alone (now v70). The one conceivable v28-derived addition — an explicitly
  non-load-bearing LSC-sufficiency remark for (H5.2) — remains available if the owner
  ever wants it, but on this audit's evidence it is not merited: it buys nothing the
  gates need and re-opens text that was deliberately hardened.
