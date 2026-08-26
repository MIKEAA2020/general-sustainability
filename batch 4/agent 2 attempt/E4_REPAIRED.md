# E4 — Intergenerational Production: REPAIRED

**Replaces:** `batch 2/02_elevation/E4_INTERGENERATIONAL_PRODUCTION.md` (Lem1 part (ii), Thm2's budget analysis), and the manifest rows at `PROOF_MANIFEST.md` lines 81–82.

**Disposition.** Three defects, of different kinds:

| # | Defect | Kind | Disposition |
|---|---|---|---|
| D1 | `E4.Lem1`'s margin definition admits vacuous pairs, so its refutation claim is false as written | definition degenerate | repaired by adding non-vacuity; the refutation then stands verbatim |
| D2 | `E4.Thm2`'s budget-solvability formula is wrong by a factor `ℓ^G`, and its infinite-horizon branch names the wrong fixed point | arithmetic | replaced with the exact, tight formula |
| D3 | **New.** The budget recursion as stated admits `r ≡ 0`, so the entire budget theory is vacuous without a minimal-erosion lower bound | structural | repaired by adding the lower bound `ρ_g > 0`, which yields a strictly stronger theorem |

**The substantive conclusion changes sign.** The record concludes that a *contracting* reset (`ℓ < 1`) is sustainable across infinitely many generations given a large enough initial margin, `r_0 ≥ b/(1−ℓ)`. **That is false.** The correct criterion is that sustainability at an unbounded horizon requires `ℓ > 1`, or `ℓ = 1` with `b = 0`. A contracting reset is unsustainable at **any** initial margin — and for `ℓ < 1` the required margin grows like `ℓ^{−G}`, **exponentially in the horizon**, even when the per-jump deficit `b` vanishes. The honest negative finding is therefore much stronger than the one recorded, and points the opposite way.

**Verification.** `reaudit/verify_e4_repair.py`, 58 assertions, exit 0. Output: `reaudit/e4_output.txt`.

---

## 0. What was false

### D1 — the margin definition is degenerate

**Original.** `R_g` has depth co-Lipschitz margin `(ℓ, b)`, `ℓ > 0`, `b ≥ 0`, if for all `r ∈ [0, r̄_g]`,

```
R_g(K_{g,−r}) ⊆ K_{g+1,−(ℓr−b)},      right side read as K_{g+1} when ℓr − b ≤ 0.
```

Since `r ≤ r̄_g` (the inradius) and depth never exceeds the inradius, **any pair with `b ≥ ℓ·r̄_g` satisfies the condition vacuously at every `r`**. On a bounded safe set such a pair always exists — e.g. `(ℓ, b) = (1, r̄_g)`. So the original's claim "**no uniform `(ℓ, b)` with `b < ∞` exists**" is false, and its witness does not establish it.

Verified: for `K = [0,1]` (`r̄ = 1/2`), the pairs `(1, 0.5)`, `(0.5, 0.25)`, `(2, 1)`, `(1, 0.6)` are all uniform margins for the entire witness family, because `ℓ·r̄ − b ≤ 0` makes the condition vacuous everywhere.

### D2 — the budget arithmetic

**Original.** "The recursion `r_{g+1} = ℓ r_g − b` admits nonnegative solutions on `{0..G}` iff `r_0 ≥ b(ℓ^G − 1)/(ℓ − 1)` … For `G = ∞`: `ℓ < 1` with `r_0 ≥ b/(1−ℓ)`, or `b = 0` with `ℓ ≤ 1`."

Solving the recursion, `r_g = ℓ^g(r_0 − r*) + r*` with fixed point `r* = b/(ℓ−1)`, gives the correct threshold

```
r_0  ≥  (b/(ℓ−1))·(1 − ℓ^{−G})          (ℓ ≠ 1),          r_0 ≥ b·G   (ℓ = 1),
```

which is **tight** (verified: `r_0` just below fails in every tested case). The record's expression equals `ℓ^G ×` the correct one — too weak for `ℓ < 1`, too strong for `ℓ > 1`:

| `ℓ` | `b` | `G` | correct | record | record/correct |
|---|---|---|---|---|---|
| 0.5 | 1 | 2 | 6.00000 | 1.50000 | 0.25 |
| 0.9 | 0.1 | 10 | 1.86797 | 0.65132 | 0.349 |
| 2.0 | 1 | 8 | 0.99609 | 255.00000 | 256 |

And `b/(1−ℓ)` is the fixed point of `r ↦ ℓr + b`, not of `r ↦ ℓr − b`; the latter's fixed point is `b/(ℓ−1) < 0` when `ℓ < 1`, so the sequence **always** eventually goes negative. Verified over 5001 generations for `ℓ ∈ {0.5, 0.9, 0.99, 0.999}`.

### D3 — the budget recursion is vacuous as stated (new)

Setting `r_0 = 0` gives `r_g ≤ 0` for all `g ≥ 1` whenever `b > 0`, and the record reads a nonpositive depth as "no erosion", i.e. `K_{g,−0} = K_g`. Verified for `ℓ ∈ {0.5, 2.0, 0.9, 1.5}`: e.g. `ℓ = 0.5, b = 1, r_0 = 0 → [0, −1, −1.5, −1.75, −1.875, …]`.

So `r ≡ 0` is always an admissible budget, and it delivers the **strongest** conclusion — invariance of the *uneroded* path `∏ K_g` — with no initial margin at all. The budget theory therefore says nothing unless within-generation invariance *requires* positive erosion. That requirement is the missing hypothesis, and adding it is what makes the module's quantitative content real (§3).

---

## 1. `E4.Lem1` repaired — non-vacuous jump-margin transfer

> ### E4.Lem1 (repaired)
>
> Let `r̄_g` be the inradius of `K_g`. Say `R_g` has a **non-vacuous depth co-Lipschitz margin `(ℓ, b)`** if `ℓ > 0`, `0 ≤ b < ℓ·r̄_g`, and for all `r ∈ (b/ℓ, r̄_g]`,
> ```
> R_g(K_{g,−r}) ⊆ K_{g+1,−(ℓr−b)}.
> ```
> (For `r ≤ b/ℓ` the right side is all of `K_{g+1}` and the inclusion is automatic; the restriction to `r > b/ℓ` is where the condition has content, and `b < ℓ·r̄_g` is exactly what makes that range nonempty.)
>
> Then: **(i)** the inclusion transfers erosion depths across generations with deficit `b` consumed per generation; **(ii)** the margin is **declared data** — not derivable from Lipschitz continuity of `R_g` plus boundary margins of `K_g, K_{g+1}`.

**Proof of (ii).** Take `K_g = K_{g+1} = [0,1]`, so `r̄ = 1/2`, and define

```
φ_g(x) = x/g                                  for x ∈ [0, 1/2],
φ_g(x) = 1/(2g) + (x − 1/2)(2 − 1/g)          for x ∈ (1/2, 1].
```

Each `φ_g` is continuous (both branches give `1/(2g)` at `x = 1/2`), increasing, with `φ_g(0) = 0` and `φ_g(1) = 1/(2g) + (1/2)(2 − 1/g) = 1`, so it is a bijection of `[0,1]`. Its slopes are `1/g` and `2 − 1/g`, both `≤ 2`, so the whole family has **uniform Lipschitz constant 2**. Depth in `[0,1]` is `min(x, 1−x)`.

At `x = 1/2`: `depth_in = 1/2`, and `φ_g(1/2) = 1/(2g)`, so `depth_out = min(1/(2g), 1 − 1/(2g)) = 1/(2g) → 0`. The margin condition at `r = 1/2` requires

```
1/(2g)  ≥  ℓ·(1/2) − b  =  ℓ/2 − b.
```

The right side is positive **exactly when `b < ℓ/2 = ℓ·r̄`** — the non-vacuity condition — and then the inequality fails for every `g > 1/(ℓ − 2b)`. Hence no non-vacuous uniform margin exists, although every `R_g` is piecewise linear with uniformly bounded Lipschitz constant and every boundary-margin datum is bounded. ∎

**Verified.** First failing generation matches the analytic prediction `g > 1/(ℓ − 2b)` exactly:

| `(ℓ, b)` | `ℓr̄ − b` | predicted | first failure |
|---|---|---|---|
| (1, 0.4) | 0.10 | `g > 5.00` | `g = 6` |
| (0.5, 0.2) | 0.05 | `g > 10.00` | `g = 11` |
| (0.2, 0.05) | 0.05 | `g > 10.00` | `g = 11` |
| (1, 0.49) | 0.01 | `g > 50.00` | `g = 51` |
| (3, 1.4) | 0.10 | `g > 5.00` | `g = 6` |
| (2, 0.9) | 0.10 | `g > 5.00` | `g = 6` |

**Honesty consequence (unchanged in force, now well founded).** Every use of jump-margin transfer must exhibit a non-vacuous `(ℓ, b)` for the declared reset family. Note that non-vacuity is a real constraint, not a formality: `b < ℓ·r̄_g` says the per-jump deficit must be strictly smaller than the depth the reset can generate from a maximally deep state.

---

## 2. `E4.Thm2` repaired — the forward budget, corrected

The inductive proof of the original (base, boundary step, concatenation) is correct and is retained unchanged. Only the analysis of when the hypothesis is satisfiable is replaced.

> ### Budget solvability (forward form) — corrected
>
> The recursion `r_{g+1} = ℓ r_g − b` has `r_g = ℓ^g(r_0 − r*) + r*` with `r* = b/(ℓ−1)` (`ℓ ≠ 1`), and `r_g = r_0 − gb` (`ℓ = 1`). It admits nonnegative values on `{0, …, G}` **iff**
> ```
> r_0  ≥  (b/(ℓ−1))·(1 − ℓ^{−G})      (ℓ ≠ 1),          r_0  ≥  b·G      (ℓ = 1).
> ```
> The bound is tight. At an unbounded horizon it admits nonnegative values for all `g` **iff** `b = 0` (any `ℓ ≥ 0`), **or** `ℓ > 1` with `r_0 ≥ b/(ℓ−1)`.

*Proof.* `r_g ≥ 0 ⟺ ℓ^g(r_0 − r*) ≥ −r* ⟺ r_0 ≥ r*(1 − ℓ^{−g})`. The right side is monotone in `g` (increasing when `r* > 0`, i.e. `ℓ > 1`; and `r*(1 − ℓ^{−g}) = |r*|(ℓ^{−g} − 1)` increasing when `ℓ < 1`), so the binding constraint is `g = G`. For `ℓ = 1`, `r_G = r_0 − Gb ≥ 0` gives `r_0 ≥ bG`. For the infinite horizon: if `b > 0` and `ℓ ≤ 1` then `r_{g+1} ≤ r_g − b`, so `r_g → −∞`; if `ℓ > 1` then `r_g ≥ r* > 0` exactly when `r_0 ≥ r* = b/(ℓ−1)`; if `b = 0` then `r_g = ℓ^g r_0 ≥ 0`. ∎

**Why the record got the sign wrong.** For `ℓ < 1` the record's expression `b(ℓ^G − 1)/(ℓ − 1)` increases to the **finite** limit `b/(1−ℓ)`, which is exactly what suggested that a finite initial margin suffices at an unbounded horizon. The correct expression `(b/(ℓ−1))(1 − ℓ^{−G}) = (b/(1−ℓ))(ℓ^{−G} − 1)` grows like `ℓ^{−G}`. The two differ by the factor `ℓ^G`, which tends to `0` for `ℓ < 1` and to `∞` for `ℓ > 1` — so the error is small where it is harmless and unbounded where it matters.

---

## 3. The substantive repair — required depths propagate backwards

D3 shows the forward form cannot carry the module's content. The meaningful question is not "is the budget nonnegative" but "**what initial margin is needed to keep every generation safely eroded**".

> ### E4.Thm2 (repaired) — Eroded generation transfer, non-vacuous form
>
> Assume for `g = 0, …, G`:
>
> 1. **Within-generation erosion with a genuine lower bound.** There are `0 < ρ_g ≤ R_g` such that `K_{g,−r}` is strongly invariant within generation `g` for every `r ∈ [ρ_g, R_g]`, and `K_g` itself is **not** strongly invariant. (This is the hypothesis D3 shows was missing; `ρ_g > 0` is what makes the budget question non-trivial.)
> 2. **Jump-margin transfer.** A non-vacuous margin `(ℓ, b)` for every `R_g` (E4.Lem1 repaired).
> 3. **Non-Zeno calendar**, `G` finite.
>
> If there is a budget sequence with `ρ_g ≤ r_g ≤ R_g` and `r_{g+1} ≤ ℓ r_g − b` for `g < G`, then the eroded path `∏_g K_{g,−r_g}` is **strongly invariant**.
>
> **Minimal required initial depth.** Writing `u_G := ρ_G` and `u_g := max(ρ_g, (u_{g+1} + b)/ℓ)`, a budget exists **iff** `r_0 ≥ u_0`, and `u_0` is then minimal. For constant `ρ_g ≡ ρ`,
> ```
> u_0  =  max( ρ ,  ρ·ℓ^{−G} + b·(ℓ^{−G} − 1)/(1 − ℓ) )      (ℓ ≠ 1),        u_0 = ρ + G·b   (ℓ = 1).
> ```

*Proof of the invariance claim.* Identical to the original induction: within generation `g`, hypothesis 1 at depth `r_g ∈ [ρ_g, R_g]`; at the boundary, E4.Lem1 gives depth `≥ ℓ r_g − b ≥ r_{g+1}`; concatenation over finitely many boundaries. ∎

*Proof of minimality.* Necessity: `r_{g+1} ≥ ρ_{g+1}` and `r_{g+1} ≤ ℓ r_g − b` force `r_g ≥ (ρ_{g+1} + b)/ℓ`, and together with `r_g ≥ ρ_g`, `r_g ≥ max(ρ_g, (r_{g+1} + b)/ℓ)`. Unrolling from `r_G ≥ ρ_G` gives `r_0 ≥ u_0`. Sufficiency: `r_g := u_g` satisfies `u_g ≥ ρ_g` by construction and `u_{g+1} ≤ (u_g + b)/ℓ`, i.e. `ℓ u_g − b ≥ u_{g+1}`, so the transfer constraint holds. The closed form follows by induction when the `max` never binds, i.e. when `(u_{g+1} + b)/ℓ ≥ ρ`; otherwise `u_g = ρ` throughout. ∎

### 3.1 The corrected sustainability criterion

> **Sustainable at an unbounded horizon** (i.e. `sup_G u_0(G) < ∞`) **iff `ℓ > 1`, or `ℓ = 1` with `b = 0`.**
>
> - `ℓ > 1`: `u_0 → max(ρ, b/(ℓ−1))`. Bounded.
> - `ℓ = 1`, `b = 0`: `u_0 = ρ`. Bounded.
> - `ℓ = 1`, `b > 0`: `u_0 = ρ + Gb → ∞`.
> - `ℓ < 1`: `u_0 ≥ ρ·ℓ^{−G} → ∞` — **and this holds even when `b = 0`**, because a contracting reset maps depth `r` to depth `ℓr`, so maintaining `ρ` after `G` jumps costs `ρℓ^{−G}` regardless of any additive deficit.

Verified: `ℓ ∈ {2.0, 1.5, 3.0}` converge to `max(ρ, b/(ℓ−1))` over 2000 generations; `b = 0` with `ℓ ≥ 1` gives `u_0 = ρ` exactly; `b = 0` with `ℓ < 1` gives `u_0 = ρℓ^{−G}` exactly; every `ℓ < 1` case diverges.

### 3.2 The exponential law

For `ℓ < 1`,

```
u_0(G)  ~  ( ρ + b/(1−ℓ) ) · ℓ^{−G}   =   ( ρ + b/(1−ℓ) ) · e^{G·|ln ℓ|},
```

verified: `u_0/ℓ^{−G} → 1.200000` against `ρ + b/(1−ℓ) = 0.2 + 1.0 = 1.2` for `ℓ = 0.9, b = 0.1, ρ = 0.2`. Concretely, doubling the horizon multiplies the required initial margin by `ℓ^{−G} + 1`:

| `G` | 5 | 10 | 20 | 40 | 80 | 160 |
|---|---|---|---|---|---|---|
| `u_0` | 1.032 | 2.442 | 8.870 | 80.19 | 5491.6 | 2.51 × 10⁷ |
| growth | — | 2.37× | 3.63× | 9.04× | 68.5× | 4578× |

**This is the module's real quantitative statement**, and it is far sharper than the record's: finitely many generations are always reachable, but at a cost exponential in the horizon; infinitely many are reachable only if the reset is depth-expanding or exactly deficit-free.

---

## 4. The corrected negative finding

The record's "Recorded negative finding (honesty)" said only that E4 does not derive `(ℓ, b)` from cheaper data, and that "when the budget recursion is unsolvable, the theorem makes no invariance claim". The repaired version yields a genuine **impossibility**:

> **A generation transition that contracts depth (`ℓ < 1`) cannot sustain positive erosion across unboundedly many generations at any initial margin.** The required initial margin grows exponentially in the number of generations, `u_0(G) ~ (ρ + b/(1−ℓ))ℓ^{−G}`, and this is true even when the per-jump deficit vanishes. Sustainability across an unbounded horizon requires either a **depth-expanding** transition (`ℓ > 1`) with initial margin at least `max(ρ, b/(ℓ−1))`, or an exactly deficit-free, non-contracting one (`ℓ = 1`, `b = 0`).

Read against the module's purpose — "the quantitative reading of *sustainability across generations*" — this says: **you cannot buy intergenerational sustainability with a large enough initial buffer if each transition strictly erodes the margin.** The buffer is consumed exponentially. That is a stronger claim than the record's, in the opposite direction, and it is the one the mathematics supports.

Certifying the *failure* still requires the R03 adversarial-exit route, as the record says; E4 supplies the budget side, not the exit certificate.

---

## 5. Consumers

- **`E4.Thm3`** (production assembly) is unaffected in structure — it consumes Thm2's invariance conclusion plus E2's selectors — but its statement must now carry the `ρ_g > 0` hypothesis, since without it the assembly is vacuous (D3).
- **`B8`** (event-surface calculus) composes `A3.Thm3` with E4's jump-margin transfer. Both parents are now repaired (`A3.Thm1` with the common-modulus hypothesis; `E4.Lem1` with non-vacuity), so B8's two declaration sets are now well formed. B8 remains `CONDITIONAL` because neither parent's conditions have been discharged on an instance.
- **Paper 2's generation chapter** should cite the corrected criterion and the exponential law, not the record's `b/(1−ℓ)` geometric budget.
- **`PROOF_REAUDIT.md`** findings 3 and 4 are discharged; finding #8's downstream note about B8 is now actionable.

---

## 6. Status and obligations

- **E4.Lem1: PROVEN (repaired).** Non-vacuous margin definition; the declared-data refutation stands, with the first failing generation predicted analytically and verified.
- **E4.Thm2: PROVEN (repaired).** Invariance induction unchanged; budget theory corrected and made non-vacuous; exact tight thresholds in both the forward and backwards forms.
- **Corrected register text.** The manifest rows should read: `E4.Lem1 | PROVEN (repaired — non-vacuity hypothesis b < ℓ·r̄_g added; original definition admitted vacuous pairs)` and `E4.Thm2 | PROVEN (repaired — budget threshold (b/(ℓ−1))(1−ℓ^{−G}); sustainability requires ℓ>1 or (ℓ=1, b=0); original formula was ℓ^G× too small for ℓ<1)`.
- **Obligation created.** Any downstream citation of "the geometric budget `r_0 ≥ b/(1−ℓ)`" must be withdrawn. A grep for `b/(1−ℓ)` and "geometric budget" is recommended before Paper 2 is finalised.

---

## 7. Verification

`reaudit/verify_e4_repair.py` — 58 assertions, exit 0:

| # | Claim | Result |
|---|---|---|
| N1 | forward threshold `(b/(ℓ−1))(1−ℓ^{−G})` is an **iff** and is tight; record's formula `= ℓ^G ×` correct | 9/9 cases; tightness checked at `0.999999×` |
| N2 | `ℓ = 1` case `r_0 ≥ bG`, tight | 3/3 |
| N3 | infinite horizon: record's `b/(1−ℓ)` fails for `ℓ<1` over 5001 generations; `ℓ>1` with `b/(ℓ−1)` survives; `b=0` survives | all |
| N4 | exponential law; record's formula tends to the finite limit `b/(1−ℓ)` | `r_0(2G)/r_0(G) = ℓ^{−G}+1` exactly |
| N5 | witness family legitimate: increasing, onto, continuous at `1/2`, slopes `≤ 2` uniformly | 8 values of `g` |
| N6 | without non-vacuity the definition is degenerate | 4 vacuous pairs |
| N7 | with non-vacuity every candidate margin is refuted at the predicted `g > 1/(ℓ−2b)` | 6/6 exact |
| N8 | `r ≡ 0` is always admissible ⟹ forward budget vacuous without a lower bound | 4 cases |
| N9 | backwards closed form `max(ρ, ρℓ^{−G} + b(ℓ^{−G}−1)/(1−ℓ))` reproduces the recursion; `u_0 ≥ ρ` | 12/12 |
| N10 | corrected criterion `ℓ>1` or `(ℓ=1, b=0)`; `b=0, ℓ<1` still diverges; exponential asymptote | all |
