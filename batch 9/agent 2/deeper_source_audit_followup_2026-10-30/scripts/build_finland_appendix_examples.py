#!/usr/bin/env python3
"""Write the illustrative Luke Appendix A matrices exactly as printed.

Diagonal entries remain U(%) or SD as labelled by the report; off-diagonal
entries are correlations. No conversion to a covariance matrix is performed.
"""
from __future__ import annotations

import csv
import pathlib
import sys

SOURCE = "Luke 6/2026; Appendix A text-identical in corrected Luke 12/2026"


def emit_table(writer, table, printed_page, scope, labels, rows, diagonal_type):
    assert len(labels) == len(rows)
    for i, (label, values) in enumerate(zip(labels, rows)):
        assert len(values) == i + 1, (table, label, len(values), i + 1)
        for j, value in enumerate(values):
            writer.writerow({
                "source_report": SOURCE,
                "source_pdf_page": printed_page + 1,
                "source_printed_page": printed_page,
                "table": table,
                "scope": scope,
                "row": label,
                "column": labels[j],
                "value": value,
                "value_type": diagonal_type if i == j else "correlation",
            })


def main(destination: pathlib.Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as handle:
        fields = ["source_report", "source_pdf_page", "source_printed_page", "table", "scope", "row", "column", "value", "value_type"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()

        a2_labels = [
            "runko|vakiotermi", "runko|d", "runko|log(d)", "runko|log(h)", "runko|I_org",
            "oksat|vakiotermi", "oksat|log(d)", "oksat|sqrt(h)",
            "lehvasto|vakiotermi", "lehvasto|d/(d+5)", "lehvasto|h/(h+1)",
        ]
        a2_rows = [
            ["7.7"],
            ["0.71", "46.1"],
            ["-0.58", "-0.82", "25.6"],
            ["-0.30", "0.08", "-0.55", "32.9"],
            ["-0.08", "0.05", "-0.06", "0.02", "22.3"],
            ["0.02", "0.01", "-0.02", "0.01", "0.01", "3.3"],
            ["-0.01", "-0.01", "0.04", "-0.05", "0.00", "-0.30", "2.9"],
            ["0.00", "0.00", "-0.03", "0.04", "-0.01", "-0.28", "-0.81", "14.2"],
            ["-0.01", "0.01", "0.00", "0.00", "0.01", "0.34", "0.31", "-0.52", "37.3"],
            ["-0.02", "0.00", "0.04", "-0.04", "0.00", "-0.22", "0.62", "-0.48", "0.65", "3.9"],
            ["0.01", "-0.01", "-0.01", "0.01", "-0.01", "-0.19", "-0.42", "0.55", "-0.97", "-0.80", "22.7"],
        ]
        emit_table(writer, "A2", 63, "Example only: pine model 2b, above-ground parameter uncertainty/correlation", a2_labels, a2_rows, "U_percent_as_printed")

        component_labels = ["runko", "oksat", "lehvasto", "kanto", "juuret"]
        a3_rows = [
            ["0.036"],
            ["-0.101", "0.204"],
            ["-0.189", "0.808", "0.345"],
            ["0.941", "0.159", "-0.105", "0.257"],
            ["-0.555", "-0.477", "-0.688", "-0.516", "0.044"],
        ]
        emit_table(writer, "A3", 63, "Example only: pine model 2b, stand-level random components", component_labels, a3_rows, "SD_as_printed")

        a4_rows = [
            ["0.032"],
            ["0.154", "0.334"],
            ["0.159", "0.702", "0.349"],
            ["0.267", "0.440", "0.294", "0.260"],
            ["0.354", "0.331", "0.183", "-0.019", "0.307"],
        ]
        emit_table(writer, "A4", 63, "Example only: pine model 2b, tree-level residuals", component_labels, a4_rows, "SD_as_printed")

        a5_labels = [
            "BCEF|manty|runko", "BCEF|manty|oksat", "BCEF|manty|lehvasto",
            "BCEF|kuusi|runko", "BCEF|kuusi|oksat", "BCEF|kuusi|lehvasto",
            "BCEF|lehtipuut|runko", "BCEF|lehtipuut|oksat", "BCEF|lehtipuut|lehvasto",
            "runkotilavuus|manty", "runkotilavuus|kuusi", "runkotilavuus|lehtipuut",
        ]
        a5_rows = [
            ["0.33"],
            ["-0.02", "1.37"],
            ["-0.20", "0.64", "1.89"],
            ["-0.09", "0.01", "0.06", "0.51"],
            ["-0.04", "0.08", "0.09", "0.30", "2.05"],
            ["-0.05", "0.08", "0.11", "0.32", "0.78", "2.67"],
            ["0.00", "0.01", "0.00", "-0.02", "0.01", "0.00", "0.86"],
            ["-0.03", "0.04", "0.01", "0.03", "0.06", "0.06", "0.17", "1.83"],
            ["-0.03", "0.03", "0.06", "0.07", "0.05", "0.06", "-0.19", "0.04", "3.22"],
            ["0.09", "-0.18", "-0.25", "0.01", "-0.03", "-0.02", "0.00", "-0.01", "0.00", "3.10"],
            ["0.10", "-0.13", "-0.18", "-0.20", "-0.41", "-0.44", "0.03", "-0.07", "-0.11", "-0.31", "4.28"],
            ["0.09", "-0.02", "-0.09", "-0.01", "-0.01", "-0.06", "0.03", "-0.05", "-0.24", "-0.24", "0.24", "3.86"],
        ]
        emit_table(writer, "A5", 64, "Example only: one NFI13 sampling region, above-ground BCEF and stem-volume sampling uncertainty/correlation", a5_labels, a5_rows, "U_percent_as_printed")


if __name__ == "__main__":
    target = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parents[1] / "evidence" / "finland_luke_appendix_A_examples_as_printed.csv"
    main(target)
