# B1.Thm1 — Sampled-Data Erosion: REPAIRED

**Target.** The `B1` section of `batch 2/04_open_problems/B_TIER_BRIDGES.md`, the manifest row `B1.Thm1` (line 95), the manifest row `R02.Cor6` (line 46), and the manifest's Part IV citation form for the "B1 erosion theorem" (line 174).

**This file is a proposal. No repository file has been modified.**

**Disposition.** The three hypotheses are sound and the core induction is correct. Two things are wrong: the headline conclusion is **ambiguous**, and on its natural (invariance) reading it is **irreparably false**; and the proof's final step claims a "verbatim" deeper iteration that the hypotheses do not supply. The repair replaces the single-depth statement with a **two-depth theorem** that (i) is proved, (ii) has a **tight** confinement condition, (iii) contains the record's actual content as a special case, and (iv) closes the `R02.Cor6` bridge with explicit depth bookkeeping — resolving the three-way disagreement between the manifest and three other documents.

**Verification.** `reaudit/verify_b1_repair.py`, 28 assertions, exit 0. Output: `reaudit/b1_output.txt`.

---

## 0. What the three hypotheses actually deliver

Restating the record's hypotheses with the target depth named:

1. **(Envelope)** `x(t) ∈ B̄(x_k, ρ)` for `t ∈ [t_k, t_{k+1})`, with `ρ ≤ V_max T_s`;
2. **(Confinement)** `V_max · T_s ≤ r/2`;
3. **(Successor certificate)** `x_k ∈ K_{−r/2} ⟹ x_{k+1} ∈ K_{−r/2}`.

The induction gives exactly two conclusions, and no more:

- **(A)** `x_0 ∈ K_{−r/2} ⟹ x_k ∈ K_{−r/2}` for every sample `k`;
- **(B)** `x(t) ∈ K` for every `t`.

For (B): `dist(x(t), K^c) ≥ dist(x_k, K^c) − ‖x(t) − x_k‖ ≥ r/2 − r/2 = 0`.

Note what is *not* among them: invariance of `K_{−r}`, or even of `K_{−r/2}` in continuous time. Between samples the trajectory is only known to stay in `K`.

**The headline is ambiguous.** "The `r`-eroded set `K_{−r}` is safe" admits two readings:

| reading | statement | verdict |
|---|---|---|
| **safety** | `x_0 ∈ K_{−r} ⟹ x(t) ∈ K` for all `t` | **true** — immediate from (A)+(B), since `K_{−r} ⊆ K_{−r/2}` |
| **invariance** | `x_0 ∈ K_{−r} ⟹ x(t) ∈ K_{−r}` for all `t` | **false** — §1 |

The record's own gloss ("In particular, if `K` is the safe set, every inter-sample trajectory remains in `K`") supports the safety reading, so the *theorem* is salvageable. But the sentence "the `r`-eroded set `K_{−r}` is safe" reads naturally as invariance, and the proof's closing step claims more than either.

---

## 1. The invariance reading is irreparably false

**Counterexample (verified).** `K = [0,1] ⊂ ℝ`, so `K_{−d} = [d, 1−d]`. Take `r = 0.4`, `T_s = 1`, `V_max = 0.2`, and the sampled dynamics

```
x_{k+1} = min(x_k + 0.2, 0.8),        x linear between samples.
```

- **H2:** `V_max T_s = 0.2 = r/2` ✓ (with equality).
- **H1:** `|x(t) − x_k| ≤ 0.2`, so `ρ = 0.2` works ✓.
- **H3:** `x ∈ [0.2, 0.8] ⟹ min(x + 0.2, 0.8) ∈ [0.4, 0.8] ⊆ [0.2, 0.8]` ✓ (verified on 200 001 points).

Start at `x_0 = 0.4 ∈ K_{−r} = [0.4, 0.6]`. The sample states are

```
0.4, 0.6, 0.8, 0.8, 0.8, …
```

