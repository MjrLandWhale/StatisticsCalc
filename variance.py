


#Variance for a discrete random variable
class variance(object):

    #This function will take in two lists, one being the
    def calculate_variance(self, variable_list, probability_list=None):

        #attempt to calculate variance
        try:

            #if true, dealing with single list of values
            if probability_list is None:

                #When presented a null set, spit back a null value
                if len(variable_list) == 0:
                    return None

                #When presented a 1 value set, the variance is 0
                elif len(variable_list) == 1:
                    return 0

                #When presented a multi value set, calculate the variance
                else:

                    #start by calculating mean of the set

                    # calculate sum of set
                    sum = 0
                    for i in variable_list:
                        sum += i

                    # divide by number of values to get mean
                    mean = float(sum) / len(variable_list)

                    #Iterate through set to get sum of square differences
                    sum_square_diff = 0

                    for i in variable_list:
                        sum_square_diff += pow(( i - mean ), 2)

                    #Divide by sample size -1 to get variance
                    variance = round(sum_square_diff / (len(variable_list ) - 1), 3)
                    return variance


            #Else dealing with a discrete random variable
            else:
                #Not yet implemented
                return None
    
        except:
            #Print a general error statement until more description is available
            print "an error has occurred"