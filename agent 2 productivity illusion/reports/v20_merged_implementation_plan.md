# Merged Implementation Plan — Lens‑1/‑4 (macros & bookkeeping) × AI corrected top‑down → v20

**Purpose.** Merge our **Lens‑1 (macro "safe operating space" in observable ratios)** and **Lens‑4
(whole‑system invariants / bookkeeping closure)** with the **AI's complete, corrected top‑down analysis**
into one coherent manuscript implementation plan. Every finding below is **verified** against the
committed code (`model_sims/corrected.py`, `char_eq.py`, `topdown.py`, `r1_basin.py`) and recorded in
`data/topdown_results.json`. **This is a plan document only — no mint, no push, no manuscript edit has
been made.**

**Baseline (corrected S0, deficit region `E>bA`):** `ρ=0.05, A_max=1.2, b=0.5, b_G=0.8, e=0.55, r=0.02,
A_ext=0.02`; `G(A)=ρA(1−A/A_max)`, `B=bA+b_G G(A)`, `K=B/e`; `R_B=E/B`, `R_A=E/(bA)`, `ψ=bA/B`.

---

## 1. The unifying spine

The two strands **converge on a single object**:

> **The operating boundary is `R_B = 1` (footprint = total biocapacity), which is exactly the neutral
> equilibrium family `P = B(A)/e`.** This is simultaneously:
> - the **bookkeeping** balance point (Lens 4): `dA/dt<0 ⟺ E>B̃` (`B̃=bA+b_G G(A(t−τ_g))`), so `R_B=1` is the decline trigger;
> - the **macro‑ratio** safe‑operating‑space boundary (Lens 1): `R_A = R_B/ψ`; `R_A>1` is a leading but non‑causal signal;
> - the **basin separator** (AI A2): the neutral family, balanced‑accuracy 99% (no/short delay) → 81% (τ_g=30).

Everything below is a facet of this spine. This gives the merged v20 a single, policy‑readable headline.

**C7 — the headline.** Framed in one sentence:

> *"The balance point is `R_B = 1` (footprint = biocapacity = the neutral family = the `§4.2` fold
> threshold); the flow‑yield ratio `R_A` is a **leading, non‑causal** signal whose lead grows with the
> flow‑share separation `1/ψ`; and once the regeneration lag is too long **neither** ratio forecasts
> collapse (silent collapse, measure‑zero rescue set) — the **lag**, not the ratio, is the controlling
> variable."*

**C2 — `R_B=1` is the coordinate‑free common fixed point.** The Lens‑4 bookkeeping trigger (`dA/dt<0⟺E>B`),
the Lens‑1 operating boundary (`R_B=1`), the AI neutral‑family separator (`P=B(A)/e`), and the `§4.2` saddle‑node
fold threshold all express the **same relation `E = B`** in different coordinates. Therefore the balance‑point
reading (`R_B=1`) and the basin‑separator reading (the family `P=B(A)/e`) are **one statement, not two**.
(Verified: at the `§4.2` fold threshold `E=B_max`, `R_B=E_sn/B_max = 1.000` exactly — see C4.)

## 2. One object, seven strengthened connections (C1–C7)

> **Naming note.** Here **C1–C7** are the **connection** labels from the gap‑analysis
> (`reports/v20_merged_plan_gap_and_connections.md`). They are **distinct** from the AI framework's own
> section labels **`AI‑A1…A7`**, **`AI‑C4`** (rescue set) and **`AI‑C6`** (asymptotic map); in this plan the
> AI sections are always written with the `AI‑` prefix.

The refinements **R1–R6** (§3–§6, §10) are precision/honesty edits applied in place. The following
**C1–C7** tighten the relationship between the **Lens** (macros & bookkeeping) and the **AI top‑down** so
they read as one argument.

