import math

class CombinationCalc(object):
    def calc_combination(self, number_of_objects, objects_chosen):
        return (math.factorial(number_of_objects))/((math.factorial(number_of_objects - objects_chosen)) * (math.factorial(objects_chosen)))

comb = CombinationCalc()
print comb.calc_combination(18, 9)