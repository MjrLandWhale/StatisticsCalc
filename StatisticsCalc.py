import sys, os
from mean import mean

def main():
    print("Welcome to StatisticsCalc. You may begin calculating. Type 'help' and hit enter to view list of functions.")
    while True:
        user_input = raw_input('>>\t')

        if user_input is 'help':
            print("Help Manual\n" +
                  "After typing a function followed by a set of numbers wrapped by parentheses, " +
                  "hit 'enter' to calculate.\n" +
                  "Below are examples of how to format and use each function:\n" +
                  "range(3, 7, 20, 4, 6)\n" +
                  "median(6, 4, 3, 2)")
            continue
        elif user_input is 'exit':
            sys.exit(0)
        else:
            if '(' in user_input:
                function = user_input[0:user_input.find("(")]
                # string = user_input[user_input.find("(") + 1:user_input.find(")")]
                if function == '':
                    print 'No function entered.'
                if function == 'mean':
                    mean_calc = mean()
                    answer = mean.calculate_mean(mean_calc, [2, 4, 5, 6, 7])
                    print(answer)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)