- **C1 — `ψ` (flow share) is the master parameter.** The single knob `ψ=bA/B` (equivalently the regime
  index `b_Gρ/b`) locates: the **fold/MSY regime boundary** (`b_Gρ⋚b`, i.e. `ψ*=2/(1+b_Gρ/b)⋚1`); the
  **masking‑illusion visibility** (prediction #5, strongest when `ψ→1`, flow‑dominated); the **macro‑ratio
  separation** `R_A=R_B/ψ`; and the **sustainable `R_A>1` operating point**. Verified across regimes:
  `b_Gρ/b = 0.05` (flow‑dominated, no interior MSY, `ψ→1`, `R_A=1`); `2.0 → ψ*=0.667, R_A^eq=1.50`;
  `37.5 → ψ*=0.052, R_A^eq=19.25`; `150 → ψ*=0.013, R_A^eq=75.5` (`ψ*=1/R_A^eq=2/(1+b_Gρ/b)`). → State in
  §4.5: *"the flow share `ψ` is the master parameter — it locates the regime, the masking, and the
  macro‑ratio separation from one closed form."*
- **C2 — coordinate‑free common fixed point** (as in §1; the balance point = separator = fold threshold).
- **C3 — two sides of one coin.** `R_B=1` is **necessary** for recovery but **not sufficient** once the
  regeneration lag is too long: at short lag the Lens macro‑ratio boundary is exactly the AI basin
  separator (balanced **99%**); at long lag it degrades (balanced **81%**) and `R_B<1` no longer guarantees
  recovery — the AI's basin‑boundary crisis / no‑CSD (AI‑A5, AI‑C6). *"The operating boundary (Lens) and the
  basin crisis (AI) are complementary statements about one object."*
- **C4 — fold ↔ `R_B=1` two‑way linkage (`§4.2` ↔ `§4.5`).** The `§4.2` interior‑MSY fold threshold
  `E_sn = A_max(b+b_Gρ)²/(4b_Gρ)` is the `R_B=1` boundary evaluated at `(A*, E=B_max)`; conversely the macro
  ratios give the fold a "balance‑point" reading. **Verified** (increment‑dominated `b=0.02`): interior MSY
  `A* = A_max(b+b_Gρ)/(2b_Gρ) = 0.900`, `B(A*)=B_max=0.0270`, `E_sn=0.0270`, `R_B = E_sn/B_max = 1.000` exactly.
  → **Regime‑scoped**: this fold exists only when `b_Gρ>b`; do **not** re‑assert a baseline fold.
- **C5 — dimensionless‑group scoping.** The AI A1 refutation of `τ_g/τ_p` scaling interacts with §4.4's
  "complete dimensionless group set": the **operative group is `b_Gρ/b`** (regime), **not `τ_g/τ_p`**
  (lag ratio). One sentence in §4.4/§8.
- **C6 — one canonical metric.** Use **balanced accuracy** (optionally precision/recall) for *both* the Lens
  **silent‑collapse** claim *and* the AI **separator** claim, so the honesty argument is uniform; **never**
  report raw accuracy on the long‑lag basin (class‑imbalance trap).
- **C7 — headline** (as in §1).

## 3. Mapped findings → manuscript locations

| # | Finding (verified) | Strand | Manuscript home | Action |
|---|---|---|---|---|
| F1 | Exact identity `dA/dt=(B̃−E)/b_G` in deficit region; `dA/dt<0⟺E>B̃` | Lens 4 | §4.3 (extend the existing deficit identity) | Add the lag‑adjusted `B̃` note + one corollary |
| F2 | Typed‑ vs‑aggregate floor gap as exact identity (stock `A` can fall while aggregate `B` floor holds) | Lens 4 | §10 / §13 | **Framing (R1), not a new computation** — leverages the existing typed‑ledger point (P3). One sentence + the exact condition `B=bA+b_G G(A)` substitution buffer |
| F3 | `R_B=1` is the trigger; `R_A=1` is necessary‑but‑not‑sufficient (leading, non‑causal) | Lens 1 | **new §4.5** | Subsection + the onset table (`R_B=1.000`, `R_A=1.01–1.06`) |
| F4 | `R_A = R_B/ψ`; closed form at interior MSY `ψ*=2/(1+b_Gρ/b)`, `R_A^eq=(1+b_Gρ/b)/2` | Lens 1 | **new §4.5** + §4.4 | Closed form + regime‑scoped (flow‑dominated `R_A=R_B=1`) |
| F5 | Sustainable state runs at `R_B=1` with `R_A>1` (footprint > flow‑yield) in increment‑dominated systems | Lens 1 | §4.5 | `R_A>1` is **not** a warning; the buffer is normal |
| F6 | **Silent collapse**: at τ_g=30, 37% of collapses begin with `R_B<1` AND `R_A<1` | Lens 1 | §13(9) extension | Neither ratio forecasts a long‑lag collapse; shorten the lag |
| F7 | τ_g‑driven cliff, **τ_p‑independent** (τ_g=18 yr for every τ_p; no dimensionless `τ_g/τ_p`) | AI A1 | §8 + §13(9) | One sentence + figure; preempts the τ_p‑scaling reviewer |
| F8 | Neutral‑family separator & its degradation (99%→81% balanced; linear functional = chance) | AI A2 | §4.5 / §13 | **Re‑frame/strengthen R2 (R5), not a new advance.** State `R_B=1` is the separator; do NOT call it a first integral; **report balanced accuracy (R4)** |
| F9 | Recovery‑overshoot scaling: real, IC‑dependent, steep (α≈4.8); no single `τ_g` law | AI A3 | §13(8)(vii) | Qualify the existing overshoot note |
| F10 | Rescue set collapses 40% → measure‑zero strip at `A_max` for τ_g≳20 (domain‑wide collapse) | AI‑C4 | §13(9) | Quantify; policy‑relevant (cannot rescue by starting higher) |
| F11 | No Hopf across the whole `(τ_g,τ_p)` plane (0 crossings; `Re λ≈+0.625` constant) | AI‑A5 | §8 / §13(9) | **The new bit is full‑delay‑plane coverage (R6).** One‑line confirmation of "monotone‑only" |
| F12 | Asymptotic map fixed points = family, but local λ constant → cliff is **nonlocal** | AI‑C6 | §13(9) | The `τ_g` transition is a basin‑boundary crisis, not a map bifurcation (reinforces no‑CSD) |
| F13 | Corrected Lin‑code (right matrices, left null vector, `R_B=1` separator, balanced accuracy) | AI Part B | Appendix / reproducibility | Provide `topdown.py` as the reproducible module |

**Everything belongs around the `R_B=1` spine**, and F1–F5 are the headline (macro‑ratio safe operating
space); F6–F12 are supporting/strengthening content already implied by v19's §13(9).

**Exact verified record to embed (R2).** Onset: `A₀∈{0.30,…,1.05} → R_B=1.000, R_A=1.01–1.06`. Regime
separation closed form: `RAeq = 1.0` (index `b_Gρ/b ≤ 1`, flow‑dominated), `(1+b_Gρ/b)/2` for
increment‑dominated (e.g. index 6 → 3.5, 12 → 6.5). Silent collapse: τ_g=10 → #R=83/#C=125, silent=2 (1.6%);
τ_g=30 → #R=11/#C=197, silent=72 (36.5%). Rescue set: recover fraction **39.9/39.9/39.4%** at τ_g=0/10/18,
then **5.3%** at τ_g=20/30/40; A‑span **0.100–1.300 (13 A)** at τ_g≤18 → **1.200–1.200 (1 A)** at τ_g≥20
(measure‑zero strip at `A_max`). Separator balanced accuracy: **99.0/99.2%** (no‑delay) → **64.4/81.2%**
(τ_g=30); linear functional 96.2/96.4% → 94.7/50.0% (τ_g=30, chance). Hopf: `n_crossing_points=0`,
`Re λ≈+0.625` constant. **AI‑C6** map fixed points: `E=0.15→0.283, 0.3→0.576, 0.5→0.986, A_max=1.2`; `Re λ_max`
`+0.5917→+0.6249→+0.6250`, no flip.

## 4. Part 1 — Lens‑4 bookkeeping/invariants (the foundation) → §4.3

- **Extend the existing deficit identity** (currently `dA/dt = (B−E)/b_G`) to the exact lag‑adjusted form:
  `dA/dt = (B̃ − E)/b_G`, `B̃ = bA + b_G G(A(t−τ_g))`. *Minor bookkeeping correction*: the identity is exact
  only if `B` uses the **delayed** regeneration; state this.
- **Corollary:** `dA/dt<0 ⟺ E>B̃`; at equilibrium `E=B̃` (so `R_B=1`).
- **Typed‑vs‑aggregate floor gap as an identity:** `B = bA + b_G G(A)`, so the aggregate floor on `B` can
  hold while the typed floor on `A` is violated, and the gap is exactly the substitution buffer
  `b_G G(A)`. State the condition for the gap to open/close. **Framing note (R1):** this is a re‑statement
  of the existing §10/§13 typed‑ledger point (P3) — frame as **leverage**, not as a new computation; only
  the buffer condition `B=bA+b_G G(A)` is added.

## 5. Part 2 — Lens‑1 macro safe operating space → **new §4.5**

Add a subsection "Macro‑ratio safe operating space (`R_B` vs `R_A`)" after §4.4:
- Definitions `R_B=E/B`, `R_A=E/(bA)`; relation `R_A=R_B/ψ`, `ψ=bA/B`.
- **The trigger is `R_B=1`**, verified: onset table `A₀∈{0.30,…,1.05} → R_B=1.000, R_A=1.01–1.06`.
- **`R_A=1` is necessary but not sufficient**; between `R_A=1` and `R_B=1` the stock still regenerates.
- **Temporal‑lead nuance (R3):** `R_A`'s lead over `R_B` is **≈0 in flow‑dominated systems**, and grows
  only with increment‑dominance (the separation `1/ψ`) — so a larger lead is a *signature* of the
  increment‑dominated regime, not a general warning property.
- **Regime‑scoped closed form:** interior MSY → `ψ*=2/(1+b_Gρ/b)`, `R_A^eq=(1+b_Gρ/b)/2`; flow‑dominated
  (baseline) → no interior MSY, `R_A=R_B=1` at the boundary `A_max`.
- **`ψ` is the master parameter (C1):** it locates the regime, the masking (prediction #5), and the
  macro‑ratio separation from one closed form — state this explicitly.
- **Fold ↔ `R_B=1` (C4):** the `§4.2` interior‑MSY fold threshold is `R_B=1` evaluated at `(A*,E=B_max)`
  (`R_B=E_sn/B_max=1.000`, verified at `b=0.02`); **regime‑scoped** (only when `b_Gρ>b`).
- **Consequence:** a sustainable increment‑dominated system runs at `R_A>1` (`R_A>1` is normal, not a
  warning); the balance point is `R_B=1`.
- **Figures:** `scans/topdown_macro_ratios.png` (two‑panel basin), `scans/topdown_ratio_separation.png`.

## 6. Part 3 — AI's corrected top‑down, placed

- **A1 (F7) → §8** one sentence + `scans/topdown_delay_boundary.png`; **§13(9)** to restate the
  τ_p‑independence with the extreme‑lag re‑opening caveat. **C5:** pair with §4.4's dimensionless‑group
  sentence — the *operative* group is `b_Gρ/b`, not `τ_g/τ_p`.
- **A2 (F8) → §4.5/§13**: the separator is `R_B=1`, the balanced‑accuracy 99%→81% table; explicitly *not*
  a "first integral"; a linear functional is chance (balanced 50%) at τ_g=30. **R5:** frame as
  **re‑frame/strengthen** R2, not a new analytic advance. **R4:** report by **balanced accuracy**, never
  raw accuracy on the long‑lag basin.
- **A3 (F9) → §13(8)(vii)** qualify the overshoot note (IC‑dependent, steep α≈4.8).
- **C4 (AI‑C4, F10) → §13(9)** quantify the rescue set (40% → measure‑zero strip; "cannot rescue by starting
  higher, must shorten the lag").
- **A5 (AI‑A5, F11) → §8 one line**: no Hopf across the whole delay plane (monotone‑only). **R6:** the *new*
  part is **full‑delay‑plane** coverage; single‑delay no‑Hopf was already R2.
- **AI‑C6 (F12) → §13(9)**: the asymptotic map reproduces the fixed points but **not** the cliff → the
  transition is **nonlocal** (basin‑boundary crisis, no CSD). (This is the AI's `C6` map section — distinct
  from the *connection* label **C6** = canonical‑metric rule in §2.)
- **B (F13) → Appendix/reproducibility**: the corrected `topdown.py` + `_run_topdown.py` +
  `data/topdown_results.json` as the reproducible companion.

## 7. Figure plan (`scans/`)
- `topdown_macro_ratios.png` — two‑panel baseline basin in the macro‑ratio plane (τ_g=10 vs 30). [new]
- `topdown_ratio_separation.png` — flow‑share separation closed form. [new]
- `topdown_delay_boundary.png` — τ_g‑driven cliff (τ_p‑independent). [new]
- Update the "Accompanying files" list in the manuscript to add these three.

## 8. Falsifiable‑prediction & abstract updates (careful, minimal)
- Add **prediction #8**: "On the corrected S0 the *operating* boundary is `R_B = 1` (footprint = total
  biocapacity); the flow‑yield ratio `R_A` crosses 1 earlier but is not the collapse trigger, so a system
  can be on the collapse side while `R_A>1` and even while `R_B<1` in the long‑lag regime (silent
  collapse)." → this is falsifiable via the basin/field data.
- **Abstract count → eight** (currently "seven predictions"). Verify and reconcile.

## 9. Sections to touch (index)
| Section | Edit |
|---|---|
| §4.3 | extend deficit identity to `B̃`; add the typed‑vs‑aggregate gap identity (framed as leverage, R1) |
| §4.5 (new) | macro‑ratio safe operating space (`R_B` vs `R_A`), closed form, `ψ` master parameter (C1), temporal‑lead nuance (R3), fold↔`R_B=1` link (C4), figures |
| §6 | new prediction #8 (→ abstract count eight) |
| §8 | τ_p‑independence one‑liner (A1) + **operative group `b_Gρ/b` not `τ_g/τ_p` (C5)** + no‑Hopf full‑plane (A5) + figure refs |
| §13(9) | extend: silent collapse %, rescue‑set measure‑zero, nonlocal‑cliff (C6), separator degradation (A2, **balanced accuracy R4**), overshoot qualifier (A3) |
| "Accompanying files" | add the three `topdown_*` figures + `topdown_results.json` |
| Appendix / reproducibility | the corrected `topdown.py` module |

## 10. Verification / QC (before any push)
- `scan`: no new coverage gap (expect 21 covered / 1 superseded 12A.1).
- `eval`: Recall@1 ≥0.82, R@3 ≥0.95 (single `12B.6` miss, unchanged).
- `pytest`: 34 passed (live symlink `data/IMPLEMENTED_revision_ECOMOD.md` must exist → restored to v19).
- All referenced `.png` resolve; §13 numbering stays clean; abstract count reconciled to eight.
- **Metric rule (R4):** confirm no raw accuracy is ever quoted on the long‑lag basin; all separator and
  silent‑collapse numbers are reported as **balanced accuracy** (or precision/recall).
- **Exact‑values check (R2):** confirm the onset / rescue‑set / silent‑collapse / separator numbers in
  §3 match `data/topdown_results.json` verbatim.
- Confirm the "run it: `PYTHONPATH=. python -m model_sims._run_topdown`" is reproducible.

## 11. Future work & conjectures — **NOT** included as verified findings

Everything below is **out of scope for the v20 revision** and is labelled clearly as **conjecture** or
**future work** so it is never mistaken for a verified result.

- **Rigorous comparison theorem (Kuang‑style) — *conjecture*, not a proof.** Research‑level. We state only
  the *numerically‑verified* rescue‑set fact (F10) and label the broader theorem a **conjecture supported
  numerically**; **we do not claim a proof.**
- **Option‑2 (growth‑accounting decomposition) — *future work*.** Deferred as previously directed.
- **Option‑3 (coarse‑grain 1‑D reduction) — *future work*.** Deferred as previously directed.
- **Model changes (Allee / stochasticity / seasonal forcing) — *future work*.** Directions only; no changes
  to the corrected S0 model are made this revision.
- **Keep the regime‑scoped E‑fold/CSD correction from v19** (this is a *correctness fix*, not out‑of‑scope):
  do **not** re‑assert a baseline fold; the fold is interior‑MSY‑only (`b_Gρ>b`).

## 12. Standing constraints honoured
- No over‑adding; only substantive, verified, grounded additions (all above are verified).
- No over‑claiming (corrected the AI's "100%/94%" first‑integral claim; regime‑scoped the fold/CSD; the
  comparison "theorem" is labelled a conjecture supported numerically; A2/F5 framed as re‑framings R5).
- Out‑of‑scope items are presented as **conjectures or future work** (§11), never as verified results.
- "Don't implement this turn" respected — this is a **plan**, not a revision.

## 13. Status & next step
The merged content is **fully analyzed, verified, and tightened** (refinements R1–R6 + connections C1–C7
applied). This plan is ready to be **implemented as v20** (mint → verify → push as `MIKEAA2020`) **if you
approve the wording**. No mint/push has been made.

---
**Files that make this concrete:** `reports/v20_topdown_macro_ratios.md` (Lens‑1/‑4 detail),
`reports/v20_corrected_topdown_framework.md` (AI corrected analysis, Parts A–E),
`reports/v20_review_adjoint_code.md`, `reports/v20_evaluation_of_ai_topdown.md`,
`reports/v20_merged_plan_gap_and_connections.md` (the standalone gap/connections analysis);
code `model_sims/topdown.py`, `model_sims/_run_topdown.py`, `data/topdown_results.json`;
figures `scans/topdown_macro_ratios.png`, `scans/topdown_ratio_separation.png`,
`scans/topdown_delay_boundary.png`.
