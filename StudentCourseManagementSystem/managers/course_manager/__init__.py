from models.student import Student
from models.instructor import Instructor
from models.course import Course
from models.enrollment import Enrollment

class CourseManager:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []
        self.enrollments = []

    def add_student(self, student: Student):
        self.students.append(student)

    def add_instructor(self, instructor: Instructor):
        self.instructors.append(instructor)

    def add_course(self, course: Course):
        self.courses.append(course)

    def enroll_student(self, student_id: int, course_id: int):
        enrollment = Enrollment(len(self.enrollments) + 1, student_id, course_id)
        self.enrollments.append(enrollment)
        student = self.get_student(student_id)
        student.enroll_course(course_id)
        return enrollment

    def get_student(self, student_id: int):
        for student in self.students:
            if student.user_id == student_id:
                return student
        return None

    def get_course(self, course_id: int):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def get_students_in_course(self, course_id: int):
        students = []
        for enrollment in self.enrollments:
            if enrollment.course_id == course_id:
                student = self.get_student(enrollment.student_id)
                students.append(student)
        return students