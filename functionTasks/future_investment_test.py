from unittest import TestCase
import futureInvestmentFunction

class TestFutureInvestmentFunction(TestCase):
    def test_if_function_exist(self):
        futureInvestmentFunction.get_future_investment(10000, 0.5, 1)
    def test_if_answer_is_correct(self):
        actual = futureInvestmentFunction.get_future_investment(70000, 2, 2)
        expected = 84065.59
        self.assertEqual(actual, expected)
    def test_if_float_and_integer_answer_is_correct(self):
        actual = futureInvestmentFunction.get_future_investment(3000, 3.4, 5)
        expected = 5561.94
        self.assertEqual(actual, expected)

