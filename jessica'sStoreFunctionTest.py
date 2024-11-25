from unittest import TestCase
import evenSumInArrayFunction

class TestEvenSumInArrayFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = evenSumInArrayFunction.get_even_sum_in_array([1, 2, 3, 4, 5])
        expected = 6
        self.assertEqual(actual, expected)
    def test_if_float_answer_is_correct(self):
        actual = evenSumInArrayFunction.get_even_sum_in_array([1.5, 2.5, 3.5, 4.5, 5.5])
        expected = 0
        self.assertEqual(actual, expected)
    def test_if_negative_and_positive_integers_answer_is_correct(self):
        actual = evenSumInArrayFunction.get_even_sum_in_array([-1, -4, 32, 16, -20])
        expected = 24
        self.assertEqual(actual, expected)
    def test_if_large_positive_integers_answer_is_correct(self):
        actual = evenSumInArrayFunction.get_even_sum_in_array([100, 1000, 10000, 150, 900])
        expected = 12150
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, evenSumInArrayFunction.get_even_sum_in_array, ["daniel"])
