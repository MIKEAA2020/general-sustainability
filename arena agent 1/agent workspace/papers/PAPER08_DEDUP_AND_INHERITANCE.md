# Paper 8 — de-duplication and correction of the inherited 6.5-yr claim

Done 2026-09-29, after paper 7's sensitivity analysis showed the inherited number does not
support the weight placed on it.

## Three problems, not two

### 1. Duplicate header block — REMOVED

The `OWNERSHIP` + `SIBLING PAPERS` comment block appeared **twice, verbatim**:

```
%% OWNERSHIP: the 6.5-year crossing is computed and owned by Paper 7 (sampled map).
%%           Cite Paper 7 for it. Remove any independent re-derivation here.
% SIBLING PAPERS: Paper 7 (Sampled Governance), Paper 9 (Certified Horizons on a Real Record).
% Cross-cite, do not re-derive: ...
```

Now present once.

### 2. The paper re-derives what its own rule says to cite — LEFT IN PLACE, DELIBERATELY

The header rule says "Cite Paper 7 for it. Remove any independent re-derivation here."
Section 7 (Proposition 7.1) computes the crossing in full. However, paper 8's Section 7
contribution is not the crossing value — it is the **three-scheme comparison** (exact
held-measurement 6.5013; start-of-period 6.5013; native ZOH 6.7279), which paper 7 does not
do. Removing the derivation would remove that. So the derivation stays, and the ownership
is handled by citation and by the framing in item 3, not by excision.

### 3. The inherited claim was FALSE — CORRECTED

Two statements in v42 are contradicted by paper 7 §3.5:

| v42 claim | status |
|---|---|
| "the reported 6.50 yr is a **robust computed crossing** of the declared map" | **FALSE** |
| "All three consistent schemes therefore restabilise in a **tight** 6.50–6.73 yr band" | true on one axis, misleading by omission |

The scheme-dependence band **is** tight and **is** paper 8's legitimate contribution — it
constrains the **discretisation** axis. It says nothing about the **parameter** axis, where
paper 7 §3.5 shows the crossing sweeps 0.87–10.67 yr under a ±0.5% joint perturbation and
vanishes entirely in 20 of 64 corners at ±1%. Conflating the two axes is what made "robust"
unsupportable.

## Edits (paper08_governance_delay_v43.tex, 7 changes)

1. Removed the duplicated header block.
2. **Corrected the "robust computed crossing" claim** — replaced with the accurate
   statement plus the paper 7 §3.5 numbers, and an explicit separation of the
   discretisation axis from the parameter axis.
3. **Qualified the "tight band"** foreshadowing to say it is scheme-dependence only.
4. Abstract qualified: the value is "stable across discretisation schemes (6.50–6.73 yr)
   but not identifiable in the parameters".
5. Discussion qualified (×2).
6. Conclusion qualified.

The one residual occurrence of the phrase "robust computed crossing" is inside my own
provenance comment, quoting the old text — not in body prose.

## Verification of paper 8's own numbers

Paper 8's arithmetic was independently recomputed from the Candidate A reconstruction and
is **correct to the reported precision**. Nothing in it was changed:

| quantity | paper 8 | recomputed |
|---|---|---|
| complex pair at crossing | 0.9846 ± 0.1746 i | 0.984640 ± 0.174594 i |
| third eigenvalue | 0.1647 | 0.164697 |
| crossing angle θ | — | 0.175494 rad |
| 2π/θ (resonance) | ≈ 35.8 | 35.80 |
| \|λ\| − 1 | — | −3.45 × 10⁻⁹ |

θ = 0.175494 also matches the value recorded in paper 7's supplementary table.

## What paper 8 can still legitimately claim

- The **operator contrast**: Euler artefacts at 47.536 / 79.143 yr (exact radii there 0.786
  and 0.597) versus the exact update.
- The **scheme comparison**: the crossing is not a discretisation artefact. This is paper 8's
  own result and it survives intact.
- The **protective channel** no-Hopf result — stable at every tested interval.
- The **delayed-recruitment** and loop-gain sections, which do not touch the 6.5 figure.

What it can no longer claim is that 6.50 yr is robust, or that the 6.50–6.73 band
establishes identifiability.

## Residual risk

Paper 8's cadence framing — "lengthening the review interval restabilises a system that
annual review destabilises" — is the *direction* claim, and it is the one the paper cares
about. It is better supported than the number, because it depends on the sign of
dρ/dT_r (−6.83×10⁻⁴, verified) rather than on the crossing location. But paper 7 §3.5 shows
the *existence* of the crossing fails in a third of ±1% corners, so even the direction claim
is conditional on the parameter vector. That is now stated, but a referee may press on
whether the cadence claim has any parameter-robust content. It may not.
