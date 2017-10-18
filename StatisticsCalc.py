import sys, os
from mean import MeanCalc
from list_parser import ListParser
from mode import ModeCalc


def main():
    print("Welcome to StatisticsCalc. You may begin calculating. Type 'help' and hit enter to view list of functions.")
    while True:
        list_parser = ListParser()
        user_input = raw_input('>>\t')
        output = ''

        if user_input == 'help':
            output = "Help Manual\n" \
                     "After typing a function followed by a set of numbers wrapped by parentheses, " \
                     "hit 'enter' to calculate.\n" \
                     "Below are examples of how to format and use each function:\n" \
                     "range(3, 7, 20, 4, 6)\n" \
                     "median(6, 4, 3, 2)"
        elif user_input == 'exit':
            sys.exit(0)
        elif '(' in user_input:
            function = user_input[0:user_input.find("(")]
            string = user_input[user_input.find("(") + 1:user_input.find(")")]
            parsed_list = ListParser.parse_list(list_parser, string)
            if function == '':
                output = 'No function entered.'
            elif function == 'mean':
                mean_calc = MeanCalc()
                output = MeanCalc.calculate_mean(mean_calc, parsed_list)
            elif function == 'mode':
                mode_calc = ModeCalc()
                output = ModeCalc.calculate_mode(mode_calc, parsed_list)
        else:
            output = 'Unknown function.'
        print output


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)
