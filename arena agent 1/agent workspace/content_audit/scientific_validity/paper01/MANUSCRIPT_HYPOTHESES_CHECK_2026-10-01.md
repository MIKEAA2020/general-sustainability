# Paper01 manuscript-hypothesis check BEFORE repair

2026-10-01. This is a check against the paper's *own* assumptions, not a Lean statement. The exact witness program `counterexamples.py` was rerun (five expected lines; 42/30/12, 4/5, -1/2, 99/100). Manuscript heads were not changed while evaluating the following.

## §3.7 oracle-recourse proposition, main lines 1168–1190

| Written hypothesis / framework condition | Witness and check |
|---|---|
| `X ⊂ R^n`; `f` continuous, `U,D` compact-valued, closed graph; all measurable selection pairs admit Carathéodory solutions; convexified relaxed inclusion Marchaud (main §2.1) | `X=R`; `f(x,u,0)=-1+xu` smooth; `U(x)=[-1,1]`, `D(x)={0}` constant compact convex; `|f|≤1+|x|` gives global Carathéodory solutions and Marchaud growth/convexity for relaxed inclusion. |
| `B0` compact initial information set, branches observation-equivalent over `[0,τ)` (main §2.3, §3.7) | `B0={1,2}` is compact and lies in the constant-observation fibre; initial prior support may be narrower than a full fibre (the §3.7 statement does not demand `B0=O⁻¹(y)`). `O≡0`, so both branches give identical records, even beyond `τ=1/2`. A single observation-independent `u=1` is allowed and keeps both safe. If *only* complete observation fibres were intended, that additional restriction is **not** in §3.7 and must be stated; an equivalent discrete hidden-mode augmentation can make the finite fibre explicit. |
| Control-affine form `f=f0(x,d)+B(x)u`, compact convex `U` | `f0=-1`, `B(x)=x`, `U=[-1,1]`. **No written state-independent-`B` hypothesis.** |
| `q_j` facet/constraint, label `(θ,j,t)` with `t∈(τ,T]`; `β` zero-control margin and zero-control transition matrix | `q(x)=x−1`, safety `x≥1`; select label on the `x0=1` branch at `t=T=1`, `τ=1/2`. Zero-control path `x̄=1−s`, `X(1,s)=1`, `β=−1`, `k(s)=1−s`. |
| λ nonnegative, sums to 1; disturbance realizations admissible; `Γ_h<0` | One stored label λ=1 (other branches need not have positive label weight), unique admissible disturbance `d=0`. `h_{[-1,1]}(1−s)=1−s` for `0≤s≤1`; `Γ_h=−1+1/2=−1/2<0`. |
| Conclusion `B0∉ERViab` for **every** policy | Contradicted by `u≡1`: `x1(t)=1` and `x2(t)=1+e^t≥1` for all time. No assumption requiring the input-output kernel to be exact is stated; the supplementary proof's “first order” aside does not provide a remainder bound. **The witness meets every explicit operational hypothesis of the proposition** and refutes its conclusion. |

Result: real counterexample to the manuscript proposition, outside P1 Lean's explicitly discrete-only scope. A narrowly provable replacement requires affine-in-**state** dynamics with control-independent coefficients, exogenous disturbances, and affine safety facets (or an explicit validated one-sided remainder); the existing hexagon/double-integrator worked example is in that smaller class.

## §10 deterministic-limit proposition, main lines 1846–1875

| Written condition | Witness and check |
|---|---|
| finite `X,A,D,Y`, deterministic maps `x⁺=F(x,a,d)` and `y=O(x,a,x⁺)` | Safe state `s`, absorbing unsafe state `⊥`, one action `a`, `D(s)={good,bad}`; `F(s,a,good)=s`, `F(s,a,bad)=⊥`; `O≡y0`. The map is deterministic conditional on `d`. |
| stochastic `T` and likelihood supports equal the disturbance-reachable states and possible observations | `T(s|s,a)=99/100`, `T(⊥|s,a)=1/100`, `T(⊥|⊥,a)=1`; observation emits `y0` with probability 1. Exact prescribed supports, no zero-probability reachable outcome. |
| belief `b` carried by `B⊂V`; first-step set-valued recursion | `B=supp(b)={s}⊂V`, `b(s)=1`. Robust `W1` fails because the bad successor is possible. |
| `V_k(b)` defined in §10 by **fixed stochastic** `T`; claimed `V1≤1−min_B b=0` | Its own §10 definition gives `V1=99/100`, so the displayed numerical inequality is false *on the fixed-kernel reading*. |
| Additional wording “the disturbance read adversarially within its support” | **Unresolved semantic collision**, not a checked numerical hypothesis: if this means an adversary can replace `T` by a point mass on `bad`, the resulting robust/minimax objective is **not** the `V_k` defined in §10. One cannot both hold the stipulated `99/100` fixed kernel and replace it with an adversarial realization in that same value. This does not rescue the claimed fixed-kernel bound; it makes the statement ambiguous unless another value is defined. |

Result: the counterexample meets the finite maps, support, full-support prior and *defined stochastic value* assumptions; the adversarial phrase makes the statement internally ambiguous, so do **not** represent the counterexample as refuting a separately defined robust value. Narrow to a deterministic **single-successor** transition kernel with deterministic observations and `B=supp(b)`, where the original min-mass bound follows by pathwise reasoning; remove the adversarial phrase from this stochastic proposition. Note an **independent missing condition**: “`b` carried by `B`” permits zero-mass states in `B`, which can defeat the strict `<1` conclusion even with deterministic dynamics. The narrower support condition is required. Replace the one-step argument with induction on the earliest failing stage; failure of `W_k` need not mean first-step exit.

## Boundaries for the other two groups

#2: H3.2 quantifies over *all implementable blind-window controls*, not inherently held controls. The conditional theorem survives; the *audited example* uses a whole-window hold only (source script and supplementary explicitly say so). Its 42/30+12 values require a declared hold class. Exact enumeration also shows 30 nonviable cells under per-step time-varying blind controls. Repair the application scope, not the theorem.

#4: The decaying-model example has correct relaxed threshold `(10/9)^K` but borrows `z0−1` from a distinct non-decaying, **held** regime. Its supplementary LP proof separates the two. The supplementary Helly block uses discrete `q(F)≤0` and convex `q`, whereas the main uses continuous-time tangent `∇q·f≥0` with `q≥0`; the main already supplies its own Helly proof. Repair the inconsistent example and replace the mismatched supplementary proof, retaining the main theorem's mathematical content.

## Cross-paper rule

For every further claim, map it to its **exact Lean statement first**, if one exists; otherwise evaluate its manuscript hypotheses and evidence independently. This is a **partial-formalization coverage risk across the corpus**, not proof that all eight papers present their whole bodies as Lean-verified: paper01 §3.8 explicitly says its continuous-time results are *not* formalized. Claim-level mapping is needed before asserting any corpus-wide overstatement. This review continues **one paper per turn**; no ws claim was evaluated here.
