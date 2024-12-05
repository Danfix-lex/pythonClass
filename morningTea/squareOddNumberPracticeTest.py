from unittest import TestCase
import squareOddNumber

class TestPrimeInListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = squareOddNumber.get_number_plus_list ([1, 2, 3])
        expected = [2, 4, 6]
        self.assertEqual(actual, expected)
class TestWordsLengthWithNumber(TestCase):
    def test_if_function_is_correct(self):
        actual = squareOddNumber.get_words_length_with_number(["Apple", "Fish", "Orange", "Ice", "Lime"], 5)
        expected = ["Apple", "Orange"]
        self.assertEqual(actual, expected)
class TestTotalWholeNumber(TestCase):
    def test_if_function_is_correct(self):
        actual = squareOddNumber.get_total_whole_number(192374)
        expected = 26
        self.assertEqual(actual, expected)
class TestVowelLetterRemover(TestCase):
    def test_if_function_is_correct(self):
        actual = squareOddNumber.get_all_vowel_letters_out_of_words(["Apple", "Fish", "Orange", "Ice", "Lime"])
        expected = ["ppl", "Fsh", "rng", "c", "Lm"]
        self.assertEqual(actual, expected)
