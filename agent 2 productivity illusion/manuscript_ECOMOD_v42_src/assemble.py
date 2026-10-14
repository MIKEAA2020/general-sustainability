"""Assemble manuscript_ECOMOD_v42.tex and manuscript_ECOMOD_v42_supplementary.tex from parts/.
Run from the folder that contains parts/ (locally: ecomod_v42/; in the repository: manuscript_ECOMOD_v42_src/)."""
import pathlib, re
main = ["parts/00_front.tex", "parts/01_methods.tex", "parts/02_results.tex", "parts/03_discussion.tex", "parts/04_refs.tex"]
si = ["parts/si_00.tex", "parts/si_01.tex", "parts/si_02.tex", "parts/si_refs.tex"]
pathlib.Path("manuscript_ECOMOD_v42.tex").write_text("".join(pathlib.Path(p).read_text() for p in main))
s = "".join(pathlib.Path(p).read_text() for p in si)
s = re.sub(r"\\input\{(parts/si_tab_[a-z]+\.tex)\}\n?", lambda m: pathlib.Path(m.group(1)).read_text().rstrip("\n") + "\n", s)
assert "\\input{" not in s
pathlib.Path("manuscript_ECOMOD_v42_supplementary.tex").write_text(s)
print("assembled main + SI (generated SI tables inlined)")
