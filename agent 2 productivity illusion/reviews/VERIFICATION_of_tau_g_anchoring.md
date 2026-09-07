# Verification & Strengthening of the τ_g Empirical-Anchoring Proposal

The reviewer proposed anchoring the regeneration lag `τ_g` via the worked estimate
`t₅₀ = τ_g ln2 ⇒ τ_g ≈ 1.44·t₅₀`, applied to three published recovery statistics (forest ~50% at ~20 yr;
soil ~20–23 yr to 50%; fisheries ~12–13 yr to 50%), giving τ_g ≈ 17–33 yr (representative 25 yr), labelled as
an illustrative empirical anchoring rather than a calibration. I evaluated, verified, and strengthened this
before implementing. The proposal is **sound in intent but has three weaknesses that were corrected**: two of
the three cited numbers are not faithful to the sources, the conversion conflates the model's regeneration
rate with its regeneration lag, and its suggested sensitivity statement ("results unchanged over 17–33 yr")
is false because the band straddles the model's own collapse cliff.

## 1. The arithmetic is correct
`t₅₀ = τ̄ ln2 ⇒ τ̄ = t₅₀/ln2 = 1.4427·t₅₀`. So forest 20 yr → 29 yr, soil 20–23 yr → 29–33 yr, fisheries
12–13 yr → 17–19 yr. Retained (as a heuristic).

## 2. The three cited statistics do not match the sources (verified, not taken at face value)

| System | Reviewer's claim | What the source actually reports |
|---|---|---|
| Tropical secondary forest | ~50% at ~20 yr | **Poorter et al. (2016):** 122 Mg ha⁻¹ above-ground biomass recovered **within 20 yr**; **median 66 yr to 90 %** of old-growth biomass (recovery varied 11.3-fold across sites). No "50% at 20 yr" headline. |
| Temperate soil | ~20–23 yr to 50% | **Poeplau et al. (2011):** a new SOC equilibrium is reached after **23 yr** (deforestation) and **17 yr** (grassland→cropland). Not "20–23 yr to 50%"; the metric is time-to-new-equilibrium. |
| Marine fisheries | ~12–13 yr to 50% | **Hutchings & Reynolds (2004):** only **29 %** of collapsed stocks recovered to 50 % within **5–15 yr**; most showed little change by 15 yr. **Neubauer et al. (2013):** recovery generally within **≈20 yr** once exploitation is reduced to FMSY. No "12–13 yr to 50%" in either. |

The manuscript's own §8 "empirical grounding" previously repeated the same two unsupported values
("forest AGB ≈50 % at ≈20 yr"; "fisheries median ~12–13 yr to 50 %"), so **both the reviewer's table and the
manuscript's existing text were corrected.**

## 3. The conversion conflates the model's regeneration rate with its lag (the key conceptual weakness)
The model separates two regeneration quantities (prediction 7 / §12.2): the regeneration **rate** `ρ` (yr⁻¹),
which sets *how long* recovery takes (recovery timescale ≈ `1/ρ = 20 yr` at `ρ = 0.05`), and the regeneration
**lag** `τ_g` (yr), which sets *whether* the stock recovers at all. Published recovery-time / time-to-equilibrium
statistics are, in the model's terms, statements about the *rate* (they are timescales); they become statements
about the *lag* only under an explicit "effective-timescale" reading. The proposal therefore crosses the
rate/lag line. **Strengthened:** the converted interval is presented as an *effective* regeneration timescale
(τ̄ ≈ 25–33 yr, representative ≈29 yr), clearly labelled illustrative, with the rate/lag caveat stated
explicitly rather than silently.

## 4. The suggested sensitivity statement is wrong; the band straddles the model's cliff (verified numerically)
The proposal suggested stating "the model's qualitative results are unchanged over 17–33 yr." This is **not**
accurate. I ran the model (`model_sims` `corrected_s0`/`corrected_basin_fraction`, `char_eq`) at fixed
`τ_p = 25`:

**Recover fraction vs `τ_g`** (coarse grid, baseline params):

| `τ_g` (yr) | 0 | 10 | 17 | 18 | 19 | 20 | 25 | 30 | 33 |
|:--:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| recover | 0.54 | 0.54 | 0.54 | 0.54 | 0.51 | 0.21 | 0.00 | 0.00 | 0.00 |
| collapse | 0.46 | 0.46 | 0.46 | 0.46 | 0.49 | 0.79 | 1.00 | 1.00 | 1.00 |

(Reported fine-mesh values in §S4.3 are 0.399 → 0.240 → 0.0529.) So the recover/collapse **outcome** switches
at the ≈18–20 yr cliff, which lies **inside** the reviewer's 17–33 yr band. A blanket "results unchanged" claim
would be false.

**The mechanism, by contrast, is band-insensitive:**

| `τ_g` (yr) | 17 | 18 | 19 | 20 | 25 | 30 | 33 |
|:--:|---:|---:|---:|---:|---:|---:|---:|
| leading λ | +0.625 | +0.625 | +0.625 | +0.625 | +0.625 | +0.625 | +0.625 |
| Hopf (imag-axis crossing) | none | none | none | none | none | none | none |

The leading eigenvalue is +0.625 (real, positive) for every `τ_g`, and `Re D(iω)` stays ≤0 (no imaginary-axis
crossing) in the scanned range — so the monotone instability, the no-Hopf result, the `R_B=1`
necessary-but-not-sufficient bound, and the silent-collapse signature all hold across the band.

**Corrected sensitivity statement:** the *structural* results are unchanged over `τ_g ∈ [17,33] yr`, while the
*recover-vs-collapse outcome* switches inside it. Because the corrected effective anchor (≈25–33 yr) lies at or
above the collapse threshold, the model's principal prediction — that these regeneration timescales place
forests, soils, and many fisheries in the collapse regime — is supported rather than overturned.

## 5. Bottom line
- Reviewer's **t₅₀ = 1.44·t₅₀ arithmetic**: correct, retained as an effective-timescale heuristic.
- Reviewer's **three recovery values**: two mis-cited (forest, fisheries); corrected to the sourced values.
- Reviewer's **rate/lag mapping**: conflates `ρ` (recovery time) with `τ_g` (recovery type); made explicit not implicit.
- Reviewer's **sensitivity line** ("unchanged over 17–33 yr"): false; replaced by a mechanism-vs-outcome statement.
- **Implemented** as SI §S5.1 ("Illustrative empirical anchoring of the regeneration timescale"), with matching
  corrections in §8 and §6 prediction 6, and a response added under reviewer item (e).
