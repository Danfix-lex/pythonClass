def get_students_score_grade(student_scores):
    student_grades = {}

    for student, score in student_scores.items():
        if 0 >= score <= 70:
            grade = "Fail"
        elif 71 >= score <= 80:
            grade = "Acceptable"
        elif 81 >= score <= 90:
            grade = "Exceeds Expectations"
        elif 91 >= score <= 100:
            grade = "Outstanding"
        else:
            grade = "Invalid Score"
        student_grades[student] = grade

    return student_grades
