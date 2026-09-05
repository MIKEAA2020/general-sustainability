#!/usr/bin/env python3
"""Wave-6 (Task 76) sentence-level normalized diff scanner.

For each of the nine arena-agent-1 papers: compares the FINAL version against
each of the five PRECEDING versions at sentence granularity, after
normalisation, and reports every sentence present in an older version but
absent from the final — the "dropped" content — paired, where possible, with
the replacement sentence added in the same version transition (a similarity
ratio is computed so modifications can be distinguished from pure deletions).

Design notes
------------
* The SAME splitter/normaliser runs on both sides of every comparison, so
  systematic splitter quirks cancel out; only real text differences surface.
* The per-version "*Version log (vN).*" paragraph is meta-content (each
  version rewrites it); it is excluded from the sentence universe but quoted
  per transition so recorded reasons can be cross-checked.
* Markdown table rows and display-math lines are atomic segments (never
  sentence-split), because builds guarantee tables byte-identical — any
  table-row drop surfacing here is a red flag to investigate manually.
* A sentence is "dropped" only if its normalised key is absent from the WHOLE
  final file (set semantics): relocation inside the paper is not a drop.
* "Last-seen" attribution: a dropped sentence is attributed to the newest
  preceding version in which it occurs, i.e. the transition L -> L+1 in which
  it disappeared.

Outputs: wave6/scan/<paper>.md (full per-transition report) and
wave6/scan/SUMMARY.csv.
"""

from __future__ import annotations

import csv
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path("/home/z/general-sustainability/arena agent 1/paper rewrites")
OUTDIR = Path("/home/z/general-sustainability/batch 7 (audits of agent arena 1 paper rewrites)/wave6/scan")

PAPERS = [
    ("paperE1_cod_forecast_ladder", 12),
    ("paperE2_cod_intervention", 18),
    ("paperE3_edwards_forecast_ladder", 12),
    ("paperE4_edwards_intervention", 11),
    ("paper1_assessment_separation", 20),
    ("paper2_obstruction_calculus", 10),
    ("paper3_material_ledgers", 29),
    ("paper4_delay_dynamics", 27),
    ("paper5_sampled_governance", 22),
]

# ---------------------------------------------------------------- splitting --

ABBREV_WORDS = {
    "Fig", "Figs", "Eq", "Eqs", "Sec", "Secs", "Sect", "Sects", "No", "nos",
    "approx", "Apx", "App", "Ch", "Vol", "pp", "Prof", "Dr", "St", "Mr", "Ms",
    "Dept", "Univ", "Inc", "Ltd", "Co", "ed", "eds", "Ex", "ca", "cf", "ibid",
    "op", "cit", "resp", "resp", "versus", "vs",
}
MULTI_ENDINGS = ("et al", "e.g", "i.e", "et seq", "q.e.d")


def _is_abbrev_boundary(text: str, i: int) -> bool:
    """True if the sentence-ending punctuation at index i is really an end."""
    tail = text[:i]
    # explicit multi-token endings: "et al.", "e.g.", "i.e."
    for m in MULTI_ENDINGS:
        if tail.endswith(m):
            return False
    w = re.search(r"([A-Za-z]+)$", tail)
    if w:
        word = w.group(1)
        if word in ABBREV_WORDS:
            return False
        if len(word) == 1 and word.isupper():  # initials: "A. B. Smith"
            return False
    return True


def split_sentences(text: str) -> list[str]:
    """Split a paragraph into sentences; tolerant, but identical on both sides."""
    text = text.strip()
    if not text:
        return []
    out: list[str] = []
    start = 0
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c in ".!?":
            j = i + 1
            if j < n and text[j] == c and c == ".":  # ellipsis "..." -> skip
                i += 1
                continue
            # decimal / version numbers: 1032.7 , v12. (digit before AND after)
            if c == "." and i > 0 and text[i - 1].isdigit():
                if j < n and (text[j].isdigit() or text[j] == "%"):
                    i += 1
                    continue
                # "884.6 kt" — digit before, space+lowercase after: NOT an end
                k = j
                while k < n and text[k] == " ":
                    k += 1
                if k < n and text[k].islower():
                    i += 1
                    continue
            # URL-ish: period inside a path
            if i > 0 and text[i - 1] in "/\\" or (j < n and text[j] in "/\\"):
                i += 1
                continue
            # need following whitespace to be a boundary
            k = j
            while k < n and text[k] == " ":
                k += 1
            if k >= n:
                i += 1
                continue
            nxt = text[k]
            if nxt.islower():  # lowercase continuation -> not a boundary
                i += 1
                continue
            if not _is_abbrev_boundary(text, i):
                i += 1
                continue
            out.append(text[start:i + 1].strip())
            start = k
            i = k
            continue
        i += 1
    if start < n:
        out.append(text[start:].strip())
    return [s for s in out if s]


