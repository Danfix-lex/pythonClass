first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
if first_number < second_number and second_number < third_number:
    print(third_number, second_number, first_number)
elif second_number < third_number and third_number < first_number:
    print(first_number, third_number, second_number)
else:
    print(second_number, first_number, third_number)
    
    
#write a program that prompts the user to enter three integers and displays them #in increasing order.


#here is a sample run
#enter first number :6
#enter second number: 4
#enter third number: 7
#output 4, 6, 7

#pseudocode
#prompt user to enter first number
#collect it
#store as first number
#prompt user to enter second number
#collect it
#store as second number
#prompt user to enter third number
#collect it
#store as third number
#check if first number if less than second number and second number is less than third number, if true print in this order, third number, second number, first number,
#elif second number is less than third number and third number is less than first number, if true print in this order, first number, third number, second number
#else print in this order, second number, first number, third number
