# v33 Revision Plan — Scope-A: the two-land conversion model (root-cause)

**Decision accepted.** This is the **revision plan** for `manuscript_ECOMOD_v33`. It is a *plan*, not the
manuscript — I will not edit any file until you accept this plan. It targets the **most honest, comprehensive,
root-cause-addressing** resolution, which is **scope-A (two-land conversion)**. It supersedes scope-B and the
one-stock framing.

**Why scope-A is the root-cause fix.** The single-stock scalar aggregate is the cause of every trouble we
found: the illusion being only a ~5-yr window (instead of generic), the false "`+0.625` for every delay," and the
inability to carry the title. The biosphere/footprint accounting is intrinsically **two-component** (fast
harvest land + slow carbon/forest land) with **land-use conversion as the historical operator**; GFN itself is
that split (cropland ≈19% of EF, equivalence factor ≈2.5; carbon ≈60% of EF). Scope-A makes the model
*the* object the title describes.

> ⚠️ **SUPERSEDING NOTE (from `JOINT_EVALUATION_of_gpt_consolidation_plan.md`, 2026-09-07).** The GPT
> consolidation plan is **verified technically more correct than Parts A–H below** on the equilibrium/stability
> inheritance, and it **fixes errors I had inherited from the one-stock result**. Specifically, the following in
> this plan are **WRONG and must be corrected**: (1) the `P = B/e` family / `det J ≡ 0` do **not** survive the
> two-land equations (the no-conversion face pins `A_c` to boundary → **boundary equilibria**, no continuum);
> (2) the regime boundary is the **ratio** `b_G,c ρ_c > b_c` (i.e. `V_eco < b_G,c/b_c`), **not** `1/ρ_c = 20 yr`;
> (3) the one-stock unified model is a **comparator / aggregation artefact**, **not** exactly nested in scope-A.
> Where this plan conflicts with the joint evaluation of the GPT plan, **the GPT correction wins** (it is
> verified). The relevant corrections are applied inline below in blue-marked edits; the full reconciliation is in
> `JOINT_EVALUATION_of_gpt_consolidation_plan.md`.

---

## Part A — The adopted model (scope-A)

**States (5 dynamical, 2 delays):** `A_f` fast/provisioning land (ha), `A_c` capital/ecological land (ha),
`P` population (cap), `D` soil/productivity debt (gha·yr). **`A_r` (reserve land, ha) is a state, not a static
residual:** the fixed-total constraint is only satisfied dynamically with `Ȧ_r = −G_c(A_c(t−τ_g)) + L_c + η_f A_f`.
**Constraint:** `A_f + A_c + A_r = A_tot` (fixed), enforced dynamically; `A_r ≥ A_r^min` is the typed floor.
**Closure decision:** `G_c` is treated as a **capital-land *growth* flow** (adds to `A_c` accounting capacity),
*i.e.* regeneration is a growth flow, **not** a land-area transition out of `A_r`, unless explicitly stated
(`A_r → A_c` under restoration).

```
G_c(A_c) = ρ_c A_c (1 − A_c / A_c,max)                         (1)
b_f      = (b_f0 + T_b(t)) e^{−α D}                            (2)
Y_f      = b_f A_f                                            (3a)
Y_c      = b_c A_c + b_G,c G_c(A_c)                           (3b)
B        = Y_f + Y_c                                          (3c)
E        = e P                                                (3d)
S        = [E − σ_f Y_f − σ_c Y_c]₊                            (4)
dA_c/dt  = G_c(A_c(t−τ_g)) − S/κ − L_c                        (5)
dA_f/dt  = S/κ − η_f A_f                                       (6)
dP/dt    = r P [1 − P / K(t−τ_p)],   K = B/e                 (7)
dD/dt    = [E − B]₊ − η D                                     (8)
T_b      = Δb / (1 + exp(−κ_w(t−t_wave)))                     (9)
```

**Adopted parameter conventions (honest):**
- `κ = b_f` (**unit fix** from grok): makes `dA_c/dt = S/κ = S/b_f` in **ha·yr⁻¹**. `κ` is the conversion
  coefficient, **not** `V_eco`. Verified: `dA_c/dt` is colometric.
- `γ = 1/b_G,c` is **timber harvest only** (the `L_c` channel), and `1/V_eco = ρ_c`. **Never write `γ = 1/V`.**
- `L_c = [H_c − σ_c Y_c]₊ / b_G,c` (optional Schaefer/fold channel).
- Ecological turnover of forests lives **only** in `ρ_c, τ_g, A_c,max`; set `V_eco ~ 30–50 yr` there without
  touching the conversion gain.
- `[·]₊ = max(·,0)`; donor limitation: `S/κ` ≤ available `A_c`.
- Floors: `A_c ≥ A_c,ext`, `A_f ≥ 0`, `K ≥ K_min`.
- Delays only where they were: recruitment of `A_c` (τ_g), demography on `K` (τ_p). `D` is not delayed.

