# Recomputation: τ_agg with carbon demand excluded, on the accounts as they can be downloaded

Runs the main text's Section 10.2 arithmetic twice on the same component totals — once with carbon demand in
the ratio set (the published convention) and once with carbon demand dropped and the weights renormalised over
the five components of positive biocapacity — and then repeats both on a second, earlier edition of the
accounts, so that the *revision* contribution to any published-vs-recomputed gap is measured rather than
asserted. ## Files

| file | contents |
|---|---|
| `recompute_tau.py` | the arithmetic; no network, no interpolation, no model |
| `tau_by_year_2018edition.csv` | per-year world totals, component ratios, and both conventions on the 2018 edition |
| `tau_by_year_2017edition.csv` | the same on the 2017 edition |
| `edition_delta.csv` | year-by-year 2018-minus-2017 differences for each convention |
| `results.txt` | the complete stdout of the run reported below |
| `checksums.txt` | sha256 of the two input tables, as read |
| `source/` | the two tables as fetched, plus `source/MANIFEST.md` with the retrieval commands, the licence, the archive and member hashes, and why the current edition is not fetched |

## Data provenance

Both editions are the ones Global Footprint Network deposited under a free licence on Kaggle, which is the only
route by which these tables can be fetched **without registration**:

- `NFA 2018.csv` — *National Footprint Accounts 2018*, Global Footprint Network on Kaggle
  (`footprintnetwork/national-footprint-accounts-2018`), licence **CC BY-SA 4.0**, 11,857,080 B,
  sha256 `60968f7c9959537f8e67f915aca4259662b5cd42c3a0ec02d094677b4c280ef6`, years 1961–2014.
- `NFA 2017 Edition.csv` — the same publisher's *National footprint accounts* deposit
  (`kingburrito666/national-footprint-accounts`), 13,229,220 B,
  sha256 `0dd766d975cd5e85f2a2d39cff1f914b92c514186ce507cb1f721a63be57b6a5`, years 1961–2013.

The 2018 edition is the release Lin et al. (2018) documents, which is the citation the main text's exhibit
already carries. **The current edition of the accounts (2025 or 2026) is not openly fetchable**: Global
Footprint Network distributes it as a "Public Data Package" behind a registration form, and its Ecological
Footprint Explorer requires an account. So this computation is *not* on the current release, and the analysis
says so where its conclusions are stated; it is on the newest edition obtainable without an account, with the
preceding edition used as the revision control. Re-running on a newer table is a configuration change, not a
code change:

```
python3 recompute_tau.py --nfa18 "NFA 2025 Edition.csv" --nfa17 "NFA 2024 Edition.csv" --out .
```

The script needs only the columns `record`, `country`, `year`, `crop_land`, `grazing_land`, `forest_land`,
`fishing_ground`, `built_up_land`, `carbon`, and the rows `record ∈ {BiocapTotGHA, EFConsTotGHA}`, which every
edition in this series has carried.

## The one methodological trap this directory exists to document

The release carries a `World` aggregate row per year *and* the national rows in the same table. Summing the
component columns over all rows — the natural first attempt — includes the `World` row among the countries and
doubles both sides of every ratio. The date is not invariant to that error: on the 2018 edition it moved
216.5 d to 223.5 d, a **7-day** shift, which is larger than the four-day difference the main text discusses as
an apparent disagreement. Summing only the national rows lands 1% above the publisher's aggregate, and that
1% is also worth about a week in the date.

Everything reported here therefore uses the publisher's `World` row, prints the alternative as a diagnostic, and
keeps the difference visible.

## What the run found

1. **The premium's downward trend survives the exclusion.** With carbon demand removed, the restricted premium
   on the 2018 edition runs 524 d (1961) → 323 d (1980) → 230 d (2000) → 179 d (2014); decade means fall
   monotonically 464 → 358 → 288 → 253 → 216 → 191 d, with 45 of 53 year-on-year changes negative (85%). The
   main text's series, read off a later edition, is 547 / 346 / 251 / 173 d — the same sign and shape, 4–8%
   above this release on the shared years. So the claim that the components converge is not an artefact of
   keeping carbon in the ratio set, and the release difference is itself a further instance of the point.
2. **The two conventions separate by about a year, mechanically.** Over the last decade of the release
   (2005–2014) the restricted date exceeds the published-convention date by 340.8 d on average (327–348 d,
   i.e. 0.93 yr), a ratio of 2.41 to 2.60, and that ratio is exactly `1/(1 − carbon share)` to 4·10⁻¹⁶ —
   maximum deviation `4.44e-16` over the ten years. The carbon share of demand runs 58.6% to 61.6% in the same
   decade.
3. **The restricted date is the fragile one, not the aggregate date.** Between the 2017 and 2018 editions the
   published-convention date moves by 1.1 d on average and 1.9 d at most, while the restricted date moves by
   6.3 d on average and 9.1 d at most (largest in 1987, 1989, 1991) — a factor of about 5.8. That measures the
   revision of a closed year across one edition step, the smallest vintage effect available. Set the main text's
   four-day difference against it: it is *larger* than any one-edition revision of the aggregate date measured
   here (at most 1.9 d), so a mature-year revision does not account for it, and it is *smaller* than the spread
   produced by the choice of aggregation level alone (7 d, above) and than the restricted date's own revision
   noise (6.3 d mean). The accurate description of such a gap is therefore "vintage, nowcasting, and the level
   at which the accounts are aggregated", not arithmetic — and the third of those is not a data-vintage matter
   at all, which is why the main text needed a clause added.
4. **A structural fact about the world aggregate that the display does not announce.** At the world level
   `r_crop = r_built-up = 1` in **54 of 54** years, exactly and not approximately: the world footprint of a
   component whose demand is the area itself is priced at world-average yields, so biocapacity and demand
   coincide by construction. The consequence is that the restricted minimum `τ_min` is pinned at 365 d in
   54 of 54 years — so the restricted premium is not measuring dispersion among components at the world level,
   it is measuring the distance of the aggregate date past the year boundary, which is the same quantity the
   second finding gives by a different route.

## Reproducing

```
python3 recompute_tau.py > results.txt                      # reads source/, writes here
python3 recompute_tau.py --nfa18 "NFA 2025 Edition.csv" --nfa17 "NFA 2024 Edition.csv"
```

With no arguments the run uses the two tables under `source/` and needs no network; a fresh run on them
reproduces `tau_by_year_2018edition.csv`, `tau_by_year_2017edition.csv` and `edition_delta.csv` byte for byte,
which is the check recorded in the results of 17 September 2026. Zip members are extracted to `.cache/` and
hashed as extracted.
