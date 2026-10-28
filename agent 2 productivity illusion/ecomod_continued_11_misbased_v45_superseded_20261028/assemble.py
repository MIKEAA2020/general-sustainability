"""Assemble the local Continued 11 revision-draft TeX outputs from editable parts.

Edition metadata is maintained in the source parts. The SI table bodies are
inlined, and outputs keep the Continued 11 draft name/date. The archived C10
sources and release artifacts are separate and remain unchanged.
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

MAIN_OUT.write_text(
    "".join(Path(p).read_text(encoding="utf-8") for p in MAIN_PARTS), encoding="utf-8"
)
si = "".join(Path(p).read_text(encoding="utf-8") for p in SI_PARTS)
si = re.sub(
    r"\\input\{(parts/si_tab_[a-z]+\.tex)\}\n?",
    lambda m: Path(m.group(1)).read_text(encoding="utf-8").rstrip("\n") + "\n",
    si,
)
assert "\\input{" not in si
SI_OUT.write_text(si, encoding="utf-8")
# Retire generic and superseded root-level working names. These were local
# intermediates, not archived C10 release artifacts.
for stale in (
    Path("manuscript_working_main.tex"),
    Path("manuscript_working_si.tex"),
    Path("ecomod_continued_10_revision_draft_20261028.tex"),
    Path("ecomod_continued_10_revision_draft_20261028_SI.tex"),
):
    if stale.exists():
        stale.unlink()
print(f"assembled local Continued 11 draft main + SI: {MAIN_OUT}, {SI_OUT}")
