import csv
import hashlib
import json
import re
import unittest
from decimal import Decimal
from pathlib import Path

from build_F16 import ROOT, expand


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(name: str) -> list[dict]:
    with (ROOT / "data" / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


class F16Integration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.main = (ROOT / "integrated_F16_A01_main.tex").read_text()
        cls.full = expand(ROOT / "integrated_F16_A01_main.tex")
        cls.si = expand(ROOT / "integrated_F16_A01_SI.tex")
        cls.links = json.loads((ROOT / "metadata/SI_linkage_F16.json").read_text())
        cls.summary = json.loads((ROOT / "data/national_physical_module_summary_F16.json").read_text())
        cls.provenance = json.loads((ROOT / "metadata/source_provenance_F16.json").read_text())
        cls.cmr_area = read_csv("CMR_reported_forest_area_2000_2020_F16.csv")
        cls.cmr_flux = read_csv("CMR_reported_net_forest_flux_2000_2020_F16.csv")
        cls.ab = read_csv("AUS_ABARES_adjusted_forest_area_1989_2021_F16.csv")
        cls.n21 = read_csv("AUS_NIR2021_stock_gains_losses_1989_2021_F16.csv")
        cls.n23 = read_csv("AUS_NIR2023_forest_land_1989_2023_F16.csv")
        cls.flows = read_csv("AUS_NIR2023_clearing_regrowth_1990_2023_F16.csv")

    def test_01_seven_main_figures(self):
        self.assertEqual(self.full.count("\\begin{figure}"), 7)

    def test_02_two_main_tables(self):
        self.assertEqual(self.full.count("\\begin{table}"), 2)

    def test_03_five_result_sections(self):
        result = self.main.split("\\section{Results}")[1].split("\\section{Discussion}")[0]
        self.assertEqual(result.count("\\subsection{"), 5)

    def test_04_SI_item_counts(self):
        counts = (sum(k.startswith("fig:") for k in self.links["labels"]), sum(k.startswith("tab:") for k in self.links["labels"]))
        self.assertEqual(counts, (2, 28))

    def test_05_every_SI_item_cited(self):
        self.assertEqual(set(self.links["labels"]), set(self.links["main_citations"]))

    def test_06_no_SI_discussion_or_workplan(self):
        self.assertNotIn("\\section{Discussion}", self.si)
        self.assertNotIn("Primary national AGB target and remaining evidence requirements", self.si)

    def test_07_abstract_limit_and_new_results(self):
        abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", self.main, re.S)[1]
        self.assertLessEqual(len(abstract.split()), 250)
        for phrase in ["0.149 million ha", "1.06 million ha", "final-year activity is carried forward", "None of eight candidates"]:
            self.assertIn(phrase, abstract)

    def test_08_seven_keywords(self):
        self.assertEqual(len(re.search(r"\\textbf\{Keywords:\}([^\n]+)", self.main)[1].split(";")), 7)

    def test_09_exact_AI_declaration(self):
        self.assertIn("Arena.ai Agent Mode was used to assist with computational methods and literature review.", self.main.replace(r"\href{http://Arena.ai}{Arena.ai}", "Arena.ai"))

    def test_10_ORCID(self):
        self.assertIn("orcid.org/0000-0002-0019-1842", self.main)

    def test_11_complete_case_set(self):
        for country in ["Brazil", "Indonesia", "DR Congo", "Cameroon", "Canada", "Finland", "France", "Australia"]:
            self.assertIn(country, self.main)

    def test_12_new_modules_replace_unexecuted_cells(self):
        self.assertNotIn("No completed physical numerical module", self.main)
        self.assertNotIn("remain unexecuted physical modules", self.main)
        self.assertIn("now have descriptive reported-area/flux modules", self.main)

    def test_13_Cameroon_annual_coverage(self):
        self.assertEqual([int(r["year"]) for r in self.cmr_area], list(range(2000, 2021)))
        self.assertEqual([int(r["year"]) for r in self.cmr_flux], list(range(2000, 2021)))

    def test_14_Cameroon_area_endpoints_and_change(self):
        a15 = next(r for r in self.cmr_area if r["year"] == "2015")
        a20 = next(r for r in self.cmr_area if r["year"] == "2020")
        start, end = int(a15["reported_total_forest_ha"]), int(a20["reported_total_forest_ha"])
        self.assertEqual((start, end, end - start), (31332386, 31183654, -148732))
        self.assertAlmostEqual((end - start) / start * 100, -0.4746909475709893, places=12)

    def test_15_Cameroon_class_changes_and_residuals(self):
        a15 = next(r for r in self.cmr_area if r["year"] == "2015")
        a20 = next(r for r in self.cmr_area if r["year"] == "2020")
        self.assertEqual(int(a20["dense_humid_forest_ha"]) - int(a15["dense_humid_forest_ha"]), -88916)
        self.assertEqual(int(a20["dry_forest_ha"]) - int(a15["dry_forest_ha"]), -59817)
        self.assertEqual([int(r["year"]) for r in self.cmr_area if r["class_sum_minus_reported_total_ha"] == "1"], [2011, 2012, 2015, 2016, 2019])
        self.assertTrue(all(int(r["class_sum_minus_reported_total_ha"]) in (0, 1) for r in self.cmr_area))

    def test_16_Cameroon_flux_endpoints_and_difference(self):
        f15 = next(r for r in self.cmr_flux if r["year"] == "2015")
        f20 = next(r for r in self.cmr_flux if r["year"] == "2020")
        start, end = Decimal(f15["reported_net_forest_flux_tCO2e_per_year"]), Decimal(f20["reported_net_forest_flux_tCO2e_per_year"])
        self.assertEqual((start, end, end - start), (Decimal("-113383116.17"), Decimal("-109599895.35"), Decimal("3783220.82")))
        sink = (abs(end) - abs(start)) / abs(start) * 100
        self.assertAlmostEqual(float(sink), -3.3366703507492777, places=12)

    def test_17_Cameroon_Table31_Table37_rounding(self):
        for row in self.cmr_flux:
            exact = Decimal(row["reported_net_forest_flux_tCO2e_per_year"])
            self.assertEqual(int(exact.to_integral_value()), int(row["table37_rounded_net_flux_tCO2e_per_year"]))
            self.assertLess(abs(Decimal(row["table31_minus_table37_rounded_tCO2e"])), Decimal("0.5"))

    def test_18_Cameroon_uncertainty_not_new_interval(self):
        f15 = next(r for r in self.cmr_flux if r["year"] == "2015")
        f20 = next(r for r in self.cmr_flux if r["year"] == "2020")
        self.assertEqual((f15["monte_carlo_relative_uncertainty_percent"], f20["monte_carlo_relative_uncertainty_percent"]), ("31.1", "32.14"))
        self.assertIn("no new confidence interval", self.summary["Cameroon"]["reported_net_forest_CO2e_flux_not_AGB_stock_change"]["uncertainty_note"])

    def test_19_flux_never_called_AGB_stock_change(self):
        self.assertIn("not forest-AGB stock changes or 2023 endpoints", self.main)
        self.assertIn("reported_net_forest_CO2e_flux_not_AGB_stock_change", self.summary["Cameroon"])

    def test_20_ABARES_adjusted_area(self):
        a15 = next(r for r in self.ab if r["year_ending_june"] == "2015")
        a21 = next(r for r in self.ab if r["year_ending_june"] == "2021")
        start, end = Decimal(a15["abares_adjusted_forest_area_Mha"]), Decimal(a21["abares_adjusted_forest_area_Mha"])
        self.assertEqual((start, end, end - start), (Decimal("132.51"), Decimal("133.57"), Decimal("1.06")))
        self.assertAlmostEqual(float((end - start) / start * 100), 0.7999396271979473, places=12)

    def test_21_ABARES_difference_rounding_audit(self):
        nonzero = [int(r["year_ending_june"]) for r in self.ab if Decimal(r["difference_column_minus_displayed_area_difference_Mha"]) != 0]
        self.assertEqual(nonzero, [1993, 2001, 2010, 2020])
        self.assertTrue(all(abs(Decimal(r["difference_column_minus_displayed_area_difference_Mha"])) <= Decimal("0.01") for r in self.ab))

    def test_22_NIR2021_stock_endpoints(self):
        t15 = next(r for r in self.n21 if r["year_ending_june"] == "2015")
        t21 = next(r for r in self.n21 if r["year_ending_june"] == "2021")
        self.assertEqual((t15["nir2021_forest_land_stock_Mha"], t21["nir2021_forest_land_stock_Mha"]), ("132.98", "134.03"))
        self.assertEqual(Decimal(t21["nir2021_forest_land_stock_Mha"]) - Decimal(t15["nir2021_forest_land_stock_Mha"]), Decimal("1.05"))

    def test_23_NIR2021_flow_rounding(self):
        rows = [r for r in self.n21 if r["gross_loss_kha"]]
        residuals = [int(r["gross_loss_plus_gain_minus_reported_net_kha"]) for r in rows]
        self.assertEqual(len(rows), 32)
        self.assertTrue(all(abs(x) <= 1 for x in residuals))
        self.assertEqual([int(r["year_ending_june"]) for r in rows if int(r["gross_loss_plus_gain_minus_reported_net_kha"]) != 0], [1990, 1994, 1999, 2019, 2020, 2021])

    def test_24_NIR2021_2021_flow_values(self):
        row = next(r for r in self.n21 if r["year_ending_june"] == "2021")
        self.assertEqual((row["gross_loss_kha"], row["gross_gain_kha"], row["net_change_kha"]), ("-216", "487", "270"))
        self.assertEqual(row["gross_loss_plus_gain_minus_reported_net_kha"], "1")

    def test_25_NIR2023_area_changes(self):
        rows = {int(r["year_ending_june"]): int(r["forest_land_kha"]) for r in self.n23}
        self.assertEqual((rows[2015], rows[2021], rows[2022], rows[2023]), (135318, 136862, 137372, 137372))
        self.assertEqual((rows[2021] - rows[2015], rows[2022] - rows[2015]), (1544, 2054))
        self.assertAlmostEqual((rows[2022] - rows[2015]) / rows[2015] * 100, 1.5179059696418806, places=12)

    def test_26_NIR2023_final_area_carried_forward(self):
        last = self.n23[-1]
        self.assertEqual(last["reporting_period"], "2022–23")
        self.assertEqual(last["activity_status"], "held_constant_at_2021_22_levels")
        self.assertEqual(last["forest_land_kha"], self.n23[-2]["forest_land_kha"])
        self.assertIn("not an independently observed annual endpoint", self.main)

    def test_27_NIR2023_flow_identity_and_rounding(self):
        for row in self.flows:
            residual = Decimal(row["primary_forest_conversion_kha"]) + Decimal(row["secondary_forest_reclearing_kha"]) - Decimal(row["identified_regrowth_kha"]) - Decimal(row["net_forest_clearing_kha"])
            self.assertEqual(residual, Decimal(row["clearing_identity_residual_kha"]))
            self.assertLessEqual(abs(residual), Decimal("0.1"))

    def test_28_NIR2023_final_flows_carried_forward(self):
        keys = ["primary_forest_conversion_kha", "secondary_forest_reclearing_kha", "identified_regrowth_kha", "net_forest_clearing_kha"]
        self.assertTrue(all(self.flows[-1][k] == self.flows[-2][k] for k in keys))
        self.assertEqual(self.flows[-1]["activity_status"], "held_constant_at_2021_22_levels")

    def test_29_NIR2023_2021_22_flow_values(self):
        row = next(r for r in self.flows if r["reporting_period"] == "2021–22")
        self.assertEqual((row["primary_forest_conversion_kha"], row["secondary_forest_reclearing_kha"], row["identified_regrowth_kha"], row["net_forest_clearing_kha"]), ("21.6", "164.5", "436.7", "-250.6"))

    def test_30_snapshot_national_categories(self):
        categories = read_csv("AUS_Forests2023_category_areas_F16.csv")
        forest = sum(int(r["area_ha"]) for r in categories if r["forest_category"] != "Non-forest")
        self.assertEqual(forest, 133564800)
        self.assertEqual(sum(int(r["area_ha"]) for r in categories), 768914778)
        self.assertEqual(next(int(r["area_ha"]) for r in categories if r["forest_category"] == "Native forest"), 131501369)

    def test_31_snapshot_jurisdictions_and_unallocated(self):
        states = read_csv("AUS_Forests2023_state_areas_F16.csv")
        self.assertEqual(sum(int(r["forest_ha"]) for r in states), 133564800)
        blank = next(r for r in states if r["state_or_territory"] == "Unallocated")
        self.assertEqual((blank["forest_ha"], blank["nonforest_ha"]), ("0", "5875"))

    def test_32_snapshot_period_and_units(self):
        snap = self.summary["Australia"]["Forests_of_Australia_2023_snapshot"]
        self.assertEqual(snap["latest_information_currency"], "30 June 2021")
        self.assertEqual(snap["difference_from_adjusted_2021_series_ha"], -5200)
        self.assertIn("COUNT equals hectares", snap["cell_size"])
        self.assertIn("not a 2023 observation", self.main)

    def test_33_source_lineages_not_spliced(self):
        combined = self.full + self.si
        for phrase in ["do not splice these sources or vintages", "not spliced or treated as uncertainty bounds", "separate NIR2021 transition table"]:
            self.assertIn(phrase, combined)

    def test_34_primary_AGB_scope_retained(self):
        self.assertIn("None of the eight calibrated national 2015--2023 forest-AGB analyses is complete", self.main)
        self.assertIn("Completion is distinct from sign resolution", self.main)

    def test_35_new_figure_caption_typed(self):
        caption = self.main.split("\\label{fig:reported_area_flux}")[0].split("\\caption{")[-1]
        self.assertIn("not AGB-stock changes", caption)
        self.assertIn("not confidence intervals", caption)
        self.assertIn("documented carry-forward", caption)

    def test_36_new_SI_tables_contain_source_values(self):
        for label in ["tab:SI_Cameroon_reported", "tab:SI_Australia_reported", "tab:SI_Australia_snapshot"]:
            self.assertIn(label, self.si)
        for value in ["31.332386", "0.148732", "135,318", "133,564,800", "5,875"]:
            self.assertIn(value, self.si)

    def test_37_new_bibliography_and_attribution(self):
        for key in ["CameroonFRL2026", "AustraliaNIR2023a", "AustraliaNIR2023b", "ABARES2023change", "ABARES2023forest"]:
            self.assertIn("\\citep{" + key, self.main) if key == "CameroonFRL2026" else self.assertIn(key, self.main)
        self.assertIn("ABARES spatial attributes are CC BY 4.0", self.si)

    def test_38_source_provenance_hashes(self):
        self.assertEqual(len(self.provenance["sources"]), 7)
        cache = ROOT.parent / ".cache/F16_sources"
        for record in self.provenance["sources"]:
            self.assertRegex(record["sha256"], r"^[0-9a-f]{64}$")
            matches = list(cache.rglob(record["local_cache_name"])) if cache.exists() else []
            if matches:
                self.assertEqual(sha(matches[0]), record["sha256"])

    def test_39_CRT_range_audit_and_no_archive(self):
        crt = self.provenance["CRT_selective_range_listing"]
        self.assertEqual((crt["bytes"], crt["range_requests"], crt["range_payload_bytes"], crt["members"]), (130761002, 4, 6160, 34))
        self.assertFalse(crt["needed"])
        self.assertFalse(any(p.suffix == ".zip" for p in ROOT.rglob("*") if p.is_file()))

    def test_40_workbook_inheritance_and_hash(self):
        report = json.loads((ROOT / "metadata/workbook_QA_F16.json").read_text())
        self.assertEqual((report["sheets"], report["inherited_sheets_unchanged"], report["new_sheets"], report["inherited_cells_checked"]), (41, 31, 10, 60336))
        self.assertEqual(sha(ROOT / report["file"]), report["sha256"])

    def test_41_plot_values_match_sources(self):
        plot = json.loads((ROOT / "metadata/plot_values_F16.json").read_text())
        self.assertEqual(plot["Cameroon_area_Mha"], {"2015": 31.332386, "2020": 31.183654})
        self.assertEqual(plot["Australia_2021_endpoints_Mha"]["ABARES_adjusted"], 133.57)
        self.assertTrue(plot["Australia_2022_23_is_carried_forward"])
        self.assertTrue((ROOT / "figures/national_physical_modules_F16.pdf").is_file())

    def test_42_frozen_F15_inputs_byte_identical(self):
        parent = ROOT.parent / "ecomod_editorial_restoration_F15_A01"
        pairs = [("integrated_F15_A01_main.tex", "F15_main.tex"), ("integrated_F15_A01_SI.tex", "F15_SI.tex"), ("national_results_F15_A01.xlsx", "national_results_F15_A01.xlsx"), ("PUBLICATION_RECEIPT_F15_A01.json", "F15_PUBLICATION_RECEIPT.json")]
        for original, copied in pairs:
            self.assertEqual(sha(parent / original), sha(ROOT / "inputs" / copied))
        for name in ["identification_protocols_SI_F15.tex", "national_protocols_SI_F15.tex"]:
            self.assertEqual(sha(parent / "src" / name), sha(ROOT / "inputs/F15_src" / name))

    def test_43_inherited_data_byte_identical(self):
        parent = ROOT.parent / "ecomod_editorial_restoration_F15_A01/data"
        inherited = [p for p in parent.iterdir() if p.is_file()]
        self.assertEqual(len(inherited), 13)
        for path in inherited:
            self.assertEqual(sha(path), sha(ROOT / "data" / path.name))

    def test_44_published_F15_root_unchanged(self):
        metadata = json.loads((ROOT / "metadata/protected_F15_identity.json").read_text())
        parent = ROOT.parent / metadata["folder"]
        self.assertEqual(len(metadata["files"]), 70)
        for record in metadata["files"]:
            self.assertEqual(sha(parent / record["path"]), record["sha256"], record["path"])

    def test_45_protected_earlier_roots_unchanged(self):
        packages = json.loads((ROOT / "metadata/protected_prior_identity_F15.json").read_text())
        checked = 0
        for package in packages:
            parent = ROOT.parent / package["folder"]
            if not parent.exists():
                parent = ROOT.parent / re.search(r"F\d+_A01", package["folder"])[0]
            for record in package["files"]:
                self.assertEqual(sha(parent / record["path"]), record["sha256"], record["path"])
                checked += 1
        self.assertEqual(checked, 597)

    def test_46_no_provider_payloads_or_credentials(self):
        token_patterns = [b"github" + b"_pat_", b"gh" + b"p_"]
        for path in ROOT.rglob("*"):
            if any(part in {".git", ".cache", "__pycache__"} for part in path.relative_to(ROOT).parts):
                continue
            if path.is_file():
                self.assertNotIn(path.suffix, {".zip", ".dbf", ".shp", ".tif", ".nc", ".nc4"})
                if path.stat().st_size < 2_000_000:
                    content = path.read_bytes()
                    for pattern in token_patterns:
                        self.assertNotIn(pattern, content)

    def test_47_disclosures_and_provider_request_complete(self):
        revision = (ROOT / "REVISION_AND_MIGRATION_ACCOUNT_F16_A01.md").read_text()
        access = (ROOT / "ACCESS_AND_EVIDENCE_WORKAROUNDS_F16_A01.md").read_text()
        self.assertIn("No files were deleted", revision)
        self.assertIn("250 → 243", revision)
        for phrase in ["CAM_FRL_FINALE_CalculationTool_02Jan2026", "CAM_FRL_CalculationTool_MonteCarlo_02jan2026", "contacts@minepded.gov.cm", "info@rainforestcoalition.org", "6,160"]:
            self.assertIn(phrase, access)

    def test_48_QA_and_visual_review_ready(self):
        qa = json.loads((ROOT / "metadata/deliverable_QA_F16.json").read_text())
        self.assertEqual((qa["main_figures"], qa["main_tables"], qa["SI_figures"], qa["SI_tables"]), (7, 2, 2, 28))
        self.assertEqual((qa["main"]["pages"], qa["SI"]["pages"]), (18, 27))
        self.assertTrue(qa["main"]["all_fonts_embedded"] and qa["SI"]["all_fonts_embedded"])
        self.assertFalse(qa["main"]["text_outside_page_bounds"] or qa["SI"]["text_outside_page_bounds"])
        self.assertEqual(qa["abstract_whitespace_words"], 243)


if __name__ == "__main__":
    unittest.main(verbosity=2)
