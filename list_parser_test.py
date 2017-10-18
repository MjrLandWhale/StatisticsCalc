import unittest
from list_parser import ListParser


class ListParserTest(unittest.TestCase):
    # Test parsing an empty string
    def test_parse_empty_string(self):
        list_parser = ListParser()

        user_input = ""
        expected = []
        actual = ListParser.parse_list(list_parser, user_input)
        self.assertEqual(expected, actual, "list = []")

    # Test parsing single value single digit input
    def test_parse_singleval_singledig(self):
        list_parser = ListParser()

        user_input = "1"
        expected = [1]
        actual = ListParser.parse_list(list_parser, user_input)
        self.assertEqual(expected, actual, "list = [1]")

    # Test parsing multi value single digit input
    def test_parse_multival_singledig(self):
        list_parser = ListParser()

        user_input = "1,4,7,8,1,7"
        expected = [1, 4, 7, 8, 1, 7]
        actual = ListParser.parse_list(list_parser, user_input)
        self.assertEqual(expected, actual, "list = [1,4,7,8,1,7]")

    # Test parsing single value multi digit input
    def test_parse_singleval_multidig(self):
        list_parser = ListParser()

        user_input = "1784"
        expected = [1784]
        actual = ListParser.parse_list(list_parser, user_input)
        self.assertEqual(expected, actual, "list = [1784]")

    # Test parsing multi value multi digit input
    def test_parse_multival_multidig(self):
        list_parser = ListParser()

        user_input = "178,518,43,32,2,48"
        expected = [178, 518, 43, 32, 2, 48]
        actual = ListParser.parse_list(list_parser, user_input)
        self.assertEqual(expected, actual, "list = [178,518,43,32,2,48]")


if __name__ == '__main__':
    unittest.main()
