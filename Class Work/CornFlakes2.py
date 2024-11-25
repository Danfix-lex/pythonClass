multiplication = 1
numbers = int(input("Enter number to be multiplied: "))
for i in range(1):
    for multiplication in range(1, 13):
        print(f"{numbers} * {multiplication} = {numbers * multiplication}", end="  ")
        print()
