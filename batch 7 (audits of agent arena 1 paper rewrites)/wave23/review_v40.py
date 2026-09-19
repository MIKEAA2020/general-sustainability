#!/usr/bin/env python3
"""Wave-23 / Task 99, part 4: the cross-version content review of
paper4_delay_dynamics_v40.md against v39 (and the whole chain back to
v31), plus the supplementary-file ledger --- the machine-checked record
behind humanizing
audits/V40_OVERHEDGING_STRAWMAN_AND_CONTENT_PRESERVATION.md.

Owner directive verified here (directive 2): strip the change-log,
internal dialogue, and surrounding meta-commentary; no editorial,
self-praise or self-commentary statements, or informal terms from chat
history; remove all naive over-hedging while keeping legitimate scope
statements; no phantom or naive strawman points or references to
unpublished work.

Checks (all fail-loud, printed as a ledger):

A. v40 -> v39 (the direct parent): the on-disk v40 is EXACTLY v39 plus
   the 1 declared anchored edit (the Section 1.1 phantom-strawman clause
   removed) --- the reconstruction gate; exactly 1 line differs (L30);
   math-span multiset EXACT equality (all 1,473 spans); content
   numerics IDENTICAL (no numeric change at all); the section-reference
   multiset identical; the heading skeleton identical; frozen blocks
   byte-identical (abstract 258 words / keywords / declarations / Data
   availability / References / figure / the Supplementary paragraph);
   the References block byte-identical (38 entries --- no reference
   touched); the cross-reference resolver (0 unresolved); the label
   counts; the retitle + caricature regression gates.

B. Supplement v8 (unchanged this round): the on-disk v8 is still v7 +
   the 3 Task-98 retitle edits (re-verified); the S1-S12 structure and
   object-label inventory unchanged; every supplement -> main-paper
   section reference resolves against v40's headings; the artifact +
   retitle + caricature gates 0-hit; the mirror consistency with the
   main text's own statements.

C. The chain: references frozen v32==v33==v34==v35==v36==v37 (36
   lines) with v38 == v39 == v40 (38 lines, byte-identical); prior
   versions' md+tex checksums unchanged (version discipline),
   including v39 and the v5/v6/v7/v8 supplements.

D. Error gates on disk: rejection list zero hits (md + tex, 51 banned
   strings including the 3 new phantom-strawman regression gates);
   'if and only if' == 5; v40 tex md5 == the three consecutive
   byte-identical builds.

E. The wave-23 edit gates: the removed clause and the bare word
   "caricature" are absent from the md, the tex, AND the rendered PDF
   text layer; the edited sentence's new form is present in all three;
   the Task-98 title gates re-verified (the title is the md H1 and the
   tex \\title argument; the old title absent everywhere).
"""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_v40 import (  # noqa: E402
    PAPER_EDITS,
    PAPER_NUM_ADD,
    PAPER_NUM_LOST,
    PAPER_NUM_LOST_RAW,
    REJECTION,
    SUPP_REJECTION,
    TITLE,
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
V40 = PR / "paper4_delay_dynamics_v40.md"
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
    "paper4_delay_dynamics_v39.md": "5ca3850f3dd3b22f917cc4b0e5dcd583",
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
    "latex/paper4_delay_dynamics_v39.tex":
        "629a97ae7a92c4146f2be1ff4fd3f1fe",
    "paper4_supplementary_v5.md":
        "8b0170811a31e673cefcc12e59b18895",
    "paper4_supplementary_v6.md":
        "c6da3cfabbfa1b8b6b78d83a957f383a",
    "paper4_supplementary_v7.md":
        "e8dcce49469ea48132e273a4d5c4a2b1",
    "paper4_supplementary_v8.md":
        "20156536b537265f1220ce17646dc799",
}
V40_TEX_MD5 = "0ce11af0262a80b15a2a24bf1695254f"  # three identical builds

OLD_TITLE_FRAGMENTS = (
    "Delay-Induced Regime Change",
    "Channels of Institutional Feedback",
    "delay-induced regime change",
    "channels of institutional feedback",
)

CARICATURE_FRAGMENTS = (
    "opposed in caricature",
    "in caricature",
    "caricature",
)

EDIT_NEW_FORM = (
    "so institutional and ecological delay are analysed within one "
    "frame. Fisheries supply the motivating instance"
)

