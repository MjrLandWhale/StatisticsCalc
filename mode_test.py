import unittest
from mode import ModeCalc


# test where mode is a single number
class ModeTest(unittest.TestCase):
    def test_mode(self):
        mode = ModeCalc()

        input1 = [4, 3, 2, 3, 2, 3]
        expected_output1 = [3]
        actual_output1 = ModeCalc.calculate_mode(mode, input1)
        self.assertEqual(expected_output1, actual_output1, 'mode = 3')

    # test where mode is two numbers
    def test_mode2(self):
        mode = ModeCalc()

        input2 = [2, 3, 4, 1, 6, 4, 7, 2]
        expected_output2 = [2, 4]
        actual_output2 = ModeCalc.calculate_mode(mode, input2)
        self.assertEqual(expected_output2, actual_output2, 'mode = 2, 4')

    # test where mode is three numbers
    def test_mode3(self):
        mode = ModeCalc()

        input3 = [2, 3, 4, 1, 6, 4, 7, 2, 9, 1]
        expected_output3 = [1, 2, 4]
        actual_output3 = ModeCalc.calculate_mode(mode, input3)
        self.assertEqual(expected_output3, actual_output3, 'mode = 1, 2, 4')

    # test where all numbers occur once
    def test_mode4(self):
        mode = ModeCalc()

        input4 = [1, 2, 3, 4]
        expected_output4 = [1, 2, 3, 4]
        actual_output4 = ModeCalc.calculate_mode(mode, input4)
        self.assertEqual(expected_output4, actual_output4, 'mode = 1, 2, 3, 4')

    # test will there is only one number
    def test_mode5(self):
        mode = ModeCalc()

        input5 = [2]
        expected_output5 = [2]
        actual_output5 = ModeCalc.calculate_mode(mode, input5)
        self.assertEqual(expected_output5, actual_output5, 'mode = 2')


if __name__ == '__main__':
    unittest.main()
