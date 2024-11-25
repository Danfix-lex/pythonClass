def squares(numbers):

    square = int(input("Enter your number: "))
    
    exponent = int(input("Enter your exponent: "))

    number_square = square ** exponent

    if number_square > 10000:
        print("its a large number square")
        else:
            print("its a small number square")