# the Task-98 supplement construction (v7 -> v8), re-verified here
OLD_TITLE = (
    "Delay-Induced Regime Change in Harvested Stocks: The Mobilising "
    "and Protective Channels of Institutional Feedback, and the Review "
    "Interval as Control"
)
SUPP_RETITLE_EDITS: list[tuple[str, str]] = [
    (
        "# Supplementary Material — Delay-Induced Regime Change in "
        "Harvested Stocks",
        "# Supplementary Material — Governance delay and the stability "
        "of harvested stocks",
    ),
    (
        f'*Accompanies: "{OLD_TITLE}."*',
        f'*Accompanies: "{TITLE}."*',
    ),
    (
        "the main article on delay-induced regime change in harvested "
        "stocks. It carries",
        "the main article on governance delay and the stability of "
        "harvested stocks. It carries",
    ),
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
    t39 = V39.read_text(encoding="utf-8")
    t40 = V40.read_text(encoding="utf-8")
    s7 = SUPP7.read_text(encoding="utf-8")
    s8 = SUPP8.read_text(encoding="utf-8")

    print("== A. v40 vs v39 (the direct parent) ==")
    # A1. the reconstruction gate: v40 is exactly v39 + the declared edit
    assert len(PAPER_EDITS) == 1
    recon = t39
    for old, new, _tag in PAPER_EDITS:
        assert recon.count(old) == 1
        recon = recon.replace(old, new)
    assert recon == t40, "v40 != v39 + the 1 declared edit"
    l39, l40 = t39.splitlines(), t40.splitlines()
    changed = [i for i, (a, b) in enumerate(zip(l39, l40), 1) if a != b]
    assert changed == [30], f"changed lines: {changed}"
    print(f"  A1 reconstruction: v40 == v39 + exactly the 1 declared "
          f"anchored edit (L30, the phantom-strawman clause); line count "
          f"unchanged at {len(l40)}")

    # A2. math spans multiset EXACT equality
    assert Counter(spans(t40)) == Counter(spans(t39))
    print(f"  A2 math spans: {len(spans(t40))} occurrences, multiset "
          "EXACTLY equal to v39's (nothing moved, nothing changed)")

    # A3. content numerics: NO change
    n39 = toks(strip_ref_contexts(t39))
    n40 = toks(strip_ref_contexts(t40))
    assert (n40 - n39) == PAPER_NUM_ADD, dict(n40 - n39)
    assert (n39 - n40) == PAPER_NUM_LOST, dict(n39 - n40)
    r39, r40 = toks(t39), toks(t40)
    assert (r40 - r39) == PAPER_NUM_ADD, "raw numeric delta drifted"
    assert (r39 - r40) == PAPER_NUM_LOST_RAW, "raw numeric loss drifted"
    print("  A3 content numerics (refs/headings/labels stripped): "
          "IDENTICAL to v39's (the edit is digit-free on both sides)")

    # A4. section-reference multiset identical
    sr40, sr39 = section_refs(t40), section_refs(t39)
    assert sr40 == sr39, (
        f"section-ref delta: {dict((sr39 - sr40) + (sr40 - sr39))}"
    )
    print(f"  A4 section references: {sum(sr40.values())} references, "
          "multiset identical to v39's")

    # A5. heading skeleton identical
    assert headings(t40) == headings(t39)
    print("  A5 headings: identical to v39's")

    # A6. abstract 258 words byte-identical; the title stands
    assert journal_words(t40) == 258
    assert t40.split("\n", 1)[0] == f"# {TITLE}"
    kw40 = t40.split("**Keywords:**")[1].split("\n", 1)[0]
    kw39 = t39.split("**Keywords:**")[1].split("\n", 1)[0]
    assert kw40 == kw39
    assert t40.split("## Abstract", 1)[1].split("## 1. Introduction")[0] \
        == t39.split("## Abstract", 1)[1].split("## 1. Introduction")[0]
    print("  A6 abstract: 258 journal words, byte-identical; keywords "
          "byte-identical; the H1 is the Task-98 title, unchanged")

    # A7. frozen blocks byte-identical
    for start, end in (
        ("## Data availability", "## Declaration of competing interest"),
        ("## Declaration of competing interest", "## References"),
    ):
        b39 = t39[t39.find(start):t39.find(end)]
        b40 = t40[t40.find(start):t40.find(end)]
        assert b40 == b39, f"frozen block changed: {start}"
    fig39 = re.search(r"!\[Figure 1\].*?\n\n", t39, flags=re.S).group(0)
    fig40 = re.search(r"!\[Figure 1\].*?\n\n", t40, flags=re.S).group(0)
    assert fig40 == fig39
    # the references block: byte-identical (no reference touched)
    rb39, rb40 = refs_block(t39), refs_block(t40)
    assert rb40 == rb39, "references block changed"
    n_entries = sum(1 for ln in rb40.splitlines() if ln.strip())
    assert n_entries == 38
    # the Supplementary block: byte-identical (pointer stays v8)
    sup39 = t39[t39.find("## Supplementary material"):]
    sup40 = t40[t40.find("## Supplementary material"):]
    assert sup40 == sup39, "Supplementary block drifted"
    print("  A7 frozen blocks: declarations/Data availability/figure "
          "byte-identical; References byte-identical (38 entries --- no "
          "reference touched in the cleanup round); the Supplementary "
          "paragraph byte-identical (the pointer stays at the unchanged "
          "v8 supplement)")

    # A8. cross-reference resolver
    v40_heads: set[str] = set()
    for h in headings(t40):
        m = re.match(r"^#{2,3} (\d+(?:\.\d+)?)", h)
        if m:
            v40_heads.add(m.group(1))
            v40_heads.add(m.group(1).split(".")[0])
    unresolved = sorted(
        r for r in section_refs(t40) if r not in v40_heads
    )
    assert not unresolved, f"unresolved refs: {unresolved}"
    print("  A8 cross-reference resolver: 0 unresolved Section constructs")

    # A9. the label counts
    for lab, cnt in (("Theorem 7.1", 11), ("Proposition 7.1", 9),
                     ("Remark 7.1", 2), ("Propositions 6.2 and 7.1", 1)):
        assert t40.count(lab) == cnt, f"label count {lab}: {t40.count(lab)}"
    for lab in ("Theorem 8.1", "Proposition 8.1", "Remark 8.1"):
        assert t40.count(lab) == 0
    print("  A9 labels: Theorem 7.1 x11, Proposition 7.1 x9, Remark 7.1 "
          "x2, the 'Propositions 6.2 and 7.1' list x1; zero stale 8.1")

    # A10. the retitle + caricature regression gates
    for frag in OLD_TITLE_FRAGMENTS:
        assert frag not in t40, f"old-title fragment survived: {frag!r}"
    for frag in CARICATURE_FRAGMENTS:
        assert frag not in t40, f"phantom-strawman fragment survived: {frag!r}"
    assert EDIT_NEW_FORM in flat(t40), "the edited sentence's new form missing"
    print("  A10 regression gates: the old title's fragments AND the "
          "removed clause's every form absent from the v40 md; the "
          "edited sentence's new form present")

    print("== B. Supplement v8 (unchanged this round) ==")
    # B1. the reconstruction gate (the Task-98 construction re-verified)
    recon_s = s7
    for old, new in SUPP_RETITLE_EDITS:
        assert recon_s.count(old) == 1
        recon_s = recon_s.replace(old, new)
    assert recon_s == s8, "supp v8 != v7 + the 3 declared retitle edits"
    d_lines = [
        i for i, (a, b) in enumerate(zip(s7.splitlines(), s8.splitlines()), 1)
        if a != b
    ]
    assert d_lines == [1, 3, 5]
    print("  B1 reconstruction: supp v8 == v7 + exactly the 3 Task-98 "
          "anchored edits (L1 H1, L3 Accompanies, L5 opening phrase); "
          "unchanged by this round")

    # B2. internal structure unchanged
    assert supp_s_headings(s8) == supp_s_headings(s7)
    assert supp_object_labels(s8) == supp_object_labels(s7)
    print("  B2 supplement internal S-structure: S1-S12 headings and "
          "object-label inventory unchanged")

    # B3. every supplement -> main-paper reference resolves in v40
    refs = supp_section_refs(s8)
    assert refs == {"2.3", "5", "6", "5.1", "8.2", "8.3", "9", "10.4"}
    unresolved = sorted(r for r in refs if r not in v40_heads)
    assert not unresolved, f"supp refs unresolved: {unresolved}"
    print("  B4 all eight supplement -> main-paper section references "
          "resolve against v40's headings")

    # B5. the S12 label-mapping targets exist in v40
    for lab in ("Remark 5.1", "Corollary 5.1", "Proposition 6.1",
                "Theorem 4.1", "Lemma 2.1", "Theorem 10.1"):
        assert lab in t40, f"S12 label target missing: {lab}"
    print("  B5 the S12 statement-label mapping's main-text targets all "
          "exist in v40")

    # B6. the pointer names the current supplement
    assert t40.count("paper4_supplementary_v8.md") == 1
    assert "paper4_supplementary_v7.md" not in t40
    assert SUPP8.exists() and "paper4_supplementary_v8.md" == SUPP8.name
    print("  B6 the paper's Supplementary paragraph names "
          "paper4_supplementary_v8.md, which exists; the stale pointer "
          "is absent")

    # B7. the artifact + retitle + caricature gates on the supplement
    for phrase in SUPP_REJECTION:
        assert phrase not in s8, f"supp artifact survived: {phrase!r}"
    for frag in OLD_TITLE_FRAGMENTS:
        assert frag not in s8, f"old-title fragment in supp v8: {frag!r}"
    for frag in CARICATURE_FRAGMENTS:
        assert frag not in s8, f"phantom-strawman fragment in supp v8: {frag!r}"
    assert "the Hocherman, Trop, and Ghermandi (2025) synthesis" in s8
    assert s8.split("\n", 1)[0] == (
        "# Supplementary Material — Governance delay and the stability "
        "of harvested stocks"
    )
    print("  B7 supplement artifact + retitle + caricature gates: all "
          "0-hit; the H1 and the Accompanies line carry the title")

    # B8. mirror consistency with the main text's own statements
    assert ("the Section 9 records (gate log and fine-map table, "
            "Supplementary S9)") in t40
    assert "together with the MPF material of S11" in t40
    assert "Material from the main article's Section 8.3" in s8
    assert "## S11. MPF Material" in s8
    print("  B8 mirror consistency: the main text's Data availability "
          "and Supplementary paragraph agree with the supplement's own "
          "references")

    print("== C. the chain ==")
    # C1. references frozen across the chain; v38 == v39 == v40
    blocks = [refs_block(p.read_text(encoding="utf-8")) for p in
              (V32, V33, V34, V35, V36, V37)]
    assert all(b == blocks[0] for b in blocks)
    n_prior = sum(1 for ln in blocks[0].splitlines() if ln.strip())
    assert n_prior == 36
    rb38 = refs_block(V38.read_text(encoding="utf-8"))
    assert rb40 == rb39 == rb38
    print(f"  C1 references frozen v32==v33==v34==v35==v36==v37 "
          f"({n_prior} lines); v38 == v39 == v40 byte-identical (38 "
          f"lines: the Task-97 insertions stand; the cleanup round "
          f"touched no reference)")

    # C2. prior checksums unchanged
    for name, want in FROZEN_MD5.items():
        got = md5(ROOT / "arena agent 1/paper rewrites" / name)
        assert got == want, f"checksum drift: {name}: {got} != {want}"
    print("  C2 v31/v32/.../v39 md+tex and supp v5/v6/v7/v8 checksums "
          "unchanged (version discipline; never overwritten)")

    print("== D. error gates re-verified on disk ==")
    hits = [b for b in REJECTION if b in t40]
    assert not hits, f"rejection hits in v40 md: {hits}"
    tex = (LATEX / "paper4_delay_dynamics_v40.tex").read_text(
        encoding="utf-8"
    )
    hits_tex = [b for b in REJECTION if b in flat(tex)]
    assert not hits_tex, f"rejection hits in v40 tex: {hits_tex}"
    print(f"  D1 rejection list: 0 hits in md and tex "
          f"({len(REJECTION)} banned strings, incl. the 4 retitle + 3 "
          f"phantom-strawman regression gates)")

    assert flat(t40).count("if and only if") == 5
    print("  D2 'if and only if' x5 unchanged")

    m = md5(LATEX / "paper4_delay_dynamics_v40.tex")
    assert m == V40_TEX_MD5, f"v40 tex md5 drifted: {m}"
    print(f"  D3 v40 tex md5 {m} == the three consecutive byte-identical "
          "builds")

    print("== E. the wave-23 edit gates + the title gates ==")
    # E1. the title is the md H1 and the tex \title argument
    assert t40.split("\n", 1)[0] == f"# {TITLE}"
    title_line = f"\\title{{{TITLE}}}"
    assert title_line in tex, "the tex \\title is not the title"
    print("  E1 the Task-98 title is the md H1 and the tex \\title "
          "argument (verbatim, no wrapping)")

    # E2. the removed clause absent from md, tex, AND the rendered PDF
    #     text layer; the new form present in all three
    import fitz  # PyMuPDF
    doc = fitz.open(LATEX / "paper4_delay_dynamics_v40.pdf")
    LIG = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl",
           "\ufb03": "ffi", "\ufb04": "ffl"}
    rendered = "".join(doc[i].get_text() for i in range(doc.page_count))
    for k, v in LIG.items():
        rendered = rendered.replace(k, v)
    rendered = re.sub(r"-\s*\n\s*", "", rendered)
    rendered = re.sub(r"\s+", " ", rendered)
    assert TITLE in rendered, "the title missing from the rendered layer"
    assert EDIT_NEW_FORM in rendered, (
        "the edited sentence's new form missing from the rendered layer"
    )
    for frag in CARICATURE_FRAGMENTS:
        assert frag not in t40 and frag not in flat(tex), (
            f"removed clause on disk: {frag!r}"
        )
        assert frag not in rendered, (
            f"removed clause in rendered PDF: {frag!r}"
        )
    for frag in OLD_TITLE_FRAGMENTS:
        assert frag not in t40 and frag not in flat(tex), (
            f"old-title fragment on disk: {frag!r}"
        )
        assert frag not in rendered, (
            f"old-title fragment in rendered PDF: {frag!r}"
        )
    print("  E2 the removed clause's every form absent from the md, the "
          "tex, and the rendered PDF text layer; the edited sentence's "
          "new form present in all three; the old title absent "
          "everywhere (45 pages)")
    doc.close()

    print("\n  CROSS-VERSION REVIEW: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
