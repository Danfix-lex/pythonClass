from unittest import TestCase
import trueOrFalseList

class TestPrimeInListFunction(TestCase):
    def test_if_function_is_correct(self):
        actual = trueOrFalseList.get_true_or_false([1,2,3,4,5])
        expected = [False, True, False, True, False]
        self.assertEqual(actual, expected)
