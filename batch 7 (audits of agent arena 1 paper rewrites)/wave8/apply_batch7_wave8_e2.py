#!/usr/bin/env python3
"""E2 v21 (wave-8 owner-directed presentation pass).

Changes:
  1. The version-log paragraph before the abstract is removed.
  2. The abstract is tightened from 459 to under 315 words. All five
     numbered findings, every recorded value, the frozen-protocol
     disclosure, and the scoped closing reading are preserved; the
     cuts are phrasal redundancy, the duplicated scoping hedge, and
     the change-log-flavoured "now ... / earlier ... verdict does not
     survive" narration, recast as a convention comparison. The
     "two new switch-above-the-LRP reactive families" loses the
     vacuous "new" (the family list defines them; their post-freeze
     status is disclosed where it is load-bearing, Table 1's caption).
  3. Keywords 5 -> 7: "NAFO 2J3KL" and "robust viability kernel"
     added.
  4. Figure 2 reference points at the regenerated figure
     figs_e2/fig2_kernel_vs_catch_v21.png (labels raised clear of the
     horizontal flat segment; built by make_fig_e2_v21.py).
  5. In-body meta-narration recasts, none touching a value:
     - "Why the filter vocabulary is retired" -> "is not used";
       "are demoted to definitional notes" -> "are stated as
       definitional notes";
     - Result 3.1's lead "demoted to a definitional note" -> "stated
       as a definitional note";
     - Definitional note 3.2's "This statement is demoted from a
       numbered result to a note" -> "This statement is a definitional
       note rather than a numbered result";
     - Section 4's "The earlier claim that boundary-harvesting rules
       are ... is not an identified finding but a consequence of the
       frozen convention's harsh floor classes" -> present-tense
       convention comparison ("The boundary-harvesting rules' ...
       reading under the frozen convention is not an identified
       finding but a consequence of that convention's harsh floor
       classes").
Fail-loud; byte-reproducible; writes paperE2_cod_intervention_v21.md.
"""
from __future__ import annotations
import hashlib
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites"
OLD = SRC / "paperE2_cod_intervention_v20.md"
NEW = SRC / "paperE2_cod_intervention_v21.md"

text = OLD.read_text()
orig = text


def rep(old: str, new: str, n: int = 1):
    global text
    assert text.count(old) == n, f"needle x{text.count(old)} (want {n}): {old[:90]!r}"
    text = text.replace(old, new)


# --- 1. remove the version-log paragraph ------------------------------
m = re.search(r"\*Version log \(v20\)\.\*[^\n]*\n\n", text)
assert m, "version log paragraph not found"
text = text[:m.start()] + text[m.end():]
assert "*Version log" not in text

# --- 2. the abstract: one paragraph, replaced wholesale ---------------
ABSTRACT_OLD = text.split("## Abstract\n\n", 1)[1].split("\n\n**Keywords:**", 1)[0]
assert ABSTRACT_OLD.startswith("The governed object of this paper is a single fitted map"), ABSTRACT_OLD[:80]

ABSTRACT_NEW = (
    "The governed object is the least-squares surplus-production map fitted to the "
    "1983\u20132007 Northern cod (NAFO 2J3KL) SSB series ($r = 0.2369$; $K = 5000$ kt "
    "at its bound, a declared fit defect) \u2014 every statement scoped to that map "
    "and its declared classes. The declared catch-policy family \u2014 moratorium "
    "removals, flat caps, the critical-zone rule, a cascade, and two reactive "
    "families \u2014 is scored against the 2016 reference point ($884.6$ kt) under "
    "persistent productivity floors, the year-$t$ catch driving the $t \\to t+1$ "
    "transition, under a protocol frozen before any score was computed: a module is "
    "kept only if it improves the declared protection-and-supply outcome. (1) Under "
    "the informative 10th-percentile class, zero catch and the moratorium hold the "
    "safe set; the largest robust constant catch is $91.6$ kt; the critical-zone and "
    "cascade rules hold the LRP from itself, reversing the frozen convention\u2019s "
    "\u201cless protective\u201d reading. (2) No non-BAU policy dominates BAU under "
    "the declared partial order: every positive-catch rule is empty at the "
    "5th-percentile class, $T=\\infty$, and the surplus-proportional family \u2014 "
    "reactive, protective at $\\phi \\le 0.5$ under the informative class, "
    "harvesting more than the moratorium \u2014 comes closest without dominating. "
    "(3) The map is expansive at the LRP for every admissible $K \\ge 2K^* = 1769.2$ "
    "kt (not an artifact of the pinned $K$), so certified kernels are empty beyond "
    "seven years. (4) Stochastic viability gives 20-year survival from the LRP of "
    "$0.91$ (zero catch) to $0.65$ ($120$ kt); its $90\\%$ bootstrap interval is "
    "$[0, 87.1]$ kt. (5) The depensatory refit leaves the constructive, selection, "
    "and expansion certificates intact; only the class-vacuity reading reverses. "
    "Only the perpetual-worst floor exceeds the map\u2019s maximum surplus "
    "($g_{\\max} = 296$ kt yr$^{-1}$) \u2014 an arithmetic identity; the 5th- and "
    "10th-percentile classes are informative. On this map the LRP is protected by "
    "good years, but the margin they must supply is smaller than the frozen "
    "convention implied."
)
rep(ABSTRACT_OLD, ABSTRACT_NEW)
nwords = len(re.findall(r"\S+", ABSTRACT_NEW))
assert nwords < 315, nwords

