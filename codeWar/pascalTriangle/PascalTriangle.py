def pascalTriangle(number):
    triangle = []

    for i in range(number):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(1)

        triangle.append(row)

    return triangle

number = 10
result = pascalTriangle(number)
for row in result:
    print(row)