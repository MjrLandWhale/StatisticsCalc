import unittest
from binomial import BinomialCalc


class Test(unittest.TestCase):

    # makes sure the success are not more than the number of trials
    def test_binomial(self):
        binomial = BinomialCalc()

        trials = 5
        successes = 6
        success_prob = 0.4
        expected_output = None
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'Success conditional did not work')

    # general binomial experiment
    def test_binomial2(self):
        binomial = BinomialCalc()

        trials = 6
        successes = 3
        success_prob = 0.4
        expected_output = [0.2765, 0.5443, 0.8208, 0.1792, 0.4557]
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'General binomial experiment failed')

    # test for zero successes
    def test_binomial3(self):
        binomial = BinomialCalc()

        trials = 8
        successes = 0
        success_prob = 0.2
        expected_output = [0.1678, 0.0, 0.1678, 0.8322, 1.0]
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'Binomial experiment with zero successes failed')

    # test for all successes
    def test_binomial4(self):
        binomial = BinomialCalc()

        trials = 9
        successes = 9
        success_prob = 0.6
        expected_output = [0.0101, 0.9899, 1.0, 0.0, 0.0101]
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'Binomial experiment with zero successes failed')

    # negative tests
    def test_binomial5(self):
        binomial = BinomialCalc()

        trials = -9
        successes = 9
        success_prob = 0.6
        expected_output = None
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_binomial6(self):
        binomial = BinomialCalc()

        trials = 9
        successes = -9
        success_prob = 0.6
        expected_output = None
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_binomial7(self):
        binomial = BinomialCalc()

        trials = 9
        successes = 9
        success_prob = -0.6
        expected_output = None
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_binomial8(self):
        binomial = BinomialCalc()

        trials = -9
        successes = -9
        success_prob = 0.6
        expected_output = None
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_binomial9(self):
        binomial = BinomialCalc()

        trials = -9
        successes = 9
        success_prob = -0.6
        expected_output = None
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_binomial10(self):
        binomial = BinomialCalc()

        trials = 9
        successes = -9
        success_prob = -0.6
        expected_output = None
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_binomial11(self):
        binomial = BinomialCalc()

        trials = -9
        successes = -9
        success_prob = -0.6
        expected_output = None
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_binomial12(self):
        binomial = BinomialCalc()

        trials = -9
        successes = 4
        success_prob = 'donkey kong'
        expected_output = None
        actual_output = BinomialCalc.binomial_calc(binomial, success_prob, trials, successes)
        self.assertEqual(expected_output, actual_output, 'Nonsense test failed')


if __name__ == '__main__':
    unittest.main()
