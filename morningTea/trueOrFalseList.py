def get_list_true_or_false(numbers):
    count = []
    for number in numbers:
        if number % 2 == 0:
            count.append(True) 
        else: count.append(False)
    return count  

def get_true_or_false(even_or_false):
    return get_list_true_or_false([m for m in even_or_false])

i = [1, 5, 7, 3, 2, 9, 8, 10]
print(get_true_or_false(i))
