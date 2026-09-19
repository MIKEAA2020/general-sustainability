#!/usr/bin/env python3
"""Wave-23 / Task 99, part 1: author paper4_delay_dynamics_v40.md --- the
over-hedging / phantom-strawman cleanup round.

Owner directive (this round, directive 2, verbatim intent): strip the
change-log, internal dialogue, and surrounding meta-commentary; no
editorial, self-praise or self-commentary statements, or informal terms
from chat history; scan for and remove all naive over-hedging
(metaphor apology / "map is not the territory" type statements) while
keeping legitimate scope statements; the manuscript should not
reference phantom or naive strawman points or unpublished work.

The wave-23 scan battery (seven artifact classes over the v39 md and
the v8 supplement, adjudicated hit by hit --- the full ledger in
humanizing audits/V40_OVERHEDGING_STRAWMAN_AND_CONTENT_PRESERVATION.md)
found exactly ONE actionable site:

  * Section 1.1 (md line 30): "... so institutional and ecological
    delay are analysed within one frame rather than opposed in
    caricature."  The trailing clause evokes an unnamed naive
    opposition ("opposed in caricature") that no cited source holds ---
    a phantom strawman point under the owner's rule.  The clause adds
    no content: the positive statement ("analysed within one frame")
    carries everything.  REMOVED.

Everything else scanned CLEAN (0 hits): no metaphor apology or
over-hedging form anywhere (the hen/eggs/apple passage is presented
without any "this is only a metaphor" disclaimer --- the owner's
"legit metaphor is fine" standard already met); no navigation/diary
patterns; no methodological self-description beyond the
certification-honesty scope statements (deliberately kept); no
editorial/self-praise; no informal chat terms; no references to
earlier unpublished manuscript versions ("superseded" survives only as
the variant-registry status label; the companion-paper references are
the owner-endorsed class).

One paper edit (v39 -> v40):
  E1  "analysed within one frame rather than opposed in caricature."
      -> "analysed within one frame."
      (5 words removed: rather, than, opposed, in, caricature; no
      digits, no math, no line-count change)

NO supplement edit: the v8 supplement scanned clean under the same
battery, so paper4_supplementary_v8.md stands unchanged and the
manuscript's pointer still names it.

FROZEN (machine-checked): everything else.  All 1,473 math spans
byte-identical; the title (the Task-98 Theoretical Ecology retitle)
unchanged; the abstract (258 journal words), keywords, declarations,
Data availability, References block (38 entries), figure, heading
skeleton and the Supplementary material paragraph byte-identical; the
body byte-identical outside md line 30; the v8 supplement untouched
with all eight of its section references resolving against v40's
headings.

"caricature" joins the permanent rejection list (3 new banned strings:
the full clause, the short clause, and the bare word).

Idempotent; v39 is never modified (version discipline).
"""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"

V39 = PR / "paper4_delay_dynamics_v39.md"
V40 = PR / "paper4_delay_dynamics_v40.md"
SUPP8 = PR / "paper4_supplementary_v8.md"

TITLE = (
    "Governance delay and the stability of harvested stocks: mobilising "
    "and protective feedback rules, and the review interval as a design "
    "parameter"
)

# --- the paper edit (1 anchored replacement) ------------------------------------
PAPER_EDITS: list[tuple[str, str, str]] = [
    (
        "so institutional and ecological delay are analysed within one "
        "frame rather than opposed in caricature.",
        "so institutional and ecological delay are analysed within one "
        "frame.",
        "E1  the phantom-strawman clause removed (the owner's "
        "no-phantom-strawman rule; the positive statement carries the "
        "content)",
    ),
]

# --- declared numeric deltas: NONE (the edit is digit-free both sides) ----------
PAPER_NUM_ADD = Counter()
PAPER_NUM_LOST = Counter()
PAPER_NUM_LOST_RAW = Counter()

REJECTION = [
    "mobilizing", "artifact", "stabilizing", "destabilizing",
    "Global Stability", "narrow window", "saddle-node of limit cycles",
    "non-autonomous and spatial domains", "anchoveta", "sardine",
    "cephalopod", "haddock", "rockfish", "orange roughy",
    "deep-sea teleost", "large sharks", "ICES", "N_min", "12.1",
    "0.2, 0.8", "Fisheries Research",
    "performance of alternative assessment frequencies",
    "fisheries management performance: A simulation approach",
    "Evaluation of management strategy performance under variable "
    "assessment intervals",
    "Effects of assessment frequency and harvest control rules",
    "plain name", "The message of the paper is stated plainly",
    "is collected in one display",
    "Sign Separation Theorem", "viability bleed",
    "phase-stabilisation trap", "administrative hunting", "basin lock-in",
    "A stable eigenvalue is not a stable fishery",
    "A stable eigenvalue is not a sustainable resource system",
    # wave-21 artifact-class regression gates
    "One point is stated once", "stated once, at the outset",
    "relocated", "the committed", "audit document", "is now established",
    "now registered", "2026-09-03", "where it belongs",
    # wave-22 retitle regression gates: the old title must never return
    "Delay-Induced Regime Change", "Channels of Institutional Feedback",
    "delay-induced regime change", "channels of institutional feedback",
    # wave-23 phantom-strawman regression gates
    "opposed in caricature", "in caricature", "caricature",
]

