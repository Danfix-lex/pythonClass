import unittest
import numberSquareFunction

class TestSearchElement(unittest.TestCase):
    def test_element_is_not_found(self):
        actual = numberSquareFunction.generate_number_square_dictionary(5)
        expected = [{1:5}, {2:25}, {3:125}, {4:625}, {5:3125}]
        self.assertEqual(actual, expected)
    def test_if_function_is_correct(self):
        actual = numberSquareFunction.generate_number_square_dictionary(2)
        expected = [{1:2}, {2:4}]
        self.assertEqual(actual, expected)
if __name__ == "__main__":
    unittest.main()