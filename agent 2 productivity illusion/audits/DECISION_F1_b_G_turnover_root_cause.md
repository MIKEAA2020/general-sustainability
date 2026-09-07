# Decision on F1: `b_G`/`V` identification — root-cause choice

**Question:** option (a) *"treat `b_G = 0.8` as a dimensionless scaled coefficient and drop the `V = 20–100 yr`
identification"* vs option (b) *"set `b_G` from a physical turnover time (`b_G = b·V`) and recompute the
spectrum, cliff, and recover fractions."*

**Answer: option (b).** It addresses the root cause thoroughly and honestly; option (a) is a quick fix that
resolves the letter of the units complaint while preserving a model that does not represent the systems it
claims to describe.

---

## The root cause is deeper than a unit typo

Three *linked* problems, all confirmed by direct calculation:

**1. Wrong unit identity.** The manuscript writes `γ = 1/b_G = 1/V`. Correct physical identity:
`V = b_G·A / (b·A) = b_G/b`, so `1/V = b/b_G`, not `1/b_G`. So
`γ_conv = 1/b_G` (harvest/conversion, `ha·gha⁻¹`) and `1/V = b/b_G` (turnover **rate**, `yr⁻¹`) are two different
quantities. The paper conflates them.

**2. The value flatly contradicts the story.** `A` is stated to be in physical hectares (md line 151, so `b = B/A`
is definable), making `b_G` a **physical** standing-stock value. Then `b_G = b·V`. At baseline `b_G = 0.8, b = 0.5`:

```
V = b_G/b = 0.8/0.5 = 1.60 yr
```

a **1.6-year** turnover — a crop-like system, *not* the 20–100 yr forest/soil the manuscript everywhere invokes.

**3. The regime contradicts the ecological claim — this is the real problem.** The model's regime index is
`b_G·ρ ⋚ b`. At baseline `b_G·ρ = 0.04 < b = 0.5` (flow-dominated); the manuscript itself states the baseline is
flow-dominated ("the orchard limit"). With a physical turnover `b_G = b·V`:

```
b_G·ρ > b   ⟺   V·ρ > 1   ⟺   V > 1/ρ = 20 yr
```

So **any** forest/soil turnover of `V = 20–100 yr` places the model in the **capital-dominated** regime
(`b_G·ρ > b`), with an interior MSY, a fold, and smooth decline — the Scheffer/fold picture — *not* the
flow-dominated orchard regime in which all the paper's headline numerics were computed. The manuscript is
self-consistently flow-dominated, but flow-domination itself requires `b_G < b/ρ = 10`, i.e. `V < 20 yr`. So
the baseline `b_G = 0.8` and the claimed `V = 20–100 yr` are **mutually exclusive**.

This is the crux: the model's framing is ecological (forests, soils, fisheries, decades), but its numerics
describe a fast-turnover (sub-20-yr) crop-like system.

---

## What option (a) actually buys

Option (a) keeps `b_G = 0.8`, keeps all numbers, and just removes the "20–100 yr" and `γ = 1/b_G = 1/V`
sentences. It resolves the *unit* error but leaves the manuscript claiming to be about forests while the
dynamics are a 1.6-yr crop. Because the manuscript's entire quantitative apparatus — the masking window, the
`τ_g ≈ 18–20 yr` collapse cliff, the `0.399 → 0.0529` recover-fraction basin, prediction 6 — was computed at
`b_G = 0.8` in the flow-dominated regime, adopting (a) would require re-scoping *all* of it as a
"fast-turnover stylised system," abandoning the ecological motivation the title, abstract, and intro all assert.
That is a large re-scoping disguised as a small edit — and it does not make the model consistent, it makes it
honest by disclaiming its own subject matter. That is still a quick fix.

## What option (b) reveals (verified, not asserted)

Setting `b_G = b·V` and re-running the characteristic equation (`D'(0)` and real-axis roots, `(τ_g,τ_p)=(30,25)`):

| `V` (yr), `b_G` | regime | `S = b/b_G + G′(A*)` | `S − r` | `D'(0)` | positive real root |
|---:|---:|---:|---:|---:|:--:|
| 1.6 (→0.8) | flow-dom | +0.608 | +0.588 | −0.903 | +0.625 |
| 20 (10.0) | marginal | +0.033 | +0.013 | −0.040 | +0.041 |
| 27 (13.5) | **capital-dom** | +0.020 | +0.0004 | −0.021 | +0.024 |
| 30 (15.0) | capital-dom | +0.017 | −0.003 | −0.015 | +0.018 |
| 40 (20.0) | capital-dom | +0.010 | −0.010 | −0.003 | +0.004 |
| 50 (25.0) | capital-dom | +0.003 | −0.017 | +0.005 | **none** |
| 100 (50.0) | capital-dom | −0.007 | −0.027 | +0.020 | **none** |

