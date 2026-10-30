#!/usr/bin/env python3
"""Extract the public Cameroon and Australia physical modules without mixing estimands.

Inputs remain in the non-durable F16 source cache. Outputs are small, source-pinned
CSV/JSON derivatives; provider PDFs and the CRT archive are not redistributed.
"""
from __future__ import annotations
import csv
import hashlib
import json
import re
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

import pymupdf
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT.parent / ".cache/F16_sources"
OUT = ROOT / "data"
META = ROOT / "metadata"
CMR_PDF = CACHE / "cameroon/cmr_nrf_2026.pdf"
AUS_NIR1 = CACHE / "australia/nir2023_volume1.pdf"
AUS_NIR2 = CACHE / "australia/nir2023_volume2.pdf"
ABARES_TXT = CACHE / "australia/abares_area_change_2023_extracted.txt"
ABARES_ATTR = CACHE / "australia/aus_for23_attributes.csv"
ABARES_META = CACHE / "australia/forests_2023_metadata.pdf"
ABARES_LUT = CACHE / "australia/forests_2023_lookup_tables.pdf"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_csv(name: str, rows: list[dict], fields: list[str]) -> None:
    with (OUT / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def decimal(value: str) -> Decimal:
    value = value.strip().replace(" ", "")
    if "," in value and "." not in value:
        value = value.replace(",", ".")
    return Decimal(value)


def cameroon_area() -> list[dict]:
    """Read Table 9 by word coordinates, preserving reported total and class rows."""
    doc = pymupdf.open(CMR_PDF)
    words = doc[30].get_text("words")  # printed/PDF page 31
    doc.close()
    columns = [
        ("dense_humid_forest_ha", 135, 225),
        ("inundated_forest_ha", 225, 300),
        ("planted_forest_ha", 300, 365),
        ("dry_forest_ha", 365, 435),
        ("mangrove_ha", 435, 485),
        ("reported_total_forest_ha", 485, 555),
    ]
    rows = []
    for year_word in words:
        if not re.fullmatch(r"20(?:0\d|1\d|20)", year_word[4]):
            continue
        x0, y0 = year_word[0], year_word[1]
        if not (80 < x0 < 115 and 220 < y0 < 690):
            continue
        line = [w for w in words if abs(w[1] - y0) < 2.0]
        row = {"year": int(year_word[4]), "source_pdf_page": 31}
        for name, left, right in columns:
            tokens = sorted((w for w in line if left <= w[0] < right), key=lambda w: w[0])
            require(tokens, f"Cameroon Table 9 missing {year_word[4]} {name}")
            row[name] = int("".join(w[4] for w in tokens))
        row["class_sum_ha"] = sum(row[name] for name, _, _ in columns[:5])
        row["class_sum_minus_reported_total_ha"] = row["class_sum_ha"] - row["reported_total_forest_ha"]
        rows.append(row)
    rows.sort(key=lambda r: r["year"])
    require([r["year"] for r in rows] == list(range(2000, 2021)), "Cameroon Table 9 annual coverage")
    fields = ["year", "source_pdf_page"] + [x[0] for x in columns] + ["class_sum_ha", "class_sum_minus_reported_total_ha"]
    write_csv("CMR_reported_forest_area_2000_2020_F16.csv", rows, fields)
    return rows


# Table 37 presents Total REDD+ at whole-tCO2e precision. These source-rendered
# integers provide an independent rounding cross-check of Table 31's decimals.
CMR_TABLE37 = dict(zip(range(2000, 2021), [
    -131183355, -132726023, -130218725, -130931384, -129233041,
    -130140442, -127982216, -125967784, -125815617, -127541568,
    -123070524, -124868357, -122914260, -122370200, -120994437,
    -113383116, -107338060, -114091849, -111824487, -113284607,
    -109599895,
]))


def cameroon_flux() -> list[dict]:
    """Read annual net forest CO2e flux and MC relative uncertainty from Table 31."""
    doc = pymupdf.open(CMR_PDF)
    rows = []
    for page_number in (86, 87):
        words = doc[page_number - 1].get_text("words")
        for year_word in words:
            if not re.fullmatch(r"20(?:0\d|1\d|20)", year_word[4]):
                continue
            x0, y0 = year_word[0], year_word[1]
            if not (80 < x0 < 115):
                continue
            line = [w for w in words if abs(w[1] - y0) < 2.0]
            net_tokens = sorted((w for w in line if 385 <= w[0] < 465), key=lambda w: w[0])
            unc_tokens = sorted((w for w in line if 475 <= w[0] < 530), key=lambda w: w[0])
            if not net_tokens or not unc_tokens:
                continue
            year = int(year_word[4])
            net = decimal("".join(w[4] for w in net_tokens))
            uncertainty = decimal("".join(w[4] for w in unc_tokens).replace("%", ""))
            rounded = CMR_TABLE37[year]
            require(int(net.to_integral_value()) == rounded, f"Cameroon Table 31/37 rounding mismatch {year}")
            rows.append({
                "year": year,
                "source_pdf_page_table31": page_number,
                "source_pdf_page_table37": 140 if year <= 2010 else 141,
                "reported_net_forest_flux_tCO2e_per_year": str(net),
                "monte_carlo_relative_uncertainty_percent": str(uncertainty),
                "table37_rounded_net_flux_tCO2e_per_year": rounded,
                "table31_minus_table37_rounded_tCO2e": str(net - Decimal(rounded)),
            })
    doc.close()
    rows.sort(key=lambda r: r["year"])
    require([r["year"] for r in rows] == list(range(2000, 2021)), "Cameroon Table 31 annual coverage")
    write_csv("CMR_reported_net_forest_flux_2000_2020_F16.csv", rows, list(rows[0]))
    return rows


def nir_area() -> list[dict]:
    text = PdfReader(AUS_NIR1).pages[315].extract_text() or ""  # PDF page 316
    rows = []
    for line in text.splitlines():
        if not re.match(r"^(?:19|20)\d{2}–\d{2}\s", line):
            continue
        parts = line.split()
        require(len(parts) == 7, f"Unexpected NIR Table 6.2.2 row: {line}")
        values = [int(x.replace(",", "")) for x in parts[1:]]
        rows.append({
            "reporting_period": parts[0],
            "year_ending_june": int(parts[0][:4]) + 1,
            "forest_land_kha": values[0],
            "source_pdf_page": 316,
            "activity_status": "held_constant_at_2021_22_levels" if parts[0] == "2022–23" else "reported_annual_land_use_total",
            "_all_six": values,
        })
    require(len(rows) == 35 and rows[0]["reporting_period"] == "1988–89" and rows[-1]["reporting_period"] == "2022–23", "NIR Table 6.2.2 coverage")
    require(rows[-1]["_all_six"] == rows[-2]["_all_six"], "Expected repeated final NIR land-total row not found")
    for row in rows:
        row.pop("_all_six")
    write_csv("AUS_NIR2023_forest_land_1989_2023_F16.csv", rows, list(rows[0]))
    return rows


def _nir_flow_lines(reader: PdfReader, pages: list[int], start: int | None = None, stop: str | None = None) -> list[str]:
    lines = []
    for offset, page_index in enumerate(pages):
        text = reader.pages[page_index].extract_text() or ""
        if start is not None and offset == 0:
            marker = "Table A5.6.12.1b"
            require(marker in text, "NIR Table A5.6.12.1b marker missing")
            text = text[text.index(marker):]
        if stop and stop in text:
            text = text[:text.index(stop)]
        lines.extend(text.splitlines())
    return lines


def nir_flows() -> list[dict]:
    reader = PdfReader(AUS_NIR2)
    # PDF 352–353: primary conversion/re-clearing; PDF 353–354: regrowth/net clearing.
    a_lines = _nir_flow_lines(reader, [351, 352], stop="Table A5.6.12.1b")
    b_lines = _nir_flow_lines(reader, [352, 353], start=1)
    def parse(lines: list[str], names: tuple[str, str]) -> dict[str, dict]:
        result = {}
        for line in lines:
            if not re.match(r"^(?:19|20)\d{2}–\d{2}\s", line):
                continue
            parts = line.split()
            require(len(parts) == 19, f"Unexpected NIR annex flow row: {line}")
            result[parts[0]] = {names[0]: Decimal(parts[1]), names[1]: Decimal(parts[2])}
        require(len(result) == 34, f"NIR annex annual flow coverage {len(result)}")
        return result
    primary = parse(a_lines, ("primary_forest_conversion_kha", "secondary_forest_reclearing_kha"))
    regrowth = parse(b_lines, ("identified_regrowth_kha", "net_forest_clearing_kha"))
    rows = []
    for period in primary:
        row = {
            "reporting_period": period,
            "year_ending_june": int(period[:4]) + 1,
            **primary[period],
            **regrowth[period],
            "source_pdf_pages": "352–354",
            "activity_status": "held_constant_at_2021_22_levels" if period == "2022–23" else "reported_annual_activity",
        }
        residual = row["primary_forest_conversion_kha"] + row["secondary_forest_reclearing_kha"] - row["identified_regrowth_kha"] - row["net_forest_clearing_kha"]
        require(abs(residual) <= Decimal("0.1000001"), f"NIR clearing identity residual {period}: {residual}")
        row["clearing_identity_residual_kha"] = residual
        for key in ("primary_forest_conversion_kha", "secondary_forest_reclearing_kha", "identified_regrowth_kha", "net_forest_clearing_kha", "clearing_identity_residual_kha"):
            row[key] = str(row[key])
        rows.append(row)
    flow_keys = ("primary_forest_conversion_kha", "secondary_forest_reclearing_kha", "identified_regrowth_kha", "net_forest_clearing_kha")
    require(all(rows[-1][k] == rows[-2][k] for k in flow_keys), "Expected repeated final NIR flow row not found")
    write_csv("AUS_NIR2023_clearing_regrowth_1990_2023_F16.csv", rows, list(rows[0]))
    return rows


def abares_series() -> tuple[list[dict], list[dict]]:
    text = ABARES_TXT.read_text(encoding="utf-8")
    first = text[text.index("**Figure 1.1a.iv-1:"):text.index("Source: ABARES Forests of Australia")]
    area = []
    for line in first.splitlines():
        match = re.match(r"^(\d{4})\s+(\d+\.\d{2})\s*(-?\d+\.\d{2})\s*$", line)
        if match:
            area.append({
                "year_ending_june": int(match[1]),
                "abares_adjusted_forest_area_Mha": match[2],
                "reported_difference_from_2016_Mha": match[3],
                "source_sheet": "Figure 1.1a.iv-1",
            })
    require([r["year_ending_june"] for r in area] == list(range(1989, 2022)), "ABARES adjusted annual area coverage")
    base = Decimal(next(r["abares_adjusted_forest_area_Mha"] for r in area if r["year_ending_june"] == 2016))
    for row in area:
        residual = Decimal(row["reported_difference_from_2016_Mha"]) - (Decimal(row["abares_adjusted_forest_area_Mha"]) - base)
        require(abs(residual) <= Decimal("0.01"), "ABARES difference-from-2016 rounding exceeds one displayed unit")
        row["difference_column_minus_displayed_area_difference_Mha"] = str(residual)
    write_csv("AUS_ABARES_adjusted_forest_area_1989_2021_F16.csv", area, list(area[0]))

    second = text[text.index("**Figure 1.1a.iv-2:"):text.index("Gross loss is sum")]
    transitions = []
    for line in second.splitlines():
        match = re.match(r"^(\d{4})\s+(\d+\.\d{2})(?:\s*(-?\d+)\s+(-?\d+)\s*(-?\d+))?\s*$", line)
        if match:
            row = {
                "year_ending_june": int(match[1]),
                "nir2021_forest_land_stock_Mha": match[2],
                "gross_loss_kha": match[3] or "",
                "gross_gain_kha": match[4] or "",
                "net_change_kha": match[5] or "",
                "source_sheet": "Figure 1.1a.iv-2",
            }
            if match[3] is not None:
                residual = int(match[3]) + int(match[4]) - int(match[5])
                require(abs(residual) <= 1, f"ABARES/NIR2021 flow rounding exceeds 1 kha {match[1]}")
                row["gross_loss_plus_gain_minus_reported_net_kha"] = residual
            else:
                row["gross_loss_plus_gain_minus_reported_net_kha"] = ""
            transitions.append(row)
    require([r["year_ending_june"] for r in transitions] == list(range(1989, 2022)), "ABARES/NIR2021 transition coverage")
    write_csv("AUS_NIR2021_stock_gains_losses_1989_2021_F16.csv", transitions, list(transitions[0]))
    return area, transitions


def abares_snapshot() -> tuple[list[dict], list[dict], dict]:
    with ABARES_ATTR.open(newline="", encoding="utf-8-sig") as handle:
        raw = list(csv.DictReader(handle, skipinitialspace=True))
    require(len(raw) == 687, "Forests of Australia attribute row count")
    for row in raw:
        row["COUNT"] = int(row["COUNT"])
        row["FOREST"] = int(row["FOREST"])
    categories = defaultdict(int)
    states = defaultdict(lambda: {"forest_ha": 0, "nonforest_ha": 0})
    for row in raw:
        categories[row["FOR_CATEGORY"].strip()] += row["COUNT"]
        key = "forest_ha" if row["FOREST"] == 1 else "nonforest_ha"
        states[row["STATE"].strip() or "Unallocated"][key] += row["COUNT"]
    total_forest = sum(v for k, v in categories.items() if k != "Non-forest")
    total_all = sum(categories.values())
    require(total_forest == 133564800 and total_all == 768914778, "Forests of Australia national totals")
    cat_rows = [{"forest_category": k, "area_ha": categories[k], "share_of_mapped_Australia_percent": str(Decimal(categories[k] * 100) / Decimal(total_all))} for k in sorted(categories)]
    state_rows = []
    for state in sorted(states):
        values = states[state]
        total = values["forest_ha"] + values["nonforest_ha"]
        state_rows.append({"state_or_territory": state, **values, "total_ha": total, "forest_share_percent": str(Decimal(values["forest_ha"] * 100) / Decimal(total))})
    write_csv("AUS_Forests2023_category_areas_F16.csv", cat_rows, list(cat_rows[0]))
    write_csv("AUS_Forests2023_state_areas_F16.csv", state_rows, list(state_rows[0]))
    # Check the exact metadata statements used to type this as a 2021-currency, 1-ha-cell snapshot.
    metadata_text = "\n".join(p.extract_text() or "" for p in PdfReader(ABARES_META).pages)
    lut_text = "\n".join(p.extract_text() or "" for p in PdfReader(ABARES_LUT).pages)
    require("30 June 2021" in metadata_text and "100 x 100 metre" in metadata_text, "ABARES snapshot currency/cell metadata")
    require("COUNT value is equivalent to area in hectares" in lut_text, "ABARES COUNT unit definition")
    return cat_rows, state_rows, {"forest_ha": total_forest, "nonforest_ha": categories["Non-forest"], "total_ha": total_all}


def make_summary(area: list[dict], flux: list[dict], nir: list[dict], flows: list[dict], abares: list[dict], transitions: list[dict], snapshot: dict) -> dict:
    def at(rows, key, value): return next(r for r in rows if r[key] == value)
    def pct(new, old): return (Decimal(new) - Decimal(old)) / Decimal(old) * 100
    c15, c20 = at(area, "year", 2015), at(area, "year", 2020)
    f15, f20 = at(flux, "year", 2015), at(flux, "year", 2020)
    n15, n21, n22, n23 = (at(nir, "year_ending_june", y) for y in (2015, 2021, 2022, 2023))
    a15, a21 = at(abares, "year_ending_june", 2015), at(abares, "year_ending_june", 2021)
    t15, t21 = at(transitions, "year_ending_june", 2015), at(transitions, "year_ending_june", 2021)
    flow15, flow22, flow23 = (at(flows, "year_ending_june", y) for y in (2015, 2022, 2023))
    cmr_delta = c20["reported_total_forest_ha"] - c15["reported_total_forest_ha"]
    cmr_flux_delta = Decimal(f20["reported_net_forest_flux_tCO2e_per_year"]) - Decimal(f15["reported_net_forest_flux_tCO2e_per_year"])
    nir_delta_15_21 = n21["forest_land_kha"] - n15["forest_land_kha"]
    nir_delta_15_22 = n22["forest_land_kha"] - n15["forest_land_kha"]
    return {
        "rounding_audit": {
            "Cameroon_class_sum_minus_reported_total_ha": {
                "years_with_plus_one_ha": [r["year"] for r in area if r["class_sum_minus_reported_total_ha"] == 1],
                "other_years": "0 ha; reported totals are never altered to force class closure",
            },
            "Australia_NIR2023_clearing_identity_residual_kha": {
                "minimum": str(min(Decimal(r["clearing_identity_residual_kha"]) for r in flows)),
                "maximum": str(max(Decimal(r["clearing_identity_residual_kha"]) for r in flows)),
                "note": "Displayed inputs and outputs are independently rounded to 0.1 kha.",
            },
            "ABARES_adjusted_difference_column": {
                "years_with_plus_0_01_Mha_residual": [r["year_ending_june"] for r in abares if Decimal(r["difference_column_minus_displayed_area_difference_Mha"]) != 0],
                "note": "Difference-from-2016 is independently rounded; displayed areas are not changed.",
            },
            "NIR2021_gain_loss_identity": {
                "years_with_nonzero_residual": [r["year_ending_june"] for r in transitions if r["gross_loss_plus_gain_minus_reported_net_kha"] not in ("", 0)],
                "minimum_kha": min(int(r["gross_loss_plus_gain_minus_reported_net_kha"]) for r in transitions if r["gross_loss_plus_gain_minus_reported_net_kha"] != ""),
                "maximum_kha": max(int(r["gross_loss_plus_gain_minus_reported_net_kha"]) for r in transitions if r["gross_loss_plus_gain_minus_reported_net_kha"] != ""),
                "note": "Reported net change is retained; gains and losses are independently rounded to 1 kha.",
            },
        },
        "Cameroon": {
            "source": "2026 revised national forest reference level; Tables 9, 31 and 37",
            "actual_annual_period": "2000–2020; no 2023 annual forest-area or AGB endpoint",
            "reported_total_forest_area": {
                "2015_ha": c15["reported_total_forest_ha"], "2020_ha": c20["reported_total_forest_ha"],
                "change_2015_to_2020_ha": cmr_delta, "change_percent": str(pct(c20["reported_total_forest_ha"], c15["reported_total_forest_ha"])),
                "class_sum_minus_reported_total_2015_ha": c15["class_sum_minus_reported_total_ha"],
                "class_sum_minus_reported_total_2020_ha": c20["class_sum_minus_reported_total_ha"],
                "class_changes_2015_to_2020_ha": {k.replace("_ha", ""): c20[k] - c15[k] for k in ("dense_humid_forest_ha", "inundated_forest_ha", "planted_forest_ha", "dry_forest_ha", "mangrove_ha")},
            },
            "reported_net_forest_CO2e_flux_not_AGB_stock_change": {
                "2015_tCO2e_per_year": f15["reported_net_forest_flux_tCO2e_per_year"], "2020_tCO2e_per_year": f20["reported_net_forest_flux_tCO2e_per_year"],
                "difference_2020_minus_2015_tCO2e_per_year": str(cmr_flux_delta),
                "net_sink_magnitude_change_percent": str((abs(Decimal(f20["reported_net_forest_flux_tCO2e_per_year"])) - abs(Decimal(f15["reported_net_forest_flux_tCO2e_per_year"]))) / abs(Decimal(f15["reported_net_forest_flux_tCO2e_per_year"])) * 100),
                "MC_relative_uncertainty_2015_percent": f15["monte_carlo_relative_uncertainty_percent"], "MC_relative_uncertainty_2020_percent": f20["monte_carlo_relative_uncertainty_percent"],
                "uncertainty_note": "Provider-reported Monte-Carlo relative uncertainty is retained; raw draws/covariances are unavailable and no new confidence interval is constructed.",
            },
        },
        "Australia": {
            "ABARES_adjusted_area": {
                "actual_period": "years ending June 1989–2021; NIR2021 changes applied to the ABARES 2021 multiple-lines-of-evidence total",
                "2015_Mha": a15["abares_adjusted_forest_area_Mha"], "2021_Mha": a21["abares_adjusted_forest_area_Mha"],
                "change_2015_to_2021_Mha": str(Decimal(a21["abares_adjusted_forest_area_Mha"]) - Decimal(a15["abares_adjusted_forest_area_Mha"])),
                "change_percent": str(pct(a21["abares_adjusted_forest_area_Mha"], a15["abares_adjusted_forest_area_Mha"])),
            },
            "NIR2021_transition_stock_and_flows": {
                "2015_stock_Mha": t15["nir2021_forest_land_stock_Mha"], "2021_stock_Mha": t21["nir2021_forest_land_stock_Mha"],
                "change_2015_to_2021_Mha": str(Decimal(t21["nir2021_forest_land_stock_Mha"]) - Decimal(t15["nir2021_forest_land_stock_Mha"])),
                "2021_gross_loss_kha": t21["gross_loss_kha"], "2021_gross_gain_kha": t21["gross_gain_kha"], "2021_net_change_kha": t21["net_change_kha"],
                "note": "Losses are negative in this ABARES presentation; this NIR2021 lineage is not spliced with NIR2023 flows.",
            },
            "NIR2023_forest_land": {
                "2014_15_kha": n15["forest_land_kha"], "2020_21_kha": n21["forest_land_kha"], "2021_22_kha": n22["forest_land_kha"], "2022_23_kha": n23["forest_land_kha"],
                "change_2014_15_to_2020_21_kha": nir_delta_15_21, "change_2014_15_to_2020_21_percent": str(pct(n21["forest_land_kha"], n15["forest_land_kha"])),
                "change_2014_15_to_2021_22_kha": nir_delta_15_22, "change_2014_15_to_2021_22_percent": str(pct(n22["forest_land_kha"], n15["forest_land_kha"])),
                "reported_change_2014_15_to_2022_23_kha": n23["forest_land_kha"] - n15["forest_land_kha"],
                "final_year_status": "2022–23 areas and disaggregated forest-cover activity are held constant at 2021–22 levels; not an independently observed annual endpoint.",
            },
            "NIR2023_clearing_regrowth": {
                "2014_15": {k: flow15[k] for k in ("primary_forest_conversion_kha", "secondary_forest_reclearing_kha", "identified_regrowth_kha", "net_forest_clearing_kha")},
                "2021_22": {k: flow22[k] for k in ("primary_forest_conversion_kha", "secondary_forest_reclearing_kha", "identified_regrowth_kha", "net_forest_clearing_kha")},
                "2022_23": {k: flow23[k] for k in ("primary_forest_conversion_kha", "secondary_forest_reclearing_kha", "identified_regrowth_kha", "net_forest_clearing_kha")},
                "sign_note": "Net clearing = primary conversion + re-clearing − identified regrowth; negative values denote net regrowth in this specific account, not national AGB change.",
            },
            "Forests_of_Australia_2023_snapshot": {
                **snapshot,
                "latest_information_currency": "30 June 2021", "publication_date": "December 2023", "cell_size": "100 x 100 m; COUNT equals hectares",
                "difference_from_adjusted_2021_series_ha": snapshot["forest_ha"] - int(Decimal(a21["abares_adjusted_forest_area_Mha"]) * 1000000),
                "note": "A publication-year label is not a 2023 observation. Exact raster attributes and the independently rounded adjusted series are retained separately.",
            },
            "AGB_status": "No public source used here supplies a calibrated national 2015–2023 forest-AGB endpoint comparison; forest area and CO2e flows are not AGB.",
        },
    }


def run() -> None:
    OUT.mkdir(exist_ok=True)
    META.mkdir(exist_ok=True)
    for path in (CMR_PDF, AUS_NIR1, AUS_NIR2, ABARES_TXT, ABARES_ATTR, ABARES_META, ABARES_LUT):
        require(path.is_file(), f"Retrieve source before extraction: {path}")
    area = cameroon_area()
    flux = cameroon_flux()
    nir = nir_area()
    flows = nir_flows()
    abares, transitions = abares_series()
    _, _, snapshot = abares_snapshot()
    summary = make_summary(area, flux, nir, flows, abares, transitions, snapshot)
    (OUT / "national_physical_module_summary_F16.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    sources = [
        ("Cameroon revised national forest reference level", CMR_PDF, "https://redd.unfccc.int/media/cmr_nrf_zero_final_20janvier2026_f.pdf?download=1", "Tables 9, 31 and 37; PDF pp. 31, 86–87, 140–141"),
        ("Australia National Inventory Report 2023, Volume 1", AUS_NIR1, "https://unfccc.int/sites/default/files/resource/National%20Inventory%20Report%202023%20-%20Volume%201.pdf", "Table 6.2.2 PDF p.316; carry-forward statement PDF p.302"),
        ("Australia National Inventory Report 2023, Volume 2", AUS_NIR2, "https://unfccc.int/sites/default/files/resource/National%20Inventory%20Report%202023%20-%20Volume%202.pdf", "Annex Tables A5.6.12.1a/b PDF pp.352–354"),
        ("ABARES Indicator 1.1a.iv workbook, five-sheet text extraction", ABARES_TXT, "https://www.agriculture.gov.au/sites/default/files/documents/Indicator_1_1a_iv_area_change_Data_Tables_2023.xlsx", "Figures 1.1a.iv-1 and 1.1a.iv-2; Jina extraction of public XLSX"),
        ("Forests of Australia (2023) attribute CSV", ABARES_ATTR, "https://data.gov.au/data/dataset/c426860e-9b55-404e-9892-e975794018d5/resource/849a0d00-577a-4eb2-b77f-4d63264201ae/download/aus_for23_attributes.csv", "687 attribute rows; CC BY 4.0"),
        ("Forests of Australia (2023) metadata", ABARES_META, "https://data.gov.au/data/dataset/c426860e-9b55-404e-9892-e975794018d5/resource/39d20025-fcac-4b66-9dbb-e84d50e7710e/download/forests_of_australia_2023_metadata.pdf", "Currency 30 June 2021; 1-ha cells; Australia excluding external territories"),
        ("Forests of Australia (2023) lookup tables", ABARES_LUT, "https://data.gov.au/data/dataset/c426860e-9b55-404e-9892-e975794018d5/resource/88faecc3-c297-46b6-8507-62e8837cea89/download/forests_of_australia_2023_lookup_tables.pdf", "COUNT equals area in hectares"),
    ]
    provenance = [{"title": title, "local_cache_name": path.name, "sha256": sha(path), "bytes": path.stat().st_size, "url": url, "used_for": used} for title, path, url, used in sources]
    (META / "source_provenance_F16.json").write_text(json.dumps({"retrieved_on": "2026-10-30", "sources": provenance, "redistribution": "Only small derived CSV/JSON results are packaged; official PDFs and CRT ZIP are excluded.", "CRT_selective_range_listing": {"url": "https://unfccc.int/sites/default/files/resource/Common%20Reporting%20Tables%201990-2023.zip", "bytes": 130761002, "range_requests": 4, "range_payload_bytes": 6160, "members": 34, "needed": False, "reason": "NIR Tables 6.2.2 and A5.6.12.1a/b already supply the required source-pinned annual physical values; no redundant CRT download was made."}}, indent=2) + "\n")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    run()
