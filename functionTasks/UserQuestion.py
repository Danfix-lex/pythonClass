import random
print("Welcome, Kindly answer the questions below to test the level of your intelligence: ")
questions = ["1. 78 + 15 = ", "2. 66 + 34 = ", "3. 56 * 63 = ", "4. 999 - 765 = ", "5. 6 + 89 = ", "6.  677 * 45 = ", "7. 55 + 789 = ", "8. 777 * 34 = ", "9. 654 - 267 = ", "10. 78 + 5550 = "]
for i in questions:
    randomQuestion = random.randint(0, 9)
    print(questions[randomQuestion])

