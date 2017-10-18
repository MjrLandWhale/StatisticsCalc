import sys, os, string
from mean import MeanCalc
from list_parser import ListParser
from mode import ModeCalc

#Define static variables and objects
mean_calc = MeanCalc()
mode_calc = ModeCalc()

def main():
    print("Welcome to StatisticsCalc. You may begin calculating. Type 'help' and hit enter to view list of functions.")

    #Program logic occurs inside this infinite loop
    while True:

#########These should all be above the infinite loop
        #Create a list parser object
        list = ListParser()
        #Get user input from command line and store in variable
        user_input = raw_input('>>\t')
        #Create output variable
        output = ''
        #Create variable to store name of list
        name_of_list_to_store = ''

        #True when help is called.  Print help text
        if user_input == 'help':
            output = "Help Manual\n" \
                     "After typing a function followed by a set of numbers wrapped by parentheses, " \
                     "hit 'enter' to calculate.\n" \
                     "Below are examples of how to format and use each function:\n" \
                     "range(3, 7, 20, 4, 6)\n" \
                     "median(6, 4, 3, 2)"

        #True when exit is called.  Leave the program
        elif user_input == 'exit':
            sys.exit(0)

        #True when a = exists.  Indicates output must be stored in a variable
        if '=' in user_input:

            #Find where in the input the equal sign is
            index_of_equals = user_input.find('=')
            #Create string of the name of the list being stored to
            name_of_list_to_store = user_input[0:index_of_equals]
            #Remove any whitespace from the name
            name_of_list_to_store.strip(' ')
            
            #Remove everything up to the equal sign from the input string so it doesn't go haywire
            user_input = user_input[index_of_equals+1:]

        #True when a ( exists in the input.  Indicates a function call
        elif '(' in user_input:
            #Create string containing name of the function being called
            function = user_input[0:user_input.find("(")]
            #Create string containing the input of a function call
            string = user_input[user_input.find("(") + 1:user_input.find(")")]
            #Parse the input of the function into a usable list of ints
            parsed_list = ListParser.parse_list(list, string)




############Function calls below#########

            #Handle Error condition when no function name is entered
            if function == '':
                output = 'No function entered.'

            #Handle mean calculation
            elif function == 'mean':
                output = MeanCalc.calculate_mean(mean_calc, parsed_list)

            #Handle mode calculation
            elif function == 'mode':
                output = ModeCalc.calculate_mode(mode_calc, parsed_list)

#            elif function == ''
        else:
            output = 'Unknown function.'
        print output


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)
