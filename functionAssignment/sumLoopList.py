def get_sum_for_loop(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def get_sum_for_while_loop(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total

def get_sum_for_do_while_loop(numbers):
    total = 0
    i = 0
    while True:
        total += numbers[i]
        i += 1
        if i >= len(numbers):
            break
    return total

