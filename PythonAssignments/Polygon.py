number = int(input("Enter the number: "))
length = int(input("Enter the length: "))

calculation1 = number * length

tan = 0.414
calculation2 = length / (2 * tan)

area = (1/2) * calculation1 * calculation2

print("The area of the polygon with", number, "sides each of length", length, "is:", area)

