def calculate_sum(number1, number2):
    if type (number1 and number2) in [float, int]:
        number_product = 0
        if number1 < 0:
            number1 = number1.abs
        for i in range (0, number2):
            number_product = number_product + number1
        return (number_product)
    raise TypeError
