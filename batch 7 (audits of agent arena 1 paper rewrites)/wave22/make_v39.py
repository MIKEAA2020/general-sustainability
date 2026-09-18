#!/usr/bin/env python3
"""Wave-22 / Task 98, part 1: author paper4_delay_dynamics_v39.md and
paper4_supplementary_v8.md --- the retitle round.

Owner directive (this round): "1- choose accurate, honest title,
appropriate to Theoretical ecology journal  2- which dois do u want?
are they on repo?"

Directive 1 (this script) = the retitle, commissioned this round.  The
title chosen under the directive:

    Governance delay and the stability of harvested stocks: mobilising
    and protective feedback rules, and the review interval as a design
    parameter

Choice rationale (recorded in full in humanizing
audits/V39_RETITLE_ROUND_AND_DOI_QUESTION.md):
  * ACCURATE --- every element is the paper's own phrase: "governance
    delay" is the defined object of Section 1.1; "the stability of
    harvested stocks" compresses the paper's actual subject (the local
    stability and attractor topology of the stock--memory--effort
    system); "mobilising and protective" are the two effort laws' own
    adjectives; "the review interval is a local spectral design
    parameter" is the abstract's own closing claim, and "design
    parameter" (title form) drops only the qualifier "local spectral",
    a conventional title compression, not an escalation.
  * HONEST --- the old title's "Delay-Induced Regime Change" is dropped:
    the large-amplitude attractor is unverified and the folds are
    certified at the discrete collocation level, so "regime change" as
    the title's headline claim would overclaim; no certification word
    ("certified", "proved") enters the title, keeping the
    certification-tier discipline in the body; no species or fishery
    enters the title (cod grounds scales, not coefficients).
  * THEORETICAL ECOLOGY APPROPRIATE --- ecological subject vocabulary
    ("harvested stocks"), the management-ecology register ("review
    interval", "design parameter") instead of control-theory jargon
    ("sample-and-hold", "monodromy", "as Control"); the topic-plus-
    design-clauses form matches the venue's own convention (cf. Adamson
    & Hilker 2020, Theoretical Ecology 13, 425-434, a 20-word
    declarative title); 21 words vs the old 23.

Two paper edits (the retitle is a one-line change; the second edit is
the mechanical consequence):
  T1  the title line (line 1);
  T2  the supplementary pointer v7 -> v8 (the retitle reaches the
      accompanying file, which carries the title in three places and is
      republished as paper4_supplementary_v8.md --- the wave-20
      accompanying-file discipline).

Three supplement edits (v7 -> v8):
  S1  the H1 "Supplementary Material --- <short title>";
  S2  the *Accompanies: "<full new title>"* line;
  S3  the opening descriptive phrase "the main article on <subject>".

Directive 2 (the DOI question) changes NO file: it is answered in the
round record and the response (the enumeration of the 29 DOI-less
reference entries with their verification classes; the repo answer ---
no reference-DOI list exists in the repository; the Zenodo record
22554217 is the paper's OWN v30-era archival deposit, DOI
10.5281/zenodo.22554217, holding three files and no reference list).

FROZEN (machine-checked): everything else.  All 1,473 math spans
byte-identical in both files; the abstract (258 journal words),
keywords, declarations, Data availability, References block (36
entries), figure and heading skeleton byte-identical; the supplement's
S1-S12 structure and object-label inventory unchanged; all eight
supplement-to-main-paper section references still resolve; content
numerics change only by the pointer's version digit (7 -> 8).

Idempotent; v38 and the v7 supplement are never modified (version
discipline).
"""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"

V38 = PR / "paper4_delay_dynamics_v38.md"
V39 = PR / "paper4_delay_dynamics_v39.md"
SUPP7 = PR / "paper4_supplementary_v7.md"
SUPP8 = PR / "paper4_supplementary_v8.md"

