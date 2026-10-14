import re, pathlib
parts = ["si_parts/si_00_front.tex","si_parts/si_01_s1_s4.tex","si_parts/si_02_s5_s9.tex","si_parts/si_03_s11_s14.tex"]
s = "".join(pathlib.Path(p).read_text() for p in parts)
def sub(m):
    body = pathlib.Path(m.group(1)).read_text().rstrip("\n") + "\n"
    return body
s = re.sub(r"\\input\{(si_parts/gen/[^}]+)\}\n?", sub, s)
pathlib.Path("paperE1_cod_forecast_ladder_v69_SI.tex").write_text(s)
print("inputs left:", s.count("\\input{"))
