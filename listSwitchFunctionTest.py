from unittest import TestCase
import listSwitchFunction

class TestListSwitchFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = listSwitchFunction.get_switch_list([1, 2, 3, 4, 5], 3)
        expected = ([4, 5, 1, 2, 3])
        self.assertEqual(actual, expected)
    def test_if_float_answer_is_correct(self):
        actual = listSwitchFunction.get_switch_list([1.5, 2.5, 3.5, 4.5, 5.5], 2)
        expected = ([3.5, 4.5, 5.5, 1.5, 2.5])
        self.assertEqual(actual, expected)
    def test_if_negative_and_positive_integers_answer_is_correct(self):
        actual = listSwitchFunction.get_switch_list([-1, -4, 32, 16, -20], 3)
        expected = ([16, -20, -1, -4, 32])
        self.assertEqual(actual, expected)
    def test_if_float_and_negative_and_positive_integers_answer_is_correct(self):
        actual = listSwitchFunction.get_switch_list([3.5, 6.7, -5, -8, 10, 22, -15], 4)
        expected = ([10, 22, -15, 3.5, 6.7, -5, -8])
        self.assertEqual(actual, expected)
    def test_if_large_positive_integers_answer_is_correct(self):
        actual = listSwitchFunction.get_switch_list([100, 1000, 10000, 150, 900], 2)
        expected = ([10000, 150, 900, 100, 1000])
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, listSwitchFunction.get_switch_list, ["daniel"])
