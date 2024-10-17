Number = int(input("Enter numbers: "))

number_one = (Number%10)

number_two = (Number//10)

number_two = (number_two%10)

number_three = (Number//100)

even_counter = 0
odd_counter = 0

print(number_one, number_two, number_three)

if (number_one % 2 == 0): even_counter+=1
else: odd_counter+=1

if (number_two % 2 == 0): even_counter+=1
else: odd_counter+=1

if (number_three % 2 == 0): even_counter+=1
else: odd_counter+=1

print ("Even: ", even_counter)
print ("Odd: ", odd_counter)
