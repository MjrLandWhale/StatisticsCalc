import unittest
from median import MedianCalc


# test for range with list of numbers with odd list length
class TestMedianListOdd(unittest.TestCase):
	def test_median_list_odd(self):
		median = MedianCalc()

		odd_number_list = [6, 3, 2, 13, 1] # list of numbers for test (odd length)

		expected_output = 3 # expected output for number_list
		actual_output = MedianCalc.calculate_median(median, odd_number_list) # calculated value for number_list

		self.assertEqual(expected_output, actual_output, 'median = %d' % actual_output)

# test for range with list of numbers with odd list length
class TestMedianListEven(unittest.TestCase):
	def test_median_list_even(self):
		median = MedianCalc()

		even_number_list = [11, 4, 2, 10, 1, 2]  # list of numbers for test (even length)

		expected_output = 3  # expected output for number_list
		actual_output = MedianCalc.calculate_median(median, even_number_list)  # calculated value for number_list

		self.assertEqual(expected_output, actual_output, 'median = %d' % actual_output)

# test for range with one number in list
class TestMedianOneNum(unittest.TestCase):
	def test_median_one_num(self):
		median = MedianCalc()

		number_list = [5] # number_list for test (length = 1)

		expected_output = None # expected output for number_list
		actual_output = MedianCalc.calculate_median(median, number_list) # calculated value for number_list

		self.assertEqual(expected_output, actual_output, 'median = %s' % actual_output)

if __name__ == '__main__':
	unittest.main()