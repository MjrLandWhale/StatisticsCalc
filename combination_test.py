import unittest
from combination import CombinationCalc

class Test(unittest.TestCase):

    #general combination calculation
    def test_combination(self):
        combination = CombinationCalc()

        number_of_objects = 7
        objects_chosen = 2
        expected_output = 21
        actual_output = CombinationCalc.calc_combination(combination, number_of_objects, objects_chosen)
        self.assertEqual(expected_output, actual_output, 'Combination of 7 choose 2 is 42')

    #one object is chosen
    def test_combination2(self):
        combination = CombinationCalc()

        number_of_objects = 13
        objects_chosen = 1
        expected_output = 13
        actual_output = CombinationCalc.calc_combination(combination, number_of_objects, objects_chosen)
        self.assertEqual(expected_output, actual_output, 'Combination of 13 choose 1 is 13')

    #all objects are selected
    def test_combination3(self):
        combination = CombinationCalc()

        number_of_objects = 12
        objects_chosen = 12
        expected_output = 1
        actual_output = CombinationCalc.calc_combination(combination, number_of_objects, objects_chosen)
        self.assertEqual(expected_output, actual_output, 'Combination of 12 choose 12 is 1')

    #no objects are chosen
    def test_combination4(self):
        combination = CombinationCalc()

        number_of_objects = 18
        objects_chosen = 0
        expected_output = 1
        actual_output = CombinationCalc.calc_combination(combination, number_of_objects, objects_chosen)
        self.assertEqual(expected_output, actual_output, 'Combination of 18 choose 0 is 1')

    #objects chosen are larger than objects available
    def test_combination5(self):
        combination = CombinationCalc()

        number_of_objects = 18
        objects_chosen = 20
        expected_output = None
        actual_output = CombinationCalc.calc_combination(combination, number_of_objects, objects_chosen)
        self.assertEqual(expected_output, actual_output, 'Chosen larger than available test failed')

    #nonsense test
    def test_combination6(self):
        combination = CombinationCalc()

        number_of_objects = 'waluigi'
        objects_chosen = 0
        expected_output = None
        actual_output = CombinationCalc.calc_combination(combination, number_of_objects, objects_chosen)
        self.assertEqual(expected_output, actual_output, 'Nonsense test failed')

if __name__ == '__main__':
    unittest.main()