which **leave `K_{−r}` at `k = 2`**, while remaining in `K_{−r/2} = [0.2, 0.8]` at every sample and in `K` continuously. All three hypotheses hold; the invariance conclusion fails.

**Why it is irreparable, not a gap.** Invariance of `K_{−R}` in continuous time is the two-depth theorem at `(R, r) = (R, R)`, which requires `V_max T_s ≤ R − R = 0`. But H1 permits the inter-sample trajectory to reach the *full* drift `V_max T_s` away from `x_k` in any direction, including outward; from a point at depth exactly `R` that reaches depth `R − V_max T_s < R`. So **no nonzero sample period admits continuous-time invariance of an eroded set under these hypotheses.** A moving trajectory cannot maintain a fixed positive depth. This is structural, and no strengthening of the proof repairs it — only a change of claim does.

---

## 2. The "verbatim" iteration is unsupported

The proof closes with: *"replacing `K` by `K_{−r}` throughout (the erosion conversion of R03.Cor5 with `Δ = 0`, `L_G r ≤ α`) yields the `r`-eroded statement verbatim."*

Set `K̃ = K_{−r}`. Then `K̃_{−d} = K_{−(r+d)}`, so the record's own depth `r/2` *inside* `K̃` is depth `r + r/2 = 3r/2` relative to `K`. Running the argument on `K̃` therefore requires the successor certificate

```
x_k ∈ K_{−3r/2}  ⟹  x_{k+1} ∈ K_{−3r/2},
```

whereas hypothesis 3 supplies depth `r/2`. Shortfall `r`, verified for `r = 0.4, 0.2, 0.6` (shortfalls `0.400, 0.200, 0.600`). The iteration is not available, and the invocation of `R03.Cor5` does not supply it — `R03.Cor5` is an erosion *conversion*, not a successor certificate at a deeper level.

---

## 3. `B1.Thm1` repaired — the two-depth theorem

The right statement separates the depth at which the certificate holds from the depth at which safety is claimed. That separation is what the inter-sample drift costs, and naming it makes the trade-off explicit and the theorem reusable.

> ### B1.Thm1 (repaired) — two-depth sampled-data erosion
>
> Let `K ⊆ ℝⁿ` be closed, and let `R > r ≥ 0`. Consider a sampled closed loop with period `T_s` and samples `x_k = x(t_k)`, `t_k = kT_s`. Assume:
>
> 1. **(Envelope)** `x(t) ∈ B̄(x_k, ρ)` for `t ∈ [t_k, t_{k+1})`, with `ρ ≤ V_max T_s`, where `V_max` bounds the closed-loop speed on the relevant compact set;
> 2. **(Confinement)** `V_max · T_s ≤ R − r`;
> 3. **(Successor certificate at depth `R`)** `x_k ∈ K_{−R} ⟹ x_{k+1} ∈ K_{−R}`.
>
> Then for every trajectory with `x_0 ∈ K_{−R}`:
>
> **(a)** `x_k ∈ K_{−R}` for every sample `k` — sample-time invariance at depth `R`;
>
> **(b)** `x(t) ∈ K_{−r}` for every `t` — continuous-time safety at depth `r`.

**Proof.** (a) Induction on `k` using hypothesis 3, with base `x_0 ∈ K_{−R}`.

(b) Fix `t ∈ [t_k, t_{k+1})`. By the triangle inequality for the distance to the closed set `K^c`,

```
dist(x(t), K^c)  ≥  dist(x_k, K^c) − ‖x(t) − x_k‖  ≥  R − V_max T_s  ≥  R − (R − r)  =  r,
```

using (a) at `t_k`, hypothesis 1, and hypothesis 2. Hence `x(t) ∈ K_{−r}`. At the sample times themselves, `x_k ∈ K_{−R} ⊆ K_{−r}` since `R > r`. ∎

