"""Assemble the local ECOMOD Continued 11 revision draft.

The main and SI modules were rebased from the actual assembled Continued 10
main/SI sources identified in README.md. Supplementary table bodies are kept as
separate parts and inlined in the assembled SI output.
"""
from pathlib import Path
import re

MAIN_PARTS = [
    "parts/00_front.tex",
    "parts/01_methods.tex",
    "parts/02_results.tex",
    "parts/03_discussion.tex",
    "parts/04_refs.tex",
]
SI_PARTS = [
    "parts/si_00.tex",
    "parts/si_01.tex",
    "parts/si_02.tex",
    "parts/si_refs.tex",
]
MAIN_OUT = Path("ecomod_continued_11_revision_draft_20261028.tex")
SI_OUT = Path("ecomod_continued_11_revision_draft_20261028_SI.tex")

main = "".join(Path(p).read_text(encoding="utf-8") for p in MAIN_PARTS)
si = "".join(Path(p).read_text(encoding="utf-8") for p in SI_PARTS)
si = re.sub(
    r"\\input\{(parts/si_tab_(?:delay|drawdown|recovery)\.tex)\}\n?",
    lambda m: Path(m.group(1)).read_text(encoding="utf-8").rstrip("\n") + "\n",
    si,
)
if "\\input{" in si:
    raise SystemExit("unexpanded input remains in assembled SI")
MAIN_OUT.write_text(main, encoding="utf-8")
SI_OUT.write_text(si, encoding="utf-8")
print(f"assembled {MAIN_OUT} and {SI_OUT}")
