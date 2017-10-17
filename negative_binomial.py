import math
from combination import CombinationCalc

#returns the probability of having a certain number of failures before you have a certain number of successes
class NegativeBinomialDist(object):
    def neg_binomial_calc(self, success_prob, failures, successes):
        comb = CombinationCalc()
        if success_prob < 0 or failures < 0 or successes < 0:
            print 'None of the numbers can be negative.'
            return
        elif success_prob == 0 or successes == 0:
            print 'Successes and success_prob cannot be zero.'
            return
        else:
            try:
                return round(comb.calc_combination(failures + successes - 1, successes - 1) * math.pow(success_prob, successes) * math.pow(1 - success_prob, failures), 4)
            except:
                print 'An error occurred. Enter numbers for parameters.'

#neg = NegativeBinomialDist()
#print neg.neg_binomial_calc(0.7, 0, 6)