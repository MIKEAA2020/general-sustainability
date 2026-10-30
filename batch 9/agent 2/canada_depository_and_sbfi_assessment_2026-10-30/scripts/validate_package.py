#!/usr/bin/env python3
"""Offline integrity checks for the Canada depository and SBFI assessment."""
from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
E = ROOT / "evidence"
checks = []


def check(name, condition, detail=""):
    checks.append({"name": name, "passed": bool(condition), "detail": detail})


def load(name):
    return json.loads((E / name).read_text())


search = load("depository_search_assessment.json")
repo = load("github_repository_audit.json")
snapshots = load("published_current_generator_snapshots.json")
sbfi = load("sbfi_zenodo_assessment.json")
schema179 = load("sbfi_schema.json")
schema705 = load("sbfi_schema_tile705.json")
inventory = load("sbfi_zip_inventory.json")

check("three public current-generator snapshots", len(snapshots) == 3)
check("public snapshots HTTP 200", all(x["http_status"] == 200 for x in snapshots))
expected_rows = {"wrt_national_point_class35_variance.json": 58, "wrt_national_changes_class35_variance.json": 58, "wrt_ecozone_changes_class35_variance.json": 550}
check("public snapshot row counts", {x["name"]: x["rows"] for x in snapshots} == expected_rows)
check("public snapshots contain both fields", all(x["var_biom_present"] and x["sep_biom_present"] for x in snapshots))
check("public snapshots frozen-byte identical", all(x["byte_identical_to_frozen_local"] and x["remote_sha256"] == x["local_sha256"] for x in snapshots))
check("public snapshots not mislabelled static", all("not static" in x["scope"] for x in snapshots))

check("named repository commit pinned", repo["commit"] == "5ec0687a9813f384b8ad76c3a10f0982a52f617c")
check("named repository tree complete", repo["tree_entries"] == 15 and repo["blob_count"] == 14 and repo["tree_truncated"] is False)
check("named repository has ten R scripts", repo["r_script_count"] == 10)
check("named repository contains no data files", repo["data_files_in_tree"] == [])
terms = repo["term_occurrences_across_readme_and_r_scripts"]
check("named repository has no biomass/target terms", terms["var_biom"] == 0 and terms["sep_biom"] == 0 and terms["biom"] == 0)
check("named repository soil-variance scope retained", terms["variance"] == 45 and "Soil-carbon" in repo["scope"])
check("named repository input CSVs registered", len(repo["requested_input_csvs"]) == 4 and all(x.startswith("Data/") for x in repo["requested_input_csvs"]))
code_files = repo["zenodo_code_archive"]["files"]
check("Zenodo soil archive is code only", len(code_files) == 10 and all(x["name"].endswith(".R") for x in code_files))

check("Zenodo exact-field metadata searches empty", len(search["queries"]["zenodo"]) == 2 and all(x["total"] == 0 for x in search["queries"]["zenodo"]))
check("Figshare exact-field metadata searches empty", len(search["queries"]["figshare"]) == 2 and all(x["results"] == 0 for x in search["queries"]["figshare"]))
both = search["queries"]["github_code_both_terms"]
check("GitHub combined search has 16 hits", both["total"] == 16 and len(both["items"]) == 16)
check("GitHub combined hits all in audit repository", all(x["repository"] == "MIKEAA2020/general-sustainability" for x in both["items"]))
check("broad absence claim corrected", "Too broad" in search["interpretation"]["broad_claim_that_exact_fields_are_not_publicly_deposited"])
check("narrow static claim recorded", "No independent" in search["interpretation"]["narrow_static_claim"])
check("search indexing limitations explicit", len(search["limitations"]) >= 4)

check("SBFI DOI and license", sbfi["record"]["doi"] == "10.5281/zenodo.19357316" and sbfi["record"]["license"] == "cc-by-4.0")
check("SBFI archive size and MD5", sbfi["archive"]["bytes"] == 11800441690 and sbfi["archive"]["md5"] == "d138ded25a3fe1a97647f44b7409f80c")
check("SBFI full archive not downloaded", sbfi["archive"]["full_archive_downloaded"] is False)
check("SBFI inventory entries", len(inventory["entries"]) == 2378 == sbfi["archive"]["entries"])
check("SBFI range listing efficient", inventory["range_bytes_fetched_for_listing"] == 815962 and inventory["range_requests_for_listing"] == 1)
check("SBFI initial layer identity", sbfi["directly_inspected_layer"]["name"] == "CA_2020_tile_179_metrics" and sbfi["directly_inspected_layer"]["features"] == 2101)
check("SBFI reproduction layer identity", sbfi["reproduction_layer"]["name"] == "CA_2020_tile_705_metrics" and sbfi["reproduction_layer"]["features"] == 7)

for label, schema in (("tile179", schema179), ("tile705", schema705)):
    fields = schema["fields"]
    check(label + " has 209 fields", len(fields) == 209)
    check(label + " has 85 AGB fields", sum("AGB" in x for x in fields) == 85)
    check(label + " has ten SD fields", sum(x.endswith("_SD") for x in fields) == 10)
    check(label + " lacks NFI target fields", "var_biom" not in fields and "sep_biom" not in fields)
    check(label + " lacks named uncertainty fields", not any(any(term in x.lower() for term in ("rse", "uncert", "conf")) for x in fields))
check("both tiles have identical field names", schema179["fields"] == schema705["fields"])
check("SBFI AGB SD is present", "STRUCTURE_AGB_SD" in schema179["fields"])

