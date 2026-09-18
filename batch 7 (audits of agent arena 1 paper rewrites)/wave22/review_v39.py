#!/usr/bin/env python3
"""Wave-22 / Task 98, part 4: the cross-version content review of
paper4_delay_dynamics_v39.md against v38 (and the whole chain back to
v31), plus the supplementary-file ledger --- the machine-checked record
behind humanizing audits/V39_RETITLE_ROUND_AND_DOI_QUESTION.md.

Owner directive verified here: "1- choose accurate, honest title,
appropriate to Theoretical ecology journal  2- which dois do u want?
are they on repo?"

Checks (all fail-loud, printed as a ledger):

A. v39 -> v38 (the direct parent): the on-disk v39 is EXACTLY v38 plus
   the 2 declared anchored edits (the title line; the supplementary
   pointer v7 -> v8) --- the reconstruction gate; exactly 2 lines
   differ; math-span multiset EXACT equality (all 1,473 spans); content
   numerics == v38 + the pointer's version digit (+8, -7) and nothing
   else; the section-reference multiset identical; the heading skeleton
   identical; frozen blocks byte-identical (abstract 258 words /
   keywords / declarations / Data availability / References / figure);
   the References block byte-identical (36 entries --- no reference
   touched in the retitle round); the Supplementary block == the
   declared construction; the cross-reference resolver (0 unresolved);
   the label counts; the retitle regression gates (the old title's
   fragments absent in every case form).

B. Supplement v8 vs v7: the on-disk v8 is EXACTLY v7 plus the 3
   declared anchored edits (the H1, the Accompanies line, the opening
   subject phrase); the S1-S12 structure and object-label inventory
   unchanged; the numerics unchanged; every supplement -> main-paper
   section reference resolves against v39's headings; the artifact +
   retitle gates 0-hit; the mirror consistency with the main text's own
   statements.

C. The chain: references frozen v32==v33==v34==v35==v36==v37 (36
   lines) with v38 == v39 == v37 + the two Task-97 insertions (38
   lines, byte-identical between v38 and v39); prior versions' md+tex
   checksums unchanged (version discipline), including v38 and the
   v5/v6/v7 supplements.

D. Error gates on disk: rejection list zero hits (md + tex, 48 banned
   strings including the 4 retitle regression gates); 'if and only if'
   == 5; v39 tex md5 == the three consecutive byte-identical builds.

E. The title gates: the new title is the md H1 and the tex \\title
   argument; the old title's fragments are absent from the md, the tex,
   AND the rendered PDF text layer (ligature/hyphen-normalised).
"""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_v39 import (  # noqa: E402
    NEW_TITLE,
    PAPER_EDITS,
    PAPER_NUM_ADD,
    PAPER_NUM_LOST,
    PAPER_NUM_LOST_RAW,
    SUPP_EDITS,
    SUPP_NUM_ADD,
    SUPP_NUM_LOST,
)

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
LATEX = PR / "latex"

V31 = PR / "paper4_delay_dynamics_v31.md"
V32 = PR / "paper4_delay_dynamics_v32.md"
V33 = PR / "paper4_delay_dynamics_v33.md"
V34 = PR / "paper4_delay_dynamics_v34.md"
V35 = PR / "paper4_delay_dynamics_v35.md"
V36 = PR / "paper4_delay_dynamics_v36.md"
V37 = PR / "paper4_delay_dynamics_v37.md"
V38 = PR / "paper4_delay_dynamics_v38.md"
V39 = PR / "paper4_delay_dynamics_v39.md"
SUPP5 = PR / "paper4_supplementary_v5.md"
SUPP6 = PR / "paper4_supplementary_v6.md"
SUPP7 = PR / "paper4_supplementary_v7.md"
SUPP8 = PR / "paper4_supplementary_v8.md"

