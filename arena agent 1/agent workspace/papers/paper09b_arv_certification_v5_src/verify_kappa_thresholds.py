#!/usr/bin/env python3
"""Exact source-row and arithmetic checks for Paper09b's conditional thresholds.

Reads the small locked CSV extracts in source_data/. It verifies the selected
NCAM and RAM SSB readings, all seventy xteNCAM adjacent-band pairs, DFO 2025
Table 1 reported-total-landings rows, the Schijns/DFO cross-file equalities,
the seven-year landings-range calculation, tonnes-to-kilotonnes conversion,
every printed kappa* entry, and both accounting identities. It checks
transcription consistency within these extracts; it does not independently
re-extract PDFs, estimate kappa, resolve timing, or validate assessment uncertainty.
"""
import csv
from decimal import Decimal, ROUND_HALF_UP, localcontext
from fractions import Fraction
from pathlib import Path

DATA = Path(__file__).resolve().parent / "source_data"


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def year_map(name: str, year_field: str = "year") -> dict[int, dict[str, str]]:
    rows = read_csv(name)
    result = {int(row[year_field]): row for row in rows}
    assert len(result) == len(rows), f"duplicate years in {name}"
    return result


def dec4(x: Fraction) -> str:
    with localcontext() as ctx:
        ctx.prec = 30
        value = Decimal(x.numerator) / Decimal(x.denominator)
        return str(value.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))


def exact_decimal(value: str) -> Fraction:
    return Fraction(value)


def kstar(b0: Fraction, b1: Fraction, catch_t: int) -> Fraction:
    c_rep_kt = Fraction(catch_t, 1_000)
    assert c_rep_kt * 1_000 == catch_t
    assert b0 > b1 > 0 and c_rep_kt > 0
    return (b0 - b1) / c_rep_kt


def verify_accounting_identity(b0: Fraction, b1: Fraction,
                               c_rep_kt: Fraction, threshold: Fraction) -> None:
    rho = b1 / b0
    ceiling = b0 / c_rep_kt
    assert 0 < threshold < ceiling
    for kappa in (threshold / 2, threshold, (threshold + ceiling) / 2):
        r = kappa * c_rep_kt / b0
        assert 0 <= r < 1
        g_after = rho + r
        g_before = rho / (1 - r)
        if kappa < threshold:
            assert g_after < 1 and g_before < 1
        elif kappa == threshold:
            assert g_after == 1 and g_before == 1
        else:
            assert g_after > 1 and g_before > 1


