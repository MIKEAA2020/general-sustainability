#!/usr/bin/env python3
"""Repair paper09_cod_certification_v32.tex: references + Declarations.

Dry-run by default; --apply writes the file.

v32 is a THREE-source merge (paper09 cod + paper09b ARV + paper10b Edwards),
and it carries three separate Declarations blocks -- one per source -- plus a
bibliography damaged by the old reference splitter.

=============================================================================
PART 1 -- BIBLIOGRAPHY
=============================================================================
The old splitter cut entries at "period + Word, ", which is the shape of a
publisher line. Six tails were detached from their heads and survive as
free-standing paragraphs. Each is reattached below, using the SOURCE papers
(paper09 v30/v31, paper09b v2, paper10b v1) as ground truth for the intact
entry -- nothing is guessed.

  1. L4103  Birkh\"auser, Boston.
            -> Aubin, J.-P., 1991. \emph{Viability Theory}.   (L4094)
               matches paper10b v1 L1133 verbatim.
  2. L4105  Birkh\"auser, Boston.
            -> DELETED. A second, identical orphan with no head of its own:
               two sources carried Aubin, the heads de-duplicated to one, both
               tails survived. This is the L.dup-ref at L4105.
  3. L4142  Edwards Aquifer Authority, San Antonio, TX.
            -> Edwards Aquifer Authority, 2024. Managing the Edwards Aquifer:
               critical period management and index wells.   (L4139)
               matches paper10b v1 L1138-1139.
  4. L4146  Edwards Aquifer Authority, San Antonio, TX.
            -> Edwards Aquifer Recovery Implementation Program, 2021.
               \emph{Habitat Conservation Plan}.   (L4144)
               matches paper10b v1 L1141-1142.
  5. L4148  Fisheries and Oceans Canada, Ottawa.
            -> DFO, 2009. A fishery decision-making framework incorporating
               the Precautionary Approach.   (L4127)
               matches paper09 v30 L1958-1959.
  6. L4150  Geological Survey Circular 1186, Denver, CO.
            -> Alley, W.M., Reilly, T.E. and Franke, O.L., 1999.
               \emph{Sustainability of Ground-Water Resources}. U.S.   (L4091)
               the head ends in a dangling "U.S."; matches paper10b v1 L1130-1131.
  7. L4243  Water Data for Texas, well 6837203 (J-17). https://...
            -> Texas Water Development Board.   (L4241)
               matches paper10b v1 L1115-1116. Found late: it does not open
               with a journal/publisher token, so the detector never flagged it.
  8. L4130  DFO 2016 appears twice in one paragraph, in the two citation styles
            of the two sources that carry it ("DFO, 2016. ..." and
            "DFO (2016). ..."). Split into two entries. They are the same
            report (2016/026) and are deliberately NOT merged -- conservative
            de-duplication -- so the duplicate stays visible as a non-fatal
            L.dup-ref-key for a human to reconcile.

=============================================================================
PART 2 -- DECLARATIONS
=============================================================================
Three blocks, each belonging to a different constituent, all of it live content:

  A (L4255) COD      -- Data availability (wave_e_cod runners, N=20,000, B=2000),
                        CRediT, competing interest, funding, Code availability
                        (paperE2_cod_intervention_v29_*), AI declaration
  B (L4358) ARV      -- Funding, competing interests, Data availability
                        (calibration record), Code availability
                        (applied_regime_viability_v9_verification.py,
                        paper2_arv_record_figure_v1.py), AI declaration
  C (L4388) Edwards  -- Data Availability Statement (J-17, recharge, pumpage,
                        frozen protocol 2026-08-26, campaign_e4_elevation.py,
                        e4_audit_layer.py), Funding, competing interests,
                        Code availability
                        (paperE4_edwards_intervention_v16_verification.py),
                        AI declaration

Collapsed into ONE \section*{Declarations}. Topic by topic:
  - Data availability: three genuinely different statements, all kept, in
    constituent order with a lead-in naming each.
  - Funding / Competing interests: all three agree; stated once.
  - Code availability: three distinct script sets, all kept, with lead-ins.
  - AI declaration: identical in all three; stated once.
  - CRediT: kept as the placeholder it is -- it must be written, not invented.
"""
from __future__ import annotations

import io
import re
import sys

PATH = "/home/user/papers/paper09_cod_certification_v32.tex"

# ---------------------------------------------------------------- part 1: refs

