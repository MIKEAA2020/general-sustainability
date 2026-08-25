# PROOF_REAUDIT — Independent Line-by-Line Re-verification of the Reconstructed Theorems

**Scope.** The 27 rows in `PROOF_MANIFEST.md` carrying the `reconstructed` qualifier (lines 72–84 and 90–103) — the same-agent reconstructions that `TRANSFER_AUDIT_RESPONSE.md` Finding 1 names as carrying an open independent-verification obligation. Ten files were read in full:

`batch 2/02_elevation/` — `E1_LANGUAGE_COMPLETENESS.md`, `E2_SELECTORS_AND_CERTIFICATES.md`, `E3_CLASSIFICATION_THEOREMS.md`, `E4_INTERGENERATIONAL_PRODUCTION.md`, `E7_CONSERVATION_VIABILITY_COUPLING.md`
`batch 2/04_open_problems/` — `A3_VARIABLE_EVENT_KERNEL.md`, `A4_NONLINEAR_SMALL_GAIN.md`, `B_TIER_BRIDGES.md`, `CA_EXECUTION.md`, `C_TIER_COMPLETIONS.md`

Cross-checked against the controlling sources actually present in the repository: `research_program/general_theory_math_closure_packet/corrected_theorems/01…09_*.md`, `batch 2/01_result_records/R01…R09`, `PROOF_MANIFEST.md`, `JOINT_AUDIT_ASSESSMENT.md`.

**Reproducibility.** Every Class-1 refutation and every confirmation is reproduced by `reaudit/verify_findings.py` (34 assertions, exit 0). Saved output: `reaudit/run_output.txt`.

---

## Headline

The reconstruction is **substantially sound but not uniformly sound**. All 27 `reconstructed` rows were read; disposition of each:

| Disposition | Rows | Count |
|---|---|---|
| Verified correct, no defect found | E1.A1, E1.A2, E2.B1(b), E3.C1, E3.C4.1, E3.C4.2, A4.Thm2, C-a.Thm2 | 8 |
| **False as stated** — refuted by explicit counterexample | A3.Thm1, B6.Thm1 (part 1), E4.Thm2 (budget paragraph), E4.Lem1 (part ii) | 4 |
| Proof gap — the argument does not establish the stated conclusion | E2.B2(a), E2.B1(a), E3.C6.3, B1.Thm1, B9.Thm1, B10.Thm1, C-a.Thm3 | 7 |
| Definitional / sign / scope defect | E7.Thm1, E7.Thm2, A3.Thm2, A3.Thm3, A4.Thm1, B7.Thm1, C-e.Thm1, C-f.Thm1 | 8 |

**27 findings** are itemised below (some rows carry more than one; `E7.Cor3` and `A4.Thm1-Explicit` are file-level results without their own manifest rows and are covered under findings 13 and 20). Of the 8 gap rows, **all 8 conclusions survive** under the stated repair. Of the 4 false rows, **3 are repairable** and one — `E4.Thm2`'s budget analysis — is not merely wrong but wrong in the direction that flatters the result.

**Two of the four false statements are load-bearing.** `A3.Thm1`'s compactness is the foundation `A3.Thm3` rests on, and `A3.Thm3` is what `B8` composes with `E4`. `B6.Thm1(1)` is the nonlinear substitution classification that `E3.C2` and `E7.Thm2` cross-reference.

**Verified good news:** the closure packet's integrity anchor checks out. `HANDOFF.md` §1 pins SHA-256 `51acc3a7…2f49e`; `sha256sum research_program/general_theory_math_closure_packet.tar.gz` returns exactly that value. The packet is present in the repo (`research_program/general_theory_math_closure_packet/`), so every packet citation in these files is resolvable — contrary to a first reading of `HANDOFF.md` §2's "Not included (get from the packet)", which refers to the batch-2 bundle, not the repository.

---

# Class 1 — False as stated

## 1. A3.Thm1 — interleaved-segment compactness is FALSE (highest severity)

