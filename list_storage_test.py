import unittest
from list_storage import list_storage

class test(unittest.TestCase):

    def test_store_empty_list(self):
        storage = list_storage()

        list_name = "Name1"
        list_values = []
  ###########################################
        expected = []
        list_storage.store_list(storage, list_name, list_values)
        actual = list_storage.retrieve_list(storage,"Name1")
        self.assertEqual(expected,actual, "Name1 = []")

    def test_store_single_value_list(self):
        storage = list_storage()

        list_name = "Name2"
        list_values = [4]
        expected = [4]
        list_storage.store_list(storage,list_name,list_values)
        actual = list_storage.retrieve_list(storage,"Name2")
        self.assertEqual(expected,actual, "Name2 = [4]")

    def test_store_multi_value_list(self):
        storage = list_storage()

        list_name = "Name3"
        list_values = [4,8,17]
        expected = [4, 8, 17]
        list_storage.store_list(storage,list_name, list_values)
        actual = list_storage.retrieve_list(storage,"Name3")
        self.assertEqual(expected, actual, "Name3 = [4, 8, 17]")
