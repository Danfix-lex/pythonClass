def divide_or_square(input)
    remainder = input % 5
    if input % 5 == 0:
        square_root_input = math.root(input)
        return (square_root_input)
    else
        return (remainder)
    raise TypeError
