import unittest
from list_storage import *


class test(unittest.TestCase):
    def test_store_empty_list(self):
        storage = list_storage()

        list_name = "Name1"
        list_values = []
        ###########################################
        expected = ["Name1"]
        storage.store_list(storage, list_name, list_values)
        actual = list_storage.stored_lists[0]
        self.assertEqual(expected, actual, "Name1 = []")

    def test_store_single_value_list(self):
        storage = list_storage()

        list_name = "Name2"
        list_values = [4]
        expected = ["Name2", 4]
        storage.store_list(list_name, list_values)
        actual = list_storage.stored_lists[0]
        self.assertEqual(expected, actual, "Name2 = [4]")

    def test_store_multi_value_list(self):
        storage = list_storage()

        list_name = "Name3"
        list_values = [4, 8, 17]
        expected = ["Name3", 4, 8, 17]
        storage.store_list(list_name, list_values)
        actual = list_storage.stored_lists[0]
        self.assertEqual(expected, actual, "Name2 = [4, 8, 17]")
