def get_palindrome_letter(message):
    return message == message[::-1]

message = "level"
result = get_palindrome_letter(message)
print(result)

