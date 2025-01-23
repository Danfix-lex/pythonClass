number = 7

for i in range(1, number + 1):
    shape = ""
    for x in range(i, 0, -1):
        shape += str(x)
    for x in range(2, i + 1):
        shape += str(x)
    print(shape)

for i in range(number - 1, 0, -1):
    shape= ""
    for x in range(i, 0, -1):
        shape += str(x)
    for x in range(2, i + 1):
        shape += str(x)
    print(shape)

