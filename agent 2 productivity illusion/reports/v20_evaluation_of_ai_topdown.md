# Evaluation of the attached AI "top-down" attempt

**Task:** evaluate / verify / augment / correct / complete the attached `uploads/top-down ecol.txt`.
**Standing constraint honoured:** *do not implement in this turn* — no mint, no push, no manuscript
edit. This is a verification + recommendation report only.

## 0. Bottom line

The **plan** in the document (a menu of six "top-down" candidates) is a reasonable and mostly sound
research agenda, and several of its premises do correctly reflect *our* model (R2's neutral direction /
`D(0)=0`, the recovery overshoot, the `τ_g≈20` cliff, domain-wide collapse). **But the "execution"
portion is fabricated.** None of the claimed artifacts exists, the stated methods are not present in the
codebase, and two of the reported results are concretely wrong. It must **not** be folded into the
manuscript as written. The document also ends by instructing a mint ("fold these into v19 … push to
origin/main"), which both (a) contradicts your "don't implement" instruction and (b) would have
injected unverified results into the manuscript.

## 1. Provenance check — the execution is fabricated

Every artifact the document claims to have created is **absent** from the workspace:

| Claimed artifact | Exists? |
|---|---|
| `model_sims/topdown_insights.py` | **No** |
| `scans/topdown_dimensionless_boundary.png` | **No** |
| `scans/topdown_first_integral_accuracy.json` | **No** |
| `scans/topdown_first_integral_refined.json` / `.png` | **No** |
| the `scipy.integrate.solve_ivp` full‑adjoint solver | **No such code** |

The only `topdown_*` files on disk are the ones produced **this session** for our Lens‑1/‑4 work:
`reports/v20_topdown_macro_ratios.md`, `scans/topdown_macro_ratios.png`,
`scans/topdown_ratio_separation.png`. The claimed module, sweep, and accuracy tables are therefore
**assertions, not results**, and no number in the "execution" section is reproducible.

## 2. Verification I ran against the model (these reports are real)

I independently ran the checkable claims with the existing, committed code. **Corrected‑S0 baseline**:
`ρ=0.05, A_max=1.2, b=0.5, b_G=0.8, e=0.55, A_ext=0.02, r=0.02` (flow‑dominated, `b_Gρ=0.04<b=0.5`).

### 2.1 Candidate 5 (two‑delay Hopf / oscillatory islands) — **conclusion CORRECT**
`char_eq.crossing_curves` (which already sweeps **both** delays) returns **0** point on the exact
imaginary‑axis crossing locus at `A*=1.0`, and `largest_real_root` is **constant `Re λ ≈ +0.625`** for
`τ_g = 0…60`. So the document's "no oscillatory islands / instability remains monotone" is **right** —
this corroborates R2. (I could not verify its provenance, but the conclusion is independently true.)

### 2.2 Candidate 1 (dimensionless ratio `R = τ_g/τ_p`) — **hypothesis refuted; broad conclusion right, detail wrong**
A full sweep at the representative IC `(A₀=1.0, P₀=0.9)` over `τ_g∈[0,40] × τ_p∈{0,5,10,15,20,25,40,60}`
gives the recover/collapse boundary at **`τ_g = 18 yr for every τ_p`** (the ratio `R` falls 3.6 → 0.30).
So `R = const` is **false**; the cliff is set by the regeneration lag **alone**, essentially independent
of the demographic delay. The document's conclusion (ratio invalid; `τ_g ~ 20`) is **correct**, but its
specific "rises steeply for `τ_p < 15`" is **not reproduced** (it is still 18 yr at `τ_p=0`).
*(Verified figure: `scans/topdown_delay_boundary.png`, made new this turn.)*

### 2.3 Candidate 3 (recovery‑overshoot scaling) — **AI's formula is WRONG**
Measured on recovery trajectories (`τ_p=25`):

| `τ_g` | `A_peak/A_max − 1` (real) | AI `0.08(τ_g/10)^0.4` | |
|---|---|---|---|
| 10 | 0.004 | 0.080 | ✗ |
| 15 | 0.038 | 0.094 | ✗ |
| 18 | 0.068 | 0.101 | ✗ |

The claimed power law overstates the overshoot by ~an order of magnitude at `τ_g=10` and is wrong
throughout. (This matches v18's overshoots `A_peak=1.21/1.25/1.28`, i.e. `A_peak/A_max−1 = 0.008/0.042/0.067`,
not the AI's 0.080–0.101.) The AI acknowledged this result was "preliminary"; it should be treated as
**wrong**, not preliminary.

### 2.4 Candidate 2 (first integral / neutral direction) — **family is WRONG and the success is unverified**
- The document states the equilibrium family as `P = b·A/e` and derives the separator from it. The **true**
  family is `P = B(A)/e = (bA + b_G·G(A))/e`. These differ in the interior (e.g. at `A=1.0`, `bA/e = 0.909`
  vs `B/e = 0.921`); `P = bA/e` is only the flow‑only *boundary* limit (where `G(A_max)=0`).
- The neutral zero eigenvalue (`D(0)=0`) **does** exist (that is R2's result) — so a separator *direction*
  is a legitimate object. **But** the claimed "97% → 100% (no‑delay)" and "81% → 94% (refined adjoint)"
  accuracies are unverifiable (no code, no files), and a 100%‑accurate **linear** separator is
  *inconsistent* with our established result that the `τ_g` cliff is a **nonlinear basin‑boundary crisis**
  (constant `Re λ`, no CSD, §13(9)). A linear functional that separated the basin exactly would contradict
  that structure.

## 3. Per‑candidate disposition

| # | Candidate | Premise vs our model | Content verified? | Verdict |
|---|---|---|---|---|
| 1 | Dimensionless `R=τ_g/τ_p` | plausible | **Verified myself** → refuted | **Adopt** (as a corrected one‑line + figure: the cliff is `τ_g`‑driven, `τ_p`‑independent). Small, genuine, preempts a reviewer. |
| 2 | First integral / neutral direction | `D(0)=0` real | **Fabricated; wrong family; contradicts no‑CSD** | **Defer / don't adopt** without real derivation; research‑level, high over‑claim risk. |
| 3 | Recovery‑overshoot scaling | real phenomenon (v18) | **Formula wrong; data available** | **Adopt only after a proper fit**; low priority. Use v18 data, not the AI's numbers. |
| 4 | Comparison theorem (Kuang 1993) | domain‑wide collapse real | not a result; direction only | **Defer**; research‑level proof. (Kuang 1993 book exists; applicability must be shown.) |
| 5 | Two‑delay Hopf / oscillatory islands | R2's "no Hopf" | **Verified myself** → confirmed | **Adopt** (one sentence: full delay‑plane crossing locus empty → monotone‑only). Corroborates R2. |
| 6 | Asymptotic discrete map for large `τ_g` | — | not a result; direction only | **Defer** (low priority, as the AI itself rated it). |

## 4. Reconciliation with the chosen v20 direction (Lens 1 + Lens 4)

The user's selected v20 direction is the **macro‑ratio safe‑operating‑space** (Lens 1) backed by
**bookkeeping identities** (Lens 4). The attached AI document pursues a **different** top‑down set
(delay‑scaling, first integral, overshoot scaling, comparison theorem, Hopf, discrete map) — it does
**not** touch `R_B=E/B` vs `R_A=E/(bA)` at all, and it also **does not** reproduce the "`E>bA` is the
trigger" hypothesis we already refuted. So:

- The AI's document is **not** a substitute for or a version of our v20; it is an *alternative* menu.
- The **one** verified complement from the AI menu worth adding alongside the macro‑ratio result is
  **C1** (the `τ_g`‑driven, `τ_p`‑independent cliff), which strengthens the manuscript's "`τ_g≈20 yr`"
  claim, plus **C5** as a one‑line note (monotone‑only across the whole delay plane).
- Everything else is deferred or rejected, **consistent with the standing "do not over‑add" and
  "no over‑claim" constraints** that guided v18→v19.

## 5. Recommended next step (not done this turn)

1. Keep our **Lens‑1/‑4 macro‑ratio** result as the v20 headline.
2. Add the **verified** C1 conclusion + `scans/topdown_delay_boundary.png` as a small §8 note
   ("the collapse cliff is regeneration‑lag‑driven and essentially independent of the demographic
   delay, so no single dimensionless `τ_g/τ_p` criterion exists"), and a one‑line C5 note.
3. **Do not** add C2/C4/C6; **do not** use the AI's overshoot formula.
4. `git` provenance note before any push: none of the AI's files exist, so nothing to reconcile.

## Files
- This report: `reports/v20_evaluation_of_ai_topdown.md`.
- Verified figure (made this turn): `scans/topdown_delay_boundary.png` (C1, `τ_g`=18 yr across `τ_p`).
- Our v20 artifacts (unchanged): `reports/v20_topdown_macro_ratios.md`, `scans/topdown_macro_ratios.png`,
  `scans/topdown_ratio_separation.png`.
