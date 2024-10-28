x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
p = int(input("Enter third number: "))
first = (x + p - 1) // p * p
second = y // p * p
third = (first - second) // p + 1
print(third)

