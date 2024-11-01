numbers = int(input("Input the number of letters you want to print out in diamond shape: "))

for i in range(numbers):
    line = ""
    for j in range(i + 1):
        line += chr(65 + j)
    for j in range(i - 1, -1, -1):
        line += chr(65 + j)
    spaces = " " * (numbers - i - 1)
    print(spaces + line)

for i in range(numbers - 2, -1, -1):
    line = ""
    for j in range(i + 1):
        line += chr(65 + j)
    for j in range(i - 1, -1, -1):
        line += chr(65 + j)
    spaces = " " * (numbers - i - 1)
    print(spaces + line)

