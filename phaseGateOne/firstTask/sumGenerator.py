import random

print("Welcome, Kindly answer the questions below to test the level of your intelligence: ")

questions = [
    ("1. 78 + 15 = ", 78 + 15), 
    ("2. 66 + 34 = ", 66 + 34), 
    ("3. 56 + 63 = ", 56 + 63), 
    ("4. 9 + 75 = ", 9 + 75), 
    ("5. 6 + 89 = ", 6 + 89), 
    ("6. 77 + 45 = ", 77 + 45), 
    ("7. 55 + 7 = ", 55 + 7), 
    ("8. 77 + 34 = ", 7 + 34), 
    ("9. 65 + 27 = ", 65 + 27), 
    ("10. 78 + 50 = ", 78 + 50)
]

right_answer = True
wrong_answer = False

for _ in range(10):
    random_question, correct_answer = random.choice(questions)
    user_answer = input(random_question)
    
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if user_answer == correct_answer:
            print(right_answer)
            break
        else:
            print(wrong_answer)
            break
    else:
        print("Invalid input. Please enter a number.")
        answered_incorrectly += 1
        failed_answers.append((random_question, correct_answer, "N/A"))
        
#write a program that generates two integers under 100 and prompts the user to enter the sum of these two integers. the program then reports true if the answer is correct, false otherwise.

#pseudocode
#create a questions in a list
#loop inside each questions and prompt the user to enter its answer
#check if answer is equals to the right answer, if true print true
#else print false
