import unittest
from zscore import ZscoreCalc


class ZscoreTest(unittest.TestCase):
    # general test
    def test_zscore(self):
        zscore = ZscoreCalc()

        raw_score = 6
        population_mean = 4.4
        standard_deviation = 2.2
        expected_output = 0.7273
        actual_output = ZscoreCalc.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'General case failed')

    # negative tests
    def test_zscore2(self):
        zscore = ZscoreCalc()

        raw_score = -9.9
        population_mean = 3.45
        standard_deviation = 1.587
        expected_output = -8.4121
        actual_output = ZscoreCalc.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'Negative test 1 failed')

    def test_zscore3(self):
        zscore = ZscoreCalc()

        raw_score = 9.9
        population_mean = -3.45
        standard_deviation = 1.587
        expected_output = 8.4121
        actual_output = ZscoreCalc.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'Negative test 2 failed')

    def test_zscore4(self):
        zscore = ZscoreCalc()

        raw_score = -9.9
        population_mean = -3.45
        standard_deviation = 1.587
        expected_output = -4.0643
        actual_output = ZscoreCalc.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'Negative test 3 failed')

    # standard deviation conditional test
    def test_zscore5(self):
        zscore = ZscoreCalc()

        raw_score = 9.9
        population_mean = -3.45
        standard_deviation = 0
        expected_output = None
        actual_output = ZscoreCalc.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'Standard deviation conditional failed')

    # nonsense input
    def test_zscore6(self):
        zscore = ZscoreCalc()

        raw_score = 9.9
        population_mean = -3.45
        standard_deviation = 'crash bandicoot'
        expected_output = None
        actual_output = ZscoreCalc.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'Input check failed')

    # test calculating zscore from a list
    def test_zscore7(self):
        zscore = ZscoreCalc()

        raw_score = 12.67
        lst = [4, 7.4, 3.2, 6, 5.321, 8, 1]
        expected_output = 3.1313
        actual_output = ZscoreCalc.calc_zscore_from_list(zscore, raw_score, lst)
        self.assertEqual(expected_output, actual_output, 'Zscore from list test failed')

    # nonsense entered into calculate zscore from list test
    def test_zscore8(self):
        zscore = ZscoreCalc()

        raw_score = 12.67
        lst = 'rubber duck'
        expected_output = None
        actual_output = ZscoreCalc.calc_zscore_from_list(zscore, raw_score, lst)
        self.assertEqual(expected_output, actual_output, 'Nonsense test failed')


if __name__ == '__main__':
    unittest.main()