**What changes vs v32 (the one-stock → two-land map):**
| v32 (one-stock) | v33 (two-land) |
|---|---|
| `A` (single stock) | `A_f` + `A_c` (two physical-hectare states) |
| `b_G` converts flow→stock loss ("eat the trees") | `S/κ` converts shortfall→**land conversion** (arc_land) |
| illusion ≈ 5-yr window | illusion **generic** — `dB>0`, `dA_c<0` whenever `b_f > b_c + b_G,c G_c′` |
| one collapse channel | **conversion-driven (food) is structural; the fold-driven (timber) channel is CONDITIONAL** — it exists only iff `b_G,c ρ_c > b_c` (an un-identified ratio), so report BOTH regimes, don't assert two guaranteed channels |

---

## Part B — Corrected identity & stability (the honest mathematics)

All verified against `char_eq.py` / the two-land reproduction. These go into §2.1 and §4.1–§4.3:

1. **`det J ≡ 0` is a ONE-STOCK result — it does NOT transfer.** On the two-land no-conversion face
   (`S = 0`, `L_c = 0`, `η_f > 0`), the equilibria are `(A_f* = 0, A_c* = 0 or A_c,max)` — **boundary**, not a
   continuum. Verified: `G_c(A_c*)=0` only at `A_c = 0, A_c,max`. So there is **no `P = B/e` equilibrium family
   and no `det J ≡ 0`**. **Derive the full 4×4 delayed Jacobian per active set; do not inherit any determinant
   sign.**
2. **Sufficiency is `D′(0) < 0` in the one-stock comparator, not `S > r`.** In scope-A, compute
   `det Δ(λ) = 0` (`Δ(λ)=λI−J₀−J_g e^{−λτ_g}−J_p e^{−λτ_p}`) per active set. No eigenvalue is inherited; the
   `λ = −r` at the interior capacity max and the `+0.625` are both **one-stock/off-MSY facts**, not scope-A.
3. **Regime boundary is a ratio, not a timescale:** interior capacity maximum
   `Y_c′(A_c*)=0 ⟺ b_G,c ρ_c > b_c`, i.e. **`V_eco < b_G,c/b_c`** (`V_eco := 1/ρ_c`). The value `1/ρ_c = 20 yr`
   is only the regeneration timescale — it is **not** the boundary. (The earlier "`V_crit = 1/ρ = 20 yr`" and
   "`V = 1/(ρ+r) ≈ 14 yr`" were wrong and are removed; do not quote them as the boundary.)
4. **`ψ_c* = 2b_c/(b_c + b_G,c ρ_c) = 2/(1 + b_G,c ρ_c/b_c)`** (state-dependent `ψ_c(A_c) = b_c A_c/Y_c(A_c)`).
   `ψ_c* = 1` iff `b_G,c ρ_c = b_c`; `ψ_c* = 1/2` iff `b_G,c ρ_c = 3b_c`; interior MSY iff `b_G,c ρ_c > b_c`.
5. **`b = B/A` is false** — `B` has two terms, and there are two lands.
6. **The vicious cycle "returns as a different loop"** — the **conversion loop**:
   `A_c↓ → A_f↑ → B↑ (if b_f > b_c^eff) → K↑ → P↑ → S↑ → A_c↓`. Gain is `(b_f − b_c^eff)/κ`, an
   **NFA-measurable** number, *not* `b/b_G` with `b_G = 0.8`. Verified: gain `+0.75 → +0.92` for
   `A_c ∈ [0.6, 1.0]`, and it is **largest past the forest MSY** (where `G_c′ < 0`).

---

## Part C — Honest accounting: survives / dies / reframed (from grok's comparison table, verified)

| Claim (v32) | Verdict | In v33 (two-land) |
|---|---|---|
| Deficit accounting | survives | survives as **conversion accounting** (shortfall above flow + sustainable increment converts land) |
| `P = B/e` family | **one-stock only** | **does NOT survive** — the two-land no-conversion face gives **boundary** equilibria (`A_f*=0`, `A_c*=0`/`A_c,max`); no continuum, no `det J ≡ 0` |
| `R_B = 1` vs `R_A` leading | structure survives | **sharper**: `R_B` is the aggregate; `R_A = E/Y_f` is the conversion trigger; `R_B < 1` with `R_A > 1` is the masking |
| Vicious cycle `λ ≈ +0.62` | **dies at forest V** | **returns as the conversion loop** (different, physical gain) |
| Fold / MSY / Scheffer | only via B1 | **CONDITIONAL on `A_c`** — present only iff `b_G,c ρ_c > b_c` (verified: absent at forest-effective `ρ_c=1/30`, present at fast-effective `ρ_c=0.08`); the fold is **identification-dependent, not structural**. Only the conversion-driven channel is structural. |
| `τ_g` cliff, no CSD | **one-stock only** | **does NOT reproduce** in two-land (recover fraction ≈ flat in τ_g, 0.54→0.52→0.50). The conversion **fold HAS CSD**. Re-scope: cliff was a one-stock reading; the honest transition is a **demand-driven fold with critical slowing** |
| Productivity illusion (~5.4 yr) | narrow/unknown | **generic and potentially long-lived** (a *hypothesis to be demonstrated numerically/empirically* — see J2): window closes when soil debt or the arable ceiling binds — decades, not 5 yr |
| Technology raises debt | Jevons on one stock | **Green Revolution**: `T_b` lifts `b_f` → lifts `K` → lifts `P` → **accelerates conversion** |
| No rescue-by-stock / no CSD | delay-cliff property | **typed-floor theorem**: any policy observing only `B` cannot guarantee `A_c ≥ A_c,min`; rescue-by-`A_f` is the illusion |
| Half-Earth | ambiguous σ on `bA` vs `B` | **one operator**: freeze conversion (cap `A_f` or floor `A_c`) |
| NFA 1961–2022 | "consistent with," not evidence | **well-posed empirical programme**: decompose `d ln B` = yield + cropland expansion + forest loss, with independent `A_c` (land cover) and `b_f` (FAO yields) |

