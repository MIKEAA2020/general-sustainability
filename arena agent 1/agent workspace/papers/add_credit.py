#!/usr/bin/env python3
"""Add a CRediT authorship template to paper09 v32 and paper08 v46.

Dry-run by default; --apply writes the files.

WHY A TEMPLATE AND NOT A FILLED STATEMENT
    Who did what is a fact about the people, not about the manuscript. It
    cannot be inferred from the .tex and must not be invented. But a bare
    "to be completed" placeholder is worse than useless: it gives the author
    nothing to fill in and no reminder of what the taxonomy covers, so it gets
    skipped at submission. A template with the full 14-role list and the
    blanks marked is fill-in-the-blank rather than composition from scratch.

    Neither paper declares \\author. The self-citations read "Abaee, A.",
    but the full name is not asserted anywhere in the file, so the name is
    left as a blank rather than assumed.

WHAT IS INSERTED
    The taxonomy is the standard CRediT set of 14 roles. For a single-author
    manuscript the usual outcome is that one name carries most or all of them,
    but that is a decision for the author, so all 14 are listed.

  paper09 v32  replaces "[To be completed at submission.]" in the existing
               CRediT subsection.
  paper08 v46  has no CRediT subsection at all; one is added before the AI
               declaration, which is where the other Declarations subsections
               already sit.
"""
from __future__ import annotations

import io
import sys

CREDIT_ROLES = (
    "Conceptualization, Methodology, Software, Validation, Formal analysis, "
    "Investigation, Resources, Data Curation, Writing~-- original draft, "
    "Writing~-- review \\& editing, Visualization, Supervision, Project "
    "administration, Funding acquisition"
)

# the BODY only. paper09 already has the heading (its CRediT subsection held a
# bare placeholder), so including the heading here duplicated it.
BODY = (
    "\\textbf{[AUTHOR NAME --- full name as it should appear]}: "
    "[list the roles that apply, deleting those that do not].\n"
    "\n"
    "The CRediT taxonomy comprises 14 roles; delete any that do not apply to\n"
    "this work and do not add roles outside the taxonomy:\n"
    "\\emph{%s}.\n"
    "\n"
    "If there are multiple authors, give one such line per author. If any\n"
    "contributor is an AI tool rather than a person, it belongs in the AI\n"
    "declaration below, not here.\n"
) % CREDIT_ROLES

TARGETS = [
    # (path, mode, anchor)
    ("/home/user/papers/paper09_cod_certification_v32.tex", "replace",
     "{[}To be completed at submission.{]}\n"),
    ("/home/user/papers/paper08_governance_delay_v46.tex", "insert_before",
     "\\subsection*{AI declaration}\n"),
]


def main() -> int:
    apply = "--apply" in sys.argv
    ok = True
    for path, mode, anchor in TARGETS:
        src = io.open(path, encoding="utf-8").read()
        name = path.rsplit("/", 1)[-1]
        n = src.count(anchor)
        if n != 1:
            print("  !! %-42s anchor found %d times (expected 1)" % (name, n))
            ok = False
            continue
        if mode == "replace":
            # heading already present -- replace the placeholder with the body
            out = src.replace(anchor, BODY, 1)
            verb = "replaced placeholder with"
        else:
            ins = ("\\subsection*{CRediT authorship contribution statement}\n\n"
                   + BODY + "\n" + anchor)
            out = src.replace(anchor, ins, 1)
            verb = "inserted CRediT subsection before"
        print("  ok %-42s %s the anchor (%+d chars)"
              % (name, verb, len(out) - len(src)))
        if apply:
            io.open(path, "w", encoding="utf-8").write(out)

    if not ok:
        return 2
    if not apply:
        print("\nDRY RUN - nothing written. Re-run with --apply.")
        return 0
    print("\napplied to %d file(s)" % len(TARGETS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
