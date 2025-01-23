def generate_number_square_dictionary(user_input):
    return [{i: user_input ** i} for i in range(1, user_input + 1)]
