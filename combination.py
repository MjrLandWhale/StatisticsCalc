import math


class CombinationCalc(object):
    def calc_combination(self, number_of_objects, objects_chosen):
        if number_of_objects < objects_chosen:
            print 'objects_chosen cannot be larger than number_of_objects'
            return
        try:
            return (math.factorial(number_of_objects))/((math.factorial(number_of_objects - objects_chosen)) * (math.factorial(objects_chosen)))
        except:
            print 'An error occurred. Only enter numbers.'

#comb = CombinationCalc()
#print comb.calc_combination(20.0, 180.0)