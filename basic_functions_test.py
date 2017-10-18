import unittest
from basic_functions import MyMath

class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_nums_and_correctly_report_sum(self):
        math = MyMath()
        input_a = 4
        input_b = 6
        expected_output = 10
        actual_output = MyMath.add(math, input_a, input_b)
        self.assertEqual(expected_output, actual_output, '%d + %d = %d' % (input_a, input_b, actual_output))


if __name__ == '__main__':
    unittest.main()
