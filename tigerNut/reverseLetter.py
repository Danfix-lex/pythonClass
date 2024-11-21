def get_palindrome_letter(message):
    reversed_message = message[::-1]
    return reversed_message

message = "hello"
result = get_palindrome_letter(message)
print(result)

