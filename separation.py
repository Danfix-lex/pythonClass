Number = int(input("Enter numbers: "))

number_one = (Number//10000)

number_two = (Number%10000)

number_three = (number_two//1000)

number_four = (number_two%1000)

number_five = (number_four//100)

number_six = (number_four%100)

number_seven = (number_six//10)

number_eight = (number_six%10)

print(number_one, number_three, number_five, number_seven, number_eight)
