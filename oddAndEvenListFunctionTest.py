from unittest import TestCase
import oddAndEvenListFunction

class TestEvenAndOddListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = oddAndEvenListFunction.get_odd_and_even_list_number([1, 2, 3, 4, 5])
        expected = ([False, True, False, True, False])
        self.assertTrue(actual, expected)
    def test_if_float_answer_is_correct(self):
        actual = oddAndEvenListFunction.get_odd_and_even_list_number([1.5, 2.5, 3.5, 4.5, 5.5])
        expected = ([False, False, False, False, False])
        self.assertTrue(actual, expected)
    def test_if_negative_and_positive_integers_answer_is_correct(self):
        actual = oddAndEvenListFunction.get_odd_and_even_list_number([-1, -4, 32, 16, -20])
        expected = ([False, True, True, True, True])
        self.assertTrue(actual, expected)
    def test_if_float_and_negative_and_positive_integers_answer_is_correct(self):
        actual = oddAndEvenListFunction.get_odd_and_even_list_number([3.5, 6.7, -5, -8, 10, 22, -15])
        expected = ([False, False, False, True, True, True, False])
        self.assertTrue(actual, expected)
    def test_if_large_positive_integers_answer_is_correct(self):
        actual = oddAndEvenListFunction.get_odd_and_even_list_number([100, 1000, 10000, 150, 900])
        expected = ([True, True, True, True, True])
        self.assertTrue(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, oddAndEvenListFunction.get_odd_and_even_list_number, ["daniel"])