# ------------------------------------------------------------- normalisation --

def norm_key(text: str) -> str:
    """Whitespace-collapse + strip markdown emphasis/backticks. Keeps math/numbers."""
    t = text
    t = t.replace("**", "")
    t = re.sub(r"(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])", r"\1", t)
    t = t.replace("`", "")
    t = re.sub(r"\s+", " ", t)
    return t.strip()


# ------------------------------------------------------------------ parsing --

VERSION_LOG_RE = re.compile(r"^\*Version log \(v[\d.]+\)\.\*", re.I)
LIST_RE = re.compile(r"^(\s*)([-*+]|\d+\.)\s+(.*)$")


def parse_file(path: Path) -> tuple[list[dict], str]:
    """Return (segments, version_log_paragraph). Each segment also records the
    nearest preceding heading (section context) for report readability."""
    segments: list[dict] = []
    vlog = ""
    cur_sect = "(top)"
    lines = path.read_text(encoding="utf-8").splitlines()
    for idx, raw in enumerate(lines, 1):
        line = raw.rstrip()
        if not line.strip():
            continue
        if VERSION_LOG_RE.match(line.lstrip()):
            vlog = line.strip()
            continue
        if line.startswith("#"):
            cur_sect = line.strip()
            segments.append({"kind": "heading", "line": idx, "key": norm_key(line), "disp": line.strip(), "sect": cur_sect})
            continue
        ls = line.lstrip()
        if ls.startswith("|"):
            segments.append({"kind": "tablerow", "line": idx, "key": norm_key(ls), "disp": ls, "sect": cur_sect})
            continue
        if ls.startswith("$$") or ls.startswith("\\[") or ls.startswith("\\begin"):
            segments.append({"kind": "display", "line": idx, "key": norm_key(ls), "disp": ls, "sect": cur_sect})
            continue
        m = LIST_RE.match(line)
        if m:
            body = m.group(3)
            kind = "listitem"
        else:
            body = line.strip()
            kind = "para"
        for sent in split_sentences(body):
            segments.append({"kind": kind, "line": idx, "key": norm_key(sent), "disp": sent, "sect": cur_sect})
    return segments, vlog


# ---------------------------------------------- supplementary relocation map --

SUPPLEMENTARIES = {
    "paper1_assessment_separation": ["paper1_supplementary.md", "paper1_supplementary_v2.md"],
    "paper3_material_ledgers": [f"paper3_supplementary{'_v%d' % v if v else ''}.md" for v in range(0, 8)],
    "paper4_delay_dynamics": ["paper4_supplementary.md", "paper4_supplementary_v2.md",
                              "paper4_supplementary_v3.md", "paper4_supplementary_v4.md"],
    "paper5_sampled_governance": ["paper5_supplementary.md", "paper5_supplementary_v2.md",
                                  "paper5_supplementary_v3.md", "paper5_supplementary_v4.md",
                                  "paper5_supplementary_v5.md"],
}


def supplementary_keys(base: str) -> dict[str, set]:
    """key-set per supplementary file for the paper family (any version counts:
    content relocated to a companion file is not lost)."""
    out: dict[str, set] = {}
    for name in SUPPLEMENTARIES.get(base, []):
        p = ROOT / name
        if p.exists():
            segs, _ = parse_file(p)
            out[name] = {s["key"] for s in segs}
    return out


# -------------------------------------------------------------------- driver --

def scan_paper(base: str, final_v: int) -> dict:
    olds = list(range(final_v - 5, final_v))
    fpath = ROOT / f"{base}_v{final_v}.md"
    fsegs, fvlog = parse_file(fpath)
    fkeys = {s["key"] for s in fsegs}

    parsed: dict[int, list[dict]] = {}
    vlogs: dict[int, str] = {}
    for v in olds + [final_v]:
        p = ROOT / f"{base}_v{v}.md"
        parsed[v], vlogs[v] = parse_file(p)

    # last-seen attribution for dropped keys
    last_seen: dict[str, int] = {}
    disp_of: dict[str, tuple[str, int]] = {}  # key -> (kind, line) of first occurrence
    for v in olds:
        for s in parsed[v]:
            if s["key"] in fkeys:
                continue
            last_seen[s["key"]] = max(last_seen.get(s["key"], 0), v)
            if s["key"] not in disp_of:
                disp_of[s["key"]] = (s["kind"], s["line"])

    # added-per-transition (for pairing): keys in L+1 not in L
    added: dict[int, list[dict]] = {}
    for v in olds:
        nxt = v + 1
        keys_v = {s["key"] for s in parsed[v]}
        added[v] = [s for s in parsed[nxt] if s["key"] not in keys_v]

    sup = supplementary_keys(base)

    per_transition: dict[int, list[dict]] = {v: [] for v in olds}
    for key, L in last_seen.items():
        kind, line = disp_of[key]
        entry = {"key": key, "kind": kind, "line": line, "disp": None, "pair": None, "ratio": 0.0,
                 "sect": "?", "sup": None}
        # recover display text + section from version L
        for s in parsed[L]:
            if s["key"] == key:
                entry["disp"] = s["disp"]
                entry["sect"] = s["sect"]
                break
        for name, keys in sup.items():
            if key in keys:
                entry["sup"] = name
                break
        best, bestr = None, 0.0
        for a in added[L]:
            r = SequenceMatcher(None, key, a["key"]).ratio()
            if r > bestr:
                bestr, best = r, a
        entry["pair"], entry["ratio"] = (best["disp"] if best else None), bestr
        per_transition[L].append(entry)
    for v in olds:
        per_transition[v].sort(key=lambda e: e["line"])

    return {
        "base": base, "final_v": final_v, "olds": olds,
        "fvlog": fvlog, "vlogs": vlogs,
        "final_counts": {k: sum(1 for s in fsegs if s["kind"] == k) for k in
                         {"para", "listitem", "heading", "tablerow", "display"}},
        "per_transition": per_transition,
    }


