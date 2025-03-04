from models.user import User

class Student(User):
    def __init__(self, user_id: int, username: str, password: str):
        super().__init__(user_id, username, password, role="student")
        self.enrolled_courses = {}  # {course_id: grade}

    def enroll_course(self, course_id: int):
        self.enrolled_courses[course_id] = None  # No grade initially

    def view_instructor(self, course_id: int, course_manager):
        course = course_manager.get_course(course_id)
        if course_id in self.enrolled_courses:
            return course.instructor
        return "Not enrolled in this course."

    def view_grades(self):
        return self.enrolled_courses

    def __str__(self):
        return f"(ID: {self.user_id}\n, Username: {self.username})"