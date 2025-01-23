school_records = { "class_1":{"students": [ {"name": "Harry", "scores": {"Math": 88, "English": 76}},
                                           {"name": "Solomon", "scores": {"Math": 95, "English": 89}},
                                            ]
                             },
                   "class_2": {"students": [ {"name": "Daniel", "scores": {"Math": 78, "English": 72}},
                                           {"name": "Samuel", "scores": {"Math": 85, "English": 80}},
                                            ]
                               }
                   }
for class_name, class_data in school_records.items():
    print(f"Class: {class_name}")
    for student in class_data["students"]:
        print(f"Student Name: {student['name']}")


total_students_math_score = 0
total_number_of_students = 0

for class_name, class_data in school_records.items():
    for student in class_data["students"]:
        total_students_math_score += student["scores"]["Math"]
        total_number_of_students += 1

average_class_math_score = total_students_math_score / total_number_of_students
print(f"Average Math Score for all class: {average_class_math_score}")