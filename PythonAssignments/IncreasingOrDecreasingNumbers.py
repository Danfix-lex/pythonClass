numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))
numberThree = int(input("Enter the third number: "))

result = "The numbers are neither in increasing nor decreasing order."

if a < b and b < c:
    result = "The numbers are in increasing order."
else if a > b and b > c:
    result = "The numbers are in decreasing order."

print(result)

