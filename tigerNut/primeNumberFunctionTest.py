from unittest import TestCase
import primeNumberFunction

class TestPrimeInListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = primeNumberFunction.get_prime_number(7)
        expected = True
        self.assertTrue(actual, expected)
    def test_if_positive_integer_answer_is_correct(self):
        actual = primeNumberFunction.get_prime_number(3)
        expected = True
        self.assertTrue(actual, expected)
    def test_if_negative_or_positive_integers_answer_is_correct(self):
        actual = primeNumberFunction.get_prime_number(-517)
        expected = True
        self.assertEqual(actual, expected)
    def test_if_large_positive_integers_answer_is_correct(self):
        actual = primeNumberFunction.get_prime_number(7000)
        expected = None
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, primeNumberFunction.get_prime_number, ["daniel"])
