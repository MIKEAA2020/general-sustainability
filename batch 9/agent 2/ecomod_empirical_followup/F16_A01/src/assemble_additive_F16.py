#!/usr/bin/env python3
"""Add source-pinned Cameroon/Australia modules to the frozen F15 manuscript."""
from __future__ import annotations
import csv
import json
import re
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def rows(name: str) -> list[dict]:
    with (DATA / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def replace_once(text: str, old: str, new: str, label: str) -> str:
    require(text.count(old) == 1, f"Expected one {label}, found {text.count(old)}")
    return text.replace(old, new)


def table(label: str, caption: str, headers: list[str], body: list[list[str]], spec: str) -> str:
    return (
        "\\begin{table}[htbp]\n\\centering\\small\n"
        f"\\caption{{{caption}}}\\label{{{label}}}\n"
        f"\\begin{{tabularx}}{{\\textwidth}}{{{spec}}}\\toprule\n"
        + " & ".join(headers) + "\\\\\\midrule\n"
        + "\n".join(" & ".join(row) + "\\\\" for row in body)
        + "\n\\bottomrule\\end{tabularx}\n\\end{table}\n"
    )


def figure(file: str, label: str, caption: str) -> str:
    return f"\\begin{{figure}}[htbp]\n\\centering\\includegraphics[width=1\\textwidth]{{{file}}}\n\\caption{{{caption}}}\\label{{{label}}}\n\\end{{figure}}\n"


def number(value: str | int | Decimal, places: int = 0) -> str:
    decimal = Decimal(str(value))
    quantum = Decimal(1).scaleb(-places)
    decimal = decimal.quantize(quantum, rounding=ROUND_HALF_UP)
    rendered = f"{decimal:,.{places}f}"
    return rendered.replace("-", "$-$")


def percent(start: str | int, end: str | int, places: int = 4) -> str:
    value = (Decimal(str(end)) - Decimal(str(start))) / Decimal(str(start)) * 100
    return ("$+$" if value > 0 else "") + number(value, places) + "\\%"


def cameroon_si() -> str:
    area = rows("CMR_reported_forest_area_2000_2020_F16.csv")
    flux = rows("CMR_reported_net_forest_flux_2000_2020_F16.csv")
    a15, a20 = (next(r for r in area if r["year"] == str(y)) for y in (2015, 2020))
    f15, f20 = (next(r for r in flux if r["year"] == str(y)) for y in (2015, 2020))
    body = []
    classes = [
        ("Reported total forest area (Mha)", "reported_total_forest_ha"),
        ("Dense humid forest (Mha)", "dense_humid_forest_ha"),
        ("Inundated/inundable forest (Mha)", "inundated_forest_ha"),
        ("Planted forest (Mha)", "planted_forest_ha"),
        ("Dry forest (Mha)", "dry_forest_ha"),
        ("Mangrove (Mha)", "mangrove_ha"),
    ]
    for label, key in classes:
        start, end = Decimal(a15[key]) / Decimal(1000000), Decimal(a20[key]) / Decimal(1000000)
        body.append([label, number(start, 6), number(end, 6), ("$+$" if end > start else "") + number(end - start, 6), percent(start, end) if start != end else "0.0000\\%"])
    start_flux, end_flux = Decimal(f15["reported_net_forest_flux_tCO2e_per_year"]) / Decimal(1000000), Decimal(f20["reported_net_forest_flux_tCO2e_per_year"]) / Decimal(1000000)
    sink_change = (abs(end_flux) - abs(start_flux)) / abs(start_flux) * 100
    body.append(["Reported net forest CO$_2$e flux (MtCO$_2$e/yr)", number(start_flux, 6), number(end_flux, 6), "$+$" + number(end_flux - start_flux, 6), "Sink magnitude " + number(sink_change, 4) + "\\%"])
    u15, u20 = Decimal(f15["monte_carlo_relative_uncertainty_percent"]), Decimal(f20["monte_carlo_relative_uncertainty_percent"])
    body.append(["Provider MC relative uncertainty (\\%)", number(u15, 2), number(u20, 2), "$+$" + number(u20 - u15, 2) + " pp", "Not a new interval"])
    caption = "Cameroon reported 2015 and 2020 values from Tables 9 and 31. Area and annual net CO$_2$e flux are different estimands; neither is a forest-AGB stock-change estimate. Reported totals are retained even where class sums differ by 1 ha. MC relative uncertainties are provider values, not newly constructed confidence intervals."
    return table("tab:SI_Cameroon_reported", caption, ["Quantity", "2015", "2020", "Change", "Relative/note"], body, "XrrrX")


def australia_si() -> str:
    ab = rows("AUS_ABARES_adjusted_forest_area_1989_2021_F16.csv")
    n21 = rows("AUS_NIR2021_stock_gains_losses_1989_2021_F16.csv")
    n23 = rows("AUS_NIR2023_forest_land_1989_2023_F16.csv")
    flows = rows("AUS_NIR2023_clearing_regrowth_1990_2023_F16.csv")
    ab15, ab21 = (next(r for r in ab if r["year_ending_june"] == str(y)) for y in (2015, 2021))
    t15, t21 = (next(r for r in n21 if r["year_ending_june"] == str(y)) for y in (2015, 2021))
    n15, n21r, n22, n23r = (next(r for r in n23 if r["year_ending_june"] == str(y)) for y in (2015, 2021, 2022, 2023))
    f15, f22 = (next(r for r in flows if r["year_ending_june"] == str(y)) for y in (2015, 2022))
    body = []
    start, end = Decimal(ab15["abares_adjusted_forest_area_Mha"]), Decimal(ab21["abares_adjusted_forest_area_Mha"])
    body.append(["ABARES-adjusted area (Mha)", number(start, 2) + " (2015)", number(end, 2) + " (2021)", "$+$" + number(end - start, 2), percent(start, end) + "; adjusted series"])
    start, end = Decimal(t15["nir2021_forest_land_stock_Mha"]), Decimal(t21["nir2021_forest_land_stock_Mha"])
    body.append(["NIR2021 transition stock (Mha)", number(start, 2) + " (2015)", number(end, 2) + " (2021)", "$+$" + number(end - start, 2), percent(start, end) + "; separate vintage"])
    for label, key, note in [
        ("NIR2021 gross loss (kha)", "gross_loss_kha", "Losses negative"),
        ("NIR2021 gross gain (kha)", "gross_gain_kha", "Transition gains"),
        ("NIR2021 reported net change (kha)", "net_change_kha", "2021 residual +1 kha"),
    ]:
        start, end = Decimal(t15[key]), Decimal(t21[key])
        body.append([label, number(start) + " (2015)", number(end) + " (2021)", ("$+$" if end > start else "") + number(end - start), note])
    for end_row, year, qualification in [(n21r, "2020--21", "Annual row"), (n22, "2021--22", "Last non-carried row"), (n23r, "2022--23", "Final row carried forward")]:
        start, end = Decimal(n15["forest_land_kha"]), Decimal(end_row["forest_land_kha"])
        body.append(["NIR2023 forest land (kha)", number(start) + " (2014--15)", number(end) + f" ({year})", "$+$" + number(end - start), percent(start, end) + "; " + qualification])
    for label, key, note in [
        ("NIR2023 primary conversion (kha)", "primary_forest_conversion_kha", "Gross activity"),
        ("NIR2023 secondary re-clearing (kha)", "secondary_forest_reclearing_kha", "Gross activity"),
        ("NIR2023 identified regrowth (kha)", "identified_regrowth_kha", "Not sustained-regrowth stock"),
        ("NIR2023 net clearing (kha)", "net_forest_clearing_kha", "Negative: net regrowth"),
    ]:
        start, end = Decimal(f15[key]), Decimal(f22[key])
        body.append([label, number(start, 1) + " (2014--15)", number(end, 1) + " (2021--22)", ("$+$" if end > start else "") + number(end - start, 1), note])
    caption = "Australia source- and vintage-specific annual quantities. ABARES-adjusted area, NIR2021 transition stock/flows and NIR2023 forest land/conversion/regrowth are not spliced or treated as uncertainty bounds. All years end in June. NIR2023 2022--23 values repeat 2021--22 under the documented carry-forward. None is AGB."
    return table("tab:SI_Australia_reported", caption, ["Source/quantity", "Start", "End", "Change", "Qualification"], body, "XrrrX")


def snapshot_si() -> str:
    categories = rows("AUS_Forests2023_category_areas_F16.csv")
    states = rows("AUS_Forests2023_state_areas_F16.csv")
    total = sum(int(r["area_ha"]) for r in categories if r["forest_category"] != "Non-forest")
    body = [["National", "All forest", number(total), "100.000"]]
    for record in sorted((r for r in categories if r["forest_category"] != "Non-forest"), key=lambda r: int(r["area_ha"]), reverse=True):
        area = int(record["area_ha"])
        body.append(["Category", record["forest_category"], number(area), number(Decimal(area * 100) / Decimal(total), 3)])
    for record in sorted(states, key=lambda r: int(r["forest_ha"]), reverse=True):
        area = int(record["forest_ha"])
        body.append(["Jurisdiction", record["state_or_territory"], number(area), number(Decimal(area * 100) / Decimal(total), 3)])
    caption = "Forests of Australia (2023) attribute-table aggregates. COUNT equals hectares for 100-m cells. Latest information currency is 30 June 2021, not 2023; coverage is Australia excluding external territories. Jurisdiction rows partition forest area; a separate 5,875-ha unallocated nonforest remainder is retained in the CSV."
    return table("tab:SI_Australia_snapshot", caption, ["Partition", "Class/jurisdiction", "Forest area (ha)", "Share of national forest (\\%)"], body, "llrr")


def build() -> None:
    main = (ROOT / "inputs/F15_main.tex").read_text()
    abstract = r"""Increasing productivity-weighted accounts need not identify ecological asset gains. We combine national accounts, source-specific forest series, official inventories and a matched-support biomass identification experiment. Of 183 eligible account identifiers in 2015--2023, 91 increase in total biocapacity; 68 have a decreasing forest account component, an accounting result rather than independent forest-loss evidence. Published mapped groups decline by 10.863, 0.703 and 3.303 million ha in Brazil, Indonesia and the Democratic Republic of the Congo, respectively, without calibrated change intervals. Cameroon's reported forest area falls by 0.149 million ha (2015--2020), whereas Australia's ABARES-adjusted area rises by 1.06 million ha (2015--2021); Australia's NIR2023 final-year activity is carried forward. Annual transitions bound the Indonesian 2015-forest-to-2023-oil-palm cohort at 0.112--2.326 million ha, conditional on classifications; repeated events are not unique hectares. Official inventories yield conditional positive Finnish/French campaign-volume differences without assuming cross-inventory independence; Canada's earlier-domain AGB-change interval includes zero and its uncertainty needs reconciliation. On the fixed 61,830 ha Brazilian footprint, the auxiliary whole-cell biomass point-map total increases by $\MapNet\times10^3$ Mg, while $\MapCancellation\%$ of absolute local differences cancels. Constructive allocations preserve cell totals and mapped fractions yet permit all four joint sign quadrants for nested cover groups. Native-cell mass narrows identification sets by $\ReductionForm\%$ and $\ReductionSav\%$ relative to one-window totals but identifies neither sign; density-contrast thresholds remain uncalibrated. None of eight candidates supplies the original calibrated national 2015--2023 forest-AGB comparison. Results separate extent, flux, volume, biomass and uncertainty; they do not establish ecological composition masking, conversion associations or reporting accuracy."""
    main = re.sub(r"\\begin\{abstract\}.*?\\end\{abstract\}", lambda _match: "\\begin{abstract}\n" + abstract + "\n\\end{abstract}", main, count=1, flags=re.S)
    main = replace_once(main, "\\input{src/SI_reference_numbers_F15.tex}", "\\input{src/SI_reference_numbers_F16.tex}", "SI reference input")
    main = replace_once(main, "Cameroon & $+0.54/-3.16$ & No completed physical numerical module.\\\\", "Cameroon & $+0.54/-3.16$ & Reported forest area: $-0.149$ Mha ($-0.47\\%$), 2015--2020. Net CO$_2$e flux is separate; no 2023 AGB endpoint.\\\\", "Cameroon overview")
    main = replace_once(main, "Australia & $+12.95/-0.33$ & No completed physical numerical module.\\\\", "Australia & $+12.95/-0.33$ & ABARES-adjusted area: $+1.06$ Mha ($+0.80\\%$), 2015--2021. NIR2023 forest land: $+2.054$ Mha through 2021--22; 2022--23 carried forward.\\\\", "Australia overview")
    main = replace_once(main, "mapped extent, volume and biomass are not interchangeable", "mapped extent, reported area/CO$_2$e flux, volume and biomass are not interchangeable", "overview caption")

    methods = r"""
Cameroon's revised national forest reference level supplies reported annual forest area and net forest CO$_2$e flux for 2000--2020 \citep{CameroonFRL2026}. We use the published totals and provider Monte-Carlo relative uncertainties without treating flux as AGB-stock change. Australia's NIR2023 supplies financial-year forest-land totals and clearing/regrowth through 2022--23; its final forest-cover activity is held constant at 2021--22 levels \citep{AustraliaNIR2023a,AustraliaNIR2023b}. ABARES separately supplies an adjusted annual area series through 2021 and the Forests of Australia (2023) attributes, whose latest information currency is 30 June 2021 \citep{ABARES2023change,ABARES2023forest}. We do not splice these sources or vintages, infer AGB from area, or interpret their differences as uncertainty intervals.
"""
    main = replace_once(main, "\n\n\\subsection{Matched support and conditional biomass allocation}", "\n" + methods + "\n\\subsection{Matched support and conditional biomass allocation}", "physical methods insertion")

    results = r"""
Cameroon's reported total forest area decreases from 31,332,386 ha in 2015 to 31,183,654 ha in 2020: $-148{,}732$ ha ($-0.4747\%$). Dense humid and dry forest classes have reported decreases of 88,916 and 59,817 ha; inundated, planted and mangrove areas are unchanged. Five annual class sums exceed the corresponding reported national total by 1 ha, including 2015, so the reported total is not silently replaced by a forced class sum. The separate reported net forest CO$_2$e flux changes from $-113.383$ to $-109.600$ MtCO$_2$e/yr, a $+3.783$ MtCO$_2$e/yr difference and a 3.34\% smaller net-sink magnitude. Provider Monte-Carlo relative uncertainty is 31.10\% in 2015 and 32.14\% in 2020. These are annual reported CO$_2$e fluxes, not forest-AGB stock changes or 2023 endpoints (Figure~\ref{fig:reported_area_flux}; Supplementary Table~\SIref{tab:SI_Cameroon_reported}).

Australia's ABARES-adjusted forest area rises from 132.51 Mha in 2015 to 133.57 Mha in 2021, an increase of 1.06 Mha ($+0.7999\%$). Its separate NIR2021 transition table reports 132.98 and 134.03 Mha, with 2021 gross loss of $-216$ kha, gross gain of $+487$ kha and reported net change of $+270$ kha. The newer NIR2023 forest-land total rises from 135,318 kha in 2014--15 to 136,862 kha in 2020--21 and 137,372 kha in 2021--22, a $+2{,}054$ kha ($+1.5179\%$) increase through 2021--22. The 2022--23 row repeats 2021--22 because the forest-cover monitoring system was unavailable and reported areas were held constant; it is not an independently observed annual endpoint. In 2021--22, NIR2023 reports 21.6 kha primary conversion, 164.5 kha re-clearing and 436.7 kha identified regrowth, giving net clearing of $-250.6$ kha under its stated identity. Forests of Australia (2023) instead contains 133,564,800 forest ha in its attribute table, with latest information currency 30 June 2021; it is not a 2023 observation. These source- and vintage-specific quantities remain distinct and none is an AGB change (Figure~\ref{fig:reported_area_flux}; Supplementary Tables~\SIref{tab:SI_Australia_reported} and \SIref{tab:SI_Australia_snapshot}).
"""
    new_figure = figure(
        "national_physical_modules_F16.pdf", "fig:reported_area_flux",
        "Reported national physical series on their actual source periods. (a) Cameroon forest area, 2000--2020. (b) Cameroon annual net forest CO$_2$e flux; negative values denote net removals and are not AGB-stock changes. (c) Australia's separate ABARES-adjusted, NIR2021 and NIR2023 forest-area lineages; years end in June and the dotted final NIR2023 segment is a documented carry-forward, not a new observation. Lines and their separations are not confidence intervals or reporting-error estimates. Exact values, source vintages and rounding checks appear in Supplementary Tables~\\SIref{tab:SI_Cameroon_reported}--\\SIref{tab:SI_Australia_snapshot}."
    )
    main = replace_once(main, "\n\n\\subsection{A common local support does not identify the forest-group trend}", "\n" + results + new_figure + "\n\\subsection{A common local support does not identify the forest-group trend}", "national physical results insertion")
    main = replace_once(main, "Australia and Cameroon remain unexecuted physical modules, not demonstrated cases of permanent data unavailability.", "Australia and Cameroon now have descriptive reported-area/flux modules on their actual periods, but these do not supply calibrated national 2015--2023 forest-AGB comparisons.", "scope update")
    main = replace_once(main, "Three executed national mapped-cover series, conditional unique endpoint-cohort bounds and official inventory-cycle quantities add substantive empirical evidence.", "Three national mapped-cover series, reported Cameroonian and Australian area/flux modules, conditional unique endpoint-cohort bounds and official inventory-cycle quantities add substantive empirical evidence.", "conclusion update")
    main = replace_once(main, "Source-specific national mapped extent and conditional inventory-cycle stock results are now quantified", "Source-specific national mapped/reported extent and conditional inventory-cycle stock results are now quantified", "discussion update")
    main = main.replace("/F15_A01", "/F16_A01")

    bibliography = r"""
\bibitem[Cameroon(2026)]{CameroonFRL2026} Republic of Cameroon (2026). \emph{Revised National Forest Reference Level}. Tables 9, 31 and 37, submitted under the UNFCCC REDD+ process. \url{https://redd.unfccc.int/media/cmr_nrf_zero_final_20janvier2026_f.pdf?download=1}.
\bibitem[DCCEEW(2025a)]{AustraliaNIR2023a} Australian Government Department of Climate Change, Energy, the Environment and Water (2025a). \emph{National Inventory Report 2023, Volume 1}. Table 6.2.2 and forest-cover carry-forward description. \url{https://unfccc.int/sites/default/files/resource/National%20Inventory%20Report%202023%20-%20Volume%201.pdf}.
\bibitem[DCCEEW(2025b)]{AustraliaNIR2023b} Australian Government Department of Climate Change, Energy, the Environment and Water (2025b). \emph{National Inventory Report 2023, Volume 2}. Annex Tables A5.6.12.1a/b. \url{https://unfccc.int/sites/default/files/resource/National%20Inventory%20Report%202023%20-%20Volume%202.pdf}.
\bibitem[ABARES(2023a)]{ABARES2023change} ABARES (2023a). \emph{Indicator 1.1a.iv: Forest area change over time}, Australia's State of the Forests Report, with Figures 1.1a.iv-1 and 1.1a.iv-2 data workbook. \url{https://www.agriculture.gov.au/abares/forestsaustralia/sofr/criterion-1/indicator-1.1a.iv-forest-area-change}.
\bibitem[ABARES(2023b)]{ABARES2023forest} ABARES (2023b). \emph{Forests of Australia (2023)}, attribute table, metadata and lookup tables; latest information currency 30 June 2021. CC BY 4.0. \url{https://data.gov.au/data/dataset/forests-of-australia-2023}.
"""
    main = replace_once(main, "\n\\end{thebibliography}", bibliography + "\n\\end{thebibliography}", "new bibliography")

    si = (ROOT / "inputs/F15_SI.tex").read_text()
    si = si.replace("/F15_A01", "/F16_A01")
    si = replace_once(si, "\\usepackage{xurl}", "\\usepackage{xurl}\n\\usepackage{needspace}", "SI needspace package")
    si = replace_once(si, "\\input{src/identification_protocols_SI_F15.tex}", "\\input{inputs/F15_src/identification_protocols_SI_F15.tex}", "identification SI input")
    si = replace_once(si, "\\input{src/national_protocols_SI_F15.tex}", "\\input{src/national_protocols_inherited_F16.tex}", "national SI input")
    availability = r"""Cameroon and Australia: Republic of Cameroon revised national forest reference level (2026), Tables 9, 31 and 37; Australian NIR2023 Volumes 1/2, Table 6.2.2 and Annex Tables A5.6.12.1a/b; ABARES Indicator 1.1a.iv workbook and Forests of Australia (2023) attributes/metadata. ABARES spatial attributes are CC BY 4.0. Only derived numerical tables and source hashes are distributed here; provider PDFs and the CRT archive are not redistributed.

"""
    si = replace_once(si, "AGBref: Araza, A., Bielig", availability + "AGBref: Araza, A., Bielig", "new SI source attribution")
    si = replace_once(si, "\n\\section{Provider technical references}", "\n\\Needspace{24\\baselineskip}\n\\section{Provider technical references}", "provider-reference page guard")
    national = (ROOT / "inputs/F15_src/national_protocols_SI_F15.tex").read_text()
    national = national.replace("corresponding to main Figure 5", "corresponding to the main endpoint-cohort figure")
    protocols = r"""
\section{Cameroon and Australian source and rounding protocols}
Cameroon Table 9 is used for reported forest area and Tables 31/37 for reported annual net forest CO$_2$e flux. Table 31 values rounded to whole tCO$_2$e reproduce the Total REDD+ rendering in Table 37 for all 21 years. The provider's Monte-Carlo relative uncertainty is transcribed without assigning a new confidence level or covariance model. In 2011, 2012, 2015, 2016 and 2019, the five class areas sum to 1 ha more than the reported total; the residual is zero in the other 16 years. Reported totals and classes are both retained without adjustment. The table's CEO 2023--2024 reference does not create a 2023 annual endpoint.

The ABARES-adjusted series applies NIR2021 area-change data to the ABARES multiple-lines-of-evidence total. Its difference-from-2016 column exceeds subtraction of the independently displayed areas by 0.01 Mha in 1993, 2001, 2010 and 2020. The separate NIR2021 gain/loss presentation has residuals of $\pm1$ kha in six years (1990, 1994, 1999, 2019, 2020 and 2021); the reported net field is retained. NIR2023 is a newer, complete vintage and is not spliced with NIR2021. Its clearing identity residuals lie within $\pm0.1$ kha, the displayed precision. Volume 1 states that the forest-cover monitoring system was unavailable for the 2023 report and that areas and disaggregated emissions were held constant at 2022 levels using an extrapolation approach; 2022--23 is therefore flagged throughout.

Forests of Australia (2023) has December 2023 publication provenance but 30 June 2021 latest-information currency. Its NGGI input combines five annual 2016--2020 layers, classifying a cell as forest if mapped forest in any of those years, before integration with other sources. The exact attribute sum is 133,564,800 forest ha, 5,200 ha below 133.57 Mha when the adjusted annual 2021 cell is expressed on the same nominal scale; this is not forced into identity or interpreted as an error bound. All 687 attribute rows are retained. A blank-state group contains 5,875 nonforest ha and is labelled Unallocated in the derived jurisdiction table. These source protocols concern extent and CO$_2$e activity, not AGB calibration.

"""
    insertion = protocols + cameroon_si() + "\n" + australia_si() + "\n" + snapshot_si() + "\n"
    national = replace_once(national, "\\section{Sharp endpoint-cohort bounds", insertion + "\\section{Sharp endpoint-cohort bounds", "new SI protocols")
    (ROOT / "src/national_protocols_inherited_F16.tex").write_text(national)
    (ROOT / "integrated_F16_A01_main.tex").write_text(main)
    (ROOT / "integrated_F16_A01_SI.tex").write_text(si)
    if not (ROOT / "src/SI_reference_numbers_F16.tex").exists():
        (ROOT / "src/SI_reference_numbers_F16.tex").write_text("\\newcommand{\\SIref}[1]{\\ifcsname SIlabel:#1\\endcsname\\csname SIlabel:#1\\endcsname\\else ??\\fi}\n")
    print("Assembled additive F16 main and SI: seven main figures, two main tables, three new linked SI tables.")


if __name__ == "__main__":
    build()
