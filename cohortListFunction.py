def get_cohort_and_months(list1, list2):
    student_grades = {}
    for cohort, months in zip(list1, list2):
        student_grades[cohort] = months
    return student_grades
