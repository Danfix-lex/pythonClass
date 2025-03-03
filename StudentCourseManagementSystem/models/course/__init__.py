class Course:
    def __init__(self, course_id: int, name: str, instructor: str, credits: int):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
        self.credits = credits

    def __repr__(self):
        return f"Course(ID: {self.course_id}, Name: {self.name}, Instructor: {self.instructor})"