def lamda_test_practice(x):
    return x + 6
print(lamda_test_practice(3.14))

lamda_test_practice = lambda x : x + 6
print(lamda_test_practice(3.14))

list_cube_practice = lambda i : i * i * i
print(f"The Cube Answer is equal to: {list_cube_practice(5.50)}.")

height = [5.5, 3.4, 8.9, 9.5, 6.5, 55.6, 2, 4, 6, 8, 10, 12, 14]
new_height = list(filter(lambda x : (x % 2 != 0), height))
print(new_height)

age = int(input("Enter Your age to get to know if you are eligible to vote or not: "))
print(f"Your age is {age}.")
eligibility_check = lambda age: print("Congratulation!!! Your are eligible to vote and be voted for.") if (age >= 18) else print("We are so sorry to disclose to you that you are not eligible to vote and be voted for.")
(eligibility_check(age))

message = "Python is a good programming language"
(lambda message : print(message))(message)
