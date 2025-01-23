import unittest
import evenNumbersFunction

class TestSearchElement(unittest.TestCase):
    def test_element_is_not_found(self):
        actual = evenNumbersFunction.get_even_numbers_from_string(
            "abcd5911")
        expected = []
        self.assertEqual(actual, expected)
    def test_if_function_is_correct(self):
        actual = evenNumbersFunction.get_even_numbers_from_string("ABCFG86855098763")
        expected = [8, 6, 8, 0, 8, 6]
        self.assertEqual(actual, expected)
if __name__ == "__main__":
    unittest.main()