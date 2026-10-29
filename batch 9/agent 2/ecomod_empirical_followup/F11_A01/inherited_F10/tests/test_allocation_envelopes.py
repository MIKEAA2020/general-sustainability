import unittest,sys,json,csv,hashlib,itertools
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from allocation_envelopes import axis_membership,certificates,envelope,difference_interval,ROOT

class AllocationTests(unittest.TestCase):
    def test_axis_identity(self):np.testing.assert_array_equal(axis_membership([0,1,2],[0,1,2]).toarray(),np.eye(2,dtype=int))
    def test_touching_edge_not_positive_area(self):np.testing.assert_array_equal(axis_membership([0,1],[0,1,2]).toarray(),[[1,0]])
    def test_tiny_positive_overlap_not_thresholded_away(self):np.testing.assert_array_equal(axis_membership([0,1],[0,1-1e-12,2]).toarray(),[[1,1]])
    def test_integer_certificate_counts(self):
        x=axis_membership([0,2],[0,1,2]);c,n=certificates(x,x,[[1,0],[0,1]]);self.assertEqual(c.item(),2);self.assertEqual(n.item(),4)
    def test_pure_cell_fixes_its_entire_mass(self):self.assertEqual(envelope([10],np.array([4]),np.array([4]))['lower_Mg'],10)
    def test_absent_group_receives_no_mass(self):
        d=envelope([10],np.array([0]),np.array([4]));self.assertEqual((d['lower_Mg'],d['upper_Mg']),(0,0))
    def test_mixed_fraction_does_not_supply_allocation(self):
        for count in [1,99]:
            d=envelope([10],np.array([count]),np.array([100]));self.assertEqual((d['lower_Mg'],d['upper_Mg']),(0,10))
    def test_lower_upper_attainable_in_minimal_model(self):
        q=np.array([10.,20.,30.,40.]);c=np.array([4,1,3,0]);n=np.array([4,4,4,4]);d=envelope(q,c,n);sums=[10+20*a+30*b for a,b in itertools.product([0,1],repeat=2)];self.assertEqual(d['lower_Mg'],min(sums));self.assertEqual(d['upper_Mg'],max(sums))
    def test_negative_mass_rejected(self):
        with self.assertRaises(ValueError):envelope([-1],np.array([1]),np.array([1]))
    def test_nonfinite_mass_rejected(self):
        with self.assertRaises(ValueError):envelope([np.nan],np.array([1]),np.array([1]))
    def test_shapes_must_match(self):
        with self.assertRaises(ValueError):envelope([1,2],np.array([1]),np.array([1]))
    def test_fractional_topology_not_accepted(self):
        with self.assertRaises(ValueError):envelope([1],np.array([.99999]),np.array([1]))
    def test_invalid_integer_count_rejected(self):
        with self.assertRaises(ValueError):envelope([1],np.array([5]),np.array([4]))
    def test_interval_difference_is_not_difference_of_matched_endpoints(self):
        d=difference_interval({'lower_Mg':10,'upper_Mg':30},{'lower_Mg':20,'upper_Mg':50});self.assertEqual((d['lower_change_Mg'],d['upper_change_Mg']),(-10,40));self.assertTrue(d['contains_zero'])
    def test_zero_density_does_not_change_class_certificate(self):
        d=envelope([0],np.array([1]),np.array([4]));self.assertEqual(d['present_cells'],1);self.assertEqual((d['lower_Mg'],d['upper_Mg']),(0,0))
    def test_all_target_cells_retained(self):
        with (ROOT/'data/allocation/endpoint_envelopes_F07.csv').open()as f:rows=list(csv.DictReader(f))
        for r in rows:self.assertEqual(int(r['pure_cells'])+int(r['mixed_cells'])+int(r['absent_cells']),65536)
    def test_actual_difference_sets_both_contain_zero(self):
        with (ROOT/'data/allocation/difference_envelopes_F07.csv').open()as f:rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),2)
        for r in rows:self.assertLess(float(r['lower_change_Mg']),0);self.assertGreater(float(r['upper_change_Mg']),0)
    def test_frozen_rule_and_no_confidence_claim(self):
        f=json.loads((ROOT/'metadata/allocation/freeze_F07.json').read_text());self.assertEqual(hashlib.sha256((ROOT/'protocol/ALLOCATION_ENVELOPE_F07.md').read_bytes()).hexdigest(),f['protocol_sha256']);d=json.loads((ROOT/'configs/allocation_F07.json').read_text());self.assertFalse(d['confidence_interval']);self.assertFalse(d['national_inference'])
    def test_xlsx_metadata_does_not_claim_worksheet_audit(self):
        d=json.loads((ROOT/'metadata/reference/xlsx_metadata_F07.json').read_text());self.assertFalse(d['full_workbook_audited']);self.assertFalse(d['whole_file_downloaded']);self.assertLess(d['distinct_source_bytes'],2_000_000);self.assertTrue(d['worksheet_exceeds_250MB_member_cap']);self.assertEqual(set(d['fully_read_metadata_members']),{'xl/workbook.xml','xl/sharedStrings.xml'})
    def test_integer_certificates_match_inherited_support_counts(self):
        d=np.load(ROOT/'data/allocation/overlap_certificates_F07.npz');old=json.loads((ROOT/'data/brazil/common_support_summary.json').read_text())
        for y in [2015,2023]:
            c=d[f'forest_formations_intersections_{y}'];n=d[f'total_intersections_{y}'];self.assertEqual(int(((c>0)&(c<n)).sum()),old[f'mixed_formation_cells_{y}'])

if __name__=='__main__':unittest.main()
