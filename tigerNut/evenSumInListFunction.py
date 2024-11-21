def get_even_sum_in_list(numbers):
    even_sum = 0
    for i in numbers:
        if i % 2 == 0:
            even_sum += i
    return even_sum
    raise TypeError
        

numbers = [1, 2, 3, 4, 5]
even_sum = get_even_sum_in_list(numbers)
print(even_sum)

