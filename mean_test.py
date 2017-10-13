import unittest
from mean import mean

class test(unittest.TestCase):


    def test_calculate_mean_of_empty_list(self):
        mean_calc = mean()
        self.assertIsNone( mean.calculate_mean( mean_calc, [] ) )

    def test_calculate_mean_of_single_value_list(self):
        mean_calc = mean()

        list = [10]
        expected = 10
        actual = mean.calculate_mean(mean_calc, list)
        self.assertEqual(expected,actual, "Mean([10]) = 10")

    def test_calculate_mean_of_multi_value_list(self):
        mean_calc = mean()

        list = [10,15,11,5,17]
        expected = 11.6
        actual = mean.calculate_mean(mean_calc, list)
        self.assertAlmostEqual(expected, actual,3, "Mean([10,15,11,5,17]) = 11.6")