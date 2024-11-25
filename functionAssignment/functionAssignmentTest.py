from unittest import TestCase
import evenNumberFunction
import primeNumberFunction
import subtractNumberFunction
import divideNumberFunction
import numberFactorFunction
import numberSquareFunction
import palindromeNumber
import factorialNumber
import squareNumber
import largestNumber
import reverseList
import oddPosition
import totalRunningList
import palindromeNumberList
import sumLoopList
import concatenateList
import numberToDigit

class TestEvenNumberFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = evenNumberFunction.get_even_number(8)
        expected = (True)
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, evenNumberFunction.get_even_number, ["daniel"])

class TestPrimeNumberFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = primeNumberFunction.get_prime_number(10)
        expected = (True)
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, primeNumberFunction.get_prime_number, ["daniel"])
        
class TestSubtractNumberFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = subtractNumberFunction.get_subtract_number(3, 7)
        expected = 4
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, subtractNumberFunction.get_subtract_number, ["daniel"])

class TestDivideNumberFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = divideNumberFunction.get_divide_number(3, 7)
        expected =  0.42857142857142855
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, divideNumberFunction.get_divide_number, ["daniel"])

class TestFactorNumberFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = numberFactorFunction.get_number_factor(5)
        expected = (2)
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, numberFactorFunction.get_number_factor, ["daniel"])
        
class TestSquareNumberFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = numberSquareFunction.get_number_square(25)
        expected = True
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, numberSquareFunction.get_number_square, ["daniel"])
        
class TestPalindromeNumberFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = palindromeNumber.get_palindrome_number(25652)
        expected = True
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, numberSquareFunction.get_number_square, ["daniel"])
        
class TestFactorialNumberFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = factorialNumber.get_factorial_number(5)
        expected = (120)
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, factorialNumber.get_factorial_number, ["daniel"])
        
class TestNumberSquareFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = squareNumber.get_square_number(5)
        expected = (25)
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, squareNumber.get_square_number, ["daniel"])
        
class TestLargestNumberFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = largestNumber.get_largest_element([1, 2, 3, 4, 5])
        expected = (5)
        self.assertEqual(actual, expected)

class TestNumberReverseFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = reverseList.get_reverse_list([1, 2, 3, 4, 5])
        expected = ([5, 4, 3, 2, 1])
        self.assertEqual(actual, expected)
        
class TestOddNumberFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = oddPosition.get_odd_positions([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected =  1
        self.assertEqual(actual, expected)
        
class TestNumberRunningTotalListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = totalRunningList.get_running_total_list([1, 2, 3, 4, 5])
        expected = ([1, 3, 6, 10, 15])
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, totalRunningList.get_running_total_list, ["daniel"])
        
class TestPalindromeNumberListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = palindromeNumberList.get_palindrome_number(["church"])
        expected = True
        self.assertEqual(actual, expected)
        
class TestLoopNumberlListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = sumLoopList.get_sum_for_loop([1, 2, 3, 4, 5])
        expected = 15
        self.assertEqual(actual, expected)
    def test_if_function_is_correct(self):
        actual = sunLoopList.get_sum_for_while_loop([1, 2, 3, 4, 5])
        expected = 15
        self.assertEqual(actual, expected)
    def test_if_function_is_correct(self):
        actual = sumLoopList.get_sum_for_do_while_loop([1, 2, 3, 4, 5])
        expected = 15
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, sumLoopList.get_sum_for_do_while_loop, ["daniel"])
        
class TestConcatenateNumberFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = concatenateList.get_concatenate_lists([1, 2, 3], [4, 5, 6])
        expected = ([1, 2, 3, 4, 5, 6])
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, concatenateList.get_concatenate_lists, ["daniel"])

class TestNumberToDigitFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = numberToDigit.get_number_to_digits("2345")
        expected = [2, 3, 4, 5]
        self.assertEqual(actual, expected)
    def test_that_the_input_is_not_invalid(self):
        self.assertRaises(TypeError, numberToDigit.get_number_to_digits, ["daniel"])