# --- 3. keywords 5 -> 7 -----------------------------------------------
rep("**Keywords:** northern cod; surplus production; viability; harvest control "
    "rules; limit reference point",
    "**Keywords:** northern cod; NAFO 2J3KL; surplus production; viability; "
    "robust viability kernel; harvest control rules; limit reference point")

# --- 4. Figure 2 path --------------------------------------------------
rep("![Figure 2](figs_e2/fig2_kernel_vs_catch.png)",
    "![Figure 2](figs_e2/fig2_kernel_vs_catch_v21.png)")

# --- 5. in-body meta-narration recasts ---------------------------------
rep("*Why the filter vocabulary is retired.*", "*Why the filter vocabulary is not used.*")
rep("are demoted to definitional notes.",
    "are stated as definitional notes.")
rep("The first result concerns dominance; the second is the vacuous-class identity, "
    "demoted to a definitional note.",
    "The first result concerns dominance; the second is the vacuous-class identity, "
    "stated as a definitional note.")
rep("This statement is demoted from a numbered result to a note: it is an "
    "arithmetic identity of the declared class,",
    "This statement is a definitional note rather than a numbered result: it is an "
    "arithmetic identity of the declared class,")
rep('The earlier claim that boundary-harvesting rules are "less protective by '
    'declared geometry" is not an identified finding but a consequence of the '
    "frozen convention's harsh floor classes:",
    'The boundary-harvesting rules\' "less protective by declared geometry" '
    'reading under the frozen convention is not an identified finding but a '
    "consequence of that convention's harsh floor classes:")

NEW.write_text(text)

# --- verification -------------------------------------------------------
def abstract_words(t):
    lines = t.split("\n")
    a = next(i for i, l in enumerate(lines) if l.strip() == "## Abstract")
    b = next(i for i in range(a + 1, len(lines)) if lines[i].startswith("## "))
    body = [l for l in lines[a + 1:b] if l.strip() and not l.startswith("**Keywords")]
    return sum(len(re.findall(r"\S+", l)) for l in body)

assert abstract_words(text) == nwords < 315, (abstract_words(text), nwords)
kw = next(l for l in text.split("\n") if l.startswith("**Keywords"))
assert len(kw.split(";")) == 7, kw
for needle in ["$r = 0.2369$", "$884.6$ kt", "91.6", "1769.2", "$0.91$",
               "$[0, 87.1]$ kt", "$g_{\\max} = 296$", "$2219.6$ kt",
               "fig2_kernel_vs_catch_v21.png"]:
    assert needle in text, needle
for banned in ["*Version log", " at this revision", "of earlier version",
               "demoted to definitional notes", "The earlier claim"]:
    assert banned not in text, banned


def table_lines(t):
    return [l for l in t.split("\n") if l.lstrip().startswith("|")]


# Table 2's one label row was harmonised in v20 and is unchanged here.
assert table_lines(text) == table_lines(orig), "table rows changed"

print("E2 v21 written;", len(orig), "->", len(text), "chars")
print("abstract words:", nwords)
print("MD5:", hashlib.md5(text.encode()).hexdigest())
