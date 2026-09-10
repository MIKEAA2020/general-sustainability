#!/usr/bin/env python3
"""
manuscript_style_scan.py -- enforce journal-article register on a LaTeX/Markdown manuscript.

Standing policy this encodes (apply to every paper, without being asked again):

  A. NO reference to unpublished/superseded versions of this manuscript. A journal
     article is not a changelog. Never "earlier versions said X", "corrected here",
     "v15 had".
  B. NO self-referential correction narrative about the authors' own prior mistakes,
     unless there is strong methodological value -- and even then, never tied to an
     unpublished version.
  C. NO editorial / self-praise / self-assessment ("importantly", "notably", "we
     believe", "this is a strength", "honest", "rigorous", "novel").
  D. NO project-report / diary register ("this pass", "in this round", "we then
     implemented", "TODO", "as noted above in the changelog").
  E. NO naive over-hedging: metaphor apologies ("the metaphor is not an empirical
     claim", "the map is not the territory", "this is only an analogy"),
     statements of the obvious. KEEP legitimate scope statements (what was tested,
     on what data, what does not generalise).
  F. Jargon register: flag project-internal coinages that a domain reader will not
     know, so they can be replaced with plain terms or defined once.

Usage:
    python3 manuscript_style_scan.py FILE [FILE ...] [--json out.json] [--quiet]

Exit code 1 if any BLOCKER hits are found, else 0. Intended for CI.
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

# severity: BLOCKER = must not ship; REVIEW = look at it, may be legitimate
RULES: list[tuple[str, str, str, str]] = [
    # ---- A/B: version & changelog references -------------------------------
    ("BLOCKER", "version-reference",
     r"\b(?:earlier|previous|prior|superseded|former|the last)\s+(?:version|versions|draft|drafts|revision|revisions|submission)\b",
     "References an unpublished/superseded version of this manuscript."),
    ("BLOCKER", "version-reference",
     # internal manuscript version tag: bare vNN NOT followed by a dot-decimal
     # (which would be a dataset/software release like G3P v1.12 or RAM v4.66),
     # and appearing near manuscript/draft vocabulary.
     r"(?:\b(?:version|draft|revision|manuscript|article|paper)\s+v\d{1,2}(?!\.\d)\b)"
     r"|(?:\bv\d{1,2}(?!\.\d)\b(?=[^.]{0,60}\b(?:of\s+(?:this|the)\s+(?:article|paper|manuscript)|draft|superseded)\b))",
     "Looks like an internal manuscript version tag (v15, v16...)."),
    ("BLOCKER", "self-correction",
     r"\b(?:that|this)\s+was\s+an\s+error\b|\bis\s+corrected\s+here\b|\bwe\s+(?:now\s+)?correct\b|\bcorrected\s+in\s+this\s+(?:version|revision|draft)\b",
     "Self-correction narrative about the authors' own earlier text."),
    ("BLOCKER", "self-correction",
     r"\b(?:previously|formerly|originally)\s+(?:stated|reported|described|claimed|said|printed)\b",
     "Describes what an earlier draft said."),
    ("BLOCKER", "changelog",
     r"\b(?:changelog|change log|revision history)\b",
     "Changelog register."),
    ("REVIEW", "changelog",
     r"\b(?:as\s+printed|quoted\s+verbatim\s+from\s+the\s+text|values?\s+as\s+printed)\b",
     "'As printed' implies a transcription record rather than a result."),

    # ---- D: project-report / diary register --------------------------------
    ("BLOCKER", "diary",
     r"\b(?:in\s+this\s+(?:pass|round|iteration|sweep)|this\s+pass|the\s+present\s+pass|post-freeze\s+layer|pre-score|freeze[- ]discipline|freeze\s+record)\b",
     "Internal process/diary vocabulary."),
    ("REVIEW", "diary",
     r"\b(?:we\s+then\s+(?:implemented|added|ran)|next\s+we\s+(?:ran|added)|TODO|FIXME|XXX)\b",
     "Implementation-log phrasing."),

    # ---- C: editorial / self-praise ----------------------------------------
    ("REVIEW", "editorial",
     r"\b(?:importantly|notably|crucially|strikingly|remarkably|interestingly|it\s+is\s+worth\s+noting|it\s+should\s+be\s+noted|we\s+emphasi[sz]e|we\s+stress)\b",
     "Editorial intensifier; state the fact instead."),
    ("BLOCKER", "self-praise",
     r"\b(?:this\s+is\s+a\s+strength|a\s+genuine\s+strength|the\s+paper\s+is\s+(?:honest|rigorous|careful)|we\s+are\s+careful\s+to|admirably|commendabl)\w*",
     "Self-assessment / self-praise."),
    ("REVIEW", "self-praise",
     r"\b(?:novel|first\s+ever|unprecedented|state[- ]of[- ]the[- ]art|cutting[- ]edge)\b",
     "Promotional adjective; let the result speak."),
    ("REVIEW", "hedged-opinion",
     r"\b(?:we\s+believe|we\s+feel|in\s+our\s+(?:view|opinion)|arguably|one\s+might\s+argue)\b",
     "Opinion register in place of evidence."),

    # ---- E: naive over-hedging / metaphor apology --------------------------
    ("BLOCKER", "metaphor-apology",
     r"(?:the\s+)?(?:metaphor|analogy|image|figure\s+of\s+speech)\s+(?:is|should\s+be|must\s+be)\s+(?:not|understood|taken|read)\b"
     r"|\bis\s+(?:only|merely|just)\s+(?:a|an)\s+(?:metaphor|analogy|illustration|heuristic)\b"
     r"|\bnot\s+(?:an?\s+)?(?:empirical|literal|quantitative)\s+claim\b"
     r"|\bthe\s+map\s+is\s+not\s+the\s+territory\b"
     r"|\bshould\s+not\s+be\s+taken\s+literally\b",
     "Metaphor apology: readers know an analogy is not data."),
    ("BLOCKER", "metaphor-apology",
     r"\bneeds\s+one\s+sentence,\s+not\s+a\s+(?:parable|story|metaphor)\b"
     r"|\bthe\s+(?:narrative|parable|story|fable|image)\s+that\s+usually\s+carries\s+the\s+point\b"
     r"|\brather\s+than\s+(?:a\s+)?(?:parable|metaphor|analogy)\b"
     r"|\bno\s+(?:parable|metaphor|analogy)\s+is\s+(?:needed|required|intended)\b",
     "Metaphor apology / narrative disclaimer; state the result plainly."),
    ("BLOCKER", "self-commentary",
     r"\bthis\s+paper\s+guards\s+against\b"
     r"|\bin\s+its\s+own\s+presentation\b"
     r"|\bwe\s+are\s+careful\b"
     r"|\bthis\s+(?:paper|article)\s+(?:is\s+careful|takes\s+care)\b"
     r"|\bwhat\s+is\s+merely\s+asserted\b",
     "Self-commentary about the paper's own virtue or method of presentation."),
    ("REVIEW", "obvious-hedge",
     r"\bof\s+course\b|\bit\s+goes\s+without\s+saying\b|\bneedless\s+to\s+say\b|\bobviously\b|\bas\s+everyone\s+knows\b",
     "States the obvious."),
    ("REVIEW", "double-hedge",
     r"\b(?:may|might|could)\s+(?:possibly|perhaps|potentially)\b|\bit\s+is\s+possible\s+that\s+.{0,40}\bmay\b",
     "Stacked hedges; one is enough."),

    # ---- F: project-internal coinages --------------------------------------
    ("REVIEW", "coinage",
     r"\b(?:negative\s+certificate|machine\s+layer|observation\s+fib(?:re|er)|class-level\s+incompatibility|"
     r"specification-matching\s+discipline|safe-set\s+map|viability\s+kernel|scored\s+ladder)\b",
     "Project-internal coinage; use a plain term or define once at first use."),
]

# Legitimate scope statements that must NOT be flagged (whitelist by content).
SCOPE_OK = re.compile(
    r"\b(?:scoped\s+to|does\s+not\s+generalis[ez]|we\s+do\s+not\s+claim|"
    r"within\s+the\s+model\s+class|conditional\s+hindcast|not\s+an\s+operational\s+forecast|"
    r"applies\s+only\s+to|restricted\s+to\s+the)\b", re.I)

COMMENT = re.compile(r"(?<!\\)%.*$")


def strip_tex_comment(line: str) -> str:
    return COMMENT.sub("", line)


def scan_text(text: str, path: str) -> list[dict]:
    hits = []
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = strip_tex_comment(raw)
        if not line.strip():
            continue
        for severity, kind, pat, why in RULES:
            for m in re.finditer(pat, line, re.I):
                # do not flag inside a clearly legitimate scope sentence
                if SCOPE_OK.search(line) and kind in {"obvious-hedge", "double-hedge"}:
                    continue
                hits.append({
                    "file": path, "line": lineno, "severity": severity,
                    "kind": kind, "match": m.group(0).strip(),
                    "why": why, "text": line.strip()[:160],
                })
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json", dest="json_out")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    all_hits: list[dict] = []
    for f in a.files:
        p = Path(f)
        if not p.exists():
            print(f"skip (missing): {f}", file=sys.stderr)
            continue
        all_hits += scan_text(p.read_text(encoding="utf-8", errors="replace"), str(p))

    blockers = [h for h in all_hits if h["severity"] == "BLOCKER"]
    reviews = [h for h in all_hits if h["severity"] == "REVIEW"]

    if not a.quiet:
        for group, label in ((blockers, "BLOCKER"), (reviews, "REVIEW")):
            if not group:
                continue
            print(f"\n=== {label} ({len(group)}) ===")
            bykind: dict[str, list[dict]] = {}
            for h in group:
                bykind.setdefault(h["kind"], []).append(h)
            for kind, items in sorted(bykind.items()):
                print(f"\n  [{kind}] {items[0]['why']}")
                for h in items:
                    print(f"    {h['file']}:{h['line']}: \"{h['match']}\"")
                    print(f"        | {h['text']}")

    print(f"\nsummary: {len(blockers)} blocker(s), {len(reviews)} review item(s) "
          f"across {len(set(h['file'] for h in all_hits)) if all_hits else 0} file(s)")

    if a.json_out:
        Path(a.json_out).write_text(json.dumps(all_hits, indent=2))
        print(f"wrote {a.json_out}")

    return 1 if blockers else 0


if __name__ == "__main__":
    sys.exit(main())
