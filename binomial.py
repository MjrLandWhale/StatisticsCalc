import math
from combination import CombinationCalc

class BinomialDist(object):
    def binomial_calc(self, success_prob, trials, successes):
        result = []
        comb = CombinationCalc()
        if success_prob < 0 or trials < 0 or successes < 0:
            return 'None of the numbers can be negative.'
        elif successes > trials:
            return 'The number of success cannot be larger than the number of trials.'
        else:
            #X = number of successes
            equal = (comb.calc_combination(trials, successes)) * math.pow(success_prob,successes) * math.pow(1 - success_prob, trials - successes)
            result.append(equal)

            #X < number of success
            less = 0
            for i in range(successes):
                less += (comb.calc_combination(trials, i)) * math.pow(success_prob, i) * math.pow(1 - success_prob, trials - i)
            result.append(less)

            #X <= number of successes
            result.append(less + equal)

            #X > number of successes
            result.append(1 - (less + equal))

            #X >= number of sucesses
            result.append(equal + (1 - (less + equal)))

            #round all numbers to fourth decimal place
            for i in range(len(result)):
                result[i] = round(result[i], 4)

        return result

#bin = BinomialDist()
#print bin.binomial_calc(-0.6, -4, -9)