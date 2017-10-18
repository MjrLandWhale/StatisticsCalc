import math


class PermutationCalc(object):
    def calc_permutation(self, number_of_objects, objects_chosen):
        if number_of_objects < objects_chosen:
            print 'objects_chosen cannot be larger than number_of_objects'
            return
        try:
            return (math.factorial(number_of_objects))/(math.factorial(number_of_objects - objects_chosen))
        except:
            print 'An error occurred. Only enter numbers.'

perm = PermutationCalc()
print perm.calc_permutation(19, 18)
