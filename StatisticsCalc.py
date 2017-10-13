import sys, os

class MyMath(object):
	def add(self, inputA, inputB):
		return inputA + inputB

calc = MyMath()
print calc.add(3,5)

while True:
	print("Welcome to Statistics Calculator. You may begin your calculations. Enter 'help' to view the list of functions.")
#	input = None
#	while input is None:
#		try:
#			input = raw_input()
#		except KeyboardInterrupt:
#			print 'Interrupted'
			#os._exit(0)
			#sys.exit()
	try:
		pass
	except:
		print 'Interrupted'
		os._exit(0)