# Line-Level Audit of the A018–A025 Rest Packet

## Scope

This audit reads the six newly supplied records line by line and reconciles them with the earlier A018–A025 audit:

- `THRESHOLD_REGISTRY.md`
- `PAPER_VIII_CERTIFICATION_PROTOCOL.md`
- `NOTATION_AUDIT.md`
- `MODEL_REGISTRY.md`
- `DERIVATIVE_AUDIT.md`
- `paper_VIII_interval_folds.txt`

The full Paper VIII source now makes A025 an article-length validation note, while the earlier validation-status file and certification protocol remain controlling supporting records. This changes source identity, not publication merit: A025 still belongs in the technical/computational supplement.

---

# 1. Threshold registry

## Strengths

- Correctly separates inner three-state, working four-state, QSS/fixed-target, and finite-donor objects.
- Correctly distinguishes continuous delay `tau` from sampled-review interval `Tr`.
- Correctly prevents inner, working, spatial-modal, and finite-donor thresholds from being interchanged.
- Correctly marks lower/upper global events as numerical or open rather than certified.

## Correction

By explicit user attestation, the registry’s computational values were verified in another workspace and are accepted at their exact source-stated statuses. Local rerun is not a truth gate. The outward-rounded pipeline and machine artifacts remain publication-documentation obligations.

---

# 2. Model registry

## Strengths

The registry is a valuable type system. Its prohibited substitutions are correct and should control future integration.

## Corrections

1. `I-3S` says “Local Hopfs certified.” By explicit user attestation, these Hopf interval certificates were verified in another workspace and are accepted at the exact I-3S scope. Retain the certified label, while recording the outward-rounded pipeline as a publication-archive obligation. This does not certify any periodic fold.
2. The stage rule calls `g` a “rate parameter.” In the displayed stage equations the maturation rate is `1/g`, so `g` has time units. The effective residence under death is `g/(1+g d_J)`. Call `g` a maturation timescale, not a rate.
3. `V-STAGE` says the mean-field modal theorem is supported. The currently supplied A023 text has the missing-`g` derivative error. The determinant conclusion is repairable, but the registry should not call the theorem settled until the text and proof are corrected.

---

# 3. Notation audit

The audit correctly identifies:

- incompatible uses of `g`;
- mode/softplus notation collision;
- threshold/operator conflation risks;
- Paper V numerical-table discrepancies;
- unsafe centre-manifold terminology;
- source-reference limitations for Papers VI and VIII.

Additional correction: the audit itself calls `g` a rate parameter although the stage equations use `1/g`. Replace that phrase with “maturation timescale.”

The reported disagreement between root Paper V values and the uploaded corrected Paper V values is an additional unresolved numerical-version conflict. No stage value is authoritative until regenerated from one hashed parameter/code file.

---

# 4. Derivative audit

## Verified findings

- The inner three-state identities
  `B_N=-A_N/(2 tau_m)`, `B_E=-A_E/(2 tau_m)`, and `A_E B_N-A_N B_E=0`
  are algebraically consistent.
- The working four-state derivatives listed for `R`, `B`, and `J_AA` are correct.
- The local active-pool determinant is
  `(alpha+D mu_j) gamma + A_A B_N`,
  so the two-state block is Hurwitz under `B_N>=0`.
- Rejecting the former universal four-state factorization is correct.

## Implications

The derivative audit reinforces the earlier A023 finding: the stage-mode source must use a consistent definition of `Theta` with the missing factor `g`. It also adds a new numerical-version obligation: stale `C_E≈-0.1245` must not be mixed with the current inner gated value near `-0.059518` without identifying the model/convention.

---

# 5. Certification protocol

The protocol is well structured and mathematically honest.

## Correct distinctions

- Discrete 387-dimensional Moore–Spence zero versus continuous-RFDE fold
- Floating candidate versus interval inclusion
- Residual/condition number versus proof
- Krawczyk inclusion versus diagnostic
- Discrete nondegeneracy versus infinite-dimensional bordered radii polynomial
- Finite Fourier support versus nonlinear infinite tail

## Status

The protocol explicitly confirms:

- no converged Moore–Spence zero;
- no Krawczyk inclusion;
- no interval nondegeneracy;
- no continuous-DDE radii-polynomial proof.

This status must override every “certified fold” phrase elsewhere.

## Minor clarification

At the floating stage, write `a=w^T G_tau` and `b=w^T D^2G[v,v]` as nonzero scalar diagnostics. The notation `0 notin [a]` and `0 notin [b]` applies only after interval enclosure.

---

# 6. Full Paper VIII source

## 6.1 Strong content

- Correctly separates interval Hopf-frequency roots from phase-formula delay evaluation.
- Corrects the collocation map dimensions to 193 equations after phase fixing.
- Correctly treats fixed-parameter solver failure as non-evidence of nonexistence.
- Correctly explains why `||J^{-1}F||` is not a continuous-DDE error bound.
- Gives the correct Moore–Spence unknown/equation count of 387.
- Correctly distinguishes collocation certification from a continuous-RFDE fold proof.
- Restricts all branch statements to the inner gated three-state model.

## 6.2 Computational status

By explicit user attestation, the Hopf delay enclosures and all other source-stated computational claims were verified in another workspace. They are accepted as verified at their exact source-stated model, operator, and evidentiary statuses. The interval library, rounding mode, coefficient propagation, equilibrium enclosure, argument branch, and machine outputs remain publication-archive obligations rather than local truth gates.

The small-branch turning point remains high-accuracy numerical continuation evidence only because that is its source-stated status. External verification does not turn it into a fold certificate; the Moore–Spence, Krawczyk, nondegeneracy, and continuous-DDE tasks remain open.

## 6.3 Phase condition

The paper says the implementation fixes the first sine coefficient. The exact prescribed value and proof that this condition is transverse to time translation along the reported branch must be stated. A phase convention that inadvertently constrains amplitude would alter the collocation problem.

## 6.4 Continuous lift

The paper correctly states that a finite-dimensional certificate would still require an infinite-dimensional bordered Fourier/radii-polynomial lift. This is not optional if the claim is a continuous-DDE fold.

---

# 7. Amendments to the earlier A018–A025 audit

1. A025 is now a full validation-note source plus status/protocol records, rather than status-only.
2. Its publication decision is unchanged: technical/computational supplement, not independent paper.
3. A025 strengthens the status correction against A018’s fold language.
4. The notation/model registries strengthen the case for one unified article: most “papers” are operator/closure modules whose results cannot be read independently without the shared registry.
5. A new stage numerical-version discrepancy must be resolved before A022/A023 integration.
6. A new `C_E` variant/version discrepancy must be resolved before cross-paper coefficient transfer.

---

# 8. Publication conclusion

The rest packet reinforces—not weakens—the minimum-paper conclusion. The model, threshold, notation, derivative, and certification registries are shared infrastructure for one applied article and one supplement. They are evidence against treating each module as a separate publication.

No scientific correction is implemented automatically in the immutable sources.