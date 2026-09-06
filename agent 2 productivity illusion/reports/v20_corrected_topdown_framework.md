# Corrected & completed top‑down analysis + adjoint code, aligned to our framework

**Scope:** the attached AI `uploads/top-down ecol.txt` (candidate menu + "execution") and its adjoint
template code are here **improved, corrected and completed to align with the corrected S0 model**, and
delivered as a **standalone documented report**. No mint, no push, no manuscript edit (your standing
"don't implement this turn"). Every number below is **verified** against the committed code
(`model_sims/corrected.py`, `model_sims/char_eq.py`, `model_sims/r1_basin.py`).

**Model (corrected S0, deficit region `E>bA`), baseline:** `ρ=0.05, A_max=1.2, b=0.5, b_G=0.8, e=0.55,
r=0.02, A_ext=0.02` (`b_Gρ=0.04 < b=0.5` → flow‑dominated). Regeneration `G(A)=ρA(1−A/A_max)`,
`B=bA + b_G G(A)`, `K=B/e`, `R_B=E/B`, `R_A=E/(bA)`, flow share `ψ=bA/B`.

---

## Part A — The candidate menu, corrected & completed

### A1. Dimensionless collapse criterion `R = τ_g/τ_p` — **refuted; the cliff is τ_g‑driven**
Full sweep at `(A₀=1.0, P₀=0.9)` over `τ_g∈[0,40] × τ_p∈{0,5,10,15,20,25,40,60}`: the recover/collapse
boundary is **`τ_g = 18 yr at every τ_p`** (`R` falls 3.6 → 0.30). **No single dimensionless ratio
exists** because the regeneration lag alone sets the threshold once the demographic response is slow.
- **Corrected conclusion:** the two delays are **not symmetric**; the cliff is regeneration‑lag‑driven.
- **Completed caveat:** at very large `τ_g` the recover fraction *re‑opens* (≈0.21 at 40, 0.30 at 50,
  0.32 at 60 yr, v18/v19); at `τ_g=60` the outcome depends on `τ_p` (recovers at `τ_p=0,5`, collapses
  at `τ_p≥10`). So the "τ_g≈20 yr" statement holds across the field‑supported band; the extreme‑lag
  re‑opening is a separate, IC‑dependent effect.
- **Figure:** `scans/topdown_delay_boundary.png` (verified, made this session).
- **Recommendation:** one sentence + figure in §8; strengthens the "τ_g≈20 yr" claim and preempts a
  reviewer asking about τ_p scaling.

### A2. First integral / neutral direction / adjoint — **corrected to the neutral‑family separator**
- **Real premise:** `D(0)=0`, so `A0+Ag+Ap` is singular and there is a **neutral continuum** (no
  isolated interior attractor) — this is R2's result, and it is the *origin* of the separator.
- **Corrected object:** the *exact* no‑delay basin separator is the **equilibrium family
  `P = B(A)/e`**, i.e. **`R_B = 1`** (verified: bisected boundary `P₀` = `B(A₀)/e` to 4 decimals at
  every `A₀`). This is a **nonlinear curve**, not a single linear functional of `(A₀,P₀)`.
- **Corrected evaluation (class‑imbalance‑aware = balanced accuracy):**

| `(τ_g,τ_p)` | #R / #C | raw acc | sens(recover) | spec(collapse) | **balanced** |
|---|---|---|---|---|---|
| (0,0) | 83/125 | 99.0% | 100.0% | 98.4% | **99.2%** |
| (10,25) | 83/125 | 99.0% | 100.0% | 98.4% | **99.2%** |
| (30,25) | 11/197 | 64.4% | 100.0% | 62.4% | **81.2%** |

  vs the AI's "linear adjoint functional": (0,0) raw 96.2%/balanced 96.4%; **(30,25) raw 94.7% but
  balanced **50.0%** — pure chance.** The AI's "94 %" is the majority‑class collapse rate (197/208),
  not a separator. So:
- **Completed interpretation:** the neutral family `P=B(A)/e` (=`R_B=1`) is the correct separator; it is
  near‑perfect at short/no lag (balanced ~99%) and **degrades at long lag** (balanced 81%, specificity
  drops — it over‑predicts recovery because the basin is *eroded*, the τ_g basin‑boundary crisis). The
  claim of an exact "first integral" with 100%/94% is **not** supported.
- **Codifies into our framework:** `R_B = 1` is the operating boundary (see A7).

