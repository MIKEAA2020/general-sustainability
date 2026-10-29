import math,sys,unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from estimands import wgs84_rectangle_area_ha,extent_density_decomposition,spatial_cancellation

class TestGeometry(unittest.TestCase):
    def test_global_area(self):
        a=6378137.;f=1/298.257223563;e=math.sqrt(f*(2-f))
        analytic=2*math.pi*a*a*(1+(1-e*e)*math.atanh(e)/e)/1e4
        self.assertAlmostEqual(wgs84_rectangle_area_ha(-180,180,-90,90)/analytic,1.,places=14)
    def test_partition(self):
        part=sum(wgs84_rectangle_area_ha(-180,180,s,s+1)for s in range(-90,90))
        self.assertAlmostEqual(part/wgs84_rectangle_area_ha(-180,180,-90,90),1.,places=14)
    def test_latitude_not_equal_area(self):
        equator=wgs84_rectangle_area_ha(0,.5,0,.5);north=wgs84_rectangle_area_ha(0,.5,60,60.5)
        self.assertGreater(equator/north,1.9)
    def test_invalid_bounds(self):
        with self.assertRaises(ValueError):wgs84_rectangle_area_ha(175,-175,-1,1)

class TestDecomposition(unittest.TestCase):
    def test_pure_extent(self):
        r=extent_density_decomposition(10,8,100,80);self.assertEqual(r['extent_Mg'],-20);self.assertEqual(r['density_Mg'],0)
    def test_pure_density(self):
        r=extent_density_decomposition(10,10,100,80);self.assertEqual(r['extent_Mg'],0);self.assertEqual(r['density_Mg'],-20)
    def test_mixed(self):
        rng=np.random.default_rng(20261029)
        for _ in range(500):
            a0,a1=rng.uniform(1,1000,2);d0,d1=rng.uniform(0,500,2)
            r=extent_density_decomposition(a0,a1,a0*d0,a1*d1)
            self.assertAlmostEqual(r['extent_Mg']+r['density_Mg'],r['total_Mg'],places=8)
    def test_zero_area_rejection(self):
        with self.assertRaises(ValueError):extent_density_decomposition(0,10,0,100)

class TestCancellation(unittest.TestCase):
    def test_offsets_are_local_net_not_gross_flows(self):
        r=spatial_cancellation([10,-8,1]);self.assertEqual(r['net_Mg'],3);self.assertEqual(r['offset_Mg'],8)
        self.assertAlmostEqual(r['cancellation_fraction'],1-3/19)
    def test_one_direction(self):self.assertEqual(spatial_cancellation([1,2,3])['cancellation_fraction'],0)
    def test_zero_denominator_abstains(self):self.assertIsNone(spatial_cancellation([0,0])['cancellation_fraction'])
    def test_invalid_values(self):
        with self.assertRaises(ValueError):spatial_cancellation([float('nan')])
    def test_measurement_noise_cancellation(self):
        # A deterministic smoke test, not a calibrated false-positive experiment.
        x=np.random.default_rng(17).normal(0,1,1000)
        self.assertGreater(spatial_cancellation(x)['cancellation_fraction'],.8)

if __name__=='__main__':unittest.main()
