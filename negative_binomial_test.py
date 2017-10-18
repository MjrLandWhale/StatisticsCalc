import unittest
from negative_binomial import NegativeBinomialDist


class NegativeBinomialTest(unittest.TestCase):
    # negative number tests
    def test_neg_binomial(self):
        neg_binomial = NegativeBinomialDist()

        failures = -5
        successes = 3
        success_prob = 0.6
        expected_output = None
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_neg_binomial2(self):
        neg_binomial = NegativeBinomialDist()

        failures = 5
        successes = -3
        success_prob = 0.6
        expected_output = None
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_neg_binomial3(self):
        neg_binomial = NegativeBinomialDist()

        failures = 5
        successes = 3
        success_prob = -0.6
        expected_output = None
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_neg_binomial4(self):
        neg_binomial = NegativeBinomialDist()

        failures = -5
        successes = -3
        success_prob = 0.6
        expected_output = None
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_neg_binomial5(self):
        neg_binomial = NegativeBinomialDist()

        failures = -5
        successes = 3
        success_prob = -0.6
        expected_output = None
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_neg_binomial6(self):
        neg_binomial = NegativeBinomialDist()

        failures = 5
        successes = -3
        success_prob = -0.6
        expected_output = None
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    def test_neg_binomial7(self):
        neg_binomial = NegativeBinomialDist()

        failures = -5
        successes = -3
        success_prob = -0.6
        expected_output = None
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Negative test failed')

    # zero for success test
    def test_neg_binomial8(self):
        neg_binomial = NegativeBinomialDist()

        failures = 7
        successes = 0
        success_prob = 0.35
        expected_output = None
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Zero success test failed')

    # zero for success_prob test
    def test_neg_binomial9(self):
        neg_binomial = NegativeBinomialDist()

        failures = 7
        successes = 2
        success_prob = 0
        expected_output = None
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Zero success_prob test failed')

    # both successes and success_prob zero test
    def test_neg_binomial10(self):
        neg_binomial = NegativeBinomialDist()

        failures = 7
        successes = 0
        success_prob = 0
        expected_output = None
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Zero success_prob and successes test failed')

    # zero failures
    def test_neg_binomial11(self):
        neg_binomial = NegativeBinomialDist()

        failures = 0
        successes = 6
        success_prob = 0.7
        expected_output = 0.1176
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Zero failures test failed')

    # general test
    def test_neg_binomial12(self):
        neg_binomial = NegativeBinomialDist()

        failures = 10
        successes = 5
        success_prob = 0.2
        expected_output = 0.0344
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'General test failed')

    # nonsense test
    def test_neg_binomial13(self):
        neg_binomial = NegativeBinomialDist()

        failures = 10
        successes = 'bilbo baggins'
        success_prob = 0.2
        expected_output = None
        actual_output = NegativeBinomialDist.neg_binomial_calc(neg_binomial, success_prob, failures, successes)
        self.assertEqual(expected_output, actual_output, 'Nonsense test failed')


if __name__ == '__main__':
    unittest.main()
