import unittest
from list_parser import list_parser


class test(unittest.TestCase):
    # Test parsing an empty string
    def test_parse_empty_string(self):
        list = list_parser()

        input = ""
        expected = []
        actual = list_parser.parse_list(list, input)
        self.assertEqual(expected, actual, "list = []")

    # Test parsing single value single digit input
    def test_parse_singleval_singledig(self):
        list = list_parser()

        input = "1"
        expected = [1]
        actual = list_parser.parse_list(list, input)
        self.assertEqual(expected, actual, "list = [1]")

    # Test parsing multi value single digit input
    def test_parse_multival_singledig(self):
        list = list_parser()

        input = "1,4,7,8,1,7"
        expected = [1, 4, 7, 8, 1, 7]
        actual = list_parser.parse_list(list, input)
        self.assertEqual(expected, actual, "list = [1,4,7,8,1,7]")

    # Test parsing single value multi digit input
    def test_parse_singleval_multidig(self):
        list = list_parser()

        input = "1784"
        expected = [1784]
        actual = list_parser.parse_list(list, input)
        self.assertEqual(expected, actual, "list = [1784]")

    # Test parsing multi value multi digit input
    def test_parse_multival_multidig(self):
        list = list_parser()

        input = "178,518,43,32,2,48"
        expected = [178, 518, 43, 32, 2, 48]
        actual = list_parser.parse_list(list, input)
        self.assertEqual(expected, actual, "list = [178,518,43,32,2,48]")


if __name__ == '__main__':
    unittest.main()
