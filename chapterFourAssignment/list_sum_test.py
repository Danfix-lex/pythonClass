from unittest import TestCase
import listSumFunction

class TestSumFunction(TestCase):
    def test_if_function_exist(self):
        listSumFunction.get_list_sum(number)
            
    def test_if_the_answer_is_correct(self):
        number = [1,3,4,5,6,78]
        actual = 99
        expected = listSumFunction.get_list_sum[number]
        self.assertEqual(actual, expected)
