def get_list_average(numbers):
    list_numbers = len(numbers)
    for i in numbers:
        list_sum = sum(numbers)
        average = list_sum / list_numbers
        return average
    raise TypeError
        

numbers = [10, 20, 30, 40]
average = get_list_average(numbers)
print(average)
