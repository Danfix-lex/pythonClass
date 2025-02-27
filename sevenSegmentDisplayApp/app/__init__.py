import re
from sevenSegmentDisplayApp.display import SegmentRenderer
from sevenSegmentDisplayApp.segment import SegmentMapper

class SevenSegmentDisplay:
    def __init__(self, binary_input=None):
        if binary_input is None:
            self.binary_input = self.collect_input()
        else:
            self.binary_input = binary_input
        self.segment_mapper = SegmentMapper()
        self.segment_renderer = SegmentRenderer()

    def collect_input(self):
        binary_input = input("Enter an 8-digit binary number: ")
        while not self.is_valid_input(binary_input):
            print("Invalid input! Please enter an 8-digit binary number.")
            binary_input = input("Enter an 8-digit binary number: ")
        return binary_input

    def is_valid_input(self):
        return len(self.binary_input) == 8 and re.fullmatch(r"[01]+", self.binary_input)

    def is_last_digit_zero(self):
        return self.binary_input[-1] == '0'

    def display(self):
        if not self.is_valid_input():
            print("Invalid input! Please enter an 8-digit binary number.")
            return

        if self.is_last_digit_zero():
            print("Nothing to display (last digit is 0).")
            return

        digit = self.segment_mapper.map_input_to_digit(self.binary_input)
        if digit == -1:
            print("No matching digit for the input.")
            return

        self.segment_renderer.render(digit)
