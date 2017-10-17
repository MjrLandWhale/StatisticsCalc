

class mean(object):

    def calculate_mean(self, list):
        mean = 0

        #Attempt calculating mean
        try:
            #when given a null set, return null
            if len(list) is 0:
                return None

            #when given a single value, the mean is that value
            elif len(list) is 1:
                return list[0]

            #when given a set of values, calculate the mean
            else:
                sum = 0
                #calculate sum of set
                for i in list:
                    sum += i

                #divide by number of values to get mean
                mean = round( float(sum) / len(list), 3)
                return mean



        except:
            print "an error has occurred"