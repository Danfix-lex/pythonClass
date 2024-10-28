again = "yes"
while again.lower() == "yes":
    numberOne = int(input("Enter the first number: "))
    numberTwo = int(input("Enter the second number: "))
    sum = numberOne + numberTwo
    print("The sum is:", sum)
    again = input("Do you want to perform another operation? (yes/no): ")