### A3. Recovery‑overshoot scaling — **real, but IC‑dependent and steep; AI's formula wrong**
Measured `A_peak/A_max − 1` vs `τ_g` (from a deep floor IC `A₀=0.20, P₀=0.10`, τ_p=25):
`τ_g=8/10/12/15/18 → 0.0001/0.0038/0.0142/0.0383/0.0683`. The AI's `0.08(τ_g/10)^0.4` is **wrong**
(overstates by ~10× at τ_g=10). A local power‑law gives exponent **α≈4.8** (steep, near the cliff).
**Completed caveat:** the magnitude depends on the recovery IC (a near‑boundary IC gives
0.008/0.042/0.067 at τ_g=10/15/18 vs 0.004/0.038/0.068 from the deep floor). **No single power‑law over
`τ_g` alone holds.** Treat as a qualitative "overshoot grows steeply as `τ_g` nears the cliff" note.

### A4. Comparison theorem for domain‑wide collapse — **implemented as the measurable "rescue set"**
Domain‑wide collapse (even healthy `A₀=1.0` collapses at `τ_g=30`) is real and verified. Implemented as
`topdown.rescue_set`: the recover fraction of the IC box and the A‑span of the rescue set vs `τ_g`
(**reported in Part E**) — 40 % → a measure‑zero strip at `A=A_max` for `τ_g≳20`. A *rigorous* comparison
theorem (Kuang‑style delayed‑logistic bound) remains a genuinely open, research‑level proof and is
**not** claimed here.

### A5. Two‑delay Hopf / oscillatory islands — **verified: monotone‑only (confirms R2)**
`char_eq.crossing_curves` over the whole `(τ_g,τ_p)` plane (it already sweeps both delays) returns
**0** imaginary‑axis crossing points; the leading eigenvalue is **constant `Re λ ≈ +0.625`** for
`τ_g=0…60`. So there are **no oscillatory islands**; the instability is monotone throughout. This
*strengthens* (does not revise) R2. **Recommendation:** a one‑line confirmation in §8/§13.

### A6. Asymptotic discrete map for large `τ_g` — **implemented, and corrected**
Implemented as `topdown.method_of_steps` / `map_fixed_points` / `map_local_stability`. The map's fixed
points **equal the equilibrium family** (`A_c(E)`), **but** its local stability is **constant**
(`Re λ = +0.59→+0.625`, no flip at `τ_g≈19`) — so the reduced map captures the fixed points **not** the
cliff. The `τ_g` transition is therefore a **nonlocal basin‑boundary crisis**, not a local map
bifurcation (strengthens the no‑CSD result). **Full numbers in Part E.**

### A7. Framework‑aligned headline (the completed top‑down result): macro‑ratio safe operating space
Our own top‑down result (Lens 1 + Lens 4), which the AI document does **not** cover, is the
bookkeeping‑anchored macro‑ratio boundary:
- **Exact identity (deficit region, no ramp):** `E − bA = b_G G(A(t−τ_g)) − b_G dA/dt`, and
  `dA/dt = (B̃ − E)/b_G` with `B̃ = bA + b_G G(A(t−τ_g))`. Hence **`dA/dt<0 ⟺ E > B̃ ≈ B`** — the
  decline trigger is **`R_B = 1`**, not `R_A = 1`.
- **Flow‑share closed form:** `R_A = R_B/ψ`; at a sustainable interior MSY (`b_Gρ>b`):
  `ψ* = 2/(1+b_Gρ/b)`, **`R_A^eq = (1+b_Gρ/b)/2`**. Flow‑dominated (baseline): no interior MSY,
  `R_A = R_B = 1` at the boundary `A_max`.
- **Leading indicator ≠ trigger:** `R_A` crosses 1 earlier (by `1/ψ`) but is not the cause; the
  balance point is `R_B=1`. This is exactly the neutral‑family separator of A2 — the two threads
  **converge**.
- **Silent collapse (policy‑relevant negative):** at `τ_g=30`, **37% of collapse cells begin with both
  `R_B<1` and `R_A<1`** — neither macro ratio warns; only shortening the `τ_g` lag helps (ties to
  §13(9) basin‑boundary crisis, no CSD). **Figures:** `scans/topdown_macro_ratios.png`,
  `scans/topdown_ratio_separation.png`.

---

## Part B — The corrected & completed template code

The AI's template is replaced by a corrected, tested module aligned to our framework. **Fixes:**
(1) correct matrices; (2) correct **left** null vector (`U[:,-1]`, not `Vh[-1]`); (3) correct
equilibrium family `P=B(A)/e` and parameters `ρ=0.05, e=0.55`; (4) the separator is the **nonlinear
neutral family `R_B=1`**, not a linear "adjoint functional"; (5) honest **balanced‑accuracy**
evaluation (the 94% raw was a class‑imbalance artifact).

