#!/usr/bin/env python3
"""Wave-20 / Task 95, part 4: the cross-version content review of
paper4_delay_dynamics_v37.md against v36, v35, v34, v33, v32 and v31,
plus the supplementary-file alignment ledger --- the machine-checked
record behind humanizing audits/V37_SUPPLEMENTARY_ALIGNMENT.md.

Owner directive verified here: "do abstract, title, keywords, individual
sections and supplementary file all align with latest version?  ensure
no errors introduced or content lost from the several humanizing
passes."

Checks (all fail-loud, printed as a ledger):

A. v37 -> v36 (the direct parent): exactly one changed line (the
   supplementary pointer); math-span multiset EXACT equality; content
   numerics == v36 + the filename version digit (+6, -5); the
   section-reference multiset identical; the heading skeleton identical;
   frozen blocks byte-identical (title/keywords/abstract/declarations/
   references/figure; the Supplementary block identical modulo the
   pointer replacement); abstract word count 258; the cross-reference
   resolver (0 unresolved); the 7.1 label counts.

B. Supplementary alignment (the round's finding and fix): the v6 file
   differs from v5 in exactly three lines (the remapped main-paper
   references 7->9, 9.3->8.3, 9.2->8.2); the internal S-structure and
   object-label inventory unchanged; every supplement -> main-paper
   section reference resolves against v37's heading inventory; the S12
   label-mapping targets all exist in v37; the paper's pointer names
   the v6 file; the main text's own statements about the supplement use
   the same section numbers the remapped supplement now uses (the
   mirror-consistency gate).

C. The chain: references frozen v32==v33==v34==v35==v36==v37 (36
   entries); prior versions' md+tex checksums unchanged (version
   discipline); the v5 supplement's checksum unchanged.

D. Error gates on disk: rejection list zero hits (md + tex, 35 banned
   strings); 'if and only if' == 5; v37 tex md5 == the three
   consecutive byte-identical builds.
"""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

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
SUPP5 = PR / "paper4_supplementary_v5.md"
SUPP6 = PR / "paper4_supplementary_v6.md"

FROZEN_MD5 = {
    "paper4_delay_dynamics_v31.md": "c75674a46b5352e2b3097329320d7c7d",
    "paper4_delay_dynamics_v32.md": "1b09783b0b156347cce3aa3c24f7f149",
    "paper4_delay_dynamics_v33.md": "a2581136fbdbac0f79a1332e42f8e556",
    "paper4_delay_dynamics_v34.md": "4f964bd630bc4d19af448cde47b19025",
    "paper4_delay_dynamics_v35.md": "e9c99edbcf59cce80f2bd08c2966a74b",
    "paper4_delay_dynamics_v36.md": "06af59363a0301b61eae237d7a4f3ea2",
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
    "paper4_supplementary_v5.md":
        "8b0170811a31e673cefcc12e59b18895",
}
V37_TEX_MD5 = "28f6eee027ba9e5449b9a712bd35a54f"  # three identical builds

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

PAPER_OLD = "paper4_supplementary_v5.md"
PAPER_NEW = "paper4_supplementary_v6.md"


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
        r"S[\d.]+", t
    )