**The two honesty commitments I will not drop:** (a) `λ ≈ +0.625` must **not** be claimed as a forest/soil/Earth
result — it is the fast-provisioning, `V = 1.6 yr` harvesting-basket signature, and the v33 mechanism is the
conversion loop; (b) the **NFA series is evidence of composition change, not of a 1.6-yr cycle**.

---

## Part D — Division of labour with the program (no duplication)

- **paper1** owns the aggregation theorem (Prop 1). v33 **cites** it and *illustrates* it with a two-land
  dynamical realisation. Do not re-prove.
- **paper3** owns the full vector ledgers / depletion horizons. v33 is a **minimal dynamic** two-component model,
  distinct from that accounting.
- **paper4 / v18** owns the slow-turnover delay-amplified regime (Hopf, bistable windows). v33 **hands off**:
  for `V_eco > 1/ρ`, collapse is the fold + τ_g cliff + debt, treated in paper4.
- **v33 owns:** the generic illusion (applied Prop 1), the conversion-driven vicious loop, emergent carrying
  capacity, `R_B`/`R_A` split, the typed-floor theorem, the recovery cliff.

---

## Part E — Section-by-section edit map

1. **Title/abstract:** keep "productivity illusion"; reframe the headline as *generic* (the aggregate `B` can
   rise while a component `A_c` falls); state the capacity-maximum boundary as the **ratio**
   `b_G,c ρ_c > b_c` (= `V_eco < b_G,c/b_c`), **not** any single timescale; label any `+0.625` as the
   harvesting-basket baseline (`V = 1.6 yr`); announce the empirical NFA-decomposition programme.
2. **§2.1 Variables/units:** two lands; `κ = b_f`; `γ = 1/b_G,c`; `1/V_eco = ρ_c`; delete `b = B/A`.
3. **§2.2 Governing equations:** replace with the two-land set (1)–(9) + closures.
4. **§3 Assumptions:** revise to two-land (conversion, donor limitation, typed floor, one-way fast conversion).
5. **§4.1** identity (γ, 1/V_eco). **§4.3** stability two-column (fast vs slow) + `D′(0)<0` + regime boundary.
   **§4.4** fixed-liability / saddle-node = MSY on `A_c`; `ψ_c* = 2/(1+b_G,c ρ_c/b_c)`. **§4.5** `R_B`/`R_A`.
6. **§5 Principal claims:** two columns (fast: conversion loop; slow: fold + τ_g cliff, no CSD).
7. **§6 Falsifiable predictions:** state each as **conditional** / to be re-derived under scope-A (predictions
   are *hypotheses*, not results) — e.g. Pred 1 only for the fast/flow-dominated face; Pred 6 (τ_g ≈18–20 yr
   cliff) re-verified on `A_c` + continuation diagram.
8. **§8 Recovery dynamics:** τ_g cliff lives on `A_c`; fast land cannot rescue a long forest lag; **recovery is
   not reversible** — requires an explicit restoration flow (`A_f→A_c` / `A_r→A_c`); report with
   `R_c(T) = (A_c(T)−A_c^deg)/(A_c^init−A_c^deg)`.
9. **§9 Half-Earth → typed-floor theorem:** freeze conversion; guarantee `A_c ≥ A_c,min` (a **typed floor**,
   distinct from the reserve floor `A_r ≥ A_r^min` and the arable ceiling `A_f ≤ A_f^max`).
10. **§12 Discussion:** bridge to paper4 (slow regime), state the honest NFA interpretation.
11. **References:** add Krausmann 2013, Haberl 2007, Erb 2017, Carvalhais 2014, GFN/equivalence factors,
    Poorter, Poeplau, Hutchings & Reynolds.

---

## Part F — Queued audit items (F1–F23, R1–R16, S1–S10)

- **Carry through v33** (now on the two-land model): F1 (b_G=b·V → becomes the two-land `κ`, `1/V_eco`),
  the τ_g/recovery items, R_B/R_A, the `det J ≡ 0` repair, `D′(0)<0`, `b=B/A` false, `γ≠1/V`, `ψ_c*` fix,
  the Neubauer citation (*Science* 340:347–349).
