from unittest import TestCase
import squareOddNumber

class TestPrimeInListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = squareOddNumber.get_list_square_total ([10,3,7,1,9,4,2,8,5,6])
        expected = [9, 49, 1, 81, 25]
        self.assertEqual(actual, expected)
