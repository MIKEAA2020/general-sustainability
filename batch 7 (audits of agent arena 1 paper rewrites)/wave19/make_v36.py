#!/usr/bin/env python3
"""Wave-19 / Task 93, part 1: author paper4_delay_dynamics_v36.md from
paper4_delay_dynamics_v35.md.

Owner directive (this round): the challenge to the Task-92 adjudication
("even the restructuring? ... provide v36") upgrades the batch-8
implementation plan from consolidation-only to restructuring-plus-
consolidation.  The restructuring layer is the one the three strategic
audits converge on (sol's recommended primary spine; qwen section 14;
sol2 section 19): the sampled-data review analysis is promoted to sit
directly after the two channel sections, the global numerics follow it,
and the ecological maturation-delay analogue becomes the comparative
chapter before the Discussion.

R (the restructuring):
  old section 7 (The Delayed-Recruitment (Maturation-Delay) System) -> 9
  old section 8 (The Review Interval as Control)                    -> 7
  old section 9 (Global Numerics at Declared Certification Levels)  -> 8
Every cross-reference is renumbered by a bijective token map (7 -> 9,
8 -> 7, 9 -> 8; 7.k -> 9.k; 9.k -> 8.k; old 7/9 own no numbered
theorem-like objects, so no label collisions exist); the three labels
of the promoted section follow their host (Theorem 8.1 -> Theorem 7.1,
Proposition 8.1 -> Proposition 7.1, Remark 8.1 -> Remark 7.1, plus the
"Propositions 6.2 and 8.1" list form); the Organization paragraph is
rewritten for the new argument arc.  No sentence inside the moved
blocks is altered beyond the declared renumbers (fragment round-trip
byte-conservation gate).  The Data availability and Supplementary
blocks carry section pointers, so their freeze is "identical modulo
the declared renumber map".

E1: the three dangling/incomplete section-1.2 cross-references repaired
    (4.2 -> 5.2, 4.4 -> 5.4, 6.2 -> "6.2 and 6.4") --- a paper defect
    present since v31 that all six audits missed --- plus the permanent
    cross-reference resolver gate.
E2: section 11.8(ii) completed --- the delay stages the single lag
    compresses, grounded in the cod chronology of section 11.4 (sol 5.1,
    sol2 4; zero new numeric values).
E3: section 11.9 completed --- parameter-box certification registered
    as the third stated open task (qwen 5.7/11.2, sol 7.3).
E4: section 11.8(i) completed --- the identification layer (deepseek 1),
    consolidating the paper's own identification admissions.

FROZEN (machine-checked): title, keywords, the 258-word abstract, all
36 references, the declarations, the figure block (byte-identical);
every math span byte-identical (multiset equality, empty whitelist);
numeric discipline = the declared section-reference permutation plus
the two E2 year tokens (+1992, +2024 --- both pre-existing values).

This script is fully reproducible from the repository alone and is
idempotent; v35 is never modified (version discipline).
"""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
V35 = PR / "paper4_delay_dynamics_v35.md"
V36 = PR / "paper4_delay_dynamics_v36.md"

V35_MD5 = "e9c99edbcf59cce80f2bd08c2966a74b"

NEW_ORG = """### 1.3 Organization

Section 2 defines the model class and its admissible domain. Section 3 derives equilibria and the characteristic equation. Section 4 develops the Hopf cubic and the even-pairs algebra. Section 5 analyses the mobilising channel, and Section 6 the protective channel; together they carry the sign separation — opposite local mathematics on the same stock–memory block. Section 7 treats sample-and-hold review: the review interval is a spectral design parameter in its own right, and the reviewed loop is a hybrid system, not the delay equation sampled at the review interval. Section 8 reports the global numerics and their certification levels. Section 9 registers the maturation-delayed recruitment system — the applied analogue in which the same governance structure acts on a stock whose own delay is the maturation lag from spawning to recruitment — and records the companion stage-analysis fine-map bands and their nonlinear ground truth. Section 10 unifies the two channels in the loop-gain family. Section 11 discusses design consequences, the generality of the institutional-loop coordinates, the documented institutional timelines that ground the two timing coordinates, the ecological reading of the registered records, the relation to the early-warning literature, and open problems. Section 12 concludes."""