**The claim** (`A3_VARIABLE_EVENT_KERNEL.md`): `ℋ` = piecewise-continuous `φ : [−τ,0] → ℝⁿ` with at most `B` breaks, jumps bounded by `J`, path bounded by `M`, is compact in `τ_IS`, where `τ_IS`-convergence requires **uniform** convergence on each inter-break segment.

**Refutation.** Take `B = 0`, `τ = 2π`, `M = 1`, and `φ_k(s) = sin(ks)`. Every `φ_k` satisfies the declared hypotheses (no breaks, bounded by 1, no jumps). The minimum pairwise sup-distance across `k = 1…8` is **1.7602** — the family has no Cauchy subsequence, hence no convergent subsequence in `τ_IS`. `ℋ` is not sequentially compact.

**Why the proof fails.** The proof anticipates the difficulty ("they are not equicontinuous … so Arzelà–Ascoli does not apply directly") and reaches for a Helly-type selection. Helly selection requires **uniformly bounded total variation**; here `TV(sin(ks)) = 4k → ∞`. The "interleaving" repair (constant continuation from segment endpoints) does not create equicontinuity. Boundedness plus a break budget plus a jump bound is simply not a compactness hypothesis for a space whose topology demands uniform segment convergence.

**Repair.** Add one of: a uniform modulus of continuity on inter-break segments (equicontinuity), a uniform total-variation bound, or a uniform Lipschitz constant per segment. The first is the natural one and is what the downstream uses actually need.

**Propagation.** `A3.Thm3` states "compactness from A3.Thm1" and `B8` composes `A3.Thm3` with `E4`. Both inherit the gap. `A3.Thm3` is already labelled `PROVEN_CONDITIONAL`; the condition list should now include segment equicontinuity. `B8` is already `CONDITIONAL`.

---

## 2. B6.Thm1(1) — MFCQ does not stabilize feasible directions

**The claim** (`B_TIER_BRIDGES.md`, B6 part 1): under MFCQ at every nearby point, "the feasible-direction property is **stable**: `d` is a feasible direction at `x̄` iff it is at every nearby `x`".

**Refutation.** `𝒢 = {(x,y) : y ≥ x²}`, i.e. `g(x,y) = x² − y ≤ 0`; `x̄ = (0,0)`; `d = (1,0)`.

| point | `∇g` | `⟨∇g, d⟩` | `d` a feasible direction? | MFCQ? |
|---|---|---|---|---|
| `(0,0)` | `(0,−1)` | `0` | **yes** | yes |
| `(½,¼)` | `(1,−1)` | `1` | **no** | yes |
| `(1,1)` | `(2,−1)` | `2` | **no** | yes |
| `(2,4)` | `(4,−1)` | `4` | **no** | yes |

MFCQ holds at every point (`∇g = (2a,−1) ≠ 0`), yet `d` is a feasible direction at `x̄` and at no nearby boundary point. The second half of the claim ("the projection of `𝒢` onto the pathway coordinate is locally constant") fails on the same example.

**Diagnosis.** MFCQ gives lower semicontinuity of the feasible-set mapping and continuity of the *linearized* cone `{v : ∇g_A(x)v ≤ 0}` — it does not make membership of a fixed `d` locally constant, because the linearized cone rotates with `x`.

**Repair.** Restate as stability of the *strictly* feasible-direction property (`⟨∇g_A, d⟩ < 0`, an open condition), or as continuity of the linearized cone in the Painlevé–Kuratowski sense with the consequence that `d` feasible at `x̄` implies `d` feasible at nearby points *up to an `O(‖x−x̄‖‖d‖)` correction*. The Clarke certificate in part (2) is unaffected — see the Verified list.

---

## 3. E4.Thm2 — the budget-solvability analysis is arithmetically wrong

**The claim** (`E4_INTERGENERATIONAL_PRODUCTION.md`): for `r_{g+1} = ℓ·r_g − b`, nonnegative solutions on `{0…G}` exist **iff** `r_0 ≥ b(ℓ^G − 1)/(ℓ − 1)`; and for `G = ∞`, "`ℓ < 1` with `r_0 ≥ b/(1−ℓ)` (geometric budget), or `b = 0` with `ℓ ≤ 1`".