- **Now moot / superseded:** B1 vs B2 (Scheffer-fold vs 1.6-yr-crop) — the two-land model *has* both collapse
  channels; "no Hopf / no gross-harvest Hopf numbers" recompute; the one-stock `V_crit = 75` **and** the
  `1/ρ = 20` — both corrected to the ratio boundary `b_G,c ρ_c > b_c` (no single-timescale boundary).
- **Still-valid standing constraints:** σ dimensionless; `[x]₊ = max(x,0)`; delay structure; `K = B/e`
  algebraic; abstract standalone ≤315 words; no "hens"; never overwrite (produce v33).

---

## Part G — Open technical questions to resolve during implementation (I will verify, not assume)

1. **κ unit convention:** adopt `κ = b_f` (`dA_c/dt = S/b_f` in ha·yr⁻¹). Confirm the conversion *rate* vs
   *stock* semantics (a permanent shortfall converts a stock of hectares per year). Resolve during the
   equilibria/stability build.
2. **The conversion-loop stability:** derive the 4×4 Jacobian at the conversion equilibrium, identify the
   loop `A_c↓→A_f↑→B↑→K↑→P↑→S↑→A_c↓`, and find its gain/threshold — this is the honest replacement for
   `+0.625`.
3. **Equilibrium structure:** derive the equilibria **per active set** (`S=0`/`S>0`/`L_c>0`/`K=K_min`). On the
   no-conversion face they are **boundary** (`A_f*=0`, `A_c*=0`/`A_c,max`); there is **no `P = B/e` continuum**.
   Determine where (if anywhere) an interior equilibriium exists under active conversion, and whether
   `A_r`'s balance term permits interior solutions.
4. **Critical slowing / no-CSD:** re-test the "no CSD" claim on the capital-land fold, in case it needs
   qualification now that the fold is two-land.
5. **NFA decomposition:** implement the `d ln B =` yield + cropland expansion + forest-loss decomposition
   against the 1961–2022 series, to test whether the "composition change" reading is quantitatively supported
   (or at least internally consistent).

---

## Part H — Remaining items from the whole corpus, incorporated (prioritised)

I swept the entire corpus (`JOINT_EVALUATION_of_four_audits_v32.md` F1–F23/R1–R16/S1–S10,
`data/MASTER_joint_assessment_and_implementation_plan.md` Parts 6/8/11/12,
`GAP_SCAN_line_level.md`, `reviews/`, `supplementary/`, and the manuscript). Each item is classified
**VERBATIM** (applies unchanged), **TRANSFORMED** (must be re-derived under two-land), **MOOT**
(superseded by scope-A), or **RECONCILIATION** (relates the prior verified model to scope-A).

### H1. RECONCILIATION (the most important new read) — scope-A *extends*, not replaces, the verified unified model

The master plan's round-2 adjudication (Part 11, Claude wins) already settled the root cause as a
**bookkeeping** fix, and verified it symbolically: the manuscript's depletion term was **not flatly wrong** —
it is the increment-harvest limit (`ψ→0`). The correct model is the **unified stock–flow (1‴)**:

```
dA/dt = G(A(t−τ_g)) − [E − bA]₊/b_G ,   B = bA + b_G G(A) ,   ψ = bA*/B*
```

This was fully verified (deficit = stock-decline identity exact; `b→0` recovers the manuscript's Eq. 1 with
`γ = 1/b_G`; moving ceiling preserved; `ψ` is a GFN-faithful cropland/grazing vs forest/fishery decomposition).

**scope-A is the *extension* of (1‴) but (1‴) is NOT exactly nested in scope-A.** GPT verified the aggregation
fails: `d(A_f+A_c)/dt = G_c(A_c(t−τ_g)) − L_c − η_f A_f` is **not** a function of `A_f+A_c` alone. So the one-stock
unified model is a **didactic aggregation / comparator / aggregation artefact** (boxed limit / Appendix G), **not**
an exact special case of the two-land system. **Consequence for the plan:** keep (1‴)'s verified results (its
own neutral zero eigenvalue on its `P = B/e` family; `Re λ ≈ +0.59→+0.62` at baseline, no Hopf; `ψ`-dependence;
R1 recover-collapse) **labelled as the one-stock comparator**, and state explicitly that these do **not**
automatically transfer to scope-A. The scope-A headline is the **conversion loop**, derived afresh.

### H2. VERBATIM items to carry unchanged

- **F4:** `t₅₀ ≈ 145/ρ` is a factor-of-20 blunder → `t₅₀ ≈ 7.1/ρ` (recompute for the capital-land recovery).
- **F5/F6:** two delays (not three); `b = B/A` false (two terms, two lands).
- **F12–F14:** Neubauer → **Science 340(6130):347–349**; qualify the H&R "29 % recovered" as paraphrase;
  "**secondary** forests", and the 66-yr/95-yr tail **beyond** the band.
- **F20:** unify `τ_p*` (231 vs 225).
- **F21–F23:** SI §S5.1 data-integrity — regenerate or delete the unreproducible coarse-grid table; quote all
  four fine values; the τ_g rate/lag caveat must be referenced against `t₅₀ ≈ 142 yr`, **not** `1/ρ = 20 yr`.
