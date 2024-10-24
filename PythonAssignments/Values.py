firstNumber = int(input("Enter first integer: "))
secondNumber = int(input("Enter second integer: "))
thirdNumber = int(input("Enter third integer: "))

count = 0

for integer in range(firstNumber, secondNumber + 1):
    if integer % thirdNumber == 0:
        count += 1
print("The range of integer is", count)
        
        
