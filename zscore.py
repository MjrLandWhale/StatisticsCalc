from mean import mean
from standard_deviation import standard_deviation

class Zscore(object):
    #Use if mean and standard deviation are known
    def calc_zscore(self, raw_score, population_mean, standard_deviation):
        if standard_deviation <= 0:
            print 'Standard deviation cannot must be larger than zero.'
        else:
            try:
                return round((raw_score - population_mean) / float(standard_deviation), 4)
            except:
                print 'An error occurred. Make sure to enter only numbers for the parameters.'

    #Use if mean and standard deviation are unknown. Calculates from list
    def calc_zscore_from_list(self, raw_score, lst):
        mean_instance = mean()
        std_dev = standard_deviation()

        try:
            mean_value = mean_instance.calculate_mean(lst)
            std_value = std_dev.calculate_standard_deviation(lst)
            return round((raw_score - mean_value) / float(std_value), 4)
        except:
            print 'An error occurred. Make sure to enter only numbers for the parameters.'



#zscore = Zscore()
#print zscore.calc_zscore(4.56,-8.5454,2)