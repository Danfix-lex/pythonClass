import unittest
import elementRangeFunction

class TestSearchElement(unittest.TestCase):
    def test_element_is_found(self):
        actual = elementRangeFunction.get_number_range_list([12, 15, 19, 21, 50, 70])
        expected = [21, 50]
        self.assertEqual(actual, expected)
    def test_if_negative_function_is_correct(self):
        actual = elementRangeFunction.get_number_range_list([-10, -50, -30, -7])
        expected = []
        self.assertEqual(actual, expected)
    def test_if_float_function_is_correct(self):
        actual = elementRangeFunction.get_number_range_list([10.2, 28.3, 31.4, 46.5, 50.6])
        expected = [28.3,31.4,46.5, 50.6]
        self.assertEqual(actual, expected)
    def test_if_positive_and_negative_and_float_function_is_correct(self):
        actual = elementRangeFunction.get_number_range_list([-10.2, 28.3, 31.4, 46.5, 50.6, 10, -89.6, -90, -48, -34.7])
        expected = [28.3,31.4,46.5, 50.6]
        self.assertEqual(actual, expected)
if __name__ == "__main__":
    unittest.main()