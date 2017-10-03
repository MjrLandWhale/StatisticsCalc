import unittest
from list_parser import list_parser

#Test parsing single value single digit input
class test_1(unittest.TestCase):
    def test_parse(self):
        list = list_parser()

        input = "1"
        expected = [1]
        actual = list_parser.parse_list(list, input)
        self.assertEqual(expected,actual, "list = [1]")


# Test parsing multi value single digit input
class test_2(unittest.TestCase):
    def test_parse(self):
        list = list_parser()

        input = "1,4,7,8,1,7"
        expected = [1,4,7,8,1,7]
        actual = list_parser.parse_list(list, input)
        self.assertEqual(expected, actual, "list = [1,4,7,8,1,7]")


# Test parsing single value multi digit input
class test_3(unittest.TestCase):
    def test_parse(self):
        list = list_parser()

        input = "1784"
        expected = [1784]
        actual = list_parser.parse_list(list, input)
        self.assertEqual(expected, actual, "list = [1784]")

# Test parsing multi value multi digit input
class test_4(unittest.TestCase):
    def test_parse(self):
        list = list_parser()

        input = "178,518,43,32,2,48"
        expected = [178,518,43,32,2,48]
        actual = list_parser.parse_list(list, input)
        self.assertEqual(expected, actual, "list = [178,518,43,32,2,48]")



if __name__ == '__main__':
    unittest.main()