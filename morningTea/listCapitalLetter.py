def get_capital_string_first_letter(strings):
    capitalized_list = []
    for string in strings:
        capitalized_list.append(string.capitalize())
    return capitalized_list

def capital_letter(first_letter_capital):
    return get_capital_string_first_letter ([i for i in first_letter_capital])
    
words = ["red", "orange", "yellow", "green", "blue"]
print(capital_letter(words))