**Both are wrong.** Solving the recursion, `r_g = ℓ^g r_0 − b(ℓ^g − 1)/(ℓ − 1)`, and requiring `r_g ≥ 0` for all `g ≤ G` gives

```
r_0  ≥  max_{1≤g≤G}  b(ℓ^g − 1) / (ℓ^g (ℓ − 1))
```

— the record's formula is missing the `ℓ^{−g}` factor. Verified:

| `ℓ` | `b` | `G` | record's `r_0` | resulting sequence | nonneg? | true threshold |
|---|---|---|---|---|---|---|
| 0.5 | 1 | 2 | 1.5000 | 1.5, **−0.25**, −1.125 | ✗ | 6.0 |
| 0.5 | 1 | 5 | 1.9375 | 1.9375, **−0.031**, … | ✗ | 62.0 |
| 0.9 | 0.1 | 4 | 0.3439 | 0.3439, 0.2095, 0.0886, **−0.020** | ✗ | 0.5242 |

The infinite-horizon branch is worse — it names the wrong side of the fixed point. `r ↦ ℓr − b` has fixed point `−b/(1−ℓ) < 0` for `ℓ < 1`, so the sequence **always** eventually goes negative when `b > 0` and `ℓ ≤ 1`. The record's `r_0 ≥ b/(1−ℓ)` is the fixed point of `ℓr + b`. Verified: `ℓ=0.5, b=1, r_0=2` gives `2, 0, −1, −1.5, …`.

**Correct statement.** Nonnegative on all of `{0,1,2,…}` **iff** `b = 0` and `ℓ ≤ 1` (any `r_0 ≥ 0`), **or** `ℓ > 1` and `r_0 ≥ b/(ℓ−1)`.

**Why this matters beyond the arithmetic.** This recursion *is* the module's quantitative reading of intergenerational sustainability — "the initial margin must cover the compounded jump deficit". As written it tells the reader that a contracting reset (`ℓ < 1`) is sustainable given enough initial margin. It is not: a contracting reset with any per-jump deficit is unsustainable at any initial margin. The honest negative finding is stronger than the one recorded, and it points the opposite way.

---

## 4. E4.Lem1(ii) — the declared-data refutation claim is false as written

**The claim.** For the displayed witness family on `K_g = K_{g+1} = [0,1]` with `φ_g(r) = λ_g r` near 0, `λ_g ↓ 0`: "**no uniform `(ℓ, b)` with `b < ∞` exists**".

**Refutation.** Depth in `[0,1]` is `min(r, 1−r) ≤` inradius `= ½`, and the margin condition `R_g(K_{g,−r}) ⊆ K_{g+1,−(ℓr−b)}` is read as `K_{g+1}` whenever `ℓr − b ≤ 0`. So `(ℓ, b) = (1, ½)` — and indeed any pair with `b ≥ ℓ · inradius` — satisfies the definition **vacuously for every `g`**. A uniform margin with finite `b` trivially exists.

**The real finding, stated precisely.** The margin *definition* is degenerate as written: it admits vacuous pairs. The refutation has teeth only after adding the non-vacuity demand `b < ℓ · r̄_g`. Under that demand the witness does work — verified: `(ℓ,b) = (1, 0.4)`, `(0.5, 0.2)`, `(0.2, 0.05)` all fail at `λ = 1/20`, with deficits `−7.5e−2`, `−2.5e−2`, `−2.5e−2`.

**Repair.** Add `b < ℓ·r̄_g` (non-vacuity) to the margin definition, then the refutation stands verbatim. As it stands, the lemma's own definition undermines its own point, and `E4.Thm2` consumes the margin without the non-vacuity guard — which is how finding #3's wrong-but-plausible budget formula went unnoticed.

---

# Class 2 — Proof gaps

