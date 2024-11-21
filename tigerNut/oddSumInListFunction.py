def get_odd_sum_in_list(numbers):
    odd_sum = 0
    for i in numbers:
        if i % 2 != 0:
            odd_sum += i
    return odd_sum
    raise TypeError
        

numbers = [1, 2, 3, 4, 5]
odd_sum = get_odd_sum_in_list(numbers)
print(odd_sum)