# (label, old_text, new_text, expected_count)
REF_EDITS = [
    # -- deletions: lift each tail out of its sorted-by-publisher position
    ("del Birkhauser x2",
     "Ecol. Econ. 36, 385--396.\n\n"
     "Birkh\\\"auser, Boston.\n\n"
     "Birkh\\\"auser, Boston.\n\n",
     "Ecol. Econ. 36, 385--396.\n\n", 1),
    ("del EAA San Antonio #1",
     "index wells.\n\nEdwards Aquifer Authority, San Antonio, TX.\n\n",
     "index wells.\n\n", 1),
    ("del EAA San Antonio #2",
     "\\emph{Habitat Conservation Plan}.\n\n"
     "Edwards Aquifer Authority, San Antonio, TX.\n\n"
     "Fisheries and Oceans Canada, Ottawa.\n\n"
     "Geological Survey Circular 1186, Denver, CO.\n\n",
     "\\emph{Habitat Conservation Plan}.\n\n", 1),
    ("del Water Data tail",
     "Texas Water Development Board.\n\n"
     "Water Data for Texas, well 6837203\n",
     "Texas Water Development Board.", 1),
    # -- reattachments: append each tail to the head it was cut from
    ("Aubin <- Birkhauser",
     "Aubin, J.-P., 1991. \\emph{Viability Theory}.\n",
     "Aubin, J.-P., 1991. \\emph{Viability Theory}. "
     "Birkh\\\"auser, Boston.\n", 1),
    ("EAA 2024 <- San Antonio",
     "index wells.\n\n",
     "index wells. Edwards Aquifer Authority, San Antonio, TX.\n\n", 1),
    ("EARIP 2021 <- San Antonio",
     "\\emph{Habitat Conservation Plan}.\n\n",
     "\\emph{Habitat Conservation Plan}. "
     "Edwards Aquifer Authority, San Antonio, TX.\n\n", 1),
    ("DFO 2009 <- Ottawa",
     "DFO, 2009. A fishery decision-making framework incorporating the\n"
     "Precautionary Approach.\n",
     "DFO, 2009. A fishery decision-making framework incorporating the\n"
     "Precautionary Approach. Fisheries and Oceans Canada, Ottawa.\n", 1),
    ("Alley 1999 <- Circular 1186",
     "\\emph{Sustainability of Ground-Water\nResources}. U.S.\n",
     "\\emph{Sustainability of Ground-Water\nResources}. U.S. "
     "Geological Survey Circular 1186, Denver, CO.\n", 1),
    ("TWDB <- Water Data",
     "Texas Water Development Board.",
     "Texas Water Development Board. Water Data for Texas, well 6837203\n", 1),
    ("split doubled DFO 2016",
     "DFO Can. Sci. Advis. Sec. Sci. Advis. Rep.~2016/026.\n"
     "DFO (2016). Stock assessment of Northern cod (NAFO 2J3KL). \\emph{Can.\n"
     "Sci. Advis. Sec. Sci. Advis. Rep.} 2016/026.\n",
     "DFO Can. Sci. Advis. Sec. Sci. Advis. Rep.~2016/026.\n\n"
     "DFO (2016). Stock assessment of Northern cod (NAFO 2J3KL). \\emph{Can.\n"
     "Sci. Advis. Sec. Sci. Advis. Rep.} 2016/026.\n", 1),
]


def fix_refs(src: str, log):
    for label, old, new, want in REF_EDITS:
        n = src.count(old)
        if n != want:
            log.append("  !! %-34s expected %d occurrence(s), found %d"
                       % (label, want, n))
            return None
        src = src.replace(old, new, want)
        log.append("  ok %-34s (%d)" % (label, n))
    return src


# --------------------------------------------------------- part 2: declarations

COD_HEAD = "https://github.com/MIKEAA2020/general-sustainability. The primary kernel"
ARV_HEAD = "\\section*{Declarations}\n\n\\section*{Funding}"
EDW_HEAD = ("\\section*{Declarations}\n\n"
            "\\subsection*{Data Availability Statement}")


def slice_block(src, start_marker, end_marker):
    i = src.index(start_marker)
    j = src.index(end_marker, i)
    return src[i:j], i, j


def between(block, start_pat, end_pat=None):
    m = re.search(start_pat, block)
    if not m:
        return None
    i = m.end()
    if end_pat:
        n = re.search(end_pat, block[i:])
        return block[i:i + n.start()] if n else block[i:]
    return block[i:]


