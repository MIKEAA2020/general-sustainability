#!/usr/bin/env python3
"""Wave-24 / Task 102, part 1: author paper4_delay_dynamics_v41.md --- the
DOI insertion round plus the abstract honesty decision.

Owner directives (this round): (1) the journal portal wants the main
manuscript as a LaTeX zip that compiles into a PDF for peer review
(served from this v41 by wave24/build_submission_zip_v41.py); (2) insert
the DOIs; (3) for the abstract phrase, choose honesty, and keep the
abstract below 260 words.

Directive 2 --- the 16 missing journal-article DOIs of the 38-entry
reference list, every one Crossref-verified in the Task-100 round
(humanizing audits/V41_COVER_LETTER_AND_VERIFIED_DOI_LIST.md, Part II:
title, container, volume and pages matched against the manuscript's
entries; never guessed), are pasted as anchored ` doi:` suffixes in
exactly the verified form.  The 7 already-pinned DOIs are untouched.
The 11 books (a style decision --- Theoretical Ecology's reference style
does not require book DOIs) and the 2 DFO grey-literature entries (no
DOI exists) stay as they are.  The frozen-reference gate re-baselines:
v38 == v39 == v40 -> v41 == v40 + the 16 declared appends.

Directive 3 --- Task 97's standing abstract-phrase flag, resolved by the
owner's word: "choose honesty".  The abstract's opening claim "those
studied so far are ecological" overstates once Adamson & Hilker (2020)
is cited (delayed KNOWLEDGE is an informational delay, not an ecological
one), so the honest form "ecological or informational" goes in.  V38
priced the upgrade at +2 journal words (258 -> 260, breaching the
standing below-260 bound), so the owner's paired directive ("keep
abstract below 260 words") is met by V38's recorded option: the upgrade
plus a compensating one-word trim --- "Under periodic review the two
rules respond oppositely" -> "Under periodic review the rules respond
oppositely" (only two rules exist; the count is carried by paragraph
one's "compares two rules"; zero content loss).  Net +1 journal word:
258 -> 259.

Paper edits (v40 -> v41): 18 anchored edits, one per line, no
line-count change:
  A1  "those studied so far are ecological."
      -> "those studied so far are ecological or informational."
  A2  "Under periodic review the two rules respond oppositely"
      -> "Under periodic review the rules respond oppositely"
  R1..R16  the 16 reference entries gain their verified
      " doi:<DOI>" suffix after the terminal period.

FROZEN (machine-checked): everything else.  All 1,473 math spans
byte-identical; the title, keywords, declarations, Data availability,
figure, heading skeleton and the Supplementary material paragraph
byte-identical; the abstract byte-identical outside the two declared
edits (259 journal words after them); the References block byte-identical
outside the 16 declared appends (38 entries; 23 "doi:" suffixes after
this round); the v8 supplement untouched with all eight of its section
references resolving against v41's headings.

The old abstract phrase (with its terminal period, so the new honest
form can never match it) and the trimmed "the two rules respond
oppositely" join the rejection list as wave-24 regression gates.

Idempotent; v40 is never modified (version discipline).
"""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "wave23"))
from make_v40 import (  # noqa: E402
    REJECTION as REJECTION_BASE,
    SUPP_REJECTION as SUPP_REJECTION_BASE,
    TITLE,
)

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"

V40 = PR / "paper4_delay_dynamics_v40.md"
V41 = PR / "paper4_delay_dynamics_v41.md"
SUPP8 = PR / "paper4_supplementary_v8.md"

# --- the 16 Crossref-verified DOIs (V41 Part II; pasted verbatim) ---------------
# (the unique reference-entry tail in v40, the verified DOI, the entry)
DOI_INSERTIONS: list[tuple[str, str, str]] = [
    ("Mathematical Biosciences 101(2), 139–153.",
     "10.1016/0025-5564(90)90019-u", "Aiello & Freedman 1990"),
    ("Science 332, 1079–1082.",
     "10.1126/science.1203672", "Carpenter et al. 2011"),
    ("Physica D 429, 133072.",
     "10.1016/j.physd.2021.133072", "Church & Lessard 2022"),
    ("J. Dyn. Differ. Equ. 36, 3385–3439.",
     "10.1007/s10884-023-10279-x", "Church & Queirolo 2024"),
    ("Nature 375, 227–230.",
     "10.1038/375227a0", "Costantino et al. 1995"),
    ("ACM Trans. Math. Softw. 28, 1–21.",
     "10.1145/513001.513002", "Engelborghs et al. 2002"),
    ("J. Differ. Equ. 122, 181–200.",
     "10.1006/jdeq.1995.1144", "Faria & Magalhães 1995"),
    ("Nature 287, 17–21.",
     "10.1038/287017a0", "Gurney et al. 1980"),
    ("Manag. Sci. 44, 1234–1248.",
     "10.1287/mnsc.44.9.1234", "Moxnes 1998"),
    ("Trends Ecol. Evol. 18, 648–656.",
     "10.1016/j.tree.2003.09.002", "Scheffer & Carpenter 2003"),
    ("Nature 461, 53–59.",
     "10.1038/nature08227", "Scheffer et al. 2009"),
    ("Nonlinear Dyn. 73, 2119–2131.",
     "10.1007/s11071-013-0928-2", "Zhang, Shen & Chen 2013"),
    ("Q. J. Econ. 52, 255–280.",
     "10.2307/1881734", "Ezekiel 1938"),
    ("J. Lond. Math. Soc. 25, 226–232.",
     "10.1112/jlms/s1-25.3.226", "Hayes 1950"),
    ("Ann. N.Y. Acad. Sci. 50, 221–246.",
     "10.1111/j.1749-6632.1948.tb39854.x", "Hutchinson 1948"),
    ("J. Anim. Ecol. 47, 315–332.",
     "10.2307/3939", "Ludwig, Jones & Holling 1978"),
]

