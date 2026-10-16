#!/usr/bin/env python3
"""Generate reproducible LaTeX tables from the v53 retained CSV outputs."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "si_parts"
OUT.mkdir(exist_ok=True)


def esc(s):
    s = str(s)
    repl = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
        "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(repl.get(c, c) for c in s)


def rows(path):
    with Path(path).open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_case_table():
    data = rows(ROOT / "src/p7_empirical/u5_case_table.csv")
    out = [
        r"\begin{landscape}", r"\scriptsize", r"\setlength{\tabcolsep}{3pt}",
        r"\begin{longtable}{@{}p{0.55cm}p{3.3cm}p{1.6cm}p{1.0cm}p{1.6cm}p{1.05cm}p{1.0cm}p{1.0cm}p{10.8cm}@{}}",
        r"\caption{Curated 32-system inventory and four-criterion dispositions. A dot denotes no assessment or not applicable; the binding-fail column records the criterion or scope exclusion that prevents full eligibility.}\label{tab:case-inventory}\\",
        r"\toprule ID & System & Domain & C1 & C2 lag & C3 & C4 & Binding fail & Evidence note \\",
        r"\midrule\endfirsthead",
        r"\toprule ID & System & Domain & C1 & C2 lag & C3 & C4 & Binding fail & Evidence note \\",
        r"\midrule\endhead", r"\bottomrule\endfoot",
    ]
    for r in data:
        # Give TeX line-break opportunities in slash-separated names, and use
        # human-readable domain labels rather than underscore identifiers.
        system = esc(r["system"]).replace("/", r"\allowbreak/")
        domain = esc(r["domain"].replace("_", " "))
        vals = [r["id"], system, domain, r["c1_responsive"], r["c2_dateable_lag"],
                r["c3_no_competing_driver"], r["c4_individual_data"], r["binding_fail"], r["evidence"]]
        out.append(" & ".join(v if i in (1, 2) else esc(v) for i, v in enumerate(vals)) + r" \\")
    out += [r"\end{longtable}", r"\end{landscape}"]
    (OUT / "s4_case_table.tex").write_text("\n".join(out) + "\n", encoding="utf-8")


def write_tr_table():
    data = rows(ROOT / "work/tr_ranked_test_results.csv")
    out = [
        r"\begin{landscape}", r"\scriptsize", r"\setlength{\tabcolsep}{4pt}",
        r"\begin{longtable}{@{}p{2.9cm}r r r r c r r c@{}}",
        r"\caption{Per-stock output of the recovered and re-executed \(\Tr\)-ranked test. Band power and AR(1) 95\% threshold are shown separately; the null-excess ratio is their quotient. The \(\Tr\) value is a group-coded proxy, not a stock-level verified field.}\label{tab:tr-stock}\\",
        r"\toprule Stock ID & \(n\) & \(\Tr\) (yr) & \(A\) & \(A_{95}\) & A flag & \(B\) & \(B_{95}\) & B flag \\",
        r"\midrule\endfirsthead",
        r"\toprule Stock ID & \(n\) & \(\Tr\) (yr) & \(A\) & \(A_{95}\) & A flag & \(B\) & \(B_{95}\) & B flag \\",
        r"\midrule\endhead", r"\bottomrule\endfoot",
    ]
    for r in data:
        sid = r"\texttt{" + esc(r["sid"]) + "}"
        tr = f'{float(r["Tr"]):.1f}'
        vals = [sid, r["n"], tr, f'{float(r["A"]):.4f}', f'{float(r["A95"]):.4f}',
                "yes" if r["sigA"].lower() == "true" else "no",
                f'{float(r["B"]):.4f}', f'{float(r["B95"]):.4f}',
                "yes" if r["sigB"].lower() == "true" else "no"]
        out.append(" & ".join(vals) + r" \\")
    out += [r"\end{longtable}", r"\end{landscape}"]
    (OUT / "s10_tr_stock_table.tex").write_text("\n".join(out) + "\n", encoding="utf-8")


def write_ota5_table():
    data = rows(ROOT / "src/p7_empirical/recovered/sens_table.csv")
    factors = ["0.9", "0.95", "1.05", "1.1"]
    names = {
        "r": r"\(r\)", "K": r"\(K\)", "q": r"\(q\)",
        "Emax": r"\(E_{\max}\)", "eta": r"\(\eta\)",
        "d0": r"\(\delta_0\)", "Zref": r"\(Z_{\rm ref}\)",
        "Dref": r"\(\Delta_{\rm ref}\)", "taum": r"\(\tau_m\)",
        "delta": r"\(\delta\)",
    }
    lookup = {(r["param"], r["factor"]): r["Trc_exact"] for r in data}
    out = [
        r"\begin{table}[htbp]", r"\centering\small",
        r"\caption{Archived one-at-a-time \(\pm5\%\) and \(\pm10\%\) sensitivity battery. Entries are first exponential-update mobilising crossings in years; ``None'' means no crossing on the archived interval scan.}",
        r"\label{tab:ota5}", r"\begin{tabular}{@{}lrrrr@{}}", r"\toprule",
        r"Parameter & \(-10\%\) & \(-5\%\) & \(+5\%\) & \(+10\%\) \\",
        r"\midrule",
    ]
    for param, label in names.items():
        vals = [label]
        for factor in factors:
            value = lookup.get((param, factor), "none")
            vals.append("None" if value.lower() == "none" else f"{float(value):.4f}")
        out.append(" & ".join(vals) + r" \\")
    out += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    (OUT / "s11_ota5_table.tex").write_text("\n".join(out) + "\n", encoding="utf-8")


def write_power_table():
    data = rows(ROOT / "work/power_table_white_noise.csv")
    out = [
        r"\begin{longtable}{@{}l r r c r r@{}}",
        r"\caption{Archived white-noise injected-signal power table (17 cells). Each cell has 50 trials; power is detections divided by trials.}\label{tab:white-power}\\",
        r"\toprule Class & \(H\) & Horizon \(T\) & \(\sigma\) & Detections / 50 & Power \\",
        r"\midrule\endfirsthead",
        r"\toprule Class & \(H\) & Horizon \(T\) & \(\sigma\) & Detections / 50 & Power \\",
        r"\midrule\endhead", r"\bottomrule\endfoot",
    ]
    for r in data:
        out.append(" & ".join([esc(r["label"]), r["H"], r["T"], r["sigma"],
                                f'{r["detections"]} / {r["trials"]}', f'{float(r["power"]):.2f}']) + r" \\")
    out.append(r"\end{longtable}")
    (OUT / "s13_power_table.tex").write_text("\n".join(out) + "\n", encoding="utf-8")


def write_mse_table():
    data = rows(ROOT / "src/results/p5_comparator_mse_mc.csv")
    out = [
        r"\begin{landscape}", r"\scriptsize", r"\setlength{\tabcolsep}{5pt}",
        r"\begin{longtable}{@{}p{3.3cm}r r r r r r@{}}",
        r"\caption{Archived 10-seed nonlinear comparator summary. The retained CSV does not contain an \(\epsilon\) or per-seed field; the earlier manuscript describes this summary as the \(30\%\) assessment-error run. Values are preserved as archived and are not presented as a new re-execution.}\label{tab:comparator-mc}\\",
        r"\toprule Controller & \(T_r\) & Seeds & Mean depletion & Mean min \(N/K\) & Mean RMSD \(N/K\) & Diverged seeds \\",
        r"\midrule\endfirsthead",
        r"\toprule Controller & \(T_r\) & Seeds & Mean depletion & Mean min \(N/K\) & Mean RMSD \(N/K\) & Diverged seeds \\",
        r"\midrule\endhead", r"\bottomrule\endfoot",
    ]
    for r in data:
        vals = [esc(r["controller"]), r["T_r"], r["n_seeds"],
                esc(r["mean_depletion"] or "--"), esc(r["mean_min_N"] or "--"),
                esc(r["mean_rmsd_N"] or "--"), r["diverged_seeds"]]
        out.append(" & ".join(vals) + r" \\")
    out += [r"\end{longtable}", r"\end{landscape}"]
    (OUT / "s11_comparator_table.tex").write_text("\n".join(out) + "\n", encoding="utf-8")


def write_f_table():
    data = rows(ROOT / "work/fplacement_table_v53.csv")
    out = [
        r"\begin{landscape}", r"\scriptsize", r"\setlength{\tabcolsep}{5pt}",
        r"\begin{longtable}{@{}p{3.2cm}r r r r r l@{}}",
        r"\caption{Screen-cohort fishing-mortality series and placement categories. Values are retained as the local v53 output; a dash indicates no usable F series.}\label{tab:fplacement}\\",
        r"\toprule Stock ID & SSB \(n\) & F \(n\) & Mean F & Median F & Max F & Placement \\",
        r"\midrule\endfirsthead",
        r"\toprule Stock ID & SSB \(n\) & F \(n\) & Mean F & Median F & Max F & Placement \\",
        r"\midrule\endhead", r"\bottomrule\endfoot",
    ]
    for r in data:
        sid = r"\texttt{" + esc(r["stockid"]) + "}"
        out.append(" & ".join([sid, r["n_SSB"], r["n_F"], esc(r["F_mean"]), esc(r["F_med"]),
                                esc(r["F_max"]), esc(r["placement"])]) + r" \\")
    out += [r"\end{longtable}", r"\end{landscape}"]
    (OUT / "s12_fplacement_table.tex").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_case_table()
    write_tr_table()
    write_ota5_table()
    write_power_table()
    write_mse_table()
    write_f_table()
    print("generated case, T_r-stock, archived OAT, power, comparator, and F-placement tables in si_parts/")
