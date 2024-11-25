from unittest import TestCase
import myfunction

class TestSumFunction(TestCase):
    def test_if_function_exist(self):
        myfunction.calculate_sum(6, 5)
    
    def test_if_the_answer_is_correct(self):
        actual = myfunction.calculate_sum(5, 5)
        expected = 25
        self.assertEqual(actual, expected)
        actual = myfunction.calculate_sum(10, 5)
        expected = 50
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, myfunction.calculate_sum, "daniel")
    def test_returns_the_correct_answer_even_if_its_a_float(self):
        actual = myfunction.calculate_sum(5.5, 5)
        expected = 27.5
        self.assertEqual(actual, expected)
    def test_if_the_negative_integer_is_correct_with_a_positive_integer(self):
        actual = myfunction.calculate_sum(-7, 5)
        expected = -35
        self.assertEqual(actual, expected)
    def test_if_negative_integer_is_correct_with_negative_integer(self):
        actual = myfunction.calculate_sum(-17, -4)
        expected = 0
        self.assertEqual(actual, expected)
    def test_if_positive_integer_is_correct_with_negative_integer(self):
        actual = myfunction.calculate_sum(7, -3)
        expected = 0
        self.assertEqual(actual, expected)
        
