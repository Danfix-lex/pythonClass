import math
def divide_or_square(input):
    float_remainder = input % 5
    integer_remainder = input % 5
    if input % 5 == 0:
        square_root_input = input ** 0.5
        return round((square_root_input), 2)
        
        if input % 5 == 0.5:
            square_root_input = input ** 0.5
            return round((square_root_input), 2)
        else:
            return (float_remainder)
    else:
        return (integer_remainder)
    raise TypeError
