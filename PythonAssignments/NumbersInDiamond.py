numbers = 7

for i in range(1, numbers + 1):
    line = ""
    for j in range(i, 0, -1):
        line += str(j)
    for j in range(2, i + 1):
        line += str(j)
    spaces = " " * (numbers - i)
    print(spaces + line)

for i in range(numbers - 1, 0, -1):
    line = ""
    for j in range(i, 0, -1):
        line += str(j)
    for j in range(2, i + 1):
        line += str(j)
    spaces = " " * (numbers - i)
    print(spaces + line)
