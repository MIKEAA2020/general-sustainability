#!/usr/bin/env python3
"""Wave-21 / Task 97, part 1: author paper4_delay_dynamics_v38.md and
paper4_supplementary_v7.md.

Owner directive (this round): "1- v38 reference round, the retitle, the
DOI list.  2- check for and remove change-long diary, meta-commentary,
self-referential, internal dialogue, informal chat artifacts, etc."

Directive 1 as commissioned this round = the Task-96 recommended v38
reference round (humanizing audits/V37_JOURNAL_FIT_EVALUATION.md,
Part V): add Adamson & Hilker (2020) at Section 1.1's lineage paragraph
(the missing delayed-knowledge modelling link between Moxnes 1998 and
Ostrom 1990), echo it once at Section 11.2's echo sentence (their
harvester-forecasting damping versus this paper's review-interval
control), and add Hocherman, Trop & Ghermandi (2025) cited at the three
"documented 2-13 yr governance-lag distribution" sites (Sections 9.3,
11.4, 11.7), which simultaneously resolves the supplementary S4
dangling citation.  References 36 -> 38 entries.  The retitle and the
owner-supplied DOI list remain blocked owner-level items (no title and
no list were supplied); the two NEW reference entries carry
web-search-verified DOIs (Adamson & Hilker:
doi:10.1007/s12080-020-00462-x, Theoretical Ecology 13, 425-434 ---
five independent sources, Task 96; Hocherman, Trop & Ghermandi:
doi:10.1007/s13280-025-02211-y, Ambio 54(12), 2042-2059 --- Springer,
PubMed and PMC records verified this round).

Directive 2 = the artifact-class removal pass over the shipped
deliverables.  The machine scan (six artifact classes: changelog diary /
editing history, meta-commentary announcements, self-referential process
references, internal dialogue, informal chat artifacts, process date
stamps) found the paper's certification-honesty register ("registered",
"recorded", "recovered", "re-execution-verified") clean throughout, and
exactly these genuine artifacts:

  paper v37:
    L485  "One point is stated once, at the outset." -- the writing
          process announcing itself; the following sentence carries the
          content unchanged
    L590  "are relocated to the supplement (S11)" -- editing-history
          verb; the paper's own register is "deposited"
    L712  "the relocated MPF sweep" -- same editing-history adjective
    L902  "the relocated MPF material of S11 (...; relocated from
          Sections 8.3 and 10.4)" -- narrates the document's own
          restructuring past
    L315  "is now established" / L776 "now registered" -- change-of-
          state diary ("previously open, NOW established"); the status
          stands without the "now"
  supplementary v6:
    L21/L163(x2)/L196  "the committed pipeline/coefficients/fundamental
          pair/certificates" -- repository-speak; replaced by the
          paper's register (deposited / registered / plain statement)
    L93/L103  "carried over from the audit document" and "stated in full
          in the audit document" (+ "(verified 2026-09-03; audit
          `audits/tikhonov_unh_verification.md`)" -- dangling internal
          pointers to a file NOT deposited in the supplementary package,
          plus a process date stamp
    L93/L103/L135  "now established/verified" -- same change-of-state
          diary class
    L215/L217  the S11 heading "Relocated MPF Material" and "Material
          relocated from the main article's Section 8.3" -- editing
          history; the section is retitled "MPF Material", matching the
          main text's own phrase "the MPF material of S11"
    L229  "stated where it belongs ... with the relocated material" --
          placement-justification meta-commentary
    L73   "the Hocherman (2025) synthesis" -- single-author citation
          form for a three-author paper; corrected to the house form
          (Hocherman, Trop, and Ghermandi, 2025) to match the new main
          reference entry
  references block formatting: the Åström and Aiello entries share one
    paragraph (single newline) while every other entry is
    paragraph-separated, and a double blank line sits between Aiello and
    Beretka -- normalised to the uniform entry/blank/entry form while
    the block is open for the two insertions.

The abstract is deliberately BYTE-IDENTICAL.  The Task-96 record flagged
the opening phrase "those studied so far are ecological" for an
exactness re-check ("an owner decision at commission time") with the
suggested repair "ecological or informational" --- which adds two
journal words (258 -> 260), violating the standing below-260 bound; the
owner's commission message supplies no ruling, and the sentence remains
defensible under the Section 12 reading (it compresses "Delays in the
ecological dynamics of harvested stocks are the classical subject of
delayed-logistic and delayed-recruitment analysis", with the
delayed-knowledge line presented in Section 1.1 as the modelling
counterpart on the institutional side of that contrast).  The re-check
was performed and recorded; the decision stays with the owner (a
one-line v39 if ruled in, with the 2-word cost or a compensating trim).

FROZEN (machine-checked): everything else.  All 1,473 math spans
byte-identical; the title, keywords, abstract (258 journal words),
declarations, Data availability and figure byte-identical; the heading
skeleton identical; the section-reference multiset loses only the one
removed "Sections 8.3 and 10.4" construct; content numerics change only
by the declared reference-entry/citation tokens and the filename
version digit; the supplement's internal S1-S12 structure and
object-label inventory unchanged; all eight supplement-to-main-paper
section references still resolve.

Idempotent; v37 and the v6 supplement are never modified (version
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

V37 = PR / "paper4_delay_dynamics_v37.md"
V38 = PR / "paper4_delay_dynamics_v38.md"
SUPP6 = PR / "paper4_supplementary_v6.md"
SUPP7 = PR / "paper4_supplementary_v7.md"

# --- the paper edits (14 anchored replacements) -------------------------------
PAPER_EDITS: list[tuple[str, str, str]] = [
    (
        "(Moxnes, 1998). Institutional design determines which signals "
        "reach which actors at which time (Ostrom, 1990).",
        "(Moxnes, 1998). The modelling counterpart treats the delay as "
        "one of knowledge: delayed knowledge of the harvested population "
        "state destabilises bioeconomic equilibria and induces "
        "resource-harvester cycles, which harvester forecasting can "
        "dampen (Adamson and Hilker, 2020). Institutional design "
        "determines which signals reach which actors at which time "
        "(Ostrom, 1990).",
        "E1  S1.1 lineage: the Adamson & Hilker delayed-knowledge link",
    ),
    (
        "One point is stated once, at the outset. Periodic review is a "
        "*hybrid* system",
        "Periodic review is a *hybrid* system",
        "E2  S7 opening: meta-commentary sentence removed",
    ),
    (
        "whose fast-block uniform normal hyperbolicity is now "
        "established as the proposition of S5",
        "whose fast-block uniform normal hyperbolicity is established as "
        "the proposition of S5",
        "E3  Remark 5.1 (H1): change-of-state 'now' removed",
    ),
    (
        "are relocated to the supplement (S11)",
        "are deposited in the supplement (S11)",
        "E4  S8.3: editing-history verb -> the deposit register",
    ),
    (
        "The $g=2$ window lies inside the documented $2$–$13$ yr "
        "governance-lag distribution with a decadal",
        "The $g=2$ window lies inside the documented $2$–$13$ yr "
        "governance-lag distribution (Hocherman, Trop, and Ghermandi, "
        "2025) with a decadal",
        "E5  S9.3: Hocherman citation (governance-lag site 1)",
    ),
    (
        "which also carries the relocated MPF sweep and intermittency "
        "records",
        "which also carries the MPF sweep and intermittency records",
        "E6  S10.4: editing-history adjective removed",
    ),
    (
        "and it supplies the missing dynamical content to the "
        "observation that institutional timing structures resource "
        "governance (Ostrom, 1990).",
        "and it supplies the missing dynamical content to the "
        "observation that institutional timing structures resource "
        "governance (Ostrom, 1990). Where harvester forecasting can "
        "dampen the cycles induced by delayed knowledge of the harvested "
        "population state (Adamson and Hilker, 2020), the review "
        "interval is the design variable analysed here.",
        "E7  S11.2 echo: the A&H forecasting/cadence contrast",
    ),
    (
        "whose $g=2$ $\\tau$-window lies inside the documented $2$–$13$ "
        "yr governance-lag distribution. And it supplies",
        "whose $g=2$ $\\tau$-window lies inside the documented $2$–$13$ "
        "yr governance-lag distribution (Hocherman, Trop, and Ghermandi, "
        "2025). And it supplies",
        "E8  S11.4: Hocherman citation (governance-lag site 2)",
    ),
    (
        "and the fold certification now registered for both folds",
        "and the fold certification registered for both folds",
        "E9  S11.5: change-of-state 'now' removed",
    ),
    (
        "the $g=2$ window is the one that lies inside the documented "
        "$2$–$13$ yr governance-lag distribution.",
        "the $g=2$ window is the one that lies inside the documented "
        "$2$–$13$ yr governance-lag distribution (Hocherman, Trop, and "
        "Ghermandi, 2025).",
        "E10 S11.7: Hocherman citation (governance-lag site 3)",
    ),
    (
        "Prentice Hall, Upper Saddle River.\nAiello, W.G., Freedman, "
        "H.I., 1990.",
        "Prentice Hall, Upper Saddle River.\n\nAdamson, M.W., Hilker, "
        "F.M., 2020. Resource-harvester cycles caused by delayed "
        "knowledge of the harvested population state can be dampened by "
        "harvester forecasting. Theoretical Ecology 13, 425–434. "
        "doi:10.1007/s12080-020-00462-x\n\nAiello, W.G., Freedman, H.I., "
        "1990.",
        "E11a references: Adamson & Hilker entry inserted; the Aström/"
        "Aiello paragraph seam separated",
    ),
    (
        "Mathematical Biosciences 101(2), 139–153.\n\n\nBeretka",
        "Mathematical Biosciences 101(2), 139–153.\n\nBeretka",
        "E11b references: double blank line normalised",
    ),
    (
        "J. Lond. Math. Soc. 25, 226–232.\n\nHutchings, J.A., Myers, "
        "R.A., 1994.",
        "J. Lond. Math. Soc. 25, 226–232.\n\nHocherman, T., Trop, T., "
        "Ghermandi, A., 2025. Time lags in environmental governance: a "
        "critical review. Ambio 54(12), 2042–2059. "
        "doi:10.1007/s13280-025-02211-y\n\nHutchings, J.A., Myers, R.A., "
        "1994.",
        "E12 references: Hocherman, Trop & Ghermandi entry inserted",
    ),
    (
        "are provided in the accompanying file `paper4_supplementary_v6."
        "md` (S1–S10), together with the relocated MPF material of S11 "
        "(the $\\eta_{\\mathrm{crit}}$ sweep and pair-birth structure, "
        "the slow-fast intermittency diagnostics, and the sigmoid-gated "
        "effort screen record; relocated from Sections 8.3 and 10.4).",
        "are provided in the accompanying file `paper4_supplementary_v7."
        "md` (S1–S10), together with the MPF material of S11 (the "
        "$\\eta_{\\mathrm{crit}}$ sweep and pair-birth structure, the "
        "slow-fast intermittency diagnostics, and the sigmoid-gated "
        "effort screen record).",
        "E13 Supplementary: pointer v6->v7 + editing-history clauses "
        "removed",
    ),
]

# --- the supplement edits (11 anchored replacements, 10 lines) ------------------
SUPP_EDITS: list[tuple[str, str, str]] = [
    (
        "the committed pipeline implements the outward-rounded "
        "coefficient/equilibrium/phase construction",
        "the deposited pipeline implements the outward-rounded "
        "coefficient/equilibrium/phase construction",
        "S1  S1.2: repository-speak 'committed' -> 'deposited'",
    ),
    (
        "the Hocherman (2025) synthesis of 101 studies",
        "the Hocherman, Trop, and Ghermandi (2025) synthesis of 101 "
        "studies",
        "S2  S4: three-author citation form",
    ),
    (
        "Two hypotheses are now established and one remains open; the "
        "remaining two are standard regularity hypotheses carried over "
        "from the audit document.",
        "Two hypotheses are established and one remains open; the "
        "remaining two are standard regularity hypotheses.",
        "S3  S5: diary 'now' + dangling audit-document clause removed",
    ),
    (
        "**Status of the hypotheses (verified 2026-09-03; audit "
        "`audits/tikhonov_unh_verification.md`).** The precise "
        "finite-time theorem — setting, hypotheses H1–H5, conclusion, "
        "and proof sketch (boundary layer on the fast clock with the "
        "delay as a slowly drifting parameter; retarded Gronwall "
        "closure) — is stated in full in the audit document. Two "
        "hypotheses are now established, one remains open:",
        "**Status of the hypotheses.** The precise finite-time theorem — "
        "setting, hypotheses H1–H5, conclusion, and proof sketch "
        "(boundary layer on the fast clock with the delay as a slowly "
        "drifting parameter; retarded Gronwall closure) — underlies the "
        "status list below; two hypotheses are established and one "
        "remains open:",
        "S4  S5: process date stamp + dangling audit-document pointer "
        "removed",
    ),
    (
        "the reduction conjecture's fast-block spectral condition is "
        "now verified (S5)",
        "the reduction conjecture's fast-block spectral condition is "
        "verified (S5)",
        "S5  S7: diary 'now' removed",
    ),
    (
        "At the committed gated Candidate A coefficients",
        "At the gated Candidate A coefficients",
        "S6a S8: repository-speak 'committed' dropped (values inline)",
    ),
    (
        "the committed fundamental pair is reproduced exactly",
        "the registered fundamental pair is reproduced exactly",
        "S6b S8: repository-speak 'committed' -> 'registered'",
    ),
    (
        "reproduces the committed P4 certificates",
        "reproduces the registered P4 certificates",
        "S7  S9.5: repository-speak 'committed' -> 'registered'",
    ),
    (
        "## S11. Relocated MPF Material",
        "## S11. MPF Material",
        "S8  S11 heading: the editing-history adjective removed (the "
        "main text's own phrase is 'the MPF material of S11')",
    ),
    (
        "Material relocated from the main article's Section 8.3",
        "Material from the main article's Section 8.3",
        "S9  S11 intro: editing-history verb removed",
    ),
    (
        "is stated where it belongs, in the main text's Section 10.4; "
        "this record is deposited here with the relocated material.",
        "is stated in the main text's Section 10.4; this record is "
        "deposited here.",
        "S10 S11 body: placement meta-commentary + editing-history clause "
        "removed",
    ),
]

# --- declared numeric deltas ---------------------------------------------------
# paper: stripped (section refs/headings/labels stripped) tokens
PAPER_NUM_ADD = Counter({
    "2020": 3, "2025": 4, "13": 1, "425": 1, "434": 1, "10.1007": 2,
    "12080": 1, "020": 1, "00462": 1, "54": 1, "12": 1, "2042": 1,
    "2059": 1, "13280": 1, "025": 1, "02211": 1, "7": 1,
})
PAPER_NUM_LOST = Counter({"6": 1})
# paper: raw (unstripped) tokens additionally lose the removed construct
PAPER_NUM_LOST_RAW = Counter({"6": 1, "8.3": 1, "10.4": 1})
# supplement: the removed date stamp only
SUPP_NUM_LOST = Counter({"2026": 1, "09": 1, "03": 1})

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
    # wave-21 artifact-class regression gates (directive 2)
    "One point is stated once", "stated once, at the outset",
    "relocated", "the committed", "audit document", "is now established",
    "now registered", "2026-09-03", "where it belongs",
]

SUPP_REJECTION = [
    "committed", "audit document", "audit `audits", "relocated",
    "2026-09-03", "now established", "is now verified", "where it "
    "belongs", "tikhonov_unh_verification",
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
    # every surviving occurrence of an old string must live inside a
    # replacement text (prefix-extension edits like the S11.2 echo
    # legitimately contain their own old form)
    for old, _new, tag in edits:
        allowed = sum(n.count(old) for _o, n, _t in edits)
        assert text.count(old) == allowed, (
            f"{label} old text survives outside the replacements: {tag}"
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
    v37_md5_before = md5(V37)
    supp6_md5_before = md5(SUPP6)
    t37 = V37.read_text(encoding="utf-8")
    s6 = SUPP6.read_text(encoding="utf-8")

    # ---------- 1. author v38 and supp v7 -------------------------------------
    t38 = apply_edits(t37, PAPER_EDITS, "paper")
    s7 = apply_edits(s6, SUPP_EDITS, "supp")

    if V38.exists():
        assert V38.read_text(encoding="utf-8") == t38, (
            "existing v38 differs from the idempotent regeneration"
        )
    V38.write_text(t38, encoding="utf-8")
    if SUPP7.exists():
        assert SUPP7.read_text(encoding="utf-8") == s7, (
            "existing supp v7 differs from the idempotent regeneration"
        )
    SUPP7.write_text(s7, encoding="utf-8")

    # ---------- 2. the paper battery ------------------------------------------
    # 2a. line-level accounting: 12 within-line edits + the reference-block
    #     restructuring (+3 insert / -1 blank / +2 insert = +4 lines)
    l37, l38 = t37.splitlines(), t38.splitlines()
    assert len(l38) - len(l37) == 4, (
        f"line-count delta {len(l38) - len(l37)} != +4"
    )
    same_pos = sum(1 for a, b in zip(l37, l38) if a == b)
    print(f"  paper lines: {len(l37)} -> {len(l38)} (+4: the two "
          f"reference entries with separators, minus the normalised "
          f"double blank); {same_pos} positions identical")

    # 2b. math spans byte-identical (multiset equality)
    assert Counter(spans(t38)) == Counter(spans(t37)), "math spans changed"
    print(f"  math spans: {len(spans(t38))} occurrences, multiset EXACTLY "
          "equal to v37's")

    # 2c. headings identical
    assert headings(t38) == headings(t37), "heading skeleton changed"

    # 2d. numeric discipline: the declared reference/citation tokens
    n37 = toks(strip_ref_contexts(t37))
    n38 = toks(strip_ref_contexts(t38))
    assert (n38 - n37) == PAPER_NUM_ADD, (
        f"stripped numeric delta: {dict(n38 - n37)}"
    )
    assert (n37 - n38) == PAPER_NUM_LOST, (
        f"stripped numeric loss: {dict(n37 - n38)}"
    )
    r37, r38 = toks(t37), toks(t38)
    assert (r38 - r37) == PAPER_NUM_ADD, "raw numeric delta drifted"
    assert (r37 - r38) == PAPER_NUM_LOST_RAW, "raw numeric loss drifted"
    print("  content numerics: the declared deltas only (2 reference "
          "entries + 5 in-text citations + the v7 filename digit; the "
          "stripped comparison loses only the removed 'Sections 8.3 and "
          "10.4' construct)")

    # 2e. word-token discipline: exactly the edits' own delta
    exp = expected_word_delta(PAPER_EDITS)
    got = Counter({k: v for k, v in
                   (words(t38) - words(t37)).items() if v > 0})
    got_lost = Counter({k: v for k, v in
                        (words(t37) - words(t38)).items() if v > 0})
    exp_add = Counter({k: v for k, v in exp.items() if v > 0})
    exp_lost = Counter({k: -v for k, v in exp.items() if v < 0})
    assert got == exp_add, (
        f"word delta mismatch: extra={dict(got - exp_add)} "
        f"missing={dict(exp_add - got)}"
    )
    assert got_lost == exp_lost, (
        f"word loss mismatch: {dict(got_lost - exp_lost)}"
    )
    for w, c in (("adamson", 3), ("hilker", 3), ("hocherman", 4),
                 ("trop", 4), ("ghermandi", 4), ("deposited", 1)):
        assert words(t38)[w] - words(t37)[w] == c, f"word {w} delta"
    assert words(t38)["relocated"] == 0 and words(t38)["now"] == 2
    print("  word tokens: exactly the declared edit delta (adamson+3, "
          "hilker+3, hocherman/trop/ghermandi+4 each, deposited+1, "
          "relocated 0, 'now' 4->2)")

    # 2f. section-reference multiset: only the removed construct
    sr37, sr38 = section_refs(t37), section_refs(t38)
    assert sr38 == sr37 - Counter({"8.3": 1, "10.4": 1}), (
        f"section-ref delta: {dict((sr37 - sr38) + (sr38 - sr37))}"
    )
    print(f"  section references: {sum(sr38.values())} (v37 minus the "
          "one removed 'Sections 8.3 and 10.4' construct)")

    # 2g. frozen blocks byte-identical
    for start, end in (
        ("# Delay-Induced Regime Change", "\n## Abstract"),
        ("## Abstract", "## 1. Introduction"),
        ("## Data availability", "## Declaration of competing interest"),
        ("## Declaration of competing interest", "## References"),
    ):
        assert block(t38, start, end) == block(t37, start, end), (
            f"frozen block changed: {start}"
        )
    fig37 = re.search(r"!\[Figure 1\].*?\n\n", t37, flags=re.S)
    fig38 = re.search(r"!\[Figure 1\].*?\n\n", t38, flags=re.S)
    assert fig37 and fig38 and fig37.group(0) == fig38.group(0), (
        "figure block changed"
    )
    print("  frozen blocks: title/abstract (258 journal words)/"
          "declarations/Data availability/figure byte-identical")

    # 2h. the references block: the declared construction, 38 entries
    rb37 = refs_block(t37)
    rb38 = refs_block(t38)
    expected_rb = rb37
    for old, new, _tag in PAPER_EDITS[10:13]:  # E11a, E11b, E12
        expected_rb = expected_rb.replace(old, new)
    assert rb38 == expected_rb, "references block drifted from the " \
        "declared construction"
    n_entries = sum(1 for ln in rb38.splitlines() if ln.strip())
    assert n_entries == 38, f"reference entries {n_entries} != 38"
    # uniform paragraph separation: no double blanks, no two entries in
    # one paragraph
    body = rb38.split("## References", 1)[1]
    assert "\n\n\n" not in body, "double blank survives in references"
    para_entries = [p for p in body.strip().split("\n\n") if p.strip()]
    assert all("\n" not in p.strip() for p in para_entries), (
        "two reference entries share a paragraph"
    )
    assert "Adamson, M.W., Hilker, F.M., 2020." in rb38
    assert "Hocherman, T., Trop, T., Ghermandi, A., 2025." in rb38
    print(f"  references: 36 -> 38 entries (Adamson & Hilker 2020 after "
          "Aström; Hocherman, Trop & Ghermandi 2025 after Hayes); "
          "paragraph separation uniform")

    # 2i. the Supplementary block: the declared construction
    sup37 = t37[t37.find("## Supplementary material"):]
    sup38 = t38[t38.find("## Supplementary material"):]
    expected_sup = sup37
    for old, new, _tag in PAPER_EDITS[13:14]:  # E13
        expected_sup = expected_sup.replace(old, new)
    assert sup38 == expected_sup, "Supplementary block drifted"
    assert t38.count("paper4_supplementary_v7.md") == 1
    assert "paper4_supplementary_v6.md" not in t38
    print("  Supplementary block: pointer v6->v7 with the "
          "editing-history clauses removed")

    # 2j. 'if and only if' still exactly five
    assert t38.count("if and only if") == 5, "'if and only if' count changed"

    # 2k. rejection list zero-hit (artifact-class regression gates in)
    hits = [b for b in REJECTION if b in t38]
    assert not hits, f"rejection hits in v38 md: {hits}"
    print(f"  rejection list: 0 hits ({len(REJECTION)} banned strings, "
          "incl. the 9 new artifact-class regression gates)")

    # 2l. abstract journal-word count unchanged (byte-identical)
    assert journal_words(t38) == journal_words(t37) == 258
    assert t38.split("## Abstract", 1)[1].split("## 1. Introduction")[0] \
        == t37.split("## Abstract", 1)[1].split("## 1. Introduction")[0]
    print("  abstract: 258 journal words, byte-identical (the exactness "
          "re-check recorded in the round deliverable; the owner-level "
          "decision stands)")

    # 2m. cross-reference resolver: 0 unresolved
    heads: set[str] = set()
    for h in headings(t38):
        m = re.match(r"^#{2,3} (\d+(?:\.\d+)?)", h)
        if m:
            heads.add(m.group(1))
            heads.add(m.group(1).split(".")[0])
    unresolved = sorted(r for r in section_refs(t38) if r not in heads)
    assert not unresolved, f"unresolved refs: {unresolved}"
    print("  cross-reference resolver: 0 unresolved Section constructs")

    # ---------- 3. the supplement battery ------------------------------------
    ls6, ls7 = s6.splitlines(), s7.splitlines()
    assert len(ls6) == len(ls7), "supp line count changed"
    d_lines = [
        i for i, (a, b) in enumerate(zip(ls6, ls7), 1) if a != b
    ]
    assert d_lines == [21, 73, 93, 103, 135, 163, 196, 215, 217, 229], (
        f"supp changed lines: {d_lines}"
    )
    print(f"  supplement: 10 changed lines (L163 carries two edits)")

    # 3b. internal S-structure: one declared heading-title change only
    exp_heads = supp_s_headings(s6)
    exp_heads = [
        "## S11. MPF Material" if h == "## S11. Relocated MPF Material"
        else h
        for h in exp_heads
    ]
    assert supp_s_headings(s7) == exp_heads, "S headings drifted"
    assert supp_object_labels(s7) == supp_object_labels(s6), (
        "supp object labels changed"
    )
    print("  supplement S-structure: S1-S12 unchanged except the declared "
          "S11 title 'Relocated MPF Material' -> 'MPF Material'; "
          "object-label inventory unchanged")

    # 3c. numeric discipline: the removed date stamp only
    sn6, sn7 = toks(s6), toks(s7)
    assert (sn7 - sn6) == Counter(), dict(sn7 - sn6)
    assert (sn6 - sn7) == SUPP_NUM_LOST, dict(sn6 - sn7)
    print("  supplement numerics: the removed (verified 2026-09-03) date "
          "stamp only (-2026, -09, -03)")

    # 3d. word-token discipline
    exp_s = expected_word_delta(SUPP_EDITS)
    got_s = Counter({k: v for k, v in
                     (words(s7) - words(s6)).items() if v > 0})
    got_s_lost = Counter({k: v for k, v in
                          (words(s6) - words(s7)).items() if v > 0})
    exp_s_add = Counter({k: v for k, v in exp_s.items() if v > 0})
    exp_s_lost = Counter({k: -v for k, v in exp_s.items() if v < 0})
    assert got_s == exp_s_add, f"supp word delta: {dict(got_s - exp_s_add)}"
    assert got_s_lost == exp_s_lost, "supp word loss drifted"
    assert words(s7)["committed"] == 0 and words(s7)["relocated"] == 0
    print("  supplement words: exactly the declared edit delta "
          "(committed 4->0, relocated 3->0, audit/document clauses "
          "removed, Trop/Ghermandi added)")

    # 3e. every supplement -> main-paper section reference resolves
    refs = supp_section_refs(s7)
    assert refs == {"2.3", "5", "6", "5.1", "8.2", "8.3", "9", "10.4"}, (
        sorted(refs)
    )
    unresolved = sorted(r for r in refs if r not in heads)
    assert not unresolved, f"supp refs unresolved: {unresolved}"
    print("  all eight supplement -> main-paper section references "
          "resolve against v38's headings")

    # 3f. artifact-class regression gates
    hits_s = [b for b in SUPP_REJECTION if b in s7]
    assert not hits_s, f"artifact hits in supp v7: {hits_s}"
    assert "the Hocherman, Trop, and Ghermandi (2025) synthesis" in s7
    print(f"  supplement artifact gates: 0 hits "
          f"({len(SUPP_REJECTION)} banned strings)")

    # 3g. mirror consistency with the main text's own statements
    assert "the Section 9 records (gate log and fine-map table, " \
        "Supplementary S9)" in t38
    assert "together with the MPF material of S11" in t38
    assert "Material from the main article's Section 8.3" in s7
    assert "## S11. MPF Material" in s7
    assert "Every value below is reproduced verbatim from the main " \
        "text" in s7
    print("  mirror consistency: the main text's Data availability and "
          "Supplementary paragraph agree with the supplement's own "
          "references")

    # 3h. the paper points at the supplement that exists
    assert SUPP7.exists() and "paper4_supplementary_v7.md" == SUPP7.name

    # ---------- 4. version discipline: priors untouched ------------------------
    assert md5(V37) == v37_md5_before, "v37 was modified!"
    assert md5(SUPP6) == supp6_md5_before, "supp v6 was modified!"

    print("\nmake_v38: ALL CHECKS PASS")
    print(f"  paper4_delay_dynamics_v38.md   "
          f"({V38.stat().st_size} bytes; 14 anchored edits)")
    print(f"  paper4_supplementary_v7.md     "
          f"({SUPP7.stat().st_size} bytes; 11 anchored edits, 10 lines)")
    print(f"  v37 md5 {v37_md5_before} and supp v6 md5 "
          f"{supp6_md5_before} unchanged on disk")
    return 0


if __name__ == "__main__":
    sys.exit(main())
