"""Independent optimization checks for the coherent three-component set."""
import csv
import hashlib
import json
from pathlib import Path
import sys
import unittest
import numpy as np
from scipy.optimize import linprog

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from joint_identification_F11 import polygon_vertices, pattern_masses, problem, joint_witness

class JointIdentificationTests(unittest.TestCase):
    def test_pattern_partition_preserves_mass(self):
        q=np.array([[1.,2.],[3.,4.]])
        ca=np.array([[2,1],[0,0]]);ch=np.array([[2,2],[2,0]]);n=np.full((2,2),2)
        mass,codes=pattern_masses(q,ca,ch,n)
        self.assertEqual(mass.sum(),10.)
        np.testing.assert_array_equal(codes,[[1,3],[2,4]])
    def test_nonnested_groups_rejected(self):
        with self.assertRaises(ValueError):pattern_masses(np.ones((1,1)),np.array([[2]]),np.array([[1]]),np.array([[2]]))
    def test_all_mixed_components_have_all_sign_quadrants(self):
        m0=np.array([0.,0,0,0,0,0,10.]);m1=np.array([0.,0,0,0,0,0,12.])
        for sa in (-1,1):
            for sh in (-1,1):
                x,r=joint_witness(m0,m1,sa,sh)
                self.assertGreater(r['maximized_common_signed_margin_Mg'],0)
                self.assertGreater(sa*r['formations_difference_Mg'],0)
                self.assertGreater(sh*r['formations_plus_savanna_difference_Mg'],0)
    def test_polygon_enforces_added_component_not_just_marginals(self):
        v,m,b=polygon_vertices((-10,12),(-10,12),(-10,12))
        self.assertEqual(len(v),6)
        self.assertFalse(np.all(m@np.array([12.,-10.])<=b))
        self.assertTrue(np.all(m@np.array([1.,-1.])<=b))
    def test_random_joint_polygon_against_full_pattern_LP(self):
        rng=np.random.default_rng(78123)
        patterns=np.arange(1,8)
        def endpoint(m):
            return dict(A=(m[0],m[(patterns&1)>0].sum()),
                        H=(m[(patterns&4)==0].sum(),m[(patterns&3)>0].sum()),
                        S=(m[1],m[(patterns&2)>0].sum()))
        for repeat in range(12):
            m0=rng.uniform(.01,100,7);m1=rng.uniform(.01,100,7)
            e0,e1=endpoint(m0),endpoint(m1)
            d={k:(e1[k][0]-e0[k][1],e1[k][1]-e0[k][0])for k in e0}
            v,_,_=polygon_vertices(d['A'],d['H'],d['S'])
            eq,b,bounds,da,dh=problem(m0,m1)
            for angle in np.linspace(0,2*np.pi,17):
                u=np.array([np.cos(angle),np.sin(angle)])
                r=linprog(-u[0]*da-u[1]*dh,A_eq=eq,b_eq=b,bounds=bounds,method='highs')
                self.assertTrue(r.success);self.assertAlmostEqual(-r.fun,(v@u).max(),places=7)
    def test_observed_joint_polygon_has_six_vertices(self):
        d=json.loads((ROOT/'metadata/joint_identification_F11.json').read_text())
        self.assertEqual(d['polygon_vertices'],6)
        self.assertTrue(d['all_four_strict_sign_quadrants_feasible'])
        self.assertFalse(d['joint_allocation_validated_as_ecological_change'])
        self.assertLess(d['worst_support_function_LP_discrepancy_Mg'],1e-6)
    def test_observed_joint_witnesses_reconstruct_cell_mass(self):
        with (ROOT/'data/joint_quadrant_certificates_F11.csv').open()as f:r=list(csv.DictReader(f))
        self.assertEqual(len(r),4)
        for x in r:
            self.assertGreater(float(x['maximized_common_signed_margin_Mg']),100000)
            self.assertLess(float(x['cell_mass_preservation_residual_Mg']),1e-8)
            self.assertEqual(x['native_cell_totals_and_nested_geometry_preserved'],'True')
    def test_pattern_cells_cover_both_complete_endpoints(self):
        with (ROOT/'data/joint_availability_patterns_F11.csv').open()as f:r=list(csv.DictReader(f))
        self.assertEqual(len(r),14)
        for year in ('2015','2023'):
            self.assertEqual(sum(int(x['native_cells'])for x in r if x['year']==year),65536)
    def test_all_218_inherited_files_exact(self):
        m=json.loads((ROOT/'metadata/inherited_F10_identity_F11.json').read_text())
        self.assertEqual(len(m['files']),218)
        for x in m['files']:
            b=(ROOT/'inherited_F10'/x['path']).read_bytes()
            self.assertEqual(hashlib.sha256(b).hexdigest(),x['sha256'],x['path'])
    def test_eleven_independently_reproduced_outputs_match(self):
        m=json.loads((ROOT/'metadata/source_reproduction_comparison_F11.json').read_text())
        self.assertEqual(len(m['files']),11)
        self.assertTrue(all(x['exact_bytes_match']and x['inherited_sha256']==x['fresh_sha256'] for x in m['files']))
    def test_prior_fourteen_workflow_creations_already_remote(self):
        m=json.loads((ROOT/'metadata/prior_R02_remote_confirmation_F11.json').read_text())
        self.assertEqual(len(m['files']),14)
        self.assertTrue(m['all_previous_creations_already_published'])
        self.assertTrue(all(x['remote_paths']for x in m['files']))

if __name__=='__main__':unittest.main()