- **R1, R4:** "no imaginary-axis crossing" must exclude the permanent zero root; display **both** fixed-liability
  roots (±).
- **R6, R8:** a single **baseline registry**; define CSD / return-time explicitly (delicate near a zero root).
- **R10:** `D = ∫[E−B]₊dt` should say "**modulo repayment**"; the `b_G` sweep is too narrow to test the physical meaning.
- **R12/S9:** separate genuine predictions from assumption/output restatements; the "fast–slow classification"
  described is a *reduction*, not the model — move it away from the model's own results.
- **S1, S3, S5–S7:** "`η` decides whether an equilibrium exists" too broad; `R_B` on `B` vs `B̃` notation; numerics
  more precise than stated; add an observation model for the empirical programme; add `γ` to the symbol table
  and define `A_ref`, `K_min`.
- **R16/S10:** reduce the phase-line / "no path memory" argument to a one-line scoping note.
- **12G.6 submission hygiene:** orphan **May 1973** reference (cite or remove); "Ecological Model(l)ing" journal
  name; keyword-list mismatch; supplementary as `.py`/`.pdf`; strip PDF-metadata author and submission tool
  artifacts.

### H3. TRANSFORMED items (re-derive under two-land — do not copy verbatim)

- **F2:** `det J ≡ 0` is **one-stock-only** (`char_eq`/S0). Under scope-A, on the no-conversion face the
  equilibria are **boundary** (`A_f*=0`, `A_c*=0`/`A_c,max`), so **no continuum and no `det J ≡ 0`**. Derive the
  4×4 delayed Jacobian per active set.
- **F3/F7:** reservation → `σ_f, σ_c` shares and the **typed floor** `A_c ≥ A_c,min`; the `σ<1` "locus" becomes
  a policy nullcline or `K_σ`; `ψ_c* = 2/(1 + b_G,c ρ_c/b_c)`, `= 1` at `b_G,c ρ_c = b_c` (not 1/2).
- **F8/F16:** `R_B = 1` is an *equilibrium/zero-delay identity*, not a trajectory boundary; `Ω → R_B`; label the
  two basin numbers.
- **F9:** state the admissible domain + clamps (`A_c ≥ A_c,ext`, `A_f ≥ 0`, `K ≥ K_min`, `A_tot`, donor limitation)
  as a constrained system; label clamped-run results as such.
- **F10/F11:** reconcile the §8 flat `0.0529` (τ_p=25) vs §12.2 non-monotone re-opening (τ_p=0); the τ_g cliff
  lives on `A_c`; the "field-supported band" vs core band must be reconciled and τ_p labelled.
- **F17/F19:** condition the typed-floor / "no rescue / measure-zero / May / compounding" claims; tag the
  gross-harvest vs deficit-driven formulations and move the `χ`/Hopf classification to "**what we are not claiming**."
- **R2, R3, R5, R11, R15:** the three-fold accounting fusion → two-book `Y_f = b_f A_f`, `Y_c = b_c A_c + b_G,c G_c(A_c)`;
  the equilibrium family is a *degeneracy of the closed-loop equations*, not a generic property (on the no-conversion
  face); nested delayed-state dependence in `K(t−τ_p)`; the "protective stance" is a **freeze-conversion** operator,
  a modelled controller; add a silent-collapse-fraction *figure*.
- **S2:** `d ln B = d ln b + d ln A` holds **only for the flow component**; `d ln A/dt` is bounded (relevant to the
  NFA decomposition).
- **S4:** the `0.608–0.625` eigenvalue range is correct but under-labelled — label it the **fast-provisioning
  baseline** value, and present the scope-A mechanism (conversion loop) as the headline, not a single eigenvalue.

### H4. MOOT / superseded by scope-A (drop, don't carry)

- B1 vs B2 (Scheffer-fold vs 1.6-yr-crop) — the two-land model **has both** collapse channels (conversion-driven
  food, fold-driven timber).
- The one-stock "`+0.625` for every delay" headline (corrected — see joint evaluation §6).
- Single-`V` "1.6-yr crop vs 20–100-yr forest" — replaced by the two-state `A_f` (fast) + `A_c` (slow) split.
- Any Allee term (replace with emergent `A_c(E)`).
- The `γE` gross-harvest depletion form as the *only* term (retain `L_c = [H_c − σ_c Y_c]₊/b_G,c` only as the
  timber/fold channel).

### H5. LIVE authorial forks (master Part 6) — recommend, but you decide

| Fork | Master default | Under scope-A (recommend) |
|---|---|---|
| F4 keep/drop `D` | drop D → 2-D | **keep D** as the soil/productivity-debt channel degrading `b_f` (a third, separately-evidenced ingredient) |
| F8 units | GFN mandatory | **GFN** — `E,B` in gha·yr⁻¹, `D` in gha·yr, `A_f,A_c` in ha |
| F9 Allee | emergent | **emergent** `A_c(E)`; drop Allee |
| F5 τ home | recruitment τ_g | **recruitment τ_g** (liquidation immediate) |
| F3 hard/smooth | hard max + state one-sided | **hard `[·]₊`** + state one-sided/boundary stability |

