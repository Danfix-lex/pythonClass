from unittest import TestCase
import listSumFunction

class TestListFunction(TestCase):

    def test_if_function_exist(self):
        self.assertTrue(listSumFunction.get_list_sum)
        
    def test_if_the_answer_is_correct(self):
        number = [1, 3, 4, 5, 6, 78]
        expected = 97
        actual = listSumFunction.get_list_sum(number)
        self.assertEqual(actual, expected)
        
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, listSumFunction.get_list_sum, "daniel")
        
    def test_if_float_numbers_answer_is_correct(self):
        number = [2.4, 5.5, 6.7, 8.9, 6.8]
        expected = 30.3
        actual = listSumFunction.get_list_sum(number)
        self.assertEqual(actual, expected)
    
    def test_if_negative_and_positive_numbers_answers_is_correct(self):
        number = [-6, -10, 6, 8, -34]
        expected = -36
        actual = listSumFunction.get_list_sum(number)
        self.assertEqual(actual, expected)
    
    def test_if_zero_numbers_answer_is_correct(self):
        number = [0, 0, 0, 0, 0, 0]
        expected = 0
        actual = listSumFunction.get_list_sum(number)
        self.assertEqual(actual, expected)
        
    def test_if_negative_numbers_answer_is_correct(self):
        number = [-45, -6, -7, -100, -67, -9]
        expected = -234
        actual = listSumFunction.get_list_sum(number)
        self.assertEqual(actual, expected)
