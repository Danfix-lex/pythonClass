from unittest import TestCase
import removeFunction

class TestListRemoveFunction(TestCase):

    def test_if_function_exist(self):
        self.assertTrue(removeFunction.remove_second_element)
    
    def test_if_the_answer_is_correct(self):
        number = [3]
        expected = [0]
        actual = removeFunction.remove_second_element(number)
        self.assertEqual(actual, expected)

