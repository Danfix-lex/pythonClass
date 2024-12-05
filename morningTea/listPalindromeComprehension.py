def get_palindrome_letter(message):
    return [word == word [::-1] for word in message]

message = ["madam", "apple", "racecar"]
result = get_palindrome_letter(message)
print(result)


#def get_palindrome_letter(message):
#    return [number for number in range(numbers)]
#
#numbers = "abc123def456"
#result = get_palindrome_letter(message)
#print(result)


def get_numbers_from_letter(word):
    return list(map(lambda x:int(x), filter(lambda x:x.isdigit(), word)))
word = "abc123def456"
result = get_palindrome_letter(word)
print(result)

#def get_palindrome_letter(message):
#    letters = ''.join(char for char in message if char.isdigit())
#    integers = int(letters)
#    return integers 

numbers = "abc123def456"
result = get_palindrome_letter(numbers)
print(result)

#def get_palindrome_letter(message):
#    return evens
#message = ["madam", "apple", "racecar"]
#evens = list(filter(lambda x: x [::-1]  , message)) 
#print(evens)
