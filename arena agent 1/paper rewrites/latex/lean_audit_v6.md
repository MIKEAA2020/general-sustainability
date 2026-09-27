# Audit v6 — obstr's five theorems: feasibility triage

This **revises my own recommendation in v5**. That recommendation ranked the
five by fault-risk using label-gap data, without first checking whether the
layer's interface can express them. It can't, for three of the five. The
ranked list was right about risk and wrong about feasibility.

## The blocker is mathematical, not just effort

`Prelude.OrdField` is a minimal ordered field: field axioms, a total order,
`add_le_add`, `mul_le_mul_of_nonneg'`. It has **no Archimedean axiom, no
completeness, no sup/inf, no topology, no derivative, no measure.**

That matters more than "we haven't built the analysis yet": the interface
admits non-Archimedean models, so statements like the exit certificate or
the Nagumo condition are not merely unprovable here — they would be **false**
if stated interface-level. The layer cannot be extended to cover them
without changing the interface (which would break the dependency-free
property the README treats as a feature).

`Formalizations.P1_Obstruction`'s own header already says this:

> "The paper's continuous-time statements (Dini derivatives, exit
> certificates, timing bounds) live in an analysis setting **outside a
> dependency-free Lean layer**; what is formalized here is the exact discrete
> core…"

## Triage

| Theorem | Requires | Verdict |
|---|---|---|
| `thm:exit` | C¹ constraint `q`, Dini-derivative drift condition, ODE trajectories | **Out of reach** — and already declared out of scope by the module header |
| `thm:delayed` | continuous exit time τ, pre-observation policies, σ* as a sup over a control class | **Out of reach** — same |
| `thm:static-complete` | compact `V`, continuous `f`, closed-graph `D`, *measurable* open-loop controls, Nagumo boundary condition | **Out of reach** — topology + measure |
| `thm:pomdp` | belief-state value recursion — but the paper assumes `X, A, D, Y` **finite** | **Feasible** — `Prelude.FinMass` (`E`, `Prb`, expectation laws) is exactly the needed machinery |
| `thm:lp-instant` | (i) LP *complexity* count (ii) Farkas multipliers (iii) definitional (iv) soundness vs incompleteness | **Partially reachable** — (ii) and (iv) done below; (i) and (iv)'s incompleteness half are not |

## What was formalized

**New module `lean/Formalizations/P1_TimingCertificate.lean`**
(namespace `Formalizations.P1Timing`, 5 theorems, **new file — nothing
overwritten**).

Models the horizon-`n` blind-window program as `dotp (a i) x ≤ b i` for
`i < n` over a declared class `Pi` — which is what unrolling the affine
dynamics of `thm:lp-instant` produces, the disturbance entering only through
precomputed support constants.

| Theorem | Claim | Content |
|---|---|---|
| `satisfies_prefix` | (i) | feasibility of a prefix is necessary for the whole |
| `infeasible_mono_horizon` | (i) | infeasibility propagates forward ⇒ `{n : infeasible}` is an up-set ⇒ `σ*` found by bisection |
| `blind_window_farkas_certifies` | (ii) | nonneg row weights, vanishing aggregate control projection, negative aggregate constant ⇒ no feasible declared control |
| `farkas_certifies_affine_system` | (ii) | declaration-independent form: the certificate kills the whole affine system, hence *every* subclass |
| `relaxation_sound` | (iv) | enlarging the declared class can only help ⇒ relaxed certificate is sound for the declared class |

### A vacuous lemma was drafted and deleted

A sixth theorem, "a Farkas certificate over the relaxed program certifies
the declared program", was written and then **removed**: because the Farkas
certificate is declaration-independent, the subclass hypothesis was never
consumed. It was `blind_window_farkas_certifies` with an unused premise —
the exact defect this audit exists to remove. The module now records an
explicit note saying why it is absent, so nobody re-adds it.

### Verification (pinned `leanprover/lean4:v4.34.1`)

- `lake build` **rc=0**, 14 jobs, `✔ Built Formalizations.P1_TimingCertificate`
- **No warnings** from the new module
- `#print axioms`: `infeasible_mono_horizon` and `relaxation_sound` depend on
  **no axioms at all** (constructive); `blind_window_farkas_certifies` uses
  only `[propext, Classical.choice, Quot.sound]`, inherited from
  `farkas_sound`

### Deliberately not formalized

- **(i)'s complexity count** ("at most ⌈log₂ K⌉ + 1 LPs of polynomial size")
  is a claim about an algorithm's cost; it needs a machine model this
  dependency-free layer does not have. Only its monotonicity ingredient is
  formalized.
- **(iii)** ("the feasible set is the declared class itself, so no relaxation
  gap arises") is definitional at this level — the program's variables *are*
  the declared controls. Recorded as a comment, not a theorem, because there
  is nothing to prove.
- **(iv)'s incompleteness half** is an existential claim about specific data
  (`ex:relax-gap`: `z⁺ = (9/10)z ± u`, floor `z ≥ 1`) — instance-level, and
  certified by the deposited Python batteries.

## What remains, in order

1. **`thm:pomdp`** — the one genuinely reachable theorem of the five. The
   paper assumes finite `X, A, D, Y`, and `Prelude.FinMass` supplies belief
   masses, `E` and `Prb`. Substantial but clean: belief update `τ`, the
   Bellman recursion for `V_k`, and the load-bearing consequence the paper's
   own `prop:chance` proof leans on (`V_{k+1} ≤ V_k`).
2. **P3's structural core** — 18 results against a 4-theorem module, still
   the worst ratio in the layer. Feasibility not yet assessed.
3. **ARV's `prop:windows` / `prop:brackets`** — cheapest wins; extend the
   existing bracket formalization.

Note that 1–3 should each get the feasibility check that v5 skipped for the
obstr five. The lesson: rank by risk, but check expressibility first.
