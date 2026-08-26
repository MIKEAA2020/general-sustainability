# E2.B2(a) — Measurable Selection: REPAIRED

**Target.** The `B2.Theorem (a)` section of `batch 2/02_elevation/E2_SELECTORS_AND_CERTIFICATES.md`, and the manifest row `E2.B2(a)` (line 74).

**This file is a proposal. No repository file has been modified.**

**Disposition.** Steps 1, 2 and 4 are correct as written. Step 3 contains a **real gap**: it proves a statement about *closed* sets and then asserts the *open*-set statement that Kuratowski–Ryll-Nardzewski actually requires. The gap is closed by one line — the metric decomposition of an open set into closed sets — and **the conclusion is unchanged**: the measurable selector exists.

**Verification.** `reaudit/verify_e2b2a_a4_repair.py`, Part A, 11 assertions, exit 0.

---

## 1. The gap

Step 3 establishes:

> "for usc compact-valued correspondences into a metric space, the upper inverse `{x : A_W(x) ∩ F ≠ ∅}` of every **closed** `F` is closed … **Closed sets are Borel, so `A_W` is weakly measurable in the KRN sense.**"

The proof of the closed-set statement is correct: if `x_n → x` with `u_n ∈ A_W(x_n) ∩ F`, compactness of `U` gives `u_{n_k} → u ∈ F` (since `F` is closed), and the closed graph forces `u ∈ A_W(x)`.

But KRN weak measurability is the statement about **open** sets:

```
{x : A_W(x) ∩ O ≠ ∅}   is measurable      for every OPEN O ⊆ U.
```

"Closed sets are Borel" does not bridge these. The open-set upper inverse is not the upper inverse of a closed set, and upper semicontinuity alone does not make `{x : A(x) ⊆ F}` closed for closed `F`, which is what an indirect route would need. The inference as written is invalid.

---

## 2. `E2.B2(a)` Step 3 repaired

> **Step 3 (weak measurability) — repaired.** `A_W` is compact-valued with closed graph, hence upper semicontinuous; by the argument above, `{x : A_W(x) ∩ F ≠ ∅}` is closed for every closed `F ⊆ U`.
>
> Now let `O ⊆ U` be open. Since `U` is a metric space,
> ```
> O = ⋃_{n ≥ 1} F_n,      F_n := { y ∈ U : dist(y, U ∖ O) ≥ 1/n },
> ```
> and each `F_n` is **closed** (a super-level set of the 1-Lipschitz map `y ↦ dist(y, U ∖ O)`), with `F_n ⊆ F_{n+1}`. Hence
> ```
> { x : A_W(x) ∩ O ≠ ∅ }  =  ⋃_{n ≥ 1} { x : A_W(x) ∩ F_n ≠ ∅ },
> ```
> a **countable union of closed sets**, therefore Borel — indeed `F_σ`. So `A_W` is weakly measurable in the KRN sense.

*Proof of the decomposition.* (`⊇`) Each `F_n ⊆ O`, so `A_W(x) ∩ F_n ≠ ∅` implies `A_W(x) ∩ O ≠ ∅`. (`⊆`) If `y ∈ A_W(x) ∩ O`, then `y ∈ O` and `O` is open, so `dist(y, U ∖ O) > 0`; choose `n` with `1/n ≤ dist(y, U ∖ O)`. Then `y ∈ F_n`. ∎

**The metric hypothesis is available and is exactly what is needed.** The setting declares `X` compact metric and `U ⊆ ℝᵐ` compact, so both are metric; the decomposition uses only that. In a general regular space an open set need not be a countable union of closed sets, so the step is not available without the metric hypothesis — worth stating rather than leaving implicit.

**Verified.** For `O = (0.3, 0.7)`, `(0, 0.5)`, `(0.25, 1)` on a 100 001-point grid, `dist(y, U ∖ O) > 0` at every `y ∈ O` (minimum `1.000e−05`, the grid spacing), and the explicit union over `n ≤ 100 003` exhausts `O` exactly in each case — 39 999 / 39 999, 49 999 / 49 999, 74 999 / 74 999 points.

---

## 3. Nothing else changes

- **Step 1** (closed values) and **Step 2** (closed graph) are correct; both use Hausdorff continuity of `Succ` in the essential way, and the closing remark about why Hausdorff continuity is needed is right.
- **Step 4** (KRN) is correct once weak measurability is established: `X` and `S` are Polish, `U` is Polish, `A_W` has nonempty closed values on `S`.
- The theorem's **conclusion is unchanged**: there is a Borel-measurable `u* : S → U` with `u*(x) ∈ A_W(x)`.

**Suggested register text** (proposal only — not applied):

> `E2.B2(a) | Measurable selection | Closed graph + compact values ⟹ A_W usc with closed upper inverses of closed sets; weak measurability then follows from the metric decomposition O = ⋃ₙ{dist(·, U∖O) ≥ 1/n}; KRN gives a Borel selector | PROVEN (repaired) — Step 3's inference from closed-set to open-set upper inverses was unstated; one line closes it and the conclusion is unchanged. See batch 4/E2_B2A_REPAIRED.md`

**Downstream.** `E2.B2(a)` is cited by `A4.Thm1` (measurable selector for the shared control), `B10.Thm1` (repaired — selector at best responses), `E4.Thm3` (intergenerational selectors) and `B_TIER_BRIDGES` B1/B2. All of those consume only the *conclusion*, which is unaffected, so no downstream statement needs revision.

---

## 4. Verification

`reaudit/verify_e2b2a_a4_repair.py`, Part A — 11 assertions, exit 0.

| # | Claim | Result |
|---|---|---|
| A1 | `dist(y, U∖O) > 0` at every `y ∈ O`; explicit `⋃ₙ Fₙ` exhausts `O` | 3 intervals, exact coverage |
| A1 | each `Fₙ` is closed (super-level set of a 1-Lipschitz map), increasing in `n` | ✓ |
| A2 | the decomposition is an equality, giving an `F_σ` open-set upper inverse | ✓ |
| A3 | Step 3's inference is invalid as stated; the metric hypothesis is what closes it | ✓ |
| A4 | Steps 1 and 4 spot-checked (`A_W` closed for a concrete `Succ`, `W`) | `A_W = [−1.0000, 0.0000]` |

**One error in my own test, caught by the checks failing.** My first coverage check looped `n` only to 4000, so grid points within `1/4000` of the interval boundary were left uncovered and all three A1 checks failed. The mathematical content is that `dist(y, U∖O) > 0` *pointwise* — which is finite at each point but has infimum `0` over `O` — so I replaced the fixed loop with a per-point required-`n` computation plus an explicit exhaustion at that `n`.
