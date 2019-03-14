import unittest

import calc_volumes

class testVolumeCalculation(unittest.TestCase):

    def test_with_missing_data(self):
        out = calc_volumes.calcVolumes([0,1,2], [{'SEGMENT':2, '0':3, '1':6,'2':6 }], 0.5, 1)
        self.assertEqual(out, [{'SEGMENT': 2, 'data': [7.5, 4.5, 4.5, 1.5, 1.5]}])

    def test_with_all_data(self):
        out = calc_volumes.calcVolumes([0,1,2], [{'SEGMENT':2, '0':3, '1':6,'2':6 }], 1, 1)
        self.assertEqual(out, [{'SEGMENT': 2, 'data': [15, 9, 3]}])

if __name__ == '__main__':
    unittest.main()