E2_E4_ANCHOR = (
    "identified from them. (ii) The delay is a single discrete lag; "
    "distributed delays and variable-time institutional lags require "
    "separate analysis."
)
E2_E4_NEW = (
    "identified from them. Identification is its own layer: different "
    "gain–delay–memory triples can realise similar observed harvest "
    "trajectories, so the institutional coordinates are latent structural "
    "parameters — separable only through exogenous variation or direct "
    "process measurement, not from the observed trajectory alone — and the "
    "functional form of the response law is identified, if at all, "
    "separately from its parameters. (ii) The delay is a single discrete "
    "lag — a reduced compression of the observation, assessment, decision, "
    "deployment, and compliance stages that a multi-stage institution "
    "carries separately; the documented cod chronology of Section 11.4 "
    "(the annual assessment cycle, the 1992 moratorium decision, the 2024 "
    "reopening) is a record of such stages at management scale, and what "
    "the single lag absorbs is their composite timing, not any one stage. "
    "Distributed delays and variable-time institutional lags require "
    "separate analysis."
)

E3_ANCHOR = "none connects to a theorem proved in this paper."
E3_NEW = (
    "A third stated open task is parameter-box certification: the interval "
    "enclosures of Section 5.1 certify the registered decimal parameter "
    "vector, and the one-at-a-time windows of Section 8.5 are not boxes — "
    "extending the interval Newton stage from the point vector to declared "
    "parameter boxes is the upgrade that would carry the threshold "
    "statements from arithmetic precision to the policy robustness that "
    "Section 11.5 reserves to a sensitivity layer."
)

E1_EDITS = [
    ("both crossings subcritical (Section 4.2)",
     "both crossings subcritical (Section 5.2)"),
    ("a sufficiently large mobilising weight (Section 4.4)",
     "a sufficiently large mobilising weight (Section 5.4)"),
    ("provably not a Hopf of the continuous system (Section 6.2)",
     "provably not a Hopf of the continuous system (Sections 6.2 and 6.4)"),
]

# range/list constructs the token map cannot see (bare continuations
# and semantic ranges whose endpoints move under the rotation)
R_EDITS = [
    ("(Sections 5.1 and 9.3)", "(Sections 5.1 and 8.3)"),
    ("the model of Sections 2–7", "the model of Sections 2–6 and 9"),
    ("Sections 2.3, 7, and 9.3", "Sections 2.3, 9, and 8.3"),
]

# device/content needles at md level (each must appear in v36)
DEVICE_NEEDLES = [
    # the restructured spine
    "Section 7 treats sample-and-hold review",
    "together they carry the sign separation",
    "not the delay equation sampled at the review interval",
    "## 7. The Review Interval as Control",
    "## 8. Global Numerics at Declared Certification Levels",
    "## 9. The Delayed-Recruitment (Maturation-Delay) System",
    "### 9.1 The registered system",
    "### 9.6 Registration and status",
    "### 8.1 Methods",
    "### 8.6 The scaffold companion: registered and verified records",
    # renumbered pointers (spot proofs of the bijective map)
    "the registration counterpart of the reproduction targets of Section 8.6",
    "relocated from Sections 8.3 and 10.4",
    "the paper's reference records (Sections 5.1 and 8.3)",
    "the model of Sections 2–6 and 9",
    "Sections 2.3, 9, and 8.3",
    "stage-analysis machinery of Section 9 is archived verbatim",
    "(Theorem 7.1, Proposition 7.1)",
    "Propositions 6.2 and 7.1",
    "**What Theorem 7.1 says.**",
    "**What Proposition 7.1 says.**",
    # E1 repairs
    "both crossings subcritical (Section 5.2)",
    "a sufficiently large mobilising weight (Section 5.4)",
    "provably not a Hopf of the continuous system (Sections 6.2 and 6.4)",
    # E2 / E4 completions
    "Identification is its own layer",
    "latent structural parameters",
    "a reduced compression of the observation, assessment, decision, "
    "deployment, and compliance stages",
    "what the single lag absorbs is their composite timing, not any one "
    "stage",
    # E3 completion
    "A third stated open task is parameter-box certification",
    "the one-at-a-time windows of Section 8.5 are not boxes",
    # inherited load-bearing markers
    "The exposed life histories are doubly selected",
    "decoupled storage, not growth-coupled ecology, is what can slow the "
    "loop",
    "more frequent assessment is not always safer",
    "grounding scales, not coefficients",
    "if and only if",
]

