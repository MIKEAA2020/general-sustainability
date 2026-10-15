"""Assemble the main text and the supplement from their parts; inline generated tables."""
import re, glob, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
NAME = "paper04_minimax_dual_certificates_v20"
def cat(files):
    out = ""
    for f in files:
        t = open(f).read()
        out += t if t.endswith("\n") else t + "\n"
    return out
main = cat(sorted(glob.glob(str(root/"parts"/"0*.tex"))) + sorted(glob.glob(str(root/"parts"/"1*.tex"))))
(root/f"{NAME}.tex").write_text(main)
si_files = [root/"si_parts"/"S0_front.tex", root/"si_parts"/"S0b_mainlabels.tex"] + [pathlib.Path(p) for p in sorted(glob.glob(str(root/"si_parts"/"S[1-9]_*.tex")))]
si_files = [p for p in si_files if p.exists()]
si = cat([str(p) for p in si_files])
def inline(m):
    body = (root/m.group(1)).read_text()
    return body if body.endswith("\n") else body+"\n"
si = re.sub(r"\\input\{(si_parts/tab_[a-z0-9_]+\.tex)\}\n?", inline, si)
(root/f"{NAME}_supplementary.tex").write_text(si)
print("main", len(main.splitlines()), "lines; SI", len(si.splitlines()), "lines")
