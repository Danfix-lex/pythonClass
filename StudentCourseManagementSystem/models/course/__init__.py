class Course:
    def __init__(self, course_id: int, name: str, instructor: str, credits: int):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
        self.credits = credits

    def __str__(self):
        return f"(ID: {self.course_id}\n, Name: {self.name}\n, Instructor: {self.instructor})"