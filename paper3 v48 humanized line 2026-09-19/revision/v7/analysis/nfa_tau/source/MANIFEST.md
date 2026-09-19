# The two edition tables, as fetched

Nothing here is redistributed by the author of the study. Both files are copies of what Global Footprint
Network deposited for public download, kept only so that the recomputation beside this directory can be re-run
without a network, and they must be re-fetched from the named deposits before any onward sharing.

| file | what it is | sha256 of the bytes as read | size |
|---|---|---|---|
| `NFA_2018_edition_kaggle.csv` | the 2018 Edition of the National Footprint and Biocapacity Accounts, series 1961–2014, delivered by Kaggle's dataset-download endpoint as a bare CSV (the deposit holds the table, not an archive) | `60968f7c9959537f8e67f915aca4259662b5cd42c3a0ec02d094677b4c280ef6` | 11,857,080 B |
| `NFA_2017_edition_kaggle.zip` | the 2017 Edition deposit, a zip holding two members: `NFA 2017 Edition.csv` (series 1961–2013, the one the analysis reads) and `EF_GDP(constant2010USD).csv` (a Footprint-per-GDP series, unused here) | archive `55474f1ac3f8a29c18844744cfa77f58c3561bbb2a2e3f8c43c4d7da19babc10`; extracted CSV `0dd766d975cd5e85f2a2d39cff1f914b92c514186ce507cb1f721a63be57b6a5`, 13,195,855 B | 4,639,839 B |

Both editions are **CC BY-SA 4.0** per the deposits' own licence fields. Attribution as the deposits request:
Global Footprint Network.

## Retrieval, exactly as it was done

```
curl -sfL -o "NFA_2018_edition_kaggle.csv" \
  https://www.kaggle.com/api/v1/datasets/download/footprintnetwork/national-footprint-accounts-2018
curl -sfL -o "NFA_2017_edition_kaggle.zip" \
  https://www.kaggle.com/api/v1/datasets/download/kingburrito666/national-footprint-accounts
```

`recompute_tau.py` takes either a CSV or the archive; zip members are extracted to `../.cache/` and the
checksum recorded in `../checksums.txt` is that of the **extracted CSV**, which is why the name in that file ends
`.zip.csv`. Re-hashing the extracted member after a fresh run should reproduce `0dd766d9…`, which is the check
that the copy on disk is the copy that was analysed.

## Why these two, and not the current release

The current edition (the 2026 Public Data Package at the time of writing) is free but distributed through a
registration form with an emailed link, so no script can fetch it unattended; the publisher's API endpoints
(`data.footprintnetwork.org`, the FoDaFo `SimpleQuery` service, data.world) either moved behind registration or
no longer serve these tables, and data.world's listing is itself the 2018 edition. These two deposits are
therefore the newest *openly fetchable, component-level* releases, which is what a two-convention recomputation
needs: the per-year world rows for `BiocapTotGHA` and `EFConsTotGHA` with all six demand components and the five
biocapacity components. A neighbouring Kaggle deposit (`jainaru/global-ecological-footprint-2023`) was examined
and rejected: it is a single-year per-capita component table with no year column and no pinnable edition, so it
cannot support a claim about a release.

Consequence for any number quoted from this analysis: the release is 2018, whose series ends in 2014. A
published headline for a later year (the 2022 Overshoot Day, for instance) cannot be reproduced from these bytes;
what can be reproduced is the *behaviour* of the two conventions, and that is what the companion commentary and
the article's Remark 37 use.
