# A021 Binding-Data Availability Crosswalk

## Conclusion

The standalone A021 source does **not** instantiate its abstract binding functional `F^k`, slack functional `G`, couplings `f,g`, or select a concrete invariant object. However, the workspace is not devoid of candidate equations or spectral data: the companion corrected A018 manuscript contains explicit three-, four-, and five-state cores, baseline parameter tables, delay structure, characteristic matrices/functions, interval-certified Hopf crossings, first Lyapunov coefficients, periodic-orbit continuations, and selected Floquet multipliers.

Therefore the precise status is **partial availability without an A021 model crosswalk**, not total absence of equations.

## What A021 itself supplies

Source: `uploads/paper_IV_liebig_cm.txt`.

- Abstract block state `X^i=(N_i,A_i,Z_i,E_i)` and reference to companion vector fields `F^i`.
- Abstract binding/slack split `F^k`, `G`, `f`, and `g`.
- A constant delay symbol `tau` and delayed histories.
- Yield-gap perturbation scale and qualitative slack stability.

It does not specify:

- which companion core is the binding block;
- which parameter point is used;
- the exact formula identifying `F^k` with a named companion equation;
- the slack blocks and their concrete equilibria/spectra;
- the cross-block coupling functionals `f,g`;
- a compact binding equilibrium or periodic orbit selected as `A_x`;
- a complete tangent/normal splitting and uniform domination table.

## Candidate data available in A018

Source: `revised_articles/A018_capital_liquidation_corrected.tex` (and its canonical source materials).

Available candidate objects include:

1. A named gated three-state DDE `(N,Z,E)` with explicit equations (`eq:stock-core`, `eq:Z-core`, `eq:effort-core`).
2. A turnover-corrected four-state working core `(N,A,Z,E)` and a five-state extension including detritus `U`.
3. Fixed-delay structure: institutional delay `tau` enters through delayed memory `Z(t-tau)` in the effort equation; `tau_m` is the memory relaxation time.
4. Baseline Candidate A and Candidate B parameter tables and dimensionless groups.
5. Characteristic matrices/functions, the Hopf cubic, interval-certified simple crossings, and crossing/criticality information.
6. First Lyapunov coefficients at named Hopf points.
7. Continued periodic-orbit branches and selected Floquet evidence, including dominant multipliers near folds and stability evidence for named cycles.

These computational claims retain their user-attested verified status. They are nevertheless not yet organized into the complete compact-NAIM hypothesis package required by A021.

## What remains missing for A021 promotion

1. A formal decision selecting one A018 core, parameter point, and invariant object as the A021 binding block.
2. A crosswalk proving that A021's `F^k` is exactly that selected vector field and identifying every slack block and coupling.
3. For an equilibrium base: confirmation that all binding and slack roots are stable if an attracting zero-manifold is intended.
4. For a periodic-orbit base: one selected orbit, complete nontrivial Floquet spectrum, invariant history-space projections, transient prefactors, and uniform normal rate—not only selected dominant multipliers.
5. The full product splitting including every binding-transverse and slack direction.
6. Numerical inverse-tangent/conorm bunching with prefactors.
7. Exact source-theorem matching and localization for the selected object.

## Operational correction

The three open A021 verification actions are blocked by **missing instantiation and crosswalk**, not by a total absence of candidate equations, parameters, or spectral computations in the workspace.