## 5. E2.B2(a) Step 3 — closed-set upper inverses do not give KRN weak measurability
The proof shows `{x : A_W(x) ∩ F ≠ ∅}` is closed for **closed** `F`, then concludes "`A_W` is weakly measurable in the KRN sense". KRN requires `{x : A_W(x) ∩ O ≠ ∅}` measurable for **open** `O`; for an usc correspondence these are different conditions.
**Repair (one line).** In a metric space write `O = ⋃ₙ Fₙ` with `Fₙ = {y : dist(y, O^c) ≥ 1/n}` closed. Then `{x : A_W(x) ∩ O ≠ ∅} = ⋃ₙ {x : A_W(x) ∩ Fₙ ≠ ∅}`, a countable union of closed sets, hence Borel. **Conclusion survives.**

## 6. E2.B1(a) — "consistency is inherited by subfamilies" is backwards
The proof asserts that any `(C,c)` with `C ⊆ 𝒱*` is a consistent certificate family. From `C ⊆ 𝒱*` and monotonicity one gets `Γ(C) ⊆ Γ(𝒱*) = 𝒱*` — the wrong direction. Post-fixedness (`C ⊆ Γ(C)`) is not inherited downward. Verified on a 3-point monotone certificate operator with `𝒱* = {1,2}`: `C = {1} ⊆ 𝒱*` but `Γ(C) = ∅`, so `C` is not post-fixed.
**Repair.** State the transfer for post-fixed points, or for subfamilies of a *post-fixed* `C`. The Knaster–Tarski core of the theorem is correct.

## 7. E3.C6.3 (⟹) — an example is cited where a proof is needed
The (⟸) direction is sound. The (⟹) direction ("delayed information inert **iff** the obstruction is unreachable before `t_d`") is supported only by "the R02.Prop3 construction … exhibits a strictly smaller delayed kernel" — one witness, not a general argument. The (⟸) hypothesis is also stronger than the statement suggests: "no trajectory … under *any* policy admissible for the prior" makes every prior-admissible policy safe by assumption.
**Repair.** Either prove the (⟹) direction or restate as a one-directional lemma with the witness recorded as a sharpness example.

## 8. B1.Thm1 — the conclusion is stronger than the hypotheses support
Hypotheses give: `K_{−r/2}` forward-invariant at sample times, and every inter-sample trajectory from `K_{−r/2}` stays in `K`. The stated conclusion — "`K_{−r}` is safe … replacing `K` by `K_{−r}` throughout … yields the `r`-eroded statement verbatim" — requires the successor certificate (hypothesis 3) at depth `3r/2`, which is not supplied.
**Repair.** State the conclusion at the depth the hypotheses actually deliver (`K_{−r/2}` invariant at sample times; `K` maintained throughout), or strengthen hypothesis 3 to the deeper erosion.

