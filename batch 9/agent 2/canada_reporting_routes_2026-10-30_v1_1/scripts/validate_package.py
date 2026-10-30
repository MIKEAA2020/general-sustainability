#!/usr/bin/env python3
"""Offline integrity and completeness checks for the Canada route supplement."""
from __future__ import annotations

import ast
import csv
import hashlib
import importlib.util
import json
import re
import urllib.parse
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
E = ROOT / "evidence"
checks: list[dict[str, object]] = []


def check(name: str, condition: bool, detail: object = "") -> None:
    checks.append({"name": name, "passed": bool(condition), "detail": detail})


def load(name: str):
    return json.loads((E / name).read_text())


static = load("static_biomass_retrieval.json")
comparison = load("html_csv_rounding_comparison.json")
anonymous = load("anonymous_generator_recheck.json")
reproduction = load("reproduction_v1_1_generator_test.json")
assessment = load("route_assessment.json")
assets = static["assets"]

check("24 static asset pairs", static["asset_count"] == 24 == len(assets), len(assets))
check("all static CSV routes HTTP 200", sum(x["csv"]["status"] == 200 for x in assets) == 24)
check("all static HTML routes HTTP 200", sum(x["html"]["status"] == 200 for x in assets) == 24)
check("all static CSVs frozen-byte identical", sum(x["csv"]["byte_identical_to_frozen"] for x in assets) == 24)
change = [x for x in assets if x["measure"] == "change"]
stock = [x for x in assets if x["measure"] == "stock"]
check("12 November 2025 change tables", len(change) == 12 and all(x["html"]["version"] == "3.1, November 2025" for x in change))
check("12 October 2025 stock tables", len(stock) == 12 and all(x["html"]["version"] == "3.1, October 2025" for x in stock))

supplied = next(x for x in assets if x["name"] == "ca_t17_forage20_biom_change_en")
check("supplied CSV hash", supplied["csv"]["sha256"] == "172ed30d9d3a6c183eed492c7b1a9bcadab824474791478fe2ac7f7576716961")
check("supplied HTML hash", supplied["html"]["sha256"] == "24d339ba6fa919a55ba6acd11449c38933e5df7768b288120c90f3093df6dba9")
check("supplied CSV frozen-byte identical", supplied["csv"]["byte_identical_to_frozen"] is True)

check("24 comparison assets", len(comparison["assets"]) == 24)
check("comparison and retrieval asset sets agree", {x["name"] for x in comparison["assets"]} == {x["name"] for x in assets})
check("18,330 cells compared", comparison["total_cells"] == 18330 == sum(x["numeric_cells_compared"] for x in comparison["assets"]), comparison["total_cells"])
check("zero HTML/CSV mismatches", comparison["total_mismatches"] == 0 and comparison["all_passed"] is True)
check("rounding method registered", comparison["method"]["numeric_columns_per_row"] == 13 and "<0.01" in comparison["method"]["small_values"])

queries = anonymous["queries"]
check("three anonymous generator queries", len(queries) == 3)
check("all generator queries HTTP 200", all(x["http_status"] == 200 for x in queries))
check("sep_biom exposed in every query", all(x["sep_biom_exposed"] for x in queries))
check("var_biom exposed in every query", all(x["var_biom_exposed"] for x in queries))
check("no anonymous credentials used", all(x["anonymous_credentials_used"] is False for x in queries))
expected_rows = {("national", "point"): 58, ("national", "changes"): 58, ("ecozone", "changes"): 550}
check("generator row counts", {(x["scope"], x["measure"]): x["rows"] for x in queries} == expected_rows)
check("generator data frozen identical", all(x["data_identical_to_frozen"] for x in queries))
check("generator schemas frozen identical", all(x["schema_identical_to_frozen"] for x in queries))

