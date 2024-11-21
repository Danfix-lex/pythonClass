from unittest import TestCase
import listAverageFunction

class TestAverageInListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = listAverageFunction.get_list_average([10, 20, 30, 40])
        expected = 25.0
        self.assertEqual(actual, expected)
    def test_if_positive_list_answer_is_correct(self):
        actual = listAverageFunction.get_list_average([40, 80, 90, 30, 10, 34])
        expected = 47.333333333333336
        self.assertEqual(actual, expected)
    def test_if_negative_or_positive_list_answer_is_correct(self):
        actual = listAverageFunction.get_list_average([-45, 90, -55, 80, -20, -24])
        expected = 4.333333333333333
        self.assertEqual(actual, expected)
    def test_if_large_positive_integers_answer_is_correct(self):
        actual = listAverageFunction.get_list_average([1000000, 80000000, 50000000, 400000000])
        expected = 132750000
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, listAverageFunction.get_list_average, ["daniel"])
