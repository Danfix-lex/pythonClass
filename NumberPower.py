numOne = float(input("Enter first number: "))
numTwo = int(input("Enter second number: "))
result = 1
for _ in range(numTwo):
    result *= numOne
print(result)
