"""Render SI drawdown and recovery tables from the canonical model CSV.

Run after drawdown_depth.py. The source tables are regenerated from the same
si_drawdown_depth.csv used for Figure 1(c), preventing hand-maintained numerical
drift. Units: areas in ha, population in cap, B/E in gha, time in years.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "si_drawdown_depth.csv"
TABLE_DIR = ROOT / "parts"
AC0S = (0.40, 0.70, 1.00, 1.18)
DRAW_P0S = (1.0, 1.5, 2.0, 2.5, 2.8, 3.0, 3.5, 4.0)
RECOVERY_P0S = (1.5, 2.0, 2.5, 3.0, 3.5, 4.0)
E_PER_CAP = 0.55
AC_REF = 1.0


def read_rows() -> dict[tuple[float, float], dict[str, str]]:
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    expected = len(AC0S) * 31
    if len(rows) != expected:
        raise AssertionError(f"expected {expected} drawdown rows, found {len(rows)}")
    keyed = {(float(r["A_c0_ha"]), float(r["P0_cap"])): r for r in rows}
    if len(keyed) != len(rows):
        raise AssertionError("duplicate initial-state row in drawdown CSV")
    for ac0 in AC0S:
        for p0 in [round(1.0 + 0.1 * i, 2) for i in range(31)]:
            if (ac0, p0) not in keyed:
                raise AssertionError(f"missing CSV row A_c0={ac0}, P0={p0}")
    return keyed


def render_drawdown(rows: dict[tuple[float, float], dict[str, str]]) -> str:
    rowbreak = chr(92) * 2
    out = [
        r"\begin{tabular}{lrrrrrrrr}",
        r"\toprule",
        r"$A_{c0}$ $\backslash$ $P_0$ & 1.0 & 1.5 & 2.0 & 2.5 & 2.8 & 3.0 & 3.5 & 4.0 " + rowbreak,
        r"\midrule",
    ]
    labels = {0.40: "0.4", 0.70: "0.7", 1.00: "1.0", 1.18: "1.18"}
    for ac0 in AC0S:
        vals = [float(rows[(ac0, p0)]["minAc_ha_chi0.10"]) for p0 in DRAW_P0S]
        out.append(f"${labels[ac0]}$ & " + " & ".join(f"{x:.3f}" for x in vals) + " " + rowbreak)
    out += [r"\bottomrule", r"\end{tabular}"]
    return "\n".join(out) + "\n"


def render_recovery(rows: dict[tuple[float, float], dict[str, str]]) -> str:
    rowbreak = chr(92) * 2
    out = [
        r"\begin{tabular}{l r r r r r r}",
        r"\toprule",
        r"$P_0$ & $E_0$ & $\min_tA_c$ & $t(\min)$ (yr) & $A_c(T)$, $\chi_r=0$ & $A_c(T)$, $\chi_r=0.10$ & $\mathcal R_c(T)$, $\chi_r=0.10$ " + rowbreak,
        r"\midrule",
    ]
    for p0 in RECOVERY_P0S:
        row = rows[(AC_REF, p0)]
        amin = float(row["minAc_ha_chi0.10"])
        amin_no_restore = float(row["minAc_ha_chi0.00"])
        if abs(amin - amin_no_restore) > 1e-8:
            raise AssertionError(f"recovery minimum differs across gates at P0={p0}")
        ac_none = float(row["finalAc_ha_chi0.00"])
        ac_restored = float(row["finalAc_ha_chi0.10"])
        tmin = float(row["tmin_yr_chi0.10"])
        recovery = (ac_restored - amin) / (AC_REF - amin)
        e0 = E_PER_CAP * p0
        out.append(
            f"${p0:.1f}$ & ${e0:.3f}$ & ${amin:.3f}$ & ${tmin:.1f}$ & "
            f"${ac_none:.3f}$ & ${ac_restored:.3f}$ & ${recovery:.2f}$ " + rowbreak
        )
    out += [r"\bottomrule", r"\end{tabular}"]
    return "\n".join(out) + "\n"

def main() -> None:
    rows = read_rows()
    drawdown = render_drawdown(rows)
    recovery = render_recovery(rows)
    (TABLE_DIR / "si_tab_drawdown.tex").write_text(drawdown, encoding="utf-8")
    (TABLE_DIR / "si_tab_recovery.tex").write_text(recovery, encoding="utf-8")
    print(f"regenerated {TABLE_DIR / 'si_tab_drawdown.tex'}")
    print(f"regenerated {TABLE_DIR / 'si_tab_recovery.tex'}")


if __name__ == "__main__":
    main()
