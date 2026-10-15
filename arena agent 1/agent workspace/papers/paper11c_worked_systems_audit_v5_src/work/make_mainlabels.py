"""Generate si_parts/S0b_mainlabels.tex from the compiled main .aux (main-text numbers used by \\mref / \\meqref in the SI)."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
aux = (root / "paper11c_worked_systems_audit_v5.aux").read_text()
labels = re.findall(r"\\newlabel\{([^}@]*)\}\{\{([^}]*)\}", aux)
out = ["% generated from the main-text .aux file: main-text numbers used by \\mref / \\meqref"]
for lab, num in labels:
    out.append("\\expandafter\\def\\csname mainlab@%s\\endcsname{%s}" % (lab, num))
(root / "si_parts" / "S0b_mainlabels.tex").write_text("\n".join(out) + "\n")
print(len(labels), "labels")