OLD_TITLE = (
    "Delay-Induced Regime Change in Harvested Stocks: The Mobilising "
    "and Protective Channels of Institutional Feedback, and the Review "
    "Interval as Control"
)
NEW_TITLE = (
    "Governance delay and the stability of harvested stocks: mobilising "
    "and protective feedback rules, and the review interval as a design "
    "parameter"
)

# --- the paper edits (2 anchored replacements) ---------------------------------
PAPER_EDITS: list[tuple[str, str, str]] = [
    (
        f"# {OLD_TITLE}",
        f"# {NEW_TITLE}",
        "T1  the retitle: the owner-delegated title choice",
    ),
    (
        "accompanying file `paper4_supplementary_v7.md`",
        "accompanying file `paper4_supplementary_v8.md`",
        "T2  Supplementary pointer v7 -> v8 (the retitled accompanying "
        "file)",
    ),
]

# --- the supplement edits (3 anchored replacements) -----------------------------
SUPP_EDITS: list[tuple[str, str, str]] = [
    (
        "# Supplementary Material — Delay-Induced Regime Change in "
        "Harvested Stocks",
        "# Supplementary Material — Governance delay and the stability "
        "of harvested stocks",
        "S1  supplement H1: the short title follows the retitle",
    ),
    (
        f'*Accompanies: "{OLD_TITLE}."*',
        f'*Accompanies: "{NEW_TITLE}."*',
        "S2  the Accompanies line: the full new title",
    ),
    (
        "the main article on delay-induced regime change in harvested "
        "stocks. It carries",
        "the main article on governance delay and the stability of "
        "harvested stocks. It carries",
        "S3  opening phrase: the subject follows the retitle",
    ),
]

# --- declared numeric deltas ---------------------------------------------------
# paper: the supplementary pointer's version digit only (7 -> 8)
PAPER_NUM_ADD = Counter({"8": 1})
PAPER_NUM_LOST = Counter({"7": 1})
PAPER_NUM_LOST_RAW = Counter({"7": 1})
# supplement: no numeric change (all three edits are digit-free both sides)
SUPP_NUM_ADD = Counter()
SUPP_NUM_LOST = Counter()

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
    # ("The Review Interval as Control" is NOT banned --- it is the live
    # Section 7 heading; only title-only fragments are banned)
    "Delay-Induced Regime Change", "Channels of Institutional Feedback",
    "delay-induced regime change", "channels of institutional feedback",
]

