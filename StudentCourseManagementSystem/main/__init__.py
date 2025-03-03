from managers.course_manager import CourseManager
from models.instructor import Instructor
from models.student import Student


def main():
    course_manager = CourseManager()

    while True:
        print("\nWelcome to the Student Course Management System!")
        print("1. Register as a Student")
        print("2. Register as an Instructor")
        print("3. Login as Student")
        print("4. Login as Instructor")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = int(input("Enter your user ID: "))
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            student = Student(user_id, username, password)
            course_manager.add_student(student)
            print(f"Student {username} registered successfully!")

        elif choice == "2":
            user_id = int(input("Enter your user ID: "))
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            instructor = Instructor(user_id, username, password)
            course_manager.add_instructor(instructor)
            print(f"Instructor {username} registered successfully!")

        elif choice == "3":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            student = next((s for s in course_manager.students if s.username == username), None)
            if student and student.verify_password(password):
                print(f"Welcome, {student.username}!")
                student_menu(student, course_manager)
            else:
                print("Invalid username or password.")

        elif choice == "4":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            instructor = next((i for i in course_manager.instructors if i.username == username), None)
            if instructor and instructor.verify_password(password):
                print(f"Welcome, {instructor.username}!")
                instructor_menu(instructor, course_manager)
            else:
                print("Invalid username or password.")

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def student_menu(student, course_manager):
    while True:
        print("\nStudent Menu")
        print("1. Enroll in a Course")
        print("2. View Instructor of a Course")
        print("3. View Your Grades")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            course_id = int(input("Enter the course ID to enroll: "))
            course = course_manager.get_course(course_id)
            if course:
                course_manager.enroll_student(student.user_id, course_id)
                print(f"Enrolled in course: {course.name}")
            else:
                print("Course not found.")

        elif choice == "2":
            course_id = int(input("Enter the course ID: "))
            instructor = student.view_instructor(course_id, course_manager)
            print(f"Instructor for course {course_id}: {instructor}")

        elif choice == "3":
            grades = student.view_grades()
            print("Your Grades:")
            for course_id, grade in grades.items():
                print(f"Course {course_id}: {grade if grade else 'No grade yet'}")

        elif choice == "4":
            print("Logging out...")
            break

        else:
            print("Invalid choice. Please try again.")


def instructor_menu(instructor, course_manager):
    while True:
        print("\nInstructor Menu")
        print("1. Create a Course")
        print("2. View Students in a Course")
        print("3. Grade a Student")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            course_id = int(input("Enter the course ID: "))
            name = input("Enter the course name: ")
            credits = int(input("Enter the number of credits: "))
            instructor.create_course(course_id, name, credits, course_manager)
            print(f"Course {name} created successfully!")

        elif choice == "2":
            course_id = int(input("Enter the course ID: "))
            students = instructor.view_students(course_id, course_manager)
            print(f"Students in course {course_id}:")
            for student in students:
                print(student)

        elif choice == "3":
            student_id = int(input("Enter the student ID: "))
            course_id = int(input("Enter the course ID: "))
            grade = input("Enter the grade: ")
            result = instructor.grade_student(student_id, course_id, grade, course_manager)
            print(result)

        elif choice == "4":
            print("Logging out...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()