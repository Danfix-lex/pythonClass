import unittest
import SearchElement

class TestSearchElement(unittest.TestCase):
    def test_element_found(self):
        actual = SearchElement.search_element([3, 4, 5, 6, 7, 8], 6)
        expected = 3
        self.assertEqual(actual, expected)
    def test_positive_and_negative_element(self):
        actual = SearchElement.search_element([4, 5, 8, -2, -7, -9], -7)
        expected = 4
        self.assertEqual(actual, expected)
    def test_float_and_negative_and_positive_element(self):
        actual = SearchElement.search_element([5.5, 8.9, 10, 14, 6, -19, -20, -11], 8.9)
        expected = 1
        self.assertEqual(actual, expected)
    def test_if_element_is_false(self):
        actual = SearchElement.search_element([2, 4, 6, 8, 10, 12, 14], 10)
        expected = 5
        self.assertTrue(actual, expected)
    def test_if_element_is_true(self):
        actual = SearchElement.search_element([2, 4, 6, 8, 10], 8)
        expected = 0
        self.assertTrue(actual, expected)


if __name__ == "__main__":
    unittest.main()