# --- the abstract edits (directive 3: honesty + the below-260 bound) ------------
ABSTRACT_EDITS: list[tuple[str, str, str]] = [
    (
        "those studied so far are ecological.",
        "those studied so far are ecological or informational.",
        "A1  the honesty upgrade (Task 97's flag resolved: choose "
        "honesty; delayed knowledge is an informational delay)",
    ),
    (
        "Under periodic review the two rules respond oppositely",
        "Under periodic review the rules respond oppositely",
        "A2  the compensating one-word trim (V38's recorded option; "
        "keeps the abstract below 260 words; zero content loss)",
    ),
]

# --- the full edit list (review_v41 imports this order) -------------------------
PAPER_EDITS: list[tuple[str, str, str]] = [
    (
        old,
        old + " doi:" + doi,
        f"R   {entry}: the Crossref-verified DOI appended",
    )
    for old, doi, entry in DOI_INSERTIONS
] + ABSTRACT_EDITS

# --- declared numeric deltas: exactly the DOI strings' own digits ---------------
APPENDED_DOI_TEXT = " ".join(" doi:" + doi for _, doi, _ in DOI_INSERTIONS)
PAPER_NUM_ADD = Counter(re.findall(r"\d+(?:\.\d+)?", APPENDED_DOI_TEXT))
PAPER_NUM_LOST = Counter()
PAPER_NUM_LOST_RAW = Counter()

REJECTION = REJECTION_BASE + [
    # wave-24 regression gates: the pre-honesty abstract form (terminal
    # period included, so the new honest form can never match it) and
    # the trimmed phrase must never return
    "those studied so far are ecological.",
    "the two rules respond oppositely",
]
SUPP_REJECTION = SUPP_REJECTION_BASE


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
        r"(?:(?:\s*,\s*(?:\s+and\s+)?|\s+and\s+|--|–)\d+(?:\.\d+)?)*",
        " ", t)
    t = re.sub(r"^#{2,3} \d+(?:\.\d+)?[^\n]*$", " ", t, flags=re.M)
    t = re.sub(
        r"\*\*(?:Theorem|Proposition|Lemma|Corollary|Remark|Definition) "
        r"\d+(?:\.\d+)?\*\*", " ", t)
    return t


