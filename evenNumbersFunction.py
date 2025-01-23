def get_even_numbers_from_string(user_input):
    return [int(char) for char in user_input if char.isdigit() and int(char) % 2 == 0]
