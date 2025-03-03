class Enrollment:
    def __init__(self, enrollment_id: int, student_id: int, course_id: int):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id

    def __repr__(self):
        return f"Enrollment(ID: {self.enrollment_id}, Student: {self.student_id}, Course: {self.course_id})"