def section_refs(t: str) -> Counter:
    c: Counter = Counter()
    for m in re.finditer(
        r"Sections?((?:\s+\d+(?:\.\d+)?)(?:(?:\s*,\s*(?:\s+and\s+)?"
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
        r"Section[s]?((?:\s+\d+(?:\.\d+)?)(?:(?:\s*,\s*(?:\s+and\s+)?"
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
    for old, new, tag in edits:
        if old in new:
            # an append edit: the anchor survives exactly once, as the
            # prefix of its own replacement
            assert text.count(old) == 1, (
                f"{label} anchor count drifted after append ({tag}): "
                f"{text.count(old)}"
            )
        else:
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
    v40_md5_before = md5(V40)
    supp8_md5_before = md5(SUPP8)
    t40 = V40.read_text(encoding="utf-8")
    s8 = SUPP8.read_text(encoding="utf-8")
    assert journal_words(t40) == 258, "v40's abstract is not the 258-word form"

    # ---------- 1. author v41 --------------------------------------------------
    t41 = apply_edits(t40, PAPER_EDITS, "paper")

    if V41.exists():
        assert V41.read_text(encoding="utf-8") == t41, (
            "existing v41 differs from the idempotent regeneration"
        )
    V41.write_text(t41, encoding="utf-8")

    # ---------- 2. the paper battery ------------------------------------------
    # 2a. line-level accounting: exactly 18 lines differ, count unchanged
    l40, l41 = t40.splitlines(), t41.splitlines()
    assert len(l41) == len(l40), (
        f"line-count delta {len(l41) - len(l40)} != 0"
    )
    d_lines = [i for i, (a, b) in enumerate(zip(l40, l41), 1) if a != b]
    expected_lines = set()
    for ln_no, ln in enumerate(l40, 1):
        if "those studied so far are ecological." in ln:
            expected_lines.add(ln_no)
        if "Under periodic review the two rules respond oppositely" in ln:
            expected_lines.add(ln_no)
        for old, _doi, _entry in DOI_INSERTIONS:
            if old in ln:
                expected_lines.add(ln_no)
    assert set(d_lines) == expected_lines, (
        f"changed lines {d_lines} != the 18 anchored sites "
        f"{sorted(expected_lines)}"
    )
    assert len(d_lines) == 18, f"expected 18 changed lines, got {len(d_lines)}"
    # every unchanged line byte-identical (no reflow anywhere)
    for i, (a, b) in enumerate(zip(l40, l41), 1):
        if i not in expected_lines:
            assert a == b, f"line {i} drifted outside the declared edits"
    print(f"  paper lines: {len(l40)} -> {len(l41)} (exactly 18 lines "
          "changed: 2 abstract + 16 reference; everything else "
          "byte-identical)")

    # 2b. math spans byte-identical (multiset equality)
    assert Counter(spans(t41)) == Counter(spans(t40)), "math spans changed"
    print(f"  math spans: {len(spans(t41))} occurrences, multiset EXACTLY "
          "equal to v40's (the edits carry no math)")

    # 2c. headings identical; the title stands
    assert headings(t41) == headings(t40), "heading skeleton changed"
    assert t41.split("\n", 1)[0] == f"# {TITLE}", "H1 is not the title"

    # 2d. numeric discipline: exactly the 16 DOI strings' own digits
    n40 = toks(strip_ref_contexts(t40))
    n41 = toks(strip_ref_contexts(t41))
    assert (n41 - n40) == PAPER_NUM_ADD, (
        f"stripped numeric delta: {dict(n41 - n40)}"
    )
    assert (n40 - n41) == PAPER_NUM_LOST, (
        f"stripped numeric loss: {dict(n40 - n41)}"
    )
    r40, r41 = toks(t40), toks(t41)
    assert (r41 - r40) == PAPER_NUM_ADD, "raw numeric delta drifted"
    assert (r40 - r41) == PAPER_NUM_LOST_RAW, "raw numeric loss drifted"
    print(f"  content numerics: the declared delta only (the 16 DOI "
          f"strings' own digits, {sum(PAPER_NUM_ADD.values())} tokens; "
          "nothing else)")

    # 2e. word-token discipline: exactly the edits' own delta
    exp = expected_word_delta(PAPER_EDITS)
    got = Counter({k: v for k, v in
                   (words(t41) - words(t40)).items() if v > 0})
    got_lost = Counter({k: v for k, v in
                        (words(t40) - words(t41)).items() if v > 0})
    exp_add = Counter({k: v for k, v in exp.items() if v > 0})
    exp_lost = Counter({k: -v for k, v in exp.items() if v < 0})
    assert got == exp_add, (
        f"word delta mismatch: extra={dict(got - exp_add)} "
        f"missing={dict(exp_add - got)}"
    )
    assert got_lost == exp_lost, (
        f"word loss mismatch: {dict(got_lost - exp_lost)}"
    )
    assert words(t41)["informational"] - words(t40)["informational"] == 1
    assert words(t41)["or"] - words(t40)["or"] == 1
    assert words(t41)["two"] - words(t40)["two"] == -1
    print("  word tokens: exactly the declared delta (or/informational "
          "each +1 in the abstract, two -1 the compensating trim, the "
          "DOI letter-tokens; nothing else)")

    # 2f. the abstract: the two declared edits and nothing else; the
    #     below-260 bound held at 259
    a40 = block(t40, "## Abstract", "## 1. Introduction")
    a41 = block(t41, "## Abstract", "## 1. Introduction")
    expected_a41 = a40
    for old, new, _tag in ABSTRACT_EDITS:
        assert expected_a41.count(old) == 1
        expected_a41 = expected_a41.replace(old, new)
    assert a41 == expected_a41, "the abstract drifted beyond the 2 edits"
    assert journal_words(t41) == 259, (
        f"abstract is {journal_words(t41)} journal words, not 259"
    )
    assert journal_words(t41) < 260, "the below-260 bound is breached"
    print("  abstract: 258 -> 259 journal words (the honest upgrade +2, "
          "the compensating trim -1); byte-identical outside the 2 "
          "declared edits; the below-260 bound held")

    # 2g. frozen blocks byte-identical
    for start, end in (
        ("## Data availability", "## Declaration of competing interest"),
        ("## Declaration of competing interest", "## References"),
    ):
        assert block(t41, start, end) == block(t40, start, end), (
            f"frozen block changed: {start}"
        )
    fig40 = re.search(r"!\[Figure 1\].*?\n\n", t40, flags=re.S)
    fig41 = re.search(r"!\[Figure 1\].*?\n\n", t41, flags=re.S)
    assert fig40 and fig41 and fig40.group(0) == fig41.group(0), (
        "figure block changed"
    )
    kw40 = t40.split("**Keywords:**")[1].split("\n", 1)[0]
    kw41 = t41.split("**Keywords:**")[1].split("\n", 1)[0]
    assert kw41 == kw40, "keywords changed"
    print("  frozen blocks: keywords/declarations/Data availability/"
          "figure byte-identical")

    # 2h. the References block: the 16 declared appends and nothing else
    rb40 = refs_block(t40)
    rb41 = refs_block(t41)
    expected_rb41 = rb40
    for old, doi, _entry in DOI_INSERTIONS:
        assert expected_rb41.count(old) == 1
        expected_rb41 = expected_rb41.replace(old, old + " doi:" + doi)
    assert rb41 == expected_rb41, (
        "the References block drifted beyond the 16 declared appends"
    )
    n_entries = sum(1 for ln in rb41.splitlines() if ln.strip())
    assert n_entries == 38, f"reference block lines {n_entries} != 38"
    assert rb41.count("doi:") == 23, (
        f"doi: suffix count {rb41.count('doi:')} != 23 (7 pinned + 16 new)"
    )
    for pinned in (
        "doi:10.1007/s12080-020-00462-x",
        "doi:10.1016/j.jde.2020.03.039",
        "doi:10.1007/s13280-025-02211-y",
        "doi:10.1139/f94-214",
        "doi:10.1080/02755947.2016.1167145",
        "doi:10.1002/mcf2.10221",
        "doi:10.1007/BF00182340",
    ):
        assert rb41.count(pinned) == 1, f"pinned DOI altered: {pinned}"
    print("  references block: byte-identical to v40's outside the 16 "
          "declared appends; 38 entries; 23 doi: suffixes (7 pinned "
          "untouched + 16 verified pasted); the frozen gate re-baselined "
          "v38==v39==v40 -> v41")

    # 2i. the Supplementary block byte-identical (the pointer stays v8)
    sup40 = t40[t40.find("## Supplementary material"):]
    sup41 = t41[t41.find("## Supplementary material"):]
    assert sup41 == sup40, "Supplementary block drifted"
    assert t41.count("paper4_supplementary_v8.md") == 1
    assert "paper4_supplementary_v7.md" not in t41
    print("  Supplementary block: byte-identical (the pointer stays at the "
          "unchanged v8 supplement)")

    # 2j. 'if and only if' still exactly five
    assert t41.count("if and only if") == 5, "'if and only if' count changed"

    # 2k. rejection list zero-hit (incl. the 2 new wave-24 gates)
    hits = [b for b in REJECTION if b in t41]
    assert not hits, f"rejection hits in v41 md: {hits}"
    print(f"  rejection list: 0 hits ({len(REJECTION)} banned strings, "
          "incl. the 2 new wave-24 regression gates: the pre-honesty "
          "abstract form and the trimmed phrase)")

    # 2l. cross-reference resolver: 0 unresolved
    heads: set[str] = set()
    for h in headings(t41):
        m = re.match(r"^#{2,3} (\d+(?:\.\d+)?)", h)
        if m:
            heads.add(m.group(1))
            heads.add(m.group(1).split(".")[0])
    unresolved = sorted(r for r in section_refs(t41) if r not in heads)
    assert not unresolved, f"unresolved refs: {unresolved}"
    print("  cross-reference resolver: 0 unresolved Section constructs")

    # ---------- 3. the supplement battery (v8 unchanged this round) -----------
    assert md5(SUPP8) == supp8_md5_before, "supp v8 was modified!"
    s41_refs = supp_section_refs(s8)
    assert s41_refs == {"2.3", "5", "6", "5.1", "8.2", "8.3", "9", "10.4"}, (
        sorted(s41_refs)
    )
    unresolved_s = sorted(r for r in s41_refs if r not in heads)
    assert not unresolved_s, f"supp refs unresolved: {unresolved_s}"
    for phrase in SUPP_REJECTION:
        assert phrase not in s8, f"supp artifact: {phrase!r}"
    print("  supplement v8: untouched (md5 unchanged); all eight "
          "supplement -> paper references resolve against v41's headings")

    # ---------- 4. version discipline ------------------------------------------
    assert md5(V40) == v40_md5_before, "v40 was modified!"
    print(f"  version discipline: v40 untouched (md5 {v40_md5_before}); "
          f"v41 written ({md5(V41)})")

    print("\nmake_v41: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
