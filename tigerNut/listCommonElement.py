def get_vowels_number(message):
    vowles = "AEIOUaeiou"
    restult = 0

    i, j = 0, 0

    while i < len(message) and j < len(vowels):
        if message[i] == vowels[j]:
            result += 1
            i += 1
            j += 1
        elif message[i] != vowels[j]:
            i += 1
        else:
            j += 1

    return result

message = "python is sweet"
result = get_vowels_number(message)
print(result)

