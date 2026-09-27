# Lean audit v35 — `comp` feasibility probe

**Branch:** `lean-audit-v4` (additive). **Toolchain:** `v4.34.1`.
**Build at time of writing:** `lake build` → rc = 0, **46 jobs**, 42 imported
modules, zero warnings, zero `sorry`.

## The question

Item (3) of four: can `paper2_computational_certification_v18.tex`'s
substantive theorems be promoted from `Comp_Certification_v2`'s
**conditional scaffolding** to genuine results? v14 found that the module's
theorems take the paper's *conclusions* as hypotheses (failure mode **D**):
`sandwich_verdict` assumes `ρ ≤ J ≤ ρ + ē`, `characterization_verdict`
assumes the characterization. So the question is what it would take to
*derive* those hypotheses.

**This probe answers that with evidence, not expectation. It reverses one
expectation I stated last turn.**

---

## 1. What I expected, and what is true

Last turn I predicted `thm:bridge` and the Farkas-based `prop:value` would
hit "the same wall as `prop:probecount`" — out of reach. **Half right.**

- The *continuous-time* theorems are indeed out of reach. Confirmed by
  reading the statements.
- **Farkas is not out of reach. It is already proved.** `Prelude.lean:748`

      farkas_sound (a : Nat → List K) (b : Nat → K) (lam : Nat → K) (x : List K)
        (n : Nat) (hlen) (hnonneg : ∀ i, i < n → 0 ≤ lam i)
        (hzero : linComb 0 lam a n = 0) (hneg : sumRange (fun i => lam i * b i) n < 0) :
        ¬ (∀ i, i < n → dotp (a i) x ≤ b i)

  — a *theorem*, not an axiom. Nonnegative multipliers combining the rows
  to zero while their combination of the right-hand sides is strictly
  negative certifies infeasibility. That is precisely the logical core of
  the paper's obstruction certificates, and `dual_feasible_certificate`
  (`Comp_Certification.lean:127`) instantiates it. The layer also has
  `dotp` (Prelude:594), `linComb` (Prelude:693), `npow`, and
  **zero `axiom`/`opaque` declarations in any imported module** (verified
  by grep across all 42 files).

So the scaffolding is conditional on the *continuous-time* facts, not on
Farkas. Farkas was never the blocker.

## 2. The layer's inventory — what there is no room for

Every declaration in the layer is finite, discrete, or algebraic:
`OrdField`, `FinMass`, `Mass`, `SafeMDP`, `DetMDP`, `lsum`, `lmax`,
`dotp`, `linComb`, `subsetsOf`, `npow`, `hamming`, `natToK`, `drift`,
`stateAfter` …

A grep for `continuous`, `Compact`, `∫`, `TopologicalSpace` across all
modules returns **five hits, every one of them prose inside a docstring**
(`Comp_Certification:11,32`, `Comp_Certification_v2:25`,
`P1_Obstruction:11`, `P1_TimingCertificate:38`). There is no continuity
predicate, no compactness, no integration, no function space, and no
vector-space hierarchy.

## 3. Verdict, result by result

`paper2_computational_certification_v18.tex` has 7 numbered environments.