### H6. MASTER residual risks — carry as honest limits (do not over-claim)

- **Parameters are not verified right**; the whole numerical table must be **recomputed** under the corrected model.
- **The `χ` fast–slow reduction fails at realistic `ρ`** (0.02–0.1 yr⁻¹); use the full transcendental equation; and
  **"no single delay destabilises" must scan to `τ_p ≳ 250 yr`** (the demographic-delay Hopf only appears at
  `τ_P ≈ 225 yr` off the knife-edge). Carry into Part G.1/G.4.
- **`η → 0` singularity** (`D* → ∞`): set `η = 0.05 yr⁻¹` and justify; it is not a free robustness dial.
- **Non-smoothness of `[·]₊`:** the sustainable state is a boundary; one-sided stability must be stated.
- **Knife-edge measure-zero parameters** (`r²a₁₁² = (γ e a₂₁)² = 1.0×10⁻⁴`, Λ = 0): non-generic and unexplained —
  justify or perturb off the surface and report the generic result ("exactly one lag destabilises, by sign of Λ").
- **Debt figure method-dependence** (5.26 / 6.74 / 18.70 depending on endpoint convention): report as a protocol
  choice, not a clean `.240` number.
- **`K → 0` non-Lipschitz blow-up**: not a smooth approach to a collapse attractor — state a minimum-viable-K /
  carrying-capacity floor as a limitation.
- **Do not claim Hutchinson priority** (unsupported); GFN's own caveats bound the 1961–2022 claim.

### H7. Notational reconciliation across the program (do this first)

The master (`M, P, r_opt, γ, b₀, χ, τ_M, τ_P`), the v32 manuscript (`A, P, D, b, b_G, ρ, σ, τ_g, τ_p`), and the
audits use **inconsistent** symbols for the same quantities. Before editing, adopt **one** convention in v33
(proposal: the manuscript's `A_f, A_c, P, D, b_f, b_c, b_G,c, ρ_c, σ_f, σ_c, τ_g, τ_p, κ, e`) and map the master's
`M→A`, `r_opt→e`, `γ→1/b_G,c`, `b₀→b_f0`, `τ_M→τ_g`, `τ_P→τ_p`. This avoids silently mixing the two notations.

---

## Part I — Second-pass items found on the deeper search (v15–v20 reports, SI, model code, master 12H)

### I1. Five verified NEGATIVE results — scope-A must preserve, not silently undo

These were computationally verified and are presented as §13(9) negative results (v18/v19). They are
**structural claims**, not gaps. Under scope-A they must either survive or be *explicitly* revised — do not let
the two-land reframing quietly erase them:

| # | Negative result | Status under scope-A |
|---|---|---|
| N1 | **No CSD / early-warning** before the τ_g cliff | **RE-SCOPED (verified two-land):** the *conversion* **fold HAS CSD** — the active-conversion saddle's `λ+ → 0` as `E → E_ceil` (0.058→0.0379→0.0225→0.0120→0.0003). And in two-land there is **no τ_g cliff** (recover fraction ≈ flat in τ_g). So N1 as one-stock did **not** transfer: the honest statement is "the fold has CSD; the one-stock 20-yr `τ_g` cliff does not reproduce." |
| N2 | **No hysteresis / path-dependence** in the fixed-liability threshold — `A_c(E)` single-valued; no bistability per fixed `E`; threshold identical up/down | Keep. Maps to R16/S10 (reduce "no path memory" to a scoping line). |
| N3 | **No sustained boom–bust limit cycle** — overshoot-recollapse is a single recovery-overshoot **pulse** (2 crossings of 0.5·A_max), not a cycle; consistent with the monotone (no-Hopf) leading mode | Keep. With the two-land fold, re-state the mechanism (the transient lives on `A_c`). |
| N4 | **No Allee-style rescue threshold** — collapse at τ_g=30 is **domain-wide** (every A₀ 0.02–1.00 collapses, incl. healthy A₀=1.0); rescue zone is a **measure-zero strip** at A₀=A_max. **"Cannot rescue by starting higher — must shorten the lag."** | Keep — this is the strongest policy-relevant negative result. |
| N5 | **No "50 % anchor ⇒ fast full recovery"** — t50/t95 ≈ 0.59–0.77, so 50 % is *not* "most of the way there" | Keep (reinforces the rate/lag decoupling and the lumped-τ_g caveat). |

### I2. RECONCILIATION — the master's "illusion is necessarily transient" proof is ONE-STOCK-only

The master Part 1 lists as a strongest result: *"`d ln B/dt = d ln b/dt + d ln A/dt`, with `d ln b/dt` bounded
(technology saturates) and `d ln A/dt` **unboundedly negative** under the stock-liquidation cycle ⇒ the illusion
is necessarily transient."* This is a **one-stock** statement. Under scope-A (two-land conversion) it does
**not** transfer: the aggregate `B` can keep rising (cropland/yield gain) while `A_c` falls, so the illusion is
**potentially long-lived** (hypothesis to be demonstrated — see J2; grok: window closes only when soil debt or the
arable ceiling binds — decades). **In the plan, state explicitly: the one-stock "necessarily transient" proof is
the didactic limit (`S = 0`); under conversion the illusion is *potentially* long-lived, and the honest claim is
the composition-change one (§ Part C row "NFA series").**

### I3. The χ Hopf "which single delay destabilises" classification is ORIGINAL-MODEL-only

The master Part 1's other strongest result (χ = q/(ρ−2q) ⇒ τ_m-only vs τ_p-only Hopf, exact sign structure,
Scenario B τ_m ≈ 85.4 yr, ρ=1.6 → τ_p ≈ 231 yr) is the **original** model's classification. The master Part
11.6 already flags **"the χ/Hopf classification does not transfer to the corrected S0."** Under scope-A (corrected
S0, two-land) do **not** carry it; place it under "what the model is **not** claiming." Keep the sign-rule
correction (Λ > 0 ⇒ τ_m-only) recorded only as the original-model result.

