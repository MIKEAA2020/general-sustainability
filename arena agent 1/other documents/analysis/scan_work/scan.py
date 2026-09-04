#!/usr/bin/env python3
"""Line-level scan of final paper versions: remnants, redundancy, informal/change-log language,
structural integrity, markdown syntax. Output: JSON report."""
import json, re, sys
from pathlib import Path

BASE = Path("/home/user/arena agen1")
FILES = [
    "paper1_assessment_separation_v10.md",
    "paper2_obstruction_calculus_v4.md",
    "paper3_material_ledgers_v15.md",
    "paper4_delay_dynamics_v14.md",
    "paper5_sampled_governance_v13.md",
    "paperE1_cod_forecast_ladder_v6.md",
    "paperE2_cod_intervention_v11.md",
    "paperE3_edwards_forecast_ladder_v7.md",
    "paperE4_edwards_intervention_v8.md",
    "paper1_supplementary.md",
    "paper3_supplementary_v5.md",
    "paper4_supplementary_v3.md",
    "paper5_supplementary_v4.md",
]

PATTERNS = {
    # remnants / placeholders
    "todo": r"\b(TODO|FIXME|XXX|TBD|placeholder|PLACEHOLDER)\b",
    "question_marks": r"\?\?\?",
    "double_em_dash_dangle": r"--\s*$",
    # change-log / meta language (paper-writing process)
    "changelog_prev": r"\b(previously|formerly|formerly called|in earlier (draft|version)s?|in the (previous|earlier|last) (draft|version|round|pass)|earlier draft|older version|the old (text|version|draft))\b",
    "changelog_now": r"\b(this version|the current version|newly (added|fixed|corrected)|now (fixed|updated|corrected|added)|has been (fixed|updated|corrected|rewritten)|we (fixed|corrected|replaced|removed|restored|reverted)\b)",
    "changelog_words": r"\b(reverted|superseded by|as of this (version|writing)|in the rewrite|per the (fix|correction)|the fix for|bugfix|regression)\b",
    "process_nouns": r"\b(audit trail|change log|changelog|diff|commit|pull request|this repo|repository\b)",
    # informal / conversational
    "informal": r"\b(basically|obviously|of course|interestingly|let's|it's worth noting that|worth mentioning|as we (saw|said|mentioned)|we'll|don't|doesn't|it's|here's|what's)\b",
    "first_person_casual": r"\b(I think|in my view|to my knowledge|we believe it is likely|we hope)\b",
    "exclamation": r"!",
    "smiley": r"[:;][-]?[()DPpd]",
    # stray artifacts
    "backslash_escape": r"\\[a-zA-Z]+\{",
    "latex_env": r"\\begin\{|\\end\{|\\cite\{|\\ref\{|\\label\{|\\eqref\{",
    "double_space": r"  +",
    "trailing_space": r" $",
}

def scan_file(path):
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    hits = {}
    for name, pat in PATTERNS.items():
        for i, ln in enumerate(lines, 1):
            if re.search(pat, ln):
                hits.setdefault(name, []).append((i, ln.strip()[:160]))
    # structural checks
    struct = {}
    # header numbering sequence
    headers = [(i, ln) for i, ln in enumerate(lines, 1) if re.match(r"^#{1,3} ", ln)]
    struct["n_headers"] = len(headers)
    struct["header_sample"] = [(i, h[:60]) for i, h in headers[:14]]
    # markdown tables: rows with mismatched pipe counts
    table_bad = []
    in_table = False
    pipe_count = None
    for i, ln in enumerate(lines, 1):
        if ln.strip().startswith("|") and ln.strip().endswith("|"):
            n = ln.count("|")
            if not in_table:
                in_table, pipe_count = True, n
            elif n != pipe_count:
                table_bad.append((i, n, pipe_count, ln.strip()[:80]))
        else:
            in_table, pipe_count = False, None
    struct["table_pipe_mismatches"] = table_bad[:10]
    # $-balance per file
    struct["dollar_count"] = text.count("$")
    struct["dollar_even"] = (text.count("$") % 2 == 0)
    # internal duplicate paragraphs (normalized, >= 250 chars)
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text)]
    seen = {}
    dups = []
    for p in paras:
        if len(p) < 250: continue
        key = p[:120]
        if key in seen and seen[key] != p and p != seen[key]:
            dups.append((seen[key][:100], p[:100]))
        seen.setdefault(key, p)
    struct["dup_para_pairs"] = dups[:8]
    return hits, struct

report = {}
for f in FILES:
    hits, struct = scan_file(BASE / f)
    n_hits = sum(len(v) for v in hits.values())
    report[f] = {"n_flag_lines": n_hits, "hits": hits, "struct": struct}
    print(f"{f}: {n_hits} flagged lines | $count={struct['dollar_count']} even={struct['dollar_even']} | headers={struct['n_headers']} | table_issues={len(struct['table_pipe_mismatches'])} | dup_paras={len(struct['dup_para_pairs'])}")

json.dump(report, open("/tmp/scan_report.json", "w"), indent=1)
print("saved /tmp/scan_report.json")
