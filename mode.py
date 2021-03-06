class ModeCalc(object):
    def calculate_mode(self, lst):
        mode = []
        max_count = 0

        # finds the maximum occurrence of repeated numbers in the list
        for i in range(len(lst)):
            count = lst.count(lst[i])
            if count > max_count:
                max_count = count

        # finds all numbers that occur as many times as the max occurrence
        for i in range(len(lst)):
            if lst.count(lst[i]) == max_count:
                mode.append(lst[i])

        return list(set(mode))



#lst = [3,3,3,1,1,2,4,5,1]
#mode = ModeCalc()
#print mode.calculate_mode(lst)