### I4. Registered baseline parameter set (pin the honest numbers; add the two-land set)

From `model_sims/models.py` the authoritative baseline is `ρ = 0.05 yr⁻¹` (note: `corrected_s0_summary` uses
`ρ = 0.08` — reconcile which is baseline), `A_max = 1.2`, `b₀ = 0.5`, `b_G = 0.8` (⇒ **`V = b_G/b₀ = 1.6 yr`**,
confirming the honest baseline), `e = 0.55`, `r = 0.02`, `η = 0.05`, `α = 0.03`. The plan's §2.1 parameter table
must start from these and add the two-land constants `ρ_c, A_c,max, b_f, b_c, b_G,c, σ_f, σ_c, κ (= b_f), η_f,
L_c, H_c, κ_w`. Use `char_eq.py` defaults to keep the S0 results reproducible.

### I5. The deepest cause (master RC1) — how scope-A fixes it

Part 1's root cause: *"the ontology of the environmental stock was never fixed, which makes the headline
decomposition `B = b·M` non-identifiable and leaves a depletion term that mis-books biocapacity and depletion in
two different 'books'."* **scope-A fixes this directly:** `A_f` and `A_c` are physical hectares (identifiable
decomposition), `B = b_f A_f + b_c A_c + b_G,c G_c(A_c)` uses one book, and the conversion `S/κ` is the
booking operator. State this as the deepest-cause resolution in the plan's opening.

### I6. Re-confirm `t₅₀ ≈ 7.1/ρ` (the v18 FAQ text is the blunder)

v18 §13(8)(vi) states "t50 ≈ 145/ρ" but its own table gives t50·ρ ≈ 4.9–6.7 (i.e. t50 ≈ 5–7/ρ). F4's corrected
`t₅₀ ≈ 7.1/ρ` is right. **Carry into v33:** fix §13(8)(vi) and Prediction 7 to `t₅₀ ≈ 7.1/ρ`.

---

## Part J — GPT consolidation-plan items now adopted (from `JOINT_EVALUATION_of_gpt_consolidation_plan.md`)

These come directly from GPT's plan and are **verified** (or are sound hygiene); they are now binding on v33:

- **Restoration flows (recovery is not reversible):** an explicit restoration pathway
  `R_fc = χ A_f Φ(B−E)` (`A_f→A_c`) and/or `R_rc = ρ_r A_r Ψ(restoration)` (`A_r→A_c`), added to `Ȧ_c, Ȧ_f, Ȧ_r`
  consistently. Without these, "recovery" means only *cessation of loss / debt repayment / demographic
  adjustment* — state which meaning is used.
- **Typed floors via complementarity/active-set (not one symbol):** reserve `A_r ≥ A_r^min`, capital viability
  `A_c ≥ A_c^min`, arable ceiling `A_f ≤ A_f^max`, carrying-capacity `K ≥ K_min`, optional `D ≤ D_max`; the
  conversion `u_c` saturates at `A_r ≤ A_r^min` or `A_c ≤ A_c^min` (`0 ≤ u_c ≤ S/κ`).
- **Hysteresis taxonomy (demonstrate, not assume):** distinguish dynamic-lag (τ_g/τ_p) / path-dependence
  (irreversible conversion) / active-set / bistable; report `ΔA_c, ΔA_f, ΔA_r, ΔD, ΔP` after the forcing returns.
- **Bifurcation classification:** fold vs Hopf vs border-collision vs constraint-activation vs rate-induced
  tipping vs one-way-irreversible loss vs numerical termination; only the first is a "fold."
- **Parameter identification:** `b_c, b_G,c, ρ_c` not identifiable from a single `Y_c` cross-section; `α` and `D`
  confounded; give proxies (cropland/managed pasture/built, mature forest/wetland/high-C soil, unallocated/
  degraded/restoration) + a sensitivity study. Reproducibility spec (§ parameter table, history functions,
  solver, tolerances, κ fixed vs `b_f(t)`, `L_c` on/off, restoration on/off, floors).
