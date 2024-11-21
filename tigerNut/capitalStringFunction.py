def get_capital_string_first_letter(strings):
    capitalized_list = []
    for string in strings:
        capitalized_list.append(string.capitalize())
    return capitalized_list

words = ["apple", "banana", "cherry"]
result = get_capital_string_first_letter(words)
print(result)