CAVEAT_NEEDLES = [
    "A mesh-range caveat is registered with the fine map",
    "they are not a calibration, and no institutional coefficient is "
    "identified from them",
    "other discretisations have different monodromies, and the "
    "continuous-delay and periodic-review recommendations are not "
    "interchangeable",
    "(H5) non-feedback mass compartments stay outside the delay loop",
    "The saddle-node-of-periodic-orbits classification remains",
    "The reversed-gain linearisation has loop gain",
    "The stable arm is not generically reachable near the fold",
]

# rejection list: inherited fabrications + this round's banned coinages
BANNED = [
    "performance of alternative assessment frequencies",
    "fisheries management performance: A simulation approach",
    "Evaluation of management strategy performance under variable "
    "assessment intervals",
    "Effects of assessment frequency and harvest control rules",
    "ICES", "Fisheries Research",
    "183, 313", "313–323", "175, 94", "94–105", "42(4),", "843–861",
    "anchoveta", "sardine", "cephalopod", "haddock", "rockfish",
    "orange roughy", "deep-sea teleost", "large sharks",
    "12.1", "4.5, 12.1", "[4.5,", "0.2, 0.8", "[0.2, 0.8]",
    "N_min",
    "Global Stability", "narrow window", "saddle-node of limit cycles",
    "non-autonomous and spatial domains", "pure mobilizing governance",
    "mobilizing", "artifact", "stabilizing", "destabilizing",
    "plain name", "The message of the paper is stated plainly",
    "is collected in one display",
    # batch-8 round: the audited coinages and overclaims stay out
    "Sign Separation Theorem",
    "viability bleed", "phase-stabilisation trap", "phase-stabilization "
    "trap",
    "administrative hunting", "basin lock-in",
    "A stable eigenvalue is not a stable fishery",
    "A stable eigenvalue is not a sustainable resource system",
]


def renumber(t: str) -> str:
    """The bijective section map 7->9, 8->7, 9->8 (7.k->9.k, 9.k->8.k)
    plus the three label renumbers of the promoted section."""
    # labels of the promoted section (old 8 -> new 7); collision-free
    t = t.replace("Propositions 6.2 and 8.1", "Propositions 6.2 and 7.1")
    t = t.replace("Theorem 8.1", "Theorem 7.1")
    t = t.replace("Proposition 8.1", "Proposition 7.1")
    t = t.replace("Remark 8.1", "Remark 7.1")
    # cross-references: subsections first, placeholders break the cycle;
    # the plain guard (?![\d.] -> (?!=\.?\d) so sentence-final
    # 'Section 9.' still renumbers while 'Section 9.6' does not
    t = re.sub(r"(Sections? )7\.(\d+)", r"\g<1>@@A\g<2>@", t)
    t = re.sub(r"(Sections? )9\.(\d+)", r"\g<1>@@C\g<2>@", t)
    t = re.sub(r"(Sections? )7(?!\.?\d)", r"\g<1>@@A@", t)
    t = re.sub(r"(Sections? )8(?!\.?\d)", r"\g<1>@@B@", t)
    t = re.sub(r"(Sections? )9(?!\.?\d)", r"\g<1>@@C@", t)
    # headings
    t = re.sub(r"^## 7\.", "## @@A@.", t, flags=re.M)
    t = re.sub(r"^## 8\.", "## @@B@.", t, flags=re.M)
    t = re.sub(r"^## 9\.", "## @@C@.", t, flags=re.M)
    t = re.sub(r"^### 7\.(\d+)", lambda m: f"### @@A{m.group(1)}@", t, flags=re.M)
    t = re.sub(r"^### 9\.(\d+)", lambda m: f"### @@C{m.group(1)}@", t, flags=re.M)
    # resolve placeholders
    t = re.sub(r"@@A(\d)@", lambda m: "9." + m.group(1), t)
    t = re.sub(r"@@C(\d)@", lambda m: "8." + m.group(1), t)
    t = t.replace("@@A@", "9").replace("@@B@", "7").replace("@@C@", "8")
    assert "@@" not in t, "placeholder residue after renumber"
    return t


