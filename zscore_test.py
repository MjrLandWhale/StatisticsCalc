import unittest
from zscore import Zscore

class Test(unittest.TestCase):

    #general test
    def test_zscore(self):
        zscore = Zscore()

        raw_score = 6
        population_mean = 4.4
        standard_deviation = 2.2
        expected_output = 0.7273
        actual_output = Zscore.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'General case failed')

    #negative tests
    def test_zscore2(self):
        zscore = Zscore()

        raw_score = -9.9
        population_mean = 3.45
        standard_deviation = 1.587
        expected_output = -8.4121
        actual_output = Zscore.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'Negative test 1 failed')

    def test_zscore3(self):
        zscore = Zscore()

        raw_score = 9.9
        population_mean = -3.45
        standard_deviation = 1.587
        expected_output = 8.4121
        actual_output = Zscore.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'Negative test 2 failed')

    def test_zscore4(self):
        zscore = Zscore()

        raw_score = -9.9
        population_mean = -3.45
        standard_deviation = 1.587
        expected_output = -4.0643
        actual_output = Zscore.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'Negative test 3 failed')

    #standard deviation conditional test
    def test_zscore5(self):
        zscore = Zscore()

        raw_score = 9.9
        population_mean = -3.45
        standard_deviation = 0
        expected_output = None
        actual_output = Zscore.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'Standard deviation conditional failed')

    #nonsense input
    def test_zscore6(self):
        zscore = Zscore()

        raw_score = 9.9
        population_mean = -3.45
        standard_deviation = 'crash bandicoot'
        expected_output = None
        actual_output = Zscore.calc_zscore(zscore, raw_score, population_mean, standard_deviation)
        self.assertEqual(expected_output, actual_output, 'Input check failed')

if __name__ == '__main__':
    unittest.main()
