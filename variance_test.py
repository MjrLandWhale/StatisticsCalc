import unittest
from variance import variance

class test(unittest.TestCase):

#########SINGLE LIST VARIANCE TESTS##################

  #      @unittest.skip("Not yet Implemented")
        def test_calculate_variance_of_empty_list(self):

            variance_calc = variance()
            self.assertIsNone(variance.calculate_variance(variance_calc,[]),"Variance = None")

 #       @unittest.skip("Not yet Implemented")
        def test_calculate_variance_of_single_value_list(self):
            variance_calc = variance()

            variable_list = [12]
            expected = 0
            actual = variance.calculate_variance(variance_calc,variable_list)
            self.assertEqual(expected,actual,"variance( [12] ) = 0")

        def test_calculate_variance_of_multi_value_list(self):
            variance_calc = variance()

            variable_list = [12,15,75,18,52,18]
            expected = 665.867
            actual = variance.calculate_variance(variance_calc,variable_list)
            self.assertAlmostEqual(expected,actual,3,"variance( [12,15,75,18,52,18] ) = 665.867")


#########DISCRETE RANDOM VARIABLE VARIANCE TESTS##################

#All DRV tests are to be skipped until implementation inside calculate_variance function

        @unittest.skip("Not yet Implemented")
        def test_calculate_variance_of_DRV_empty_lists(self):
            variance_calc = variance()
            self.assertIsNone(variance.calculate_variance(variance_calc,[],[]),"Variance = None")

        @unittest.skip("Not yet Implemented")
        def test_calculate_variance_of_DRV_empty_variable_list(self):
            variance_calc = variance()

            variable_list = []
            probability_list = [0.2, 0.2, 0.1, 0.5]
            expected = "Error: list of random variables must not be empty"
            actual = variance.calculate_variance(variance_calc,variable_list,probability_list)
            self.assertEqual(expected,actual,"variance( [], [0.2, 0.2, 0.1, 0.5] ) = Error")

        @unittest.skip("Not yet Implemented")
        def test_calculate_variance_of_DRV_empty_probability_list(self):
            variance_calc = variance()

            variable_list = [1,2,3,4]
            probability_list = []
            expected = "Error: list of probabilities must not be empty"
            actual = variance.calculate_variance(variance_calc,variable_list, probability_list)
            self.assertEqual(expected, actual, "variance( [1,2,3,4], [] ) = Error")

        @unittest.skip("Not yet Implemented")
        def test_calculate_variance_of_DRV_probability_sum_greater_than_one(self):
            variance_calc = variance()

            variable_list = [1,2,3,4,5]
            probability_list = [0.2, .05, 0.1, 0.5, 0.2]
            expected = "Error: sum of probabilities must be equal to 1"
            actual = variance.calculate_variance(variance_calc,variable_list, probability_list)
            self.assertEqual(expected, actual, "variance( [1,2,3,4,5], [0.2, .05, 0.1, 0.5, 0.2] ) = Error")

        @unittest.skip("Not yet Implemented")
        def test_calculate_variance_of_DRV_probability_sum_less_than_one(self):
            variance_calc = variance()

            variable_list = [1,2,3,4]
            probability_list = [0.2, .05, 0.1, 0.5]
            expected = "Error: sum of probabilities must be equal to 1"
            actual = variance.calculate_variance(variance_calc,variable_list, probability_list)
            self.assertEqual(expected, actual, "variance( [1,2,3,4], [0.2, .05, 0.1, 0.5] ) = Error")

        @unittest.skip("Not yet Implemented")
        def test_calculate_variance_with_DRV_variable_probability_length_mismatch(self):
            variance_calc = variance()

            variable_list = [1,2,3,4,5]
            probability_list = [0.2, 0.1, 0.5, 0.2]
            expected = "Error: variable list must be same length as probability list"

            actual = variance.calculate_variance(variance_calc,variable_list, probability_list)
            self.assertEqual(expected, actual, "variance( [1,2,3,4,5], [0.2, 0.1, 0.5, 0.2] ) = Error")


            variable_list = [1,2,3,4]
            probability_list = [0.2, 0.1, 0.5, 0.15, 0.05]
            actual = variance.calculate_variance(variance_calc,variable_list, probability_list)
            self.assertEqual(expected, actual, "variance( [1,2,3,4], [0.2, 0.1, 0.5, 0.15, 0.05] ) = Error")

        @unittest.skip("Not yet Implemented")
        def test_calculate_variance_of_DRV_single_values(self):
            variance_calc = variance()

            variable_list = [1]
            probability_list = [1]
            expected = 0
            actual = variance.calculate_variance(variance_calc,variable_list,probability_list)
            self.assertEqual(expected,actual, "variance( [1], [1] ) = 0")

        @unittest.skip("Not yet Implemented")
        def test_calculate_variance_of_DRV_multiple_values(self):
            variance_calc = variance()

            variable_list = [1,2,3,4,5]
            probability_list = [0.1,0.2,0.3,0.15,0.25]
            expected = 0
            actual = variance.calculate_variance(variance_calc,variable_list,probability_list)
            self.assertEqual(expected,actual, "variance( [1,2,3,4,5], [0.1,0.2,0.3,0.15,0.25] ) = 0")









