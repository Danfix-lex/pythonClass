number = int(input("Enter a three-digit number: "))
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")
