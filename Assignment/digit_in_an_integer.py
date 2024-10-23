numbers = int(input("Enter an integer between 0 and 1000: "))
numberOne = numbers // 100
numberTwo = numberOne // 1
numberThree = numbers % 10
digits = numberOne + numberTwo + numberThree
print("The digits in an integer: ", digits)