**The record's theorem is the case `(R, r) = (r_rec/2, 0)`.** Its confinement `V_max T_s ≤ r_rec/2` is exactly `R − r` at that pair; its conclusions "`K_{−r/2}` forward-invariant at the sample times" and "every inter-sample trajectory remains in `K`" are exactly (a) and (b) at `r = 0`, where `K_{−0} = K`. So nothing the record *proved* is lost — it is recovered verbatim as a special case, and the ambiguous headline disappears.

---

## 4. Sharpness

> **Proposition 4.1.** The confinement bound `V_max T_s ≤ R − r` is tight.

*Proof.* Take `x_k` on the inner boundary of `K_{−R}`, so `dist(x_k, K^c) = R`. Hypothesis 1 permits the inter-sample trajectory to reach any point of `B̄(x_k, V_max T_s)`, including one at depth `R − V_max T_s`. That point lies in `K_{−r}` iff `R − V_max T_s ≥ r`. ∎

**Verified.** With `R = 0.4`, `r = 0.2` the threshold is attained exactly at `V_max T_s = 0.2`: at `0.1999` the deepest point is `0.2001 ≥ r` (holds); at `0.2000001` it is `0.1999999 < r` (fails); at `0.3` it is `0.1` (fails). A 2-D check on the unit disc (`K_{−R}` = disc of radius `1−R`) confirms this is not a 1-D artefact: an outward excursion of `V_max T_s` from radius `1−R` reaches radius `1−R+V_max T_s`, inside `K_{−r}` iff `V_max T_s ≤ R − r`.

**Practical reading.** The theorem gives an explicit **sample-period budget**:

```
T_s  ≤  (R − r) / V_max.
```

The record explicitly declined to address sample-period selection ("an engineering question outside the certificate discipline"). The repaired form makes it a one-line corollary, which is what a governance-design paper needs: the certificate depth you can afford to lose per sample is exactly the drift budget.

---

## 5. The `R02.Cor6` bridge — resolution of the three-way disagreement

**The disagreement.** Four documents currently say incompatible things:

| document | statement |
|---|---|
| `PROOF_MANIFEST.md` line 46 | `R02.Cor6 … PROVEN_CONDITIONAL (sampled-data erosion bridge open)` |
| `B_TIER_BRIDGES.md` | `B1 … PROVED (closes R02.Cor6's bridge)` |
| `WAVE_E_UPDATE.md` | "R02.Cor6's bridge is **now a theorem, not a conditional**" |
| `PUBLICATION_STRATEGY.md` Paper 5 | "sampled-data erosion theorem (B1) **closes** R02.Cor6's bridge" |

**What the bridge is.** `R02.Cor6` is a *continuous-time* erosion statement: under packet Lemma 2's hypotheses and `L_G r + Δ_ε ≤ α`, `0 < r < ρ`, `K_{−r} ≠ ∅`, the tube clause may be verified on `K_{−r}`. `R02` itself is a *sampled* closed-loop theorem. Combining them requires controlling the trajectory **between** samples — which Lemma 2 does not do when the certificate is available only at sample times, as it is for a held command.

**B1 supplies exactly that.** Lemma 2's strong invariance of `K_{−R}` implies the sample-time implication `x_k ∈ K_{−R} ⟹ x_{k+1} ∈ K_{−R}`, i.e. hypothesis 3 at depth `R`. B1's confinement hypothesis then converts the discrete certificate into continuous-time safety at depth `r`.

> ### Corollary 5.1 (the closed bridge)
>
> Suppose packet Lemma 2's hypotheses hold for `K` with two-sided tubular radius `ρ`, envelope modulus `L_G`, boundary margin `α`, and implementation/model error budget `Δ`; and the sampled closed loop satisfies hypothesis 1 with `ρ ≤ V_max T_s`. If
> ```
> L_G R + Δ ≤ α,      0 < R < ρ,      K_{−R} ≠ ∅,      V_max T_s ≤ R − r,
> ```
> then every sampled closed-loop trajectory with `x_0 ∈ K_{−R}` satisfies `x_k ∈ K_{−R}` at sample times and `x(t) ∈ K_{−r}` for all `t`.

