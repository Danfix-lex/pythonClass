print(f"Welcome to Lagbaja School Student's Grade App")

students = {}
subjects = {}

print("Welcome Teacher, please enter the student numbers (4 students max) or enter -1 to stop:")
for i in range(4):
    student_number = int(input(f"Enter student number for Student {i + 1}: "))
    if student_number == -1:
        break
    students[student_number] = []

print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>\nSaved successfully\n")

print("Welcome Teacher, please enter the subject numbers (4 subjects max) or enter -1 to stop:")
for i in range(4):
    subject_number = int(input(f"Enter subject number for Subject {i + 1}: "))
    if subject_number == -1:
        break
    subjects[subject_number] = []

print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>\nSaved successfully\n")

print("Enter scores for each student:")
for student in students:
    print(f"Entering scores for Student {student}:")
    for subject in subjects:
        score = int(input(f"Enter score for Subject {subject}: "))
        students[student].append(score)

student_totals = {}
student_averages = {}

for student, scores in students.items():
    total = sum(scores)
    average = total / len(scores)
    student_totals[student] = total
    student_averages[student] = average

ranked_students = list(student_totals.items())
for i in range(len(ranked_students)):
    for j in range(i + 1, len(ranked_students)):
        if ranked_students[j][1] > ranked_students[i][1]:
            ranked_students[i], ranked_students[j] = ranked_students[j], ranked_students[i]

student_ranks = {}
rank = 1
for student, _ in ranked_students:
    student_ranks[student] = rank
    rank += 1

print("=" * 120)
print(f"{'STUDENT':<15}{'SUB1':<15}{'SUB2':<15}{'SUB3':<15}{'SUB4':<15}{'TOT':<15}{'AVE':<15}{'POS':<15}")
print("=" * 120)
for student, scores in students.items():
    total = student_totals[student]
    average = student_averages[student]
    position = student_ranks[student]
    print(f"{student:<15}{scores[0]:<15}{scores[1]:<15}{scores[2]:<15}{scores[3]:<15}{total:<15}{average:<15.2f}{position:<15}")
print("=" * 120)


print("\nSUBJECT SUMMARY")
for subject_index, subject in enumerate(subjects):
    total_score = sum(students[student][subject_index] for student in students)
    highest_score = max(students[student][subject_index] for student in students)
    lowest_score = min(students[student][subject_index] for student in students)
    pass_count = sum(1 for student in students if students[student][subject_index] >= 50)
    fail_count = len(students) - pass_count
    average_score = total_score / len(students)

    print(f"\nSubject {subject}")
    print(f"Highest Score for this subject is: {highest_score}")
    print(f"Lowest Score for this subject is: {lowest_score}")
    print(f"Total Score is: {total_score}")
    print(f"Average Score is: {average_score:.2f}")
    print(f"Number of Passes: {pass_count}")
    print(f"Number of Fails: {fail_count}")

class_total_score = sum(student_totals.values())
class_average_score = class_total_score / len(students)
best_student = ranked_students[0][0]
worst_student = ranked_students[-1][0]

print("\n" + "=" * 67)
print("CLASS SUMMARY")
print("=" * 67)
print(f"Best Graduating Student is: Student {best_student} scoring {student_totals[best_student]}")
print(" " * 67)
print("!" * 67)
print(f"Worst Graduating Student is: Student {worst_student} scoring {student_totals[worst_student]}")
print("!" * 67)
print(" " * 67)
print("=" * 67)
print(f"Class Total Score is: {class_total_score}")
print(f"Class Average Score is: {class_average_score:.2f}")
print("=" * 67)