SUPP_REJECTION = [
    "committed", "audit document", "audit `audits", "relocated",
    "2026-09-03", "now established", "is now verified", "where it "
    "belongs", "tikhonov_unh_verification",
    # wave-22 retitle regression gates
    "Delay-Induced Regime Change", "Channels of Institutional Feedback",
    "delay-induced regime change", "channels of institutional feedback",
    # wave-23 phantom-strawman regression gates
    "opposed in caricature", "in caricature", "caricature",
]


def md5(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def spans(t: str) -> list[str]:
    return re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", t, flags=re.S)


def toks(t: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", t))


def words(t: str) -> Counter:
    return Counter(w.lower() for w in re.findall(r"[A-Za-z]+", t))


def headings(t: str) -> list[str]:
    return re.findall(r"^#{2,3} .*$", t, flags=re.M)


def block(t: str, start: str, end: str | None = None) -> str:
    i = t.find(start)
    assert i >= 0, f"heading not found: {start}"
    j = t.find(end) if end else len(t)
    assert j > i, f"end heading not found after {start}: {end}"
    return t[i:j]


def strip_ref_contexts(t: str) -> str:
    t = re.sub(
        r"Sections? (\d+(?:\.\d+)?)"
        r"(?:(?:\s*,\s*(?:and\s+)?|\s+and\s+|--|–)\d+(?:\.\d+)?)*",
        " ", t)
    t = re.sub(r"^#{2,3} \d+(?:\.\d+)?[^\n]*$", " ", t, flags=re.M)
    t = re.sub(
        r"\*\*(?:Theorem|Proposition|Lemma|Corollary|Remark|Definition) "
        r"\d+(?:\.\d+)?\*\*", " ", t)
    return t


def section_refs(t: str) -> Counter:
    c: Counter = Counter()
    for m in re.finditer(
        r"Sections?((?:\s+\d+(?:\.\d+)?)(?:(?:\s*,\s*(?:and\s+)?"
        r"|\s+and\s+|--|–)\d+(?:\.\d+)?)*)",
        re.sub(r"\s+", " ", t),
    ):
        for r in re.findall(r"\d+(?:\.\d+)?", m.group(1)):
            c[r] += 1
    return c


def refs_block(t: str) -> str:
    lines = t.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.strip() == "## References")
    j = next(
        k for k, ln in enumerate(lines)
        if ln.strip() == "## Supplementary material"
    )
    return "\n".join(lines[i:j]).rstrip("\n")


def journal_words(t: str) -> int:
    a = t.split("## Abstract\n\n", 1)[1].split("\n\n**Keywords:**")[0]
    return sum(
        1 for w in re.findall(r"\S+", a)
        if re.search(r"[A-Za-z0-9]", w)
    )


def supp_section_refs(t: str) -> set[str]:
    refs: set[str] = set()
    for m in re.finditer(
        r"Section[s]?((?:\s+\d+(?:\.\d+)?)(?:(?:\s*,\s*(?:and\s+)?"
        r"|\s+and\s+|--|–)\d+(?:\.\d+)?)*)",
        re.sub(r"\s+", " ", t),
    ):
        refs |= set(re.findall(r"\d+(?:\.\d+)?", m.group(1)))
    return refs


def apply_edits(text: str, edits: list[tuple[str, str, str]],
                label: str) -> str:
    for old, new, tag in edits:
        assert text.count(old) == 1, (
            f"{label} anchor not unique ({text.count(old)}): {tag}: "
            f"{old[:80]!r}"
        )
    for old, new, _tag in edits:
        text = text.replace(old, new)
    for old, _new, tag in edits:
        assert text.count(old) == 0, (
            f"{label} old text survives after replacement: {tag}"
        )
    for _old, new, tag in edits:
        assert text.count(new) == 1, f"{label} replacement not unique: {tag}"
    return text


def expected_word_delta(
    edits: list[tuple[str, str, str]],
) -> Counter:
    d: Counter = Counter()
    for old, new, _tag in edits:
        d.update(words(new))
        d.subtract(words(old))
    return Counter({k: v for k, v in d.items() if v != 0})


def main() -> int:
    # ---------- 0. pre-state (version discipline) ----------------------------
    v39_md5_before = md5(V39)
    supp8_md5_before = md5(SUPP8)
    t39 = V39.read_text(encoding="utf-8")
    s8 = SUPP8.read_text(encoding="utf-8")

    # ---------- 1. author v40 --------------------------------------------------
    t40 = apply_edits(t39, PAPER_EDITS, "paper")

    if V40.exists():
        assert V40.read_text(encoding="utf-8") == t40, (
            "existing v40 differs from the idempotent regeneration"
        )
    V40.write_text(t40, encoding="utf-8")

    # ---------- 2. the paper battery ------------------------------------------
    # 2a. line-level accounting: exactly 1 line differs, count unchanged
    l39, l40 = t39.splitlines(), t40.splitlines()
    assert len(l40) == len(l39), (
        f"line-count delta {len(l40) - len(l39)} != 0"
    )
    d_lines = [i for i, (a, b) in enumerate(zip(l39, l40), 1) if a != b]
    assert d_lines == [30], f"paper changed lines: {d_lines}"
    print(f"  paper lines: {len(l39)} -> {len(l40)} (exactly 1 line "
          "changed: L30, the Section 1.1 phantom-strawman clause)")

    # 2b. the strongest body gate: everything outside line 30 is
    # byte-identical (title included --- the Task-98 retitle stands)
    assert "\n".join(l40[:29]) == "\n".join(l39[:29]), (
        "body drifted before the edit line"
    )
    assert "\n".join(l40[30:]) == "\n".join(l39[30:]), (
        "body drifted after the edit line"
    )
    print("  body: byte-identical outside md line 30 (title, abstract, "
          "keywords and every section untouched)")

    # 2c. math spans byte-identical (multiset equality)
    assert Counter(spans(t40)) == Counter(spans(t39)), "math spans changed"
    print(f"  math spans: {len(spans(t40))} occurrences, multiset EXACTLY "
          "equal to v39's (the edit carries no math)")

    # 2d. headings identical
    assert headings(t40) == headings(t39), "heading skeleton changed"

    # 2e. the title gates (the retitle stands unchanged)
    assert t40.split("\n", 1)[0] == f"# {TITLE}", "H1 is not the title"

    # 2f. numeric discipline: NO numeric change at all
    n39 = toks(strip_ref_contexts(t39))
    n40 = toks(strip_ref_contexts(t40))
    assert (n40 - n39) == PAPER_NUM_ADD, (
        f"stripped numeric delta: {dict(n40 - n39)}"
    )
    assert (n39 - n40) == PAPER_NUM_LOST, (
        f"stripped numeric loss: {dict(n39 - n40)}"
    )
    r39, r40 = toks(t39), toks(t40)
    assert (r40 - r39) == PAPER_NUM_ADD, "raw numeric delta drifted"
    assert (r39 - r40) == PAPER_NUM_LOST_RAW, "raw numeric loss drifted"
    print("  content numerics: unchanged (the edit is digit-free on both "
          "sides)")

    # 2g. word-token discipline: exactly the edit's own delta
    exp = expected_word_delta(PAPER_EDITS)
    got = Counter({k: v for k, v in
                   (words(t40) - words(t39)).items() if v > 0})
    got_lost = Counter({k: v for k, v in
                        (words(t39) - words(t40)).items() if v > 0})
    exp_add = Counter({k: v for k, v in exp.items() if v > 0})
    exp_lost = Counter({k: -v for k, v in exp.items() if v < 0})
    assert got == exp_add, (
        f"word delta mismatch: extra={dict(got - exp_add)} "
        f"missing={dict(exp_add - got)}"
    )
    assert got_lost == exp_lost, (
        f"word loss mismatch: {dict(got_lost - exp_lost)}"
    )
    for w in ("rather", "than", "opposed", "in", "caricature"):
        assert words(t40)[w] - words(t39)[w] == -1, f"word {w} delta"
    print("  word tokens: exactly the declared delta (rather/than/opposed/"
          "in/caricature each -1; nothing else)")

    # 2h. frozen blocks byte-identical
    for start, end in (
        ("## Abstract", "## 1. Introduction"),
        ("## Data availability", "## Declaration of competing interest"),
        ("## Declaration of competing interest", "## References"),
    ):
        assert block(t40, start, end) == block(t39, start, end), (
            f"frozen block changed: {start}"
        )
    fig39 = re.search(r"!\[Figure 1\].*?\n\n", t39, flags=re.S)
    fig40 = re.search(r"!\[Figure 1\].*?\n\n", t40, flags=re.S)
    assert fig39 and fig40 and fig39.group(0) == fig40.group(0), (
        "figure block changed"
    )
    kw39 = t39.split("**Keywords:**")[1].split("\n", 1)[0]
    kw40 = t40.split("**Keywords:**")[1].split("\n", 1)[0]
    assert kw40 == kw39, "keywords changed"
    print("  frozen blocks: abstract (258 journal words)/keywords/"
          "declarations/Data availability/figure byte-identical")

    # 2i. the References block byte-identical (38 entries)
    assert refs_block(t40) == refs_block(t39), "references block changed"
    n_entries = sum(1 for ln in refs_block(t40).splitlines() if ln.strip())
    assert n_entries == 38, f"reference block lines {n_entries} != 38"
    print("  references block: byte-identical to v39's (38 entries; no "
          "reference touched in the cleanup round)")

    # 2j. the Supplementary block byte-identical (the pointer stays v8)
    sup39 = t39[t39.find("## Supplementary material"):]
    sup40 = t40[t40.find("## Supplementary material"):]
    assert sup40 == sup39, "Supplementary block drifted"
    assert t40.count("paper4_supplementary_v8.md") == 1
    assert "paper4_supplementary_v7.md" not in t40
    print("  Supplementary block: byte-identical (the pointer stays at the "
          "unchanged v8 supplement)")

    # 2k. 'if and only if' still exactly five
    assert t40.count("if and only if") == 5, "'if and only if' count changed"

    # 2l. rejection list zero-hit (incl. the caricature regression gates)
    hits = [b for b in REJECTION if b in t40]
    assert not hits, f"rejection hits in v40 md: {hits}"
    print(f"  rejection list: 0 hits ({len(REJECTION)} banned strings, "
          "incl. the 3 new phantom-strawman regression gates)")

    # 2m. abstract journal-word count unchanged (byte-identical)
    assert journal_words(t40) == journal_words(t39) == 258
    print("  abstract: 258 journal words, byte-identical")

    # 2n. cross-reference resolver: 0 unresolved
    heads: set[str] = set()
    for h in headings(t40):
        m = re.match(r"^#{2,3} (\d+(?:\.\d+)?)", h)
        if m:
            heads.add(m.group(1))
            heads.add(m.group(1).split(".")[0])
    unresolved = sorted(r for r in section_refs(t40) if r not in heads)
    assert not unresolved, f"unresolved refs: {unresolved}"
    print("  cross-reference resolver: 0 unresolved Section constructs")

    # ---------- 3. the supplement battery (v8 unchanged this round) -----------
    assert md5(SUPP8) == supp8_md5_before, "supp v8 was modified!"
    s40_refs = supp_section_refs(s8)
    assert s40_refs == {"2.3", "5", "6", "5.1", "8.2", "8.3", "9", "10.4"}, (
        sorted(s40_refs)
    )
    unresolved_s = sorted(r for r in s40_refs if r not in heads)
    assert not unresolved_s, f"supp refs unresolved vs v40: {unresolved_s}"
    print("  supplement v8: unchanged; all eight supplement -> main-paper "
          "section references resolve against v40's headings")

    hits_s = [b for b in SUPP_REJECTION if b in s8]
    assert not hits_s, f"artifact hits in supp v8: {hits_s}"
    assert s8.split("\n", 1)[0] == (
        "# Supplementary Material — Governance delay and the stability "
        "of harvested stocks"
    )
    print(f"  supplement artifact gates: 0 hits ({len(SUPP_REJECTION)} "
          "banned strings)")

    # 3c. mirror consistency with the main text's own statements
    assert "together with the MPF material of S11" in t40
    assert "Material from the main article's Section 8.3" in s8
    assert "## S11. MPF Material" in s8
    assert "Every value below is reproduced verbatim from the main " \
        "text" in s8
    print("  mirror consistency: the main text's Supplementary paragraph "
          "names the v8 file, which exists and agrees")

    # ---------- 4. version discipline: priors untouched ------------------------
    assert md5(V39) == v39_md5_before, "v39 was modified!"

    print("\nmake_v40: ALL CHECKS PASS")
    print(f"  paper4_delay_dynamics_v40.md   "
          f"({V40.stat().st_size} bytes; 1 anchored edit)")
    print(f"  v39 md5 {v39_md5_before} and supp v8 md5 "
          f"{supp8_md5_before} unchanged on disk")
    return 0


if __name__ == "__main__":
    sys.exit(main())
