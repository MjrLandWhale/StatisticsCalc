class MedianCalc(object):
	def calculate_median(self, number_list):
		calculated_median = None

		if len(number_list) > 1:
			sorted_list = sorted(number_list) # sort list of numbers
			if len(sorted_list) % 2 == 0: # if mod 2 is 0 then list is of even length
				first_num = sorted_list[(len(sorted_list) / 2) - 1] # get number to the left side of the middle of the list
				second_num = sorted_list[(len(sorted_list) / 2)] # get number to the right side of the middle of the list
				calculated_median = (first_num + second_num) / 2 # find mean of two numbers
			else: # list length is odd
				calculated_median = sorted_list[int(len(sorted_list) / 2)] #
		return calculated_median

# number_list = [2, 3, 5, 7]
# median = MedianCalc()
# print median.calculate_median(number_list)

