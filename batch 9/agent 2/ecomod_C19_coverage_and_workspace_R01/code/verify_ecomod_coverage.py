"""Independent C18→C19 source-coverage checks; no manuscript files are modified."""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT.parent
C18 = HOME / "ecomod_audit_remediation_C18_A01"
C19 = HOME / "ecomod_editorial_division_C19_A01"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def labels(text):
    return re.findall(r"\\label\{([^}]+)\}", text)


def sections(text):
    return re.findall(r"\\(?:sub)*section\{([^}]+)\}", text)


def bibkeys(text):
    return re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text)


def citekeys(text):
    return {k.strip() for group in re.findall(r"\\cite\w*\{([^}]+)\}", text) for k in group.split(",")}


def floats(text, kind):
    if kind == "table":
        return len(re.findall(r"\\begin\{(?:longtable|table)\}", text))
    return len(re.findall(r"\\begin\{figure\}", text))


def equations(text):
    return len(re.findall(r"\\begin\{(?:equation|align|gather|multline)\*?\}", text))


def without_links(text):
    text = re.sub(r"\\url\{[^}]*\}", "", text)
    return re.sub(r"\\href\{[^}]*\}\{[^}]*\}", "", text)


def main():
    old_main = (C18 / "ecomod_C18_A01_main.tex").read_text()
    old_si = (C18 / "ecomod_C18_A01_SI.tex").read_text()
    new_main = (C19 / "ecomod_C19_A01_main.tex").read_text()
    new_si = (C19 / "ecomod_C19_A01_SI.tex").read_text()
    assert old_main == (C19 / "inherited_C18/ecomod_C18_A01_main.tex").read_text()
    assert old_si == (C19 / "inherited_C18/ecomod_C18_A01_SI.tex").read_text()

    structural = {
        "main_labels": [len(labels(old_main)), len(labels(new_main))],
        "SI_labels": [len(labels(old_si)), len(labels(new_si))],
        "main_section_titles": [len(sections(old_main)), len(sections(new_main))],
        "SI_section_titles": [len(sections(old_si)), len(sections(new_si))],
        "main_bibliography_records": [len(bibkeys(old_main)), len(bibkeys(new_main))],
        "SI_bibliography_records": [len(bibkeys(old_si)), len(bibkeys(new_si))],
        "main_equations": [equations(old_main), equations(new_main)],
        "SI_equations": [equations(old_si), equations(new_si)],
        "main_tables": [floats(old_main, "table"), floats(new_main, "table")],
        "main_figures": [floats(old_main, "figure"), floats(new_main, "figure")],
        "SI_tables": [floats(old_si, "table"), floats(new_si, "table")],
        "SI_figures": [floats(old_si, "figure"), floats(new_si, "figure")],
    }
    assert structural == {
        "main_labels": [52, 52], "SI_labels": [54, 54],
        "main_section_titles": [22, 22], "SI_section_titles": [37, 37],
        "main_bibliography_records": [45, 45], "SI_bibliography_records": [12, 12],
        "main_equations": [17, 17], "SI_equations": [5, 5],
        "main_tables": [6, 6], "main_figures": [3, 3],
        "SI_tables": [18, 18], "SI_figures": [5, 5],
    }
    assert labels(old_main) == labels(new_main)
    assert labels(old_si) == labels(new_si)
    assert sections(old_main) == sections(new_main)
    assert sections(old_si) == sections(new_si)
    assert bibkeys(old_main) == bibkeys(new_main)
    assert bibkeys(old_si) == bibkeys(new_si)
    assert not (citekeys(old_main + old_si) - citekeys(new_main + new_si))
    assert len(re.findall(r"\\section\{", old_si)) == len(re.findall(r"\\section\{", new_si)) == 11
    assert "\\section{Discussion}" not in new_si

    for i in range(1, 19):
        assert f"SI Table S{i}" in new_main
    for i in range(1, 6):
        assert f"SI Fig. S{i}" in new_main

    main_evidence = [
        r"$39\%$", r"$46.16\%$", r"$51.72\%$", r"$24.86\%$", r"$52.71\%$", r"$16.73\%$",
        "0.547925", "0.231310", "[0.05,1.658163]", "[0.606061,0.8]", "0.401217", "0.678295",
    ]
    assert all(x in new_main for x in main_evidence)
    si_detail = [
        r"7.1\times10^{-5}", r"8.9\times10^{-6}", "0.00221", "0.00102", "0.000831", "0.000924",
        r"B(A)=(b+b_G\rho)A", "$0.60$ & $+0.534$", "$0.85$ & $+0.784$", "$1.20$ & $+1.134$", "$2.00$ & $+1.934$",
        r"\subsection{Proof and feasibility construction}", r"\section{Derivations and proofs}",
    ]
    assert all(x in new_si for x in si_detail)
    assert new_main.count(r"\begin{proposition}") == 4
    assert new_main.count("Proof sketch.") == 4
    assert new_main.count(r"\begin{proof}") == 0

    number = re.compile(r"(?<![\w.])\d+(?:\.\d+)?(?![\w.])")
    unique_numeric_tokens_not_in_live_combined = sorted(
        set(number.findall(without_links(old_main))) - set(number.findall(without_links(new_main + new_si)))
    )
    assert unique_numeric_tokens_not_in_live_combined == ["0.807659", "1.1", "10.1"]

    with (C19 / "data/quality_law_comparison_C18_A01.csv").open(newline="") as handle:
        rows = {row["mode"]: row for row in csv.DictReader(handle)}
    current = float(rows["current"]["Ac_end"])
    delayed = float(rows["delayed"]["Ac_end"])
    assert round(current, 6) == 0.807659
    assert round(delayed, 6) == 0.807657
    assert round(delayed, 3) == 0.808
    assert f"{100 * (1.5 - delayed) / 1.5:.2f}" == "46.16"

    verification = json.loads((C19 / "metadata/document_verification_C19_A01.json").read_text())
    assert verification["main"]["pages"] == 39 and verification["SI"]["pages"] == 31
    assert verification["main"]["all_pages_thumbnail_QA"] and verification["SI"]["all_pages_thumbnail_QA"]
    for mode in ["normal", "optimized"]:
        log = (C19 / f"evidence/tests_{mode}_C19_A01.txt").read_text()
        assert "Ran 60 tests" in log and "\nOK" in log
    reproduction = json.loads((C19 / "evidence/reproduction_C19_A01.json").read_text())
    assert reproduction["status"] == "PASS"

    result = {
        "date": "2026-10-31",
        "status": "PASS",
        "source_sha256": {
            "C18_main": sha(C18 / "ecomod_C18_A01_main.tex"),
            "C18_SI": sha(C18 / "ecomod_C18_A01_SI.tex"),
            "C19_main": sha(C19 / "ecomod_C19_A01_main.tex"),
            "C19_SI": sha(C19 / "ecomod_C19_A01_SI.tex"),
            "quality_law_comparison": sha(C19 / "data/quality_law_comparison_C18_A01.csv"),
        },
        "structural_C18_then_C19": structural,
        "main_labels_identical_ordered": True,
        "SI_labels_identical_ordered": True,
        "section_titles_identical_ordered": True,
        "bibliography_keys_identical_ordered": True,
        "combined_citation_keys_lost": [],
        "SI_floats_explicitly_cited_in_main": {"tables": 18, "figures": 5},
        "main_key_evidence_retained": main_evidence,
        "SI_specialist_detail_retained": si_detail,
        "unique_numeric_tokens_not_in_live_combined_after_link_removal": unique_numeric_tokens_not_in_live_combined,
        "numeric_token_exceptions": {
            "1.1 and 10.1": "Superseded, unverified companion section locators intentionally replaced by content-based DOI-linked locators.",
            "0.807659": "Do not restore as the selected delayed-run endpoint: it rounds the current-quality comparator. The selected delayed value is 0.8076571663098769; C19's 0.808 and 46.16% are correct rounded displays.",
        },
        "endpoint_check": {
            "current_quality_comparator_Ac_end": current,
            "selected_delayed_quality_Ac_end": delayed,
            "C19_rounded_display": 0.808,
            "selected_area_decline_percent": round(100 * (1.5 - delayed) / 1.5, 2),
        },
        "C19_tests": {"normal": 60, "optimized": 60},
        "C19_reproduction": reproduction,
        "manual_diff_review": {"main_patch_lines": 248, "SI_patch_lines": 33, "completed": True},
        "conclusion": "No further main/SI redistribution or restorative manuscript edit is warranted on coverage, precision, or content grounds.",
    }
    output = ROOT / "metadata/ecomod_coverage_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "structural": structural, "endpoint_check": result["endpoint_check"], "conclusion": result["conclusion"]}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    main()