```python
# topdown_framework.py — corrected & completed, aligned to the corrected S0 model
import numpy as np

# ---- baseline parameters (flow-dominated) ----
RHO, AMAX, B0, BG, E, R = 0.05, 1.2, 0.5, 0.8, 0.55, 0.02

def G(A):  return RHO*np.asarray(A,float)*(1-np.asarray(A,float)/AMAX)
def Gp(A): return RHO*(1-2*np.asarray(A,float)/AMAX)
def B(A):  return B0*np.asarray(A,float) + BG*G(A)
def K(A):  return B(A)/E

def equilibrium_family(A):        # one-param family P=B(A)/e  (== R_B=1 locus)
    return K(np.asarray(A,float))

# ---- CORRECT linearised matrices (the AI's placeholders were wrong) ----
def linearised_matrices(Astar):
    a1 = Gp(Astar)                 # regeneration, DELAYED tau_g
    a3 = B0/BG                     # depletion (current, +A)
    aE = -E/BG                     # depletion -> P (current)
    a4 = R*(B0+BG*Gp(Astar))/E     # K -> P, DELAYED tau_p
    return (np.array([[a3,aE],[0.0,-R]]),
            np.array([[a1,0.0],[0.0,0.0]]),
            np.array([[0.0,0.0],[a4,0.0]]))

def neutral_direction(Astar):
    """LEFT null vector (for the adjoint) = U[:,-1]; the AI used Vh[-1] = RIGHT null (bug)."""
    A0,Ag,Ap = linearised_matrices(Astar); J=A0+Ag+Ap
    U,s,Vh = np.linalg.svd(J)
    return U[:,-1], Vh[-1,:], s          # left_null, right_null, singular values

# ---- macro ratios (the result) ----
def ratios(A0v,P0v):
    return (E*P0v)/B(A0v), (E*P0v)/max(B0*A0v,1e-9)      # R_B, R_A

def neutral_separator(A0v,P0v):
    RB,RA = ratios(A0v,P0v)
    return ("R" if RB<1.0 else "C"), RB, RA              # below family -> recover

def flow_share(A0v): return (B0*A0v)/B(A0v)
def RAeq_from_regime(index):        # =1 for index<=1 (no interior MSY), else (1+index)/2
    return 1.0 if index<=1.0 else (1.0+index)/2.0
```

