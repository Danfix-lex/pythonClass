number = int(input("Enter number to be printed in asteriks: "))
count = 0
for number in range(number, 0, -1):
    if count != number:
        number - number
        print(f"{count - number}")
        count += 1
print()
