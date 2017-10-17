import math

class PermutationCalc(object):
    def calc_permutation(self, number_of_objects, objects_chosen):
        try:
            return (math.factorial(number_of_objects))/(math.factorial(number_of_objects - objects_chosen))
        except:
            print 'An error occured. Only enter numbers.'

#perm = PermutationCalc()
#print perm.calc_permutation(16, 18)
