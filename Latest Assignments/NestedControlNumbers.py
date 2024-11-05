numbers = int(input("Enter number: "))
largest = numbers
for numbers in range(1, 11):
    number = int(input("Enter number: "))
    if number > largest:
        largest = number
        print(largest)
    else:
        print(largest)
