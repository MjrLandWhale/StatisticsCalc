class ModeCalc(object):
    def calculate_mode(self, lst):
        mode = []
        maxCount = 0

        # finds the maximum occurrence of repeated numbers in the list
        for i in range(len(lst)):
            count = lst.count(lst[i])
            if count > maxCount:
                maxCount = count

        # finds all numbers that occur as many times as the max occurrence
        for i in range(len(lst)):
            if lst.count(lst[i]) == maxCount:
                mode.append(lst[i])
        return list(set(mode))


lst = [3]
mode = ModeCalc()
# print mode.calculate_mode(lst)
