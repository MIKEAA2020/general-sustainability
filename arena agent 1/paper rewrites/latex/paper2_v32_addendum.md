# v32 addendum — Tier A/B caveats + Helly sparse-witness theorem

Built on v31 (verified revision of the three Automatica routes). v30/v31 untouched.

## Tier A (correctness/clarity caveats, from the remaining audit points)

1. **Convexification wording** (review 3.1): the relaxed-inclusion parentheticals in (H1.2) and (H3.3)
   now state the real reason — for `C^1 q` the directional derivative `∇q(x)·v` is affine in the velocity —
   instead of "because the constraint is convex in the velocity".
2. **Zero-margin phrasing** (review 3.5): the common-action obstruction is now a "formal zero-margin
   counterpart" of the delayed obstruction, explicitly distinct (local action-feasibility vs finite-time
   survival-value), "so the pair is not related as a T_obs→∞ limit".
3. **Continuous-time information model** (review 1.3): §2.3 conventions now state the within-interval
   record is observed continuously but cannot change the held action, and the §3.2–3.4 certificates use
   only observation-equivalence, so they hold under any within-interval record refinement that does not
   separate compatible branches.
4. **Sufficient-statistic qualification** (review 2.1): sufficiency is scoped to the delay-free
   set-membership semantics; delays / hidden parameters / history-dependent constraints require an
   augmented belief (Section 6.5).
5. **Example 1 vs the discrete instance** (review 7): §3.5 now calls the one-step system "the discrete
   one-step abstraction of Example 1" with its transition and grid stated.
6. **Exponential belief-space caveat** (review 4.1): §3.5 notes the recursion is exact but worst-case
   exponential in |X| (up to 2^|X| beliefs); finite-checkability is per belief.
7. **Farkas finite-witness caveat** (review 5): §3.3 states the Farkas certificate is finite when the
   constraint family admits a finite representation, and points to the Helly witness for the infinite case.
8. **Case-study scope caveat** (review 8.2): §8 states the audit is symbolic/one-dimensional and makes no
   claim of a general-purpose computational calculus.

## Tier B (micro-wordings)

- Reach set defined as the "all-disturbance, all-solution" reachable set (review 3.3).
- Obstruction-ladder caption: the response sets "form nested necessary conditions for viability" (review 3.4).
- Chance constraint written explicitly as `ℙ_{b,π}(x_0,…,x_k ∈ V) ≥ 1−ε` (review 9.2).
- Theorem 7 notes the horizon counts the current state (review 9.1).

## New result: sparse common-action witness (Helly) — Proposition 3

Inserted in §3.3 after the Farkas certificate. Under affine-in-control dynamics
`f(x,u,d)=f_0(x,d)+f_u(x,d)u`, compact convex control set `U`, convex closed `U(x)`, compact `D(x)`, and
`C^1` constraints, each safe-control set is a compact convex subset of `ℝ^m`, and the safety-case
common-action obstruction `∩_{x∈B} R_𝒱(x)=∅` holds **iff** it is witnessed by at most `m+1` compatible
states. Proof: compactness gives a finite subfamily with empty intersection, and the finite Helly theorem
reduces it to `m+1` members. The admissibility analogue holds under the same convexity assumptions.

This is the "Theorem D" the review's revised spine requested: it shows the common-action obstruction always
has a sparse witness independent of the size of the belief, and it makes the worked two-floor certificate
(m=1, two states) an instance of the bound.

## Renumbering note

The new proposition is **Proposition 3**; subsequent propositions shift: uniform-margin → 4, ladder → 5,
fibre → 6, monotone → 7, chance → 8, degenerate → 9. All references are `\ref`-based; §1.4's range now reads
"Propositions 2–5".

## Build verification

- Main: 15 pages, two-column, 4 figures, 1 table, 0 `??`, no overfull boxes, no undefined references;
  abstract 262 words.
- Supplementary: 13 pages, 3 figures, 0 `??`, no warnings; S1 carries the corrected statements/proofs.
