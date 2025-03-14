def getNumbersInDictionaryOrder(numbers):
    tempoary_numbers = {}
    
    if not numbers:
        return {}
    
    for i in numbers:
        if i in tempoary_numbers:
            tempoary_numbers[i] += 1
        else:
            tempoary_numbers[i] = 1
    sorted_numbers = dict(sorted(tempoary_numbers.items()
    return sorted_numbers

numbers = [2, 2, 1, 3, 5, 5]
result = getNumbersInDictionaryOrder(numbers)
print(result)

for key, values in result.items():
    print({f"{key}:{values}"})


