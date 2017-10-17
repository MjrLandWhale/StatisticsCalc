import sys, os


def main():
    print("Welcome to Statistics Calculator. You may begin your calculations. Enter 'help' to view list of functions.")
    while True:
        user_input = None
        while user_input is None:
            user_input = raw_input('>>\t')

        if user_input == 'hey':
            print("what's up?")
            continue

        if user_input == 'exit':
            sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)


class MyMath(object):
    def add(self, inputA, inputB):
        return inputA + inputB

# calc = MyMath()
# print calc.add(3, 5)
