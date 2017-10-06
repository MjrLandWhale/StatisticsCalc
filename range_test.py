import unittest
from range import RangeCalc


# test for range
class TestRange(unittest.TestCase):
	def test_range(self):
		range_num = RangeCalc()

		number_list = [10, 6, 4, 2, 4, 7] # list of numbers for test

		expected_output = 8 # expected output for number_list
		actual_output = RangeCalc.calculate_range(range_num, number_list) # calculated value for number_list

		self.assertEqual(expected_output, actual_output, 'range = %d' % actual_output)

if __name__ == '__main__':
	unittest.main()