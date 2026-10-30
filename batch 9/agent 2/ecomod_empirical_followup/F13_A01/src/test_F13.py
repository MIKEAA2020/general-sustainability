#!/usr/bin/env python3
import json,sys,unittest
from pathlib import Path
import pandas as pd
from analyze_sources_F13 import ROOT,france,source,french_band,parse_french_workbook,require
class AnalysisTests(unittest.TestCase):
 def setUp(self):
  self.s=json.loads((ROOT/'data/source_analysis_summary_F13.json').read_text())
 def test_01_primary_holds(self):self.assertEqual(self.s['original_primary_AGB_admissions'],0)
 def test_02_historic_country_not_ile_de_france(self):
  x=pd.read_csv(ROOT/'data/FRA_inventory_endpoints_F13.csv');self.assertEqual(x.iloc[0].volume_Mm3,2716)
 def test_03_historic_CI(self):
  x=pd.read_csv(ROOT/'data/FRA_inventory_endpoints_F13.csv');self.assertEqual(x.iloc[0].halfwidth95_Mm3,45)
 def test_04_french_delta(self):self.assertEqual(self.s['france_longest_cycle_delta_Mm3'],200)
 def test_05_union_coverage(self):self.assertEqual(self.s['france_longest_cycle_union90'],[104,296])
 def test_06_conditional_normal(self):
  lo,hi=self.s['france_longest_cycle_normal95'];self.assertTrue(90<lo<91 and 309<hi<310)
 def test_07_family_band(self):
  x=pd.read_csv(ROOT/'data/FRA_volume_change_bounds_F13.csv');r=x[(x.initial_cycle=='2013-2017')&(x.endpoint_family==4)].iloc[0];self.assertTrue(78<r.lower_Mm3<79)
 def test_08_latest_overlap_unresolved(self):
  b=french_band(2827,46,2916,47);self.assertLess(b['lower_Mm3'],0)
 def test_09_bonferroni_not_independence(self):
  b=french_band(2716,45,2916,47,mode='normal95');self.assertGreater(b['CI_rescaling_factor'],1)
 def test_10_rounding_conservative(self):
  a=french_band(2716,45,2916,47,round_unit=0);b=french_band(2716,45,2916,47);self.assertGreater(a['lower_Mm3'],b['lower_Mm3'])
 def test_11_negative_CI_rejected(self):
  with self.assertRaises(ValueError):french_band(1,-1,2,1)
 def test_12_nonfinite_rejected(self):
  with self.assertRaises(ValueError):french_band(float('nan'),1,2,1)
 def test_13_bad_mode_rejected(self):
  with self.assertRaises(ValueError):french_band(1,1,2,1,mode='independent95')
 def test_14_xlsx_reset(self):
  r=parse_french_workbook('FRA_2021_2025_national.zip');self.assertEqual(r['actual_columns'],7);self.assertEqual(r['volume_Mm3'],2916);self.assertTrue(r['reset_dimensions_applied'])
 def test_15_canada_total(self):self.assertEqual(self.s['canada_annual_change_total']['estimate'],17.639)
 def test_16_canada_interval_unresolved(self):
  r=self.s['canada_annual_change_total'];self.assertLess(r['outward_interval_lower'],0);self.assertGreater(r['outward_interval_upper'],0)
 def test_17_canada_RSE_not_naively_used(self):self.assertGreater(self.s['canada_annual_change_total']['CI_to_usual_RSE_SE_ratio'],100)
 def test_18_canada_confidence_not_invented(self):self.assertFalse(self.s['canada_annual_change_total']['confidence_level_for_current_change_export_independently_established'])
 def test_19_canada_geographic_hold(self):
  r=json.loads((ROOT/'data/CAN_NFI_scope_audit_F13.json').read_text());self.assertEqual(r['not_inventoried_area_thousand_ha'],262189.89);self.assertFalse(r['pure_paired_field_census'])
 def test_20_canada_all_groups(self):
  d=pd.read_csv(ROOT/'data/CAN_NFI_biomass_intervals_F13.csv');self.assertEqual(len(d),10);self.assertEqual(set(d.forest_type),{'Subtotal','Treed Coniferous','Treed Mixedwood','Non-treed','Treed Broadleaf'})
 def test_21_canada_totals(self):
  r=json.loads((ROOT/'data/CAN_NFI_scope_audit_F13.json').read_text());self.assertTrue(all(x['within_CSV_rounding']for x in r['totals_checks']))
 def test_22_COD_national_forest(self):
  r=next(r for r in self.s['congo_country_changes']if r['group']=='source_forest_group');self.assertAlmostEqual(r['delta_ha'],-3303015.65,places=5)
 def test_23_COD_class_mapping(self):
  d=pd.read_csv(ROOT/'data/COD_C1_class_crosswalk_F13.csv');self.assertIn('claire',d[d.class_id==4].iloc[0].class_level2)
 def test_24_COD_extent_not_AGB(self):
  r=json.loads((ROOT/'data/COD_C1_interpretation_F13.json').read_text());self.assertFalse(r['original_primary_AGB_admission']);self.assertTrue(r['no_biomass_change_or_conversion_causality_inferred'])
 def test_25_COD_complete_years(self):
  d=pd.read_csv(ROOT/'data/COD_C1_extent_annual_F13.csv');self.assertEqual(set(d.year),set(range(2000,2026)))
 def test_26_COD_subunit_nonclosure_retained(self):
  d=pd.read_csv(ROOT/'data/COD_C1_subunit_footprint_differences_F13.csv');self.assertGreater(d[d.level=='province'].national_minus_subunit_total_ha.min(),39000)
 def test_27_COD_error_threshold_not_CI(self):
  r=next(r for r in self.s['congo_country_changes']if r['group']=='source_forest_group');self.assertAlmostEqual(r['symmetric_endpoint_net_area_error_sign_threshold_ha'],1651507.825,places=5)
 def test_28_france_bias_unbounded(self):
  d=json.loads((ROOT/'data/FRA_scope_and_bias_F13.json').read_text());self.assertTrue(d['unknown_differential_method_bias_not_bounded']);self.assertTrue(d['retrospective_cubage_and_rebut_harmonization_not_certified'])
 def test_29_source_integrity(self):self.assertTrue(source('COD_C1_wide_csv.zip').exists())
 def test_30_require_not_disabled_by_optimization(self):
  with self.assertRaises(ValueError):require(False,'must fail')
if __name__=='__main__':unittest.main(verbosity=2)
