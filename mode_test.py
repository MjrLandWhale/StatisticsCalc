import unittest
from mode import ModeCalc

class Test1(unittest.TestCase):
	def test_mode(self):
		mode = ModeCalc()
		input_a = [4, 3, 2, 3, 2, 3]
		expected_output = 3
		actual_output = ModeCalc.calculate_mode(mode, input_a)
		self.assertEqual(expected_output, actual_output, 'mode = %d' % (actual_output))

if __name__ == '__main__':
	unittest.main()