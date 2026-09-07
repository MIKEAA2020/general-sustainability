# Honest Outcome of Option (b) — what the recompute actually shows

I implemented the root-cause choice (physical `b_G = b·V`) and re-derived the ground truth using the
registered model code. This memo states **what survives**, **what changes**, and **what no longer holds**,
verifiably. It does not hide the fact that option (b) materially weakens the manuscript's central quantitative
claim.

The governing identity, now correct: `V = b_G·A/(b·A) = b_G/b`, so **`1/V = b/b_G`** (turnover rate, `yr⁻¹`),
and `γ = 1/b_G` (harvest/conversion coefficient, `ha·gha⁻¹`) are **distinct** — the manuscript's
`γ = 1/b_G = 1/V` conflates them. With `A` stated in physical hectares (md line 151), `b_G` is physical and
`b_G = b·V` is mandatory. Baseline `b_G = 0.8, b = 0.5` ⟹ `V = 1.6 yr` (a fast crop), **not** 20–100 yr.

---

## 1. What SURVIVES (regime-independent — verified)

These are the paper's genuine, robust contributions and they are **unaffected** by the `b_G` correction:

- **Emergent carrying capacity** `K = B/e` (not imposed).
- **Deficit-driven accounting** `dA/dt = G(A(t−τ_g)) − [E − σbA]₊/b_G`: only the shortfall above the flow yield
  liquidates stock.
- **The one-parameter equilibrium family** `P = B(A)/e` (neutral continuum) — I verified `dA/dt = 0` and
  `dP/dt = 0` hold on it for **any** `b_G` and **any** regime. (Note: persists; only the stability of the
  transverse mode changes.)
- **`R_B = 1` is the balance point / neutral continuum**, and `R_A = 1` is a leading but non-causal signal
  (structure).
- **The `τ_g` recover-vs-collapse cliff (Prediction 6).** Coarse-grid probe at `τ_p = 0` (6×8, dt 0.5, T 600):
  the recover fraction falls through the cliff at `τ_g ≈ 18–20` for **every** `b_G` tested (`0.417 → 0.375 →
  0.229 → 0.104` at `τ_g = 10/18/19/20/30`, identical across `V = 1.6…50`). So the cliff is **not** an artifact
  of the invalid `b_G`; it survives. *(To be re-confirmed at the manuscript's `τ_p = 25` and full grid before it
  is re-printed, but the structure is real.)*

## 2. What CHANGES (verified)

- **The regime flips.** Regime index `b_G·ρ ⋚ b` ⟺ `V·ρ ⋚ 1` ⟺ `V ⋚ 20 yr`. For any forest/soil turnover
  `V > 20 yr` the model is **capital-dominated** (`b_G·ρ > b`): `B(A)` has an **interior maximum (MSY)**, a
  **fold/saddle-node is realised**, and the stable object is an **interior `A* < A_max`**, not the boundary
  `A_max`. The "orchard / flow-dominated / `ψ → 1`" framing the manuscript uses everywhere **does not apply** to
  forests, soils, and most fisheries. The operative picture at ecological scale is the **Scheffer/fold regime**,
  not the orchard.
- **The steady-state structure changes** from "boundary `A_max`" to "interior `A*`, fold at `E = B_max`."

## 3. What NO LONGER HOLDS (verified — this is the honest finding)

- **The headline "monotone instability / positive real eigenvalue for every delay" (the vicious cycle) is NOT
  robust to physical `b_G`.** At the manuscript's baseline `b_G = 0.8` the transverse root is `+0.62`
  (timescale ≈ 1.6 yr). Under physical `b_G = b·V`:

  | `V` (yr) | `b_G` | regime | transverse root | timescale |
  |---:|---:|---:|---:|---:|
  | 1.6 (baseline) | 0.8 | flow-dom | **+0.62** | ~1.6 yr |
  | 10 | 5.0 | flow-dom | +0.098 | ~10 yr |
  | 20 | 10.0 | marginal | +0.041 | ~24 yr |
  | 27 | 13.5 | capital-dom | +0.024 | ~42 yr |
  | 40 | 20 | capital-dom | +0.0035 | ~290 yr |
  | **50** | 25 | capital-dom | **none** (only `s = 0` continuum) | — |
  | **100** | 50 | capital-dom | **none** | — |

  I discriminated the `s = 0` continuum root from a genuine transverse root: scanning only `s > 0.05`, there is
  **no** positive real eigenvalue for `V ≥ 50` (the only root is the neutral `s = 0` from the continuum). So at
  physical **old-growth turnover the system is no longer monotonically unstable** — the "structural vicious
  cycle" is a **flow-dominated / fast-turnover** phenomenon.
