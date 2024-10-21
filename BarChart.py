for _ in range(5):
    num = int(input("Enter a number between 1 and 30: "))
    while num < 1 or num > 30:
        num = int(input("Invalid input. Enter a number between 1 and 30: "))
    print('*' * num)
