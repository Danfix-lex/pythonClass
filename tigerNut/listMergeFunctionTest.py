from unittest import TestCase
import listMergeFunction

class TestListMergeFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = listMergeFunction.get_list_number_merge(([1, 3, 5], [2, 4, 6]))
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)
    def test_if_float_answer_is_correct(self):
        actual = listMergeFunction.get_list_number_merge(([1.5, 3.5, 5.5], [2.5, 4.5, 6.5]))
        expected = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
        self.assertEqual(actual, expected)
    def test_if_negative_and_positive_list_answer_is_correct(self):
        actual = listMergeFunction.get_list_number_merge(([-1, -4, 32, 16, -20], [-2, -6, 7, 8, 70]))
        expected = [-2, -6, -1, -4, 7, 8, 32, 16, -20, 70]
        self.assertEqual(actual, expected)
    def test_if_large_positive_list_answer_is_correct(self):
        actual = listMergeFunction.get_list_number_merge(([100, 1000, 10000, 150, 900], [80000000, 40, 600000, 10000000000000, 3000000]))
        expected = [100, 1000, 10000, 150, 900, 80000000, 40, 600000, 10000000000000, 3000000]
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, listMergeFunction.get_list_number_merge, ["daniel"], ["ojo"])
