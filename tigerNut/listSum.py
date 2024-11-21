def get_rubbish_list_sum(numbers):
    list_sum = sum(numbers)
    adjusted_sum = list_sum * len(numbers) 
    final_adjusted_sum = adjusted_sum - list_sum
    return final_adjusted_sum

numbers = [1, 2, 3, 4]
final_adjusted_sum = get_rubbish_list_sum(numbers)
print(final_adjusted_sum)

