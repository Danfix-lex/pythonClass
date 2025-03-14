from models.student import Student
from models.instructor import Instructor
from models.course import Course
from models.enrollment import Enrollment


class RepeatedCourseCreationException(Exception):
    pass


class CourseManager:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []
        self.enrollments = []
        self.load_from_file()

    def add_student(self, student: Student):
        self.students.append(student)
        self.save_to_file()

    def add_instructor(self, instructor: Instructor):
        self.instructors.append(instructor)
        self.save_to_file()

    def add_course(self, course: Course):
        for existing_course in self.courses:
            if existing_course.course_id == course.course_id:
                raise RepeatedCourseCreationException("Course already exists!")
        self.courses.append(course)
        self.save_to_file()

    def enroll_student(self, student_id: int, course_id: int):
        enrollment = Enrollment(len(self.enrollments) + 1, student_id, course_id)
        self.enrollments.append(enrollment)
        student = self.get_student(student_id)
        student.enroll_course(course_id)
        self.save_to_file()
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

    @property
    def get_size_of_students(self):
        return len(self.students)

    @property
    def get_size_of_instructor(self):
        return len(self.instructors)

    @property
    def get_size_of_course(self):
        return len(self.courses)

    def display_all_course(self):
        for course in self.courses:
            print(course)

    def save_to_file(self):
        with open('data.txt', 'w') as f:
            f.write('Students:\n')
            for student in self.students:
                f.write(f"{student.user_id},{student.username},{student.password.decode('utf-8')}\n")
            f.write('Instructors:\n')
            for instructor in self.instructors:
                f.write(f"{instructor.user_id},{instructor.username},{instructor.password.decode('utf-8')}\n")

    def load_from_file(self):
        try:
            with open('data.txt', 'r') as f:
                section = None
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line == 'Students:':
                        section = 'students'
                    elif line == 'Instructors:':
                        section = 'instructors'
                    elif line == 'Courses:':
                        section = 'courses'
                    elif line == 'Enrollments:':
                        section = 'enrollments'
                    elif section == 'students' and line:
                        try:
                            user_id, username, password_hash = line.split(',')
                            password_hash = password_hash.encode('utf-8')
                            self.students.append(Student(int(user_id), username, password_hash))
                        except ValueError:
                            print(f"Error reading student data: {line}")
                    elif section == 'instructors' and line:
                        try:
                            user_id, username, password_hash = line.split(',')
                            password_hash = password_hash.encode('utf-8')
                            self.instructors.append(Instructor(int(user_id), username, password_hash))
                        except ValueError:
                            print(f"Error reading instructor data: {line}")
                    elif section == 'courses' and line:
                        try:
                            course_id, name, instructor_id = line.split(',')
                            self.courses.append(Course(int(course_id), name, int(instructor_id)))
                        except ValueError:
                            print(f"Error reading course data: {line}")
                    elif section == 'enrollments' and line:
                        try:
                            enrollment_id, student_id, course_id = line.split(',')
                            self.enrollments.append(Enrollment(int(enrollment_id), int(student_id), int(course_id)))
                        except ValueError:
                            print(f"Error reading enrollment data: {line}")
        except FileNotFoundError:
            print("No previous data found, starting fresh.")
        except ValueError as e:
            print(f"Error reading data from file: {e}")