reproduction_queries = reproduction["queries"]
check("v1.1 live regression has three queries", len(reproduction_queries) == 3)
check("v1.1 live regression HTTP 200", all(x["http_status"] == 200 for x in reproduction_queries))
check("v1.1 live regression row counts", {(x["scope"], x["measure"]): x["rows"] for x in reproduction_queries} == expected_rows)
check("v1.1 observed array payload", all(x["payload_structure"] == "title/name/data" for x in reproduction_queries))
check("v1.1 fields present in every row", all(x["sep_biom_exposed"] and x["var_biom_exposed"] for x in reproduction_queries))
check("v1.1 data and schemas frozen identical", all(x["data_identical_to_frozen"] and x["schema_identical_to_frozen"] for x in reproduction_queries))
check("v1.1 anonymous queries", all(x["anonymous_credentials_used"] is False for x in reproduction_queries))
expected_snapshot_hashes = {
    ("national", "point"): "707147ed6a4d097f4a212a92b80c62e4c0b0ea97266e7fcbddb5a7ce5257881d",
    ("national", "changes"): "2c666e35263ce29ba6e9a38808a8625cabbbe5abf07de91f2a6276181d06a57d",
    ("ecozone", "changes"): "01d3be837556303b42c055a96b176f72a0a9e6b3275ce7da8f2686abb821adbf",
}
check("v1.1 response bytes frozen identical", {(x["scope"], x["measure"]): x["snapshot_sha256"] for x in reproduction_queries} == expected_snapshot_hashes)

check("legacy route registered as 404", assessment["legacy_generator"]["http_status"] == 404)
check("current generator route registered as 200", assessment["current_generator_page"]["http_status"] == 200)
check("reported CSV fault not reproduced", assessment["reported_csv_misconfiguration_reproduced"] is False)
check("static raw var_biom not claimed public", assessment["static_var_biom_exposed"] is False)
check("static precision preserved", assessment["corresponding_static_csv"]["national_total_full_precision_million_tonnes"] == 17.639)
check("HTML rounded total distinguished", assessment["user_supplied_static_html"]["national_total_displayed_million_tonnes"] == 17.64)
check("no static-release selector claimed", assessment["generator_release_selection"]["static_release_selector_found"] is False)
check("measurement choices limited to point and changes", {x["name"] for x in assessment["generator_release_selection"]["measurements"]} == {"point", "changes"})
check("provider request narrowly targeted", "static-run" in assessment["data_request"]["appropriate_remaining_use"])
check("static/current version boundary stated", "17.639" in assessment["version_boundary"] and "19.066" in assessment["version_boundary"])

with (E / "source_files.csv").open(newline="", encoding="utf-8") as handle:
    sources = list(csv.DictReader(handle))
counts = Counter(x["route"] for x in sources)
expected_counts = {
    "static_biomass": 48,
    "anonymous_generator": 3,
    "anonymous_generator_v1_1": 3,
    "standard_reports": 1,
    "customized_report": 1,
    "data_and_tools": 1,
    "data_request": 1,
    "generator_javascript": 1,
    "measurement_list": 1,
    "legacy_reportgenerator": 1,
}
check("61-source registry", len(sources) == 61 and dict(counts) == expected_counts, dict(counts))
check("source registry unique keys", len({(x["route"], x["name"], x["format"]) for x in sources}) == 61)
check("source registry hashes", all(re.fullmatch(r"[0-9a-f]{64}", x["sha256"]) for x in sources))
check("source registry statuses", all(int(x["http_status"]) == (404 if x["route"] == "legacy_reportgenerator" else 200) for x in sources))
check("source registry sizes", all(int(x["bytes"]) > 0 for x in sources))
check("generator registry hashes agree", all(x["snapshot_sha256"] == next(s["sha256"] for s in sources if s["route"] == "anonymous_generator" and s["name"] == x["scope"] + "_" + x["measure"]) for x in queries))
check("v1.1 registry hashes agree", all(x["snapshot_sha256"] == next(s["sha256"] for s in sources if s["route"] == "anonymous_generator_v1_1" and s["name"] == x["scope"] + "_" + x["measure"]) for x in reproduction_queries))

for relative in ("scripts/reproduce_route_checks.py", "scripts/validate_package.py"):
    try:
        ast.parse((ROOT / relative).read_text())
        check(relative + " parses", True)
    except SyntaxError as error:
        check(relative + " parses", False, str(error))