Two consequences:

1. **Regime flip.** For `V > 20 yr` the model leaves the flow-dominated baseline; the masking-window and
   recover-fraction results, all computed in flow-dominated regime, must be re-derived in the capital-dominated
   regime. This is the correct regime for forests/soils and changes the numerical story substantially.
2. **The headline "positive real eigenvalue for every delay" is not robust to physical `b_G`.** It survives
   only up to `V ≈ 40 yr` (and then only marginally), and it **vanishes** for slow old-growth turnover
   (`V ≥ 50 yr`), where `D'(0) > 0` and there is no positive real root. This is independent of the delay, so at
   physical forest turnover the *structural* vicious cycle weakens and then disappears.

I also found a subtle error in **my own v31/v32** sufficiency statement: I wrote the condition as `S > r`.
The correct condition for a positive real root (given `D(0) = 0` and `D(s) → +∞` for real `s → +∞`) is
`D'(0) < 0`. `S > r` is *sufficient* but not *necessary* — at `V = 30` (`S − r = −0.003`) there is still a
positive root (`+0.018`) because `D'(0) = −0.015 < 0`. This correction must be made wherever the "positive real
eigenvalue for every delay" claim is stated (abstract, §4.3, §5, §6, §8, SI §S3.4).

---

## Why (b) is the thorough fix

- It makes the **parameter, the units, and the regime** mutually consistent with the model's stated ecological
  subject — the root cause, not its symptom.
- It forces the paper to honestly **re-run** the numerics in the correct regime, and to state whether the
  results — the masking illusion, the `τ_g ≈ 18–20 yr` cliff, the recover-fraction basin, prediction 6 — survive
  at physical forest/soil turnover. That re-run is exactly what a thorough fix demands, and it may change the
  paper's central claims.
- It surfaces the deeper truth the audits (Grok and GPT especially) hinted at but stopped short of: the headline
  "vicious cycle" is a property of the *fast-turnover flow-dominated* regime, not of the slow ecological systems
  the paper is nominally about.
- Option (a), by contrast, preserves a model that is internally inconsistent at its core.

## What implementing (b) requires (v33)

1. **Fix the unit identity everywhere:** `γ_conv = 1/b_G` (ha·gha⁻¹) is **not** `1/V`; `1/V = b/b_G` (yr⁻¹).
   Correct md lines ~199, ~314 and SI §S2/§S1.2; add `γ` to Table 2.1; define `b_G` as a physical value.
2. **Pick one defensible interpretation** and state it. Given the framing, either (i) adopt a physical
   `b_G = b·V` with a stated `V` (so the model genuinely treats forests/soils), or (ii) explicitly re-scope as a
   *fast-turnover stylised* orchard and drop the ecological-motivation claims. The ecologically-honest choice is
   (i), and it is the one implied by "address the root cause."
3. **Recompute in the capital-dominated regime** (`V > 20 yr`): the spectrum (`S`, `D'(0)`, the positive-real-root
   condition, and the no-Hopf claim), the `τ_g` decay-response cliff and recover-fraction basin, and the masking
   window. Report whether prediction 6 and the "collapse whenever `τ_g ≳ 20`" claim survive.
4. **Correct the sufficiency condition** `S > r` → `D'(0) < 0` (my v31/v32 error) across abstract, §4.3, §5,
   §6, §8, SI §S3.4.
5. Reconcile the two recover-fraction tables (τ_p = 25 flat vs τ_p = 0 re-opening) and the regime-scoped
   `b_G` sweep — the current `0.4–1.2` sweep does not reach the physical `b_G ≳ 10`.
6. Re-verify the empirical `τ_g` anchor (SI §S5.1) once the regime/units are fixed, since its rate/lag caveat and
   the "band lies in the collapse regime" claim both depend on the (re-derived) regime.

This is a substantial re-derivation, not a patch; it is the honest cost of the root-cause fix. I recommend
proceeding with (b) and am ready to carry out items 1–6 for a v33 (recomputed, error-free LuaLaTeX + PDF),
never overwriting v30/v31/v32.
