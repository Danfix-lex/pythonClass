def get_list_even_sum(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count
    
def get_even(even_list):
    return get_list_even_sum([x for x in even_list])
    
i= [1,5,7,3,2,9,8,10]
print(get_even(i))