## 9. B9.Thm1(1) — the reverse inclusion is hand-waved
The forward inclusion and the Fatou closedness step are fine. The reverse inclusion is written as: "a policy with `ℙ(safety) ≥ p` induces … conditional survival probability whose quantiles satisfy the budget split ***somehow***". The recursion's hypothesis is a **quantile-set inclusion** (`Q_{p_k}(x'; ℒ) ⊆ W_k`), strictly stronger than a conditional-probability budget; the passage from one to the other is the whole content and is not given.
**Repair.** Prove the quantile-set inclusion under support alignment, or restrict the claim to the forward inclusion and record the reverse as open.

## 10. B10.Thm1(1) — "optimistic and pessimistic readings coincide" is asserted
The proof establishes only that the pessimistic objective `c ↦ min_{π∈BR(c)} v_l(c,π)` attains its maximum. (It is in fact continuous by Berge, not merely usc — the proof undersells this.) Equality of the optimistic and pessimistic values requires `BR` single-valued or `v_l` constant on `BR` fibres; neither is assumed. Also, the displayed `v_l(c*,π*) = max_c min_{π∈BR(c)} v_l(c,π)` does not follow: `π* ∈ BR(c*)` need not attain the inner minimum.
**Repair.** Drop the coincidence claim, or add the hypothesis that makes it true.

## 11. B10.Thm1(2) — "closed graph inheritance" fails under Berge alone
`{c : BR(c) ⊆ F}` need not be closed for closed `F` when `BR` is only usc with compact values, which is all Berge supplies. Verified counterexample: `Π = {a,b}`, `v_f(c,a) = 0`, `v_f(c,b) = −|c|`, so `BR(c) = {a}` for `c ≠ 0` and `BR(0) = {a,b}`. `BR` is usc with compact values, yet `{c : BR(c) ⊆ {a}} = (−1,1] \ {0}` — not closed.
The analogy to "E2's Step 2" does not hold: E2 had **Hausdorff** continuity of `Succ` (both directions); Berge gives only upper.
**Repair.** Add lower semicontinuity (or single-valuedness) of `BR`, or restrict to the existential form `{c : BR(c) ∩ F ≠ ∅}`, which *is* closed under usc.

## 12. C-a.Thm3 — the arbitrariness lower bound needs a separation the language does not have
The proof needs "two instantiations differing in any successor-table entry … are separated by an atomic claim". Kernel-membership atoms do not separate table-distinct models. Verified: `X_h = {a,b}`, `K = {a,b}`, tables `Succ(a,·,·) = {b}` versus `Succ(a,·,·) = {a,b}` (identical at `b`) give the **same** viability kernel `{a,b}`.
**Repair.** Replace "arbitrary subsets of the lattice" with "arbitrary subsets *definable in the kernel-membership language*", and note that table-distinct models can be language-indistinguishable. The per-instance decidability half is unaffected.

---

# Class 3 — Definitional, sign and scope defects

## 13. E7.Cor3 and C-e misidentify `L_G` (conceptual, affects two rows)
The controlling definition is in `research_program/general_theory_math_closure_packet/corrected_theorems/02_operator_I_strong_invariance_and_erosion.md`, Lemma 2: `L_G` is the **Hausdorff–Lipschitz modulus of the velocity envelope** `G`,
```
d_H(G(x), G(p)) ≤ L_G ‖x − p‖   in the inner tube,
sup_{v∈G(p)} ⟨n(p), v⟩ ≤ −α < 0   on ∂K,
L_G r + Δ_ε ≤ α  ⟹  K_{−r} strongly invariant.
```
`L_G` is a property of the **dynamics**, not of the barrier.

- `E7.Cor3` claims `L_G = 0` for affine barriers because "the normal is constant". Under the packet's definition this is false: an affine constraint with a Lipschitz-varying velocity envelope has `L_G > 0`.
- `C-e` computes `L_G = inf{2√(xᵀM²x) : B(x) = b}` — a lower bound on `‖∇B‖`, again a barrier-geometric quantity.

What *is* true for affine barriers, and is presumably the intended point: the signed distance to a half-space is globally linear, so Lemma 2's two-sided tubular radius and `C^{1,1}` signed-distance hypotheses hold **without a radius restriction** — the erosion calculus applies globally rather than locally. That is a real and useful statement; it is not `L_G = 0`.

**Repair.** Introduce a separate symbol (e.g. `L_B`) for the barrier-geometry constant, keep `L_G` for the packet's envelope modulus, and restate Cor3/C-e in terms of `L_B`. `PROOF_MANIFEST.md`'s `C-e.Thm1` row ("Quadratic moiety sandwich with `L_G > 0`") needs the same change.

## 14. A4.Thm1 Step 2 — sign inconsistent with the controlling packet
The file writes `⟨n_i, f_i(x_i,u)⟩ ≤ α_i + L_i r*_i` and "the encroachment `Λ_i Σ_j δ_ij(r*_j) + Δ_i` is covered by `α_i + L_i r*_i`". The packet's Lemma 2 has `α` entering **negatively** (`⟨n,v⟩ ≤ −α < 0`) with the erosion terms **added** (`⟨n,w⟩ ≤ −α + L_G r + Δ_ε ≤ 0`, closed by `L_G r + Δ_ε ≤ α`). The step should read
```
⟨n_i, f_i(x_i,u)⟩  ≤  −α_i + L_i r*_i + Λ_i Σ_j δ_ij(r*_j) + Δ_i  ≤  0
```
with the last inequality being exactly `(∗)` from Step 1. The conclusion of Thm1 survives — Step 1 and the packet's Lemma 2 do the work — but the displayed step as written is not the packet's inequality.

## 15. E7.Thm2 — the noncompensation claim contradicts the file's own sanity check
"a deficit in moiety `i` (i.e. `q_{L_i}(0) < D_{i,T}`) cannot be compensated … the compensated state is outside the kernel". Deficit relative to the **committed budget** does not exclude kernel membership — the inner rule is conservative by construction. The same file's E5 sanity check says exactly this: "the floor's `D_T = 0.4·T` is **conservative against the true kernel** `S ≥ 2`". Only deficit relative to the **outer** bound `D⁻_T − F⁺_T` forces non-membership.
**Repair.** Replace `D_{i,T}` with `D⁻_{i,T} − F⁺_{i,T}` in the noncompensation clause.

## 16. E7.Thm1(b) and (c) — hypothesis/conclusion mismatch and a sub-sharp bound
- **(b)** "moreover **every** trajectory exits the floor within time `q_L(0)/γ`" requires `F ≤ 0` for all realizations. The first hypothesis ("`F ≡ 0` is possible") supports only `Viab_T = ∅` — the robust-kernel half, which is what makes it an adversarial-exit certificate. The two disjuncts in the hypothesis support different halves of the conclusion.
- **(c)** The proof establishes `q_L(0) ≥ D⁻_T − F⁻_T` (adversarial inflow is the **lower** bound `F⁻`). The displayed bound substitutes the **upper** bound `F⁺_T` and calls it "crediting the best-case relief". The displayed inequality is true but strictly weaker than what was proved, and it loosens the (d) sandwich. `C-e`'s sandwich repeats the same substitution (`{B ≥ Φ⁺_T − Φ⁻_T}` where the proof gives `{B ≥ Φ⁻_T}`, which is sharp).
- Notation: (d)'s inner bound is written `{q_L ≥ D⁺_T-budget}` while rule (a) uses the committed budget `D_T`.

## 17. A3.Thm2 — typing inconsistency between statement and proof
The statement has `W ⊆ 𝒜 × ℬ_info` "(finite × compact)"; the proof requires `ℬ` **finite** ("the finite lattice of subsets of `𝒜 × ℬ_finite`") for the termination claim. With `ℬ_info` merely compact, `Pre_𝒜` is still monotone and the gfp exists by Knaster–Tarski, but the recursion need not terminate. Also: "`≤ |𝒜| · dim` steps" — `dim` is undefined; the correct bound is at most `|𝒜 × ℬ|` strict decreases. And "`Pre_𝒜(W)` is clopen" is vacuous once the space is finite (every subset is clopen), so it is either trivial or, if `ℬ` is infinite, unjustified.

## 18. C-f.Thm1 — statement is general, proof is scope-locked
The Statement quantifies over an arbitrary observable `π : C([−τ,0],ℝⁿ) → Y`; the proof establishes the (⟹) direction only for "restriction-type/window observables" and says so in a parenthetical. The (⟸) direction is correct and standard for the truncated-history case.
**Repair.** Move the window-observable restriction into the Statement.

## 19. B7.Thm1(3) — genericity claim needs an unfolding hypothesis
"the transversal-contact parameter values form a residual (dense `G_δ`) subset" is attributed to jet-transversality. Thom's jet transversality yields genericity for a *versal/unfolding* family; an arbitrary one-parameter family `λ ∈ Λ` need not be transversal for residual `λ`. Parts (1) and (2) are unaffected, and (1)'s "uniform exhaustion radius … structural stability gives" is a plausible but unelaborated step.

## 20. Minor
- **C-a.Thm2 complexity.** "`O(G·|U|·|D|)` bit operations" per `Pre` step undercounts the subsethood tests by a factor of `G`; the honest figure is `O(G²·|U|·|D|)` bit operations, or `O(G·|U|·|D|)` word operations. The overall `O(N·G·|U|·|D|)` headline is unaffected under the word-parallel convention, which the file should name.
- **E3.C2.** The Statement's Farkas alternative is written `y^⊤A ≤ 0`, the Proof's `y^⊤A = 0`. Both are valid variants of the homogeneous alternative, but the file should pick one. Typo: "surflux".
- **A4.Thm1-Explicit.** The composite condition is `δ₁₂(δ₂₁(r)) ≤ r` — non-strict. In the linear shadow this gives `γ₁₂γ₂₁ ≤ 1`, whereas the "Reading" says it replaces `γ₁₂γ₂₁ < 1` (R05.Cor3's strict form). At equality the feasible set is a ray with no least positive contract, which is exactly why R05.Cor3 is strict. Worth one clause.
- **A4 Setting-section lemma** writes `φ_i(s) = φ_i(r*)` where the correct relation is `φ_i(s) ≥ φ_i(r*)`; `A4.Thm2`'s proof of the same point gets it right.
- **E1.A1 Move 1.** "the two readings are definitionally the same set" — equivalence of adversary-promotion versus input-quantifier requires the promoted block's trajectory set to coincide with the admissible disturbance class. That is a hypothesis, not a definition.

---

# Verified correct

Re-derived from scratch, no defect found:

- **E3.C1 in full** — the complete scalar-delay classification. Step 1's `|λ+α| = |β|` half-plane argument; Step 3's crossing direction, where I independently reproduced `Re λ̇ = ω²/|1+τα+iτω|²` from `λ̇ = βλe^{−λτ}/(1−βτe^{−λτ})` and confirmed it equals the implicit-differentiation value to 10 digits (`0.3237274894`); Step 4's `τ* = arccos(−α/β)/√(β²−α²)`; Step 5's monotone-count argument. Root-tracking confirms the sign change across `τ*` (`α=1, β=2, τ*=1.209200`: max `Re λ` = −0.00398 at `0.99τ*`, +0.00385 at `1.01τ*`).
- **E3.C3** — the two-patch moment closure `ṁ = m²+v`, `v̇ = 4mv`, verified to machine precision.
- **E3.C4.1, C4.2** — definitional unfolding and the compactness/horizon argument, both correct.
- **E2.B1(b) in full** — the decreasing-iteration/gfp identification, including the Vietoris-convergence and closed-graph steps. This is the cleanest proof in the set.
- **E2.B2(a) Steps 1, 2, 4** — closed values, closed graph, KRN application.
- **E2.B1(a) Knaster–Tarski core** — complete-lattice structure of `𝒦(X)`, gfp existence, the post-fixed-point formula.
- **A4.Thm2 parts 1–4** — meet-closure, the Tarski least-fixed-point argument, the genuineness gate, and the Kleene construction. The truncation-semantics theory is correct and, unusually, honest about the Kleene/Tarski boundary.
- **A4.Thm1-Explicit** and **A4.Ex3** — the two-module composite condition (both directions) and the nonconvex-control sharpness witness.
- **E4.Thm2's inductive proof** — base, boundary step, concatenation. Only the appended budget analysis fails.
- **E7.Thm1(a)** and the first half of **(b)**; **E7.Thm2**'s inclusion half.
- **C-a.Thm2 Steps 1–3** — the fixed-point structure of all eight families' recursions and the Boolean closure.
- **B6 part (2)** — the Clarke-cone separation argument is correct given a blocking point; only part (1) fails.
- **B9's Fatou step** — `ℙ(limsup A_n) ≥ limsup ℙ(A_n)` follows from the stated pointwise inequality.
- **B10 part (1)'s existence half** — Berge plus compactness.
- **Packet integrity** — SHA-256 of `research_program/general_theory_math_closure_packet.tar.gz` is `51acc3a760e2a08f2ccc68aa5bacf9aea8a36434aa9047e2a6f7a4902932f49e`, matching the `HANDOFF.md` §1 anchor exactly.

---

# Status-register consequences

If these findings are accepted, `PROOF_MANIFEST.md` needs the following corrections. Per TCS-1.0 §9 axiom 5 (status monotonicity), all moves are demotions or scope-locks — none is a promotion.

| Row | Current | Proposed | Reason |
|---|---|---|---|
| A3.Thm1 | PROVEN (reconstructed) | **FALSE_AS_STATED / repairable** | compactness refuted (sin ks); needs segment equicontinuity |
| A3.Thm3 | PROVEN_CONDITIONAL (reconstructed) | PROVEN_CONDITIONAL, condition list extended | inherits A3.Thm1 |
| B6.Thm1 | PROVEN (reconstructed) | **PROVEN_CONDITIONAL** — part (2) only | part (1) refuted (parabola witness) |
| E4.Thm2 | PROVEN (reconstructed) | PROVEN (reconstructed) **with the budget paragraph corrected** | recursion analysis false; corrected form is a *stronger* negative |
| E4.Lem1 | PROVEN (reconstructed) | PROVEN (reconstructed) **with non-vacuity hypothesis added** | margin definition degenerate as written |
| E7.Cor3 | PROVEN (reconstructed) | **restate** with a barrier constant `L_B` | `L_G` misidentified against packet 02 Lemma 2 |
| C-e.Thm1 | PROVEN (reconstructed) | **restate** with `L_B` | same |
| E7.Thm2 | PROVEN (reconstructed) | PROVEN, noncompensation clause re-scoped to the outer bound | contradicts the file's own E5 check |
| B9.Thm1 | PROVEN (restricted; reconstructed) | PROVEN (restricted), **forward inclusion only** | reverse inclusion not proved |
| B10.Thm1 | PROVEN (reconstructed) | PROVEN for existence; **reduction license conditional** on `BR` lsc | closed-graph inheritance refuted |
| C-a.Thm3 | PROVEN (reconstructed) | PROVEN, arbitrariness re-scoped to language-definable subsets | atoms do not separate tables |
| E2.B2(a) | PROVEN (reconstructed) | PROVEN (reconstructed) — one-line measurability repair | KRN direction |
| E2.B1(a) | PROVEN (reconstructed) | PROVEN (reconstructed) — subfamily claim re-scoped | monotonicity direction |
| E3.C6.3 | PROVEN (reconstructed) | PROVEN one direction; converse recorded as witnessed | ⟹ not proved |
| B1.Thm1 | PROVEN (reconstructed) | PROVEN at the delivered depth; conclusion re-scoped | successor certificate depth |
| C-f.Thm1 | PROVEN (reconstructed) | PROVEN (window observables) | statement/proof scope |
| B7.Thm1 | PROVEN (reconstructed) | PROVEN (1),(2); (3) needs an unfolding hypothesis | genericity |
| R02.Cor6 | PROVEN_CONDITIONAL (sampled-data erosion bridge open) | **reconcile with B1** | `B_TIER_BRIDGES.md` claims B1 "closes R02.Cor6's bridge" while manifest line 46 still records the bridge as open. One of the two is stale. |

---

# What I did not verify

Stated plainly, so nothing below is mistaken for a checked result.

- **The 43 plain `PROVEN` rows** — the packet bases B1–B8 and the batch-2 records R01–R09 — were not re-audited. This pass covered only the 26 `reconstructed` rows. The packet and records are present and verifiable; that is a separate and larger job.
- **`E5` and `E6`** carry no `reconstructed` label and were read only where the E-wave files cross-reference them (E7's sanity check, B2's Michael class).
- **Wave E numerics** (`wave_e_cod`, `wave_e_edwards`) were not run. That is item 2 of the agreed plan.
- **The `.tex`/`.docx` manuscripts** were not checked for claims that outrun these statuses. That is item 3.
- **Judgments of novelty** against the external literature were not attempted. Several results here (E3.C1's classification, E2's Knaster–Tarski and KRN applications, B10's Berge argument) are standard or near-standard; the files mostly say so, but I did not check the novelty register against sources.