def main() -> None:
    ncam = year_map("ncam_2016_table_a2.csv")
    dfo = year_map("dfo_2025_table1_landings.csv")
    schijns = year_map("catch_schijns_2021.csv")
    ram_rows = read_csv("paperE1_calibration_data_v1_ram_timeseries.csv")
    ram = {
        int(row["year"]): row
        for row in ram_rows
        if row["stockid"] == "COD2J3KL" and row["year"] in {"2020", "2021"}
    }
    assert set(ram) == {2020, 2021}
    xte = year_map("xtencam_table17_ssb.csv")

    # Check all source rows used in the primary threshold table.
    for year in range(1983, 1996):
        assert year in ncam and year in dfo
    assert year_map("ncam_2016_table_a2.csv")[1983]["ssb_kt"] == "841.08"
    assert int(dfo[1983]["catch_t"]) == 232_345
    expected_ssb = {
        1985: "902.94", 1986: "836.00", 1989: "921.66", 1990: "861.92",
        1991: "734.51", 1992: "381.95", 1993: "101.05", 1994: "30.55",
        1995: "9.68",
    }
    for year, value in expected_ssb.items():
        assert ncam[year]["ssb_kt"] == value, (year, ncam[year]["ssb_kt"], value)

    # DFO 2025 Table 1 is the reported-total-landings series; keep it distinct
    # from SSB and from the separate catch-reconstruction file.
    expected_landings = {
        1985: 231_293, 1986: 266_713, 1989: 253_990, 1990: 219_452,
        1991: 172_012, 1992: 40_956, 1993: 11_392, 1994: 1_314,
        1995: 413, 2015: 4_436, 2020: 10_260, 2021: 10_977,
    }
    for year, value in expected_landings.items():
        assert int(dfo[year]["catch_t"]) == value, (year, dfo[year]["catch_t"], value)
        assert dfo[year]["source"].startswith("Regular et al. 2025 Table 1")
        assert Fraction(dfo[year]["catch_kt"]) == Fraction(value, 1_000)

    # The input-vintage database SSB extract is stored in tonnes; convert it
    # to kt exactly. The DFO 2025 reassessment is a different series.
    ram_ssb_kt = {}
    for year, expected_t in ((2020, 440_000), (2021, 411_000)):
        value_t = int(ram[year]["SSB"])
        assert value_t == expected_t, (year, value_t, expected_t)
        ram_ssb_kt[year] = Fraction(value_t, 1_000)

    # Check the full reassessment-band claim: all 70 adjacent pairs, not just
    # the four displayed transitions, and the displayed interval endpoints.
    assert len(xte) == 71 and set(xte) == set(range(1954, 2025))
    band_declines = [
        year for year in range(1954, 2024)
        if exact_decimal(xte[year + 1]["ssb_hi"]) < exact_decimal(xte[year]["ssb_lo"])
    ]
    assert band_declines == [1991, 1992, 1993, 1994], band_declines
    assert (exact_decimal(xte[1992]["ssb_lo"]) / exact_decimal(xte[1991]["ssb_hi"])
            == Fraction(265, 754))
    assert (exact_decimal(xte[1992]["ssb_hi"]) / exact_decimal(xte[1991]["ssb_lo"])
            == Fraction(468, 478))
    assert (exact_decimal(xte[1993]["ssb_lo"]) / exact_decimal(xte[1992]["ssb_hi"])
            == Fraction(54, 468))
    assert (exact_decimal(xte[1993]["ssb_hi"]) / exact_decimal(xte[1992]["ssb_lo"])
            == Fraction(115, 265))
    assert exact_decimal(xte[1993]["ssb_hi"]) == 115 and exact_decimal(xte[1993]["ssb_hi"]) < 276
    assert exact_decimal(xte[1992]["ssb_lo"]) <= 276 <= exact_decimal(xte[1992]["ssb_hi"])
    assert [exact_decimal(xte[y]["ssb_kt"]) for y in (1991, 1992, 1993)] == [600, 352, 79]
    implied_blim = [exact_decimal(r["ssb_kt"]) / exact_decimal(r["ssb_over_blim"])
                    for r in xte.values()]
    assert min(implied_blim) == 250 and max(implied_blim) < 289

    # Cross-file reported-series equalities cited in the paper.
    for year in (1992, 1993, 1994, 1995, 2015):
        assert int(dfo[year]["catch_t"]) == int(schijns[year]["catch_t"])

    # Verify the reported-landings scale comparison uses all seven 1983--1989
    # rows, not a four-row subset, and both 1994--1995 values.
    ref_values = [int(dfo[y]["catch_t"]) for y in range(1983, 1990)]
    later_values = [int(dfo[y]["catch_t"]) for y in (1994, 1995)]
    assert min(ref_values) == 231_293 and max(ref_values) == 268_677
    pair_ratios = [Fraction(a, b) for a in ref_values for b in later_values]
    assert min(pair_ratios) == Fraction(231_293, 1_314)
    assert max(pair_ratios) == Fraction(268_677, 413)

    steps = [
        ("1985->1986", 1985, 1986, "ncam"),
        ("1989->1990", 1989, 1990, "ncam"),
        ("1990->1991", 1990, 1991, "ncam"),
        ("1991->1992", 1991, 1992, "ncam"),
        ("1992->1993", 1992, 1993, "ncam"),
        ("1993->1994", 1993, 1994, "ncam"),
        ("1994->1995", 1994, 1995, "ncam"),
        ("2020->2021 RAM database series", 2020, 2021, "ram"),
    ]
    expected_rounded = {
        "1985->1986": ("0.2894", "0.2510"),
        "1989->1990": ("0.2352", "0.2722"),
        "1990->1991": ("0.5806", "0.7407"),
        "1991->1992": ("2.0496", "8.6083"),
        "1992->1993": ("6.8586", "24.6577"),
        "1993->1994": ("6.1886", "53.6530"),
        "1994->1995": ("15.8828", "50.5327"),
        "2020->2021 RAM database series": ("2.8265", "2.6419"),
    }

    print("step | SSB loss (kt) | C_t^rep (kt) | C_t+1^rep (kt) | kappa*_t | kappa*_(t+1)")
    results: dict[str, tuple[Fraction, Fraction]] = {}
    for label, t, tp1, vintage in steps:
        if vintage == "ncam":
            b0 = exact_decimal(ncam[t]["ssb_kt"])
            b1 = exact_decimal(ncam[tp1]["ssb_kt"])
        else:
            b0, b1 = ram_ssb_kt[t], ram_ssb_kt[tp1]
        c_t, c_tp1 = int(dfo[t]["catch_t"]), int(dfo[tp1]["catch_t"])
        loss = b0 - b1
        c_t_kt, c_tp1_kt = Fraction(c_t, 1_000), Fraction(c_tp1, 1_000)
        star_t, star_tp1 = kstar(b0, b1, c_t), kstar(b0, b1, c_tp1)
        assert star_t == loss / c_t_kt and star_tp1 == loss / c_tp1_kt
        verify_accounting_identity(b0, b1, c_t_kt, star_t)
        verify_accounting_identity(b0, b1, c_tp1_kt, star_tp1)
        actual = (dec4(star_t), dec4(star_tp1))
        assert actual == expected_rounded[label], (label, actual, expected_rounded[label])
        results[label] = star_t, star_tp1
        print(f"{label} | {loss} | {Decimal(c_t)/1000} | {Decimal(c_tp1)/1000} | "
              f"{actual[0]} | {actual[1]}")

    assert min(results["1991->1992"]) == Fraction(352_560, 172_012)
    assert min(results["1992->1993"]) == Fraction(280_900, 40_956)
    assert min(results["1993->1994"]) == Fraction(70_500, 11_392)
    assert min(results["1994->1995"]) == Fraction(20_870, 1_314)
    assert min(results["2020->2021 RAM database series"]) == Fraction(29_000, 10_977)
    print("PASS: source rows, 70 xteNCAM band pairs, landings range, exact conversion, kappa* thresholds, both accounting identities")


if __name__ == "__main__":
    main()
