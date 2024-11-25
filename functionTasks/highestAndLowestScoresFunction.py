students_data = []

student_names = [
    "Hamid", "Edwin", "Samuel", "Ifeayin", "Divine",
    "Oyinyechi", "Emmanuel", "Christopher", "Ogene", "Dozie"
]

for name in student_names:
    print(f"Enter scores for {name}:")
    scores = []
    for i in range(4):
        while True:
            try:
                score = int(input(f"Enter score {i+1} (1 to 100): "))
                if 1 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Invalid input! Please enter a score between 1 and 100.")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
    students_data.append([name, scores])

subjects = ["C#", "Python", "Java", "Java Script"]

print("\nStudent Scores:")
print(f"{'Name':<15}{'C#':<10}{'Python':<10}{'Java':<10}{'Java Script':<10}")
print("=" * 55)

for student in students_data:
    name = student[0]
    marks = student[1]
    print(f"{name:<15}{marks[0]:<10}{marks[1]:<10}{marks[2]:<10}{marks[3]:<10}")

print("\nHighest and Lowest Scores in Each Subject:")
print("=" * 40)

def get_highest_and_lowest_students_scores(students_data, subjects):
    for subject_index in range(len(subjects)):
        highest_index = 0
        lowest_index = 0

        for student_index in range(1, len(students_data)):
            if students_data[student_index][1][subject_index] > students_data[highest_index][1][subject_index]:
                highest_index = student_index
            if students_data[student_index][1][subject_index] < students_data[lowest_index][1][subject_index]:
                lowest_index = student_index

        print(f"Subject: {subjects[subject_index]}")
        print(f"  Highest: {students_data[highest_index][0]} with score {students_data[highest_index][1][subject_index]}")
        print(f"  Lowest: {students_data[lowest_index][0]} with score {students_data[lowest_index][1][subject_index]}")
        print()

get_highest_and_lowest_students_scores(students_data, subjects)

