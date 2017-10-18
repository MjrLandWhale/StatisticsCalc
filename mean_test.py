import unittest
from mean import MeanCalc


class MeanTest(unittest.TestCase):
    def test_calculate_mean_of_empty_list(self):
        mean_calc = MeanCalc()
        self.assertIsNone(MeanCalc.calculate_mean(mean_calc, []))

    def test_calculate_mean_of_single_value_list(self):
        mean_calc = MeanCalc()

        num_list = [10]
        expected = 10
        actual = MeanCalc.calculate_mean(mean_calc, num_list)
        self.assertEqual(expected,actual, "Mean([10]) = 10")

    def test_calculate_mean_of_multi_value_list(self):
        mean_calc = MeanCalc()

        num_list = [10,15,11,5,17]
        expected = 11.6
        actual = MeanCalc.calculate_mean(mean_calc, num_list)
        self.assertAlmostEqual(expected, actual,3, "Mean([10,15,11,5,17]) = 11.6")