reproduction = sbfi["reproduction_layer"]
check("cross-tile type differences recorded", reproduction["storage_type_difference_count"] == 16 and len(reproduction["storage_type_differences"]) == 16)
expected_type_fields = {f"SPECIES_{species}_AGB_{component}_PERC" for species in range(1, 5) for component in ("STEMWOOD", "BARK", "BRANCH", "FOLIAGE")}
check("cross-tile type difference fields exact", {x["field"] for x in reproduction["storage_type_differences"]} == expected_type_fields)
check("type differences not hidden as identical schemas", reproduction["schema_definition_identical_to_initial_layer"] is False and reproduction["field_names_identical_to_initial_layer"] is True)
check("type harmonization required", "harmonize" in reproduction["interpretation"].lower())

check("SBFI estimand is 2020", sbfi["documented_estimand"]["year"] == 2020)
check("SBFI SD is within-stand dispersion", "within-stand" in sbfi["documented_estimand"]["sd_interpretation"] and "not design-based" in sbfi["documented_estimand"]["sd_interpretation"])
check("SBFI formal-inference caution retained", "not intended to support formal statistical inference" in sbfi["documented_estimand"]["formal_inference_caution"])
not_valid = " ".join(sbfi["fitness"]["not_valid_for"])
check("SBFI not a static reconciliation substitute", "17C.0" in not_valid and "18C.0" in not_valid and "covariance" in not_valid)
for name, digest in sbfi["evidence_hashes"].items():
    target = {"archive_inventory_sha256": "sbfi_zip_inventory.json", "schema_sha256": "sbfi_schema.json", "reproduction_schema_sha256": "sbfi_schema_tile705.json"}[name]
    check(name + " matches evidence", hashlib.sha256((E / target).read_bytes()).hexdigest() == digest)

with (E / "source_files.csv").open(newline="", encoding="utf-8") as handle:
    sources = list(csv.DictReader(handle))
counts = Counter(x["route"] for x in sources)
expected_counts = {"github_api": 3, "github_repository_file": 11, "zenodo_record": 2, "zenodo_metadata_search": 2, "figshare_metadata_search": 2, "github_code_search": 3, "zenodo_archive": 1, "published_current_generator_snapshot": 3}
check("27-source registry", len(sources) == 27 and dict(counts) == expected_counts, dict(counts))
check("source registry unique keys", len({(x["route"], x["name"]) for x in sources}) == 27)
check("source registry statuses", all(int(x["http_status"]) == (206 if x["route"] == "zenodo_archive" else 200) for x in sources))
check("source registry positive sizes", all(int(x["bytes"]) > 0 for x in sources))
check("source registry hashes", all(re.fullmatch(r"[0-9a-f]{64}", x["sha256"]) for x in sources if x["route"] != "zenodo_archive"))
archive_row = next(x for x in sources if x["route"] == "zenodo_archive")
check("archive MD5 registered without full SHA", archive_row["md5"] == "d138ded25a3fe1a97647f44b7409f80c" and archive_row["sha256"] == "")
check("snapshot registry hashes agree", all(x["remote_sha256"] == next(s["sha256"] for s in sources if s["route"] == "published_current_generator_snapshot" and s["name"] == x["name"]) for x in snapshots))

for relative in ("scripts/reproduce_depository_checks.py", "scripts/validate_package.py"):
    try:
        ast.parse((ROOT / relative).read_text())
        check(relative + " parses", True)
    except SyntaxError as error:
        check(relative + " parses", False, str(error))
reproduction_text = (ROOT / "scripts/reproduce_depository_checks.py").read_text()
check("range reader reproduction present", "class RangeReader" in reproduction_text and '"Range": f"bytes={start}-{end}"' in reproduction_text)
check("four reproduction commands present", all(f'sub.add_parser("{x}")' in reproduction_text for x in ("github", "search", "inventory", "schema")))
check("schema retrieval remains selective", "min(feature_tables" in reproduction_text and "remote.extract" in reproduction_text)

readme = (ROOT / "README.md").read_text()
for label, needle in {
    "README public counterexample": "Exact `var_biom` and `sep_biom` fields are publicly archived",
    "README bounded negative": "No independent, provider-issued, version-matched static deposit was located",
    "README schema count": "209 field names",
    "README type differences": "Sixteen species 1–4 component-percentage fields",
    "README formal inference boundary": "not intended to support formal statistical inference",
    "README registry": "27 registered source responses",
    "README v1.1 correction": "reproduction-only defect",
}.items():
    check(label, needle in readme)

excluded = {"evidence/package_manifest.csv", "evidence/package_qa.json", "publication_receipt.json"}
payload = sorted(p for p in ROOT.rglob("*") if p.is_file() and p.relative_to(ROOT).as_posix() not in excluded and "__pycache__" not in p.parts and p.suffix != ".pyc")
check("payload contains no bulk archive or provider PDF", not any(p.suffix.lower() in {".zip", ".pdf", ".gdbtable"} for p in payload))
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

result = {"package": "canada_depository_and_sbfi_assessment_2026-10-30", "checks_run": len(checks), "checks_passed": sum(x["passed"] for x in checks), "checks_failed": sum(not x["passed"] for x in checks), "all_passed": all(x["passed"] for x in checks), "checks": checks}
(E / "package_qa.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: result[k] for k in ("checks_run", "checks_passed", "checks_failed", "all_passed")}, indent=2))
if not result["all_passed"]:
    for item in checks:
        if not item["passed"]:
            print("FAILED", item)
    raise SystemExit(1)