def main() -> int:
    t36 = V36.read_text(encoding="utf-8")
    t37 = V37.read_text(encoding="utf-8")
    s5 = SUPP5.read_text(encoding="utf-8")
    s6 = SUPP6.read_text(encoding="utf-8")

    print("== A. v37 vs v36 (the direct parent) ==")
    # A1. exactly one changed line: the pointer
    d = [
        (a, b) for a, b in zip(t36.splitlines(), t37.splitlines()) if a != b
    ]
    assert len(t36.splitlines()) == len(t37.splitlines())
    assert len(d) == 1 and PAPER_NEW in d[0][1], f"diff != 1 pointer line"
    print("  A1 exactly one changed line: the supplementary file pointer "
          "(paper4_supplementary_v5.md -> paper4_supplementary_v6.md)")

    # A2. math spans multiset EXACT equality
    assert Counter(spans(t37)) == Counter(spans(t36))
    print(f"  A2 math spans: {len(spans(t37))} occurrences, multiset "
          "EXACTLY equal to v36's (nothing moved, nothing changed)")

    # A3. content numerics: the filename version digit only
    n36 = toks(strip_ref_contexts(t36))
    n37 = toks(strip_ref_contexts(t37))
    assert (n37 - n36) == Counter({"6": 1}), dict(n37 - n36)
    assert (n36 - n37) == Counter({"5": 1}), dict(n36 - n37)
    print("  A3 content numerics (refs/headings/labels stripped): "
          "identical to v36 except the filename version digit (+6, -5)")

    # A4. section-reference multiset identical
    assert section_refs(t37) == section_refs(t36)
    print(f"  A4 section references: {sum(section_refs(t37).values())} "
          "references, multiset identical to v36's")

    # A5. heading skeleton identical
    assert headings(t37) == headings(t36)
    print("  A5 headings: identical to v36's (the v36 rotation stands; "
          "nothing moved)")

    # A6. abstract 258 words; title/keywords byte-identical
    assert journal_words(t37) == 258
    assert t37.split("\n", 1)[0] == t36.split("\n", 1)[0]
    kw37 = t37.split("**Keywords:**")[1].split("\n", 1)[0]
    kw36 = t36.split("**Keywords:**")[1].split("\n", 1)[0]
    assert kw37 == kw36
    print("  A6 abstract: 258 journal words (byte-identical); title and "
          "keywords byte-identical")

    # A7. frozen blocks + Supplementary modulo the pointer
    assert refs_block(t37) == refs_block(t36)
    for start, end in (
        ("## Data availability", "## Declaration of competing interest"),
        ("## Declaration of competing interest", "## References"),
    ):
        b36 = t36[t36.find(start):t36.find(end)]
        b37 = t37[t37.find(start):t37.find(end)]
        assert b37 == b36, f"frozen block changed: {start}"
    sup36 = t36[t36.find("## Supplementary material"):]
    sup37 = t37[t37.find("## Supplementary material"):]
    assert sup37 == sup36.replace(PAPER_OLD, PAPER_NEW)
    fig36 = re.search(r"!\[Figure 1\].*?\n\n", t36, flags=re.S).group(0)
    fig37 = re.search(r"!\[Figure 1\].*?\n\n", t37, flags=re.S).group(0)
    assert fig37 == fig36
    print("  A7 frozen blocks: references (36 entries)/declarations/figure "
          "byte-identical; Data availability byte-identical; "
          "Supplementary identical modulo the pointer replacement")

    # A8. cross-reference resolver (the permanent gate)
    v37_heads: set[str] = set()
    for h in headings(t37):
        m = re.match(r"^#{2,3} (\d+(?:\.\d+)?)", h)
        if m:
            v37_heads.add(m.group(1))
            v37_heads.add(m.group(1).split(".")[0])
    unresolved = sorted(
        r for r in section_refs(t37) if r not in v37_heads
    )
    assert not unresolved, f"unresolved refs: {unresolved}"
    print("  A8 cross-reference resolver: 0 unresolved Section constructs")

    # A9. the 7.1 label counts (rotation labels stand)
    for lab, cnt in (("Theorem 7.1", 11), ("Proposition 7.1", 9),
                     ("Remark 7.1", 2), ("Propositions 6.2 and 7.1", 1)):
        assert t37.count(lab) == cnt, f"label count {lab}: {t37.count(lab)}"
    for lab in ("Theorem 8.1", "Proposition 8.1", "Remark 8.1"):
        assert t37.count(lab) == 0
    print("  A9 labels: Theorem 7.1 x11, Proposition 7.1 x9, Remark 7.1 "
          "x2, the 'Propositions 6.2 and 7.1' list x1; zero stale 8.1")

    print("== B. Supplementary alignment (the round's finding and fix) ==")
    # B1. exactly three changed lines
    d5 = [
        (a, b) for a, b in zip(s5.splitlines(), s6.splitlines()) if a != b
    ]
    assert len(s5.splitlines()) == len(s6.splitlines())
    assert len(d5) == 3, f"supp diff != 3 lines: {len(d5)}"
    wants = [
        "All records of Section 9 of the main paper",
        "relocated from the main article's Section 8.3 (the MPF paragraph)",
        "(main text, Sections 5.1 and 8.2;",
    ]
    for (_, new), want in zip(d5, wants):
        assert want in new, f"unexpected supp line: {new!r}"
    print("  B1 supplement v6 differs from v5 in exactly three lines: "
          "S9 intro 'Section 7'->'Section 9'; S11 intro 'Section 9.3'"
          "->'Section 8.3'; S12 status note 'Sections 5.1 and 9.2'"
          "->'Sections 5.1 and 8.2'")

    # B2. internal structure unchanged
    assert supp_s_headings(s6) == supp_s_headings(s5)
    assert supp_object_labels(s6) == supp_object_labels(s5)
    print("  B2 supplement internal S-structure (S1-S12) and object-label "
          "inventory unchanged")

    # B3. every supplement -> main-paper reference resolves in v37
    refs = supp_section_refs(s6)
    assert refs == {"2.3", "5", "6", "5.1", "8.2", "8.3", "9", "10.4"}, (
        sorted(refs)
    )
    unresolved = sorted(r for r in refs if r not in v37_heads)
    assert not unresolved, f"supp refs unresolved: {unresolved}"
    print("  B3 all eight supplement -> main-paper section references "
          "resolve against v37's headings {2.3, 5, 6, 5.1, 8.2, 8.3, 9, "
          "10.4} (the three remapped ones now point at the Delayed-"
          "Recruitment chapter 9, the registered numerical families 8.3, "
          "and the attractor-topology fold records 8.2)")

    # B4. the S12 label-mapping targets exist in v37
    for lab in ("Remark 5.1", "Corollary 5.1", "Proposition 6.1",
                "Theorem 4.1", "Lemma 2.1", "Theorem 10.1"):
        assert lab in t37, f"S12 label target missing: {lab}"
    print("  B4 the S12 statement-label mapping's main-text targets all "
          "exist in v37 (Remark 5.1, Corollary 5.1, Proposition 6.1, "
          "Theorem 4.1, Lemma 2.1, Theorem 10.1)")

    # B5. the pointer names the aligned supplement
    assert t37.count(PAPER_NEW) == 1 and PAPER_OLD not in t37
    assert SUPP6.exists() and PAPER_NEW == SUPP6.name
    print("  B5 the paper's Supplementary paragraph names "
          "paper4_supplementary_v6.md, which exists and is the aligned "
          "file; the stale pointer is absent")

    # B6. mirror consistency with the main text's own statements
    assert ("the Section 9 records (gate log and fine-map table, "
            "Supplementary S9)") in t37
    assert "relocated from Sections 8.3 and 10.4" in t37
    print("  B6 mirror consistency: the main text's Data availability "
          "('the Section 9 records ... Supplementary S9') and the "
          "Supplementary paragraph ('relocated from Sections 8.3 and "
          "10.4') now agree with the remapped supplement's own "
          "references")

    print("== C. the chain ==")
    # C1. references frozen across the whole chain (the prior gates'
    #     counting convention: non-empty lines of the refs block)
    blocks = [refs_block(p.read_text(encoding="utf-8")) for p in
              (V32, V33, V34, V35, V36, V37)]
    assert all(b == blocks[0] for b in blocks)
    n_entries = sum(1 for ln in blocks[0].splitlines() if ln.strip())
    print(f"  C1 references frozen v32==v33==v34==v35==v36==v37 "
          f"({n_entries} entries; the v36 gate's counting convention)")

    # C2. prior checksums unchanged
    for name, want in FROZEN_MD5.items():
        got = md5(ROOT / "arena agent 1/paper rewrites" / name)
        assert got == want, f"checksum drift: {name}: {got} != {want}"
    print("  C2 v31/v32/v33/v34/v35/v36 md+tex and supp v5 checksums "
          "unchanged (version discipline; never overwritten)")

    print("== D. error gates re-verified on disk ==")
    hits = [b for b in REJECTION if b in t37]
    assert not hits, f"rejection hits in v37 md: {hits}"
    tex = (LATEX / "paper4_delay_dynamics_v37.tex").read_text(
        encoding="utf-8"
    )
    hits_tex = [b for b in REJECTION if b in flat(tex)]
    assert not hits_tex, f"rejection hits in v37 tex: {hits_tex}"
    print(f"  D1 rejection list: 0 hits in md and tex "
          f"({len(REJECTION)} banned strings)")

    assert flat(t37).count("if and only if") == 5
    print("  D2 'if and only if' x5 unchanged")

    m = md5(LATEX / "paper4_delay_dynamics_v37.tex")
    assert m == V37_TEX_MD5, f"v37 tex md5 drifted: {m}"
    print(f"  D3 v37 tex md5 {m} == the three consecutive byte-identical "
          "builds")

    print("\n  CROSS-VERSION REVIEW: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
