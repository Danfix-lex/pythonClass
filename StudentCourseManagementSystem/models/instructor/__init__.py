from models.course import Course
from models.user import User

class Instructor(User):
    def __init__(self, user_id: int, username: str, password: str):
        super().__init__(user_id, username, password, role="instructor")
        self.taught_courses = []  # List of course IDs

    def create_course(self, course_id: int, name: str, credits: int, course_manager):
        course = Course(course_id, name, self.username, credits)
        course_manager.add_course(course)
        self.taught_courses.append(course_id)

    def view_students(self, course_id: int, course_manager):
        return course_manager.get_students_in_course(course_id)

    def grade_student(self, student_id: int, course_id: int, grade: str, course_manager):
        student = course_manager.get_student(student_id)
        if course_id in student.enrolled_courses:
            student.enrolled_courses[course_id] = grade
            return f"Graded {student.username} with {grade} in course {course_id}."
        return "Student not enrolled in this course."

    def __repr__(self):
        return f"Instructor(ID: {self.user_id}, Username: {self.username})"