**Verified smoke test** (runs without error): `A*=1.0` → `A0=[[0.625,-0.688],[0,-0.02]]`,
`Ag=[[-0.033,0],[0,0]]`, `Ap=[[0,0],[0.017,0]]` (match `char_eq` coefficients); singular values
`[0.907, 0]` → `D(0)=0`; **left null** `[-0.029, 0.9996]`, **right null** `[-0.758, -0.652]`
(distinct — the AI's bug); `neutral_separator(1.0,0.9) → 'R', R_B=0.977`; `equilibrium_family(1.0)=0.9212`;
`RAeq_from_regime(3)=2.0`.

**What this code delivers (use it this way):**
- `neutral_separator(A0,P0)` recovers/collapse by `R_B=1` (the neutral family), and pairs numerically with
  the **balanced‑accuracy** measure (A2 table) — do not report raw accuracy for the imbalanced long‑lag basin.
- `neutral_direction`, `linearised_matrices`, `RAeq_from_regime` give the exact analytic structure.
- **Do NOT** present a linear "adjoint functional" as a 100%/94% first‑integral separator; it is
  chance (balanced 50%) at long lag.

---

## Part C — Reconciliation & what to actually publish

| AI claimed | Corrected / verified | Status |
|---|---|---|
| dimensionless `R` criterion | no such ratio; cliff is τ_g‑driven | adopt (1 line + fig) |
| first‑integral 100%/94% | neutral family `R_B=1` is the separator: balanced 99%→81%; linear functional = chance at long lag | correct & adopt as neutral‑family result; do NOT call it a first integral |
| overshoot `0.08(τ_g/10)^0.4` | real but IC‑dependent & steep (α≈4.8); AI formula wrong | qualify; descriptive note only |
| no oscillatory islands | verified monotone‑only (confirms R2) | **done** (A5) |
| comparison theorem | observation real; rescue set 40%→measure‑zero strip at `τ_g≥20` | **done** (C4) — rigorous proof out of scope |
| discrete map | fixed points == family, but local λ constant → cliff is **nonlocal** | **done** (C6, corrected) |

**Bottom line:** the AI's plan is a reasonable menu, but its "execution" was fabricated and two results
were wrong. Corrected to align with our framework, the genuine top‑down advances are (i) the **`τ_g`‑driven,
`τ_p`‑independent cliff** (A1), (ii) the **convergence of the basin separator, the neutral family, and
`R_B=1`** (A2 + A7), (iii) the **measure‑zero rescue set** (C4) and (iv) the **nonlocal‑cliff** map
reading (C6), together with the verified monotone‑only confirmation (A5). All are consistent with and
strengthen v18/v19.

## Part E — the two remaining candidates, now implemented (C4, C6)

**C4 — comparison theorem ⇒ quantified "rescue set" (topdown.rescue_set).** Recovery fraction of the
208‑cell IC box vs `τ_g`:

| `τ_g` | recover | rescue set (A‑span) |
|---|---|---|
| 0 / 10 / 18 | 39.9 / 39.9 / 39.4 % | 0.100–1.300 (13 distinct A) |
| 20 / 30 / 40 | 5.3 % | **1.200–1.200 (1 distinct A)** |

So the rescue set collapses from ~40 % of the initial‑condition space to a **measure‑zero strip at
`A=A_max`** for `τ_g≳20` (domain‑wide collapse) — this quantifies the C4 premise. A *rigorous* comparison
theorem remains genuinely open and is *not* claimed.

**C6 — asymptotic discrete map ⇒ implemented and corrected (topdown.method_of_steps).** Fixed points of
`A_{k+1} = A_k + τ_g[G(A_{k-1}) − (E − bA_k)_+/b_G]` equal the equilibrium family
(`E=0.15/0.30/0.50 → [0.283,1.2]/[0.576,1.2]/[0.986,1.2]`, interior root = `A_c(E)` plus the boundary
`A_max`). **But** its local stability is **constant** (`Re λ = +0.59→+0.625`, no flip at `τ_g≈19`) — the
map captures the fixed points **not** the cliff. The `τ_g` transition is **nonlocal** (basin‑boundary
crisis), not a local map bifurcation. This reinforces the no‑CSD result (A5, §13(9)).

## Part D — Completed, reproducible scripts & augmentations

The ad‑hoc `/tmp` verification scripts are now **completed and promoted into the repo** so the whole
top‑down analysis is reproducible and the bug‑fixes are locked in.

| Artifact | Role |
|---|---|
| `model_sims/topdown.py` | The completed module: A1 `delay_boundary`, A2 `neutral_direction`/`neutral_separator`/`separator_accuracy`, A3 `recovery_overshoot`, A5 `no_crossing_confirmation`, **C4 `rescue_set`**, **C6 `method_of_steps`/`map_fixed_points`/`map_local_stability`**, A7 `ratios`/`flow_share`/`RAeq_from_regime`. |
| `model_sims/_run_topdown.py` | Driver: runs all sections, regenerates the 3 figures, writes `data/topdown_results.json`. |
| `data/topdown_results.json` | Verified results record (reproducible, machine‑readable). |
| `scans/topdown_delay_boundary.png`, `scans/topdown_macro_ratios.png`, `scans/topdown_ratio_separation.png` | Regenerated figures. |

**Run it:** `PYTHONPATH=. python -m model_sims._run_topdown` (≈4 min; two basin sweeps dominate).

**Bug fixed during completion.** In `separator_accuracy` the local true‑positive count was named `tp`,
which **overwrote the `tp`(=τ_p) parameter** and was stored as the delay label (`(0,83)` etc.). Renamed
to `tpv`; verified output now correctly `(tg=0,tp=0)`, `(tg=10,tp=25)`, `(tg=30,tp=25)`.

**Augmentations (weaknesses addressed)**
1. **Class‑imbalance trap** → the separator is now scored by **balanced accuracy** (mean of sensitivity
   & specificity), which exposes the AI's "94 %" as trivial (balanced 50 % at `τ_g=30`).
2. **Overshoot "power law"** → replaced with measured, **IC‑dependent** scaling; local exponent ≈4.8, not
   0.4; no single `τ_g`‑only law.
3. **Dimensionless ratio** → verified refuted (cliff at τ_g=18 yr for every τ_p).
4. **"No Hopf"** → verified across the **full** delay plane (0 crossing points, `Re λ ≈ +0.625`).
5. **Separator unified with the macro‑ratio result** → the neutral family `P=B(A)/e` **is** the `R_B=1`
   locus; the two threads (AI's "first integral" and our Lens‑1‑/‑4 "safe operating space") converge.
6. **Silent‑collapse quantified** → 2/125 (1.6 %) at τ_g=10 vs **72/197 (36.5 %)** at τ_g=30 — neither
   macro ratio warns; the lag is the controlling variable (§13(9)).

## Files
- This report: `reports/v20_corrected_topdown_framework.md`.
- Completed scripts: `model_sims/topdown.py`, `model_sims/_run_topdown.py`.
- Results record: `data/topdown_results.json`.
- Regenerated figures: `scans/topdown_delay_boundary.png`, `scans/topdown_macro_ratios.png`,
  `scans/topdown_ratio_separation.png`.
