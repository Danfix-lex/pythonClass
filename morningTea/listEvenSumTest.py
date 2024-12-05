from unittest import TestCase
import numbersFromLetterComprehension

class TestPrimeInListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = numbersFromLetterComprehension.get_dictionary_list(["Name", "Age", "City", "Work"], ["Daniel", "20", "Lagos", "C.E.O"])
        expected = {"Name":"Daniel", "Age":"20", "City":"Lagos", "Work":"C.E.O"}
        self.assertEqual(actual, expected)
    def test_if_function_is_correct(self):
        actual = numbersFromLetterComprehension.get_values_from_dictionary({"Name":"Daniel", "Age":"20", "City":"Lagos", "Work":"C.E.O"})
        expected = ["Daniel", "20", "Lagos", "C.E.O"]
        self.assertEqual(actual, expected)