def render_report(res: dict) -> str:
    base, final_v = res["base"], res["final_v"]
    L: list[str] = []
    L.append(f"# Sentence-level normalised diff scan — {base} (final v{final_v})")
    L.append("")
    L.append(f"Universe: body sentences/segments of the final v{final_v} vs the five preceding versions "
             f"(v{final_v-5} … v{final_v-1}). A segment counts as dropped only if absent from the *whole* final "
             f"file. Table rows and display-math lines are atomic. The per-version `*Version log*` paragraph is "
             f"excluded from the universe (meta) and quoted per transition.")
    L.append("")
    L.append(f"Final v{final_v} segment counts: " + ", ".join(f"{k} {v}" for k, v in res["final_counts"].items()))
    L.append("")
    for v in res["olds"]:
        nxt = v + 1
        entries = res["per_transition"][v]
        n_mod = sum(1 for e in entries if e["ratio"] >= 0.55)
        n_drop = len(entries) - n_mod
        vlog = res["vlogs"].get(nxt, "")
        L.append(f"## Transition v{v} → v{nxt} — {len(entries)} dropped "
                 f"({n_mod} modified-with-replacement r≥0.55, {n_drop} no-close-replacement)")
        L.append("")
        if vlog:
            L.append(f"> v{nxt} version log: {vlog[:900]}{'…' if len(vlog) > 900 else ''}")
        else:
            L.append(f"> v{nxt} carries no in-file version log (pre-batch-7 transition).")
        L.append("")
        if not entries:
            L.append("_(no dropped sentences)_")
            L.append("")
            continue
        for i, e in enumerate(entries, 1):
            disp = e["disp"] or e["key"]
            if len(disp) > 700:
                disp = disp[:700] + " …[truncated]"
            sup_note = f" — ⚠ PRESENT IN SUPPLEMENTARY {e['sup']}" if e["sup"] else ""
            L.append(f"{i}. **[{e['kind']} @v{v} L{e['line']} · {e['sect']}]**{sup_note} {disp}")
            if e["pair"] is not None and e["ratio"] >= 0.35:
                p = e["pair"]
                if len(p) > 320:
                    p = p[:320] + " …[truncated]"
                L.append(f"   - paired replacement (r={e['ratio']:.2f}): {p}")
            elif e["pair"] is not None:
                p = e["pair"]
                if len(p) > 200:
                    p = p[:200] + " …[truncated]"
                L.append(f"   - weak pairing only (r={e['ratio']:.2f}): {p}")
            else:
                L.append("   - no replacement sentence found in v%d" % nxt)
        L.append("")
    return "\n".join(L)


def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for base, final_v in PAPERS:
        res = scan_paper(base, final_v)
        report = render_report(res)
        out = OUTDIR / f"{base}.md"
        out.write_text(report, encoding="utf-8")
        total = sum(len(v) for v in res["per_transition"].values())
        print(f"{base}: final v{final_v}; {total} dropped sentences across 5 transitions -> {out.name}")
        for v in res["olds"]:
            entries = res["per_transition"][v]
            rows.append({
                "paper": base, "transition": f"v{v}->v{v+1}",
                "dropped": len(entries),
                "modified_r>=0.55": sum(1 for e in entries if e["ratio"] >= 0.55),
                "no_close_replacement": sum(1 for e in entries if e["ratio"] < 0.55),
                "tablerow_drops": sum(1 for e in entries if e["kind"] == "tablerow"),
                "heading_drops": sum(1 for e in entries if e["kind"] == "heading"),
                "relocated_to_suppl": sum(1 for e in entries if e["sup"]),
            })
    with open(OUTDIR / "SUMMARY.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"SUMMARY.csv written with {len(rows)} transitions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
