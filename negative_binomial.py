import math
from combination import CombinationCalc

#returns the probability of having a certain number of failures before you have a certain number of successes
class NegativeBinomialDist(object):
    def neg_binomial_calc(self, success_prob, failures, successes):
        comb = CombinationCalc()
        if success_prob < 0 or failures < 0 or successes < 0:
            return 'None of the numbers can be negative.'
        elif success_prob == 0 or successes == 0:
            return 'Successes and success_prob cannot be zero.'
        else:
            return round(comb.calc_combination(failures + successes - 1, successes - 1) * math.pow(success_prob, successes) * math.pow(1 - success_prob, failures), 4)

#neg = NegativeBinomialDist()
#print neg.neg_binomial_calc(0.7, 0, 6)