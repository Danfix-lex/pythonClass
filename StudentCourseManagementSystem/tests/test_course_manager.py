import unittest

from six import assertRaisesRegex

from managers.course_manager import CourseManager
from models.course import Course
from models.instructor import Instructor
from models.student import Student


# class UsedIdException(Exception):
#     pass


class TestCourseManager(unittest.TestCase):
    my_course = CourseManager()
    my_student = Student(1, "John", "0000")
    def test_student_can_be_added_to_managers_list(self):
        my_course = CourseManager()
        my_student = Student(1, "John", "0000")
        my_course.add_student(my_student)
        self.assertEqual(my_course.get_size, 1)

    def test_more_student_can_be_added_to_managers_list(self):
        my_course = CourseManager()
        my_student = Student(1, "John", "0000")
        my_course.add_student(my_student)
        self.assertEqual(my_course.get_size, 1)

        my_student2 = Student(0, "Stephen", "2020")
        my_course.add_student(my_student2)
        self.assertEqual(my_course.get_size, 2)

    def test_instructor_can_be_added_to_managers_list(self):
        my_course = CourseManager()
        my_instructor = Instructor(1, "John", "0000")
        my_course.add_instructor(my_instructor)
        self.assertEqual(my_course.get_size_instructor, 1)

    def test_more_instructor_can_be_added_to_managers_list(self):
        my_course = CourseManager()
        my_instructor1 = Instructor(1, "John", "0000")
        my_course.add_instructor(my_instructor1)
        self.assertEqual(my_course.get_size_instructor, 1)

        my_instructor2 = Instructor(2, "Chris", "1212")
        my_course.add_instructor(my_instructor2)
        self.assertEqual(my_course.get_size_instructor, 2)

    def test_instructor_creates_course(self):
        my_course = CourseManager()
        my_instructor = Instructor(1, "John", "0000")
        my_course.add_instructor(my_instructor)
        my_instructor.create_course(1, "Python", 4, my_course)
        self.assertEqual(my_course.get_size_course, 1)

    # def test_manager_display_all_courses(self):
    #     my_course = CourseManager()
    #     my_instructor = Instructor(1, "John", "0000")
    #     my_course.add_instructor(my_instructor)
    #     my_instructor.create_course(1, "Python", 4, my_course)
    #     my_course.di



    # def test_exception_is_raised_for_the_same_id_instructor(self):
    #     my_course = CourseManager()
    #     my_instructor = Instructor(1, "John", "0000")
    #     my_course.add_instructor(my_instructor)
    #
    #     my_instructor2 = Instructor(1, "John", "0000")
    #     with self.assertRaises(UsedIdException):
    #         my_course.add_instructor(my_instructor2)




