import random
from datetime import datetime

current_time = datetime.now().strftime("%I:%M:%S %p")

name = input("Welcome whats your name? ")

print(f"Welcome Dear {name} this is the current time {(current_time)} you have 30 seconds to answer these questions that will be displayed one after the other below\n")

questions = [
    ("1. 78 - 15 = ", 78 - 15), 
    ("2. 66 - 34 = ", 66 - 34), 
    ("3. 56 - 43 = ", 56 - 43), 
    ("4. 99 - 5 = ", 99 - 5), 
    ("5. 91 - 89 = ", 91 - 89), 
    ("6. 7 - 5 = ", 7 - 5), 
    ("7. 55 - 9 = ", 55 - 9), 
    ("8. 60 - 34 = ", 60 - 34), 
    ("9. 87 - 7 = ", 87 - 7), 
    ("10. 78 - 5 = ", 78 - 5)
]

answered_correctly = 0
answered_incorrectly = 0
failed_answers = []

for _ in range(10):
    random_question, correct_answer = random.choice(questions)
    user_answer = input(random_question)
    
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if user_answer == correct_answer:
            answered_correctly += 1
        else:
            answered_incorrectly += 1
            failed_answers.append((random_question, correct_answer, user_answer))
    else:
        print("Invalid input. Please enter a number.")
        answered_incorrectly += 1
        failed_answers.append((random_question, correct_answer, "N/A"))

print("\nQuiz Results:")
print(f"Answered correctly: {answered_correctly}")
print(f"Answered incorrectly: {answered_incorrectly}")
stop_time = datetime.now().strftime("%I:%M:%S %p")
print(f"Out of the time given to you which was {current_time} you used {stop_time}")
if answered_correctly > answered_incorrectly:
    print(f"Congratulations!!! {name}, you passed your Exam")
else:
    print(f"Am sorry {name} failed this exam You can do better next coming year, please start reading now!!!")

