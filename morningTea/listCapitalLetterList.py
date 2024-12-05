from unittest import TestCase
import listCapitalLetter

class TestPrimeInListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = listCapitalLetter.capital_letter(["Red", "orange", "yellow", "green", "blue"])
        expected = ['Red', 'Orange', 'Yellow', 'Green', 'Blue']
        self.assertEqual(actual, expected)
