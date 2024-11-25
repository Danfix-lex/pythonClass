number = int(input("Enter number to be printed as triangle: "))
for digit in range(0, number +1):
    for triangle in range(1, digit +1):
        print(f"{triangle}", end = " ")
    print()
for digit in range(1, number + 1):
    for triangle in range(1, number + 1 - digit):
        print(f"{triangle}", end = " ")
    print()
for digit in range(0, number +1):
    for triangle in range(1, digit +1):
        print(f"{triangle}", end = " ")
    print()
