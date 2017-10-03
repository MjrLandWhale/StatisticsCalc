import unittest
from permutation import PermutationCalc

#general permutation calculation
class Test1(unittest.TestCase):
    def test_permutation(self):
        permutation = PermutationCalc()

        number_of_objects = 7
        objects_chosen = 2
        expected_output = 42
        actual_output = PermutationCalc.calc_permutation(permutation, number_of_objects, objects_chosen)
        self.assertEqual(expected_output, actual_output, 'Permutation of 7 choose 2 is 42')

#one object is selected
class Test2(unittest.TestCase):
    def test_permutation2(self):
        permutation = PermutationCalc()

        number_of_objects = 11
        objects_chosen = 1
        expected_output = 11
        actual_output = PermutationCalc.calc_permutation(permutation, number_of_objects, objects_chosen)
        self.assertEqual(expected_output, actual_output, 'Permutation of 11 choose 1 is 11')

#all objects are selected
class Test3(unittest.TestCase):
    def test_permutation3(self):
        permutation = PermutationCalc()

        number_of_objects = 8
        objects_chosen = 8
        expected_output = 40320
        actual_output = PermutationCalc.calc_permutation(permutation, number_of_objects, objects_chosen)
        self.assertEqual(expected_output, actual_output, 'Permutation of 8 choose 8 is 40320')

#no object is selected
class Test4(unittest.TestCase):
    def test_permutation4(self):
        permutation = PermutationCalc()

        number_of_objects = 16
        objects_chosen = 0
        expected_output = 1
        actual_output = PermutationCalc.calc_permutation(permutation, number_of_objects, objects_chosen)
        self.assertEqual(expected_output, actual_output, 'Permutation of 16 choose 0 is 1')

if __name__ == '__main__':
    unittest.main()