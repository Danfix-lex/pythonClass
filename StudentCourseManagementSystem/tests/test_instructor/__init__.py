import unittest
from models.instructor import Instructor
from managers.course_manager import CourseManager

class TestInstructor(unittest.TestCase):
    def setUp(self):
        self.instructor = Instructor(1, "dr_smith", "password123")
        self.course_manager = CourseManager()

    def test_create_course(self):
        self.instructor.create_course(101, "Mathematics", 3, self.course_manager)
        self.assertIn(101, self.instructor.taught_courses)

if __name__ == '__main__':
    unittest.main()