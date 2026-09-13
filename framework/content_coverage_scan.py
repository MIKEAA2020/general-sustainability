#!/usr/bin/env python3
"""Content-coverage scanner — detects scientific/pedagogical content lost from earlier
manuscript versions (original upload v0 and frozen v13) in the current version.

Two checks:
  1. NUMERIC CLAIM COVERAGE: every numeric token of v0/v13 must appear in the current
     version, either exactly or via an updated value recorded in UPDATES (a mapping of
     old -> new literal from the version lineage). Unmatched tokens are listed with
     their sentence context for review.
  2. TERM COVERAGE: every term in the domain vocabulary must appear in the current
     version.

Usage: python3 content_coverage_scan.py <current.md> <older1.md> [older2.md ...]
"""
import re
import sys

# Known legitimate number updates across the lineage (old literal -> new literal(s)).
# Missing pairs are reported, not assumed.
UPDATES = {
    "0.965": "0.955", "0.985": "0.960/0.995",
    "0.710": "0.780", "0.130": "0.060",
    "0.090": "0.110",
    "0.015": "0.010/0.005",
    "0.680": "0.633", "0.760": "0.733",
    "0.975": "0.933", "0.925": "0.867",
    "0.376": "0.373", "0.044": "0.034",
    "62.7%": "61%", "64.5%": "61%",
    "25.8%": "37%", "3.8%": "1%",
    "18–22×": "18–20×", "69%": "72%", "94%": "93%",
    "98%": "93%", "99%": "99.5%", "97%": "95%",
    "0.970": "0.950", "0.030": "0.050", "0.0225": "0.005/0.050",
    "0.68": "0.633", "0.76": "0.733", "0.97": "0.95",
    "1.5": "0.5", "3.0%": "5.0%",
    "45.6": "13–110", "7.0": "2.2–16.7",
    "14000": "≈25 CPU-hours", "36480": "≈25 CPU-hours", "91200": "≈25 CPU-hours",
    "3.89": "≈25 CPU-hours", "10.13": "≈25 CPU-hours", "25.33": "≈25 CPU-hours",
    "2000": "≈25 CPU-hours",
    "3.0%": "2.96%", "7.2%": "7.16%", "17.3%": "17.34%", "9.0%": "9.01%",
    "4.3%": "4.33%", "13.23": "13.2301", "7.55": "7.5467", "12.28": "12.2832",
    "98.0": "98.05", "114.8": "114.80", "17.1%": "17.09%", "264.7": "264.72",
    "288.6": "288.58", "119.5": "119.47", "36.3%": "36.30%", "87.6": "87.65",
    "317.7": "317.71", "35.9%": "35.94%", "431.9": "431.90",
    "0.0358": "0.0359", "200×": "× 200", "4000": "4,000",
    # cross-reference tokens: the groundwater section was renumbered in the
    # restructured version (Phase J); not scientific claims
    "5.2": "Section 4",
}

TERMS = [
    "M2m", "oracle", "capelin", "Brier", "MASE", "Künsch", "Allee", "depensation",
    "persistence", "tie band", "comparator", "ladder", "rung", "class grounds",
    "climatological-flux", "LRP", "Schaefer", "stock-flow", "regime", "negative certificate",
    "information-set", "pre-registered", "block-bootstrap", "Diebold-Mariano",
    "likelihood ratio", "identification", "origin-matched", "hindcast", "M4",
    "Amendment", "T=71", "0.10", "power", "specificity", "misattribution",
]

SENT_RE = re.compile(r"(?<=[.!?])\s+|\n")

def sentences(text):
    parts = SENT_RE.split(text)
    out = []
    for p in parts:
        p = p.strip()
        if p.startswith("#"):
            continue  # section headers: their numbering is not a numeric claim
        if p and re.search(r"\d", p):
            out.append(p)
    return out

def numbers(sent):
    # decimals or >=3-digit integers, optionally %; bare small integers (years, kt) are noise
    return set(re.findall(r"\d+\.\d+(?:%)?|\d{3,}(?:\.\d+)?(?:%)?", sent))

def main():
    current, older = sys.argv[1], sys.argv[2:]
    cur = open(current).read()
    cur_nums = set(re.findall(r"\d+\.\d+(?:%)?|\d{3,}(?:\.\d+)?(?:%)?", cur))
    print(f"current: {current} ({len(cur_nums)} numeric tokens)\n")

    for old_path in older:
        old = open(old_path).read()
        print(f"--- {old_path} ---")
        missing = {}
        for sent in sentences(old):
            for num in sorted(numbers(sent)):
                if num in cur_nums:
                    continue
                mapped = UPDATES.get(num)
                if mapped and any(m in cur for m in mapped.split("/")):
                    continue
                missing.setdefault(sent[:140], set()).add(num)
        if not missing:
            print("  all numeric claims covered (exact or via recorded updates)")
        else:
            for sent, nums in sorted(missing.items()):
                print(f"  MISSING nums {sorted(nums)} in: {sent}")
        print()

    print("--- domain-term coverage ---")
    low = cur.lower()
    for t in TERMS:
        print(f"  {'OK  ' if t.lower() in low else 'MISS'} {t}")

if __name__ == "__main__":
    main()
