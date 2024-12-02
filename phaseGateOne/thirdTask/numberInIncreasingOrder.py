first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
if first_number < second_number and second_number < third_number:
    print(third_number, second_number, first_number)
elif second_number < third_number and third_number < first_number:
    print(first_number, third_number, second_number)
else:
    print(second_number, first_number, third_number)
