# Paper09b v5 source extracts for arithmetic checks

These small CSV extracts are included so that the version-specific checker can verify the printed SSB and reported-landings inputs without downloading PDFs or depending on a machine-local path.

- `ncam_2016_table_a2.csv`: DFO (2016), *Stock Assessment of Northern Cod (NAFO Divs. 2J3KL) in 2016*, Table A2. The `ssb_kt` column is assessed spawning-stock biomass in kilotonnes; it is an assessment output, not a direct measurement.
- `dfo_2025_table1_landings.csv`: Regular et al. (2025), DFO CSAS Research Document 2025/048, Table 1. The `catch_t` column is reported **total landings** in tonnes; it is not relabelled here as all fishing removals.
- `paperE1_calibration_data_v1_ram_timeseries.csv`: RAM Legacy v4.66 database extract for stock `COD2J3KL`, as used in the associated E1 calibration record. Its `SSB` column is in tonnes; the checker divides it by 1,000 to compare in kilotonnes. This later database vintage is kept distinct from both DFO assessment vintages.
- `xtencam_table17_ssb.csv`: Regular et al. (2025), Table 17, reassessment-vintage SSB point values, 95% bands, and rounded SSB-to-B_lim ratios. The checker uses it to reproduce the exhaustive adjacent-band comparisons and selected cross-vintage values.
- `catch_schijns_2021.csv`: Schijns et al. (2021), Table 1, catch reconstruction in tonnes. The checker uses it only to cross-check selected reported-row equalities; equality between reported series does not show that either exhaustively lists removals.

All conversions and threshold calculations are performed with exact rational arithmetic. The extracts are transcription files from the cited sources, not substitutes for the source documents or their uncertainty statements.
