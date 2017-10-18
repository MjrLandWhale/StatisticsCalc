class list_storage(object):


    #lets try a dict
    stored_lists = dict()

    #Store a list coming in from command line.  The list should already have been converted to integers at this point
    def store_list(self, name, list_to_store, DEBUG=False):

        self.stored_lists[name] = list_to_store

    #Retrieve a list from storage based on its name
    def retrieve_list(self,name):

        try:
            return self.stored_lists[name]
        except:
            #on missing key an exception is thrown
            return None
