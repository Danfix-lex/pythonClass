import random

print("Welcome, Kindly answer the questions below to test the level of your intelligence: ")

questions = [
    ("1. 78 + 15 = ", 78 + 15), 
    ("2. 66 + 34 = ", 66 + 34), 
    ("3. 56 * 63 = ", 56 * 63), 
    ("4. 999 - 765 = ", 999 - 765), 
    ("5. 6 + 89 = ", 6 + 89), 
    ("6. 677 * 45 = ", 677 * 45), 
    ("7. 55 + 789 = ", 55 + 789), 
    ("8. 777 * 34 = ", 777 * 34), 
    ("9. 654 - 267 = ", 654 - 267), 
    ("10. 78 + 5550 = ", 78 + 5550)
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

if answered_incorrectly > 0:
    print("\nIncorrect answers:")
    for question, correct, user in failed_answers:
        print(f"{question} Your answer: {user}. Correct answer: {correct}")

