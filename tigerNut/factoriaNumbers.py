def get_number_factoria(number):
    factoria = 1
    for i in range(1, number+1):
            factoria *= i
    return factoria
    raise TypeError
        

number = 5
factoria = get_number_factoria(number)
print(factoria)

