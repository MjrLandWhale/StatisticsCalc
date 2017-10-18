import string


class ListParser(object):
    # Assume here that values being parse are coming in from command line, therefore being read as string
    def parse_list(self, str):
        parsed_list = []

        # attempt parsing
        try:
            # Strip leading and trailing list delimiters [,],(,) if they exist
            for i in ['[',']','(',')','{','}']:
                str = string.replace(str,i,'')

            # If input is empty, return an empty list
            if len(str) == 0:
                pass

            # Parse single value single digit input
            elif len(str) == 1:
                # convert single value into numerical form
                parsed_list.append(int(str))
                # parsed_list.append(ord(str)-48)

            # Parse larger lists
            else:
                # Split the input string into a list of strings, each representing a value
                split_input = string.split(str,',')

                # Iterate through resulting list of values and append to list to be returned
                for i in split_input:
                    parsed_list.append(int(i))

            return parsed_list

        # Handle any unknown exceptions taking place and return an empty list
        except:
            print "An unknown error occurred while attempting to parse input."
            return []
