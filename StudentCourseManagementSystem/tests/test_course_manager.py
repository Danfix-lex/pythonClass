import unittest

from six import assertRaisesRegex

from managers.course_manager import CourseManager, RepeatedCourseCreationException
from models.course import Course
from models.instructor import Instructor
from models.student import Student


# class UsedIdException(Exception):
#     pass


class TestCourseManager(unittest.TestCase):
    my_manager = CourseManager()
    my_student = Student(1, "John", "0000")
    def test_student_can_be_added_to_managers_list(self):
        my_manager = CourseManager()
        my_student = Student(1, "John", "0000")
        my_manager.add_student(my_student)
        self.assertEqual(my_manager.get_size_of_students, 1)

    def test_more_student_can_be_added_to_managers_list(self):
        my_manager = CourseManager()
        my_student = Student(1, "John", "0000")
        my_manager.add_student(my_student)
        self.assertEqual(my_manager.get_size_of_students, 1)

        my_student2 = Student(0, "Stephen", "2020")
        my_manager.add_student(my_student2)
        self.assertEqual(my_manager.get_size_of_students, 2)

    def test_instructor_can_be_added_to_managers_list(self):
        my_manager = CourseManager()
        my_instructor = Instructor(1, "John", "0000")
        my_manager.add_instructor(my_instructor)
        self.assertEqual(my_manager.get_size_of_instructor, 1)

    def test_more_instructor_can_be_added_to_managers_list(self):
        my_manager = CourseManager()
        my_instructor1 = Instructor(1, "John", "0000")
        my_manager.add_instructor(my_instructor1)
        self.assertEqual(my_manager.get_size_of_instructor, 1)

        my_instructor2 = Instructor(2, "Chris", "1212")
        my_manager.add_instructor(my_instructor2)
        self.assertEqual(my_manager.get_size_of_instructor, 2)

    def test_instructor_creates_course(self):
        my_manager = CourseManager()
        my_instructor = Instructor(1, "John", "0000")
        my_manager.add_instructor(my_instructor)
        my_instructor.create_course(1, "Python", 4, my_manager)
        self.assertEqual(my_manager.get_size_of_course, 1)

    def test_manager_display_all_courses(self):
        my_manager = CourseManager()
        my_instructor = Instructor(1, "John", "0000")
        my_manager.add_instructor(my_instructor)
        my_instructor.create_course(1, "Python", 4, my_manager)
        self.assertEqual(my_manager.get_size_of_course, 1)

        my_instructor = Instructor(2, "Moses", "1010")
        my_manager.add_instructor(my_instructor)
        my_instructor.create_course(2, "Java", 4, my_manager)
        self.assertEqual(my_manager.get_size_of_course, 2)

        my_instructor = Instructor(3, "Mark", "2020")
        my_manager.add_instructor(my_instructor)
        my_instructor.create_course(3, "JavaScript", 3, my_manager)
        self.assertEqual(my_manager.get_size_of_course, 3)

    def test_cause_created_more_than_once_raises_exception(self):
        my_manager = CourseManager()
        my_instructor = Instructor(1, "John", "0000")
        my_manager.add_instructor(my_instructor)
        my_instructor.create_course(1, "Python", 4, my_manager)
        self.assertEqual(my_manager.get_size_of_course, 1)

        my_instructor = Instructor(2, "Mark", "1111")
        my_manager.add_instructor(my_instructor)
        with self.assertRaises(RepeatedCourseCreationException):
            my_instructor.create_course(1, "Python", 4, my_manager)











    #
    #
    # # def test_exception_is_raised_for_the_same_id_instructor(self):
    # #     my_course = CourseManager()
    # #     my_instructor = Instructor(1, "John", "0000")
    # #     my_course.add_instructor(my_instructor)
    # #
    # #     my_instructor2 = Instructor(1, "John", "0000")
    # #     with self.assertRaises(UsedIdException):
    # #         my_course.add_instructor(my_instructor2)




