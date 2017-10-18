class list_storage(object):

    #Lists are stored as tuples in (name, list[]) format
#    stored_lists = []

    #lets try a dict
    stored_lists = dict()

    #Store a list coming in from command line.  The list should already have been converted to integers at this point
    def store_list(self, name, list_to_store, DEBUG=False):

        #Due to expected scope of this class, we do not need to sort stored_lists
 #       self.stored_lists.append( ( name, list_to_store ) )

        self.stored_lists[name] = list_to_store

    #Retrieve a list from storage based on its name
    def retrieve_list(self,name):

        try:
            return self.stored_lists[name]
        except:
            #on missing key an exception is thrown
            return None


        #Iterate through current stored lists in search of the correct name
#        for i in self.stored_lists:

            #If the stored name is equivalent to the requested name
##               return i[1]

        #If we reach this point that means the list isn't in storage, so return none
#        return None
