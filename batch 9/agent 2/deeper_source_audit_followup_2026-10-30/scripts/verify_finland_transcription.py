#!/usr/bin/env python3
"""Independently compare the Appendix A CSV with numeric rows in PDF text."""
from __future__ import annotations

import csv
import hashlib
import json
import pathlib
import re
import sys

EXPECTED = {"A2": 11, "A3": 5, "A4": 5, "A5": 12}
NUMBER = re.compile(r"(?<![\d.])-?\d+\.\d+(?![\d.])")


def source_rows(text: str, table: str) -> list[list[str]]:
    start = re.search(rf"Taulukko A\s*{table[1:]}\.", text)
    if not start:
        raise ValueError(f"Table {table} start not found")
    if table in {"A2", "A3", "A4"}:
        end = re.search(rf"Taulukko A\s*{int(table[1:]) + 1}\.", text[start.end():])
        stop = start.end() + end.start() if end else len(text)
    else:
        end = text.find("Kuva A1.", start.end())
        stop = end if end >= 0 else len(text)
    result = []
    for line in text[start.end():stop].splitlines():
        values = NUMBER.findall(line)
        if values:
            result.append(values)
    if len(result) != EXPECTED[table]:
        raise ValueError(f"Table {table}: expected {EXPECTED[table]} numeric rows, found {len(result)}")
    return result


def main(report6_text: pathlib.Path, report12_text: pathlib.Path, csv_path: pathlib.Path, destination: pathlib.Path):
    with csv_path.open(newline="", encoding="utf-8") as handle:
        csv_rows = list(csv.DictReader(handle))
    result = {"csv_rows": len(csv_rows), "editions": {}}
    for edition, path in [("6/2026", report6_text), ("12/2026", report12_text)]:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        expected = []
        for table in ["A2", "A3", "A4", "A5"]:
            expected.extend({"table": table, "values": row} for row in source_rows(text, table))
        flattened = [(item["table"], value) for item in expected for value in item["values"]]
        actual = [(row["table"], row["value"]) for row in csv_rows]
        mismatches = [{"index": i, "source": source, "csv": csv_value} for i, (source, csv_value) in enumerate(zip(flattened, actual)) if source != csv_value]
        if len(flattened) != len(actual):
            raise ValueError(f"Length mismatch: source {len(flattened)}, CSV {len(actual)}")
        result["editions"][edition] = {
            "source_text": str(path),
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "numeric_cells_compared": len(actual),
            "mismatches": mismatches,
            "all_match": not mismatches,
        }
    result["all_passed"] = all(item["all_match"] for item in result["editions"].values())
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise SystemExit("Usage: verify_finland_transcription.py REPORT6_TXT REPORT12_TXT EXAMPLES_CSV DESTINATION_JSON")
    main(*(pathlib.Path(value) for value in sys.argv[1:]))