module_path = ROOT / "scripts/reproduce_route_checks.py"
spec = importlib.util.spec_from_file_location("route_reproduction_v1_1", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
query_shapes = []
for item in module.generator_specs():
    query = module.build_generator_query(item)
    gdas = urllib.parse.parse_qs(urllib.parse.urlsplit(query["gdasUrl"]).query)
    query_shapes.append(
        gdas.get("DatasetName") == [item["dataset"]]
        and "sep_biom" in gdas.get("Attribute", [""])[0]
        and "var_biom" in gdas.get("Attribute", [""])[0]
        and query["filterClause"] == 'class_comb_id EQUALS "35"'
        and query["templateUrl"].endswith("n3wrt_classifiers_list_tmp.txt")
    )
check("v1.1 GDAS-to-WRT query builder", all(query_shapes) and len(query_shapes) == 3)
rows, structure = module.parse_wrt_payload({"title": ["RSE", "Variance"], "name": ["sep_biom", "var_biom"], "data": [["1.2", "3.4"]]})
check("v1.1 NFI array parser fixture", structure == "title/name/data" and rows == [{"sep_biom": "1.2", "var_biom": "3.4"}])
geo_rows, geo_structure = module.parse_wrt_payload({"features": [{"properties": {"sep_biom": "1.2", "var_biom": "3.4"}}]})
check("v1.1 GeoJSON fallback fixture", geo_structure == "GeoJSON features" and geo_rows[0]["var_biom"] == "3.4")
try:
    module.parse_wrt_payload({"unexpected": []})
    unrecognized_rejected = False
except ValueError:
    unrecognized_rejected = True
check("v1.1 unrecognized payload rejected", unrecognized_rejected)
check("v1.1 empty live response rejected", "if not properties:" in module_path.read_text() and "raise RuntimeError" in module_path.read_text())

readme = (ROOT / "README.md").read_text()
for label, needle in {
    "README static precision": "17.639",
    "README current generator boundary": "19.066",
    "README cell comparison": "18,330/18,330",
    "README current generator URL": "https://nfi.nfis.org/en/customized_report",
    "README data request": "nfisupport@nfis.org",
    "README no uncertainty selection": "does not select between their uncertainties",
    "README v1.1 correction disclosed": "reproduction-code defect",
    "README corrected request chain": "GDAS→WRT",
    "README expanded source registry": "61 retrieved responses",
}.items():
    check(label, needle in readme)

excluded = {"evidence/package_manifest.csv", "evidence/package_qa.json", "publication_receipt.json"}
payload = sorted(
    p for p in ROOT.rglob("*")
    if p.is_file() and p.relative_to(ROOT).as_posix() not in excluded and "__pycache__" not in p.parts and p.suffix != ".pyc"
)
check("payload contains no provider PDFs", not any(p.suffix.lower() == ".pdf" for p in payload))
texts = {p.relative_to(ROOT).as_posix(): p.read_text(encoding="utf-8") for p in payload}
sandbox_needle = "sandbox" + ":"
check("payload contains no sandbox links", not any(sandbox_needle in text for text in texts.values()))
secret_patterns = [r"github" + r"_pat_[A-Za-z0-9_]{10,}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----", r"GITHUB" + r"_PAT=[^\s]+"]
check("payload contains no credential material", not any(re.search(pattern, text) for pattern in secret_patterns for text in texts.values()))
workspace_needle = "/home" + "/user"
check("payload has no hardcoded workspace paths", not any(workspace_needle in text for text in texts.values()))

manifest_path = E / "package_manifest.csv"
if manifest_path.exists():
    with manifest_path.open(newline="", encoding="utf-8") as handle:
        manifest = list(csv.DictReader(handle))
    expected = {p.relative_to(ROOT).as_posix(): p for p in payload}
    check("manifest payload path set", {x["path"] for x in manifest} == set(expected), len(manifest))
    check("manifest payload hashes", all(row["sha256"] == hashlib.sha256(expected[row["path"]].read_bytes()).hexdigest() and int(row["bytes"]) == expected[row["path"]].stat().st_size for row in manifest))
else:
    check("manifest pending", True, "Manifest is generated after the first validation pass")

result = {
    "package": "canada_reporting_routes_2026-10-30_v1_1",
    "checks_run": len(checks),
    "checks_passed": sum(bool(x["passed"]) for x in checks),
    "checks_failed": sum(not bool(x["passed"]) for x in checks),
    "all_passed": all(bool(x["passed"]) for x in checks),
    "checks": checks,
}
(E / "package_qa.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: result[k] for k in ("checks_run", "checks_passed", "checks_failed", "all_passed")}, indent=2))
if not result["all_passed"]:
    for item in checks:
        if not item["passed"]:
            print("FAILED", item)
    raise SystemExit(1)
