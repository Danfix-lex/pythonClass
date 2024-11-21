def get_vowels_number(message):
    vowels = "AEIOUaeiou"
    result = 0

    for char in message:
        if char in vowels:
            result += 1

    return result

message = "python is sweet"
result = get_vowels_number(message)
print(result)

