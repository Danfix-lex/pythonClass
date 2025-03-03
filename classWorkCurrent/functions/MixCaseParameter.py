def join_mix_case_letters(letters):
    mix_numbers_and_symbols = ""
    mix_upper_case_letters = ""
    mix_lower_case_letters = ""
    for letter in letters:
        if letter.isupper():
            mix_upper_case_letters += letter
        elif letter.islower():
            mix_lower_case_letters += letter
        else:
            mix_numbers_and_symbols += letter
    return mix_upper_case_letters + mix_lower_case_letters + mix_numbers_and_symbols