def tidy(t):
    t = re.sub(r'\n{3,}', '\n\n', t.strip())
    return t.rstrip()


def build_declarations(src, log):
    m = re.search(r'\\section\*\{Declarations\}', src)
    head = src[:m.start()]

    cod_full = src[m.start():]           # block A .. end of file
    j = cod_full.index(ARV_HEAD)         # A ends where B starts
    blkA = cod_full[:j]
    rest = cod_full[j:]
    k = rest.index(EDW_HEAD)             # B ends where C starts
    blkB_whole = rest[:k]
    blkC = rest[k:]

    # A -- COD
    cod_da = between(blkA, r'\\subsection\*\{Data availability\}\n',
                     r'\\subsection\*\{CRediT')
    cod_credit = between(blkA, r'\\subsection\*\{CRediT[^}]*\}\n',
                         r'\\subsection\*\{Declaration of competing')
    cod_ci = between(blkA, r'\\subsection\*\{Declaration of competing interest\}\n',
                     r'\\subsection\*\{Funding\}')
    cod_fund = between(blkA, r'\\subsection\*\{Funding\}\n',
                       r'\\subsection\*\{Code availability\}')
    cod_code = between(blkA, r'\\subsection\*\{Code availability\}\n',
                       r'\\subsection\*\{AI declaration\}')
    cod_ai = between(blkA, r'\\subsection\*\{AI declaration\}\n')

    # B -- ARV
    arv_da = between(blkB_whole, r'\\section\*\{Data availability\}\n',
                     r'\\section\*\{Code availability\}')
    arv_code = between(blkB_whole, r'\\section\*\{Code availability\}\n',
                       r'\\section\*\{AI declaration\}')

    # C -- Edwards
    edw_da = between(blkC, r'\\subsection\*\{Data Availability Statement\}\n',
                     r'\\subsection\*\{Funding\}')
    edw_code = between(blkC, r'\\subsection\*\{Code availability\}\n',
                       r'\\subsection\*\{AI declaration\}')

    for name, val in [("cod_da", cod_da), ("cod_credit", cod_credit),
                      ("cod_ci", cod_ci), ("cod_fund", cod_fund),
                      ("cod_code", cod_code), ("cod_ai", cod_ai),
                      ("arv_da", arv_da), ("arv_code", arv_code),
                      ("edw_da", edw_da), ("edw_code", edw_code)]:
        if not val or not val.strip():
            log.append("  !! declaration fragment %s came back empty" % name)
            return None

    out = []
    out.append("\\section*{Declarations}\n\n")

    out.append("\\subsection*{Data availability}\n\n")
    out.append(tidy(cod_da) + "\n\n")
    out.append("\\emph{Applied-regime-viability record.} "
               + tidy(arv_da) + "\n\n")
    out.append("\\emph{Edwards Aquifer.} " + tidy(edw_da) + "\n\n")

    out.append("\\subsection*{Funding}\n\n")
    out.append(tidy(cod_fund) + "\n\n")

    out.append("\\subsection*{Declaration of competing interest}\n\n")
    out.append(tidy(cod_ci) + "\n\n")

    out.append("\\subsection*{Code availability}\n\n")
    out.append(tidy(cod_code) + "\n\n")
    out.append("\\emph{Applied-regime-viability record.} "
               + tidy(arv_code) + "\n\n")
    out.append("\\emph{Edwards Aquifer.} " + tidy(edw_code) + "\n\n")

    out.append("\\subsection*{CRediT authorship contribution statement}\n\n")
    out.append(tidy(cod_credit) + "\n\n")

    out.append("\\subsection*{AI declaration}\n")
    out.append(tidy(cod_ai) + "\n")

    return head + "".join(out) + "\n\\end{document}\n"


def main() -> int:
    apply = "--apply" in sys.argv
    src = io.open(PATH, encoding="utf-8").read()
    log = []

    log.append("PART 1 -- bibliography")
    src2 = fix_refs(src, log)
    if src2 is None:
        print("\n".join(log))
        return 2
    log.append("PART 2 -- declarations")
    out = build_declarations(src2, log)
    if out is None:
        print("\n".join(log))
        return 2

    print("\n".join(log))
    print()
    print("size: %d -> %d chars (%+d)" % (len(src), len(out), len(out) - len(src)))

    if not apply:
        print("\nDRY RUN - nothing written. Re-run with --apply.")
        return 0
    io.open(PATH, "w", encoding="utf-8").write(out)
    print("\napplied: %s" % PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
