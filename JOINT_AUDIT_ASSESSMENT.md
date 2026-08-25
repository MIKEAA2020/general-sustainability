# Joint Audit Assessment — Batch 2 (R01–R09) × Batch 3 (five external audits) × independent re-audit

**Scope.** This document (a) re-audits the nine result records of `batch 2` independently and *before* reading `batch 3`; (b) reads all five batch-3 audits (deepseek, gpt, qwen, grok, grok 2); (c) adjudicates every disagreement between audits with explicit counterexamples; (d) corrects the errors found **in the audits themselves**; and (e) specifies the consolidated repair set that is then implemented in the record files.

**Verification method.** Every load-bearing witness was re-verified computationally (branch arithmetic, closed-form solutions, Grönwall checks, moment identities, characteristic-root crossings) or by explicit construction. Counterexamples against proposed repairs were tested the same way. Nothing below rests on authority.

---

## 1. The six audits at a glance

| Audit | Character | Line-level findings | Errors in the audit |
|---|---|---|---|
| **deepseek** | Focused defect list (8 items) | R06.Thm2 criterion invalid; R03.Lem4 gap; R05.Cor3 "iff" overclaim; R09.M1 local-only; R09.M5 kernel wrong; R02 "computable"; R07.Thm5 ill-typed nesting; R06 Thm2/Thm3 relation | **Its Lem4 repair (joint usc) is insufficient** — refuted by counterexample |
| **gpt** | Exhaustive record-by-record audit; status-vocabulary reform; layer hierarchy | 40+ findings incl. R01 W₁=[−1,1]; R01 open-loop-vs-feedback; R02.Prop3 false; R02.Cor6 unproved; R03 trichotomy non-exhaustive; R04 necessity false; R06.Thm2 self-defeating (A=dPF); R06 identity missing Cov; R07.Thm5 nonstationary policy-existence gap; R09.M5 forward-completeness violation | Slightly conservative on R06.Thm3 scope; severity calibration occasionally harsh |
| **qwen** | Consensus-compatible + programme-level augmentation | R02 observation typing/Prop3; computability; (REG)-assumes-certificate; Cor6 sampled bridge; R01 unbounded feedback; M1/M5/U-completeness; **unique:** greatest-fixed-point certificate construction; observation-morphism calculus; strategic-implementation docket; explicit erosion constants | Its Lem4 §3.9 claim is wrong — the record's Monotonicity paragraph contains the induction |
| **grok (1st)** | Strategic elevation bar; no line-level math | Defines what "general theory" would require; six-cluster minimum; forbidden-claims list | None (no line claims made) |
| **grok 2** | Chunked referee with own replacement theorems | CLSW 4.3.8-based invariance/erosion replacements; **unique:** finite-N two-patch moment closure (verified); M1 global root-locus completion; scope locks; reset-quantifier inconsistency | **Four verification errors:** accepted R02.Prop3 as correct (refuted); accepted R04's ẋ=u+1 witness (refuted); its own R01 Step-1 repair repeats the W₁=ℝ admissibility error; its "repaired Lem4" under joint usc is refuted |
| **this re-audit** | Independent pre-read of batch 2 | R02.Prop3 witness flawed (independent + explicit safe-policy construction); R03.Lem4 needs **lower** semicontinuity (counterexample refuting both usc repairs); R04 map-(3) witness broken; R05.Ex4 (H2) fails at the lower face; R09.M1 global completion; R09.M3 positive-witness typing; R01 Field-9 convexity overstatement; R06.Thm3 raw-moment-family extension | — |

**Consensus core (found independently by ≥3 audits, all verified):**
R02.Prop3 witness false · R03.Lem4 semicontinuity gap · R09.M1 statement/proof mismatch · R09.M5 converse witness broken · R02 "computable" overclaim · R06.Thm2 hypothesis defective · R05.Cor3 "iff" scoping · selector regularity systemic · R09 completeness overclaim.

---

## 2. Adjudications

### 2.1 R03.Lem4 — usc repairs are WRONG; lower semicontinuity is load-bearing

deepseek and grok 2 both propose repairing Lem4 with **joint upper semicontinuity** of `Succ(x,u,d)` in `(x,u)`. Both repairs are refuted by one counterexample: `Succ(x,0) = [0,1]` at `x = 0`, `{0}` for `x > 0` is jointly usc with closed values, yet `Pre({0}) = (0,1]` is **not closed**. The correct repair: **Hausdorff continuity** (both directions) — which the packet's corrected `08` already assumes.

