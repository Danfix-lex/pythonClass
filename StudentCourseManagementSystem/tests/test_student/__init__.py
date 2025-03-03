import unittest
from models.student import Student
from managers.course_manager import CourseManager

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(1, "john_doe", "password123")
        self.course_manager = CourseManager()

    def test_enroll_course(self):
        self.student.enroll_course(101)
        self.assertIn(101, self.student.enrolled_courses)

if __name__ == '__main__':
    unittest.main()