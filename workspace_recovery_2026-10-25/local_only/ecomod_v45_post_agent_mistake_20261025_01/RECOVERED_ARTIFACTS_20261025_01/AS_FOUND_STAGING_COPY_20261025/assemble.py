"""Assemble temporary working TeX files from the editable ECOMOD source parts.

Edition metadata is maintained in the source parts; this script only assembles
the working TeX inputs and inlines the SI tables. It does not rename outputs.
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

Path("manuscript_working_main.tex").write_text(
    "".join(Path(p).read_text(encoding="utf-8") for p in MAIN_PARTS), encoding="utf-8"
)
si = "".join(Path(p).read_text(encoding="utf-8") for p in SI_PARTS)
si = re.sub(
    r"\\input\{(parts/si_tab_[a-z]+\.tex)\}\n?",
    lambda m: Path(m.group(1)).read_text(encoding="utf-8").rstrip("\n") + "\n",
    si,
)
assert "\\input{" not in si
Path("manuscript_working_si.tex").write_text(si, encoding="utf-8")
print("assembled working main + SI (SI tables inlined; edition metadata comes from parts)")
