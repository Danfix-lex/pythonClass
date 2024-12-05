from unittest import TestCase
import squareOddNumber
import listPalindromeComprehension
import numbersFromLetterComprehension

class TestPrimeInListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = squareOddNumber.get_number_square_total (4)
        expected = [0, 1, 4, 9, 16]
        self.assertEqual(actual, expected)
class TestPalindromeLetter(TestCase):
    def test_palindrome_letter(self):
        actual = listPalindromeComprehension.get_palindrome_letter(["madam", "apple", "racecar"])
        expected = [True, False, True]
        self.assertEqual(actual, expected)
class TestIntegersInLetters(TestCase):
    def test_numbers_from_letter(self):
        actual = numbersFromLetterComprehension.get_numbers_from_letter("abc123def456")
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)
