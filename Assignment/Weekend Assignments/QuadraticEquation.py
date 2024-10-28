numberOne = float(input("Input a: "))
numberTwo = float(input("Input b: "))
numberThree = float(input("Input c: "))

calculation = numberTwo * numberTwo - 4 * numberOne * numberThree

if calculation > 0:
    rootOne = (-numberTwo + calculation ** 0.5) / (2 * numberOne)
    rootTwo = (-numberTwo - calculation ** 0.5) / (2 * numberOne)
    print("The roots are: ", rootOne, "and", rootTwo)
elif calculation == 0:
    rootOne = -numberTwo / (2 * numberOne)
    print("The root is: ", rootOne)
else:
    print("The equation has no roots.")