| Result | Verdict | Evidence from the statement |
|---|---|---|
| `prop:rows` — soundness | **already a result** | `robust_row_sound` (`Comp_Certification:54`) |
| `prop:rows` — converse | **blocked, not walled** | "the initial-state and disturbance maximizations separate from the control term because the control signal in a mode does not depend on `x₀` or `d`, so the rows are exact". Needs `𝓕_a` *defined* (kernels, support functions, `β_a`); today it is an opaque parameter `F` |
| `prop:value` | **out of reach** | "the policy-signal space is a finite product of weak-* compact sets `L^∞(I_r;U)` … and each `𝓕_a` is weak-* continuous; the maximum over labels is attained on the compact label set". Weak-* topology, Banach–Alaoglu-type attainment |
| `thm:bridge` | **out of reach** | (H1) Lipschitz in `t`; (H2) `TV(k_a) ≤ V_U`; (H3) `L¹` continuity of `a ↦ k_a` — "the `L¹` form is the operative one"; (H5) covering radius. Integration, total variation, Lipschitz bounds |
| `prop:beliefcells` | **out of reach** | `sup` over a cell, certified enclosure radius `δ_C`, conic/LP duality, refinement limit to singletons |
| `prop:rank` | **partially feasible — see §4** | the paper's *proof* is an explicit Farkas certificate: "safety requires `−w_j ≤ −1` for `j ≤ q` and `Σ_j w_j ≤ q − ε`; summing gives `0 ≤ −ε`, a contradiction" |
| `prop:redesign` (i)(ii) | **feasible, low value** | closed-form rational identities (`Γ_a(τ) = τ − 7/50 − (a−1)/2`, `τ_max(a) = 7/50 + (a−1)/2`), but they need the instance's control-set model — the dilated hexagon `aU` |
| `prop:redesign` (iii)(iv) | **no** | (iii) needs the pooled-kernel model `Σ_j λ_j k_j ≡ 0`; (iv) is a claim about the printed dual |
| `prop:ladder` (comp's own, l.1040) | **not examined** | out of this probe's scope; the probe targeted the two theorems the scaffolding points at, plus a feasibility sweep |

## 4. The one thing worth building

`prop:rank` ("arbitrarily large minimal obstructions with one input") is
the only result where the paper's own proof is a finite algebraic
certificate that the layer can already check.

The argument: with `w_j = ∫_{I_j} u`, safety of mode `j ≤ q` forces
`w_j ≥ 1`, and safety of the last mode forces `Σ_j w_j ≤ q − ε`. Summing,
`q ≤ Σ_j w_j ≤ q − ε`, i.e. `0 ≤ −ε`. **That is `farkas_sound` with
multipliers `λ = (1,…,1,1)`**: the rows combine to zero and the
right-hand sides sum to a strictly negative number.

What stands between this and a theorem is **not** Farkas and **not**
analysis — it is that `w_j` is defined by an **integral over a
continuous-time interval** and the modes are **ODEs**
(`ẋ = 1_{I_j}(t)(u−1)`). The layer has no integration and no ODEs. The
gap is a *modelling* gap, and it is the same kind of gap `EBC_Dynamics`
closed for the cube this session: replace the analytic object by the
finite quantity the argument actually uses.

Concretely, what is provable today, honestly labelled:

- the **certificate core**: from `1 ≤ w_j` (`j < q`) and
  `Σ_j w_j ≤ q − ε` with `ε > 0`, a contradiction — as an application of
  `farkas_sound`, or directly;
- *not* the paper's proposition, which asserts the **existence of a
  continuous-time system** with those properties.

That would be recorded as **machinery** (the certificate that makes every
obstruction involve all `q+1` modes), not as "`prop:rank` proved".

## 5. Recommendation

1. **Do not attempt** `prop:value`, `thm:bridge`, `prop:beliefcells`. The
   layer will not have weak-* compactness or integration, and building
   them is a different project from this one. Record them as out of reach,
   like `prop:probecount`.
2. **Keep** `Comp_Certification_v2`'s four theorems relabelled as
   conditional scaffolding (v16). They are correct as stated and their
   status is now honest.
3. **If comp coverage is wanted**, build `prop:rank`'s certificate core
   (§4). It is small, it is the paper's own argument, and it turns an
   "out of reach" row into a genuine partial.
4. **Correct the record**: Farkas soundness is proved in this layer
   (`Prelude:748`), axiom-free. Earlier framing that grouped it with the
   unreachable parts was wrong.

## 6. Files

Read, not modified: `paper2_computational_certification_v18.tex`
(`prop:rows` 253, `prop:value` 271, `thm:bridge` 411, `prop:rank` 889,
`prop:beliefcells` 980, `prop:redesign` 1107);
`lean/Formalizations/Comp_Certification.lean`;
`lean/Formalizations/Comp_Certification_v2.lean`;
`lean/Formalizations/Prelude.lean` (`dotp` 594, `linComb` 693,
`farkas_sound` 748).
