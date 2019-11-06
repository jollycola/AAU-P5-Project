import unittest

import computervision.imagecal.distance_calc as distCalc
import computervision.imagecal.direction_calc as dirCalc


class Test(unittest.TestCase):
    def setUp(self):
        self.coords = [[1215, 1363], [1261, 1363], [1215, 1750], [1263, 1749]]

    def test_distance(self):
        self.assertAlmostEqual(distCalc.calculate_distance(self.coords), 702.1870, delta=0.0001)

    def test_direction(self):
        self.assertAlmostEqual(dirCalc.calculate_direction(self.coords), -7.6232, delta=0.0001)


if __name__ == '__main__':
    unittest.main() 
