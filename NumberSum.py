while True:
    numOne = float(input("Enter first number: "))
    numTwo = float(input("Enter second number: "))
    total = numOne + numTwo
    print("The sum is:", total)

    again = input("Do you want to perform the operation again? (yes/no): ")
    if again.lower() != "yes":
        break