SUPP_REJECTION = [
    "committed", "audit document", "audit `audits", "relocated",
    "2026-09-03", "now established", "is now verified", "where it "
    "belongs", "tikhonov_unh_verification",
    # wave-22 retitle regression gates
    "Delay-Induced Regime Change", "Channels of Institutional Feedback",
    "delay-induced regime change", "channels of institutional feedback",
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


def supp_s_headings(t: str) -> list[str]:
    return re.findall(r"^#{2,3} S[\d.]+.*$", t, flags=re.M)


def supp_object_labels(t: str) -> list[str]:
    return re.findall(
        r"\*\*(?:Definition|Proposition|Theorem|Remark|Corollary|Lemma) "
        r"S[\d.]+", t,
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
    v38_md5_before = md5(V38)
    supp7_md5_before = md5(SUPP7)
    t38 = V38.read_text(encoding="utf-8")
    s7 = SUPP7.read_text(encoding="utf-8")

    # ---------- 1. author v39 and supp v8 -------------------------------------
    t39 = apply_edits(t38, PAPER_EDITS, "paper")
    s8 = apply_edits(s7, SUPP_EDITS, "supp")

    if V39.exists():
        assert V39.read_text(encoding="utf-8") == t39, (
            "existing v39 differs from the idempotent regeneration"
        )
    V39.write_text(t39, encoding="utf-8")
    if SUPP8.exists():
        assert SUPP8.read_text(encoding="utf-8") == s8, (
            "existing supp v8 differs from the idempotent regeneration"
        )
    SUPP8.write_text(s8, encoding="utf-8")

    # ---------- 2. the paper battery ------------------------------------------
    # 2a. line-level accounting: exactly 2 lines differ, count unchanged
    l38, l39 = t38.splitlines(), t39.splitlines()
    assert len(l39) == len(l38), (
        f"line-count delta {len(l39) - len(l38)} != 0"
    )
    d_lines = [i for i, (a, b) in enumerate(zip(l38, l39), 1) if a != b]
    assert d_lines == [1, 906], f"paper changed lines: {d_lines}"
    print(f"  paper lines: {len(l38)} -> {len(l39)} (exactly 2 lines "
          "changed: L1 the title, L906 the supplementary pointer)")

    # 2b. math spans byte-identical (multiset equality)
    assert Counter(spans(t39)) == Counter(spans(t38)), "math spans changed"
    print(f"  math spans: {len(spans(t39))} occurrences, multiset EXACTLY "
          "equal to v38's (the title carries no math)")

    # 2c. headings identical (the H1 title is not a ## / ### heading)
    assert headings(t39) == headings(t38), "heading skeleton changed"

    # 2d. the title gates
    assert t39.split("\n", 1)[0] == f"# {NEW_TITLE}", "H1 is not the new title"
    assert t38.split("\n", 1)[0] == f"# {OLD_TITLE}"
    # everything between the title line and the pointer line is
    # byte-identical: the strongest possible one-line-round gate
    assert "\n".join(l39[1:905]) == "\n".join(l38[1:905]), (
        "body drifted between the title and the supplementary pointer"
    )
    print("  title: the new 21-word title on L1; the body byte-identical "
          "up to the supplementary pointer")

    # 2e. numeric discipline: the pointer's version digit only
    n38 = toks(strip_ref_contexts(t38))
    n39 = toks(strip_ref_contexts(t39))
    assert (n39 - n38) == PAPER_NUM_ADD, (
        f"stripped numeric delta: {dict(n39 - n38)}"
    )
    assert (n38 - n39) == PAPER_NUM_LOST, (
        f"stripped numeric loss: {dict(n38 - n39)}"
    )
    r38, r39 = toks(t38), toks(t39)
    assert (r39 - r38) == PAPER_NUM_ADD, "raw numeric delta drifted"
    assert (r38 - r39) == PAPER_NUM_LOST_RAW, "raw numeric loss drifted"
    print("  content numerics: the declared delta only (the pointer's "
          "version digit 7 -> 8; both titles are digit-free)")

    # 2f. word-token discipline: exactly the edits' own delta
    exp = expected_word_delta(PAPER_EDITS)
    got = Counter({k: v for k, v in
                   (words(t39) - words(t38)).items() if v > 0})
    got_lost = Counter({k: v for k, v in
                        (words(t38) - words(t39)).items() if v > 0})
    exp_add = Counter({k: v for k, v in exp.items() if v > 0})
    exp_lost = Counter({k: -v for k, v in exp.items() if v < 0})
    assert got == exp_add, (
        f"word delta mismatch: extra={dict(got - exp_add)} "
        f"missing={dict(exp_add - got)}"
    )
    assert got_lost == exp_lost, (
        f"word loss mismatch: {dict(got_lost - exp_lost)}"
    )
    assert words(t39)["governance"] - words(t38)["governance"] == 1
    assert words(t39)["stability"] - words(t38)["stability"] == 1
    for w in ("induced", "regime", "channels", "institutional", "control"):
        assert words(t39)[w] - words(t38)[w] == -1, f"word {w} delta"
    print("  word tokens: exactly the declared title delta "
          "(governance+1, stability+1, rules/a/design/parameter in; "
          "induced/regime/channels/institutional/control out)")

    # 2g. frozen blocks byte-identical
    for start, end in (
        ("## Abstract", "## 1. Introduction"),
        ("## Data availability", "## Declaration of competing interest"),
        ("## Declaration of competing interest", "## References"),
    ):
        assert block(t39, start, end) == block(t38, start, end), (
            f"frozen block changed: {start}"
        )
    fig38 = re.search(r"!\[Figure 1\].*?\n\n", t38, flags=re.S)
    fig39 = re.search(r"!\[Figure 1\].*?\n\n", t39, flags=re.S)
    assert fig38 and fig39 and fig38.group(0) == fig39.group(0), (
        "figure block changed"
    )
    kw38 = t38.split("**Keywords:**")[1].split("\n", 1)[0]
    kw39 = t39.split("**Keywords:**")[1].split("\n", 1)[0]
    assert kw39 == kw38, "keywords changed"
    print("  frozen blocks: abstract (258 journal words)/keywords/"
          "declarations/Data availability/figure byte-identical")

    # 2h. the References block byte-identical (36 entries / 38 lines)
    assert refs_block(t39) == refs_block(t38), "references block changed"
    n_entries = sum(1 for ln in refs_block(t39).splitlines() if ln.strip())
    assert n_entries == 38, f"reference block lines {n_entries} != 38"
    print("  references block: byte-identical to v38's (36 entries; no "
          "reference touched in the retitle round)")

    # 2i. the Supplementary block: the declared construction
    sup38 = t38[t38.find("## Supplementary material"):]
    sup39 = t39[t39.find("## Supplementary material"):]
    expected_sup = sup38
    for old, new, _tag in PAPER_EDITS[1:2]:  # T2
        expected_sup = expected_sup.replace(old, new)
    assert sup39 == expected_sup, "Supplementary block drifted"
    assert t39.count("paper4_supplementary_v8.md") == 1
    assert "paper4_supplementary_v7.md" not in t39
    print("  Supplementary block: pointer v7 -> v8 (the retitled "
          "accompanying file); nothing else in the block changed")

    # 2j. 'if and only if' still exactly five
    assert t39.count("if and only if") == 5, "'if and only if' count changed"

    # 2k. rejection list zero-hit (incl. the retitle regression gates)
    hits = [b for b in REJECTION if b in t39]
    assert not hits, f"rejection hits in v39 md: {hits}"
    print(f"  rejection list: 0 hits ({len(REJECTION)} banned strings, "
          "incl. the 4 new old-title regression gates)")

    # 2l. abstract journal-word count unchanged (byte-identical)
    assert journal_words(t39) == journal_words(t38) == 258
    assert t39.split("## Abstract", 1)[1].split("## 1. Introduction")[0] \
        == t38.split("## Abstract", 1)[1].split("## 1. Introduction")[0]
    print("  abstract: 258 journal words, byte-identical")

    # 2m. cross-reference resolver: 0 unresolved
    heads: set[str] = set()
    for h in headings(t39):
        m = re.match(r"^#{2,3} (\d+(?:\.\d+)?)", h)
        if m:
            heads.add(m.group(1))
            heads.add(m.group(1).split(".")[0])
    unresolved = sorted(r for r in section_refs(t39) if r not in heads)
    assert not unresolved, f"unresolved refs: {unresolved}"
    print("  cross-reference resolver: 0 unresolved Section constructs")

    # ---------- 3. the supplement battery ------------------------------------
    ls7, ls8 = s7.splitlines(), s8.splitlines()
    assert len(ls7) == len(ls8), "supp line count changed"
    d_lines_s = [
        i for i, (a, b) in enumerate(zip(ls7, ls8), 1) if a != b
    ]
    assert d_lines_s == [1, 3, 5], f"supp changed lines: {d_lines_s}"
    print("  supplement: exactly 3 changed lines (L1 H1, L3 Accompanies, "
          "L5 the opening subject phrase)")

    # 3b. math spans multiset-equal
    assert Counter(spans(s8)) == Counter(spans(s7)), "supp math spans changed"

    # 3c. internal S-structure unchanged (the H1 is not an S-heading)
    assert supp_s_headings(s8) == supp_s_headings(s7), "S headings drifted"
    assert supp_object_labels(s8) == supp_object_labels(s7), (
        "supp object labels changed"
    )
    print("  supplement S-structure: S1-S12 headings and object-label "
          "inventory unchanged")

    # 3d. numeric discipline: no change
    sn7, sn8 = toks(s7), toks(s8)
    assert (sn8 - sn7) == SUPP_NUM_ADD, dict(sn8 - sn7)
    assert (sn7 - sn8) == SUPP_NUM_LOST, dict(sn7 - sn8)
    print("  supplement numerics: unchanged (all three title edits are "
          "digit-free on both sides)")

    # 3e. word-token discipline
    exp_s = expected_word_delta(SUPP_EDITS)
    got_s = Counter({k: v for k, v in
                     (words(s8) - words(s7)).items() if v > 0})
    got_s_lost = Counter({k: v for k, v in
                          (words(s7) - words(s8)).items() if v > 0})
    exp_s_add = Counter({k: v for k, v in exp_s.items() if v > 0})
    exp_s_lost = Counter({k: -v for k, v in exp_s.items() if v < 0})
    assert got_s == exp_s_add, f"supp word delta: {dict(got_s - exp_s_add)}"
    assert got_s_lost == exp_s_lost, "supp word loss drifted"
    assert words(s8)["governance"] - words(s7)["governance"] == 3
    print("  supplement words: exactly the declared edit delta "
          "(governance x3: H1, Accompanies, opening phrase)")

    # 3f. every supplement -> main-paper section reference resolves
    refs = supp_section_refs(s8)
    assert refs == {"2.3", "5", "6", "5.1", "8.2", "8.3", "9", "10.4"}, (
        sorted(refs)
    )
    unresolved_s = sorted(r for r in refs if r not in heads)
    assert not unresolved_s, f"supp refs unresolved: {unresolved_s}"
    print("  all eight supplement -> main-paper section references "
          "resolve against v39's headings")

    # 3g. artifact + retitle regression gates on the supplement
    hits_s = [b for b in SUPP_REJECTION if b in s8]
    assert not hits_s, f"artifact/retitle hits in supp v8: {hits_s}"
    assert s8.split("\n", 1)[0] == (
        "# Supplementary Material — Governance delay and the stability "
        "of harvested stocks"
    )
    print(f"  supplement artifact + retitle gates: 0 hits "
          f"({len(SUPP_REJECTION)} banned strings); the old title absent "
          "in every case form")

    # 3h. mirror consistency with the main text's own statements
    assert "together with the MPF material of S11" in t39
    assert "Material from the main article's Section 8.3" in s8
    assert "## S11. MPF Material" in s8
    assert "Every value below is reproduced verbatim from the main " \
        "text" in s8
    print("  mirror consistency: the main text's Supplementary paragraph "
          "names v8, which exists; the supplement's own references agree")

    # 3i. the paper points at the supplement that exists
    assert SUPP8.exists() and "paper4_supplementary_v8.md" == SUPP8.name

    # ---------- 4. version discipline: priors untouched ------------------------
    assert md5(V38) == v38_md5_before, "v38 was modified!"
    assert md5(SUPP7) == supp7_md5_before, "supp v7 was modified!"

    print("\nmake_v39: ALL CHECKS PASS")
    print(f"  paper4_delay_dynamics_v39.md   "
          f"({V39.stat().st_size} bytes; 2 anchored edits)")
    print(f"  paper4_supplementary_v8.md     "
          f"({SUPP8.stat().st_size} bytes; 3 anchored edits)")
    print(f"  v38 md5 {v38_md5_before} and supp v7 md5 "
          f"{supp7_md5_before} unchanged on disk")
    return 0


if __name__ == "__main__":
    sys.exit(main())