- **The reformulated central result (adopt verbatim):** *"Aggregate biocapacity can rise while slow ecological
  capital is being converted into faster provisioning land. Whether this produces transient growth, instability,
  overshoot, or irreversible loss depends on land-productivity contrasts, regeneration and demographic delays,
  debt feedbacks, retirement and restoration pathways, and binding land constraints."* This **replaces** the
  legacy "universal `+0.625`" / "universal delay cliff" as the headline.

---

### J2. Cross-check sweep — the remaining GPT items, now made explicit

- **Epistemics (GPT §9) — the illusion claim is a HYPOTHESIS, not a theorem.** State "the illusion is
  generic and historically long" as a **hypothesis to be demonstrated numerically/empirically**, not an algebraic
  theorem. Enumerate the four-stage ladder explicitly:
  (1) **illusion onset** `Ȧ_c<0, Ḃ>0`; (2) **illusion duration** (time until `Ḃ≤0`, or the arable ceiling binds,
  or debt degradation dominates, or a typed floor activates); (3) **masking state** `R_B<1` while `Ȧ_c<0`;
  (4) **conversion crisis** (loss of `A_c` viability / floor activation).
- **Non-negativity & forward invariance (GPT §15).** Admissible set
  `Ω = {A_f,A_c,A_r,P,D ≥ 0; A_f+A_c+A_r=A_tot}`; show trajectories stay in `Ω`. Guard against: `A_c<0` under
  unrestricted conversion; `A_f` exceeding available land; delayed regeneration positive after `A_c=0`; `D<0` from
  numerics; `K` undefined if `B≤0`; `P` overshooting a collapsing delayed `K`. Implementation: event detection at
  land boundaries, non-negativity enforcement, constrained conversion rate, explicit delay-history functions,
  active-set logging, step-size/tolerance convergence checks. **Delayed-regeneration-at-extinction caveat:** if
  `A_c(t)=0` but `A_c(t−τ_g)>0`, recruitment may still arrive — physically fine only if it represents maturing
  cohorts; if it represents current ecological growth, revise the delayed formulation.
- **Active-set enumeration (GPT §10/§13) — all five, not a subset:** derive `det Δ(λ)=0` and seek folds separately
  for (1) no conversion `S=0`; (2) active conversion `S>0`; (3) active timber liquidation `L_c>0`; (4) boundary
  states where the positive-part function is **nonsmooth**; (5) carrying-capacity floor active `K=K_min`.
- **Verification suite (GPT §19) — report each:** land conservation `A_f+A_c+A_r=A_tot`; non-negativity; debt
  balance; convergence under step refinement; agreement between direct simulation and equilibrium continuation;
  recovery of the ODE limit as `τ_g,τ_p→0`; recovery of the no-debt limit as `α→0` (or `D→0`).
- **Sensitivity design (GPT §20):** structured/global sweeps over
  `ρ_c, b_f, b_c, b_G,c, κ, η_f, η, α, r, τ_g, τ_p, A_r^min, A_c^min`; report min `A_c`, max `A_f`,
  time-to-conversion-onset, illusion duration, peak `B`, peak `D`, population overshoot, floor-activation
  probability/occurrence, recovery fraction `R_c`, dominant root. **A local table alone is insufficient near
  active-set transitions** — use Latin-hypercube / Sobol / continuation as appropriate.
- **Retire list (GPT §24) — make the "what we are NOT claiming" block explicit** (add to Part C/N1 block):
  (i) **equivalence `R_B>1 ⟺ capital-land decline` does not hold** along delayed trajectories — the true
  stock-decline condition is `Ṡ/κ + L_c > G_c(A_c(t−τ_g))`; (ii) **a single scalar stock is not physically
  identifiable.** Plus the already-recorded retirements (universal zero-det, universal `+0.625`, universal
  20-yr delay, `V_crit=1/ρ_c` identity, automatic `P=B/e` preservation, unexplained `ψ_c=1/2`).
- **Architecture — DECIDED (minimal-edit path; reorg deferred).** GPT proposes a 12-section reorg and 9 appendices
  (Appendix G: one-stock comparator, C: equilibria by active set, D: Jacobian/determinant, I: continuation
  diagrams). **Decision: use the minimal-edit path — keep Part E's existing §-map** (edit in place per §, do not
  renumber/reorganise the manuscript now). The architectural reorg is **deferred**; revisit after the content is
  correct. The *content* items above are mandatory either way.

---

## Next step

I have **not** edited any manuscript or created v33. On your confirmation I will (1) resolve Part G open
questions **and** the GPT-flagged derivations (per-active-set equilibria, 4×4 delayed Jacobian, capacity-max
ratio boundary, restoration flows) with verified numerics, (2) produce `manuscript_ECOMOD_v33.tex` + the
supporting `data/revisions/` note, and (3) present the compiled PDF for your review. Confirm, or tell me which
Part(s) to adjust first.

*Read-only plan; all parameters and the conversion gain verified. No manuscript modified. Superseding
corrections applied per `JOINT_EVALUATION_of_gpt_consolidation_plan.md` (GPT plan verified).*