*Proof.* Lemma 2 gives strong invariance of `K_{−R}`, hence hypothesis 3 at depth `R`. Apply B1.Thm1 repaired. ∎

**Resolution.** Both sides were partly right:

- The **manifest is too pessimistic.** The mathematical bridge *does* close; "open" is no longer accurate once the depth bookkeeping `R − r ≥ V_max T_s` is stated.
- **The three asserting documents are too optimistic.** They do not record that the conclusion is at depth `r < R`, not at the certified depth `R`, and B1's own headline claimed invariance of `K_{−r}`, which §1 refutes.

**Suggested register entries** (proposals only — not applied):

- `R02.Cor6` → `PROVEN_CONDITIONAL`, condition **discharged at the two-depth form**: "the sampled-data erosion bridge is closed by B1.Thm1 (repaired) with explicit depth bookkeeping `R − r ≥ V_max T_s`; the residual condition is model-level verification of `L_G R + Δ ≤ α` and `V_max T_s ≤ R − r`."
- `B1.Thm1` → `PROVEN (repaired)`, statement replaced by the two-depth form.
- Part IV citation form (line 174) → *"The two-depth erosion theorem converts a sample-time certificate at depth `R` into continuous-time safety at depth `r`, at the cost `V_max T_s ≤ R − r`; this closes the sampled-data bridge."* The current wording, "the three-hypothesis erosion theorem closes the sampled-data bridge", should not be used unqualified, because the theorem it names claims an invariance that is false.

**What remains genuinely open** is untouched by this repair and is already carried elsewhere in the manifest: no specific model has been verified against these hypotheses (line 153, `NOT CONFIRMED`). That is an empirical gate, not a mathematical one.

**Where B1 adds value over Lemma 2 alone.** If continuous strong invariance of `K_{−R}` is already available from Lemma 2, B1 is redundant. Its value is precisely the sampled-governance setting of Paper 5, where the command is *held* between samples and the certificate is only available **discretely** — from a numerical check at sample points, not from a continuous invariance proof. That is the case hypothesis 3 is written for.

---

## 6. Verification

`reaudit/verify_b1_repair.py` — 28 assertions, exit 0. Reads and writes no repository file.

| # | Claim | Result |
|---|---|---|
| N1 | counterexample: all three hypotheses hold, `x_0 ∈ K_{−r}`, trajectory leaves `K_{−r}` | states `0.4, 0.6, 0.8, …`, first failure `k=2`; stays in `K_{−r/2}` and in `K` |
| N2 | repaired two-depth theorem holds on 60 random systems | sample-time depth `R` maintained **and** continuous safety at depth `r` |
| N3 | confinement `V_max T_s ≤ R − r` is tight, in 1-D and on a 2-D disc | threshold attained with equality; fails at `+1e-7` |
| N4 | the "verbatim" iteration needs depth `3r/2` | shortfalls `0.400, 0.200, 0.600` |
| N5 | the record's proved content is the case `(R, r) = (r_rec/2, 0)`; its claimed content needs `V_max T_s ≤ 0` | both |
| N6 | bridge bookkeeping: Lemma 2 at depth `R` supplies H3; `L_G R + Δ ≤ α` checked on three parameter sets | all |

**Two errors in my own tests, caught by the checks failing.** First, my initial tightness test used a 1-D interval with monotone motion, where `K_{−R}` is convex so the inter-sample excursion cannot leave it — the test passed for admissible *and* inadmissible drift. Fixed by modelling the outward excursion H1 actually permits, plus a 2-D disc check. Second, I first derived the iteration depth as `2r`; the correct figure is `r + r/2 = 3r/2`, matching the record's own arithmetic.
