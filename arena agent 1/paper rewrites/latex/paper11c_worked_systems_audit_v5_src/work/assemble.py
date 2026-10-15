"""Assemble the main text and the supplement from their parts; inline generated tables."""
import re, glob, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
NAME = "paper11c_worked_systems_audit_v5"


def cat(files):
    out = ""
    for f in files:
        t = open(f).read()
        out += t if t.endswith("\n") else t + "\n"
    return out


def inline(m):
    p = root / m.group(1)
    if not p.exists():
        return "%% (table " + m.group(1) + " not generated yet)\n"
    body = p.read_text()
    return body if body.endswith("\n") else body + "\n"


PAT = r"\\input\{(si_parts/tab_[a-z0-9_]+\.tex)\}\n?"
main_parts = sorted(glob.glob(str(root / "parts" / "*.tex")))
main = cat(main_parts)
main = re.sub(PAT, inline, main)
(root / f"{NAME}.tex").write_text(main)


def si_key(p):
    m = re.match(r"S(\d+)", pathlib.Path(p).name)
    return int(m.group(1)) if m else -1


si_files = [root / "si_parts" / "S0_front.tex", root / "si_parts" / "S0b_mainlabels.tex"]
si_files += sorted([pathlib.Path(p) for p in glob.glob(str(root / "si_parts" / "S[0-9]*_*.tex"))
                    if not pathlib.Path(p).name.startswith("S0")], key=si_key)
si_files = [p for p in si_files if p.exists()]
si = cat([str(p) for p in si_files])
si = re.sub(PAT, inline, si)
(root / f"{NAME}_supplementary.tex").write_text(si)
print("main", len(main.splitlines()), "lines; SI", len(si.splitlines()), "lines;", [p.name for p in si_files])
