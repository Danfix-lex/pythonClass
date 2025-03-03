from unittest import TestCase
from classWorkCurrent.functions import CharacterFrequency
from classWorkCurrent.functions import SeperatedStrings
from classWorkCurrent.functions import MixCaseParameter
from classWorkCurrent.functions import TupleCharacter
from classWorkCurrent.functions import RemoveSpecialCharacter
from classWorkCurrent.functions import AddLettersToWord


class CharacterFrequencyTest(TestCase):
    def test_if_function_exist(self):
        CharacterFrequency.calculate_letters_frequency_and_appearance("semicolon.africa")

    def test_output_of_characters_to_be_a_dictionary(self):
        actual = CharacterFrequency.calculate_letters_frequency_and_appearance("semicolon.africa")
        expected = {"s": 1, "e": 1, "m": 1, "i": 2, "c": 2, "o": 2, "l": 1, "n": 1, ".": 1, "a": 2, "f": 1, "r": 1}
        self.assertEqual(actual, expected)

    def test_out_of_character_if_it_is_a_lower_or_upper_case(self):
        actual = CharacterFrequency.calculate_letters_frequency_and_appearance("Jesus is Lord")
        expected = {'J': 1, 'e': 1, 's': 3, 'u': 1, ' ': 2, 'i': 1, 'L': 1, 'o': 1, 'r': 1, 'd': 1}
        self.assertEqual(actual, expected)

    def test_if_letters_and_symbols_can_be_in_a_dictionary(self):
        actual = CharacterFrequency.calculate_letters_frequency_and_appearance("-mummy/?")
        expected = {'-': 1, 'm': 3, 'u': 1, 'y': 1, '/': 1, '?': 1}
        self.assertEqual(actual, expected)

    def test_if_letters_numbers_symbols_can_be_in_a_dictionary(self):
        actual = CharacterFrequency.calculate_letters_frequency_and_appearance("-DaddyaNdmummy12346/?")
        expected = {'-': 1, '/': 1, '1': 1, '2': 1, '3': 1, '4': 1, '6': 1, '?': 1, 'D': 1, 'N': 1, 'a': 2, 'd': 3, 'm': 3, 'u': 1, 'y': 2}
        self.assertEqual(actual, expected)

    def test_output_of_characters_to_be_not_splited(self):
        actual = SeperatedStrings.join_seperated_words_together("abc", "xyz")
        expected = "xyc abz"
        self.assertEqual(actual, expected)

    def test_output_of_characters_with_symbols_to_be_splited(self):
        actual = SeperatedStrings.join_seperated_words_together("bc/", "?xz")
        expected = "?x/ bcz"
        self.assertEqual(actual, expected)

    def test_mix_case_of_letters(self):
        actual = MixCaseParameter.join_mix_case_letters("sEmIColOn")
        expected = "EICOsmoln"
        self.assertEqual(actual, expected)

    def test_mix_case_of_letters_and_symbols(self):
        actual = MixCaseParameter.join_mix_case_letters("-mummyANDdaddy/?")
        expected = "ANDmummydaddy-/?"
        self.assertEqual(actual, expected)

    def test_if_numbers_and_letters_and_symbols(self):
        actual = MixCaseParameter.join_mix_case_letters("0123456789ANDuouwillBeminE?><")
        expected = "ANDBEuouwillemin0123456789?><"
        self.assertEqual(actual, expected)

    def test_if_tuple_character_is_correct(self):
        actual = TupleCharacter.get_tuple_character_from_input("semicolon", "o")
        expected = ("o", 2)
        self.assertEqual(actual, expected)

    def test_if_tuple_sentence_is_correct(self):
        actual = TupleCharacter.get_tuple_character_from_input("Daddy", "d")
        expected = ("d", 2)
        self.assertEqual(actual, expected)

    def test_if_character_in_word_are_removed(self):
        actual = RemoveSpecialCharacter.get_special_characters_away("he,ll.o")
        expected = "hello"
        self.assertEqual(actual, expected)

    def test_is_numbers_and_special_characters_are_removed(self):
        actual = RemoveSpecialCharacter.get_special_characters_away("1234he>l?lo?")
        expected = "hello"
        self.assertEqual(actual, expected)

    def test_if_letters_inside_word_is_correct(self):
        actual = AddLettersToWord.get_letters_inside_word("helloo", "ce")
        expected = "helceloo"
        self.assertEqual(actual, expected)