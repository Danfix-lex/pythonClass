numberOne = float(input("Enter first floating number: "))
numberTwo = float(input("Enter second floating number: "))
roundedNumberOne = int(numberOne * 1000)
roundedNumberTwo = int(numberTwo * 1000)
if roundedNumberOne == roundedNumberTwo:
    print("They are the same")
else:
    print("They are different")