- **The sufficiency condition I wrote in v31/v32 is wrong.** The correct condition for a positive real root
  (given `D(0) = 0`, `D(s) → +∞` on the real axis) is **`D′(0) < 0`**, not `S > r`. `S > r` is sufficient but
  not necessary — at `V = 30`, `S − r = −0.003` yet a positive root exists because `D′(0) = −0.015 < 0`. This
  must be corrected everywhere the claim is stated (abstract, §4.3, §5, §6, §8, SI §S3.4).
- **The manuscript's `γ = 1/b_G = 1/V` is wrong** (see top); it must be corrected to `γ = 1/b_G` (harvest
  coefficient) and `1/V = b/b_G` (turnover rate).

## 4. What was NOT reliably re-derived (I will not over-state)

- The **masking-window width** (the paper's title result, `≈5.4 yr`). My probe of the reduced masking model was
  unreliable (it returned 0 even at baseline where the manuscript documents 5.4 yr), so I make **no** claim about
  whether the mask survives at physical `b_G`. It needs a proper re-derivation with the registered `demo` driver.
- The **full recover-fraction basin** at `τ_p = 25` and the masking/cliff **numbers** need re-computation on the
  documented grid at physical `b_G`. The coarse structure suggests the cliff survives; the magnitudes are not yet
  re-established.

---

## The honest bottom line

Under option (b), the paper's **central quantitative claim — a structural, delay-independent "vicious cycle"
(`Re λ ≈ +0.62`) — is specific to the fast-turnover `b_G = 0.8` baseline and does not hold at physical
forest/soil turnover** (`V ≳ 50` yr). The paper's **robust** contributions (emergent `K`, deficit accounting,
the `P = B(A)/e` family, the `R_B=1`/`R_A=1` split, and the `τ_g` delay cliff) **all survive**. So (b) does not
"kill" the paper; it **moves it** from a "structural vicious cycle" headline to a **regime-and-parameter
framing** in which the instability is a fast-turnover fact and the forest-scale picture is the fold/MSY +
delay-cliff (Scheffer) regime.

## The one decision that determines the v33 re-scoping (B1 vs B2)

There are two honest, internally-consistent ways to present the forced change, and they require different
rewrites. Please pick:

- **B1 — Re-scope to the capital-dominated (forest/soil) regime.** Adopt a physical `b_G` (state `V ≈ 30–50 yr`,
  e.g. `b_G ≈ 15–25`), present the model as **capital-dominated** with an interior MSY and a realised fold, and
  make the **fold + delay-cliff** the operative collapse mechanism. The "positive real eigenvalue for every
  delay / vicious cycle" is then **dropped or re-scoped to the fast-turnover limit**, and the abstract, title
  suggestion, §4.3, §5, §6, §8, §12 and the comparison table are rewritten to that framing. This is the most
  honest to the ecological subject and keeps the title's "productivity illusion."
- **B2 — Keep `b_G = 0.8` as a deliberately fast-turnover (crop/orchard) stylised system, and **disclaim** the
  `V = 20–100 yr` ecological anchoring.** i.e. drop the "forest/soil/fishery" framing and the `1/V` identification
  entirely; present the instability as a property of fast-turnover systems and the orchard as the literal
  subject, not a metaphor for forests. Smaller rewrite; keeps the `+0.62` result, at the cost of the ecological
  motivation.

Both are honest. B1 is the more faithful execution of "address the root cause" (it re-derives at physical scale),
but it is a large rewrite and it re-frames the paper's headline downward. B2 is smaller but keeps a model whose
subject is a 1.6-yr crop.

**I recommend B1** if the paper's purpose is to say something about real forests/soils/fisheries; **B2** if it
is specifically an orchard/flow accounting model. Tell me which, and I will produce v33 (new revision, error-free
LuaLaTeX + PDF, never overwriting v30–v32) to that framing.

*Verified read-only against the registered model (`char_eq`, `r1_basin`) and the manuscript; all numbers above
were recomputed. No manuscript file was modified.*
