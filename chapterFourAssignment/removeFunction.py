def remove_second_element(numbers: list) -> list:
    num = [0]
    if len(numbers) <= 1:
        return num
    else:
        numbers.pop(1)
        return numbers

number = [2, 4, 5, 6, 7, 8]

print(remove_second_element(number))

