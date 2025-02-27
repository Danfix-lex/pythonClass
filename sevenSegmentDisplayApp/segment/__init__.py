class SegmentMapper:
    def map_input_to_digit(self, binary_input):
        digit_mapping = {
            "01100001": 1, "11011011": 2, "11110011": 3,
            "01100111": 4, "10110111": 5, "10111111": 6,
            "11100001": 7, "11111111": 8, "11100111": 9,
            "00000000": 0
        }
        return digit_mapping.get(binary_input, -1)
