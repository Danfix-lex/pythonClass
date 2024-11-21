def get_number_duplicates(numbers):
    return len(numbers) != len(set(numbers))

numbers = [1, 2, 3, 4, 5, 2]
result = get_number_duplicates(numbers)
print(result)

