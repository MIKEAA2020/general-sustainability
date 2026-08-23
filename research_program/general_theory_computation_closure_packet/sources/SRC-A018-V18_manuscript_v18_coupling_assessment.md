# Assessment of `manuscript_v18_dehedged.txt` for the A021 Coupling Gap

## Source identity

- File: `uploads/manuscript_v18_dehedged.txt`
- SHA-256: `15b6da19449d40ae9c5233dc8110e44b4f604f1673fd34a1671ab45b50d99acd`
- Size: approximately 606 KB
- Status: newly supplied supplemental manuscript version; not automatically substituted for the canonical corrected A018 source.

## Relevant new material

The manuscript supplies explicit general-framework ingredients that were not embedded in standalone A021:

1. vector stock states and service states;
2. a stock-service conversion matrix;
3. vector stock equations with effort-driven extraction;
4. a smooth vector Liebig service function
   \[
   S_{i,c}=S_{i,c}^{\max}\left[-\rho_{i,c}^{-1}
   \log\sum_m w_{m,i,c}
   e^{-\rho_{i,c}\widetilde Y_{m,i,c}/S_{i,c}^{\max}}
   \right];
   \]
5. smooth saturated sub-yields depending on the collection of stocks and wastes;
6. a variant registry identifying the canonical effort-saturation-corrected four-state core;
7. explicit acknowledgment that the scalar/four-state core is not yet a rigorous projection of the full vector framework.

## Does it close `G,f,g`?

**No.** It improves the source architecture but does not provide an exact multi-block RFDE of the A021 form

\[
\dot x=F^k(x_t)+\varepsilon f(x_t,y_t),
\qquad
\dot y=G(y_t)+\varepsilon g(x_t,y_t)
\]

with coordinate residuals derived from the four-state working cores.

The manuscript itself states that:

- the scalar core is a phenomenological proof-of-principle, not a rigorous projection of the vector accounting;
- the general vector framework and the delayed core share an architecture but are not yet one formally reduced system;
- deriving a rigorous reduction from the vector deficit space to the scalar/four-state core remains open;
- the smooth Liebig sharpness does not enter the reduced core's existing quantitative results.

Therefore no unique subtraction can define concrete `f,g` without an additional modeling/derivation decision. The general service map `F_i(N,W)` is not the same object as the four-state C4 RFDE vector field.

## What can now be stated more precisely

A future source-derived coupling must:

1. select the service component(s) through which blocks interact;
2. map the smooth vector Liebig service into the C4 regeneration and/or deficit-memory equations;
3. state whether stock equations remain local while only the perceived deficit is coupled;
4. specify physical cross-block coupling separately;
5. prove that subtraction from the uncoupled C4 product is `C1`-small on a uniform yield-gap tube;
6. preserve the donor/stock/waste units and the model-variant distinctions.

## Effect on theorem work

- The generic perturbation theorem remains available for an explicitly declared `C1` residual class.
- The original A021 vector-Liebig theorem remains blocked by the missing reduction/coupling map.
- The newly supplied manuscript does not change the numerical periodic-NAIM or CAP status.
- No manuscript source is replaced or merged from this file without a separate full-version audit.

## Minimal coupling decision now required

Choose one:

### Coupling A — memory-only service coupling

Keep each C4 physical stock/pool equation local and replace only the local regeneration term inside the institutional deficit signal by the vector-Liebig service. This is closest to the statement that coupling occurs through the service entering the deficit.

### Coupling B — physical regeneration coupling

Replace the local regeneration flux in both `dot N` and the deficit memory by the vector-Liebig service. This is stronger and changes mass/stock dynamics.

### Coupling C — generic perturbation class

Prove persistence for every residual satisfying

\[
\|R_\varepsilon\|_{C^1(\mathcal U)}\le C|\varepsilon|,
\]

without claiming that the residual has been derived from the full vector manuscript.

Absent an explicit choice and derivation, Coupling C is the only non-fabricated theorem route.