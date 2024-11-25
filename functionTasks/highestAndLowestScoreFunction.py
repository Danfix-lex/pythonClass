def get_highest_and_lowest_student(students, marks, min_score):
    
    highest_students = []
    lowest_students = []
    
    num_subjects = len(marks[0])
    
    for subject_index in range(num_subjects):
        best_student_index = -1
        worst_student_index = -1
        
        for student_index in range(len(marks)):
            if marks[student_index][subject_index] < min_score:
                continue
                
            if best_student_index == -1 or marks[student_index][subject_index] > marks[best_student_index][subject_index]:
                best_student_index = student_index
                
            if worst_student_index == -1 or marks[student_index][subject_index] < marks[worst_student_index][subject_index]:
                worst_student_index = student_index
                
        if best_student_index != -1:
            best_students.append(students[best_student_index])
        else:
            best_students.append("No eligible students")
        
        if worst_student_index != -1:
            worst_students.append(students[worst_student_index])
        else:
            worst_students.append("No eligible students")
    
    return best_students, worst_students