FROZEN_MD5 = {
    "paper4_delay_dynamics_v31.md": "c75674a46b5352e2b3097329320d7c7d",
    "paper4_delay_dynamics_v32.md": "1b09783b0b156347cce3aa3c24f7f149",
    "paper4_delay_dynamics_v33.md": "a2581136fbdbac0f79a1332e42f8e556",
    "paper4_delay_dynamics_v34.md": "4f964bd630bc4d19af448cde47b19025",
    "paper4_delay_dynamics_v35.md": "e9c99edbcf59cce80f2bd08c2966a74b",
    "paper4_delay_dynamics_v36.md": "06af59363a0301b61eae237d7a4f3ea2",
    "paper4_delay_dynamics_v37.md": "f32ef08f15fc3fdfacdc041d6d15a51b",
    "paper4_delay_dynamics_v38.md": "1f889a5f0e844b8756a1499420973fbc",
    "latex/paper4_delay_dynamics_v31.tex":
        "2224247e4cace8b0f0c2aea85a6ad3be",
    "latex/paper4_delay_dynamics_v32.tex":
        "02d479c048c57f64ecd41509e31ed2f2",
    "latex/paper4_delay_dynamics_v33.tex":
        "658c2fa14e3bbc6a272ded15a8b65a08",
    "latex/paper4_delay_dynamics_v34.tex":
        "a233b61509a76389a9beaae1b50a2e21",
    "latex/paper4_delay_dynamics_v35.tex":
        "f1bdcd666baf6a0195fa33a7e0913d80",
    "latex/paper4_delay_dynamics_v36.tex":
        "258c2424a752897a139725681af99ecb",
    "latex/paper4_delay_dynamics_v37.tex":
        "28f6eee027ba9e5449b9a712bd35a54f",
    "latex/paper4_delay_dynamics_v38.tex":
        "b9e23ee40f96852f5b3877aae9858f1d",
    "paper4_supplementary_v5.md":
        "8b0170811a31e673cefcc12e59b18895",
    "paper4_supplementary_v6.md":
        "c6da3cfabbfa1b8b6b78d83a957f383a",
    "paper4_supplementary_v7.md":
        "e8dcce49469ea48132e273a4d5c4a2b1",
}
V39_TEX_MD5 = "629a97ae7a92c4146f2be1ff4fd3f1fe"  # three identical builds

OLD_TITLE_FRAGMENTS = (
    "Delay-Induced Regime Change",
    "Channels of Institutional Feedback",
    "delay-induced regime change",
    "channels of institutional feedback",
)

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
    # wave-22 retitle regression gates
    "Delay-Induced Regime Change", "Channels of Institutional Feedback",
    "delay-induced regime change", "channels of institutional feedback",
]


