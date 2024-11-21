def get_vowels_number(message):
    letter1, letter2 = message
    result = False

    for char in letter1:
        for dar in letter2:
            if char == dar:
                result = True

    return result

message = "listen", "silent"
result = get_vowels_number(message)
print(result)