def inverse_renumber(t: str) -> str:
    """The exact inverse of renumber (round-trip byte-conservation)."""
    t = t.replace("Propositions 6.2 and 7.1", "Propositions 6.2 and 8.1")
    t = t.replace("Theorem 7.1", "Theorem 8.1")
    t = t.replace("Proposition 7.1", "Proposition 8.1")
    t = t.replace("Remark 7.1", "Remark 8.1")
    t = re.sub(r"(Sections? )9\.(\d+)", r"\g<1>@@A\g<2>@", t)
    t = re.sub(r"(Sections? )8\.(\d+)", r"\g<1>@@C\g<2>@", t)
    t = re.sub(r"(Sections? )9(?!\.?\d)", r"\g<1>@@A@", t)
    t = re.sub(r"(Sections? )7(?!\.?\d)", r"\g<1>@@B@", t)
    t = re.sub(r"(Sections? )8(?!\.?\d)", r"\g<1>@@C@", t)
    t = re.sub(r"^## 9\.", "## @@A@.", t, flags=re.M)
    t = re.sub(r"^## 7\.", "## @@B@.", t, flags=re.M)
    t = re.sub(r"^## 8\.", "## @@C@.", t, flags=re.M)
    t = re.sub(r"^### 9\.(\d+)", lambda m: f"### @@A{m.group(1)}@", t, flags=re.M)
    t = re.sub(r"^### 8\.(\d+)", lambda m: f"### @@C{m.group(1)}@", t, flags=re.M)
    t = re.sub(r"@@A(\d)@", lambda m: "7." + m.group(1), t)
    t = re.sub(r"@@C(\d)@", lambda m: "9." + m.group(1), t)
    t = t.replace("@@A@", "7").replace("@@B@", "8").replace("@@C@", "9")
    assert "@@" not in t, "placeholder residue after inverse renumber"
    return t


def tokens(s: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", s))


def strip_ref_contexts(t: str) -> str:
    """Remove heading lines, theorem-label phrases and Section
    cross-reference constructs (prefix, comma-lists, 'and'-lists,
    en-dash ranges), so the numeric discipline can compare pure
    content numbers."""
    t = re.sub(r"^#{2,3} \d+.*$", " ", t, flags=re.M)
    t = re.sub(
        r"(?:Theorem|Proposition|Corollary|Lemma|Remark)s? "
        r"\d+(?:\.\d+)?(?: and \d+(?:\.\d+)?)*",
        " ", t,
    )
    t = re.sub(
        r"Sections? \d+(?:\.\d+)?"
        r"(?:(?:\s*,\s*(?:and\s+)?|\s+and\s+|–)\d+(?:\.\d+)?)*",
        " ", t,
    )
    return t


def block_by_heading(t: str, start: str, end: str | None = None) -> str:
    lines = t.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.strip() == start)
    if end is None:
        return "\n".join(lines[i:]).rstrip("\n")
    j = next(k for k, ln in enumerate(lines) if ln.strip() == end)
    return "\n".join(lines[i:j]).rstrip("\n")


def journal_words(s: str) -> int:
    return sum(1 for w in re.findall(r"\S+", s) if re.search(r"[A-Za-z0-9]", w))


def section_refs(t: str) -> Counter:
    return Counter(re.findall(r"Sections? (\d+(?:\.\d+)?)", t))


def map_ref(r: str) -> str:
    if r.startswith("7."):
        return "9." + r[2:]
    if r.startswith("9."):
        return "8." + r[2:]
    return {"7": "9", "8": "7", "9": "8"}.get(r, r)


def strip_trailing_sep(b: str) -> str:
    """Drop a block's trailing '---' separator line (it belonged to a
    boundary that the rotation reassembles)."""
    b = b.rstrip()
    if b.endswith("\n---"):
        b = b[:-4].rstrip()
    return b


