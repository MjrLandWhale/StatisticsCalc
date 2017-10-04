class list_storage(object):
    #Create a 2 D array of stored lists in format 'input name' 'list values'
    MAX_STORED_LISTS = 15
    MAX_LIST_SIZE = 20

    stored_lists = list
    #initialze every column and row of the storage array
    for i in MAX_STORED_LISTS:
        for j in range(MAX_LIST_SIZE):
            stored_lists[i][j] = ''




    #Store a list coming in from command line.  The list should already have been converted to integers at this point
    def store_list(self, name, list, DEBUG=False):
        pass

    #Retrieve a list from storage based on its name
    def retrieve_list(self,name):
        pass