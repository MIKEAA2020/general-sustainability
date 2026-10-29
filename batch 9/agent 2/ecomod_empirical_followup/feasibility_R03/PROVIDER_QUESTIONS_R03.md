# Evidence questions for provider/author follow-up — R03

Prepared for author review; **not sent**. These questions request evidence rather than assuming corrections or asking the provider to certify our analysis.

## Production uncertainty aggregation

1. E3UB v7 p. 23 prints 1/N and 2/N in the variance-of-average expressions, whereas PVP v6 p. 26 gives the covariance sum divided by N². Which normalization is used in the released v7 aggregation pipeline? Please identify the exact code/version or an implementation specification, including area weighting and treatment of missing/nonforest/zero-valued support.
2. E3UB v7 pp. 24–25, Eqs. 3-17/18, imply decaying correlation; printed Eq. 3-19 increases from zero, unlike the plotted curves. What exact spatial kernel, diagonal/zero-lag convention, coefficient units and truncation are used in production? Is there an erratum? The general covariance identity alone does not identify the intended code repair.
3. Does the production implementation differ from the public Plot2Map validation tool's `SpatCor.R`? Please distinguish native uncertainty propagation, published coarse-map uncertainty aggregation and validation-reference error modelling.

## Native endpoint uncertainty and masks

4. For the same bounded v7 Brazilian window at 2015 and 2023, 1,032 and 946 positive-AGB cells respectively have stored `agb_sd = 0`; their AGB values are 1–4 Mg/ha. What storage quantization, clipping, precision modelling or masking rules can generate those cases? Can source/quality flags distinguish these causes? No cause or zero true error has been assumed here.
5. Which exact land-cover masks/epochs and cropland/evergreen merging exceptions apply to the two selected endpoints and converted land? Are pre-mask estimates or zero-origin flags available? A native variable list without such flags cannot reconstruct this history.
6. The native AGB attribute points to `agb_se`, while the listed uncertainty layer is `agb_sd`. Is that an obsolete ancillary-variable name, and are additional uncertainty fields intended? Please confirm rather than silently relabelling the source.

## Change and zero/NoData conventions

7. The public change script uses the sum of endpoint variances. Is any empirical or model-based final-map cross-year covariance available for 2015–2023, distinct from within-stack C-/L-band correlations and the spatial kernel? Temporal merging/refinement can create dependence; it does not identify its value.
8. The script assigns quality class 0 to both-zero AGB and sets that GeoTIFF band's NoData value to 0, while inspected released coarse NetCDF metadata has fill −32768 and valid classes 0–5. How should users preserve the both-zero category across those representations? What is the intended handling of input fill values? This is not presented as proof of an error in released products.

## AGBref reference provenance

9. The current open v2 export has a local 500 m centroid with N=1, zero minimum/local-representativity/strict flags, and target-epoch labels 2010/2015/2020. Can actual census dates, source-provider identity, original plot identity/reuse and support metadata be made available for compatibility assessment? Neither a shared centroid nor different aggregate IDs establishes repeated field observations.
10. Is there a released reference version with actual observations supporting the 2023 endpoint on this support? The inspected archive has no named 2023 member and its unnamed CSV has no date field. A planned 2025 release is not treated as an available 2023 reference.

These requests do not seek an assumed sign of biomass change, a universal error percentage, an imported correlation of 0.5 or automatic admission of any country.