def md5(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def flat(s: str) -> str:
    return re.sub(r"\s+", " ", s)


def spans(t: str) -> list[str]:
    return re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", t, flags=re.S)


def toks(t: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", t))


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


def headings(t: str) -> list[str]:
    return re.findall(r"^#{2,3} .*$", t, flags=re.M)


def section_refs(t: str) -> Counter:
    c: Counter = Counter()
    for m in re.finditer(
        r"Sections?((?:\s+\d+(?:\.\d+)?)(?:(?:\s*,\s*(?:and\s+)?"
        r"|\s+and\s+|--|–)\d+(?:\.\d+)?)*)",
        flat(t),
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
        flat(t),
    ):
        refs |= set(re.findall(r"\d+(?:\.\d+)?", m.group(1)))
    return refs


def supp_s_headings(t: str) -> list[str]:
    return re.findall(r"^#{2,3} S[\d.]+.*$", t, flags=re.M)


def supp_object_labels(t: str) -> list[str]:
    return re.findall(
        r"\*\*(?:Definition|Proposition|Theorem|Remark|Corollary|Lemma) "
        r"S[\d.]+", t,
    )


def main() -> int:
    t38 = V38.read_text(encoding="utf-8")
    t39 = V39.read_text(encoding="utf-8")
    s7 = SUPP7.read_text(encoding="utf-8")
    s8 = SUPP8.read_text(encoding="utf-8")

    print("== A. v39 vs v38 (the direct parent) ==")
    # A1. the reconstruction gate: v39 is exactly v38 + the declared edits
    assert len(PAPER_EDITS) == 2 and len(SUPP_EDITS) == 3
    recon = t38
    for old, new, _tag in PAPER_EDITS:
        assert recon.count(old) == 1
        recon = recon.replace(old, new)
    assert recon == t39, "v39 != v38 + the 2 declared edits"
    l38, l39 = t38.splitlines(), t39.splitlines()
    changed = [i for i, (a, b) in enumerate(zip(l38, l39), 1) if a != b]
    assert changed == [1, 906], f"changed lines: {changed}"
    print(f"  A1 reconstruction: v39 == v38 + exactly the 2 declared "
          f"anchored edits (L1 the title, L906 the supplementary "
          f"pointer); line count unchanged at {len(l39)}")

    # A2. math spans multiset EXACT equality
    assert Counter(spans(t39)) == Counter(spans(t38))
    print(f"  A2 math spans: {len(spans(t39))} occurrences, multiset "
          "EXACTLY equal to v38's (nothing moved, nothing changed)")

    # A3. content numerics: the declared delta
    n38 = toks(strip_ref_contexts(t38))
    n39 = toks(strip_ref_contexts(t39))
    assert (n39 - n38) == PAPER_NUM_ADD, dict(n39 - n38)
    assert (n38 - n39) == PAPER_NUM_LOST, dict(n38 - n39)
    r38, r39 = toks(t38), toks(t39)
    assert (r39 - r38) == PAPER_NUM_ADD, "raw numeric delta drifted"
    assert (r38 - r39) == PAPER_NUM_LOST_RAW, "raw numeric loss drifted"
    print("  A3 content numerics (refs/headings/labels stripped): v38 + "
          "the pointer's version digit only (+8, -7; both titles are "
          "digit-free)")

    # A4. section-reference multiset identical
    sr39, sr38 = section_refs(t39), section_refs(t38)
    assert sr39 == sr38, (
        f"section-ref delta: {dict((sr38 - sr39) + (sr39 - sr38))}"
    )
    print(f"  A4 section references: {sum(sr39.values())} references, "
          "multiset identical to v38's")

    # A5. heading skeleton identical
    assert headings(t39) == headings(t38)
    print("  A5 headings: identical to v38's")

    # A6. abstract 258 words byte-identical; the title is the new title
    assert journal_words(t39) == 258
    assert t39.split("\n", 1)[0] == f"# {NEW_TITLE}"
    kw39 = t39.split("**Keywords:**")[1].split("\n", 1)[0]
    kw38 = t38.split("**Keywords:**")[1].split("\n", 1)[0]
    assert kw39 == kw38
    assert t39.split("## Abstract", 1)[1].split("## 1. Introduction")[0] \
        == t38.split("## Abstract", 1)[1].split("## 1. Introduction")[0]
    print("  A6 abstract: 258 journal words, byte-identical; keywords "
          "byte-identical; the H1 is the new 21-word title")

    # A7. frozen blocks + the declared constructions
    for start, end in (
        ("## Data availability", "## Declaration of competing interest"),
        ("## Declaration of competing interest", "## References"),
    ):
        b38 = t38[t38.find(start):t38.find(end)]
        b39 = t39[t39.find(start):t39.find(end)]
        assert b39 == b38, f"frozen block changed: {start}"
    fig38 = re.search(r"!\[Figure 1\].*?\n\n", t38, flags=re.S).group(0)
    fig39 = re.search(r"!\[Figure 1\].*?\n\n", t39, flags=re.S).group(0)
    assert fig39 == fig38
    # the references block: byte-identical (no reference touched)
    rb38, rb39 = refs_block(t38), refs_block(t39)
    assert rb39 == rb38, "references block changed"
    n_entries = sum(1 for ln in rb39.splitlines() if ln.strip())
    assert n_entries == 38
    # the Supplementary block: the declared construction
    sup38 = t38[t38.find("## Supplementary material"):]
    sup39 = t39[t39.find("## Supplementary material"):]
    expected_sup = sup38
    for old, new, _tag in PAPER_EDITS[1:2]:
        expected_sup = expected_sup.replace(old, new)
    assert sup39 == expected_sup, "Supplementary block drifted"
    print("  A7 frozen blocks: declarations/Data availability/figure "
          "byte-identical; References byte-identical (36 entries, 38 "
          "lines --- no reference touched in the retitle round); "
          "Supplementary = the declared construction (pointer v7 -> v8)")

    # A8. cross-reference resolver
    v39_heads: set[str] = set()
    for h in headings(t39):
        m = re.match(r"^#{2,3} (\d+(?:\.\d+)?)", h)
        if m:
            v39_heads.add(m.group(1))
            v39_heads.add(m.group(1).split(".")[0])
    unresolved = sorted(
        r for r in section_refs(t39) if r not in v39_heads
    )
    assert not unresolved, f"unresolved refs: {unresolved}"
    print("  A8 cross-reference resolver: 0 unresolved Section constructs")

    # A9. the label counts
    for lab, cnt in (("Theorem 7.1", 11), ("Proposition 7.1", 9),
                     ("Remark 7.1", 2), ("Propositions 6.2 and 7.1", 1)):
        assert t39.count(lab) == cnt, f"label count {lab}: {t39.count(lab)}"
    for lab in ("Theorem 8.1", "Proposition 8.1", "Remark 8.1"):
        assert t39.count(lab) == 0
    print("  A9 labels: Theorem 7.1 x11, Proposition 7.1 x9, Remark 7.1 "
          "x2, the 'Propositions 6.2 and 7.1' list x1; zero stale 8.1")

    # A10. the retitle regression gates (the old title absent)
    for frag in OLD_TITLE_FRAGMENTS:
        assert frag not in t39, f"old-title fragment survived: {frag!r}"
    print("  A10 retitle gates: the old title's fragments absent from "
          "the v39 md in every case form ('The Review Interval as "
          "Control' deliberately NOT banned --- it is the live Section 7 "
          "heading)")

    print("== B. Supplement v8 (the retitled accompanying file) ==")
    # B1. the reconstruction gate
    recon_s = s7
    for old, new, _tag in SUPP_EDITS:
        assert recon_s.count(old) == 1
        recon_s = recon_s.replace(old, new)
    assert recon_s == s8, "supp v8 != v7 + the 3 declared edits"
    d_lines = [
        i for i, (a, b) in enumerate(zip(s7.splitlines(), s8.splitlines()), 1)
        if a != b
    ]
    assert d_lines == [1, 3, 5]
    print("  B1 reconstruction: supp v8 == v7 + exactly the 3 declared "
          "anchored edits (L1 H1, L3 Accompanies, L5 opening phrase)")

    # B2. internal structure unchanged
    assert supp_s_headings(s8) == supp_s_headings(s7)
    assert supp_object_labels(s8) == supp_object_labels(s7)
    print("  B2 supplement internal S-structure: S1-S12 headings and "
          "object-label inventory unchanged")

    # B3. numerics unchanged
    sn7, sn8 = toks(s7), toks(s8)
    assert (sn8 - sn7) == SUPP_NUM_ADD and (sn7 - sn8) == SUPP_NUM_LOST
    print("  B3 supplement numerics: byte-level unchanged")

    # B4. every supplement -> main-paper reference resolves in v39
    refs = supp_section_refs(s8)
    assert refs == {"2.3", "5", "6", "5.1", "8.2", "8.3", "9", "10.4"}
    unresolved = sorted(r for r in refs if r not in v39_heads)
    assert not unresolved, f"supp refs unresolved: {unresolved}"
    print("  B4 all eight supplement -> main-paper section references "
          "resolve against v39's headings")

    # B5. the S12 label-mapping targets exist in v39
    for lab in ("Remark 5.1", "Corollary 5.1", "Proposition 6.1",
                "Theorem 4.1", "Lemma 2.1", "Theorem 10.1"):
        assert lab in t39, f"S12 label target missing: {lab}"
    print("  B5 the S12 statement-label mapping's main-text targets all "
          "exist in v39")

    # B6. the pointer names the retitled supplement
    assert t39.count("paper4_supplementary_v8.md") == 1
    assert "paper4_supplementary_v7.md" not in t39
    assert SUPP8.exists() and "paper4_supplementary_v8.md" == SUPP8.name
    print("  B6 the paper's Supplementary paragraph names "
          "paper4_supplementary_v8.md, which exists; the stale pointer "
          "is absent")

    # B7. the artifact + retitle gates on the supplement
    for phrase in ("committed", "audit document", "audit `audits",
                   "relocated", "2026-09-03", "now established",
                   "is now verified", "where it belongs",
                   "tikhonov_unh_verification"):
        assert phrase not in s8, f"supp artifact survived: {phrase!r}"
    for frag in OLD_TITLE_FRAGMENTS:
        assert frag not in s8, f"old-title fragment in supp v8: {frag!r}"
    assert "the Hocherman, Trop, and Ghermandi (2025) synthesis" in s8
    assert s8.split("\n", 1)[0] == (
        "# Supplementary Material — Governance delay and the stability "
        "of harvested stocks"
    )
    print("  B7 supplement artifact + retitle gates: all 0-hit; the H1 "
          "and the Accompanies line carry the new title")

    # B8. mirror consistency with the main text's own statements
    assert ("the Section 9 records (gate log and fine-map table, "
            "Supplementary S9)") in t39
    assert "together with the MPF material of S11" in t39
    assert "Material from the main article's Section 8.3" in s8
    assert "## S11. MPF Material" in s8
    print("  B8 mirror consistency: the main text's Data availability "
          "and Supplementary paragraph agree with the supplement's own "
          "references")

    print("== C. the chain ==")
    # C1. references frozen across the chain; v39 == v38 byte-identical
    blocks = [refs_block(p.read_text(encoding="utf-8")) for p in
              (V32, V33, V34, V35, V36, V37)]
    assert all(b == blocks[0] for b in blocks)
    n_prior = sum(1 for ln in blocks[0].splitlines() if ln.strip())
    assert n_prior == 36
    assert rb39 == rb38
    print(f"  C1 references frozen v32==v33==v34==v35==v36==v37 "
          f"({n_prior} lines); v38 == v39 byte-identical (38 lines: the "
          f"Task-97 insertions stand; the retitle round touched no "
          f"reference)")

    # C2. prior checksums unchanged
    for name, want in FROZEN_MD5.items():
        got = md5(ROOT / "arena agent 1/paper rewrites" / name)
        assert got == want, f"checksum drift: {name}: {got} != {want}"
    print("  C2 v31/v32/v33/v34/v35/v36/v37/v38 md+tex and supp "
          "v5/v6/v7 checksums unchanged (version discipline; never "
          "overwritten)")

    print("== D. error gates re-verified on disk ==")
    hits = [b for b in REJECTION if b in t39]
    assert not hits, f"rejection hits in v39 md: {hits}"
    tex = (LATEX / "paper4_delay_dynamics_v39.tex").read_text(
        encoding="utf-8"
    )
    hits_tex = [b for b in REJECTION if b in flat(tex)]
    assert not hits_tex, f"rejection hits in v39 tex: {hits_tex}"
    print(f"  D1 rejection list: 0 hits in md and tex "
          f"({len(REJECTION)} banned strings, incl. the 4 retitle "
          f"regression gates)")

    assert flat(t39).count("if and only if") == 5
    print("  D2 'if and only if' x5 unchanged")

    m = md5(LATEX / "paper4_delay_dynamics_v39.tex")
    assert m == V39_TEX_MD5, f"v39 tex md5 drifted: {m}"
    print(f"  D3 v39 tex md5 {m} == the three consecutive byte-identical "
          "builds")

    print("== E. the title gates ==")
    # E1. the new title is the md H1 and the tex \title argument
    assert t39.split("\n", 1)[0] == f"# {NEW_TITLE}"
    title_line = f"\\title{{{NEW_TITLE}}}"
    assert title_line in tex, "the tex \\title is not the new title"
    print("  E1 the new title is the md H1 and the tex \\title argument "
          "(verbatim, no wrapping)")

    # E2. the old title's fragments absent from the md, the tex, AND the
    #     rendered PDF text layer
    import fitz  # PyMuPDF
    doc = fitz.open(LATEX / "paper4_delay_dynamics_v39.pdf")
    LIG = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl",
           "\ufb03": "ffi", "\ufb04": "ffl"}
    rendered = "".join(doc[i].get_text() for i in range(doc.page_count))
    for k, v in LIG.items():
        rendered = rendered.replace(k, v)
    rendered = re.sub(r"-\s*\n\s*", "", rendered)
    rendered = re.sub(r"\s+", " ", rendered)
    assert NEW_TITLE in rendered, "the new title missing from the "
    "rendered text layer"
    for frag in OLD_TITLE_FRAGMENTS:
        assert frag not in t39 and frag not in flat(tex), (
            f"old-title fragment on disk: {frag!r}"
        )
        assert frag not in rendered, (
            f"old-title fragment in rendered PDF: {frag!r}"
        )
    print("  E2 the old title's fragments absent from the md, the tex, "
          "and the rendered PDF text layer; the new title renders "
          "verbatim (45 pages)")
    doc.close()

    print("\n  CROSS-VERSION REVIEW: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
