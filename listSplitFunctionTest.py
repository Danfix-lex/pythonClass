from unittest import TestCase
import listSplitFunction

class TestListSplitFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = listSplitFunction.get_split_list([1, 2, 3, 4, 5])
        expected = ([1, 2], [3, 4, 5])
        self.assertEqual(actual, expected)
    def test_if_float_answer_is_correct(self):
        actual = listSplitFunction.get_split_list([1.5, 2.5, 3.5, 4.5, 5.5])
        expected = ([1.5, 2.5], [3.5, 4.5, 5.5])
        self.assertEqual(actual, expected)
    def test_if_negative_and_positive_integers_answer_is_correct(self):
        actual = listSplitFunction.get_split_list([-1, -4, 32, 16, -20])
        expected = ([-1, -4], [32, 16, -20])
        self.assertEqual(actual, expected)
    def test_if_float_and_negative_and_positive_integers_answer_is_correct(self):
        actual = listSplitFunction.get_split_list([3.5, 6.7, -5, -8, 10, 22, -15])
        expected = ([3.5, 6.7, -5], [-8, 10, 22, -15])
        self.assertEqual(actual, expected)
    def test_if_large_positive_integers_answer_is_correct(self):
        actual = listSplitFunction.get_split_list([100, 1000, 10000, 150, 900])
        expected = ([100, 1000], [10000, 150, 900])
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, listSplitFunction.get_split_list, ["daniel"])