### 2.2 R02.Prop3 — grok 2's acceptance is wrong

Under the record's conservative update with `O^{co}(z,θ) = z`, the two mode branches sit at z = 3 and z = 1 at `t₁` under any first command, so the observation **separates the modes at t₁**; a z-only policy exists that is safe forever. Repair: the quantized observation `1_{z≥4}` (non-separating on the safe-play range).

### 2.3 R04 map-(3) necessity witness

`ẋ = u+1` does **not** have an empty viability kernel (u=−1 cancels the drift). Repair: `ẋ = u+2` (drift dominates the control span).

### 2.4 R01.Thm1 Step 1 — gpt's `W₁ = [−1,1]` is correct

The record's `u ≡ −x` is inadmissible for `|x| > 1`. gpt: `W₁ = [−1,1]`; grok 2's repair repeats the error.

### 2.5 R01.Thm1 information pattern

gpt shows the witness is refuted under within-interval state feedback (`u = −4x` keeps both branches in `S₀` forever). grok 2 shows the theorem is saved by the sampled/open-loop pattern. Both correct: the theorem holds under the open-loop class; the meta-action class is now explicit.

### 2.6 R06.Thm3 scope — finite/atomic positive case

grok 2's counterexample verified: two quadratic patches close exactly in (m, Var). The theorem is scope-locked to non-atomic probability spaces; the finite/atomic positive case is the boundary.

### 2.7 R06.Thm2 — gpt's refutation is decisive

For smooth data the augmentation `A(x) = dP_xF(x)` **itself** separates all dPF-distinct pairs, so the hypothesis is essentially unsatisfiable. Demoted to conditional schema.

### 2.8 R05 — verified sound at the arithmetic level; retyping only

All algebra verified (Neumann series, M-matrix equivalence, 2×2 small-gain product). The retyping: one-sided (H3), convexified-inclusion conclusions, Cor3 linearized-sufficient scoping.

### 2.9 R07.Thm5 — three stacked repairs

deepseek's typing repair (common compact enclosure); Hausdorff-continuity successors; gpt's policy-tree compactness argument.

### 2.10 R09.M1 — the global claim is true and proved

All audits flag the local-only proof; the complete argument: imaginary-axis roots occur only at `ω = ±1, τ = π/2 + 2kπ`; every crossing is rightward. Hence unstable for every `τ > π/2`.

### 2.11 R09.M5 — gpt's forward-completeness catch decides the witness

`ẋ₁ = μ + x₁²` blows up in finite time. Repair: `(μ+x₁²)/(1+x₁²)`.

### 2.12 Consensus retypings

R02: "computable" → "causally determined"; observation typed; Cor6 demoted to conditional. R03: trichotomy → partial taxonomy. R04: necessity re-scoped. R06: Cov term restored. R07: universal reset preimage displayed. R08: ż typo fixed. R09: registered-inventory re-wording.

---

## 3. What survives as proved (post-repair)

**Sound after repair:** R01 (open-loop pattern, W₁=[−1,1]); R02.Thm1/Lem2/Prop4/Cor5 + Prop3 (quantized observation) + Cor6 (conditional); R03.Thm1 (partial taxonomy), Thm2, Thm3, Lem4 (Hausdorff continuity), Cor5; R04.Thm1 sufficiency + witness-necessity, Cor2; R05.Thm1/Thm2 (convexified), Cor3 (linearized-sufficient), Ex4; R06.Lem1, Thm3 (non-atomic scope lock), Cor4, Ex5; R07 (repaired); R08 (repaired); R09 Part U (registered inventory), M1–M6.

**Demoted:** R02.Cor6 (conditional); R06.Thm2 (conditional schema); R04's per-pair necessity; R09's completeness claim (registered inventory).

---

## 4. Audit scorecard

- **Most accurate line audit:** gpt
- **Best strategic frame:** grok 1
- **Best independent mathematics in service of repair:** grok 2 (marred by four verification errors)
- **Best programme augmentation:** qwen
- **deepseek:** correct on its three headline items; its Lem4 repair required correction
- **This re-audit's unique contributions:** the lsc counterexample adjudicating the two usc repairs; the independent discovery of the Prop3 and R04 witness flaws; the M1 global completion; the raw-moment-family extension

All corrected suggestions are implemented in the `batch 2` record files and the master review; the change log is `batch 2/REPAIR_CHANGELOG.md`.
