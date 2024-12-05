from unittest import TestCase
import morningTea

class TestPrimeInListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = morningTea.get_prime_even_number([2,7,9,17,19,2,8,10])
        expected = 22
        self.assertEqual(actual, expected)
    def test_if_positive_integer_answer_is_correct(self):
        actual = morningTea.get_prime_even_number([1,2,3,4,5])
        expected = 6
        self.assertEqual(actual, expected)
    def test_if_negative_and_positive_integer_answer_is_correct(self):
        actual = morningTea.get_prime_even_number([2, -12, 33, 67, -87, -60])
        expected = -70
        self.assertEqual(actual, expected)