def main() -> int:
    t35 = V35.read_text(encoding="utf-8")
    assert hashlib.md5(V35.read_bytes()).hexdigest() == V35_MD5, "v35 drifted"
    text = t35

    # --- R: the three-block rotation -------------------------------------
    for h in ("## 7. ", "## 8. ", "## 9. ", "## 10. "):
        assert sum(1 for ln in text.split("\n") if ln.startswith(h)) == 1, h
    i7 = text.find("## 7. ")
    i8 = text.find("## 8. ")
    i9 = text.find("## 9. ")
    i10 = text.find("## 10. ")
    assert 0 < i7 < i8 < i9 < i10, "section boundaries out of order"
    pre, block7, block8, block9, post = (
        text[:i7], text[i7:i8], text[i8:i9], text[i9:i10], text[i10:],
    )
    # fragment byte-conservation: renumber is exactly invertible on each
    for name, frag in (("pre", pre), ("post", post), ("b7", block7),
                       ("b8", block8), ("b9", block9)):
        assert inverse_renumber(renumber(frag)) == frag, (
            f"round-trip failed for fragment {name}"
        )
    SEP = "\n\n---\n\n"
    text = (
        renumber(pre)
        + strip_trailing_sep(renumber(block8)) + SEP
        + strip_trailing_sep(renumber(block9)) + SEP
        + strip_trailing_sep(renumber(block7)) + SEP
        + renumber(post)
    )
    assert "\n---\n\n---\n" not in text and "---\n\n---" not in text, (
        "double separator after rotation"
    )

    # --- R2: the Organization paragraph ---------------------------------
    i = text.find("### 1.3 Organization")
    j = text.find("Section 12 concludes.") + len("Section 12 concludes.")
    assert 0 < i < j, "Organization paragraph not found"
    text = text[:i] + NEW_ORG + text[j:]

    # --- R3: range/list constructs the token map cannot see --------------
    for old, new in R_EDITS:
        assert text.count(old) == 1, f"R-edit anchor not unique: {old!r}"
        text = text.replace(old, new)

    # --- E1: cross-reference repairs -------------------------------------
    for old, new in E1_EDITS:
        assert text.count(old) == 1, f"E1 anchor not unique: {old!r}"
        text = text.replace(old, new)

    # --- E2 + E4: the limitations completions ---------------------------
    assert text.count(E2_E4_ANCHOR) == 1, "E2/E4 anchor not unique"
    text = text.replace(E2_E4_ANCHOR, E2_E4_NEW)

    # --- E3: the open-task registration ----------------------------------
    assert text.count(E3_ANCHOR) == 1, "E3 anchor not unique"
    text = text.replace(E3_ANCHOR, E3_ANCHOR + " " + E3_NEW)

    # ================= fail-loud battery =================================
    # 1. math spans: multiset EXACT equality with v35 (nothing added,
    #    nothing lost; the rotation only moves blocks)
    s35 = re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", t35, flags=re.S)
    s36 = re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", text, flags=re.S)
    assert Counter(s35) == Counter(s36), (
        f"math-span multiset differs: "
        f"lost={[s for s in s35 if Counter(s36)[s] < Counter(s35)[s]][:3]} "
        f"added={[s for s in s36 if s not in s35][:3]}"
    )

    # 2. numeric discipline on stripped content: v36 == v35 + {1992, 2024}
    n35s = tokens(strip_ref_contexts(t35))
    n36s = tokens(strip_ref_contexts(text))
    delta = n36s - n35s
    lost = {t: c for t, c in (n35s - n36s).items() if c > 0}
    assert not lost, f"content numeric tokens lost: {lost}"
    assert delta == Counter({"1992": 1, "2024": 1}), (
        f"unexpected content numeric delta: {dict(delta)}"
    )

    # 3. section-reference multiset: the bijective map + the E1/E3 deltas
    r35, r36 = section_refs(t35), section_refs(text)
    expected = Counter({map_ref(r): c for r, c in r35.items()})
    expected["4.2"] -= 1
    expected["4.4"] -= 1
    expected["5.2"] += 1
    expected["5.4"] += 1
    expected["5.1"] += 1   # E3
    expected["8.5"] += 1   # E3 (renumbered from the drafted 9.5)
    expected["11.4"] += 1  # E2
    expected["11.5"] += 1  # E3
    assert r36 == expected, (
        f"section-ref multiset mismatch: "
        f"missing={dict((expected - r36))} extra={dict((r36 - expected))}"
    )

    # 4. label renumber counts
    for lab, cnt in (("Theorem 7.1", 11), ("Proposition 7.1", 9),
                     ("Remark 7.1", 2), ("Propositions 6.2 and 7.1", 1)):
        assert text.count(lab) == cnt, f"label count {lab}: {text.count(lab)}"
    for lab in ("Theorem 8.1", "Proposition 8.1", "Remark 8.1"):
        assert text.count(lab) == 0, f"stale label remains: {lab}"

    # 5. heading skeleton: the three-block rotation with renumbers
    h35 = [ln.rstrip() for ln in t35.split("\n") if ln.startswith("#")]
    h36 = [ln.rstrip() for ln in text.split("\n") if ln.startswith("#")]
    a = h35.index("## 7. The Delayed-Recruitment (Maturation-Delay) System")
    b = h35.index("## 8. The Review Interval as Control")
    c = h35.index("## 9. Global Numerics at Declared Certification Levels")
    d = h35.index("## 10. The Loop-Gain Family")
    exp = (
        h35[:a]
        + [renumber(x) for x in h35[b:c]]
        + [renumber(x) for x in h35[c:d]]
        + [renumber(x) for x in h35[a:b]]
        + h35[d:]
    )
    assert h36 == exp, "heading skeleton differs from the declared rotation"
    assert h36.index("## 7. The Review Interval as Control") < h36.index(
        "## 8. Global Numerics at Declared Certification Levels"
    ) < h36.index("## 9. The Delayed-Recruitment (Maturation-Delay) System")

    # 6. the permanent cross-reference resolver (new gate): every number
    #    inside a Section construct (prefix, comma-list, and-list,
    #    en-dash range) must resolve to an existing heading
    heads = set(re.findall(r"^## (\d+)\.", text, re.M)) | set(
        re.findall(r"^### (\d+\.\d+)", text, re.M)
    )
    for m in re.finditer(
        r"Sections? (\d+(?:\.\d+)?)(?:(?:\s*,\s*(?:and\s+)?|\s+and\s+|–)\d+(?:\.\d+)?)*",
        text,
    ):
        for tgt in re.findall(r"\d+(?:\.\d+)?", m.group(0)[len("Sections"):]):
            assert tgt in heads, (
                f"unresolved cross-reference {tgt!r} in "
                f"{text[max(0, m.start()-60):m.end()+20]!r}"
            )

    # 7. frozen blocks
    assert text.split("\n", 1)[0] == t35.split("\n", 1)[0], "title changed"
    kw35 = [ln for ln in t35.split("\n") if ln.startswith("**Keywords:")][0]
    kw36 = [ln for ln in text.split("\n") if ln.startswith("**Keywords:")][0]
    assert kw35 == kw36, "keywords line changed"
    a35 = t35.split("## Abstract\n\n", 1)[1].split("\n\n**Keywords:**")[0]
    a36 = text.split("## Abstract\n\n", 1)[1].split("\n\n**Keywords:**")[0]
    assert a35 == a36, "abstract changed"
    aw = journal_words(a36)
    assert aw <= 259, f"abstract runs {aw} words"
    for start, end in (
        ("## Declaration of competing interest", "## References"),
        ("## References", "## Supplementary material"),
    ):
        assert block_by_heading(t35, start, end) == block_by_heading(
            text, start, end
        ), f"frozen block changed: {start}"
    # Data availability + Supplementary: identical modulo the renumber map
    for start, end in (
        ("## Data availability", "## Declaration of competing interest"),
        ("## Supplementary material", None),
    ):
        b35 = block_by_heading(t35, start, end)
        b36 = block_by_heading(text, start, end)
        assert renumber(b35) == b36, f"block not map-frozen: {start}"
    fig35 = [ln for ln in t35.split("\n") if ln.startswith("![Figure")][0]
    cap35 = [ln for ln in t35.split("\n") if ln.startswith("**Figure 1.**")][0]
    assert text.count(fig35) == 1 and text.count(cap35) == 1, (
        "figure block changed"
    )

    # 8. device and caveat needles
    flat = re.sub(r"\s+", " ", text)
    for nd in DEVICE_NEEDLES + CAVEAT_NEEDLES:
        assert nd in flat, f"needle missing: {nd!r}"

    # 9. rejection scanner
    hits = [b for b in BANNED if b in text]
    assert not hits, f"rejection-list hits in v36 md: {hits}"

    # 10. 'if and only if' count unchanged
    assert flat.count("if and only if") == 5

    # idempotence + version discipline
    if V36.exists():
        assert V36.read_text(encoding="utf-8") == text, "non-idempotent rebuild"
    V36.write_text(text, encoding="utf-8")
    assert V35.read_text(encoding="utf-8") == t35, "v35 was modified"

    print(
        f"  paper4_delay_dynamics_v36.md: OK  {len(text)} chars "
        f"({len(text.splitlines())} lines); rotation 8->7, 9->8, 7->9 with "
        f"{sum(r36.values())} section references remapped "
        f"(v35: {sum(r35.values())}); {len(s36)} math spans "
        f"(multiset-equal to v35); content numerics == v35 + 1992 + 2024 "
        f"only; labels Theorem/Proposition/Remark 7.1 x11/9/2; E1-E4 "
        f"applied; resolver gate: 0 unresolved; abstract {aw} words; "
        f"v35 untouched"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
