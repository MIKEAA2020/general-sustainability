#!/usr/bin/env python3
"""Offline reproduction of the Canada static-report and N3WRT diagnostics.

Run from any directory:
    python scripts/run_canada_diagnostics.py

Inputs are the public CSV/JSON snapshots in data/. Outputs are written to
evidence/. No uncertainty value is substituted across products or versions.
"""
from __future__ import annotations

import csv
import json
import math
import pathlib
import statistics
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATIC = ROOT / "data" / "canada_static"
WRT = ROOT / "data" / "canada_wrt"
OUT = ROOT / "evidence"
OUT.mkdir(exist_ok=True)
TABLES = ("t15_forage20_vol", "t17_forage20_biom", "t18_lsage20_biom")


def read_csv(path: pathlib.Path) -> list[list[str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.reader(handle))


def national_value(table: str, change: bool, suffix: str) -> float:
    middle = "_change" if change else ""
    rows = read_csv(STATIC / f"ca_{table}{middle}{suffix}_en.csv")
    total_column = rows[1].index("Total")
    row = next(row for row in rows if row and row[0] == "Subtotal")
    return float(row[total_column])


def ecozone_values(table: str, change: bool, suffix: str) -> list[float]:
    middle = "_change" if change else ""
    rows = read_csv(STATIC / f"nfi_{table}{middle}{suffix}_en.csv")
    total_column = rows[1].index("Total")
    return [
        float(row[total_column])
        for row in rows
        if len(row) > 1 and row[1] == "Subtotal" and row[total_column] not in ("None", "")
    ]


def write_csv(path: pathlib.Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"No rows for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def static_diagnostics() -> list[dict]:
    output = []
    for table in TABLES:
        for change in (False, True):
            point = national_value(table, change, "")
            rse = national_value(table, change, "_sep")
            halfwidth = national_value(table, change, "_intv")
            points = ecozone_values(table, change, "")
            rses = ecozone_values(table, change, "_sep")
            halfwidths = ecozone_values(table, change, "_intv")
            if not (len(points) == len(rses) == len(halfwidths)):
                raise AssertionError(f"Aligned ecozone rows differ for {table}, change={change}")
            se_rss = math.sqrt(sum((abs(x) * r / 100) ** 2 for x, r in zip(points, rses)))
            ci_rss = math.sqrt(sum(x * x for x in halfwidths))
            output.append(
                {
                    "table": table,
                    "estimand": "change" if change else "stock",
                    "national_point": point,
                    "ecozone_point_sum": sum(points),
                    "national_rse_percent": rse,
                    "rse_derived_se_rss": se_rss,
                    "rse_rollup_percent_of_national_point": 100 * se_rss / abs(point),
                    "national_ci_halfwidth": halfwidth,
                    "ecozone_ci_halfwidth_rss": ci_rss,
                    "ci_rss_minus_national": ci_rss - halfwidth,
                    "implied_static_multiplier": halfwidth / (abs(point) * rse / 100),
                    "n_ecozone_rows": len(points),
                }
            )
    write_csv(OUT / "canada_static_rollup_summary.csv", output)
    (OUT / "canada_static_rollup_summary.json").write_text(
        json.dumps(output, indent=2), encoding="utf-8"
    )
    return output


def number(value) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return math.nan


def generator_diagnostics() -> tuple[dict, list[dict]]:
    summary = {}
    all_cells = []
    for measure in ("point", "changes"):
        data = json.loads((WRT / f"wrt_national_{measure}_class35_variance.json").read_text())["data"]
        records = []
        for row in data:
            point = float(row[8])
            sep = float(row[9])
            lower = float(row[10])
            upper = float(row[11])
            variance = float(row[12])
            se = math.sqrt(variance) / 1e6
            halfwidth = (upper - lower) / 2
            var_rse = 100 * se / abs(point) if point else None
            records.append(
                {
                    "measure": measure,
                    "forest2": row[2],
                    "forest_type": row[4],
                    "age_class": row[6],
                    "point_million_tonnes": point,
                    "published_sep_biom_percent": sep,
                    "var_biom_tonnes_squared": variance,
                    "se_from_var_biom_million_tonnes": se,
                    "ci_halfwidth_million_tonnes": halfwidth,
                    "generator_interval_multiplier": halfwidth / se if se else None,
                    "var_derived_rse_percent": var_rse,
                    "absolute_rse_difference_percentage_points": abs(var_rse - sep) if var_rse is not None else None,
                }
            )
        multipliers = [r["generator_interval_multiplier"] for r in records if r["generator_interval_multiplier"] and math.isfinite(r["generator_interval_multiplier"])]
        differences = [r["absolute_rse_difference_percentage_points"] for r in records if r["absolute_rse_difference_percentage_points"] is not None]
        matches = [r for r in records if r["absolute_rse_difference_percentage_points"] is not None and r["absolute_rse_difference_percentage_points"] <= 0.02]
        forest = [r for r in records if r["forest2"] == "FOR"]
        forest_point = sum(r["point_million_tonnes"] for r in forest)
        forest_variance = sum(r["var_biom_tonnes_squared"] for r in forest)
        forest_se = math.sqrt(forest_variance) / 1e6
        summary[measure] = {
            "n": len(records),
            "n_forest": len(forest),
            "k_min": min(multipliers),
            "k_median": statistics.median(multipliers),
            "k_max": max(multipliers),
            "rse_matches_within_0_02_percentage_points": len(matches),
            "rse_comparisons": len(differences),
            "forest_point_sum_million_tonnes": forest_point,
            "forest_var_sum_tonnes_squared": forest_variance,
            "forest_se_from_summed_cell_var_million_tonnes": forest_se,
            "forest_var_derived_rse_percent": 100 * forest_se / abs(forest_point),
            "forest_halfwidth_at_1_965_million_tonnes": 1.965 * forest_se,
        }
        all_cells.extend(records)
    write_csv(OUT / "canada_generator_cell_diagnostics.csv", all_cells)
    (OUT / "canada_generator_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    return summary, all_cells


def ecozone_rollup() -> tuple[list[dict], dict]:
    national = json.loads((WRT / "wrt_national_changes_class35_variance.json").read_text())["data"]
    ecozone = json.loads((WRT / "wrt_ecozone_changes_class35_variance.json").read_text())["data"]

    def national_key(row):
        return row[2], row[4], row[6]

    def ecozone_key(row):
        return row[3], row[5], row[7]

    national_by_key = {national_key(row): row for row in national}
    groups = defaultdict(list)
    for row in ecozone:
        groups[ecozone_key(row)].append(row)
    rows = []
    for key in sorted(set(national_by_key) | set(groups)):
        n = national_by_key.get(key)
        es = groups.get(key, [])
        point_sum = sum(number(row[9]) for row in es)
        variance_sum = sum(number(row[13]) for row in es)
        n_point = number(n[8]) if n else math.nan
        n_variance = number(n[12]) if n else math.nan
        rows.append(
            {
                "forest2": key[0],
                "for_type": key[1],
                "ageclass": key[2],
                "n_ecozones": len(es),
                "national_point": n_point,
                "ecozone_point_sum": point_sum,
                "point_diff": point_sum - n_point,
                "national_var": n_variance,
                "ecozone_var_sum": variance_sum,
                "var_ratio_sum_over_national": variance_sum / n_variance if n_variance and math.isfinite(n_variance) else math.nan,
                "var_diff": variance_sum - n_variance,
            }
        )
    write_csv(OUT / "canada_ecozone_to_national_variance_rollup.csv", rows)
    scope = {}
    for name, keys in (
        ("all", set(national_by_key) | set(groups)),
        ("forest", {key for key in set(national_by_key) | set(groups) if key[0] == "FOR"}),
        ("nonforest", {key for key in set(national_by_key) | set(groups) if key[0] != "FOR"}),
    ):
        ns = [national_by_key[key] for key in keys if key in national_by_key]
        es = [row for key in keys for row in groups.get(key, [])]
        national_variance = sum(number(row[12]) for row in ns)
        ecozone_variance = sum(number(row[13]) for row in es)
        scope[name] = {
            "national_cells": len(ns),
            "ecozone_cells": len(es),
            "national_point_sum": sum(number(row[8]) for row in ns),
            "ecozone_point_sum": sum(number(row[9]) for row in es),
            "national_var_sum": national_variance,
            "ecozone_var_sum": ecozone_variance,
            "var_ratio": ecozone_variance / national_variance,
            "national_se_million_tonnes": math.sqrt(national_variance) / 1e6,
            "ecozone_se_million_tonnes": math.sqrt(ecozone_variance) / 1e6,
        }
    scope["missing_national_keys"] = len(set(groups) - set(national_by_key))
    scope["missing_ecozone_keys"] = len(set(national_by_key) - set(groups))
    (OUT / "canada_ecozone_rollup_scope_summary.json").write_text(
        json.dumps(scope, indent=2), encoding="utf-8"
    )
    return rows, scope


def assertions(static: list[dict], generator: dict, rollup: list[dict], scope: dict) -> dict:
    t17_change = next(r for r in static if r["table"] == "t17_forage20_biom" and r["estimand"] == "change")
    checks = {
        "static_table_17C0_point_rse_halfwidth_preserved": (
            t17_change["national_point"] == 17.639
            and t17_change["national_rse_percent"] == 1.16
            and t17_change["national_ci_halfwidth"] == 38.918
        ),
        "static_table_17C0_fields_are_not_a_1_96_interval": not math.isclose(t17_change["implied_static_multiplier"], 1.96, rel_tol=0.01),
        "all_static_ecozone_ci_rss_match_national_to_0_001": all(abs(r["ci_rss_minus_national"]) < 0.001 for r in static),
        "all_stock_rse_rollups_match_national_to_0_02_pp": all(abs(r["rse_rollup_percent_of_national_point"] - r["national_rse_percent"]) < 0.02 for r in static if r["estimand"] == "stock"),
        "all_change_rse_rollups_fail_by_more_than_4_pp": all(abs(r["rse_rollup_percent_of_national_point"] - r["national_rse_percent"]) > 4 for r in static if r["estimand"] == "change"),
        "generator_has_58_national_cells": generator["changes"]["n"] == 58,
        "generator_stock_rse_variance_match_count_53_of_57": generator["point"]["rse_matches_within_0_02_percentage_points"] == 53 and generator["point"]["rse_comparisons"] == 57,
        "generator_change_rse_variance_match_count_1_of_57": generator["changes"]["rse_matches_within_0_02_percentage_points"] == 1 and generator["changes"]["rse_comparisons"] == 57,
        "all_58_ecozone_to_national_variances_are_additive": len(rollup) == 58 and all((math.isclose(r["ecozone_var_sum"], r["national_var"], rel_tol=1e-9, abs_tol=1e-6) or (r["ecozone_var_sum"] == 0 and r["national_var"] == 0)) for r in rollup),
        "no_missing_ecozone_or_national_keys": scope["missing_national_keys"] == 0 and scope["missing_ecozone_keys"] == 0,
        "current_generator_forest_change_is_not_static_table_17C0": math.isclose(generator["changes"]["forest_point_sum_million_tonnes"], 19.066, abs_tol=1e-9) and not math.isclose(generator["changes"]["forest_point_sum_million_tonnes"], t17_change["national_point"]),
    }
    result = {"all_passed": all(checks.values()), "checks": checks}
    (OUT / "canada_diagnostic_assertions.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    if not result["all_passed"]:
        raise AssertionError(json.dumps(result, indent=2))
    return result


def main() -> None:
    static = static_diagnostics()
    generator, _ = generator_diagnostics()
    rollup, scope = ecozone_rollup()
    result = assertions(static, generator, rollup, scope)
    print(json.dumps({"all_passed": result["all_passed"], "n_checks": len(result["checks"])}, indent=2))
    print(json.dumps(generator, indent=2))


if __name__ == "__main__":
    main()
