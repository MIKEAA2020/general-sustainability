#!/usr/bin/env python3
"""Reproduce the additive Canada NFI route checks without modifying frozen inputs.

Commands are deliberately separate and ordered: static -> compare -> generator ->
measurements. Each command writes a new output snapshot. Optional frozen paths are
read-only. Requires requests and beautifulsoup4 for network/HTML operations.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup

BASE = "https://nfi.nfis.org"
STATIC_BASE = BASE + "/resources/general/summaries/t1/en"
WRT_ENDPOINT = BASE + "/wrt/service"
MEASUREMENT_URL = BASE + "/wrl/resource"
TIMEOUT = 90
TOLERANCE = 0.0050000001


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save_bytes(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def get(url: str, *, params: dict[str, Any] | None = None) -> requests.Response:
    """Use a fresh anonymous request: no credentials or persistent cookie session."""
    response = requests.get(url, params=params, timeout=TIMEOUT)
    return response


def static_names() -> list[tuple[str, str]]:
    names = []
    for scope in ("CA", "NFI"):
        for table in (17, 18):
            for measure in ("change", "stock"):
                for kind in ("", "sep", "intv"):
                    suffix = f"_{kind}" if kind else ""
                    names.append((scope, f"{scope.lower()}_t{table}_forage20_biom_{measure}{suffix}_en"))
    return names


def retrieve_static(output: Path, frozen_static: Path | None) -> None:
    """Retrieve all 24 static biomass CSV/HTML pairs and record their versions."""
    results = []
    for scope, name in static_names():
        record: dict[str, Any] = {
            "scope": scope,
            "name": name,
            "measure": "change" if "_change" in name else "stock",
        }
        for fmt in ("csv", "html"):
            url = f"{STATIC_BASE}/{scope}/{fmt}/{name}.{fmt}"
            response = get(url)
            target = output / scope / fmt / f"{name}.{fmt}"
            save_bytes(target, response.content)
            item: dict[str, Any] = {
                "url": url,
                "status": response.status_code,
                "bytes": len(response.content),
                "sha256": hashlib.sha256(response.content).hexdigest(),
            }
            if fmt == "csv" and frozen_static is not None:
                frozen = frozen_static / f"{name}.csv"
                item["byte_identical_to_frozen"] = bool(
                    frozen.exists() and frozen.read_bytes() == response.content
                )
            record[fmt] = item
        text = response.content.decode("utf-8", errors="replace")
        version = re.search(r"Version\s*([0-9.]+),\s*([A-Za-z]+\s+[0-9]{4})", text)
        record["html"]["version"] = (
            f"{version.group(1)}, {version.group(2)}" if version else "NOT FOUND"
        )
        results.append(record)
        print(scope, name, record["csv"]["status"], record["html"]["status"], record["html"]["version"])
    output.mkdir(parents=True, exist_ok=True)
    (output / "retrieval_results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(
        "SUMMARY",
        "assets=", len(results),
        "csv_200=", sum(x["csv"]["status"] == 200 for x in results),
        "html_200=", sum(x["html"]["status"] == 200 for x in results),
        "frozen_csv_matches=", sum(x["csv"].get("byte_identical_to_frozen", False) for x in results),
    )


def clean_html_number(value: str) -> str:
    # Static stock HTML uses spaced thousands separators; RSE caps carry an asterisk.
    return re.sub(r"[\s,]+", "", value.replace("±", "").replace("*", "")).strip()


def compare_static(input_dir: Path) -> None:
    """Compare 13 numeric columns per data row, allowing only HTML presentation rounding."""
    retrieval_path = input_dir / "retrieval_results.json"
    raw = json.loads(retrieval_path.read_text())
    results = raw["assets"] if isinstance(raw, dict) else raw
    report = []
    for item in results:
        scope, name = item["scope"], item["name"]
        csv_path = input_dir / scope / "csv" / f"{name}.csv"
        html_path = input_dir / scope / "html" / f"{name}.html"
        with csv_path.open(newline="", encoding="utf-8-sig") as handle:
            rows = list(csv.reader(handle))
        csv_rows = [row for row in rows[2:] if len(row) >= 14]
        soup = BeautifulSoup(html_path.read_bytes(), "html.parser")
        html_rows = []
        for tr in soup.find("table").find_all("tr"):
            cells = [c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"])]
            if len(cells) >= 14 and cells[0] not in {"Forest type", "Terrestrial ecozone"}:
                html_rows.append(cells)
        mismatches = []
        compared = 0
        if len(csv_rows) != len(html_rows):
            mismatches.append({"row_count_csv": len(csv_rows), "row_count_html": len(html_rows)})
        for row_index, (csv_row, html_row) in enumerate(zip(csv_rows, html_rows), 1):
            for column_index, (csv_value, html_value) in enumerate(zip(csv_row[-13:], html_row[-13:]), 1):
                compared += 1
                cleaned = clean_html_number(html_value)
                if csv_value in {"None", ""}:
                    matches = cleaned == "-"
                elif cleaned == "-":
                    matches = False
                elif cleaned.startswith("<"):
                    matches = 0 < abs(float(csv_value)) < float(cleaned[1:])
                else:
                    matches = abs(float(cleaned) - float(csv_value)) <= TOLERANCE
                if not matches:
                    mismatches.append({
                        "row": row_index,
                        "column": column_index,
                        "csv": csv_value,
                        "html": html_value,
                    })
        report.append({
            "name": name,
            "scope": scope,
            "csv_rows": len(csv_rows),
            "html_rows": len(html_rows),
            "numeric_cells_compared": compared,
            "mismatches": mismatches,
            "all_match_within_html_rounding": not mismatches,
        })
    summary = {
        "assets": report,
        "all_passed": all(x["all_match_within_html_rounding"] for x in report),
        "total_cells": sum(x["numeric_cells_compared"] for x in report),
        "total_mismatches": sum(len(x["mismatches"]) for x in report),
        "method": {
            "numeric_columns_per_row": 13,
            "missing": "HTML dash aligned to CSV None",
            "rounded_values": f"absolute HTML-CSV difference <= {TOLERANCE}",
            "small_values": "HTML <0.01 accepted only when 0 < abs(CSV) < 0.01",
            "presentation_markers": "Thousands separators, plus-minus and RSE-cap asterisk removed",
        },
    }
    (input_dir / "html_csv_rounding_comparison.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(
        "COMPARISON",
        "assets=", len(report),
        "cells=", summary["total_cells"],
        "mismatches=", summary["total_mismatches"],
        "all_passed=", summary["all_passed"],
    )


def generator_specs() -> list[dict[str, str]]:
    return [
        {"scope": "national", "measure": "point", "dataset": "v_pp_summary_national_en_point"},
        {"scope": "national", "measure": "changes", "dataset": "v_pp_summary_national_en_changes"},
        {"scope": "ecozone", "measure": "changes", "dataset": "v_pp_summary_ecozone_en_changes"},
    ]


def retrieve_generator(output: Path, frozen_generator: Path | None) -> None:
    """Run three public WRT queries; no cookie, token or collaborator login is supplied."""
    output.mkdir(parents=True, exist_ok=True)
    records = []
    for spec in generator_specs():
        params = {
            "SERVICE": "WRT",
            "REQUEST": "GetData",
            "VERSION": "1.0",
            "outputFormat": "application/json",
            "infoFormat": "application/json",
            "dataset": spec["dataset"],
            "lang": "en",
            "filter": 'class_comb_id EQUALS "35"',
            "template": "template_json_en.txt",
        }
        response = get(WRT_ENDPOINT, params=params)
        name = f"wrt_{spec['scope']}_{spec['measure']}_class35_variance.json"
        target = output / name
        save_bytes(target, response.content)
        data = response.json()
        features = data.get("features", [])
        properties = [feature.get("properties", {}) for feature in features]
        record: dict[str, Any] = {
            **spec,
            "endpoint": WRT_ENDPOINT,
            "filter": params["filter"],
            "http_status": response.status_code,
            "rows": len(features),
            "anonymous_credentials_used": False,
            "top_level_properties": sorted(data.keys()),
            "sep_biom_exposed": any("sep_biom" in row for row in properties),
            "var_biom_exposed": any("var_biom" in row for row in properties),
            "snapshot_sha256": sha256(target),
        }
        if frozen_generator is not None:
            frozen_path = frozen_generator / name
            if frozen_path.exists():
                frozen = json.loads(frozen_path.read_text())
                record["data_identical_to_frozen"] = data == frozen
                frozen_properties = [f.get("properties", {}) for f in frozen.get("features", [])]
                record["schema_identical_to_frozen"] = (
                    sorted(data.keys()) == sorted(frozen.keys())
                    and all(sorted(a.keys()) == sorted(b.keys()) for a, b in zip(properties, frozen_properties))
                    and len(properties) == len(frozen_properties)
                )
        records.append(record)
        print(spec["scope"], spec["measure"], response.status_code, len(features), record["sep_biom_exposed"], record["var_biom_exposed"])
    summary = {
        "retrieved_on": datetime.now(timezone.utc).date().isoformat(),
        "authentication": "No cookies, tokens or collaborator login supplied",
        "queries": records,
    }
    (output / "anonymous_recheck.json").write_text(json.dumps(summary, indent=2) + "\n")


def retrieve_measurements(output: Path) -> None:
    """Retrieve the generator's measurement choices; this is not a release-history probe."""
    output.mkdir(parents=True, exist_ok=True)
    params = {
        "namespace": "nfi_web_measurement_numbers",
        "version": "1.0",
        "outputformat": "xml",
        "domain": "nfi",
        "lang": "en",
    }
    response = get(MEASUREMENT_URL, params=params)
    target = output / "pp_measurements.xml"
    save_bytes(target, response.content)
    root = ET.fromstring(response.content)
    measurements = [
        {"name": row.findtext("resources_name", ""), "title": row.findtext("english_title", "")}
        for row in root.findall(".//resource_list")
    ]
    result = {"http_status": response.status_code, "url": response.url, "measurements": measurements, "sha256": sha256(target)}
    (output / "measurement_list.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    static = sub.add_parser("static")
    static.add_argument("--output", type=Path, required=True)
    static.add_argument("--frozen-static", type=Path)
    compare = sub.add_parser("compare")
    compare.add_argument("--input", type=Path, required=True)
    generator = sub.add_parser("generator")
    generator.add_argument("--output", type=Path, required=True)
    generator.add_argument("--frozen-generator", type=Path)
    measurements = sub.add_parser("measurements")
    measurements.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "static":
        retrieve_static(args.output, args.frozen_static)
    elif args.command == "compare":
        compare_static(args.input)
    elif args.command == "generator":
        retrieve_generator(args.output, args.frozen_generator)
    else:
        retrieve_measurements(args.output)


if __name__ == "__main__":
    main()
