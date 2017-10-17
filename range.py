class RangeCalc(object):
    def calculate_range(self, number_list):
        calculated_range = None

        if len(number_list) > 1:
            sorted_list = sorted(number_list)
            smallest_num = sorted_list[0]
            greatest_num = sorted_list[len(sorted_list) - 1]
            calculated_range = greatest_num - smallest_num

        return calculated_range

# number_list = [2, 3, 5, 7]
# range_num = RangeCalc()
# print range_num.calculate_range(number_list)
