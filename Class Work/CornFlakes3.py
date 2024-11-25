number = int(input("Enter number to be printed: "))
total_rows = number
for rows in range(1, total_rows + 1):
    print(" " * (total_rows - rows), end="")
    for num in range(rows, 0, -1):
        print(num, end="")
    for num in range(2, rows + 1):
        print(num, end="")
    print()

