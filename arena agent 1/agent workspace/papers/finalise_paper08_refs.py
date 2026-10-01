#!/usr/bin/env python3
"""Structural repair of paper08's reference list.

Two defects remain after the tail reattachment and de-duplication passes:

  1. The "Supplementary material" section sits in the MIDDLE of the
     bibliography, splitting it into two blocks -- rule, \\subsection{Supple-
     mentary material} and its prose come between "Zhang" and "Nesic", and the
     remaining references (Nesic ... World Bank) follow the prose. It is prose,
     not a citation, so it belongs after the reference list. A second, separate
     supplementary paragraph follows the closing rule and stays where it is.

  2. The list is not alphabetical. Entries were scrambled when heads and tails
     were sorted separately and re-merged: Hutchinson, Karlsson and Kuang sit
     between "Alkire" and "Ashwin"; Moore precedes Lomb; the DFO block and
     Halanay follow Ostrom; Shertzer, Walters and Zhang end the first block.

Also separates the first entry (Astrom 1997) from the \\subsection*{References}
heading, which it was glued to.

Sort key: first author's surname with LaTeX accents and braces stripped,
year as tie-breaker.

Dry run by default; --apply writes.
"""
import os
import re
import sys

from label_fetch import PAPERS

FN = "paper08_governance_delay_v46.tex"
RULE = r"\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}"
WIDTH = 78

ACCENTS = [
    (r"\AA", "A"), (r"\aa", "a"), (r"\'a", "a"), (r"\'e", "e"), (r"\'i", "i"),
    (r"\'o", "o"), (r"\'u", "u"), (r"\'c", "c"), (r"\'s", "s"), (r"\^e", "e"),
    (r"\~a", "a"), (r"\~n", "n"), (r"\~o", "o"), (r"\'A", "A"), (r"\'E", "E"),
    (r"\'I", "I"), (r"\'O", "O"), (r"\'U", "U"), (r"\v{s}", "s"), (r"\v{S}", "S"),
]


def sort_key(entry):
    text = re.sub(r"\s+", " ", entry).strip()
    # surname = everything up to the first ", " or ". ". Splitting on "," alone
    # is wrong: "DFO. 2011. ... (NAFO Divs. 2GHJ, 3KLNO) ..." has a comma inside
    # the title and no comma after the name.
    m = re.match(r"^(.*?)(?:,\s|\.\s)", text + " ")
    head = m.group(1) if m else text.split(",")[0]
    for k, v in ACCENTS:
        head = head.replace(k, v)
    head = re.sub(r"\\[A-Za-z]+", "", head)
    head = head.replace("{", "").replace("}", "")
    head = re.sub(r"[^A-Za-z\- ]", "", head).strip()
    m = re.search(r"\b(1[89]\d{2}|20\d{2})\b", text)
    return (head.lower(), m.group(1) if m else "9999", text.lower())


def blocks(lines):
    out, cur, at = [], [], None
    for i, l in enumerate(lines):
        if l.strip():
            if at is None:
                at = i
            cur.append(l)
        else:
            if cur:
                out.append((at, cur))
            cur, at = [], None
    if cur:
        out.append((at, cur))
    return out


def wrap(text, width=WIDTH):
    out, line = [], ""
    for w in text.split():
        if len(line) + len(w) + 1 > width and line:
            out.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    if line:
        out.append(line)
    return out


def main():
    dry = "--apply" not in sys.argv
    p = os.path.join(PAPERS, FN)
    lines = open(p, encoding="utf-8", errors="replace").read().split("\n")

    refs_i = next(i for i, l in enumerate(lines)
                  if l.startswith(r"\subsection*{References}"))
    decl_i = next(i for i, l in enumerate(lines)
                  if re.search(r"\\section\*\{Declarations\}", l))
    sup_i = next(i for i, l in enumerate(lines)
                 if l.startswith(r"\subsection{Supplementary material}"))

    # rule immediately above the Supplementary material heading
    rule1_i = next(i for i in range(sup_i - 1, sup_i - 6, -1)
                   if lines[i].strip() == RULE)
    # the prose is the single block after the heading
    prose1 = next((a, bl) for a, bl in blocks(lines) if a > sup_i)
    sup_end = prose1[0] + len(prose1[1])          # end of the prose block

    # the closing rule, after the second run of references
    rule2_i = next(i for i in range(sup_end, decl_i) if lines[i].strip() == RULE)

    print("References heading      L%d" % (refs_i + 1))
    print("Supplementary material  L%d-L%d" % (rule1_i + 1, sup_end))
    print("closing rule            L%d" % (rule2_i + 1))
    print("Declarations            L%d\n" % (decl_i + 1))

    # ---- collect entries: everything between heading and Declarations that is
    #      not the supplementary section and not a rule ----------------------
    entries, astrom = [], None
    for a, bl in blocks(lines):
        if not (refs_i < a < decl_i):
            continue
        if rule1_i <= a < sup_end:               # supplementary section
            continue
        txt = re.sub(r"\s+", " ", " ".join(x.strip() for x in bl)).strip()
        if txt == RULE or txt.startswith("\\"):
            continue
        if txt.startswith("Wittenmark, B., 1997."):
            astrom = txt
            continue
        entries.append(txt)

    # the first entry is glued to the References heading
    if astrom is None:
        m = re.search(r"\n(\\AA\{\}str\\\"om, K\.J\., Wittenmark,.*?Saddle River\.)",
                      "\n".join(lines), re.S)
        if m:
            astrom = re.sub(r"\s+", " ", m.group(1)).strip()
    assert astrom, "Astrom 1997 entry not found"
    entries.append(astrom)

    print("reference entries collected: %d" % len(entries))
    ordered = sorted(entries, key=sort_key)
    moved = sum(1 for a, b in zip(entries, ordered) if a != b)
    print("entries that change position: %d\n" % moved)

    print("--- resulting order ---")
    for e in ordered:
        print("   %s" % e[:88])

    if dry:
        print("\n(re-run with --apply to write)")
        return

    # ---- rebuild -----------------------------------------------------------
    new = lines[:refs_i + 1]          # \subsection*{References}
    new.append("")
    for e in ordered:
        new.extend(wrap(e))
        new.append("")
    new.extend(lines[rule1_i:rule2_i])   # rule + Supplementary material + prose
    new.append("")
    new.extend(lines[rule2_i:])          # closing rule + 2nd para + Declarations

    open(p, "w", encoding="utf-8").write("\n".join(new))
    print("\nwritten: %d -> %d lines" % (len(lines), len(new)))


if __name__ == "__main__":
    main()
