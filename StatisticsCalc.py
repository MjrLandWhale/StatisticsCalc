import sys, os, string
from mean import MeanCalc
from list_parser import ListParser
from mode import ModeCalc
from list_storage import ListStorage
from variance import VarianceCalc
from binomial import BinomialCalc
from median import MedianCalc
from range import RangeCalc

# Define static variables and objects
mean_calc = MeanCalc()
mode_calc = ModeCalc()
# Create a list parser object
list_p = ListParser()
storage = ListStorage()
binomial = BinomialCalc()
variance = VarianceCalc()
median = MedianCalc()
range = RangeCalc()


def main():
    print("Welcome to StatisticsCalc. You may begin calculating. Type 'help' and hit enter to view list of functions.")

    # Program logic occurs inside this infinite loop
    while True:

        # Get user input from command line and store in variable
        user_input = raw_input('>>\t')
        # Create output variable
        output = ''
        # Create variable to store name of list
        name_of_list_to_store = ''

        # True when help is called.  Print help text
        if user_input == 'help':
            output = "Help Manual\n" \
                     "After typing a function followed by one or more set of numbers wrapped by parentheses, " \
                     "hit 'enter' to calculate.\n" \
                     "Each set of numbers is wrapped by brackets. Numbers and sets are separated by commas.\n" \
                     "Below are examples of how to format and use each function:\n" \
                     "range([3, 7, 20, 4, 6])\n" \
                     "median([6, 4, 3, 2])\n" \
                     "mode([1, 0, 6, 7, 4])\n" \
                     "mean([3, 2, 4])\n" \
                     "binomial(1, 0, 6, 7, 4)\n" \
                     "variance([0, 7, 8, 9, 4])\n" \
                     "zscore(2, 4, 6) OR zscore_from_list(5, [43, 42, 54, 32])\n" \
                     "permutation(7, 4)\n" \
                     "negative_binomial(0.6, 6, 3)\n" \
                     "combination(4, 2)\n" \
                     "add([4, 5, 6, 7, 8])\n" \
                     "subtract([3, 5])\n" \
                     "divide([7, 8, 5, 4])\n" \
                     "multiply([4, 5, 6])\n" \

        # True when exit is called.  Leave the program
        elif user_input == 'exit':
            sys.exit(0)

        ########Command Line interpretation below
        else:
            # True when a '=' exists.  Indicates output must be stored in a variable
            if '=' in user_input:
                # Split the input on the = sign
                split_input = user_input.split('=')
                # Store name of list for later
                name_of_list_to_store = split_input[0]
                # Recreate user input
                user_input = split_input[1]

            # True when a ( exists in the input.  Indicates a function call.  Check within
            if '(' in user_input:

                # Splits input into separate function call and parameters
                split_method = user_input.split('(')
                func = split_method[0]
                parameters = split_method[1]
                print parameters

                # List of parsed parameters
                op_list = []

                # Iterate through all sets of parameters
                while True:
                    # catch a list first
                    if parameters[0] is '[':

                        end_of_list = parameters.find(']')
                        # Add each list to
                        op_list.append(ListParser.parse_list(list_p, parameters[0:end_of_list]))

                        # use +1 in order to remove next , or final )
                        parameters = parameters[end_of_list + 1:]

                        # check to make sure we don't have to leave
                        if parameters is '':
                            break

                    # If not list, then maybe number?
                    elif parameters[0].isdigit():
                        # If we have multiple inputs still
                        if ',' in parameters:
                            end_of_list = parameters.find(',')
                            # Add the single value to the list of values
                            op_list.append(ListParser.parse_list(list_p, parameters[0:end_of_list]))
                            # Use +1 to remove the , from the string
                            parameters = parameters[end_of_list + 1:]

                        # No, exists meaning this digit is the only parameter
                        else:
                            op_list.append(ListParser.parse_list(list_p, parameters))
                            break

                    # If we hit ) then we have finished iterating the list
                    elif parameters[0] is ')':
                        break
                    # This case is just so we don't get hung up on some weird bug and will always leave
                    else:
                        break




                    ############Function calls below#########

                # Handle Error condition when no function name is entered
                if func == '':
                    output = 'No function entered.'

                # Handle mean calculation
                elif func == 'mean':
                    output = MeanCalc.calculate_mean(mean_calc, op_list[0])

                # Handle mode calculation
                elif func == 'mode':
                    output = ModeCalc.calculate_mode(mode_calc, op_list[0])

                # elif function == '':
                # Handle binomial calculation
                elif func == 'binomial':
                    print op_list[0], op_list[1], op_list[2]
                    if len(op_list) != 3:  # If there are not exactly three inputs, tell the user
                        output = 'Binomial function takes three inputs. \n' \
                                 'binomial(success probability, number of trials, number of successes)'
                    else:
                        output = BinomialCalc.binomial_calc(binomial, op_list[0], op_list[1], op_list[2])
                elif func == 'median':
                    output = MedianCalc.calculate_median(median, op_list[0])
                elif func == 'range':
                    output = RangeCalc.calculate_range(range, op_list[0])
            else:
                print 'Unknown function.'
                continue

        print output
        if name_of_list_to_store is not '':
            ListStorage.store_list(storage, name_of_list_to_store, output)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)
