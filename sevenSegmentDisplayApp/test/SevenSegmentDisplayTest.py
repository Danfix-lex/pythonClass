import unittest
from unittest.mock import patch

from sevenSegmentDisplayApp.app import SevenSegmentDisplay


class TestSevenSegmentDisplay(unittest.TestCase):

    def test_valid_input(self):
        display = SevenSegmentDisplay("11001100")
        self.assertTrue(display.is_valid_input())

    def test_invalid_input_length(self):
        display = SevenSegmentDisplay("11001")
        self.assertFalse(display.is_valid_input())

    def test_invalid_input_characters(self):
        display = SevenSegmentDisplay("1100abcd")
        self.assertFalse(display.is_valid_input())

    def test_is_last_digit_zero(self):
        display = SevenSegmentDisplay("11001110")
        self.assertTrue(display.is_last_digit_zero())
        display = SevenSegmentDisplay("11001110")
        self.assertTrue(display.is_last_digit_zero())

    def test_display_invalid_input(self):
        display = SevenSegmentDisplay("1100abcd")
        with patch('builtins.print') as mocked_print:
            display.display()
            mocked_print.assert_called_with("Invalid input! Please enter an 8-digit binary number.")

    def test_display_last_digit_zero(self):
        display = SevenSegmentDisplay("11001110")
        with patch('builtins.print') as mocked_print:
            display.display()
            mocked_print.assert_called_with("Nothing to display (last digit is 0).")

if __name__ == '__main__':
    unittest.main()
