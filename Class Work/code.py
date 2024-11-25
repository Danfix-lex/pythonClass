number1: float(input("Enter first number"))
number2: float(input("Enter second number"))
def calculate_sum(number1=6, number2=5):    
    if type (number1 and number2) in [int]:
        number_sum = number1 * number2
        print(number_sum)
        return round((number1 + number1 + number1 + number1 + number1), 1)
    raise TypeError
 
