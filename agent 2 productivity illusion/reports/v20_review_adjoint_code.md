# Review of the attached "full‑adjoint solver" code (Candidate 2, refined)

**Task:** evaluate / verify / correct / complete the attached `top-down ecol.txt` adjoint code.
**Constraint honoured:** *do not implement this turn* — no mint, no push, no manuscript edit. This is a
verification + recommendation report. Baseline corrected S0: `ρ=0.05, A_max=1.2, b=0.5, b_G=0.8, e=0.55,
r=0.02, A_ext=0.02` (flow‑dominated, `b_Gρ=0.04 < b=0.5`).

## Bottom line

The code is a **template with placeholders that are also wrong**, contains a **left/right null‑vector bug**,
does **not** correctly implement the DDE adjoint, uses the **wrong equilibrium family and wrong parameters**,
and its promised "up to 100% (no‑delay), ~94% (`τ_g=30, τ_p=25`)" **is not achievable as described** —
the 94 % figure is a trivial majority‑class artefact. It must not be used to fold a "first integral" into
the manuscript.

## 1. Concrete defects

### 1.1 The placeholder matrices are wrong, not merely incomplete
Our corrected S0 (deficit region, from `model_sims/char_eq.py`) linearises to

```
A0 = [[+b0/b_G,  -e/b_G ],        Ag = [[ G'(A*),  0],        Ap = [[ 0,      0],
      [   0,      -r   ]]               [   0,     0]]              [ r K'(A*), 0]]
```
with `K'(A*) = (b0 + b_G G'(A*))/e`. The template instead has `A0[0,1] = -e` (missing the `1/b_G`),
`A0[0,0] = 0` (missing the `+b0/b_G` depletion term), and `Ap[1,0] = r(b/e)` (should be `r·K'(A*)`).
Even after substitution the template's matrices are therefore wrong and would produce a meaningless
functional.

### 1.2 Left vs right null‑vector bug
```
U, s, Vh = np.linalg.svd(J_total)
ell = Vh[-1, :]          # labelled 'left null vector (row)' — actually the RIGHT null vector
```
`Vh[-1]` is the last **right** singular vector, i.e. the **right** null vector. The **left** null vector
(the one needed for the adjoint) is `U[:, -1]`. They differ for our model (`A*=1.0`):
left null ≈ `[-0.029, 0.9996]` (≈ δP), right null ≈ `[-0.758, -0.652]`. So the seed is the wrong object.

### 1.3 The adjoint DDE is not correctly implemented
- The backward‑Euler scheme uses nearest‑index (`idx = int(...)`) for the delayed terms — no interpolation.
- The functional reduces to `I = I_A·A0 + I_P·P0` for constant histories, i.e. a **linear function of
  `(A0, P0)`**. A linear functional cannot capture the delay‑history dependence the method claims to add,
  and it buys no discriminating power beyond re‑weighting `(A0, P0)`.

### 1.4 Wrong equilibrium family and wrong parameters in the example
`params` uses `ρ=0.02` (not 0.05), `e=1.0` (not 0.55), and `P_star = b·A/e`. The latter is the **flow‑only
boundary limit**, not the model's equilibrium family `P = B(A)/e = (bA + b_G G(A))/e` (verified to differ in
the interior: `A=1.0` → `bA/e = 0.909` vs `B/e = 0.921`).

### 1.5 The accuracy promise is unverifiable
No code/files exist; the table ("97→100 %", "81→94 %") is not reproducible from the workspace.

## 2. What I verified empirically

### 2.1 The neutral direction is real (this is the correct premise)
With the **correct** matrices, `det(A0+Ag+Ap) = 0` (singular values include a 0) for `A*=0.6, 1.0, 1.1`.
So `D(0)=0` and the zero eigenvalue / neutral continuum are genuine — R2's result, correctly captured.

### 2.2 The true no‑delay separator is the nonlinear family curve, not a linear functional
Bisecting the no‑delay recover→collapse boundary gives, at every `A₀`, **`P₀` exactly equal to `B(A₀)/e`**:

| `A₀` | boundary `P₀` (bisect) | `P = B(A₀)/e` |
|---|---|---|
| 0.30 | 0.2891 | 0.2891 |
| 0.50 | 0.4758 | 0.4758 |
| 0.70 | 0.6576 | 0.6576 |
| 0.90 | 0.8345 | 0.8345 |
| 1.05 | 0.9641 | 0.9641 |
| 1.20 | 1.0909 | 1.0909 |

So the separator is the **neutral family curve** (a nonlinear parabola in `A`), not a single linear
functional of `(A₀, P₀)`. This is the same object R2 already identifies as the neutral continuum, and it
equals the `R_B = 1` locus of our macro‑ratio result.

### 2.3 Classifier accuracy on the 208‑cell basin

| `(τ_g, τ_p)` | #R / #C | family‑curve sep. | linear functional |
|---|---|---|---|
| (0, 0) | 83 / 125 | 99.0 % | 96.2 % |
| (10, 25) | 83 / 125 | 99.0 % | 96.2 % |
| (30, 25) | 11 / 197 | 64.4 % | 94.7 % |

Two conclusions:
- The **real** separator (the family curve) hits **99 % at no‑delay** but **degrades to 64 % at `τ_g=30`** —
  exactly the basin‑boundary‑crisis / no‑CSD distortion we established (the linear‑adjoint "100 % no‑delay"
  is not achievable; the nearest true result is 99 % and it is the *nonlinear* curve).
- The **94.7 %** at `(30,25)` **equals the majority‑class collapse rate (197/208)**. It is a trivial
  baseline, not a genuine separator — the basin at long lag is ~95 % collapse, so any
  "almost‑always‑collapse" classifier scores ~95 %. This inflates the AI's "refined" accuracy number.

## 3. Verdict on the claim

| The AI's claim | Verified |
|---|---|
| "will reproduce up to 100 % (no‑delay)" | **Not as described** — the true no‑delay separator is the nonlinear family curve (99 %), not a linear adjoint functional (96 %). |
| "~94 % for `(τ_g=30, τ_p=25)`" | **Trivial majority‑class artefact** (197/208 collapse = 94.7 %), not evidence of a basin separator. The genuine separator degrades to 64 % at that lag. |
| "placeholder matrices must be replaced" | True, but even + correct matrices, the linear functional does **not** deliver the promised accuracy; the code also has a null‑vector bug and wrong family/params. |

## 4. Recommendation

- **Do not** fold the "full‑adjoint first integral" into the manuscript as an analytic basin separator.
  The honest, verified statement is the one R2 already establishes: **the neutral family
  `P = B(A)/e` is the exact no‑delay basin separator; with delays the basin distorts (basin‑boundary
  crisis, no CSD), so no single scalar/linear functional separates it.** This is *worth saying* and
  already maps onto our macro‑ratio result (`R_B=1`), but it is **not** a new "100 %/94 % analytic
  advance."
- If a semi‑analytic separator is ever wanted, use the **nonlinear family curve** `P = B(A)/e` (with
  explicit caption of the 99 % → 64 % degradation), not a linear adjoint functional, and report it with
  a class‑imbalance‑aware metric (balanced accuracy / precision‑recall), not raw accuracy.

## Files
- This report: `reports/v20_review_adjoint_code.md`.
- Reuses `model_sims/char_eq.py` (correct matrices, `crossing_curves`) and `model_sims/corrected.py`.
- Verification figures/tables from this turn in `reports/v20_evaluation_of_ai_topdown.md`.
