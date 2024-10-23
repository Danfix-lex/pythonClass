numOne = float(input("Enter the first number: "))
numTwo = float(input("Enter the second number: "))
numThree = float(input("Enter the third number: "))

if numOne <= numTwo and numOne <= numThree:
    smallest = numOne
    if numTwo <= numThree:
        middle = numTwo
        largest = numThree
    else:
        middle = numThree
        largest = numTwo
elif numTwo <= numOne and numTwo <= numThree:
    smallest = numTwo
    if numOne <= numThree:
        middle = numOne
        largest = numThree
    else:
        middle = numThree
        largest = numOne
else:
    smallest = numThree
    if numOne <= numTwo:
        middle = numOne
        largest = numTwo
    else:
        middle = numTwo
        largest = numOne

print("The smallest is: ", smallest, "The middle is: ", middle, "The largest is: ", largest)

