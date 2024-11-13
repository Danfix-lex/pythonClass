from unittest import TestCase
import divideOrSquareFunction

class TestDivideOrSquareFunction(TestCase):
    def test_if_function_exist(self):
        divideOrSquareFunction.divide_or_square(10)
            
    def test_if_the_answer_is_correct(self):
        actual = divideOrSquareFunction.divide_or_square(10)
        expected = 3.16
        self.assertEqual(actual, expected)
        
    def test_if_even_float_number_answer_will_be_correct(self):
        actual = divideOrSquareFunction.divide_or_square(10.5)
        expected = 0.50
        self.assertEqual(actual, expected)
    def test_if_odd_float_number_answer_will_be_correct(self):
        actual = divideOrSquareFunction.divide_or_square(7.5)
        expected = 2.5
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, divideOrSquareFunction.divide_or_square, "daniel")

        

        

        
