print("This is a record and scoring board by ori oke imole group of schools to score the number of schools that sat for their 2024/2025 examination ")
print("Please take note that the average score to pass this examination is 50 and above, and the recommended age to sit for this exam is 18 years old, the expected time to sit for this exam is 8:00am and the minimum number of exams to be written in this examination is 6")
Question = int(input("Enter the nunmber of schools that participated in the exams: "))
Question1 = int(input("Enter the number of students that sat for the exams: "))
Question2 = int(input("Enter the score of students that sat for the exams: "))
Question3 = int(input("Enter the age of students that sat for the exams: "))
Question4 = float(input("Enter the time each students came to sit for the exams: "))
Question5 = int(input("Enter how many exams were done by the school: "))

schools = 0
students = 0
score = 0
age = 0
time_sat_for_exams = 0
number_of_exams = 0

print("Number of Schools: ", Question)
print("Number of Students: ", Question1)
print("Score of Students: ", Question2)
print("Age of Students: ", Question3)
print("Time sat for the exams: ", Question4)
print("Number of Exams done: ", Question5)

if (Question2 >= 50): score+=1

if (Question3 >= 18): age+=1

if (Question4 >= 8): time_sat_for_exams+=1

if (Question5 >= 6): number_of_exams+=1

print("Score: ", score)
print("Age: ", age)
print("Time: ", time_sat_for_exams)
print("Exams: ", number_of_exams)
