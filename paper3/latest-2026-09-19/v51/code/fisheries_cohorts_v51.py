r"""Recompute the ADH summaries used in Section 6.5.2 and supplementary S5.

This is arithmetic on the three cohort files in ``../data``: cohort medians,
the archived file's internal ADH formula check, the v4.66 taxonomic summary,
the archived/public identifier overlap, and an exact finite-population
random-draw benchmark.  It does not rebuild or reclassify the RAM Legacy
source data.

Run from this directory:
    python3 fisheries_cohorts_v51.py
"""
from __future__ import annotations

import csv
import math
import statistics
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
FILES = (
    ("archived 43-stock cohort", DATA / "fisheries_adh_archived_43.csv", "ADH_yr"),
    ("RAM Legacy v4.44 cohort", DATA / "ram_legacy_v444_adh_cohort.csv", "ADH"),
    ("RAM Legacy v4.66 broad cohort", DATA / "ram_legacy_v466_adh_cohort.csv", "ADH"),
)

print("%-32s %8s %10s %16s %16s" % ("cohort", "n", "ADH=0", "median ADH", "rounded"))
for label, path, column in FILES:
    with path.open(newline="", encoding="utf-8") as handle:
        values = [float(row[column]) for row in csv.DictReader(handle)]
    median = statistics.median(values)
    print("%-32s %8d %10d %16.6f %16.2f"
          % (label, len(values), sum(v == 0.0 for v in values), median, median))

print()
print("The zero count uses the stored ADH value; no stock assessment is rerun here.")

# Archived-file internal consistency: stored ADH against the displayed formula.
archived_path = DATA / "fisheries_adh_archived_43.csv"
with archived_path.open(newline="", encoding="utf-8") as handle:
    archived_rows = list(csv.DictReader(handle))
max_abs_error = 0.0
for row in archived_rows:
    calculated = max(
        0.0,
        math.log(float(row["SSB"]) / float(row["B_lim"])) / float(row["F"]),
    )
    max_abs_error = max(max_abs_error, abs(calculated - float(row["ADH_yr"])))
archived_values = [float(row["ADH_yr"]) for row in archived_rows]
archived_median = statistics.median(archived_values)
print()
print("Archived ADH formula check: max |stored - max(0, log(SSB/B_lim)/F)| = %.3g"
      % max_abs_error)

# v4.66 taxonomic summary and the exact identifier overlap with the archive.
v466_path = DATA / "ram_legacy_v466_adh_cohort.csv"
with v466_path.open(newline="", encoding="utf-8") as handle:
    v466_rows = list(csv.DictReader(handle))
by_group = defaultdict(list)
for row in v466_rows:
    by_group[row["taxGroup"]].append(float(row["ADH"]))
print()
print("RAM Legacy v4.66 taxonomic ADH summary")
print("%-26s %6s %8s %14s %18s %12s"
      % ("group", "n", "ADH=0", "median", "median positives", "max"))
for group, values in sorted(by_group.items(), key=lambda item: -statistics.median(item[1])):
    positives = [value for value in values if value > 0.0]
    print("%-26s %6d %8d %14.4f %18.4f %12.1f"
          % (group, len(values), sum(value == 0.0 for value in values),
             statistics.median(values), statistics.median(positives), max(values)))
archived_ids = {row["stock"] for row in archived_rows}
v466_ids = {row["stockid"] for row in v466_rows}
print()
print("Exact archived-stock identifiers also present in v4.66 cohort: %d of %d"
      % (len(archived_ids & v466_ids), len(archived_ids)))


def draw_median_tail_probability(pool, sample_size, threshold):
    """Exact P(median of a without-replacement draw <= threshold).

    For odd sample_size=2r+1, this is the hypergeometric event that at
    least r+1 sampled values are <= threshold.
    """
    population = len(pool)
    successes = sum(value <= threshold for value in pool)
    needed = sample_size // 2 + 1
    probability = sum(
        Fraction(
            math.comb(successes, k) * math.comb(population - successes, sample_size - k),
            math.comb(population, sample_size),
        )
        for k in range(needed, min(successes, sample_size) + 1)
    )
    return successes, probability

print()
print("Exact 43-stock random-draw benchmark at the archived median %.10f" % archived_median)
for label, pool in (
    ("v4.66 broad cohort", [float(row["ADH"]) for row in v466_rows]),
    ("v4.66 forage-fish group", by_group["forage fish"]),
):
    successes, probability = draw_median_tail_probability(pool, 43, archived_median)
    print("  %-24s pool n=%3d, values <= threshold=%3d, P(sample median <= threshold) = %.6f%%"
          % (label, len(pool), successes, 100.0 * float(probability)))
