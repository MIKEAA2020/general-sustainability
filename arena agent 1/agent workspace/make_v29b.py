#!/usr/bin/env python3
"""Second pass on v29: fix what the first pass's escaping got wrong.

Uses plain literal strings only -- no regex, no escaping surprises.
"""
from pathlib import Path

P = Path("/home/user/fam/e2/paperE2_cod_intervention_v29.tex")
t = P.read_text(encoding="utf-8")

EDITS = [
    # --- constructive bound at C (Section 3.8) -----------------------------
    ("stoch C value",
     r"At \(C = 57.6\) kt the 20-year survival probability from the LRP is",
     r"At \(C = 91.59\) kt the 20-year survival probability from the LRP is"),

    ("stoch P at C",
     r"""\(0.77\) under i.i.d. draws, \(0.79\) under blocks, and \(0.88\) when
the 1992 residual is removed.""",
     r"""\(0.74\) under i.i.d. draws, \(0.73\) under blocks, and \(0.84\) when
the 1992 residual is removed."""),

    ("stoch caps",
     r"""at \(0.868\) and block survival at \(0.808\)""",
     r"""at \(0.906\) and block survival at \(0.849\)"""),

    ("stoch P>=0.8 crossings",
     r"""crossings are \(48.4\) kt (i.i.d.),
\(38.9\) kt (blocks), and \(95.1\) kt (no-1992).""",
     r"""crossings are \(81.2\) kt (i.i.d.),
\(72.3\) kt (blocks), and \(105.2\) kt (no-1992)."""),

    ("stoch at bound again",
     r"""falls to \(0.77\) under i.i.d. draws (\(0.79\) under
blocks, \(0.88\) without the 1992 draw)""",
     r"""falls to \(0.74\) under i.i.d. draws (\(0.73\) under
blocks, \(0.84\) without the 1992 draw)"""),

    ("stoch range",
     r"(\(0.87\) at zero-to-moratorium removals to \(0.58\) at \(120\) kt).",
     r"(\(0.91\) at zero-to-moratorium removals to \(0.65\) at \(120\) kt)."),

    # --- Table 4: block / no-1992 / 1500-kt columns (regenerated) ----------
    ("T4 zero catch",
     r"zero catch & 0.906 & 0.862 & 0.958 & 1.000 \\",
     r"zero catch & 0.906 & 0.852 & 0.954 & 1.000 \\"),
    ("T4 BAU",
     r"BAU (5 kt) & 0.903 & 0.857 & 0.955 & 1.000 \\",
     r"BAU (5 kt) & 0.903 & 0.852 & 0.954 & 1.000 \\"),
    ("T4 60 kt",
     r"60 kt / S1 / cascade & 0.835 & 0.816 & 0.899 & 1.000 \\",
     r"60 kt / S1 / cascade & 0.835 & 0.806 & 0.917 & 1.000 \\"),
    ("T4 120 kt",
     r"120 kt & 0.647 & 0.650 & 0.766 & 0.996 \\",
     r"120 kt & 0.647 & 0.650 & 0.769 & 0.999 \\"),
]

applied, missing = [], []
for label, old, new in EDITS:
    n = t.count(old)
    if n != 1:
        missing.append(f"{label} (found {n})")
        continue
    t = t.replace(old, new, 1)
    applied.append(label)

P.write_text(t, encoding="utf-8")
print(f"applied {len(applied)}   missing {len(missing)}")
for m in missing:
    print("  MISS:", m)
