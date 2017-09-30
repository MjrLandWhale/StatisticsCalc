class ModeCalc(object):
    def calculate_mode(self, lst):
        mode = []
        maxCount = 0

        for i in range(len(lst)):
            count = lst.count(lst[i])
            if count > maxCount:
               maxCount = count

        for i in range(len(lst)):
            if lst.count(lst[i]) == maxCount:
                mode.append(lst[i])
        return list(set(mode))


lst = [1,3,2,1,3,2,1,4,1,2,2,2,2,3,7,8,3,9,5,3,4,3,8,3,2,2]
mode = ModeCalc()
print mode.calculate_mode(lst)

