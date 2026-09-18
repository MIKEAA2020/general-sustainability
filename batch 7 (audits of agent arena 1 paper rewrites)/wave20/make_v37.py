#!/usr/bin/env python3
"""Wave-20 / Task 95, part 1: author paper4_delay_dynamics_v37.md and
paper4_supplementary_v6.md.

Owner directive (this round): "do abstract, title, keywords, individual
sections and supplementary file all align with latest version?  ensure
no errors introduced or content lost from the several humanizing
passes."

The round's audit found the paper side aligned (title, keywords, the
258-word abstract, every individual section, the Organization paragraph,
all repaired cross-references, the rotation seams, the relative-pointer
scan, the rendered spine) and the humanizing-pass content spine intact
(review_v34/v35/v36 all re-run ALL CHECKS PASS).  It found exactly ONE
genuine misalignment: the accompanying supplementary file (last authored
in the v29 era, Task 78, 2026-09-06) still carries three main-paper
section references under the pre-v36 structure, because the v36
restructuring's bijective renumber map (7->9, 8->7, 9->8) was applied to
the paper's md/tex/rendered text but the supplementary file was never in
any gate's scope:

  supplement S9 intro : "All records of Section 7 of the main paper"
     -> Section 9 (v29/v35 Section 7 = The Delayed-Recruitment
        (Maturation-Delay) System = v36 Section 9; the main text's Data
        availability already says "the Section 9 records ... gate log
        and fine-map table, Supplementary S9")
  supplement S11 intro: "relocated from the main article's Section 9.3
     (the MPF paragraph)" -> Section 8.3 (v29/v35 Section 9.3 = The
        registered numerical families = v36 Section 8.3; the in-paper
        Supplementary paragraph already says "relocated from Sections
        8.3 and 10.4")
  supplement S12 note : "(main text, Sections 5.1 and 9.2; the recovered
     compute core of S9.5)" -> Sections 5.1 and 8.2 (v29/v35 Section 9.2
        = The attractor topology and the lower boundary events, where
        the rebuilt Krawczyk stage's discrete-collocation certificates
        live, = v36 Section 8.2)

The paper's Supplementary paragraph names the accompanying file by
version (paper4_supplementary_v5.md), so the aligned supplement is
published as a NEW file paper4_supplementary_v6.md (version discipline)
and the paper pointer is updated in paper4_delay_dynamics_v37.md --- a
one-line, accuracy-only edit.

FROZEN (machine-checked): everything else.  The paper diff vs v36 is
exactly one line (the filename); the supplement diff vs v5 is exactly
three lines (the remapped references); every math span, word token,
heading, section reference, theorem label, the 36 references, the
declarations and the figure block are byte-identical; the only numeric
change is the filename's version digit (5 -> 6); the supplement's
internal S-structure and object-label inventory are unchanged; every
main-paper section reference carried by the supplement resolves against
v37's heading inventory; the S12 label-mapping targets all exist in v37.

Idempotent; v36 and the v5 supplement are never modified (version
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

V36 = PR / "paper4_delay_dynamics_v36.md"
V37 = PR / "paper4_delay_dynamics_v37.md"
SUPP5 = PR / "paper4_supplementary_v5.md"
SUPP6 = PR / "paper4_supplementary_v6.md"

# --- the edits ---------------------------------------------------------------
PAPER_OLD = "paper4_supplementary_v5.md"
PAPER_NEW = "paper4_supplementary_v6.md"

SUPP_EDITS = [
    (
        "All records of Section 7 of the main paper",
        "All records of Section 9 of the main paper",
    ),
    (
        "relocated from the main article's Section 9.3 (the MPF paragraph)",
        "relocated from the main article's Section 8.3 (the MPF paragraph)",
    ),
    (
        "(main text, Sections 5.1 and 9.2;",
        "(main text, Sections 5.1 and 8.2;",
    ),
]

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


def section_refs_in_supp(t: str) -> set[str]:
    """Every 'Section(s) N(.k)' target the supplement points at."""
    refs: set[str] = set()
    for m in re.finditer(
        r"Section[s]?((?:\s+\d+(?:\.\d+)?)(?:(?:\s*,\s*(?:and\s+)?"
        r"|\s+and\s+|--|–)\d+(?:\.\d+)?)*)",
        t,
    ):
        refs |= set(re.findall(r"\d+(?:\.\d+)?", m.group(1)))
    return refs


def supp_object_labels(t: str) -> list[str]:
    return re.findall(
        r"\*\*(?:Definition|Proposition|Theorem|Remark|Corollary|Lemma) "
        r"S[\d.]+", t
    )


def supp_s_headings(t: str) -> list[str]:
    return re.findall(r"^#{2,3} S[\d.]+.*$", t, flags=re.M)


def journal_words(t: str) -> int:
    a = t.split("## Abstract\n\n", 1)[1].split("\n\n**Keywords:**")[0]
    return sum(
        1 for w in re.findall(r"\S+", a)
        if re.search(r"[A-Za-z0-9]", w)
    )


def main() -> int:
    # ---------- 0. pre-state (version discipline) ----------------------------
    v36_md5_before = md5(V36)
    supp5_md5_before = md5(SUPP5)

    t36 = V36.read_text(encoding="utf-8")
    s5 = SUPP5.read_text(encoding="utf-8")

    # ---------- 1. the paper edit (one anchored replacement) -----------------
    assert t36.count(PAPER_OLD) == 1, (
        f"paper anchor not unique: {t36.count(PAPER_OLD)}"
    )
    t37 = t36.replace(PAPER_OLD, PAPER_NEW)
    assert t37.count(PAPER_NEW) == 1 and PAPER_OLD not in t37

    # ---------- 2. the supplement edits (three anchored replacements) --------
    for old, new in SUPP_EDITS:
        assert s5.count(old) == 1, f"supp anchor not unique: {old!r}"
    s6 = s5
    for old, new in SUPP_EDITS:
        s6 = s6.replace(old, new)
    for _, new in SUPP_EDITS:
        assert s6.count(new) == 1
    for old, _ in SUPP_EDITS:
        assert old not in s6

    # ---------- 3. write (idempotent outputs; priors untouched) --------------
    if V37.exists():
        assert V37.read_text(encoding="utf-8") == t37, (
            "existing v37 differs from the idempotent regeneration"
        )
    V37.write_text(t37, encoding="utf-8")
    if SUPP6.exists():
        assert SUPP6.read_text(encoding="utf-8") == s6, (
            "existing supp v6 differs from the idempotent regeneration"
        )
    SUPP6.write_text(s6, encoding="utf-8")

    # ---------- 4. the paper battery ------------------------------------------
    # 4a. exactly one changed line, and it is the pointer line
    d = [
        (i, a, b)
        for i, (a, b) in enumerate(zip(t36.splitlines(), t37.splitlines()))
        if a != b
    ]
    assert len(t36.splitlines()) == len(t37.splitlines()), "line count changed"
    assert len(d) == 1 and PAPER_NEW in d[0][2], f"paper diff != 1 line: {d}"

    # 4b. math spans byte-identical (multiset equality)
    assert Counter(spans(t37)) == Counter(spans(t36)), "math spans changed"

    # 4c. headings identical
    assert headings(t37) == headings(t36), "heading skeleton changed"

    # 4d. numeric discipline: the filename's version digit only
    dt, lost = toks(t37) - toks(t36), toks(t36) - toks(t37)
    assert dt == Counter({"6": 1}) and lost == Counter({"5": 1}), (
        f"numeric delta {dict(dt)} / lost {dict(lost)}"
    )

    # 4e. word tokens identical
    assert words(t37) == words(t36), "word tokens changed"

    # 4f. frozen blocks byte-identical
    # byte-identical blocks
    for start, end in (
        ("# Delay-Induced Regime Change", "\n## Abstract"),
        ("## Abstract", "## 1. Introduction"),
        ("## References", "## Supplementary material"),
        ("## Data availability", "## Declaration of competing interest"),
        ("## Declaration of competing interest", "## References"),
    ):
        assert block(t37, start, end) == block(t36, start, end), (
            f"frozen block changed: {start}"
        )
    # the Supplementary block is identical modulo the pointer replacement
    # (the wave-19 precedent: blocks carrying versioned pointers freeze
    #  'identical modulo the declared replacement', not byte-wise)
    assert block(t37, "## Supplementary material") == block(
        t36, "## Supplementary material"
    ).replace(PAPER_OLD, PAPER_NEW), "Supplementary block changed beyond " \
        "the pointer"
    # the figure block
    fig36 = re.search(r"!\[Figure 1\].*?\n\n", t36, flags=re.S)
    fig37 = re.search(r"!\[Figure 1\].*?\n\n", t37, flags=re.S)
    assert fig36 and fig37 and fig36.group(0) == fig37.group(0), (
        "figure block changed"
    )

    # 4g. 'if and only if' still exactly five
    assert t37.count("if and only if") == 5, "'if and only if' count changed"

    # 4h. rejection list zero-hit
    hits = [b for b in REJECTION if b in t37]
    assert not hits, f"rejection hits in v37 md: {hits}"

    # 4i. abstract journal-word count unchanged
    assert journal_words(t37) == journal_words(t36) == 258, (
        "abstract word count changed"
    )

    # ---------- 5. the supplement battery -------------------------------------
    # 5a. exactly three changed lines
    d5 = [
        (i, a, b)
        for i, (a, b) in enumerate(zip(s5.splitlines(), s6.splitlines()))
        if a != b
    ]
    assert len(s5.splitlines()) == len(s6.splitlines()), "supp line count"
    assert len(d5) == 3, f"supp diff != 3 lines: {len(d5)}"
    for (_, _, new), (_, want) in zip(d5, SUPP_EDITS):
        assert want in new, f"unexpected supp change line: {new!r}"

    # 5b. internal S-structure unchanged
    assert supp_s_headings(s6) == supp_s_headings(s5), "S headings changed"
    assert supp_object_labels(s6) == supp_object_labels(s5), (
        "supp object labels changed"
    )

    # 5c. numeric discipline: the three remapped references only
    dt5 = toks(s6) - toks(s5)
    lost5 = toks(s5) - toks(s6)
    assert dt5 == Counter({"9": 1, "8.3": 1, "8.2": 1}), dict(dt5)
    assert lost5 == Counter({"7": 1, "9.3": 1, "9.2": 1}), dict(lost5)

    # 5d. every supplement -> main-paper section reference resolves
    #     against v37's heading inventory
    v37_heads: set[str] = set()
    for h in headings(t37):
        m = re.match(r"^#{2,3} (\d+(?:\.\d+)?)", h)
        if m:
            v37_heads.add(m.group(1))
            v37_heads.add(m.group(1).split(".")[0])
    supp_refs = section_refs_in_supp(s6)
    expected_refs = {"2.3", "5", "6", "5.1", "8.2", "8.3", "9", "10.4"}
    assert supp_refs == expected_refs, (
        f"supp reference set drifted: {sorted(supp_refs)}"
    )
    unresolved = sorted(r for r in supp_refs if r not in v37_heads)
    assert not unresolved, f"supp refs unresolved in v37: {unresolved}"

    # 5e. the three remapped references point at the right headings
    assert "## 9. The Delayed-Recruitment (Maturation-Delay) System" in t37
    assert "### 8.3 The registered numerical families" in t37
    assert "### 8.2 The attractor topology and the lower boundary" in t37
    assert "### 5.1 Local crossings and interval-certified delays" in t37
    assert "### 10.4 The saturating-gate negative screen" in t37

    # 5f. the S12 label-mapping targets all exist in v37
    for lab in (
        "Remark 5.1", "Corollary 5.1", "Proposition 6.1", "Theorem 4.1",
        "Lemma 2.1", "Theorem 10.1",
    ):
        assert lab in t37, f"S12 label target missing from v37: {lab}"

    # 5g. the paper points at the supplement that exists and is aligned
    assert PAPER_NEW in t37 and SUPP6.exists() and PAPER_NEW == SUPP6.name
    assert PAPER_OLD not in t37

    # 5h. the mirror-consistency gate: the main text's own statements about
    #     the supplement (Data availability + Supplementary paragraph) use
    #     the same section numbers the remapped supplement now uses
    assert "the Section 9 records (gate log and fine-map table, " \
        "Supplementary S9)" in t37
    assert "relocated from Sections 8.3 and 10.4" in t37

    # ---------- 6. version discipline: priors untouched ------------------------
    assert md5(V36) == v36_md5_before, "v36 was modified!"
    assert md5(SUPP5) == supp5_md5_before, "supp v5 was modified!"

    print("make_v37: ALL CHECKS PASS")
    print(f"  paper4_delay_dynamics_v37.md   "
          f"({V37.stat().st_size} bytes; one line changed: the "
          f"supplementary pointer)")
    print(f"  paper4_supplementary_v6.md     "
          f"({SUPP6.stat().st_size} bytes; three lines changed: the "
          f"remapped main-paper references 7->9, 9.3->8.3, 9.2->8.2)")
    print(f"  v36 md5 {v36_md5_before} and supp v5 md5 {supp5_md5_before} "
          f"unchanged on disk")
    return 0


if __name__ == "__main__":
    sys.exit(main())
