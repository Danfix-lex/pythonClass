def get_running_total_list(numbers):
    result = []
    total = 0
    for number in numbers:
        total += number
        result.append(total)
    return result

