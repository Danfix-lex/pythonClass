import unittest
from models.instructor import Instructor, CourseAlreadyCreatedException
from managers.course_manager import CourseManager
from models.student import Student

class TestInstructor(unittest.TestCase):
    def setUp(self):
        self.instructor = Instructor(1, "dr_smith", "password123")
        self.course_manager = CourseManager()

    def test_create_course(self):
        self.instructor.create_course(101, "Mathematics", 3, self.course_manager)
        self.assertIn(101, self.instructor.taught_courses)

    def test_exception_is_raised_when_course_already_created(self):
        self.instructor = Instructor(1, "dr_smith", "password123")
        self.instructor.create_course(101, "Python", 3, self.course_manager)
        self.assertEqual(self.instructor.get_course_size(), 1)
        with self.assertRaises(CourseAlreadyCreatedException):
            self.instructor.create_course(201, "Java", 4, self.course_manager)


if __name__ == '__main__':
    unittest.main()