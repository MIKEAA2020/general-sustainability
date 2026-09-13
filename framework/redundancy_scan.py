#!/usr/bin/env python3
"""Remnant + redundancy scanner for manuscript versions.

Checks:
  R1 exact-duplicate prose lines (normalized, length > 60, excluding tables/headings/code);
  R2 near-duplicate long phrases: word n-grams (n >= 8, content words required) repeated
     >= 3 times anywhere in the document;
  R3 remnant probes beyond journal_formalization_scan.py: dates, "rerun", "post-hoc",
     "not executed", "TODO/TBD/placeholder", "will be added", "for future work we",
     "as the paper", "the reader should note", leftover telegraphic fragments
     (" — labelled", " vs ", " — " at line end), stray "frozen 5% band";
  R4 numeric-consistency probes: superseded point values outside their legitimate
     archived-row context (0.965, 0.985, 0.710, 0.130, 0.090, 0.015, 0.680, 0.760,
     0.975, 0.925, 0.044, 0.970, 62.7%, 25.8%, 3.8%, 69%, 94%, 45.6, 7.0).

Usage: python3 redundancy_scan.py <file.md> [--verbose]
Exit 0 = clean; 1 = findings printed.
"""
import re
import sys
from collections import Counter

# superseded values whose only legitimate occurrences are the archived-row contexts
OLD_VALUES = ["0.965", "0.985", "0.710", "0.130", "0.090", "0.680", "0.760",
              "0.975", "0.925", "0.044", "0.970", "62.7%", "64.5%", "25.8%",
              "69%", "45.6", "0.376", "0.978"]
# contexts where the archived replicate-table row legitimately keeps an old value
ALLOWED_CTX = ["archived", "Section 4.5", "replicate table"]

# legitimate recurring parameter-definition phrases (summary constants carried
# from the results into abstract / sections / appendix; not prose duplication)
ALLOWED_NGRAMS = [
    "0 0055 per module replicate under the null",
    "per module replicate under the null",
    "0 034 per module replicate pair",
    "0 900 1 000",
    "0 000 0 000",
    "power 0 900 1 000 and d5 false",
    "d5 false retention 0 000 0 000",
]

REMNANTS = [
    r"\b20\d\d-\d\d-\d\d\b", r"\brerun\b", r"\bre-run\b", r"\bpost-hoc\b", r"\bpost hoc\b",
    r"\bnot executed\b", r"\bTODO\b", r"\bTBD\b", r"\bplaceholder\b", r"\bFIXME\b",
    r"\bto be added\b", r"\bwill be added\b", r"\bfor future work\b", r"\bwe leave\b",
    r"\bas the paper\b", r"\bthe reader should note\b", r"\bnote that we\b",
    r"frozen 5% band", r"frozen rule", r"frozen specification",
    r" — labelled", r"\bvs\b", r"\bn\.b\.\b", r"\bshall see\b", r"\bsee above\b",
    r"\bas noted\b", r"\bthe earlier\b", r"\bpreviously reported\b",
]

def sentences(text):
    parts = re.split(r"\n|(?<=[.!?])\s+(?=[A-Z])", text)
    return [re.sub(r"\s+", " ", p).strip() for p in parts if p.strip()]

def main():
    path = sys.argv[1]
    verbose = "--verbose" in sys.argv
    text = open(path).read()
    lines = text.split("\n")
    findings = []

    in_fence = False
    def skip_line(line):
        return line.strip().startswith(("|", "```", "- `", "*")) or in_fence

    # R1 exact duplicates (prose only)
    seen = {}
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
        s = re.sub(r"\s+", " ", line).strip()
        if (len(s) > 60 and not skip_line(line)
                and re.search(r"[a-zA-Z]{4,}", s)):
            if s in seen:
                findings.append(("R1-duplicate-line", f"L{i} repeats L{seen[s]}: {s[:100]}"))
            else:
                seen[s] = i

    # R2 repeated long n-grams (>= 3 occurrences, n>=8, >=4 content words)
    words = [w for w in re.findall(r"[a-z0-9%’'-]+", text.lower())]
    n = 8
    grams = Counter()
    for i in range(len(words) - n + 1):
        gram = " ".join(words[i:i + n])
        content = [w for w in words[i:i + n] if re.fullmatch(r"[a-z]{4,}", w)]
        if len(content) >= 4:
            grams[gram] += 1
    for gram, cnt in grams.items():
        if cnt >= 3 and gram not in ALLOWED_NGRAMS:
            findings.append(("R2-repeated-phrase", f"'{gram}' appears {cnt}x"))

    # R3 remnant probes (prose only; "vs" is permitted in tables and code blocks)
    in_fence = False
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or line.strip().startswith("|"):
            continue
        stripped = re.sub(r"`[^`]*`|https?://\S+", " ", line)
        for p in REMNANTS:
            if re.search(p, stripped, re.IGNORECASE):
                findings.append(("R3-remnant", f"L{i} [{p}]: {line.strip()[:100]}"))
                break

    # R4 superseded values outside allowed contexts (word-boundary guards; prose only)
    in_fence = False
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or line.strip().startswith("|"):
            continue
        low = line.lower()
        if any(a in low for a in ALLOWED_CTX):
            continue
        for v in OLD_VALUES:
            for m in re.finditer(re.escape(v), line):
                start = m.start()
                if start > 0 and (line[start-1].isdigit() or line[start-1] == "."):
                    continue  # part of a larger number, e.g. "+35.94%"
                findings.append(("R4-superseded-value", f"L{i} [{v}]: {line.strip()[:110]}"))

    if findings:
        uniq = sorted(set(findings))
        for f in uniq:
            print(f"[{f[0]}] {f[1]}")
        print(f"\n{len(uniq)} findings")
        return 1
    print(f"{path}: 0 remnant/redundancy findings")
    return 0

if __name__ == "__main__":
    sys.exit(main())
