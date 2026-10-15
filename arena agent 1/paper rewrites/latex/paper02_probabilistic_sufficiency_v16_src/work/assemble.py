"""Assemble the main text and the supplement from their parts; inline generated tables."""
import re, glob, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
def cat(files):
    return "".join(open(f).read() if open(f).read().endswith("\n") else open(f).read()+"\n" for f in files)
main = cat(sorted(glob.glob(str(root/"parts"/"0*.tex"))) + sorted(glob.glob(str(root/"parts"/"1*.tex"))))
(root/"paper02_probabilistic_sufficiency_v16.tex").write_text(main)
si_files = [root/"si_parts"/"S0_front.tex", root/"si_parts"/"S0b_mainlabels.tex"] + [pathlib.Path(p) for p in sorted(glob.glob(str(root/"si_parts"/"S[1-8]_*.tex")))]
si = cat([str(p) for p in si_files])
def inline(m):
    body = (root/m.group(1)).read_text()
    return body if body.endswith("\n") else body+"\n"
si = re.sub(r"\\input\{(si_parts/tab_[a-z]+\.tex)\}\n?", inline, si)
(root/"paper02_probabilistic_sufficiency_v16_supplementary.tex").write_text(si)
print("main", len(main.splitlines()), "lines; SI", len(si.splitlines()), "lines")
