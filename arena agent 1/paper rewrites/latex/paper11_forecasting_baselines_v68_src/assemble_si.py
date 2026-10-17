import re, pathlib
parts = sorted(pathlib.Path("si_parts").glob("si_0*.tex"))
s = "".join(p.read_text() for p in parts)
s = re.sub(r"\\input\{(si_parts/gen/[^}]+)\}\n?", lambda m: pathlib.Path(m.group(1)).read_text().rstrip("\n") + "\n", s)
s = s.replace("\\centering\\small\n", "\\centering\\footnotesize\\setlength{\\tabcolsep}{3.5pt}\n")
for lab in ["tab:si_blocks","tab:si_rollingB","tab:si_horizon"]:
    i = s.index("\\label{%s}" % lab); j = s.index("\\begin{tabular}", i); k = s.index("\\end{tabular}", j) + len("\\end{tabular}")
    s = s[:j] + "\\resizebox{\\textwidth}{!}{%\n" + s[j:k] + "}\n" + s[k:]
pathlib.Path("paper11_forecasting_baselines_v68_supplementary.tex").write_text(s)
print([p.name for p in parts], "inputs left:", s.count("\\input{"), "lines:", s.count("\n"), "footnotesize tables:", s.count("\\centering\\footnotesize"))
